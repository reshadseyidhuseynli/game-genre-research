from src.common.config import arguments, load_game
from src.common.io import read_json, write_text
from src.common.logging import run_cli


def pct(value):
    return 'məlum deyil' if value is None else f'{value * 100:.2f}%'


def generate(game, data_dir):
    source = data_dir / 'processed' / game['key'] / 'themes' / 'statistics.json'
    if not source.exists():
        raise ValueError('Mövzu statistikası tapılmadı; əvvəl theme_candidates işlədilməlidir')
    stats = read_json(source)

    lines = [
        f'# {game["name"]} — Bütün rəylər üzrə mövzu namizədlərinin yoxlanması',
        '',
        '> Bu hesabat yekun məna yönümlü təsnifat deyil. Regex/açar söz qaydaları ilə tapılan',
        '> rəy namizədlərini və həmin rəylərin Steam tövsiyəsi və oyun müddəti üzrə paylanmasını göstərir.',
        '> Mövzunun müsbət rəy nisbəti həmin aspektə münasibət demək deyil; bu, həmin mövzunu qeyd edən',
        '> rəylərin ümumi Steam tövsiyə nisbətidir.',
        '',
        '## Əhatə',
        '',
        f'- Ümumi rəylər: {stats["total_reviews"]}',
        f'- Ən azı bir mövzu namizədi tutulan rəylər: {stats["reviews_with_any_theme_candidate"]}',
        f'- Namizəd əhatəsi: {pct(stats["coverage_ratio"])}',
        f'- Taksonomiya versiyası: {stats["taxonomy_version"]}',
        '',
        '## Mövzu statistikası',
        '',
        '| Maşın etiketi | Azərbaycan dilində | Qeyd sayı | Pay | Müsbət rəylər | Mənfi rəylər | Ümumi müsbət rəy nisbəti | Rəy anındakı orta oyun müddəti |',
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
            f'{"məlum deyil" if avg is None else f"{avg:.2f}h"} |'
        )

    lines += [
        '',
        '## Ən çox birlikdə görünən mövzular',
        '',
        '| Mövzu A | Mövzu B | Rəy sayı |',
        '|---|---|---:|',
    ]
    for item in stats.get('top_theme_pairs', []):
        lines.append(f'| {item["themes"][0]} | {item["themes"][1]} | {item["count"]} |')

    lines += [
        '',
        '## Şərh qaydaları',
        '',
        '- Bu nəticələr mövzuların yayılması üçün ilkin seçim siqnalıdır.',
        '- Bir rəydə mövzuya aid açar sözün olması həmin aspektin mütləq tərifləndiyi və ya tənqid edildiyi demək deyil.',
        '- Ümumi müsbət/mənfi Steam tövsiyəsi aspekt üzrə münasibət kimi istifadə edilməməlidir.',
        '- Mövzular üzrə yaradılan müsbət/mənfi nümunə CSV-ləri əl ilə və ya LLM ilə məna yönümlü yoxlama üçün istifadə olunur.',
        '- Yekun rəqəmlər yoxlanmış aspekt təsnifatından sonra analysis/<game>/deep-research.md faylına keçirilir.',
        '',
    ]

    target = data_dir / 'reports' / game['key'] / 'theme-candidates.md'
    write_text(target, '\n'.join(lines))
    return target


def main():
    args = arguments('Mövzu namizədləri üzrə hesabat yarat').parse_args()
    generate(load_game(args.game, args.config), args.data_dir)


if __name__ == '__main__':
    run_cli(main)
