"""Read-only consistency checks for a completed research snapshot."""
import csv
import logging
from src.common.config import arguments, load_game
from src.common.io import read_json, read_jsonl, sha256
from src.common.logging import run_cli
from src.processors.clean_reviews import normalize, samples
from src.processors.deduplicate import deduplicate
from src.processors.statistics import calculate


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify(game, data_dir):
    raw = data_dir / 'raw' / game['key']
    processed = data_dir / 'processed' / game['key']
    manifest = read_json(raw / 'reviews_manifest.json')
    require(manifest['completed'], 'Incomplete collection')
    require(sha256(raw / 'steam_reviews.jsonl') == manifest['raw_sha256'], 'Raw checksum mismatch')
    page_rows = []
    for name, checksum in manifest['page_sha256'].items():
        path = raw / 'review_pages' / name
        require(sha256(path) == checksum, f'Page checksum mismatch: {name}')
        page_rows.extend(read_json(path)['response']['response']['reviews'])
    source = read_jsonl(raw / 'steam_reviews.jsonl')
    require(source == page_rows, 'Raw JSONL differs from archived API pages')
    require(len(source) == manifest['raw_reviews'], 'Raw count mismatch')
    require(all(r['language'] == 'english' for r in source), 'Non-English review')
    expected, _ = deduplicate([normalize(r, game) for r in source])
    rows = read_jsonl(processed / 'reviews.jsonl')
    require(rows == expected, 'Processed rows differ from raw normalization')
    require(len({r['review_id'] for r in rows}) == len(rows), 'Duplicate processed IDs')
    info = read_json(processed / 'processing.json')
    require(sha256(processed / 'reviews.jsonl') == info['processed_sha256'], 'Processed checksum mismatch')
    require(read_json(processed / 'statistics.json') == calculate(rows, len(source)), 'Statistics mismatch')
    def check_csv(path, expected_rows):
        with path.open(encoding='utf-8', newline='') as handle:
            actual = list(csv.DictReader(handle))
        expected_csv = [{k: '' if v is None else str(v) for k, v in row.items()} for row in expected_rows]
        require(actual == expected_csv, f'CSV mismatch: {path.name}')
    check_csv(processed / 'reviews.csv', rows)
    for name, subset in samples(rows, game['sample_size']).items():
        check_csv(processed / 'samples' / (name + '.csv'), subset)
    report = data_dir / 'reports' / game['key'] / 'summary.md'
    require(report.exists() and report.stat().st_size > 0, 'Missing report')
    logging.info('Verified %s raw reviews, %s unique reviews, page hashes, text, CSVs, samples and statistics',
                 len(source), len(rows))


def main():
    args = arguments('Verify snapshot integrity without network access').parse_args()
    verify(load_game(args.game, args.config), args.data_dir)


if __name__ == '__main__':
    run_cli(main)
