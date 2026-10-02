import json
import logging
import time
from datetime import datetime, timezone
from src.common.config import arguments, load_game
from src.common.http import get_json
from src.common.io import read_json, write_json, write_jsonl, sha256
from src.common.logging import run_cli

ENDPOINT = 'https://api.steampowered.com/IUserReviewsService/GetAppReviews/v1/'


def validate(payload):
    body = payload.get('response')
    if not isinstance(body, dict):
        raise ValueError('Review response missing response object')

    reviews = body.get('reviews')
    if reviews is None:
        summary = body.get('query_summary')
        if isinstance(summary, dict) and summary.get('num_reviews') == 0:
            return
        raise ValueError('Review response missing reviews list')

    if not isinstance(reviews, list):
        raise ValueError('Review response reviews field is not a list')

    for row in reviews:
        if not isinstance(row, dict) or not row.get('recommendationid') or row.get('language') != 'english':
            raise ValueError('Invalid review identifier or non-English review')
    if reviews and not body.get('cursor'):
        raise ValueError('Non-empty page missing cursor')


def collect(game, data_dir, fetch=get_json, sleep=time.sleep):
    raw = data_dir / 'raw' / game['key']
    pages = raw / 'review_pages'
    pages.mkdir(parents=True, exist_ok=True)
    manifest_path = raw / 'reviews_manifest.json'
    output = raw / 'steam_reviews.jsonl'
    if manifest_path.exists():
        manifest = read_json(manifest_path)
        if manifest['params']['appid'] != game['steam_app_id'] or not manifest.get('completed'):
            raise ValueError('Completed snapshot does not match configured app')
        if sha256(output) != manifest['raw_sha256']:
            raise ValueError('Raw review checksum mismatch')
        logging.info('Using completed snapshot: %s raw reviews', manifest['raw_reviews'])
        return manifest
    base = {'appid': game['steam_app_id'], 'languages': ['english'], 'filter': 1,
            'review_type': 0, 'purchase_type': 1, 'num_per_page': 100,
            'filter_offtopic_activity': False}
    cursor, rows, seen_cursors = '*', [], set()
    index, first_summary, first_matching = 0, None, None
    while True:
        params = {**base, 'cursor': cursor}
        path = pages / f'{index:06d}.json'
        if path.exists():
            page = read_json(path)
            if page['params'] != params or page['endpoint'] != ENDPOINT:
                raise ValueError(f'Cached page query mismatch: {path}')
            validate(page['response'])
        else:
            sleep(game['request_delay_seconds'])
            payload = fetch(ENDPOINT, {'input_json': json.dumps(params)}, validate)
            page = {'endpoint': ENDPOINT, 'params': params,
                    'collected_at': datetime.now(timezone.utc).isoformat(), 'response': payload}
            write_json(path, page, immutable=True)
        body = page['response']['response']
        if index == 0:
            first_summary = body.get('query_summary')
            first_matching = body.get('total_matching')
            started = page['collected_at']
        batch = body.get('reviews', [])
        rows.extend(batch)
        logging.info('Page %s: %s reviews; total %s', index + 1, len(batch), len(rows))
        index += 1
        if not batch:
            break
        next_cursor = body['cursor']
        if next_cursor == cursor or next_cursor in seen_cursors:
            raise ValueError('Pagination cursor repeated before an empty page; collection incomplete')
        seen_cursors.add(cursor)
        cursor = next_cursor
    write_jsonl(output, rows, immutable=True)
    manifest = {'endpoint': ENDPOINT, 'params': base, 'started_at': started,
                'finished_at': page['collected_at'], 'completed': True, 'termination': 'empty_page',
                'pages': index, 'raw_reviews': len(rows), 'query_summary': first_summary,
                'total_matching_first_page': first_matching, 'raw_sha256': sha256(output),
                'page_sha256': {p.name: sha256(p) for p in sorted(pages.glob('*.json'))}}
    write_json(manifest_path, manifest, immutable=True)
    logging.info('Raw reviews collected: %s; API first-page total: %s', len(rows), first_matching)
    if first_matching is not None and len({r['recommendationid'] for r in rows}) != first_matching:
        logging.warning('Unique collected count differs from API first-page total; see manifest')
    return manifest


def main():
    args = arguments('Collect English Steam reviews').parse_args()
    collect(load_game(args.game, args.config), args.data_dir)


if __name__ == '__main__':
    run_cli(main)
