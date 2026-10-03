# Orwell: Keeping an Eye On You — Review Theme Analizi

## 1. Məqsəd

Bu sənəd Orwell üçün verified Steam review dataset üzərində full-corpus theme scan və semantic audit nəticələrini saxlayır.

Əsas research sualı:

> **Məlumatı yalnız tapmaq deyil, hansı məlumatı sistemə ötürmək qərarı real player agency və moral tension yaradırmı?**

Qısa nəticə:

> **Bəli, bu Orwell-un ən güclü fərqləndiricisidir. Amma auto-highlight, adviser interpretasiyası və mandatory progression həmin agency-ni qismən zəiflədir.**

---

## 2. Dataset

Snapshot: **2026-10-02**

- Total reviews: **8,549**
- Positive: **7,735**
- Negative: **814**
- Positive ratio: **90.48%**
- Negative baseline: **9.52%**
- Average playtime at review: **6.41h**
- Median playtime: **5.07h**
- Positive average playtime: **6.62h**
- Negative average playtime: **4.43h**
- Very short reviews: **1,060**
- Missing playtime-at-review: **108**

Əsas data:
- `data/processed/orwell/reviews.jsonl`
- `data/processed/orwell/statistics.json`
- `data/reports/orwell/summary.md`

---

## 3. Audit metodu

Analiz üç layer-dən ibarətdir:

1. bütün 8,549 review üzrə reusable regex/theme candidate scan;
2. helpful, recent, low-playtime və high-playtime sample-lar üzrə semantic audit;
3. Orwell-specific candidate-lər üzrə targeted review retrieval.

Bütün 814 negative review manual classify edilməyib.

Candidate taxonomy:
- `config/theme_taxonomy.yaml` — v5

Semantic taxonomy:
- `config/aspect_taxonomy.yaml` — v5

Ən azı bir candidate theme tutulan review:

**65.15%**

Bu rəqəm semantic coverage deyil; lexical retrieval coverage-dir.

---

# 4. Playtime cohort-ları

| Playtime | Reviews | Positive ratio |
|---|---:|---:|
| 0–1h | 357 | **54.34%** |
| 1–3h | 896 | **79.46%** |
| 3–10h | 6,064 | **93.26%** |
| 10h+ | 1,124 | **95.28%** |
| unknown | 108 | 95.37% |

Orwell-da risk ən çox ilk saatdadır.

0–1h cohort-un yarısına yaxını negative-dir.

Sonra satisfaction kəskin yüksəlir.

Bu selection bias daşıyır, amma early-session friction üçün güclü siqnaldır.

Early negative review-lərdə əsas səbəblər:
- “sadəcə highlight edilmiş text-i drag edirəm” hissi;
- gameplay expectation mismatch;
- adviser-in həddindən artıq yönləndirməsi;
- reading-heavy interaction;
- real deduction gözləyən player-in passiv hiss etməsi.

---

# 5. Əsas theme statistikası

Dataset baseline negative ratio: **9.52%**

