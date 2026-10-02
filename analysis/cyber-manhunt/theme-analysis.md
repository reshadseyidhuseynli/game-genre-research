# Cyber Manhunt — Review Theme Analizi

## Məqsəd

Bu sənəd Cyber Manhunt üçün verified Steam review dataset üzərində aparılan full-corpus theme scan və semantic audit nəticələrini saxlayır. Rəqəmlər review-lərdəki mövzuların yayılmasını və negative recommendation konsentrasiyasını göstərir; aspect-level sentiment kimi şərh edilməməlidir.

## Dataset

Collection snapshot: **2026-10-02**

- Total Steam-provided English reviews: **847**
- Positive: **681**
- Negative: **166**
- Positive ratio: **80.40%**
- Negative baseline: **19.60%**
- Average playtime at review: **10.95h**
- Median playtime: **9.27h**
- Positive review average playtime: **12.07h**
- Negative review average playtime: **6.33h**
- Very short reviews: **172**

Steam-in English kimi qaytardığı corpus daxilində bəzi başqa-dilli review-lər də var. Pipeline ayrıca language detection etmir; buna görə theme prevalence lexical retrieval siqnalı kimi istifadə olunur.

Candidate taxonomy: `config/theme_taxonomy.yaml` v3  
Semantic taxonomy: `config/aspect_taxonomy.yaml` v3  
Ən azı bir candidate theme tutulan review: **64.70%**

## Əsas theme statistikası

Dataset baseline negative ratio: **19.60%**

| Theme | Mentions | Share | Negative payı | Baseline-a nisbət |
|---|---:|---:|---:|---:|
| STORY_NARRATIVE | 315 | 37.19% | 19.68% | 1.00× |
| INVESTIGATION_DISCOVERY | 190 | 22.43% | 21.58% | 1.10× |
| LOCALIZATION_WRITING | 188 | 22.20% | **36.17%** | **1.85×** |
| PUZZLE_CLARITY | 181 | 21.37% | **29.28%** | **1.49×** |
| CLUE_EVIDENCE_QUALITY | 120 | 14.17% | **29.17%** | **1.49×** |
| INFORMATION_SEARCH | 93 | 10.98% | **30.11%** | **1.54×** |
| DEDUCTION_REASONING | 68 | 8.03% | **32.35%** | **1.65×** |
| REPETITION | 57 | 6.73% | **43.86%** | **2.24×** |
| SOCIAL_ENGINEERING | 51 | 6.02% | **33.33%** | **1.70×** |
| REALISM_ACCURACY | 36 | 4.25% | **8.33%** | **0.43×** |
| UI_USABILITY | 36 | 4.25% | **36.11%** | **1.84×** |
| TIMED_EVENTS | 35 | 4.13% | **34.29%** | **1.75×** |
| LINEARITY_SCRIPTING | 34 | 4.01% | **55.88%** | **2.85×** |
| PUBLIC_OPINION_MINIGAME | 13 | 1.53% | **53.85%** | **2.75×** |

## Early-session risk

| Playtime | Reviews | Positive | Negative | Positive ratio |
|---|---:|---:|---:|---:|
| 0–1h | 36 | 10 | 26 | **27.78%** |
| 1–3h | 59 | 26 | 33 | **44.07%** |
| 3–10h | 364 | 293 | 71 | 80.49% |
| 10h+ | 388 | 352 | 36 | **90.72%** |

İlk 3 saat birlikdə 95 review-dan 59-u negative-dir: **62.11% negative**. Selection bias nəzərə alınmalıdır, amma early-session expectation və usability riski çox güclüdür.

## Əsas semantic nəticələr

### Linearity və scripted progression

LINEARITY_SCRIPTING candidate-lərində negative payı **55.88%**-dir. Review-lərdə oyunçunun nəticəni artıq başa düşməsinə baxmayaraq yalnız xüsusi clue və ya əvvəlcədən təyin edilmiş sıra ilə irəliləyə bilməsi təkrarlanır.

> Investigation oyunu yalnız scripted trigger state-ni yox, mümkün qədər oyunçunun knowledge state-ni qəbul etməlidir.

### Clue və evidence keyfiyyəti

