from statistics import mean, median
from src.common.config import arguments, load_game
from src.common.io import read_json, read_jsonl, write_json, sha256
from src.common.logging import run_cli
from src.processors.segment_reviews import SEGMENT_NAMES


def aggregate(rows, field, operation=mean):
    values = [r[field] for r in rows if r[field] is not None]
    return operation(values) if values else None


def calculate(rows, raw_count):
    total = len(rows)
    positive = [r for r in rows if r['recommended'] is True]
    negative = [r for r in rows if r['recommended'] is False]
    result = {'total_reviews': total, 'raw_reviews': raw_count, 'unique_reviews': total,
              'duplicates_removed': raw_count - total, 'positive_reviews': len(positive),
              'negative_reviews': len(negative), 'unknown_sentiment_reviews': total - len(positive) - len(negative),
              'positive_ratio': len(positive) / total if total else None,
              'negative_ratio': len(negative) / total if total else None,
              'empty_reviews': sum(r['is_empty'] for r in rows),
              'very_short_reviews': sum(r['is_very_short'] for r in rows),
              'playtime_unit': 'hours; all playtime statistics use playtime_at_review',
              'average_playtime_at_review': aggregate(rows, 'playtime_at_review_hours'),
              'median_playtime_at_review': aggregate(rows, 'playtime_at_review_hours', median),
              'known_playtime_reviews': sum(r['playtime_at_review_hours'] is not None for r in rows)}
    for label, subset in [('positive', positive), ('negative', negative)]:
        result['average_playtime_' + label] = aggregate(subset, 'playtime_at_review_hours')
        result['average_votes_up_' + label] = aggregate(subset, 'votes_up')
    result['review_count_by_playtime_segment'] = {}
    result['positive_ratio_by_playtime_segment'] = {}
    for label in SEGMENT_NAMES:
        subset = [r for r in rows if r['playtime_segment'] == label]
        result['review_count_by_playtime_segment'][label] = len(subset)
        result['positive_ratio_by_playtime_segment'][label] = (
            sum(r['recommended'] is True for r in subset) / len(subset) if subset else None)
    result['missing_field_counts'] = {field: sum(r[field] is None for r in rows) for field in rows[0]} if rows else {}
    return result


def generate(game, data_dir):
    target = data_dir / 'processed' / game['key']
    info = read_json(target / 'processing.json')
    if sha256(target / 'reviews.jsonl') != info['processed_sha256']:
        raise ValueError('Processed dataset checksum mismatch; rerun processing')
    result = calculate(read_jsonl(target / 'reviews.jsonl'), info['raw_reviews'])
    write_json(target / 'statistics.json', result)
    return result


def main():
    args = arguments('Calculate dataset statistics').parse_args()
    generate(load_game(args.game, args.config), args.data_dir)


if __name__ == '__main__':
    run_cli(main)