| Theme | Mentions | Dataset payı | Negative review payı | Baseline-a nisbət |
|---|---:|---:|---:|---:|
| STORY_NARRATIVE | 3,856 | 45.10% | 10.22% | 1.07× |
| PRIVACY_SURVEILLANCE | 1,384 | 16.19% | **8.38%** | **0.88×** |
| INVESTIGATION_DISCOVERY | 1,140 | 13.33% | 12.81% | 1.35× |
| CLUE_EVIDENCE_QUALITY | 779 | 9.11% | **22.46%** | **2.36×** |
| ETHICAL_SOCIAL_THEME | 671 | 7.85% | **8.35%** | **0.88×** |
| PLAYER_AGENCY | 647 | 7.57% | 16.54% | 1.74× |
| INFORMATION_SEARCH | 589 | 6.89% | 16.30% | 1.71× |
| CONSEQUENCE_VISIBILITY | 529 | 6.19% | **8.32%** | **0.87×** |
| MORAL_AMBIGUITY | 495 | 5.79% | **8.48%** | **0.89×** |
| UI_USABILITY | 474 | 5.54% | 16.88% | 1.77× |
| LINEARITY_SCRIPTING | 458 | 5.36% | **22.71%** | **2.38×** |
| SAVE_REPLAY | 395 | 4.62% | 9.11% | 0.96× |
| DEDUCTION_REASONING | 368 | 4.30% | 19.29% | 2.03× |
| AUTO_HIGHLIGHTING | 352 | 4.12% | **36.93%** | **3.88×** |
| WORLD_REACTIVITY | 325 | 3.80% | **7.08%** | **0.74×** |
| ONBOARDING_CLARITY | 184 | 2.15% | **31.52%** | **3.31×** |
| READING_LOAD | 178 | 2.08% | 10.11% | 1.06× |
| REPETITION | 174 | 2.04% | **27.01%** | **2.84×** |
| CONTRADICTORY_EVIDENCE | 163 | 1.91% | **23.31%** | **2.45×** |
| INTERPRETATION_GUIDANCE | 154 | 1.80% | **29.87%** | **3.14×** |
| INFORMATION_SELECTION | 133 | 1.56% | **18.80%** | **1.97×** |
| HANDHOLDING_GUIDANCE | 89 | 1.04% | **39.33%** | **4.13×** |
| INFORMATION_IRREVERSIBILITY | 28 | 0.33% | **25.00%** | **2.63×** |

Bu rəqəmlər aspect sentiment deyil; theme-i qeyd edən review-lərdə overall Steam recommendation payını göstərir.

---

# 6. Əsas uğur: consequence görünəndə information selection işləyir

CONSEQUENCE_VISIBILITY:
- 529 mentions;
- 8.32% negative;
- baseline-dan aşağı.

WORLD_REACTIVITY:
- 325 mentions;
- 7.08% negative.

PRIVACY_SURVEILLANCE:
- 1,384 mentions;
- 8.38% negative.

MORAL_AMBIGUITY:
- 495 mentions;
- 8.48% negative.

Bu dörd theme eyni istiqamətdədir:

> **Orwell-un əsas premise-i sadəcə maraqlı concept deyil; player response-da real satisfaction yaradır.**

Positive review-lərdə ən güclü pattern:
- hansı datachunk-u ötürəcəyini düşünmək;
- hansı information-u gizlətməyin mümkün nəticəsini hesablamaq;
- adviser-in yalnız sənin ötürdüyün data əsasında insan haqqında fikir qurması;
- öz bias-ını hiss etmək;
- şəxsi məlumatı context-dən çıxarmağın təhlükəsini görmək.

Developer Daniel Marx-in postmortem-i də mechanic-in məhz bu məqsədlə qurulduğunu deyir: hər datachunk potensial consequence daşımalı və player hər micro-decision-u düşünməlidir.

**Confidence: High**

---

# 7. Information selection özü niyə mixed görünür?

INFORMATION_SELECTION candidate-lərində:
- 133 explicit mention;
- 18.80% negative;
- baseline-dan təxminən 1.97× yüksək.

Bu mechanic-in zəif olduğunu göstərmir.

Semantic audit iki fərqli experience göstərir.

## Positive

Player:
- sensitive data-nı gizlədə bilir;
- conflicting data arasında seçim edir;
- story outcome-u dəyişə bilir;
- öz bias-ını mechanic vasitəsilə hiss edir.

## Negative

Player:
- hansı information-un mandatory progression üçün lazım olduğunu bilmir;
- privacy qorumaq üçün data verməyəndə story dayana bilər;
- seçim “moral choice” yox, “hansı trigger-i aktivləşdirim?” kimi hiss oluna bilər.

### Əsas lesson

> **Selection yalnız real alternativlər arasında seçim olanda agency-dir. Mandatory hidden progression dependency seçim hissini zəiflədir.**

---

# 8. Auto-highlighting — ən güclü usability/deduction problemi

AUTO_HIGHLIGHTING:
- 352 mentions;
- 130 negative;
- **36.93% negative**;
- baseline-dan **3.88×** yüksək.

