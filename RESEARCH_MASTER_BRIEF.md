# RESEARCH_MASTER_BRIEF.md

## 0. Bu sənəd nə üçündür?

Bu sənəd **Game Genre Research** layihəsinin əsas kontekst və davamlılıq sənədidir.

Əgər əvvəlki ChatGPT söhbətinin konteksti itərsə, yeni chat açılsa və ya layihəni başqa bir AI/komanda üzvü davam etdirsə, əvvəlcə bu fayl oxunmalıdır. Bu sənəd layihənin:

- məqsədini;
- araşdırma suallarını;
- scope-u;
- istifadə edilən metodologiyanı;
- data və evidence qaydalarını;
- hər oyun üçün görüləcək işi;
- oyunlararası müqayisə üsulunu;
- final deliverable-ları;
- rəhbərliyə təqdim ediləcək yekun report strukturunu;
- cari vəziyyəti və növbəti addımı

müəyyən edir.

Bu layihənin məqsədi **indidən oyun ideyası seçmək deyil**. Məqsəd ideya yaratmazdan və dəqiqləşdirməzdən əvvəl bazarda mövcud olan oxşar oyunları sistemli şəkildə öyrənmək, işləyən və işləməyən pattern-ləri tapmaq və komandanın sonrakı concept qərarlarını evidence ilə dəstəkləməkdir.

---

# 1. Yeni sessiyada konteksti necə bərpa etmək lazımdır?

Yeni AI sessiyası və ya yeni komanda üzvü bu ardıcıllıqla başlamalıdır:

1. **Bu faylı tam oxu:** `RESEARCH_MASTER_BRIEF.md`
2. **Data pipeline qaydalarını oxu:** `AGENTS.md`
3. **Repo-nun texniki istifadəsini oxu:** `README.md`
4. `analysis/` qovluğunda hazır olan araşdırmaları yoxla.
5. `data/reports/` və `data/processed/` altında hansı oyunların datasının hazır olduğunu yoxla.
6. Bu sənədin sonundakı **Cari vəziyyət** bölməsini oxu.
7. Hazır milestone tamamlanmadan özbaşına yeni oyun və ya yeni research istiqamətinə keçmə.

Sənədlərin rolu:

| Fayl / qovluq | Rolu |
|---|---|
| `RESEARCH_MASTER_BRIEF.md` | Layihənin məqsədi, metodologiyası, deliverable standartı və cari research istiqaməti |
| `AGENTS.md` | Kod, data collection, reproducibility və pipeline qaydaları |
| `README.md` | Texniki setup və command-lar |
| `data/raw/<game>/` | Mənbədən gələn dəyişdirilməmiş xam data |
| `data/processed/<game>/` | Təmizlənmiş və analysis-ready data |
| `data/reports/<game>/summary.md` | Avtomatik, deterministik statistik xülasə; interpretasiya etmir |
| `analysis/<game>/deep-research.md` | Həmin oyun üzrə qualitative + quantitative + external research interpretasiyası |
| `analysis/comparisons/` | Oxşar oyunların birbaşa müqayisəsi |
| `analysis/final/` | Rəhbərliyə və komanda qərarlarına təqdim ediləcək yekun sənədlər |

Əgər sənədlər arasında research məqsədi baxımından uyğunsuzluq varsa, bu master brief əsas götürülür. Kod/data integrity məsələlərində isə `AGENTS.md` qaydaları qorunmalıdır.

---

# 2. Layihənin əsas məqsədi

Araşdırdığımız sahə geniş mənada belədir:

> **Computer-interface / fictional OS / terminal / hacking / digital investigation / surveillance / found-device tipli oyunlar.**

Bu oyunlarda əsas gameplay klassik 3D dünya və ya action sistemi deyil. Oyunçu əsasən:

- terminal;
- fictional desktop/OS;
- browser;
- email;
- chat;
- phone;
- database;
- file system;
- social network;
- surveillance tools;
- network map;
- log və digər rəqəmsal interfeyslər

vasitəsilə oynayır.

Hazırkı əsas reference istiqamətlərimiz **Hacknet** və **Cyber Manhunt** tipli oyunlardır.

Pure programming puzzle oyunları — məsələn yalnız kod yazmaq və ya elektronika/programlaşdırma tapmacası üzərində qurulan oyunlar — bu araşdırmanın əsas scope-u deyil.

---

# 3. Biz hansı qərara hazırlaşırıq?

Bu research-in sonunda komanda yeni oyun ideyasını yaratmalı və ya mövcud ideyaları dəqiqləşdirməlidir.

Yəni araşdırmanın əsas biznes/product sualı belədir:

> **Bu geniş janrda hansı oyunçu fantasy-si, gameplay loop-u, UI modeli, narrative delivery üsulu və sistem dərinliyi işləyir; hansı yanaşmalar repetition, confusion, shallow gameplay, yanlış expectation və zəif market response yaradır; bizim komanda hansı opportunity-ləri daha ağıllı şəkildə hədəfləyə bilər?**

Araşdırmanın məqsədi “filan oyunu kopyalayaq” nəticəsinə gəlmək deyil.

Məqsəd:

1. bazarda artıq sınanmış yanaşmaları anlamaq;
2. təkrarlanan uğur pattern-lərini tapmaq;
3. təkrarlanan failure pattern-lərini tapmaq;
4. player expectation-ları anlamaq;
5. underserved / zəif həll olunmuş ehtiyacları tapmaq;
6. yeni concept üçün design constraint və opportunity-lər yaratmaq;
7. komandanın ideyaları yalnız zövqlə deyil, evidence ilə qiymətləndirməsinə imkan verməkdir.

---

# 4. Əsas research sualları

