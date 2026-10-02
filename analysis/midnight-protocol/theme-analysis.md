# Midnight Protocol — Review Theme Analizi

## 1. Məqsəd

Bu sənəd Midnight Protocol üçün verified Steam review dataset-in full-corpus theme scan və semantic audit nəticələrini saxlayır.

Əsas məqsəd:

- oyunçuların ən çox hansı mövzuları müzakirə etdiyini ölçmək;
- hansı theme-lərin negative review-lərdə normadan daha çox toplandığını görmək;
- positive və negative review-lərdə eyni mechanic-in necə fərqli qəbul edildiyini ayırmaq;
- Midnight Protocol-un Hacknet-dən fərqli olaraq hansı yeni design trade-off-ları yaratdığını müəyyən etmək;
- sonrakı `Hacknet vs Midnight Protocol` comparison üçün evidence bazası hazırlamaqdır.

Bu sənəd review text-lərin sadə positive/negative xülasəsi deyil.

---

# 2. Dataset

Collection snapshot: **2026-10-02**

- Total English Steam reviews: **301**
- Unique reviews: **301**
- Positive: **253**
- Negative: **48**
- Overall positive ratio: **84.05%**
- Overall negative ratio: **15.95%**
- Empty reviews: **2**
- Very short reviews: **31**
- Average playtime at review: **15.19h**
- Median playtime at review: **11.70h**
- Positive review average playtime: **17.01h**
- Negative review average playtime: **5.59h**

Deterministik dataset:

- `data/processed/midnight-protocol/reviews.jsonl`
- `data/processed/midnight-protocol/statistics.json`
- `data/reports/midnight-protocol/summary.md`

---

# 3. Audit coverage

Midnight Protocol dataset Hacknet-dən xeyli kiçik olduğu üçün daha dərin semantic audit aparmaq mümkün olub.

Oxunmuş audit materialı:

- **bütün 48 negative review**
- **50 ən helpful positive review**
- **50 low-playtime review**
- **25 ən yeni positive review**
- developer interview
- Steam store positioning
- professional reviews

Sample-lar arasında overlap var. Bunlar 173 distinct review demək deyil.

Bu audit full 253 positive review-un manual classification-ı deyil, amma bütün negative population-un oxunması Midnight Protocol-un failure pattern-ləri üçün xüsusilə güclü evidence verir.

---

# 4. Full-corpus candidate scan

Expanded candidate taxonomy ilə:

- total reviews: **301**
- ən azı bir theme candidate-i tutulan reviews: **226**
- coverage: **75.08%**

Taxonomy:

`config/theme_taxonomy.yaml`

Semantic taxonomy:

`config/aspect_taxonomy.yaml`

Candidate retrieval final semantic classification deyil. Theme-in “negative review payı” həmin theme keyword/pattern-i olan review-lərin neçə faizinin overall Steam recommendation-ının negative olduğunu göstərir.

Dataset baseline negative ratio:

**15.95%**

---

# 5. Theme statistikası

| Theme | Mentions | Dataset payı | Negative review payı | Baseline-a nisbət |
|---|---:|---:|---:|---:|
| STORY_NARRATIVE | 136 | 45.18% | 11.03% | 0.69× |
| DEPTH_CHALLENGE | 112 | 37.21% | 21.43% | 1.34× |
| LOADOUT_BUILD | 82 | 27.24% | 15.85% | 0.99× |
| TACTICAL_TURN_BASED | 73 | 24.25% | 16.44% | 1.03× |
| TERMINAL_UI | 57 | 18.94% | 24.56% | **1.54×** |
| UI_USABILITY | 41 | 13.62% | 19.51% | 1.22× |
| IMMERSION | 40 | 13.29% | 7.50% | **0.47×** |
| SOUND_AUDIO | 40 | 13.29% | 7.50% | **0.47×** |
| RNG_FAIRNESS | 36 | 11.96% | **36.11%** | **2.26×** |
| CHOICE_REPUTATION | 29 | 9.63% | 6.90% | **0.43×** |
| KEYBOARD_ONLY | 28 | 9.30% | 14.29% | 0.90× |
| INVESTIGATION_DISCOVERY | 20 | 6.64% | 5.00% | **0.31×** |
| RETRY_ROLLBACK | 20 | 6.64% | **35.00%** | **2.19×** |
| REPETITION | 19 | 6.31% | **36.84%** | **2.31×** |
| ONBOARDING_CLARITY | 18 | 5.98% | 16.67% | 1.05× |
| REALISM_ACCURACY | 17 | 5.65% | 5.88% | 0.37× |
| URGENCY_TRACE | 16 | 5.32% | **50.00%** | **3.14×** |
| MOD_REPLAYABILITY | 14 | 4.65% | 21.43% | 1.34× |
| BUGS_COMPATIBILITY | 12 | 3.99% | **33.33%** | **2.09×** |
| PLAYER_AGENCY | 9 | 2.99% | 11.11% | 0.70× |
| PACING_WAITING | 9 | 2.99% | 11.11% | 0.70× |
| HACKER_FANTASY | 8 | 2.66% | 0.00% | 0× |
| WORLD_REACTIVITY | 8 | 2.66% | 0.00% | 0× |
| LENGTH_CONTENT | 7 | 2.33% | 0.00% | 0× |