Relevant görünən məlumatın sistem tərəfindən qəbul edilməməsi və ya progress üçün zəif əlaqəli spesifik detail-in məcburi olması deduction hissini zəiflədir.

> Evidence qaydası oyunçunun insan məntiqinə mümkün qədər yaxın olmalıdır.

### Deduction və reasoning

Ən yaxşı anlarda məlumat parçalarını birləşdirmək real “aha” momenti yaradır. Zəif anlarda reasoning yalnız artıq məlum story-ni təsdiqləyən checklist-ə çevrilir.

> Deduction dəyəri cavabın özündə yox, oyunçunun cavaba çatma prosesindədir.

### Localization və writing

LOCALIZATION_WRITING 188 review-da tutulur və negative payı **36.17%**-dir. Text-heavy investigation oyununda zəif tərcümə yalnız presentation problemi deyil; clue interpretation, puzzle instruction, character credibility və emosional təsirə birbaşa zərər verir.

> Narrative/investigation oyununda localization QA gameplay QA-nın hissəsidir.

### Investigation və search

Investigation fantasy özü geniş maraq yaradır, amma search çox istiqamətləndirici və yalnız bir doğru query/progression qəbul edəndə “araşdırma” yox, “scripted routing” kimi hiss oluna bilir.

### Repetition

REPETITION candidate-lərində negative payı **43.86%**-dir. Eyni database/search/account workflow-un target-dən target-ə təkrarlanması göstərir ki, information-driven gameplay də repetition-dan immun deyil.

> Repetition interface növündən yox, decision structure dəyişməyəndə yaranır.

### UI/UX

Investigation UI sadəcə control surface deyil; oyunçunun xarici yaddaşıdır. Scroll, hover detection, click target və info-management friction-i reasoning cost-u artırır.

### Timed events və minigame-lər

Timed event-lərdə negative payı **34.29%**-dir. Yeni və zəif izah edilmiş puzzle-lə timer birləşəndə challenge learning əvəzinə trial-and-error hissi yarada bilir.

Public-opinion/influence minigame cəmi 13 explicit mention daşısa da onların **53.85%**-i negative-dir. Volume aşağıdır, amma mandatory bir zəif mechanic-in bütün recommendation-a təsir edə bilməsi üçün güclü nümunədir.

### Realism / authenticity

REALISM_ACCURACY candidate-lərində negative payı yalnız **8.33%**-dir. Bu, əvvəlki oyunlarla eyni istiqaməti gücləndirir: full technical realism əsas tələb deyil; tanınan real-world səbəb-nəticə və coherent fiction daha vacibdir.

## Developer intent ilə uyğunluq

Developer materiallarında privacy, cyber violence, real hadisələr və social-engineering research əsas məqsədlər kimi göstərilir. Review-lər real-world relevance və investigation fantasy-ni təsdiqləyir, amma English localization və sərt scripted progression bu məqsədin təsirini zəiflədən əsas execution problemləridir.

## Cross-game implication

Üç oyun artıq eyni fundamental riski müxtəlif formalarda göstərir:

- Hacknet — command repetition;
- Midnight Protocol — tactical action repetition;
- Cyber Manhunt — information workflow repetition.

Bu, genre-level hypothesis-i gücləndirir:

> **Dərinlik feature sayından deyil, hər mərhələdə yaranan yeni və mənalı qərarlardan gəlməlidir.**

## Confidence

| Nəticə | Confidence |
|---|---|
| 0–3h xüsusi risk zone-dur | High |
| Linearity deduction hissini zəiflədir | High |
| Localization gameplay keyfiyyətinə ciddi təsir edir | High |
| Story/investigation əsas retention layer-ləridir | High |
| Clue acceptance player logic ilə uyğun olmalıdır | High |
| Repetition information gameplay-də də qalır | High |
| Search freedom və redundant paths böyük opportunity-dir | High |
| Timed puzzles investigation rhythm-i poza bilir | Medium-High |
| Public-opinion minigame yüksək-impact friction-dir | Medium-High |
| Full realism tələb deyil | High |

## Növbəti addım

Nəticələr `analysis/cyber-manhunt/deep-research.md` sənədində product/game-design səviyyəsində birləşdirilməli, sonra Hacknet və Midnight Protocol ilə cross-game comparison aparılmalıdır.