Hər oyun və bütün janr üzrə aşağıdakı suallara cavab axtarılır.

## 4.1. Attraction / purchase

- Oyun bir cümlədə hansı fantasy-ni satır?
- İnsan niyə store page-də buna maraq göstərir?
- Trailer, screenshot və description hansı vədi verir?
- Oyun hansı auditoriyanı cəlb edir?
- Hansı market positioning işləyir?
- “Real hacking”, “investigation”, “story”, “simulation”, “horror” və s. expectation-ları necə formalaşdırır?

## 4.2. First-session experience

- İlk 5, 15, 30 və 60 dəqiqədə oyunçu nə edir?
- Time-to-first-fun nə qədərdir?
- Onboarding necə işləyir?
- İlk saatlarda niyə insanlar qalır və ya çıxır?
- UI və command sistemi qorxuducudur, yoxsa fantasy-ni gücləndirir?

## 4.3. Core loop

- Oyunçu hər 2–5 dəqiqədə nə edir?
- Bu loop neçə dəfə təkrar olunur?
- Loop hansı yollarla dəyişir və dərinləşir?
- Tool-lar real seçim yaradır, yoxsa sadəcə doğru “açarı” seçməkdir?
- Oyunçu problem həll edir, yoxsa məlum sequence-ni təkrar edir?

## 4.4. Player fantasy və immersion

- Oyunçu özünü kim kimi hiss etməlidir?
- UI bu fantasy-ni necə yaradır?
- Audio, visual feedback, typing, network, files, messages və s. bu hissə necə xidmət edir?
- Realizm nə qədər lazımdır?
- “Kifayət qədər real” ilə “oynamaq üçün sadələşdirilmiş” arasındakı balans necə qurulub?

## 4.5. Information / investigation loop

- Məlumat necə tapılır?
- Oyunçu hansı məlumatın vacib olduğunu necə anlayır?
- Məlumatlar bir-biri ilə əlaqələndirilirmi?
- Oyunçu hipotez qururmu?
- Tapdığı məlumat sonrakı gameplay-i dəyişirmi?
- Discovery özü reward-durmu?

## 4.6. Narrative

- Story necə təqdim olunur?
- Email, file, log, chat, voice, cutscene və s. hansı rolu oynayır?
- Story gameplay-in içindədir, yoxsa gameplay-dən ayrıdır?
- Story repetition-ı gizlədir, yoxsa mechanic özü kifayət qədər güclüdür?
- Yadda qalan narrative/gameplay momentləri hansılardır?

## 4.7. Progression və pacing

- Yeni tool, mechanic, permission, story layer nə vaxt açılır?
- Oyun nə vaxt monotonlaşmağa başlayır?
- Difficulty necə artır?
- Progression real yeni decision yaradır, yoxsa sadəcə daha çox eyni action verir?
- Oyun uzunluğu core loop-a uyğundurmu?

## 4.8. Consequence və world reactivity

- Səhv qərarın real nəticəsi varmı?
- Dünya oyunçunun fəaliyyətinə reaksiya verirmi?
- Log silmək, trace, reputation, identity, hacking və s. sistemlər həqiqətən vacibdirmi?
- Oyunçunun qərarları yeni vəziyyət yaradırmı?

## 4.9. Friction və failure

- Ən çox negative review yazdıran səbəblər hansılardır?
- Repetition harada yaranır?
- UI friction varmı?
- Instructions qeyri-müəyyəndirmi?
- Realizm expectation-u pozulurmu?
- Bugs, crashes, softlock, save corruption və compatibility problemi varmı?
- Returning player oyuna qayıdanda nəyi unudur?

## 4.10. Long-term value

- Replayability varmı?
- Multiple path / endings varmı?
- Mod support varmı?
- Community content ömrü uzadırmı?
- Sequel-də nələr dəyişib və nəticə yaxşılaşıb/pisləşibmi?

---

# 5. Araşdırmanın əsas prinsipi

Bir oyunun yüksək Steam review faizi onun bütün dizayn qərarlarının yaxşı olduğunu göstərmir.

Eyni şəkildə aşağı satış estimate-i oyunun pis olduğunu avtomatik sübut etmir.

Ona görə research aşağıdakı source-ları **triangulate** etməlidir:

```text
market/performance data
+ Steam review dataset
+ qualitative player feedback
+ Reddit/community discussions
+ gameplay/walkthrough evidence
+ professional reviews
+ developer interviews/postmortems
+ store positioning
= daha etibarlı design/product nəticəsi
```

Heç bir mənbə təkbaşına final nəticə sayılmamalıdır.

---

# 6. Evidence səviyyələri

## Səviyyə A — birbaşa fakt

Məsələn:

- release date;
- qiymət;
- review sayı;
- Steam recommendation ratio;
- developer-in açıq dediyi məlumat;
- oyunda bir mechanic-in mövcud olması.

Bunlar mənbə ilə birbaşa göstərilə bilər.

## Səviyyə B — güclü pattern

Məsələn:

- müxtəlif Steam review sample-larında repetition şikayətinin təkrar görünməsi;
- Reddit və professional review-lərdə eyni problemin qeyd olunması;
- playtime segmentlərində aydın fərqin görünməsi.

Bu artıq sadə anecdote deyil, amma yenə də səbəb-nəticə kimi təqdim edilməməlidir.

## Səviyyə C — interpretasiya / hipotez

Məsələn:

> “Hacknet-in əsas commercial üstünlüyü realizm yox, hacker fantasy-sinin accessibility ilə verilməsidir.”

Bu evidence-dən çıxarılan product/design nəticəsidir.

Final report-da A, B və C bir-biri ilə qarışdırılmamalıdır.

---

