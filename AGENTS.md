# AGENTS.md

## Layihənin məqsədi

Bu repository terminal, fictional-computer, hacking, digital investigation və computer-UI əsaslı oyunların bazar və oyunçu rəylərini sistemli şəkildə araşdırmaq üçün data pipeline layihəsidir.

Məqsəd yeni oyun implement etmək deyil.

Məqsəd mövcud oyunlar haqqında mümkün qədər strukturlaşdırılmış dataset yaratmaq və sonradan:

- uğurlu oyunların niyə uğurlu olduğunu;
- zəif nəticə göstərən oyunların hansı problemlər yaşadığını;
- oyunçuların hansı xüsusiyyətləri sevdiyini;
- hansı xüsusiyyətlərdən şikayət etdiyini;
- playtime ilə feedback arasında hansı əlaqələrin olduğunu;
- eyni janrdakı uğurlu və zəif oyunlar arasındakı fərqləri

analiz etməyə imkan verən research infrastructure qurmaqdır.

İlk iteration yalnız **Hacknet** oyunu üzərində işləməlidir.

Hacknet Steam App ID:

```text
365450
```

Pipeline Hacknet üçün uğurla işlədikdən sonra digər oyunlara genişləndiriləcək.

---

# Əsas prinsip

Bu repository-də:

```text
data collection
→ raw storage
→ cleaning
→ normalization
→ derived datasets
→ statistics
→ analysis-ready output
```

pipeline-i qurulmalıdır.

Raw data heç vaxt itirilməməli və ya overwrite edilməməlidir.

Processed data həmişə raw data-dan yenidən yaradıla bilməlidir.

---

# Scope

İlk iteration üçün implement edilməli hissələr:

1. game configuration
2. Steam metadata collector
3. Steam review collector
4. raw data storage
5. review cleaning
6. review normalization
7. deduplication
8. playtime segmentation
9. basic statistics
10. analysis-ready CSV/JSON output
11. Markdown summary report

İlk iteration-da Reddit, YouTube, press review və developer interview collector-ları implement edilməməlidir.

Bunlar sonrakı mərhələyə aiddir.

---

# Texnologiya

Python istifadə et.

Tövsiyə olunan versiya:

```text
Python 3.12+
```

Sadə dependency-lərə üstünlük ver.

Mümkün olduqda:

- requests və ya httpx
- pandas
- PyYAML
- python-dateutil

istifadə edilə bilər.

Ağır framework əlavə etmə.

İlk iteration üçün database tələb olunmur.

CSV və JSON/JSONL kifayətdir.

---

# Repository strukturu

Tövsiyə olunan struktur:

```text
game-genre-research/

├── AGENTS.md
├── README.md
├── requirements.txt
│
├── config/
│   └── games.yaml
│
├── src/
│   ├── collectors/
│   │   ├── steam_metadata.py
│   │   └── steam_reviews.py
│   │
│   ├── processors/
│   │   ├── clean_reviews.py
│   │   ├── deduplicate.py
│   │   ├── segment_reviews.py
│   │   └── statistics.py
│   │
│   ├── reports/
│   │   └── game_report.py
│   │
│   └── common/
│       ├── config.py
│       ├── io.py
│       └── logging.py
│
├── data/
│   ├── raw/
│   │   └── hacknet/
│   │
│   ├── processed/
│   │   └── hacknet/
│   │
│   └── reports/
│       └── hacknet/
│
└── tests/
```

Struktur real ehtiyaca görə kiçik dəyişikliklər ala bilər, amma məsuliyyətlər qarışdırılmamalıdır.

---

# Game Configuration

Oyun məlumatları kod daxilində hard-code edilməməlidir.

`config/games.yaml` istifadə et.

İlk versiyada:

```yaml
games:
  - key: hacknet
    name: Hacknet
    steam_app_id: 365450
```

Collector-lar config-dən oyun məlumatını oxumalıdır.

Sonradan yeni oyun əlavə etmək yalnız config dəyişməklə mümkün olmalıdır.

