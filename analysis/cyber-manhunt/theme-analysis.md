# Cyber Manhunt — rəy mövzu Analizi

## Məqsəd

Bu sənəd Cyber Manhunt üçün verified Steam rəy məlumat toplusu üzərində aparılan full-corpus mövzu yoxlama və məna yönümlü yoxlama nəticələrini saxlayır. Rəqəmlər rəy-lərdəki mövzuların yayılmasını və mənfi recommendation konsentrasiyasını göstərir; aspect-level sentiment kimi şərh edilməməlidir.

## məlumat toplusu

Collection snapshot: **2026-10-02**

- Total Steam-provided English reviews: **847**
- müsbət: **681**
- mənfi: **166**
- müsbət ratio: **80.40%**
- mənfi baseline: **19.60%**
- orta oyun müddəti at rəy: **10.95h**
- Median oyun müddəti: **9.27h**
- müsbət rəy orta oyun müddəti: **12.07h**
- mənfi rəy orta oyun müddəti: **6.33h**
- Very short reviews: **172**

Steam-in English kimi qaytardığı corpus daxilində bəzi başqa-dilli rəy-lər də var. Pipeline ayrıca language detection etmir; buna görə mövzu prevalence lexical retrieval siqnalı kimi istifadə olunur.

namizəd taxonomy: `config/theme_taxonomy.yaml` v3  
məna yönümlü taxonomy: `config/aspect_taxonomy.yaml` v3  
Ən azı bir namizəd mövzu tutulan rəy: **64.70%**

## Əsas mövzu statistikası

məlumat toplusu baseline mənfi ratio: **19.60%**

| mövzu | Mentions | Share | mənfi payı | Baseline-a nisbət |
|---|---:|---:|---:|---:|
| STORY_NARRATIVE | 315 | 37.19% | 19.68% | 1.00× |
| INVESTIGATION_DISCOVERY | 190 | 22.43% | 21.58% | 1.10× |
| LOCALIZATION_WRITING | 188 | 22.20% | **36.17%** | **1.85×** |
| PUZZLE_CLARITY | 181 | 21.37% | **29.28%** | **1.49×** |
| CLUE_EVIDENCE_QUALITY | 120 | 14.17% | **29.17%** | **1.49×** |
| INFORMATION_SEARCH | 93 | 10.98% | **30.11%** | **1.54×** |
| DEDUCTION_REASONING | 68 | 8.03% | **32.35%** | **1.65×** |
| təkrarçılıq | 57 | 6.73% | **43.86%** | **2.24×** |
| SOCIAL_ENGINEERING | 51 | 6.02% | **33.33%** | **1.70×** |
| REALISM_ACCURACY | 36 | 4.25% | **8.33%** | **0.43×** |
| UI_USABILITY | 36 | 4.25% | **36.11%** | **1.84×** |
| TIMED_EVENTS | 35 | 4.13% | **34.29%** | **1.75×** |
| LINEARITY_SCRIPTING | 34 | 4.01% | **55.88%** | **2.85×** |
| PUBLIC_OPINION_MINIGAME | 13 | 1.53% | **53.85%** | **2.75×** |

## Early-session risk

| oyun müddəti | Reviews | müsbət | mənfi | müsbət ratio |
|---|---:|---:|---:|---:|
| 0–1h | 36 | 10 | 26 | **27.78%** |
| 1–3h | 59 | 26 | 33 | **44.07%** |
| 3–10h | 364 | 293 | 71 | 80.49% |
| 10h+ | 388 | 352 | 36 | **90.72%** |

İlk 3 saat birlikdə 95 rəy-dan 59-u mənfi-dir: **62.11% mənfi**. Selection bias nəzərə alınmalıdır, amma early-session expectation və usability riski çox güclüdür.

## Əsas məna yönümlü nəticələr

### Linearity və scripted progression

LINEARITY_SCRIPTING namizəd-lərində mənfi payı **55.88%**-dir. rəy-lərdə oyunçunun nəticəni artıq başa düşməsinə baxmayaraq yalnız xüsusi clue və ya əvvəlcədən təyin edilmiş sıra ilə irəliləyə bilməsi təkrarlanır.

> Investigation oyunu yalnız scripted trigger state-ni yox, mümkün qədər oyunçunun knowledge state-ni qəbul etməlidir.

### Clue və dəlil keyfiyyəti

Relevant görünən məlumatın sistem tərəfindən qəbul edilməməsi və ya progress üçün zəif əlaqəli spesifik detail-in məcburi olması deduction hissini zəiflədir.