# 7. Araşdırma scope-u və oyun seçimi

Məqsəd yalnız uğurlu oyunları öyrənmək deyil.

Ən dəyərli məlumat çox vaxt **oxşar konseptə sahib, amma fərqli nəticə göstərmiş oyunların müqayisəsindən** gəlir.

İlkin research universe:

## Güclü nəticə göstərmiş əsas reference-lər

- Hacknet
- Cyber Manhunt
- Cyber Manhunt 2
- The Operator
- Orwell: Keeping an Eye On You
- SIMULACRA
- Hypnospace Outlaw
- Welcome to the Game / Welcome to the Game II
- CaseCracker
- Emily is Away seriyası — hacking deyil, amma interface-as-world baxımından faydalıdır

## Orta / niche nəticə göstərmiş reference-lər

- Grey Hack
- NITE Team 4
- Song of Farca
- SIMULACRA 2
- CaseCracker2
- Scrutinized
- hackmud
- A Normal Lost Phone
- Another Lost Phone: Laura’s Story

## Zəif və ya underperform etmiş müqayisə nümunələri

- Midnight Protocol
- Mainlining
- Need to Know
- SIMULACRA 3
- NeuroNet: Mendax Proxy
- Keyword: A Spider’s Thread
- Tech Support: Error Unknown

Bu siyahı dəyişə bilər. Oyunların “successful / medium / weak” təsnifatı moral keyfiyyət hökmü deyil; market/review/traction kontekstində research grouping-dir və istifadə edilən metriklər hər report-da ayrıca göstərilməlidir.

---

# 8. Prioritet comparison qrupları

Ən çox informasiya verəcəyi gözlənilən müqayisələr:

## 8.1. Terminal/hacking

```text
Hacknet
vs
Midnight Protocol
vs
Mainlining
vs
NITE Team 4
```

Araşdırılan sual:

> Eyni “hacking/terminal” fantasy-si niyə bəzi oyunlarda böyük auditoriya tapır, digərlərində daha məhdud qalır?

## 8.2. Digital investigation

```text
Cyber Manhunt
vs
The Operator
vs
Orwell
vs
Song of Farca
vs
Need to Know
```

Araşdırılan sual:

> Information-search və investigation gameplay-i nə vaxt satisfying deduction olur, nə vaxt sadəcə text/data oxumağa çevrilir?

## 8.3. Found-device / phone interface

```text
SIMULACRA
vs
SIMULACRA 2
vs
SIMULACRA 3
```

Bu xüsusilə dəyərlidir, çünki eyni franchise daxilində nəticə fərqləri var.

Araşdırılan sual:

> Eyni interface/fantasy formulu sequel-lərdə necə dəyişib və hansı dəyişikliklər player response ilə əlaqəlidir?

---

# 9. Araşdırma metodu — hər oyun üçün addımlar

Hər oyun mümkün qədər eyni metodla araşdırılmalıdır ki, sonradan müqayisə mənalı olsun.

## Mərhələ 1 — Market və product snapshot

Topla:

- release date;
- developer/publisher;
- current/base price;
- Steam review sayı;
- positive/negative ratio;
- estimated owners/sales varsa;
- estimate mənbəyi;
- review volume;
- Steam tags;
- store description;
- screenshots/trailer positioning;
- DLC/sequel/mod support;
- təxmini oyun uzunluğu;
- platformlar.

Qayda:

> Owner/sales estimate heç vaxt exact sales kimi təqdim edilməməlidir.

Mümkün olduqda bir neçə estimate mənbəyi triangulate edilməlidir.

---

## Mərhələ 2 — Steam review dataset

Mümkün qədər bütün English public review-ləri topla.

Minimum metadata:

- review id;
- recommendation;
- review text;
- creation/update date;
- playtime at review;
- total playtime;
- helpful votes;
- purchase/free/refund flags;
- author review count və mövcud digər metadata.

Raw data immutable saxlanmalıdır.

Processed data raw data-dan yenidən yaradıla bilməlidir.

---

## Mərhələ 3 — Deterministik preprocessing

- normalization;
- deduplication;
- empty/very-short flag;
- playtime conversion;
- playtime segmentation;
- basic statistics;
- deterministic helpful/recent/low/high playtime samples;
- verification.

Bu mərhələdə interpretation edilməməlidir.

Output:

`data/reports/<game>/summary.md`

---

## Mərhələ 4 — Qualitative taxonomy discovery

Əvvəlcə review-lərin seçilmiş, müxtəlif sample-ları oxunmalıdır:

- helpful positive;
- helpful negative;
- recent positive;
- recent negative;
- low playtime;
- high playtime;
- lazım olduqda random/stratified sample.

Məqsəd əvvəlcədən hazırlanmış theme siyahısını kor-koranə tətbiq etmək yox, **oyunun öz datasından taxonomy çıxarmaqdır**.

İlkin ümumi theme nümunələri:

- player fantasy;
- immersion;
- UI;
- terminal;
- story;
- mystery;
- investigation;
- exploration;
- discovery;
- soundtrack;
- atmosphere;
- puzzle;
- difficulty;
- onboarding;
- repetition;
- depth;
- realism;
- technical accuracy;
- player agency;
- consequences;
- pacing;
- length;
- replayability;
- mod support;
- bugs;
- compatibility;
- ending.

Hər oyun üçün taxonomy genişlənə və ya dəyişə bilər.

---

## Mərhələ 5 — Aspect-based review analysis

Sadəcə review-un overall positive/negative olması kifayət deyil.

Məsələn:

> “Story əladır, amma hacking çox repetitive-dir.”

belə kodlanmalıdır:

```text
STORY       → positive
REPETITION  → negative
HACKING_LOOP → negative
```

