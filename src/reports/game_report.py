import html
import json
from src.common.config import arguments, load_game
from src.common.io import read_json, read_jsonl, write_text
from src.common.logging import run_cli
from src.processors.clean_reviews import samples
from src.processors.statistics import generate as statistics


def display(value):
    if value is None:
        return 'unknown'
    if isinstance(value, float):
        return f'{value:.4f}'
    return html.escape(str(value)).replace('|', '&#124;').replace('\n', ' ')


def generate(game, data_dir):
    target = data_dir / 'processed' / game['key']
    stats = statistics(game, data_dir)
    metadata = read_json(target / 'metadata.json')
    manifest = read_json(data_dir / 'raw' / game['key'] / 'reviews_manifest.json')
    rows = read_jsonl(target / 'reviews.jsonl')
    lines = [f"# {game['name']} Research Dataset Summary", '', '## Steam Metadata', '']
    lines += [f'- {key}: {display(value)}' for key, value in metadata.items()]
    sections = {
        'Dataset Size': ['raw_reviews', 'total_reviews', 'unique_reviews', 'duplicates_removed'],
        'Sentiment': ['positive_reviews', 'negative_reviews', 'unknown_sentiment_reviews', 'positive_ratio', 'negative_ratio'],
        'Playtime': ['playtime_unit', 'known_playtime_reviews', 'average_playtime_at_review', 'median_playtime_at_review'],
        'Review Quality': ['empty_reviews', 'very_short_reviews'],
        'Positive vs Negative Review Statistics': ['average_playtime_positive', 'average_playtime_negative',
                                                   'average_votes_up_positive', 'average_votes_up_negative']}
    for title, fields in sections.items():
        lines += ['', '## ' + title, ''] + [f'- {key}: {display(stats[key])}' for key in fields]
        if title == 'Dataset Size':
            lines += [f"- Collection: {manifest['started_at']} to {manifest['finished_at']}",
                      f"- Termination: {manifest['termination']}; pages: {manifest['pages']}",
                      f"- API first-page total_matching: {manifest['total_matching_first_page']}",
                      f"- API first-page query_summary: {display(json.dumps(manifest['query_summary']))}",
                      '- Pagination exhausted the public query; a live API is not an atomic snapshot and may change during collection.']
            matching = manifest['total_matching_first_page']
            if matching is not None:
                lines.append(f"- Unique collected minus first-page API total: {stats['unique_reviews'] - matching}")
    lines += ['', '## Playtime Segments', '', '| Segment | Reviews | Positive ratio |', '|---|---:|---:|']
    for label, count in stats['review_count_by_playtime_segment'].items():
        lines.append(f"| {label} | {count} | {display(stats['positive_ratio_by_playtime_segment'][label])} |")
    selected = samples(rows, 20)
    for title, prefix in [('Most Helpful Review Samples', 'helpful'), ('Recent Review Samples', 'recent')]:
        lines += ['', '## ' + title, '']
        for sentiment in ('positive', 'negative'):
            lines += [f'### {sentiment.title()} (up to 20)', '',
                      '| Review ID | Created UTC | Votes up | Hours at review |', '|---|---|---:|---:|']
            for row in selected[prefix + '_' + sentiment]:
                lines.append('| ' + ' | '.join(display(row[k]) for k in (
                    'review_id', 'created_at', 'votes_up', 'playtime_at_review_hours')) + ' |')
            lines += ['', 'Full original text is retained in the corresponding sample CSV.', '']
    lines += ['', '## Missing Fields and Limitations', '',
              '- Missing values remain null (empty CSV cells); false is not inferred from absence.',
              '- Metadata price uses the US store and minor currency units; it is a collection-time value.',
              '- Review language is Steam-provided; no independent language classification is applied.',
              '- Means and medians exclude missing values. Ratios use all reviews in the respective group.',
              '- No sales/owner estimates or textual theme/sentiment classification were collected.', '']
    lines += [f'- {key}: {count} missing' for key, count in stats['missing_field_counts'].items() if count]
    lines += [f'- Metadata {key}: missing' for key, value in metadata.items() if value is None]
    lines += ['', '## Generated Files', '']
    paths = sorted(p for p in target.rglob('*') if p.is_file())
    paths += sorted(p for p in (data_dir / 'raw' / game['key']).glob('*') if p.is_file())
    lines += [f'- `{p.relative_to(data_dir).as_posix()}`' for p in paths]
    lines += [f"- `raw/{game['key']}/review_pages/`: immutable complete API pages",
              f"- `reports/{game['key']}/summary.md`", '']
    write_text(data_dir / 'reports' / game['key'] / 'summary.md', '\n'.join(lines))


def main():
    args = arguments('Generate Markdown dataset report').parse_args()
    generate(load_game(args.game, args.config), args.data_dir)


if __name__ == '__main__':
    run_cli(main)