Rəqəmlər theme prevalence və negative concentration üçün **retrieval siqnalıdır**, aspect sentiment faizi deyil.

---

# 6. Playtime cohort-ları

## 6.1. Overall review nəticəsi

| Playtime | Reviews | Positive | Negative | Positive ratio |
|---|---:|---:|---:|---:|
| 0–1h | 21 | 16 | 5 | 76.19% |
| 1–3h | 45 | 28 | 17 | **62.22%** |
| 3–10h | 79 | 60 | 19 | 75.95% |
| 10h+ | 156 | 149 | 7 | **95.51%** |

Midnight Protocol-da ən zəif review cohort-u **1–3 saat** aralığıdır.

Bu Hacknet-dən fərqli pattern-dir. Hacknet-də ən aşağı satisfaction 0–1h cohort-da idi və sonra davamlı yüksəlirdi.

Midnight Protocol-da isə:

```text
0–1h   → 76.2%
1–3h   → 62.2%
3–10h  → 75.9%
10h+   → 95.5%
```

Bu, tutorial-dan sonra ilk dəfə sistemlərin tam interaction-a girdiyi hissədə xüsusi friction olduğunu göstərən güclü siqnaldır.

Causation sübut olunmur; sevən oyunçuların daha uzun oynaması selection bias yaradır.

---

# 7. 1–3 saatlıq “danger zone”

Semantic audit həmin dip üçün mümkün səbəbləri göstərir.

1–3 saat aralığındakı negative review-lərdə tez-tez:

- RNG;
- trace;
- rollback/retry;
- loadout-un necə qurulacağını anlamamaq;
- required tool slot-ların çox tez dolması;
- terminal/keyboard friction;
- tutorial-dan sonra difficulty spike;
- “hacking” gözləntisi ilə “board game” reallığı arasındakı fərq

görünür.

Theme cohort-ları bunu dəstəkləyir:

### RNG_FAIRNESS

1–3h cohort:
- 9 mention
- 7 negative
- **77.8% negative**

### RETRY_ROLLBACK

1–3h cohort:
- 3 mention
- **3 negative**

### REPETITION

1–3h cohort:
- 6 mention
- 4 negative
- **66.7% negative**

### URGENCY_TRACE

1–3h cohort:
- 2 mention
- **2 negative**

### TERMINAL_UI

1–3h cohort:
- 12 mention
- 5 negative
- **41.7% negative**

### TACTICAL_TURN_BASED

1–3h cohort:
- 11 mention
- 5 negative
- **45.5% negative**

Bu pattern göstərir ki, Midnight Protocol-un problem nöqtəsi “ilk ekran qorxuducudur”dan daha çox:

> **tutorial sonrası player model-in core systems-lə toqquşduğu mərhələdir.**

**Confidence: High**

---

# 8. Əsas güc: hacker fantasy dərin tactical sistemlə birləşir

Explicit HACKER_FANTASY candidate sayı cəmi 8-dir, amma hamısı positive review-dur.

Regex çox dar olduğu üçün bu 2.66% real prevalence kimi qəbul edilmir.

Semantic audit-də fantasy daha geniş formada görünür:

- “feel like a hacker”;
- keyboard-only typing;
- futuristic network map;
- terminal;
- deck/program hazırlamaq;
- trace altında hərəkət;
- black/white/grey hat reputation;
- information oğurlamaq və qərar vermək.

Recent 2025–2026 review-lər də bu hissi hələ əsas value proposition kimi göstərir.