> dəlil qaydası oyunçunun insan məntiqinə mümkün qədər yaxın olmalıdır.

### Deduction və reasoning

Ən yaxşı anlarda məlumat parçalarını birləşdirmək real “aha” momenti yaradır. Zəif anlarda reasoning yalnız artıq məlum hekayə-ni təsdiqləyən checklist-ə çevrilir.

> Deduction dəyəri cavabın özündə yox, oyunçunun cavaba çatma prosesindədir.

### Localization və writing

LOCALIZATION_WRITING 188 rəy-da tutulur və mənfi payı **36.17%**-dir. Text-heavy investigation oyununda zəif tərcümə yalnız presentation problemi deyil; clue interpretation, puzzle instruction, character credibility və emosional təsirə birbaşa zərər verir.

> Narrative/investigation oyununda localization QA oyun gedişi QA-nın hissəsidir.

### Investigation və search

Investigation fantasy özü geniş maraq yaradır, amma search çox istiqamətləndirici və yalnız bir doğru query/progression qəbul edəndə “araşdırma” yox, “scripted routing” kimi hiss oluna bilir.

### təkrarçılıq

təkrarçılıq namizəd-lərində mənfi payı **43.86%**-dir. Eyni database/search/account iş axını-un target-dən target-ə təkrarlanması göstərir ki, information-driven oyun gedişi də təkrarçılıq-dan immun deyil.

> təkrarçılıq interface növündən yox, qərar structure dəyişməyəndə yaranır.

### UI/UX

Investigation UI sadəcə control surface deyil; oyunçunun xarici yaddaşıdır. Scroll, hover detection, click target və info-management çətinlik-i reasoning cost-u artırır.

### Timed events və minigame-lər

Timed event-lərdə mənfi payı **34.29%**-dir. Yeni və zəif izah edilmiş puzzle-lə timer birləşəndə çətinlik learning əvəzinə trial-and-error hissi yarada bilir.

Public-opinion/influence minigame cəmi 13 explicit mention daşısa da onların **53.85%**-i mənfi-dir. Volume aşağıdır, amma mandatory bir zəif mexanika-in bütün recommendation-a təsir edə bilməsi üçün güclü nümunədir.

### realizm / həqiqilik hissi

REALISM_ACCURACY namizəd-lərində mənfi payı yalnız **8.33%**-dir. Bu, əvvəlki oyunlarla eyni istiqaməti gücləndirir: full technical realizm əsas tələb deyil; tanınan real-world səbəb-nəticə və ardıcıl fiction daha vacibdir.

## yaradıcı intent ilə uyğunluq

yaradıcı materiallarında privacy, cyber violence, real hadisələr və social-engineering araşdırma əsas məqsədlər kimi göstərilir. rəy-lər real-world relevance və investigation fantasy-ni təsdiqləyir, amma English localization və sərt scripted progression bu məqsədin təsirini zəiflədən əsas execution problemləridir.

## oyunlararası implication

Üç oyun artıq eyni fundamental riski müxtəlif formalarda göstərir:

- Hacknet — command təkrarçılıq;
- Midnight Protocol — tactical action təkrarçılıq;
- Cyber Manhunt — information iş axını təkrarçılıq.

Bu, genre-level hypothesis-i gücləndirir:

> **Dərinlik feature sayından deyil, hər mərhələdə yaranan yeni və mənalı qərarlardan gəlməlidir.**

## etibarlılıq

| Nəticə | etibarlılıq |
|---|---|
| 0–3h xüsusi risk zone-dur | High |
| Linearity deduction hissini zəiflədir | High |
| Localization oyun gedişi keyfiyyətinə ciddi təsir edir | High |
| hekayə/investigation əsas oyunda qalma qat-ləridir | High |
| Clue acceptance oyunçu logic ilə uyğun olmalıdır | High |
| təkrarçılıq information oyun gedişi-də də qalır | High |
| Search freedom və redundant paths böyük imkan-dir | High |
| Timed puzzles investigation rhythm-i poza bilir | Medium-High |
| Public-opinion minigame yüksək-impact çətinlik-dir | Medium-High |
| tam realizm tələb deyil | High |

## Növbəti addım

Nəticələr `analysis/cyber-manhunt/deep-research.md` sənədində məhsul/game-dizayn səviyyəsində birləşdirilməli, sonra Hacknet və Midnight Protocol ilə oyunlararası müqayisə aparılmalıdır.
