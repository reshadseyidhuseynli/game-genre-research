import logging
import math
import unicodedata
from datetime import datetime, timezone
from src.common.config import arguments, load_game
from src.common.io import read_json, read_jsonl, write_json, write_jsonl, write_csv, sha256
from src.common.logging import run_cli
from src.collectors.steam_metadata import normalize_metadata
from src.processors.deduplicate import deduplicate
from src.processors.segment_reviews import segment


def number(value):
    if value is None or isinstance(value, bool):
        return None
    try:
        result = float(value)
        return result if math.isfinite(result) and result >= 0 else None
    except (ValueError, TypeError):
        return None


def timestamp(value):
    value = number(value)
    if value is None:
        return None
    try:
        return datetime.fromtimestamp(value, timezone.utc).isoformat()
    except (OverflowError, ValueError, OSError):
        return None


def normalize(review, game):
    author = review.get('author') or {}
    original = review.get('review')
    if original is not None and not isinstance(original, str):
        raise ValueError('Review text must be string or null')
    clean = ''.join(' ' if c.isspace() else c for c in original or ''
                    if c.isspace() or unicodedata.category(c) != 'Cc')
    clean = ' '.join(clean.split())
    recommended = review.get('voted_up')
    recommended = recommended if type(recommended) is bool else None
    row = {'review_id': str(review['recommendationid']), 'steam_app_id': game['steam_app_id'],
           'game_key': game['key'], 'game_name': game['name'], 'language': review.get('language'),
           'review_text_raw': original, 'review_text_clean': clean, 'recommended': recommended,
           'created_at': timestamp(review.get('timestamp_created')),
           'updated_at': timestamp(review.get('timestamp_updated'))}
    for field in ('playtime_forever', 'playtime_at_review', 'playtime_last_two_weeks'):
        row[field + '_minutes'] = number(author.get(field))
    for field in ('votes_up', 'votes_funny', 'weighted_vote_score'):
        row[field] = number(review.get(field))
    for field in ('steam_purchase', 'received_for_free', 'written_during_early_access', 'refunded'):
        row[field] = review.get(field) if type(review.get(field)) is bool else None
    row['author_steam_id'] = str(author['steamid']) if author.get('steamid') is not None else None
    row['author_num_games_owned'] = number(author.get('num_games_owned'))
    row['author_num_reviews'] = number(author.get('num_reviews'))
    row.update(is_empty=not clean, is_very_short=len(clean.split()) < 5,
               review_length_chars=len(clean), review_length_words=len(clean.split()))
    for field in ('playtime_forever', 'playtime_at_review'):
        minutes = row[field + '_minutes']
        row[field + '_hours'] = minutes / 60 if minutes is not None else None
    row['playtime_segment'] = segment(row['playtime_at_review_minutes'])
    row['overall_sentiment'] = 'positive' if recommended is True else 'negative' if recommended is False else None
    return row


def samples(rows, size):
    result = {}
    for sentiment in ('positive', 'negative'):
        subset = [r for r in rows if r['overall_sentiment'] == sentiment]
        result['helpful_' + sentiment] = sorted(subset, key=lambda r: (
            -(r['votes_up'] or 0), -(r['weighted_vote_score'] or 0), r['review_id']))[:size]
        result['recent_' + sentiment] = sorted(subset, key=lambda r: (
            r['created_at'] or '', r['review_id']), reverse=True)[:size]
    known = [r for r in rows if r['playtime_at_review_minutes'] is not None]
    result['low_playtime'] = sorted(known, key=lambda r: (r['playtime_at_review_minutes'], r['review_id']))[:size]
    result['high_playtime'] = sorted(known, key=lambda r: (-r['playtime_at_review_minutes'], r['review_id']))[:size]
    return result


def process(game, data_dir):
    raw = data_dir / 'raw' / game['key']
    target = data_dir / 'processed' / game['key']
    manifest = read_json(raw / 'reviews_manifest.json')
    if manifest['params']['appid'] != game['steam_app_id']:
        raise ValueError('Raw snapshot does not match configured app')
    source = raw / 'steam_reviews.jsonl'
    if not manifest.get('completed') or sha256(source) != manifest['raw_sha256']:
        raise ValueError('Processing requires complete, verified raw collection')
    raw_rows = read_jsonl(source)
    if any(r.get('language') != 'english' for r in raw_rows):
        raise ValueError('Non-English row in raw dataset')
    rows, removed = deduplicate([normalize(r, game) for r in raw_rows])
    fields = list(normalize({'recommendationid': 'schema'}, game))
    write_jsonl(target / 'reviews.jsonl', rows)
    write_csv(target / 'reviews.csv', rows, fields)
    for name, subset in samples(rows, game['sample_size']).items():
        write_csv(target / 'samples' / (name + '.csv'), subset, fields)
    metadata = read_json(raw / 'steam_metadata.json')
    write_json(target / 'metadata.json', normalize_metadata(metadata['response'], game))
    write_json(target / 'processing.json', {'raw_reviews': len(raw_rows), 'unique_reviews': len(rows),
               'duplicates_removed': removed, 'raw_sha256': sha256(source),
               'processed_sha256': sha256(target / 'reviews.jsonl'), 'sample_size': game['sample_size'],
               'schema_version': 1})
    logging.info('Processing: %s raw, %s duplicates removed, %s final', len(raw_rows), removed, len(rows))
    return rows


def main():
    args = arguments('Normalize reviews and generate samples').parse_args()
    process(load_game(args.game, args.config), args.data_dir)


if __name__ == '__main__':
    run_cli(main)