Hər review:

- 0..N theme;
- hər theme üçün sentiment: positive / negative / mixed / neutral;
- lazım olsa confidence

daşıya bilər.

Mümkün qədər full dataset classification edilir.

Əgər full-dataset LLM classification texniki və ya cost səbəbindən mümkün deyilsə:

1. stratified sample yaradılır;
2. taxonomy həmin sample üzərində tətbiq edilir;
3. keyword-assisted genişlənmə aparılır;
4. nəticənin sample-based olduğu report-da açıq yazılır.

Heç vaxt sample nəticəsi full population faizi kimi təqdim edilmir.

---

## Mərhələ 6 — Classification keyfiyyət yoxlaması

Avtomatik classification kor-koranə qəbul edilməməlidir.

Minimum audit:

- positive və negative;
- low və high playtime;
- common və rare theme-lər

üzrə stratified manual yoxlama.

Səhv pattern görünərsə taxonomy/prompt düzəldilir və classification təkrarlanır.

Model/prompt versiyası mümkün olduqda saxlanmalıdır.

---

## Mərhələ 7 — Playtime və cohort analysis

Araşdır:

- 0–1h;
- 1–3h;
- 3–10h;
- 10h+;
- recent vs historical;
- helpful vs ordinary;
- refunded varsa;
- technical complaint vs design complaint.

Əsas suallar:

- erkən churn-a bənzər negative feedback nədir?
- uzun oynayanların şikayəti nədir?
- uzun oynayanlar hansı dəyərə görə qalır?
- illər keçdikcə complaint profile dəyişirmi?

Correlation səbəb-nəticə kimi təqdim edilməməlidir.

---

## Mərhələ 8 — Reddit və community research

Axtar:

- “worth playing”;
- “best part”;
- “worst part”;
- “repetitive”;
- “ending”;
- “what do you wish was different?”;
- “games like X”;
- “why did you stop playing?”;
- sequel comparison;
- technical audience reaction.

Xüsusilə yüksək dəyərli cümlələr:

- “I wish the game had…”
- “I loved X but hated Y…”
- “I stopped because…”
- “The part I still remember is…”

Community materialı Steam review-ləri ilə cross-check edilməlidir.

---

## Mərhələ 9 — Gameplay / walkthrough research

İstifadəçi bu research layihəsində oyunları özü almaq və oynamaq məcburiyyətində deyil.

Buna görə gameplay evidence ayrıca vacibdir.

İstifadə edilə bilər:

- first 30/60 minutes gameplay;
- full walkthrough;
- longplay;
- no-commentary gameplay;
- video transcript;
- retrospective/review.

Analiz ediləcək:

- ilk interaction;
- tutorial;
- time-to-first-fun;
- mechanic introduction timeline;
- neçə dəqiqədən bir yeni sistem açılır;
- interaction density;
- reading vs doing balansı;
- failure/retry;
- UI friction;
- memorable sequence-lər.

Video/transcript evidence review fikri ilə qarışdırılmamalıdır.

---

## Mərhələ 10 — Professional reviews

Professional review-lərin rolu:

- structure/pacing;
- game-design language;
- broader comparison;
- launch-period problemləri

haqqında əlavə context verməkdir.

Professional review oyunçu datasını əvəz etmir.

---

## Mərhələ 11 — Developer interview / postmortem

Mümkün olduqda araşdır:

- developer-in ilkin məqsədi;
- prototype necə yaranıb;
- target audience;
- hansı mechanic dəyişdirilib;
- development constraints;
- hansı feedback-ə reaksiya verilib;
- sequel/DLC-də niyə dəyişiklik edilib;
- launch nəticələri barədə açıqlama.

Ən dəyərli müqayisələrdən biri budur:

```text
developer intent
vs
player experienced outcome
```

---

## Mərhələ 12 — Store positioning analizi

Araşdır:

- oyun özünü hansı cümlə ilə satır;
- screenshot-lar nə göstərir;
- trailer-də hansı interaction prioritetdir;
- tags hansı expectation yaradır;
- “realistic”, “simulation”, “story-rich” və s. sözlər player expectation-a necə təsir edir.

Marketing expectation ilə actual gameplay arasında mismatch ayrıca qeyd olunmalıdır.

---

## Mərhələ 13 — Per-game synthesis

Bütün evidence birləşdirilərək:

`analysis/<game>/deep-research.md`

hazırlanır.

Bu sənəd sadəcə source summary deyil; **design/product interpretation** olmalıdır.

---

# 10. Hər oyun üçün deep-research report standartı

Hər `analysis/<game>/deep-research.md` mümkün qədər eyni professional strukturu izləməlidir.

## 1. Executive Summary

1–2 səhifəlik qısa nəticə:

- oyun nədir;
- nəyi düzgün edir;
- əsas problem nədir;
- niyə oyunçular oynayır;
- bizim üçün ən vacib 3–5 dərs.

Rəhbər yalnız bu bölməni oxusa belə əsas mənzərəni anlamalıdır.

## 2. Research Scope və Data Quality

- hansı dataset istifadə olunub;
- review sayı;
- tarix aralığı;
- external source-lar;
- limitations;
- classification coverage;
- confidence.

## 3. Product / Market Snapshot

- release;
- developer/publisher;
- price;
- traction göstəriciləri;
- review göstəriciləri;
- positioning;
- target audience hipotezi.

## 4. Oyunun mahiyyəti

- bir cümləlik description;
- player fantasy;
- game loop;
- primary interactions;
- progression.

## 5. Attraction: insanlar niyə başlayır?

- hook;
- fantasy;
- store promise;
- visual identity;
- novelty;
- audience motivation.

## 6. Retention: insanlar niyə davam edir?

