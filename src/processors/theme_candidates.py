import re
from collections import Counter
from pathlib import Path

import yaml

from src.common.config import ROOT, arguments, load_game
from src.common.io import read_jsonl, write_csv, write_json, write_jsonl, sha256
from src.common.logging import run_cli


DEFAULT_TAXONOMY = ROOT / 'config/theme_taxonomy.yaml'


def load_taxonomy(path=DEFAULT_TAXONOMY):
    path = Path(path)
    with path.open(encoding='utf-8') as handle:
        raw = yaml.safe_load(handle)
    if not isinstance(raw, dict) or not isinstance(raw.get('themes'), dict):
        raise ValueError('Theme taxonomy requires a themes mapping')

    themes = {}
    for name, spec in raw['themes'].items():
        if not re.fullmatch(r'[A-Z0-9_]+', name):
            raise ValueError(f'Invalid theme name: {name}')
        if not isinstance(spec, dict) or not isinstance(spec.get('label_az'), str):
            raise ValueError(f'Missing label_az for theme: {name}')
        patterns = spec.get('patterns')
        if not isinstance(patterns, list) or not patterns or not all(isinstance(p, str) and p for p in patterns):
            raise ValueError(f'Invalid patterns for theme: {name}')
        try:
            compiled = [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
        except re.error as exc:
            raise ValueError(f'Invalid regex in theme {name}: {exc}') from exc
        themes[name] = {
            'label_az': spec['label_az'],
            'patterns': patterns,
            'compiled': compiled,
        }
    return {
        'version': raw.get('version'),
        'description': raw.get('description'),
        'themes': themes,
        'path': path,
    }


def detect_themes(text, taxonomy):
    text = text or ''
    detected = {}
    for name, spec in taxonomy['themes'].items():
        matched = [pattern for pattern, compiled in zip(spec['patterns'], spec['compiled']) if compiled.search(text)]
        if matched:
            detected[name] = matched
    return detected


def _rank(rows, sentiment, size):
    subset = [row for row in rows if row.get('overall_sentiment') == sentiment]
    return sorted(
        subset,
        key=lambda row: (
            -(row.get('votes_up') or 0),
            -(row.get('weighted_vote_score') or 0),
            -(row.get('review_length_words') or 0),
            row['review_id'],
        )
    )[:size]


def calculate(rows, taxonomy, sample_size):
    theme_rows = {name: [] for name in taxonomy['themes']}
    candidates = []
    for row in rows:
        matches = detect_themes(row.get('review_text_clean'), taxonomy)
        if not matches:
            continue
        names = sorted(matches)
        candidates.append({
            'review_id': row['review_id'],
            'themes': names,
            'matched_patterns': {name: matches[name] for name in names},
        })
        for name in names:
            theme_rows[name].append(row)

    total = len(rows)
    stats = {
        'method': 'deterministic_regex_candidate_retrieval',
        'warning': (
            'Theme hits are retrieval candidates, not final semantic/aspect labels. '
            'Positive ratio is the Steam recommendation ratio among reviews mentioning the theme, '
            'not aspect-level sentiment.'
        ),
        'taxonomy_version': taxonomy['version'],
        'taxonomy_sha256': sha256(taxonomy['path']),
        'total_reviews': total,
        'reviews_with_any_theme_candidate': len(candidates),
        'coverage_ratio': len(candidates) / total if total else None,
        'themes': {},
    }

    for name, subset in theme_rows.items():
        positive = sum(row.get('recommended') is True for row in subset)
        negative = sum(row.get('recommended') is False for row in subset)
        known = positive + negative
        segments = Counter(row.get('playtime_segment') for row in subset)
        playtimes = [row['playtime_at_review_hours'] for row in subset if row.get('playtime_at_review_hours') is not None]
        stats['themes'][name] = {
            'label_az': taxonomy['themes'][name]['label_az'],
            'mention_count': len(subset),
            'mention_ratio': len(subset) / total if total else None,
            'positive_reviews': positive,
            'negative_reviews': negative,
            'positive_ratio': positive / known if known else None,
            'average_playtime_at_review_hours': sum(playtimes) / len(playtimes) if playtimes else None,
            'playtime_segments': dict(sorted(segments.items())),
        }

    pair_counts = Counter()
    for candidate in candidates:
        names = candidate['themes']
        for i, left in enumerate(names):
            for right in names[i + 1:]:
                pair_counts[(left, right)] += 1
    stats['top_theme_pairs'] = [
        {'themes': [left, right], 'count': count}
        for (left, right), count in pair_counts.most_common(30)
    ]

    samples = {}
    for name, subset in theme_rows.items():
        samples[name] = {
            'positive': _rank(subset, 'positive', sample_size),
            'negative': _rank(subset, 'negative', sample_size),
        }
    return candidates, stats, samples


def generate(game, data_dir, taxonomy_path=DEFAULT_TAXONOMY):
    taxonomy = load_taxonomy(taxonomy_path)
    source = data_dir / 'processed' / game['key'] / 'reviews.jsonl'
    if not source.exists():
        raise ValueError('Processed reviews not found; run the main pipeline first')
    rows = read_jsonl(source)
    candidates, stats, samples = calculate(rows, taxonomy, game['sample_size'])

    target = data_dir / 'processed' / game['key'] / 'themes'
    write_jsonl(target / 'candidates.jsonl', candidates)
    write_json(target / 'statistics.json', stats)

    fields = list(rows[0]) if rows else []
    for theme, groups in samples.items():
        for sentiment, subset in groups.items():
            write_csv(target / 'samples' / f'{theme.lower()}_{sentiment}.csv', subset, fields)

    return stats


def main():
    parser = arguments('Generate deterministic theme candidates for review analysis')
    parser.add_argument('--taxonomy', type=Path, default=DEFAULT_TAXONOMY)
    args = parser.parse_args()
    generate(load_game(args.game, args.config), args.data_dir, args.taxonomy)


if __name__ == '__main__':
    run_cli(main)
