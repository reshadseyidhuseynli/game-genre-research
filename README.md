# Game Genre Research

Reproducible Python research pipeline for public Steam metadata and English reviews.
Iteration one targets **Hacknet (365450)**. It collects evidence and descriptive
statistics, not game-design interpretations. No Reddit, YouTube, LLM, theme
classification, sales/owner estimates, database or infrastructure services.

## Setup

Python 3.12+ recommended. From the repository root:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m src.pipeline --game hacknet
```

On Linux/macOS activate with `source .venv/bin/activate` instead.
This workspace also has a local portable interpreter (excluded from version control):
`\.runtime\python\python.exe` (use `.\.runtime\python\python.exe` from this directory).

## Commands

```powershell
python -m src.pipeline --game hacknet
python -m src.pipeline --game hacknet --offline
python -m src.collectors.steam_metadata --game hacknet
python -m src.collectors.steam_reviews --game hacknet
python -m src.processors.clean_reviews --game hacknet
python -m src.processors.statistics --game hacknet
python -m src.reports.game_report --game hacknet
python -m src.verify --game hacknet
python -m src.theme_pipeline --game hacknet
python -m src.processors.theme_candidates --game hacknet
python -m src.reports.theme_candidate_report --game hacknet
python -m unittest discover -s tests -v
```

All commands accept `--config PATH` and `--data-dir PATH`. Run one pipeline per
data directory at a time. Collection pauses two seconds between requests by
default. Timeouts, HTTP 429/5xx and malformed successful responses retry up to
six attempts with exponential backoff and Retry-After support. Other HTTP errors
fail explicitly. Logs never contain review text.

## Sources

- Metadata: `https://store.steampowered.com/api/appdetails?appids=365450&l=english&cc=us`.
  Public store endpoint; schema/availability is not guaranteed. Entire JSON response
  retained. Normalized metadata includes release date, developer, publisher, price,
  currency, descriptions, genres, categories, languages and image. Price is the
  final amount in minor currency units, for the US store at collection time.