Developer intent də bunu birbaşa təsdiqləyir: keyboard-only input oyunun immersion üçün əsas elementlərindən biri kimi nəzərdə tutulub.

**Confidence: High**

---

# 9. Turn-based sistem: Hacknet probleminə real cavabdır, amma tam həll deyil

TACTICAL_TURN_BASED:

- 73 mentions
- 24.25% dataset share
- negative ratio 16.44% — dataset baseline-a çox yaxın.

Bu özü nə aydın positive, nə də aydın negative theme-dir.

Semantic audit göstərir ki, iki player qrupu var.

## Müsbət qəbul

Turn-based sistem:

- speed requirement-i azaldır;
- planlama imkanı verir;
- “hacking = sürətli typing” modelindən çıxır;
- network-u tactical puzzle-a çevirir;
- action economy yaradır.

Bəzi review-lər turn-based design-i məhz Hacknet/Uplink tipli real-time stress-ə qarşı üstünlük hesab edir.

## Mənfi qəbul

Bəzi oyunçular isə:

- “hacking yox, chess/board game” kimi görür;
- typing-in turn-based sistemdə funksional mənasını zəif sayır;
- SysOp sisteminin oyunun genre expectation-ını dəyişdirdiyini düşünür;
- action economy-ni həddindən artıq məhdud hiss edir.

Əsas nəticə:

> **Midnight Protocol mechanical depth-i artırıb, amma bunun müqabilində genre expectation riskini böyüdüb.**

**Confidence: High**

---

# 10. RNG/fairness — ən ciddi design problemi

RNG_FAIRNESS:

- 36 mentions
- 11.96% dataset share
- 13 negative review
- **36.11% negative**
- baseline-dan **2.26×** yüksək negative concentration.

Bu sadəcə negative reviewer complaint-i deyil.

Ən helpful positive review belə RNG və rollback-u oyunun ən ciddi qüsuru kimi təsvir edir.

Semantic audit-də əsas problem random elementin mövcudluğu deyil.

Problem oyunçunun failure-i öz qərarı ilə əlaqələndirə bilməməsidir.

Negative feedback-də:

- SysOp gözlənilməz istiqamətdə hərəkət edir;
- trace random artır;
- hidden ICE ilə toqquşma build-i dağıdır;
- cloak percentage nəticəsi uğuru dəyişir;
- wrong loadout əvvəlcədən kifayət qədər görünmür.

Belə olduqda:

```text
failure
→ "səhv qərar verdim"
```

əvəzinə:

```text
failure
→ "pis roll gəldi"
```

hissi yarana bilir.

Bu isə mastery loop-u zəiflədir.

### Design prinsipi

> **Randomness oyunçuya yeni vəziyyət təqdim edə bilər; amma uğur/uduzma əsasən oyunçunun izah edə bildiyi qərarlardan gəlməlidir.**

**Confidence: High**

---

# 11. Retry/rollback problemi RNG-ni böyüdür

RETRY_ROLLBACK:

- 20 mentions
- 35% negative
- baseline-dan **2.19×** yüksək.

RNG təkbaşına bu qədər zərərli olmazdı, əgər failure recovery daha yaxşı olsaydı.

Review-lərdə:

- rollback;
- mission restart;
- failed mission-in permanently bağlanması;
- loadout-u dəyişib re-plan edə bilməmək;
- manual save olmaması;
- game-i bağlayıb açmaqla faktiki save-scumming

kimi problemlər görünür.

Bu sistemik zəncir yaradır:

```text
incomplete information
→ wrong loadout / bad RNG
→ mission failure
→ weak recovery
→ repetition
→ frustration
```

Bu, Midnight Protocol üçün ən vacib design nəticələrindən biridir.

**Confidence: High**

---

# 12. Trace/turn cap — tension və experimentation arasında konflikt

URGENCY_TRACE:

- 16 mentions
- 8 negative
- **50% negative**
- baseline-dan **3.14×** yüksək negative concentration.

Sample sayı böyük deyil, amma bütün negative population-un audit-i pattern-i təsdiqləyir.

Bəzi oyunçular trace-i:

- pressure;
- tension;
- mission rhythm

kimi bəyənir.

Digərləri üçün isə:

- map-i araşdırmağa;
- optional data toplamağa;
- stealth plan qurmağa;
- fərqli tool test etməyə

mane olur.

Xüsusilə turn-cap kimi əlavə limit gələndə oyunçu bunu:

> “öz planımı qururam”

deyil,

> “designer-in istədiyi templə gedirəm”

kimi hiss edə bilər.

### Design prinsipi

> **Urgency exploration və strategy-ni öldürəcək qədər sərt olmamalıdır; xüsusilə investigation/discovery oyunun dəyər hissəsidirsə.**

**Confidence: High**

---

# 13. Keyboard-only — eyni anda əsas üstünlük və əsas UX riski

KEYBOARD_ONLY:

- 28 explicit mentions
- negative ratio 14.29% — dataset baseline-a yaxın.

Bu rəqəm mechanic-in polarizing olduğunu gizlədir.

Semantic audit çox aydın iki istiqamət göstərir.

## Müsbət

- immersion artır;
- oyunçu fiziki olaraq “hacker” roluna girir;
- typing command player intent-i thematic şəkildə ifadə edir;
- mouse-dan fərqli distinctive product identity yaradır.

## Mənfi

- mouse ilə bir klik olacaq action uzun command-a çevrilir;
- typo;
- help discoverability;
- node name yadda saxlamaq;
- slow repeated input;
- keyboard-only olmasına baxmayaraq UI-nin vizual GUI kimi görünməsi

bəzi oyunçular üçün artificial friction yaradır.

Developer özü də keyboard-only UI-nin discoverability-ni azaltdığını etiraf edir.

### Əsas nəticə

> **Input gimmick özünü yalnız fantasy ilə yox, interaction efficiency ilə də doğrultmalıdır.**

Əgər keyboard daha immersive, amma ardıcıl olaraq daha yavaşdırsa, novelty tükənəndən sonra friction görünür.

**Confidence: High**

---

# 14. Terminal/technical authenticity Hacknet-dən fərqli işləyir

TERMINAL_UI:

- 57 mentions
- 24.56% negative
- baseline-dan **1.54×** yüksək.

REALISM_ACCURACY:

- 17 mentions
- yalnız 5.88% negative.

Bu paradoks görünür:

- oyunçular ümumiyyətlə real hacking simulator tələb etmir;
- amma command-line görünüşü müəyyən usability və authenticity expectation yaradır.

Positive review-lərdə çox aydın fikir var:

> “realistic deyil və məhz buna görə yaxşı oyundur.”

Developer də “fun game first, hacking theme second” yanaşmasını açıq deyir.

Bu Hacknet-də tapdığımız selective authenticity prinsipini ikinci oyunda da təsdiqləyir.

Cross-game hypothesis artıq daha güclüdür:

> **Bu janrda full realism əsas tələb deyil; oyunçunun tanıdığı texniki işarələr və coherent fiction kifayət qədər authenticity yarada bilər.**

**Confidence: High**

---

# 15. Loadout/build sistemi real dərinlik verir, amma dominant build problemi var

LOADOUT_BUILD:

- 82 mentions
- 27.24% dataset share
- positive/negative ratio təxminən overall baseline ilə eynidir.

Bu theme-in özü polarizing deyil.

Semantic audit daha faydalıdır.

## Güclü tərəf

Positive review-lərdə:

- stealth;
- aggression;
- bypass;
- hardware;
- program combinations;
- resource/slice management

real build choice kimi təriflənir.

Recent review-lərdə də “başqa approach üçün deck-i dəyişmək” əsas satisfaction driver kimi qalır.

## Problem

Negative və mixed review-lərdə:

- bəzi basic tool-lar demək olar məcburidir;
- 5 slot çox tez dolur;
- mission requirements qabaqcadan aydın deyil;
- bəzi dominant configurations çox mission-da işləyir;
- çox sayda tool olsa da effective choice azalır.

Bu çox vacib distinction-dır:

> **Feature count ≠ decision depth.**

10 tool seçimi verib 3-ü mandatory, 2-si dominantdırsa real choice aşağıdır.

**Confidence: High**

---

# 16. Choice/reputation sistemi oyunun ən güclü fərqləndiricilərindəndir

CHOICE_REPUTATION:

- 29 mentions
- 93.10% overall positive
- average playtime: **25.17h**

Semantic audit və recent reviews:

- black/white/grey hat;
- bank hesabına toxunmaq/tunmamaq;
- mission nəticəsinin reputation-a təsiri;
- side mission açılması/bağlanması;
- endings;
- morally ambiguous qərarlar

kimi elementləri yüksək qiymətləndirir.