- story;
- discovery;
- progression;
- mastery;
- tension;
- collection;
- curiosity;
- social/community content.

## 7. Onboarding və ilk sessiya

- first 5/15/30/60 min;
- friction;
- early negative themes;
- learning curve.

## 8. Core Loop və System Depth

- loop breakdown;
- decision density;
- mechanic variation;
- progression;
- repetition onset;
- meaningful choice.

## 9. UI/UX və Immersion

- interface-as-world;
- usability;
- authenticity;
- audio/visual feedback;
- technical-user expectation.

## 10. Narrative və Content Design

- delivery method;
- writing;
- characters;
- mystery;
- memorable moments;
- gameplay-story integration.

## 11. Player Feedback — Quantitative

Theme/aspect cədvəlləri:

- mention count;
- positive;
- negative;
- mixed;
- segmentlər;
- mümkün olduqda playtime fərqləri.

## 12. Player Feedback — Qualitative

Ən vacib pattern-lər:

- nə bəyənilir;
- nə bəyənilmir;
- representative examples;
- player language.

Uzun quote-lar yox, qısa evidence və paraphrase üstünlük təşkil etməlidir.

## 13. Technical / Compatibility Issues

Design complaint ilə texniki complaint qarışdırılmamalıdır.

## 14. Audience Segments

Məsələn:

- casual fantasy audience;
- investigation audience;
- technical/cyber audience;
- narrative audience.

Hansı audience üçün oyun işləyir və harada expectation mismatch yaranır?

## 15. Developer Intent vs Player Outcome

Developer məqsədi məlumdursa, real player feedback ilə müqayisə et.

## 16. Uğurun / zəifliyin izah hipotezləri

Burada correlation və causation ayrılmalıdır.

“Bunun səbəbi budur” əvəzinə evidence tam deyilsə:

> “Mövcud evidence bunu güclü izah hipotezi kimi göstərir.”

## 17. Bizim üçün design dərsləri

İki kateqoriya:

### Saxlamağa / öyrənməyə dəyər

### Qaçmalı olduğumuz risklər

## 18. Opportunity-lər

Oyun hansı problemi tam həll etməyib?

- daha yaxşı reactivity;
- deeper investigation;
- alternative paths;
- better onboarding;
- stronger consequence;
- better returning-player support;
- və s.

Bu bölmə hələ konkret yeni oyun ideyası yazmamalıdır.

## 19. Açıq suallar

Nəyi hələ bilmirik?

## 20. Sources və Evidence Notes

Daxili dataset və public sources.

---

# 11. Oyunlararası comparison report standartı

Path:

`analysis/comparisons/<game-a>-vs-<game-b>.md`

və ya 3–4 oyun üçün topic-based comparison.

Struktur:

## 1. Comparison Question

Nəyi anlamaq üçün müqayisə edirik?

## 2. Why These Games Are Comparable

Ortaq fantasy, mechanic, audience və ya interface.

## 3. Product/Market Snapshot

Eyni metriklərlə yan-yana.

## 4. Hook və Positioning

## 5. Core Loop

## 6. Onboarding

## 7. Depth və Repetition

## 8. Narrative Integration

## 9. UI/UX

## 10. Consequence / Reactivity

## 11. Player Feedback Differences

Eyni taxonomy mümkün qədər istifadə olunmalıdır.

## 12. Audience Expectation Differences

## 13. Why Outcomes May Have Diverged

Yalnız evidence-supported hipotezlər.

## 14. Transferable Lessons

Bu müqayisədən bizim layihəyə nə keçir?

---

# 12. Cross-game genre synthesis

Path:

`analysis/final/genre-synthesis.md`

Bu sənəd individual oyunları təkrar xülasə etməməlidir.

Məqsəd **oyunlar arasında təkrarlanan pattern-ləri** çıxarmaqdır.

Struktur:

## 1. Executive Summary

## 2. Genre / Category Definition

Bu bazarda əslində hansı subcategory-lər var?

Məsələn:

- terminal hacking;
- digital investigation;
- surveillance;
- found phone/device;
- fictional OS/internet;
- interface narrative.

## 3. Player Jobs / Fantasies

Oyunçu nə yaşamaq istəyir?

## 4. Purchase Drivers

Nə click və interest yaradır?

## 5. Satisfaction Drivers

Nə positive feedback yaradır?

## 6. Retention Drivers

Nə oyunçunu davam etdirməyə sövq edir?

## 7. Repeated Failure Modes

Məsələn:

- repetitive fake hacking;
- too much reading without interaction;
- no meaningful consequence;
- confusing onboarding;
- shallow “tool = key” systems;
- fake choice;
- weak ending;
- technical instability;
- marketing expectation mismatch.

Bu siyahı əvvəlcədən nəticə deyil; research ilə təsdiqlənməlidir.

## 8. Successful vs Weak Pattern Comparison

## 9. Audience Segments

## 10. UI/UX Principles

## 11. Narrative Principles

## 12. System/Gameplay Principles

## 13. Onboarding Principles

## 14. Content/Pacing Principles

## 15. Market Positioning Principles

## 16. Opportunity Map

Bazarda hansı boşluqlar var?

## 17. Risk Map

Yeni oyunda ən böyük risklər hansılardır?

## 18. Design Principles

Yalnız bir neçə oyunda yox, cross-game evidence ilə dəstəklənən qaydalar.

## 19. Open Questions

## 20. Evidence / Methodology Appendix

---

# 13. Rəhbərliyə təqdim ediləcək FINAL REPORT

Əsas professional deliverable:

`analysis/final/executive-genre-research-report.md`

Sonradan eyni sənəd PDF/slide deck formasına çevrilə bilər.