Bu Orwell-un ən güclü negative concentration theme-lərindən biridir.

Developer postmortem-də bunun niyə yarandığı aydındır:
- ilkin prototipdə demək olar hər text/image extract edilə bilirdi;
- bu player-ləri overload edirdi;
- task sistemi isə oyunu çox linear hiss etdirirdi;
- finalda yalnız predefined datachunk-lar extract edilə bildi və onları görünən etmək üçün highlight tətbiq olundu.

Bu accessibility problemini həll etdi.

Amma player response göstərir ki, yeni problem yarandı:

> **Relevant information-u sistem əvvəlcədən göstərirsə, player-in oxuma və tapma rolu azalır.**

Negative review-lərdə:
- “highlight edilmiş hissələri drag et”;
- “oxumağa ehtiyac yoxdur”;
- “detective work deyil”;
- “game mənim yerimə relevant data-nı seçib”

şikayətləri təkrarlanır.

### Design principle

> **Discovery assistance progressive olmalıdır; default state player-in relevance judgment-ını tam əvəz etməməlidir.**

**Confidence: High**

---

# 9. Interpretation guidance və adviser paradoksu

INTERPRETATION_GUIDANCE:
- 154 mentions;
- **29.87% negative**;
- baseline-dan **3.14×** yüksək.

HANDHOLDING_GUIDANCE:
- 89 mentions;
- **39.33% negative**;
- baseline-dan **4.13×** yüksək.

Developer üçün adviser çox vacib idi:
- consequence feedback verir;
- player-in ötürdüyü data əsasında target haqqında model qurur;
- arrest və intervention kimi real action-ları o edir.

Bu uğurlu systemdir.

Amma eyni character:
- player-a nə düşünməli olduğunu deyəndə;
- next step-i həddindən artıq izah edəndə;
- yanlış və ya qərəzli conclusion çıxardıqda player-in correction imkanı olmayanda

agency zəifləyir.

### Əsas distinction

Adviser-in iki rolu ayrılmalıdır:

1. **world actor** — sənin məlumatına reaksiya verir;
2. **tutorial/interpreter** — sənə məlumatın nə demək olduğunu deyir.

Birinci rol immersion və consequence yaradır.

İkinci rol həddindən artıq olduqda deduction-u öldürür.

**Confidence: High**

---

# 10. Contradictory evidence — concept güclü, execution risklidir

CONTRADICTORY_EVIDENCE:
- 163 mentions;
- **23.31% negative**;
- baseline-dan 2.45× yüksək.

Developer bunu qəsdən yaratdığını açıq deyir:
- online information subyektiv ola bilər;
- insanlar yalan deyə bilər;
- system context-i səhv anlaya bilər;
- player özü bias daşıya bilər.

Bu Orwell-un ən ağıllı design layer-lərindən biridir.

Positive experience:

> “məndə kifayət qədər evidence var, amma hansı interpretation-a inanmalıyam?”

Negative experience:

> “məndə kifayət qədər evidence yoxdur, amma sistem məni irreversible seçimə məcbur edir.”

### Fundamental distinction

> **Ambiguity yaxşıdır; blindness yaxşı deyil.**

Moral/deductive uncertainty üçün player:
- relevant context-i görə bilməli;
- alternatives-i müqayisə edə bilməli;
- qərarın niyə çətin olduğunu anlaya bilməlidir.

**Confidence: High**

---

# 11. Information irreversibility

INFORMATION_IRREVERSIBILITY:
- cəmi 28 explicit mention;
- **25% negative**;
- baseline-dan 2.63× yüksək.

Volume aşağıdır, amma semantic evidence consistent-dir.

Orwell-da upload edilmiş data:
- adviser-in worldview-na daxil olur;
- geri götürülmür;
- sonrakı action-a təsir edə bilər.

Bu permanence consequence hissi üçün vacibdir.

Amma problem:
- yeni evidence sonradan gəlirsə;
- əvvəlki interpretation artıq yanlış görünürsə;
- player correction edə bilmirsə