Bu Hacknet-dən əsas üstünlüklərdən biridir.

Hacknet əsasən hacker fantasy və story verir.

Midnight Protocol buna əlavə edir:

> **“mən necə hackerəm?”**

sualını.

Bu yalnız role-playing flavor deyil; programs, missions və narrative path ilə əlaqələnəndə gameplay identity yaradır.

### Risk

Bəzi review-lər consequence-ların həddindən artıq sərt/permanent olduğunu deyir.

Deməli:

> meaningful consequence lazımdır, amma player-in qərarı anlamadan irreversibly cəzalandırılması agency-ni zəiflədə bilər.

**Confidence: High**

---

# 17. Story oyunun əsas retention sistemidir

STORY_NARRATIVE:

- 136 mentions
- dataset-in **45.18%**-i
- negative ratio yalnız 11.03%.

Bu, ən geniş theme-dir.

10h+ cohort-da STORY candidate-i olan:

- 100 review;
- yalnız 4 negative.

Recent positive review-lərdə story hələ də əsas praise səbəbidir.

Co-occurrence:

- STORY + DEPTH_CHALLENGE: 71
- STORY + LOADOUT_BUILD: 63
- STORY + TACTICAL_TURN_BASED: 52
- STORY + TERMINAL_UI: 39
- STORY + IMMERSION: 31
- STORY + SOUND: 30
- STORY + CHOICE_REPUTATION: 24

Bu göstərir ki, story gameplay-dən ayrı layer deyil.

> **Narrative tactical gameplay, loadout və choice systems-ə context verir.**

Negative review-lərin bir hissəsi gameplay-dən bezsə belə story-ni davam etmək üçün səbəb kimi qeyd edir.

**Confidence: High**

---

# 18. Immersion və audio güclü, davamlı satisfaction driver-ləridir

IMMERSION və SOUND_AUDIO:

- hər biri 40 mentions
- hər ikisinin negative ratio-su 7.5%
- baseline-dan təxminən yarı qədər negative concentration.

Praise:

- minimalist cyberpunk UI;
- animation;
- node visualization;
- typing;
- music;
- feedback;
- story presentation.

Professional review də presentation və interface-i əsas güclərdən sayır, soundtrack üçün isə variety-ni zəif nöqtə kimi qeyd edir.

Bu Hacknet ilə başqa ortaq principle-dir:

> interface-heavy oyunda audio/visual presentation sadəcə polish deyil, fantasy-nin mexaniki hissəsidir.

**Confidence: High**

---

# 19. Investigation/discovery az görünür, amma çox müsbətdir

INVESTIGATION_DISCOVERY:

- 20 mentions
- 19 positive
- 1 negative.

Review-lərdə:

- side clues;
- optional data;
- intranet;
- hidden secrets;
- real-world-style extra investigation;
- easter eggs

yüksək dəyər yaradır.

Developer də fourth-wall secrets və curiosity-ni xüsusi design məqsədi kimi qeyd edir.

Lakin bu sistem Hacknet-də olduğu qədər core loop-un mərkəzində görünmür.

Midnight Protocol daha çox:

> tactical network puzzle + narrative RPG

kimidir.

Bu, Hacknet comparison-da vacibdir.

**Confidence: Medium-High**

---

# 20. Repetition tam həll olunmayıb

REPETITION:

- 19 mentions
- **36.84% negative**
- baseline-dan **2.31×** yüksək.

Midnight Protocol Hacknet-dən daha çox tactical depth verir, amma repetition yox olmur.

Complaint forması dəyişir.

Hacknet:

```text
same command sequence
→ same port tools
→ same breach
```

Midnight Protocol:

```text
move
→ sniff
→ break ICE
→ manage trace
→ wait/end turn
→ repeat
```

Bəzi long-play positive review-lər isə mission variety, bosses və special mechanics sayəsində bu repetition-ın qırıldığını deyir.

Nəticə:

> **Depth repetition riskini azalda bilər, amma fundamental action grammar çox dəyişmirsə onu tam aradan qaldırmır.**

**Confidence: High**

---

# 21. “More depth” avtomatik olaraq “better” deyil

Midnight Protocol Hacknet-in shallow loop probleminə cavab olaraq daha çox sistem təqdim edir:

- action economy;
- loadout;
- resource slicing;
- ICE;
- SysOps;
- trace;
- reputation;
- mission choices;
- hardware/program progression.

Buna baxmayaraq 1–3h cohort-da satisfaction düşür.