---

# Steam Metadata Collector

Hacknet haqqında mümkün public Steam metadata toplanmalıdır.

Minimum:

```text
steam_app_id
name
release_date
developers
publishers
price
currency
is_free
short_description
genres
categories
supported_languages
header_image
store_url
```

Əgər Steam public endpoint bəzi field-ləri qaytarmırsa, uydurma məlumat əlavə etmə.

Missing məlumat `null` və ya uyğun boş dəyər kimi saxlanmalıdır.

Output:

```text
data/raw/hacknet/steam_metadata.json
```

---

# Steam Review Collector

Əsas dataset Steam review-ləridir.

Mümkün qədər bütün public **English-language** review-ləri toplamağa çalış.

Pagination dəstəklənməlidir.

API rate limit-ə hörmət et.

Transient error zamanı məntiqli retry/backoff istifadə et.

Collector yarıda dayansa, mümkün olduqda əvvəldən hər şeyi yenidən yükləmək məcburiyyəti yaratma.

Raw response məlumatını mümkün qədər qoruyub saxla.

Tövsiyə olunan output:

```text
data/raw/hacknet/steam_reviews.jsonl
```

Hər sətir bir review olmalıdır.

---

# Review Dataset Field-ləri

Mümkün olduqda aşağıdakı field-ləri saxla:

```text
review_id
steam_app_id
game_key
game_name

language
review_text
recommended

created_at
updated_at

playtime_forever_minutes
playtime_at_review_minutes
playtime_last_two_weeks_minutes

votes_up
votes_funny
weighted_vote_score

steam_purchase
received_for_free
written_during_early_access

author_steam_id
author_num_games_owned
author_num_reviews

refunded
```

Steam API müəyyən field-i qaytarmırsa onu fabricate etmə.

Schema daxilində nullable field kimi saxlamaq olar.

---

# Raw Data Qaydası

Raw data dəyişdirilməməlidir.

Collector-dan gələn original review text raw dataset-də olduğu kimi saxlanmalıdır.

Məsələn:

```text
data/raw/hacknet/steam_reviews.jsonl
```

processor tərəfindən rewrite edilməməlidir.

Processed dataset ayrıca yaradılmalıdır.

---

# Review Cleaning

Processed dataset üçün review text cleaning tətbiq edilə bilər.

Amma original mətn mütləq ayrıca saxlanmalıdır.

Field-lər:

```text
review_text_raw
review_text_clean
```

Cleaning yalnız yüngül olmalıdır.

Edilə bilər:

- leading/trailing whitespace silmək;
- repeated whitespace normallaşdırmaq;
- control character-ləri təmizləmək;
- empty review-ləri flag etmək.

Etmə:

- stemming;
- aggressive punctuation removal;
- stopword removal;
- sentence structure dəyişmək;
- meaning dəyişdirən normalization.

Araşdırma üçün original ifadələr vacibdir.

---

# Deduplication

Duplicate review-ləri müəyyən et.

Əsas unique identifier:

```text
review_id
```

olmalıdır.

Eyni `review_id` bir neçə dəfə varsa ən yeni representation saxlanıla bilər.

Deduplication nəticəsində neçə row silindiyi statistikada göstərilməlidir.

---

# Review Quality Flags

Processed dataset-ə aşağıdakı derived field-ləri əlavə et:

```text
is_empty
is_very_short
review_length_chars
review_length_words
```

`is_very_short` üçün başlanğıc threshold:

```text
< 5 words
```

ola bilər.

Review dataset-dən silinməsin.

Sadəcə flag-lənsin.

---

# Playtime Normalization

Minutes field-lərindən əlavə hour field-ləri yarat:

```text
playtime_forever_hours
playtime_at_review_hours
```

Rounding zamanı original minute məlumatını itirmə.

---

# Playtime Segments

Review-ləri `playtime_at_review` əsasında segmentlə.

Başlanğıc segmentlər:

```text
0-1h
1-3h
3-10h
10h+
unknown
```

Derived field:

```text
playtime_segment
```

Segment sərhədləri kod daxilində bir yerdə saxlanmalıdır.

---

# Sentiment

Steam `recommended` field-i overall sentiment kimi istifadə edilə bilər.

Mapping:

```text
recommended = true  -> positive
recommended = false -> negative
```

Derived field:

```text
overall_sentiment
```

İlk iteration-da review text üzərindən AI sentiment classification etmə.

Steam recommendation kifayətdir.

---

# Helpful Review Segmentation

Helpful analysis üçün derived məlumat yarat.

Məsələn:

```text
votes_up
weighted_vote_score
```

əsasında review-ləri sort etmək mümkün olsun.

Ayrıca hard-coded `helpful=true/false` yaratmaq məcburi deyil.

Amma report-da:

```text
top 20 helpful positive reviews
top 20 helpful negative reviews
```

çıxarıla bilər.

---

# Recent Review Segmentation

`created_at` əsasında review-ləri tarixə görə sort etmək mümkün olmalıdır.

Report-da:

```text
20 most recent positive
20 most recent negative
```

sample-ları yaradılmalıdır.

---

# Processed Dataset

Əsas analysis-ready dataset:

```text
data/processed/hacknet/reviews.csv
```

və mümkün olduqda:

```text
data/processed/hacknet/reviews.jsonl
```

yarat.

CSV insan tərəfindən baxmaq üçün rahat olmalıdır.

JSONL gələcək automation/LLM processing üçün istifadə ediləcək.

---

# Basic Statistics

Hacknet üçün aşağıdakı statistikaları hesabla:

```text
total_reviews
positive_reviews
negative_reviews
positive_ratio
negative_ratio

unique_reviews
duplicates_removed

empty_reviews
very_short_reviews

average_playtime_at_review
median_playtime_at_review

average_playtime_positive
average_playtime_negative

review_count_by_playtime_segment

positive_ratio_by_playtime_segment

average_votes_up_positive
average_votes_up_negative
```

Mümkündürsə əlavə faydalı descriptive statistic-lər də əlavə edilə bilər.

Amma lazımsız kompleks statistik model qurma.

---

# Review Samples

Sonrakı qualitative analysis üçün ayrıca sample faylları yarat.

Minimum:

```text
data/processed/hacknet/samples/helpful_positive.csv
data/processed/hacknet/samples/helpful_negative.csv

data/processed/hacknet/samples/recent_positive.csv
data/processed/hacknet/samples/recent_negative.csv

data/processed/hacknet/samples/low_playtime.csv
data/processed/hacknet/samples/high_playtime.csv
```

Sample review-lərin original review text-i saxlanmalıdır.

Sample ölçüləri config vasitəsilə dəyişdirilə bilən olsun.

Default:

```text
50
```

---

# Report

Pipeline sonunda aşağıdakı fayl yaranmalıdır:

```text
data/reports/hacknet/summary.md
```

Report yalnız faktiki dataset-dən hesablanan məlumatlardan ibarət olmalıdır.

Report strukturu:

```markdown
# Hacknet Research Dataset Summary

## Steam Metadata

## Dataset Size

## Sentiment

## Playtime

## Review Quality

## Positive vs Negative Review Statistics

## Playtime Segments

## Most Helpful Review Samples

## Recent Review Samples

## Generated Files
```

Bu report hələ game-design interpretation etməməlidir.

Məsələn belə nəticə yazma:

```text
Players love the story.
```

əgər theme analysis hələ aparılmayıbsa.

Yalnız:

```text
Positive reviews: X
Negative reviews: Y
Median playtime: Z
```

kimi dataset-based nəticələr ver.

Interpretation sonrakı mərhələdə ayrıca ediləcək.

---

# Theme Analysis

İlk iteration-da theme classification implement etmə.

Məsələn:

```text
STORY
ATMOSPHERE
REPETITION
UI
```