system epistemic olaraq sərt hiss olunur.

### Design principle

> **Irreversible consequence yalnız player-in kifayət qədər məlumatla şüurlu commitment etdiyi nöqtədə ən yaxşı işləyir.**

Yeni evidence gəldikdə correction/qualification imkanı ayrıca design edilməlidir.

**Confidence: Medium-High**

---

# 12. Player agency

PLAYER_AGENCY:
- 647 mentions;
- 16.54% negative;
- baseline-dan 1.74× yüksək.

Bu mixed signal-dır.

Orwell The Operator-dan daha çox real agency verir:
- information-u ötürmək və ya gizlətmək;
- conflicting chunk seçmək;
- müəyyən character-lərin fate-inə təsir etmək;
- alternative outcomes.

Amma agency limits:
- progression üçün bəzi data mandatory-dir;
- player adviser-in interpretation-na birbaşa cavab verə bilmir;
- highlighted data outside system-in information universe-i araşdırıla bilmir;
- bəzi outcome-lar player-in intent-indən fərqli yarana bilər.

### Nəticə

> **Orwell strategic/narrative agency-də The Operator-dan daha güclüdür, amma procedural investigation agency-si hələ məhduddur.**

---

# 13. Story və character depth

STORY_NARRATIVE:
- 3,856 mentions;
- 45.10% dataset share.

Negative ratio:
- 10.22%;
- baseline-a çox yaxındır.

Story həm praise, həm criticism-in əsas mövzusudur.

Positive:
- character complexity;
- tension;
- personal consequences;
- episodic mystery;
- moral discomfort.

Negative:
- bəzi player-lər political message-i çox açıq sayır;
- bəzi ending və character motivation-ları zəif hesab olunur;
- investigation autonomy expectation-ı story-first structure ilə toqquşur.

Developer-in IGF interview-i göstərir ki, character-lər qəsdən müxtəlif privacy layer-lərində qurulub:
- public persona;
- private social communication;
- şəxsi documents və browser-history kimi daha dərin layer.

Bu structure player-a bir insan haqqında “single truth” yox, müxtəlif context-lər göstərir.

**Confidence: High**

---

# 14. Privacy/surveillance — theme gameplay-in özündə yaşayır

PRIVACY_SURVEILLANCE:
- 1,384 mentions;
- negative ratio 8.38%, baseline-dan aşağı.

Bu vacibdir.

Orwell-un social message-i sadəcə exposition deyil.

Player:
- private chat oxuyur;
- personal files açır;
- bank və metadata kimi məlumatlara baxır;
- sonra həmin məlumatı ötürmək barədə qərar verir.

Yəni theme:

> **mechanic-in özündədir.**

Bu Papers, Please-dən gələn design DNA ilə uyğun gəlir: moral issue explicit dialogue choice kimi yox, routine work decision kimi təqdim edilir.

**Confidence: High**

---

# 15. Moral ambiguity — uğurlu, amma hamı üçün deyil

MORAL_AMBIGUITY:
- 495 mentions;
- 8.48% negative.

ETHICAL_SOCIAL_THEME:
- 671 mentions;
- 8.35% negative.

Hər ikisi baseline-dan daha yaxşıdır.

Bu göstərir ki, Orwell-un ethical layer-i ümumən satisfaction driver-dir.

Positive review-lərdə:
- conscience;
- guilt;
- privacy vs safety;
- personal bias;
- “mən system-in pis tərəfinə çevrildimmi?” hissi

güclüdür.

Negative review-lərin bir hissəsi isə:
- game-in moral mövqeyini artıq müəyyən etdiyini;
- terror context-in surveillance criticism-i zəiflətdiyini;
- message-in preachy və ya binary olduğunu

deyir.

### Principle

> **Ethical tension player öz conclusion-na gəldikdə daha güclüdür.**

**Confidence: High**

---

# 16. Consequence visibility — Orwell-un ən güclü design nailiyyətlərindən biri

CONSEQUENCE_VISIBILITY:
- 529 mentions;
- 8.32% negative.

