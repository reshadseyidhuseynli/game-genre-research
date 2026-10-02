import html
import json
from src.common.config import arguments, load_game
from src.common.io import read_json, read_jsonl, write_text
from src.common.logging import run_cli
from src.processors.clean_reviews import samples
from src.processors.statistics import generate as statistics


LABELS = {
    'raw_reviews': 'Xam rəylər',
    'total_reviews': 'Ümumi rəylər',
    'unique_reviews': 'Təkrarsız rəylər',
    'duplicates_removed': 'Silinmiş təkrarlar',
    'positive_reviews': 'Müsbət rəylər',
    'negative_reviews': 'Mənfi rəylər',
    'unknown_sentiment_reviews': 'Münasibəti məlum olmayan rəylər',
    'positive_ratio': 'Müsbət rəy nisbəti',
    'negative_ratio': 'Mənfi rəy nisbəti',
    'playtime_unit': 'Oyun müddəti vahidi',
    'known_playtime_reviews': 'Oyun müddəti məlum olan rəylər',
    'average_playtime_at_review': 'Rəy anındakı orta oyun müddəti',
    'median_playtime_at_review': 'Rəy anındakı median oyun müddəti',
    'empty_reviews': 'Boş rəylər',
    'very_short_reviews': 'Çox qısa rəylər',
    'average_playtime_positive': 'Müsbət rəylərdə orta oyun müddəti',
    'average_playtime_negative': 'Mənfi rəylərdə orta oyun müddəti',
    'average_votes_up_positive': 'Müsbət rəylərdə orta faydalı səs sayı',
    'average_votes_up_negative': 'Mənfi rəylərdə orta faydalı səs sayı',
}


def display(value):
    if value is None:
        return 'məlum deyil'
    if isinstance(value, float):
        return f'{value:.4f}'
    return html.escape(str(value)).replace('|', '&#124;').replace('\n', ' ')


def generate(game, data_dir):
    target = data_dir / 'processed' / game['key']
    stats = statistics(game, data_dir)
    metadata = read_json(target / 'metadata.json')
    manifest = read_json(data_dir / 'raw' / game['key'] / 'reviews_manifest.json')
    rows = read_jsonl(target / 'reviews.jsonl')

    lines = [f"# {game['name']} — Araşdırma məlumat toplusunun xülasəsi", '', '## Steam metaməlumatı', '']
    lines += [f'- {key}: {display(value)}' for key, value in metadata.items()]

    sections = {
        'Məlumat toplusunun ölçüsü': ['raw_reviews', 'total_reviews', 'unique_reviews', 'duplicates_removed'],
        'Rəy bölgüsü': ['positive_reviews', 'negative_reviews', 'unknown_sentiment_reviews', 'positive_ratio', 'negative_ratio'],
        'Oyun müddəti': ['playtime_unit', 'known_playtime_reviews', 'average_playtime_at_review', 'median_playtime_at_review'],
        'Rəy keyfiyyəti': ['empty_reviews', 'very_short_reviews'],
        'Müsbət və mənfi rəylərin müqayisəsi': [
            'average_playtime_positive', 'average_playtime_negative',
            'average_votes_up_positive', 'average_votes_up_negative'
        ],
    }

    for title, fields in sections.items():
        lines += ['', '## ' + title, '']
        lines += [f'- {LABELS.get(key, key)}: {display(stats[key])}' for key in fields]
        if title == 'Məlumat toplusunun ölçüsü':
            lines += [
                f"- Toplanma müddəti: {manifest['started_at']} — {manifest['finished_at']}",
                f"- Dayanma səbəbi: {manifest['termination']}; səhifələr: {manifest['pages']}",
                f"- API ilk səhifə total_matching: {manifest['total_matching_first_page']}",
                f"- API ilk səhifə query_summary: {display(json.dumps(manifest['query_summary']))}",
                '- Açıq API səhifələməsi sona qədər oxunub; canlı API atomik kəsim deyil və toplama zamanı dəyişə bilər.',
            ]
            matching = manifest['total_matching_first_page']
            if matching is not None:
                lines.append(
                    f"- Toplanmış təkrarsız rəylərlə ilk səhifədəki API ümumi sayı arasındakı fərq: "
                    f"{stats['unique_reviews'] - matching}"
                )

    lines += [
        '', '## Oyun müddəti qrupları', '',
        '| Qrup | Rəy sayı | Müsbət rəy nisbəti |',
        '|---|---:|---:|',
    ]
    for label, count in stats['review_count_by_playtime_segment'].items():
        lines.append(f"| {label} | {count} | {display(stats['positive_ratio_by_playtime_segment'][label])} |")

    selected = samples(rows, 20)
    for title, prefix in [('Ən faydalı rəy nümunələri', 'helpful'), ('Ən yeni rəy nümunələri', 'recent')]:
        lines += ['', '## ' + title, '']
        for sentiment, sentiment_az in (('positive', 'Müsbət'), ('negative', 'Mənfi')):
            lines += [
                f'### {sentiment_az} (maksimum 20)',
                '',
                '| Rəy ID | Yaradılma vaxtı (UTC) | Faydalı səslər | Rəy anındakı oyun müddəti (saat) |',
                '|---|---|---:|---:|',
            ]
            for row in selected[prefix + '_' + sentiment]:
                lines.append('| ' + ' | '.join(display(row[k]) for k in (
                    'review_id', 'created_at', 'votes_up', 'playtime_at_review_hours')) + ' |')
            lines += ['', 'Rəylərin tam mətni uyğun nümunə CSV faylında saxlanılır.', '']

    lines += [
        '', '## Çatışmayan sahələr və məhdudiyyətlər', '',
        '- Çatışmayan dəyərlər null kimi saxlanılır; sahənin olmamasından false nəticəsi çıxarılmır.',
        '- Qiymət metaməlumatı ABŞ mağazasından və valyutanın kiçik vahidlərində alınır; bu, toplama anındakı dəyərdir.',
        '- Rəy dili Steam tərəfindən verilir; ayrıca dil təsnifatı aparılmır.',
        '- Orta və median hesablamaları çatışmayan dəyərləri nəzərə almır. Nisbətlər uyğun qrupdakı bütün rəylərdən hesablanır.',
        '- Satış/sahiblik təxminləri və mətn üzrə mövzu/münasibət təsnifatı bu hesabatda toplanmır.',
        '',
    ]
    lines += [
        f'- {LABELS.get(key, key)}: {count} çatışmayan dəyər'
        for key, count in stats['missing_field_counts'].items() if count
    ]
    lines += [
        f'- Metaməlumat {key}: çatışmır'
        for key, value in metadata.items() if value is None
    ]

    lines += ['', '## Yaradılan fayllar', '']
    paths = sorted(p for p in target.rglob('*') if p.is_file())
    paths += sorted(p for p in (data_dir / 'raw' / game['key']).glob('*') if p.is_file())
    lines += [f'- `{p.relative_to(data_dir).as_posix()}`' for p in paths]
    lines += [
        f"- `raw/{game['key']}/review_pages/`: dəyişdirilməyən tam API səhifələri",
        f"- `reports/{game['key']}/summary.md`",
        '',
    ]
    write_text(data_dir / 'reports' / game['key'] / 'summary.md', '\n'.join(lines))


def main():
    args = arguments('Markdown məlumat toplusu hesabatı yarat').parse_args()
    generate(load_game(args.game, args.config), args.data_dir)


if __name__ == '__main__':
    run_cli(main)