Bu sənəd research arxivindən fərqlənməlidir.

Məqsəd:

> rəhbərin və game/product komandasının 20–40 dəqiqə ərzində bazarı, oyunçu ehtiyaclarını, işləyən/işləməyən pattern-ləri və concept development üçün əsas constraint-ləri anlaya bilməsi.

Final report aşağıdakı struktura sahib olmalıdır.

---

## 1. Executive Summary

Maksimum yüksək informasiya sıxlığı.

Cavab verməlidir:

- nə araşdırdıq;
- nə öyrəndik;
- oyunçular bu janra niyə gəlir;
- əsas satisfaction drivers nədir;
- əsas failure modes nədir;
- ən böyük opportunity-lər hansıdır;
- yeni concept yaradarkən hansı 5–10 prinsip nəzərə alınmalıdır.

Bu bölmə öz-özünə oxuna bilən olmalıdır.

---

## 2. Research Objective və Scope

- biznes/product qərarı;
- araşdırılan oyun sayı;
- time period;
- source-lar;
- metod;
- nələr scope-dan kənardır.

---

## 3. Market Landscape

Vizual/cədvəl şəklində:

- subgenre-lər;
- əsas oyunlar;
- release ili;
- price;
- review volume;
- sentiment;
- owner/sales estimate range;
- primary fantasy;
- primary interface.

Məqsəd bazarın “xəritəsini” göstərməkdir.

---

## 4. Player Needs və Core Fantasies

Məsələn research təsdiqləyərsə:

- hacker kimi hiss etmək;
- gizli məlumat tapmaq;
- ağıllı problem solver olmaq;
- başqa insanların digital həyatını araşdırmaq;
- təhlükəli/illegal sistemlərə giriş hissi;
- məlumat parçalarını birləşdirmək;
- sirri açmaq;
- nəzarət/operator rolu.

Hər fantasy evidence və oyun nümunələri ilə göstərilməlidir.

---

## 5. What Makes These Games Work

Cross-game evidence əsasında:

- hook;
- immersion;
- information discovery;
- system depth;
- narrative integration;
- meaningful consequence;
- memorable moments;
- audio/visual feedback;
- progression;
- pacing.

Burada konkret oyunlardan nümunələr istifadə olunur.

---

## 6. Why These Games Fail or Underperform

Təkrarlanan failure pattern-lər.

Hər pattern üçün:

| Problem | Player impact | Evidence | Example games | Design implication |
|---|---|---|---|---|

---

## 7. Successful vs Underperforming Comparisons

Ən vacib pair/group nəticələrinin qısa executive versiyası.

Məsələn:

- Hacknet vs Midnight Protocol;
- Cyber Manhunt vs Mainlining;
- Orwell vs Need to Know;
- SIMULACRA vs SIMULACRA 3.

Məqsəd “winner seçmək” deyil; outcome divergence-i anlamaqdır.

---

## 8. Audience Segmentation

Hansı player type-lar var?

Hər segment üçün:

- motivation;
- tolerance;
- desired depth;
- preferred interface;
- risk;
- representative games.

---

## 9. Design Principles for Concept Development

Bu bölmə final research-in əsas məhsullarından biridir.

Hər prinsip:

```text
Principle
→ Evidence
→ Why it matters
→ What to do
→ What to avoid
```

formatında yazılmalıdır.

Bu prinsiplər yeni ideyanın design brief-i üçün input olacaq.

---

## 10. Opportunity Map

Hələ konkret oyun ideyası deyil.

Məsələn opportunity-lər belə kateqoriyalaşdırıla bilər:

- underserved fantasy;
- interaction opportunity;
- narrative opportunity;
- system-depth opportunity;
- multiplayer/social opportunity;
- content-production opportunity;
- creator/mod opportunity;
- market-positioning opportunity.

Hər opportunity üçün:

- hansı problemə cavab verir;
- hansı oyunlarda boşluq görünür;
- hansı auditoriyaya xidmət edir;
- implementation risk nədir.

---

## 11. Risk Register

Yeni concept üçün əvvəlcədən görünən risklər:

| Risk | Evidence | Impact | Early validation method |
|---|---|---|---|

Məsələn:

- novelty tez bitir;
- command loop repetitive olur;
- çox reading;
- false realism expectation;
- content production cost;
- onboarding complexity;
- weak replayability;
- UI friction.

---

## 12. Concept Evaluation Framework

Araşdırmadan sonra yaranacaq hər yeni oyun ideyası eyni rubric ilə yoxlanmalıdır.

Rubric final research nəticələrindən yaradılacaq.

Mümkün sahələr:

- fantasy clarity;
- hook;
- time-to-first-fun;
- mechanic depth;
- repetition resistance;
- narrative/gameplay integration;
- discovery;
- consequence;
- audience clarity;
- production feasibility;
- content scalability;
- differentiation;
- market positioning.

Bu mərhələdə rubric-in çəkiləri research bitmədən təsadüfi təyin edilməməlidir.

---

## 13. Recommended Next Product-Discovery Steps

Research bitəndən sonra:

1. opportunity-lərdən concept variants yarat;
2. concept-ləri evaluation framework ilə müqayisə et;
3. 2–3 yüksək potensiallı concept seç;
4. çox kiçik prototype qur;
5. target audience ilə test et;
6. first-session və fantasy validation apar;
7. yalnız bundan sonra böyük production qərarı ver.

---

## 14. Methodology və Limitations

Rəhbər üçün də görünən olmalıdır.

- Steam review bias;
- public-data limitations;
- owner estimate uncertainty;
- self-selection;
- review ≠ all players;
- correlation ≠ causation;
- game-playing yerine video/walkthrough evidence istifadə edilməsi;
- LLM classification limitations.

