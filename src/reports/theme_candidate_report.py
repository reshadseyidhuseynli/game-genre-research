from src.common.config import arguments, load_game
from src.common.io import read_json, write_text
from src.common.logging import run_cli


def pct(value):
    return 'n/a' if value is None else f'{value * 100:.2f}%'


def generate(game, data_dir):
    source = data_dir / 'processed' / game['key'] / 'themes' / 'statistics.json'
    if not source.exists():
        raise ValueError('Theme statistics not found; run theme_candidates first')
    stats = read_json(source)

    lines = [
        f'# {game["name"]} — Theme Candidate Corpus Scan',
        '',
        '> Bu report final semantic classification deyil. Regex/keyword qaydaları ilə tapılan',
        '> review namizədlərini və həmin review-lərin Steam recommendation/playtime paylanmasını göstərir.',
        '> Theme-in positive ratio-su aspect sentiment deyil; həmin theme-i qeyd edən review-lərin',
        '> overall Steam recommendation ratio-sudur.',
        '',
        '## Coverage',
        '',
        f'- Total reviews: {stats["total_reviews"]}',
        f'- Reviews with at least one theme candidate: {stats["reviews_with_any_theme_candidate"]}',
        f'- Candidate coverage: {pct(stats["coverage_ratio"])}',
        f'- Taxonomy version: {stats["taxonomy_version"]}',
        '',
        '## Theme statistics',
        '',
        '| Theme | Azərbaycan dilində | Mentions | Share | Positive reviews | Negative reviews | Overall positive ratio | Avg playtime at review |',
        '|---|---|---:|---:|---:|---:|---:|---:|',
    ]

    ordered = sorted(
        stats['themes'].items(),
        key=lambda item: (-item[1]['mention_count'], item[0])
    )
    for name, item in ordered:
        avg = item['average_playtime_at_review_hours']
        lines.append(
            f'| {name} | {item["label_az"]} | {item["mention_count"]} | '
            f'{pct(item["mention_ratio"])} | {item["positive_reviews"]} | '
            f'{item["negative_reviews"]} | {pct(item["positive_ratio"])} | '
            f'{"n/a" if avg is None else f"{avg:.2f}h"} |'
        )

    lines += [
        '',
        '## Top theme co-occurrences',
        '',
        '| Theme A | Theme B | Reviews |',
        '|---|---|---:|',
    ]
    for item in stats.get('top_theme_pairs', []):
        lines.append(f'| {item["themes"][0]} | {item["themes"][1]} | {item["count"]} |')

    lines += [
        '',
        '## Interpretation rules',
        '',
        '- Bu nəticələr theme prevalence üçün ilkin retrieval siqnalıdır.',
        '- Bir review theme keyword-u daşısa da həmin aspect-i tərifləməyə və ya tənqid etməyə bilər.',
        '- Overall positive/negative recommendation aspect sentiment kimi istifadə edilməməlidir.',
        '- Theme-lər üzrə generated positive/negative sample CSV-ləri manual/LLM audit üçün istifadə olunmalıdır.',
        '- Final rəqəmlər audit edilmiş aspect classification-dan sonra analysis/<game>/deep-research.md faylına keçirilməlidir.',
        '',
    ]

    target = data_dir / 'reports' / game['key'] / 'theme-candidates.md'
    write_text(target, '\n'.join(lines))
    return target


def main():
    args = arguments('Generate theme candidate corpus report').parse_args()
    generate(load_game(args.game, args.config), args.data_dir)


if __name__ == '__main__':
    run_cli(main)