classification sonrakı mərhələyə saxlanmalıdır.

İlk məqsəd etibarlı dataset yaratmaqdır.

---

# Reddit

İlk iteration-da Reddit scraping/collection implement etmə.

---

# YouTube

İlk iteration-da YouTube scraping/transcript collection implement etmə.

---

# Press / Developer Interviews

İlk iteration-da implement etmə.

---

# AI / LLM

İlk iteration-da OpenAI və ya başqa LLM API əlavə etmə.

Dataset əvvəlcə deterministic pipeline ilə hazırlanmalıdır.

LLM classification sonrakı mərhələdə ayrıca modul kimi əlavə ediləcək.

---

# CLI

Pipeline command line-dan rahat işləməlidir.

Məsələn:

```bash
python -m src.collectors.steam_metadata --game hacknet
python -m src.collectors.steam_reviews --game hacknet
python -m src.processors.clean_reviews --game hacknet
python -m src.processors.statistics --game hacknet
python -m src.reports.game_report --game hacknet
```

Əgər daha sadə vahid command yaratmaq mümkündürsə:

```bash
python -m src.pipeline --game hacknet
```

üstünlük verilir.

Bu command:

```text
collect
→ process
→ statistics
→ report
```

ardıcıllığını işlədə bilər.

Amma modul command-lar ayrıca işlək qalmalıdır.

---

# Idempotency

Pipeline mümkün qədər idempotent olmalıdır.

Eyni command ikinci dəfə işlədikdə:

- duplicate data yaratmamalıdır;
- raw data-nı səbəbsiz korlamamalıdır;
- processed nəticələri deterministik şəkildə yenidən yarada bilməlidir.

---

# Logging

Aydın logging istifadə et.

Məsələn:

```text
Collecting Hacknet reviews...
Page 1: 100 reviews
Page 2: 100 reviews
...
Raw reviews collected: 12,431

Processing...
Duplicates removed: 14
Final processed reviews: 12,417
```

Amma review text-lərini log-a yazma.

---

# Error Handling

Network error, malformed response və rate limit halları graceful şəkildə handle edilməlidir.

Silent failure etmə.

Error mesajı hansı mərhələdə problem olduğunu aydın göstərməlidir.

---

# Testing

Minimum test-lər:

- config parsing
- review normalization
- deduplication
- playtime segmentation
- statistics calculations

Network collector test-lərində real API-yə hər test zamanı request göndərmə.

Mock/sample response istifadə et.

---

# README

README daxilində bunlar yazılmalıdır:

1. layihənin məqsədi;
2. setup;
3. dependency install;
4. pipeline necə işlədilir;
5. output faylları harada yaranır;
6. yeni oyun necə əlavə edilir;
7. hansı məlumatların Steam-dən gəldiyi;
8. owner/sales estimate-lərin bu iteration-da collect edilmədiyi.

---

# Sales / Owners

Steam exact sales məlumatı vermir.

İlk iteration-da sales/owner estimate scraping etmə.

Bu məlumat daha sonra SteamDB/VG Insights/Gamalytic kimi üçüncü tərəf mənbələrdən ayrıca əlavə edilə bilər.

Collector heç vaxt estimate-i exact sales kimi təqdim etməməlidir.

---

# Kod keyfiyyəti

Prioritet:

```text
correctness
> reproducibility
> readability
> simplicity
> abstraction
```

Overengineering etmə.

İlk iteration bir research tool-dur, production SaaS deyil.

Microservice, database, queue, scheduler, Docker orchestration kimi infrastructure əlavə etmə.

---

# Codex üçün əsas qayda

Əgər tələb aydın deyilsə, özbaşına feature əlavə etmə.

İlk iteration-un məqsədi yalnız budur:

> Hacknet üçün etibarlı, təkrar yaradıla bilən Steam metadata + review dataset hazırlamaq və basic statistics/report yaratmaq.

Bu işləmədən Reddit, YouTube, AI classification və digər oyunlara keçmə.