Bu bölmə report-un etibarlılığı üçün vacibdir.

---

## 15. Appendix

- game list;
- per-game report links;
- comparison report links;
- taxonomy;
- data dictionary;
- source list;
- əlavə cədvəllər.

---

# 14. Final report-un keyfiyyət standartı

Yekun sənədlər “ChatGPT cavabı” kimi görünməməlidir.

Onlar professional research deliverable kimi hazırlanmalıdır.

## Yazı standartı

- əsas dil Azərbaycan dili;
- zəruri industry terminləri English formada qala bilər;
- eyni fikir təkrar edilməməlidir;
- nəticə ilə evidence ayrılmalıdır;
- hər vacib nəticənin mənbəsi olmalıdır;
- çox uzun review quote-ları istifadə edilməməlidir;
- raw data əsas mətni boğmamalıdır;
- leadership üçün ən vacib məlumat yuxarıda olmalıdır;
- detail appendix və per-game report-lara ötürülməlidir.

## Vizual standart

Final mərhələdə report-da mümkün olduqda:

- comparison tables;
- theme charts;
- player-segment diagrams;
- opportunity map;
- risk matrix;
- market landscape;
- evidence heatmap

istifadə olunmalıdır.

## Confidence

Vacib nəticələr üçün lazım olduqda:

- High confidence;
- Medium confidence;
- Low confidence

işarəsi istifadə edilə bilər.

Confidence evidence breadth və consistency-yə əsaslanmalıdır, “model hissinə” yox.

---

# 15. Nə etməməliyik?

- Yalnız Steam positive ratio-ya baxıb nəticə çıxarma.
- Bir viral Reddit postunu ümumi player opinion kimi təqdim etmə.
- Owner estimate-i exact sales kimi göstərmə.
- “Successful game-də bu feature var, deməli feature uğurun səbəbidir” kimi səbəb-nəticə qurma.
- Əvvəlcədən sevdiyimiz ideyanı doğrulamaq üçün evidence seçmə.
- Bütün technical audience-i eyni hesab etmə.
- Negative review-ləri yalnız “oyunçunun başa düşməməsi” kimi dismiss etmə.
- Positive review-ləri də avtomatik design validation sayma.
- Oyunları yalnız feature checklist ilə müqayisə etmə; fantasy və player experience əsasdır.
- Research bitmədən konkret yeni concept-ə emosional bağlanma.

---

# 16. Araşdırmanın “Definition of Done” şərti

Research mərhələsi o zaman tamamlanmış sayılır ki:

1. əsas representative oyunların per-game deep research-i var;
2. ən vacib successful-vs-underperforming comparison-lar hazırdır;
3. recurring positive və negative theme-lər cross-game səviyyədə müəyyən edilib;
4. player fantasy və audience segmentləri aydındır;
5. market positioning pattern-ləri çıxarılıb;
6. design principles evidence ilə dəstəklənir;
7. opportunity map hazırlanıb;
8. risk register hazırlanıb;
9. concept evaluation framework hazırlanıb;
10. `analysis/final/executive-genre-research-report.md` professional şəkildə tamamlanıb.

Bundan sonra ideya generation/selection ayrıca mərhələ kimi başlayır.

---

# 17. Cari vəziyyət — 2026-10-02

## Tamamlanan

### Phase 2 theme-candidate infrastructure

Hacknet üçün full-corpus theme/aspect analizindən əvvəl audit edilə bilən deterministik retrieval mərhələsi əlavə olunub:

- `config/theme_taxonomy.yaml`
- `src/processors/theme_candidates.py`
- `src/reports/theme_candidate_report.py`

Bu mərhələ final semantic classification deyil. Məqsədi bütün review corpus-da theme namizədlərini tapmaq, playtime və overall recommendation paylanmasını ölçmək və hər theme üçün manual/LLM audit sample-ları yaratmaqdır.

Generated output-lar script lokalda işə salındıqdan sonra:

- `data/processed/hacknet/themes/candidates.jsonl`
- `data/processed/hacknet/themes/statistics.json`
- `data/processed/hacknet/themes/samples/<theme>_positive.csv`
- `data/processed/hacknet/themes/samples/<theme>_negative.csv`
- `data/processed/hacknet/themes/samples/<theme>_audit.csv`
- `data/reports/hacknet/theme-candidates.md`

olacaq.

Vahid command:

`python -m src.theme_pipeline --game hacknet`

`positive/negative` sample-lar helpful review-ləri prioritetləşdirir. `audit` sample-lar isə recommendation və playtime cohort-ları arasında deterministik balans yaradır ki, validation yalnız viral/helpful review-lərə bağlı qalmasın.


### Research infrastructure

Steam üçün reproducible research pipeline qurulub:

- metadata collection;
- paginated English Steam review collection;
- immutable raw pages;
- resume;
- normalization;
- deduplication;
- playtime segmentation;
- statistics;
- samples;
- deterministic report;
- integrity verification;
- cross-platform line-ending handling.

### Hacknet dataset

Hacknet Steam App ID: `365450`

Verified dataset:

- raw reviews: **11,773**
- unique reviews: **11,773**
- positive: **11,082**
- negative: **691**
- positive ratio: **94.13%**

Verification uğurla keçir.

Əsas data:

`data/processed/hacknet/`

Deterministik report:

`data/reports/hacknet/summary.md`

### Hacknet deep research

Hacknet üzrə əsas per-game research mərhələsi tamamlanıb:

- `analysis/hacknet/deep-research.md`
- `analysis/hacknet/theme-analysis.md`
- `config/aspect_taxonomy.yaml`