WORLD_REACTIVITY:
- 325 mentions;
- yalnız 7.08% negative.

Developer postmortem-də immediate feedback xüsusi design məqsədi idi:
- adviser comment;
- arrest/intervention;
- later conversation branch;
- target behavior change.

Bu player-a micro-decision-ların boş olmadığını göstərir.

Bu Midnight Protocol və The Operator research-lərində tapdığımız “choice contract” probleminə konkret cavabdır.

### Cross-game principle

> **Choice-in dəyəri yalnız branch count ilə ölçülmür; player qərardan sonra dəyişmiş world state-i hiss etməlidir.**

**Confidence: High**

---

# 17. Repetition

REPETITION:
- 174 mentions;
- **27.01% negative**;
- baseline-dan 2.84× yüksək.

Orwell-un core action grammar-i:
- page aç;
- highlighted data tap;
- drag/upload;
- adviser response;
- yeni document;
- repeat.

Story və moral context bu loop-u çox player üçün daşıyır.

Amma mechanic özü dəyişmədikdə:
- drag-and-drop;
- reading;
- waiting;
- upload

monotonlaşa bilir.

Bu artıq əvvəlki oyunlarla eyni genre-level finding-i dördüncü dəfə dəstəkləyir:

> **Repetition interface-dən yox, cognitive/action grammar-in dəyişməməsindən yaranır.**

**Confidence: High**

---

# 18. Reading load

READING_LOAD:
- 178 mentions;
- 10.11% negative;
- baseline-a yaxındır.

Bu maraqlı nəticədir.

Orwell text-heavy oyundur, amma “çox oxumaq” özü əsas problem deyil.

Problem daha çox:
- oxuduğunun relevance-ni game özü highlight edəndə;
- passiv reading real decision-a çevrilməyəndə;
- dialogue skip/pace friction-i yarananda

görünür.

### Nəticə

> **Text volume yox, text-in decision value-su əsasdır.**

---

# 19. Developer intent vs player outcome

## Intent: hər micro-decision meaningful olsun

Developer datachunk mechanic-i məhz buna görə qurub.

**Outcome:** böyük ölçüdə uğurlu.

Consequence və world-reactivity signals sağlamdır.

## Intent: ambiguity saxlanılsın

Developer explicit right/wrong sistemindən qaçıb.

**Outcome:** çox vaxt uğurlu, amma conflicting-data hissəsində bəzi player-lər blind choice hiss edir.

## Intent: player özü relevance seçsin

Final system-də datachunks highlighted edilir.

**Outcome:** accessibility yaxşılaşır, amma deduction/discovery zəifləyir.

## Intent: adviser consequence feedback versin

**Outcome:** çox uğurlu world-reactivity layer, amma bəzi player üçün excessive interpretation/hand-holding.

---

# 20. Orwell-un əsas uğur faktorları

1. **Information selection mechanic narrative choice-u interface action-a çevirir.**
2. **Consequence feedback tez və görünəndir.**
3. **Privacy theme gameplay-in özündə yaşayır.**
4. **Character information müxtəlif context layer-lərində verilir.**
5. **Player öz bias-ı ilə üzləşir.**
6. **Moral choice explicit dialogue menu olmadan yaranır.**
7. **Desktop interface və data workflow fantasy ilə uyğun gəlir.**
8. **Story routine information work-ə emosional weight verir.**

---

# 21. Əsas failure pattern-lər

1. **Auto-highlight deduction və reading relevance-ni player-dan alır.**
2. **Adviser consequence feedback-dən interpretasiya diktəsinə keçə bilir.**
3. **Mandatory hidden datachunks real information selection agency-ni zəiflədir.**
4. **Contradictory evidence bəzən meaningful ambiguity yox, insufficient information hissi verir.**
5. **Irreversible upload yeni evidence gəldikdə unfair görünə bilər.**
6. **Core drag/upload loop repetition yaradır.**
7. **Procedural investigation freedom məhduddur.**
8. **Early-session gameplay expectation mismatch yüksəkdir.**

---