- Reviews: `https://api.steampowered.com/IUserReviewsService/GetAppReviews/v1/`.
  [Valve documentation](https://partner.steamgames.com/doc/webapi/IUserReviewsService).
  `input_json` specifies `appid`, `languages=["english"]`, `filter=1` (recent),
  `review_type=0` (all), `purchase_type=1` (all), `num_per_page=100`,
  `filter_offtopic_activity=false`, and an encoded pagination cursor.
  No API key required. The older `/appreviews` endpoint is deprecated.

Steam supplies text, recommendation, timestamps, author identifiers, playtimes,
helpfulness votes and purchase/free/early-access/refund flags where available.
The current review API no longer returns `author.num_games_owned`; this remains
nullable. Absent boolean fields are **not** interpreted as false. No sales or
owner counts are collected or inferred. Public reviews are not all owners.

## Storage and reproducibility

```text
config/games.yaml
src/collectors/                 metadata and paginated review collection
src/processors/                 normalization, deduplication, segments, statistics
src/reports/                    Markdown generator
src/common/                     config, HTTP retry, file IO, logging
data/raw/hacknet/
  steam_metadata.json           timestamp, query, entire metadata response
  review_pages/000000.json ...   immutable timestamped queries and full responses
  steam_reviews.jsonl           one unmodified API review object per line
  reviews_manifest.json         completion, counts, parameters, SHA-256 checksums
data/processed/hacknet/
  metadata.json
  reviews.csv
  reviews.jsonl
  processing.json               input/output hashes and dedup counts
  statistics.json
  samples/                      six CSVs, default up to 50 rows each
data/reports/hacknet/summary.md
tests/test_pipeline.py
```

Pages are atomically saved before moving the cursor. After interruption, rerun
the same command: existing pages are replayed locally and downloading resumes
at the first absent page. Only an empty response marks collection complete;
repeated cursors fail instead of silently reporting success. The raw JSONL and
manifest are published after completion. All downloaded reviews are already
durable in page files during collection. Raw files are never overwritten.

Completed collections are reused without requests. `--offline` regenerates
processed files, statistics and report from raw data. Same input/config/code
produces the same output bytes. To collect a **new** snapshot while preserving
the old one, use a fresh directory, e.g. `--data-dir data/snapshots/2026-10-02`.
Do not delete raw data to refresh it. Preserve code and requirements alongside
snapshots. Files are UTF-8; CSV uses standard quoting, JSONL uses JSON nulls and
CSV uses empty cells for missing values. Import Steam IDs as text in spreadsheets
to avoid numeric precision loss; review text is literal user-authored text.

The API is live, may cache responses and rate-limit anonymous callers. Exhausting
pagination is not proof of an atomic complete historical archive: reviews can be
added, edited, hidden or deleted during collection. First-page API totals and
actual dataset counts are separately recorded; no rows are fabricated to fill
a difference. Language is Steam's label, not independently classified.

## Derived data definitions

- Original review text is retained in `review_text_raw`; cleaning only removes
  control characters and collapses whitespace. Lengths use cleaned text; words
  are whitespace-delimited. Empty and fewer-than-five-word reviews are flagged,
  never discarded. Missing text remains null in the raw-text field.
- Deduplication uses review ID, latest update timestamp, then later source
  occurrence for ties. Output order is stable by review ID.
- UTC ISO timestamps come from Steam epoch seconds. Minute fields are retained;
  hours divide by 60 without rounding. Invalid/missing numeric values become null.
- Playtime segments use time **at review**: `[0,60)`, `[60,180)`, `[180,600)`,
  `[600,infinity)` minutes and unknown. Boundaries live in one module.
- `overall_sentiment` maps Steam's recommendation to positive/negative; absent
  recommendation stays null. There is no text sentiment model.
- `total_reviews` means processed unique rows; `raw_reviews` is before dedup.
  Ratios use all rows in each group, including unknown sentiment. Means/medians
  exclude nulls, include zero, and playtime statistics are in hours at review.
  Empty groups have null ratios/averages. Missing counts are included.
- Helpful samples sort by votes up, then weighted score, then ID. Recent samples
  sort by creation timestamp descending, then ID descending. Low/high playtime
  samples are the lowest/highest known time-at-review values, with ID tie-breaks.
  They are deterministic ranked selections, not random representative samples.
  Report tables include up to 20 helpful/recent reviews per sentiment; the sample
  CSVs preserve full original text and all normalized fields.

## Configuration and extending later

`config/games.yaml` contains the game identity, `sample_size` (default 50) and
`request_delay_seconds` (default 2; minimum 1). After validating Hacknet, another
game requires only a new `games` entry with `key`, `name`, and `steam_app_id`;
select it using `--game KEY`. No game identity is hard-coded in collectors.

Tests use fixtures/mocks only; they never call Steam.


## Phase 2: theme candidate analysis

After the verified Steam dataset exists, run:

```powershell
python -m src.theme_pipeline --game hacknet
```

Equivalent lower-level commands:

```powershell
python -m src.processors.theme_candidates --game hacknet
python -m src.reports.theme_candidate_report --game hacknet
```

The taxonomy lives in `config/theme_taxonomy.yaml`. This stage is intentionally
a deterministic regex/keyword **candidate retrieval** pass, not final semantic
classification. It creates:

```text
data/processed/hacknet/themes/candidates.jsonl
data/processed/hacknet/themes/statistics.json
data/processed/hacknet/themes/samples/<theme>_positive.csv
data/processed/hacknet/themes/samples/<theme>_negative.csv
data/processed/hacknet/themes/samples/<theme>_audit.csv
data/reports/hacknet/theme-candidates.md
```

The reported positive ratio is the overall Steam recommendation ratio among
reviews mentioning a theme. It must not be interpreted as aspect-level
sentiment. The positive/negative samples prioritize helpful reviews for qualitative reading.
The audit samples are deterministically balanced across recommendation and playtime
cohorts to reduce helpful-review bias. All are inputs for manual/LLM audit and the
later aspect-based classification described in `RESEARCH_MASTER_BRIEF.md`.