11,773 review üzrə full-corpus theme candidate scan və semantic audit aparılıb. Əsas evidence-backed nəticələr:

- hacker fantasy və immersion güclü satisfaction driver-ləridir;
- story, terminal və discovery eyni experience stack-in hissələri kimi işləyir;
- repetition əsas game-design riskidir;
- bugs/compatibility ayrıca böyük negative-review driver-dir;
- selective authenticity full realism-dən daha sağlam görünür;
- agency/consequence/world reactivity gələcək comparison-larda əsas opportunity suallarıdır.

Hacknet nəticələri artıq növbəti oyun üzərində test edilməlidir.

### Midnight Protocol deep research

Midnight Protocol üzrə əsas research mərhələsi tamamlanıb:

- verified Steam dataset: **301 English review**
- positive: **253**
- negative: **48**
- `analysis/midnight-protocol/theme-analysis.md`
- `analysis/midnight-protocol/deep-research.md`

Bütün 48 negative review semantic audit edilib. Əsas nəticələr:

- turn-based tactical model Hacknet-dən daha çox decision depth yaradır;
- RNG/fairness və retry/rollback əsas failure driver-ləridir;
- 1–3h cohort xüsusi risk nöqtəsidir;
- keyboard-only control həm immersion driver, həm UX friction-dır;
- choice/reputation Hacknet-də zəif olan player agency/consequence problemini xeyli yaxşı həll edir;
- selective authenticity prinsipi ikinci oyunda da təsdiqlənir.

### Hacknet vs Midnight Protocol

Comparison tamamlanıb:

`analysis/comparisons/hacknet-vs-midnight-protocol.md`

Əsas cross-game tension:

```text
Hacknet:
fast fantasy payoff
→ simple loop
→ repetition risk

Midnight Protocol:
deeper decision model
→ higher system/cognitive load
→ fairness + recovery + friction risk
```

### Cyber Manhunt deep research

Cyber Manhunt üzrə əsas research mərhələsi tamamlanıb:

- verified Steam dataset: **847 review**
- positive: **681**
- negative: **166**
- `analysis/cyber-manhunt/theme-analysis.md`
- `analysis/cyber-manhunt/deep-research.md`

Əsas nəticələr:

- 0–3h cohort çox yüksək risk daşıyır: 95 review-un 59-u negative-dir;
- LINEARITY_SCRIPTING ən güclü design risk-lərindən biridir;
- localization/writing text-heavy gameplay-ə birbaşa təsir edir;
- investigation fantasy güclüdür, amma exact clue/progression dependency deduction hissini zəiflədir;
- information-driven gameplay də repetition-dan immun deyil;
- full realism tələb olunmur, selective authenticity üçüncü oyunda da işləyir.

### Three-game comparison

Tamamlanıb:

`analysis/comparisons/hacknet-midnight-protocol-cyber-manhunt.md`

Üç depth modeli müqayisə olunur:

- Hacknet — execution depth;
- Midnight Protocol — tactical/system depth;
- Cyber Manhunt — information/deduction depth.

Əsas cross-game hypothesis:

> Depth feature sayından deyil, meaningful decision density-dən gəlir; repetition isə interface növündən yox, decision structure dəyişməyəndə yaranır.

Cyber Manhunt üçün v3 taxonomy ilə deterministik theme output-ların lokal pipeline vasitəsilə generasiyası hələ push edilməlidir.

---

# 18. Hazırkı növbəti addım

**Cyber Manhunt deterministic theme artifacts + növbəti digital-investigation target.**

Cyber Manhunt dataset və analysis tamamlanıb.

Əvvəl reproducibility artefaktlarını yarat:

1. `python -m src.theme_pipeline --game cyber-manhunt`
2. generated `data/processed/cyber-manhunt/themes/` və `data/reports/cyber-manhunt/theme-candidates.md` fayllarını push et.

Bundan sonra növbəti research target seçilməlidir.

Növbəti target seçilib: **The Operator**

- key: `the-operator`
- Steam App ID: `1771980`
- kickoff: `analysis/the-operator/research-kickoff.md`

The Operator Cyber Manhunt-un əsas research sualını test edəcək:

> scripted clue progression əvəzinə focused analysis tools və evidence comparison player-a daha real deduction hissi verirmi?

Bundan sonrakı yüksək informasiya dəyərli namizədlər:
- Mainlining — hacking + investigation + choice;
- Orwell — information selection + surveillance + ethics.

---

# 19. Research-in uzunmüddətli workflow-u

```text
Hacknet
  ↓
full theme/aspect analysis
  ↓
final per-game deep research
  ↓
Midnight Protocol
  ↓
same methodology
  ↓
Hacknet vs Midnight Protocol
  ↓
Cyber Manhunt
  ↓
Mainlining / The Operator
  ↓
comparison
  ↓
Orwell / Need to Know
  ↓
SIMULACRA series
  ↓
other representative games
  ↓
cross-game synthesis
  ↓
genre design principles
  ↓
opportunity map + risk map
  ↓
executive final report
  ↓
concept generation
  ↓
concept evaluation
  ↓
prototype validation
```

---

# 20. Son prinsip

Bu research-in uğuru çox data toplamaqda deyil.

Əsas nəticə bu olmalıdır:

> **Komanda yeni oyun ideyası haqqında danışanda artıq “məncə belə maraqlı olar” səviyyəsində yox, oyunçu davranışı, əvvəlki oyunların uğur və uğursuzluqları, market positioning və sistem dizaynı barədə evidence ilə danışa bilsin.**

Final report ideyanı bizim əvəzimizə yaratmayacaq.

O, **daha yaxşı ideya yaratmaq və pis qərarları erkən görmək üçün qərar infrastrukturu** yaradacaq.