Bu bizim gələcək oyun üçün ən vacib dərslərdən biridir:

> **Sistem sayı deyil, oyunçunun hər anda etdiyi mənalı qərarların keyfiyyəti vacibdir.**

Depth:

- izah edilə bilən;
- öyrənilə bilən;
- qabaqcadan planlana bilən;
- failure-dan feedback verən

olmalıdır.

Əks halda depth complexity/friction kimi hiss olunur.

---

# 22. Developer intent vs player outcome

## Intent: keyboard immersion

Developer:

- keyboard-u immersion üçün “heart of the game” sayır;
- discoverability downside-ını qəbul edir.

Player outcome:

- positive: çox güclü fantasy və distinctive identity;
- negative: inefficient UI və repetitive typing.

**Intent achieved, trade-off realdır.**

---

## Intent: fun over realism

Developer:

- real hacking simulyasiyası məqsəd olmayıb;
- fun game first.

Player outcome:

- positive review-lərin çoxu bunu qəbul edir;
- technical accuracy complaint Hacknet-dən daha az dominant görünür.

**Intent böyük ölçüdə achieved.**

---

## Intent: accessible turn-based strategy

Developer:

- real-time prototipi stressli və əyləncəsiz sayıb turn-based-a keçib.

Player outcome:

- bir qrup planlama və stress-in azalmasını çox sevir;
- digər qrup turn-based/chess modelini hacking expectation-a uyğun görmür;
- RNG və trace yeni fairness problem yaradır.

**Stress problemi azaldılıb, amma failure/fairness problemi yaranıb.**

---

## Intent: simple action language, complex appearance

Developer:

- 2-action board-game grammar;
- command-line presentation ilə complex feel.

Player outcome:

- immersion işləyir;
- bəzi technical/UX-oriented oyunçular bu layer-i “unnecessary typing” kimi görür.

**Perceived complexity uğurludur, interaction efficiency audience-dan asılıdır.**

---

# 23. Midnight Protocol-un ən güclü design nailiyyətləri

1. **Hacker fantasy-ni tactical decision-making ilə birləşdirir.**
2. **Keyboard-only input güclü product identity yaradır.**
3. **Story + choice + reputation gameplay context-i artırır.**
4. **Loadout/build sistemi Hacknet-dən daha çox agency verir.**
5. **Turn-based sistem non-speed-based hacking fantasy üçün alternativ yaradır.**
6. **Presentation və immersion yüksək səviyyədədir.**
7. **Selective authenticity real simulation olmadan işləyir.**
8. **Side content və moral choices “hacker identity” yaradır.**
9. **Recent reviews göstərir ki, core strengths uzun müddət aktual qalıb.**

---

# 24. Əsas failure pattern-lər

1. **RNG failure-i player skill-dən ayıra bilir.**
2. **Retry/rollback/replanning modeli failure-i daha ağrılı edir.**
3. **Trace/turn cap experimentation ilə toqquşa bilir.**
4. **Keyboard-only input bəzi action-ları lazımsız yavaşladır.**
5. **Tutorial sonrası 1–3h mərhələsində complexity spike görünür.**
6. **Loadout choices bəzən mandatory slots və hidden mission needs səbəbilə azalır.**
7. **Turn-based board-game identity bəzi hacking-game expectation-ları ilə toqquşur.**
8. **Core action grammar yenə repetition yarada bilir.**
9. **Bəzi consequence-lar həddindən artıq permanent görünür.**
10. **Bugs/softlock/save issues az volume-da olsa da negative recommendation-a güclü təsir edir.**

---

# 25. Bizim gələcək oyun üçün design dərsləri

## 25.1. Tactical depth qur, amma failure explainable olsun

Oyunçu bilməlidir:

- niyə uduzdu;
- hansı qərar səhv idi;
- növbəti dəfə nəyi dəyişə bilər.

“Pis roll gəldi” əsas feedback olmamalıdır.

---

## 25.2. Mission öncəsi planning üçün kifayət qədər intel ver

Loadout meaningful olacaqsa:

> oyunçu nəyə hazırlaşdığını müəyyən dərəcədə bilməlidir.

Tam məlumat lazım deyil.

Amma blind build seçimləri skill test yox, trial-and-error yarada bilər.

---

## 25.3. Failure recovery design-in bir hissəsidir

Retry:

- tez;
- aydın;
- re-plan etməyə imkan verən;
- optional branch-ləri əsassız permanent bağlamayan

olmalıdır.

---

## 25.4. Urgency ilə curiosity-ni balanslaşdır

Əgər gameplay:

- optional files;
- hidden data;
- investigation;
- exploration

üzərində də qurulursa, timer/trace onları faktiki cəzalandırmamalıdır.

---

## 25.5. Input fantasy-ni dəstəkləsin, əməliyyatı yavaşlatmasın

Typing:

- hacker fantasy üçün güclüdür.

Amma tez-tez təkrarlanan low-value action üçün:

- autocomplete;
- aliases;
- context-sensitive suggestions;
- history;
- shortcuts

olmalıdır.

---

## 25.6. More systems əvəzinə better decision density

Hər 30–60 saniyədə oyunçu:

> “nə edim?”

deyə düşünməlidir,

> “hansı syntax-i yazmalıyam?”

deyil.

---

## 25.7. Choice + consequence çox güclü opportunity-dir

Midnight Protocol Hacknet-dən burada daha irəli gedir.

Bizim gələcək oyun üçün:

```text
information
→ decision
→ consequence
→ changed world/options
```

loop-u çox güclü ola bilər.

---

# 26. Confidence matrix

| Nəticə | Confidence |
|---|---|
| RNG/fairness əsas failure driver-dir | High |
| Retry/recovery RNG problemini böyüdür | High |
| 1–3h xüsusi risk cohort-udur | High |
| Story əsas retention driver-dir | High |
| Keyboard-only güclü immersion + UX trade-off yaradır | High |
| Turn-based sistem real-time speed requirement-i uğurla azaldır | High |
| Hacker fantasy güclü value proposition-dır | High |
| Loadout sistemi real agency yaradır, amma mandatory/dominant build riski var | High |
| Choice/reputation əsas fərqləndiricidir | High |
| Repetition daha dərin sistemə baxmayaraq qalır | High |
| Selective authenticity cross-game principle-dir | High |
| Investigation/discovery daha da dərinləşdirilə bilən opportunity-dir | Medium-High |
| Mod/Workshop long-tail böyük driver-dir | Low-Medium — dataset evidence azdır |

---

# 27. Məhdudiyyətlər

- 301 review bütün player population deyil.
- Steam review self-selection daşıyır.
- Positive/negative recommendation aspect sentiment deyil.
- Candidate regex semantic classifier deyil.
- Positive semantic audit bütün 253 positive review-u əhatə etmir.
- Negative population-un hamısı oxunsa da, qısa/zarafat review-lər analytical value daşımaya bilər.
- Playtime correlation causation deyil.
- Steam store display review sayı ilə API snapshot sayı fərqlənə bilər; daxili analiz üçün verified API snapshot istifadə olunur.
- Bəzi negative complaint-lər patch-lərlə sonradan qismən dəyişmiş ola bilər; review tarixi nəzərə alınmalıdır.

---

# 28. Mənbələr

## Daxili

- `data/processed/midnight-protocol/reviews.jsonl`
- `data/processed/midnight-protocol/statistics.json`
- `data/reports/midnight-protocol/summary.md`
- `data/processed/midnight-protocol/samples/helpful_negative.csv`
- `data/processed/midnight-protocol/samples/helpful_positive.csv`
- `data/processed/midnight-protocol/samples/low_playtime.csv`
- `data/processed/midnight-protocol/samples/recent_positive.csv`

## Xarici

**Steam Store**  
https://store.steampowered.com/app/1162700/

**Game Developer — Road to IGF 2022 / Sam Agten interview**  
https://www.gamedeveloper.com/design/hacking-answers-tactical-narrative-game-midnight-protocol

**Quarter to Three — Tom Chick review**  
https://www.quartertothree.com/fp/2022/01/16/midnight-protocol-hacks-into-the-sweet-spot-between-storytelling-and-strategy/

**Softpedia review**  
https://www.softpedia.com/reviews/games/pc/midnight-protocol-review-534571.shtml

---

# 29. Status

**Mərhələ:** Midnight Protocol full-corpus review analysis — tamamlanıb  
**Dataset:** 301 verified English Steam review  
**Negative semantic audit:** 48/48 negative reviews  
**Positive audit:** helpful + low-playtime + recent cohorts  
**Növbəti:** `analysis/midnight-protocol/deep-research.md` və sonra Hacknet vs Midnight Protocol comparison.