# 22. Bizim gələcək oyun üçün design dərsləri

## 22.1. Information selection real mechanic ola bilər

Player yalnız “nə doğrudur?” yox:

> “nəyi paylaşmağa hazıram?”

sualına cavab verə bilər.

## 22.2. Consequence tez görünməlidir

Qərarın:
- immediate;
- delayed;
- systemic

feedback-i olmalıdır.

## 22.3. Context extraction özü mechanic ola bilər

Raw sentence-i “fact” kimi götürmək təhlükəlidir.

Player:
- source;
- context;
- reliability;
- intent

haqqında düşünməlidir.

## 22.4. Highlight hint kimi işləməlidir

Default olaraq bütün relevant text görünməməlidir.

## 22.5. Adviser reaksiya versin, cavabı deməsin

NPC:
- qərarın nəticəsini göstərə bilər;
- öz bias-ını ifadə edə bilər;

amma player-in evidence interpretation-nı tam əvəz etməməlidir.

## 22.6. Irreversibility informed commitment-dən sonra olsun

Player yeni evidence görmədən əvvəl irreversible qərara məcbur edilməməlidir.

## 22.7. Moral ambiguity binary choice-dan güclüdür

Ən yaxşı dilemma:
- hər iki qərarın cost-u var;
- player niyə seçdiyini özü izah edə bilir.

---

# 23. Cross-game nəticə

Hazır dörd əsas oyun belə bir evolution göstərir:

Hacknet:
- information tapmaq və access etmək.

Midnight Protocol:
- action plan və consequence.

Cyber Manhunt:
- information əlaqələndirmək.

The Operator:
- focused evidence analysis.

Orwell:
- **information-u seçib başqasına təqdim etmək və onun consequence-nı görmək.**

Bu research üçün vacib progression-dır.

Gələcək concept üçün ən maraqlı loop artıq belə görünür:

> **discover → verify → contextualize → choose what to reveal → consequence → changed information space**

Bu hələ final concept deyil, amma evidence-backed opportunity istiqamətidir.

---

# 24. Confidence matrix

| Nəticə | Confidence |
|---|---|
| Privacy/surveillance theme əsas satisfaction driver-dir | High |
| Consequence visibility Orwell-un əsas gücüdür | High |
| Auto-highlighting deduction-u zəiflədir | High |
| Adviser həm güclü feedback system, həm hand-holding riski yaradır | High |
| Contradictory evidence concept dəyərlidir, amma blind-choice riski var | High |
| Information selection real agency yaradır, lakin mandatory progression onu zəiflədə bilir | High |
| Irreversibility yalnız informed commitment ilə sağlamdır | Medium-High |
| Reading load özü əsas problem deyil | Medium-High |
| Repetition əsas recurring risk olaraq qalır | High |
| Moral ambiguity explicit moral choice-dan daha güclü görünür | High |

---

# 25. Mənbələr

## Daxili

- `data/processed/orwell/statistics.json`
- `data/processed/orwell/reviews.jsonl`
- `data/reports/orwell/summary.md`
- helpful/recent/low/high review samples

## Xarici

**Osmotic Studios — Orwell: Keeping an Eye On You**  
https://www.osmoticstudios.com/orwell-keeping-an-eye-on-you/

**Game Developer — Game Design Deep Dive: Decisions that matter in Orwell**  
https://www.gamedeveloper.com/design/game-design-deep-dive-decisions-that-matter-in-i-orwell-i-

**Game Developer — Road to the IGF: Osmotic Studios' Orwell**  
https://www.gamedeveloper.com/design/road-to-the-igf-osmotic-studios-i-orwell-i-

**Osmotic Studios — Big Brother has arrived – and it’s you**  
https://www.osmoticstudios.com/2016/08/big-brother-has-arrived/

---

# Status

**Mərhələ:** Orwell full-corpus review analysis — tamamlanıb  
**Dataset:** 8,549 verified reviews  
**Növbəti:** `analysis/orwell/deep-research.md` və sonra Orwell vs Need to Know focused comparison.
