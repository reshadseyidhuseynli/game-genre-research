# Midnight Protocol — rəy mövzu Analizi

## 1. Məqsəd

Bu sənəd Midnight Protocol üçün verified Steam rəy məlumat toplusu-in full-corpus mövzu yoxlama və məna yönümlü yoxlama nəticələrini saxlayır.

Əsas məqsəd:

- oyunçuların ən çox hansı mövzuları müzakirə etdiyini ölçmək;
- hansı mövzu-lərin mənfi rəy-lərdə normadan daha çox toplandığını görmək;
- müsbət və mənfi rəy-lərdə eyni mexanika-in necə fərqli qəbul edildiyini ayırmaq;
- Midnight Protocol-un Hacknet-dən fərqli olaraq hansı yeni dizayn kompromis-ları yaratdığını müəyyən etmək;
- sonrakı `Hacknet vs Midnight Protocol` müqayisə üçün dəlil bazası hazırlamaqdır.

Bu sənəd rəy text-lərin sadə müsbət/mənfi xülasəsi deyil.

---

# 2. məlumat toplusu

Collection snapshot: **2026-10-02**

- Total English Steam reviews: **301**
- Unique reviews: **301**
- müsbət: **253**
- mənfi: **48**
- Overall müsbət ratio: **84.05%**
- Overall mənfi ratio: **15.95%**
- Empty reviews: **2**
- Very short reviews: **31**
- orta oyun müddəti at rəy: **15.19h**
- Median oyun müddəti at rəy: **11.70h**
- müsbət rəy orta oyun müddəti: **17.01h**
- mənfi rəy orta oyun müddəti: **5.59h**

Deterministik məlumat toplusu:

- `data/processed/midnight-protocol/reviews.jsonl`
- `data/processed/midnight-protocol/statistics.json`
- `data/reports/midnight-protocol/summary.md`

---

# 3. yoxlama əhatə

Midnight Protocol məlumat toplusu Hacknet-dən xeyli kiçik olduğu üçün daha dərin məna yönümlü yoxlama aparmaq mümkün olub.

Oxunmuş yoxlama materialı:

- **bütün 48 mənfi rəy**
- **50 ən faydalı müsbət rəy**
- **50 low-oyun müddəti rəy**
- **25 ən yeni müsbət rəy**
- yaradıcı interview
- Steam mağaza positioning
- peşəkar reviews

nümunə-lar arasında overlap var. Bunlar 173 distinct rəy demək deyil.

Bu yoxlama full 253 müsbət rəy-un manual classification-ı deyil, amma bütün mənfi population-un oxunması Midnight Protocol-un uğursuzluq nümunələri üçün xüsusilə güclü dəlil verir.

---

# 4. Full-corpus namizəd yoxlama

Expanded namizəd taxonomy ilə:

- total reviews: **301**
- ən azı bir mövzu namizəd-i tutulan reviews: **226**
- əhatə: **75.08%**

Taxonomy:

`config/theme_taxonomy.yaml`

məna yönümlü taxonomy:

`config/aspect_taxonomy.yaml`

namizəd retrieval final məna yönümlü classification deyil. mövzu-in “mənfi rəy payı” həmin mövzu keyword/nümunə-i olan rəy-lərin neçə faizinin overall Steam recommendation-ının mənfi olduğunu göstərir.

məlumat toplusu baseline mənfi ratio:

**15.95%**

---

# 5. mövzu statistikası

| mövzu | Mentions | məlumat toplusu payı | mənfi rəy payı | Baseline-a nisbət |
|---|---:|---:|---:|---:|
| STORY_NARRATIVE | 136 | 45.18% | 11.03% | 0.69× |
| DEPTH_CHALLENGE | 112 | 37.21% | 21.43% | 1.34× |
| LOADOUT_BUILD | 82 | 27.24% | 15.85% | 0.99× |
| TACTICAL_TURN_BASED | 73 | 24.25% | 16.44% | 1.03× |
| TERMINAL_UI | 57 | 18.94% | 24.56% | **1.54×** |
| UI_USABILITY | 41 | 13.62% | 19.51% | 1.22× |
| oyuna dalma hissi | 40 | 13.29% | 7.50% | **0.47×** |
| SOUND_AUDIO | 40 | 13.29% | 7.50% | **0.47×** |
| RNG_FAIRNESS | 36 | 11.96% | **36.11%** | **2.26×** |
| CHOICE_REPUTATION | 29 | 9.63% | 6.90% | **0.43×** |
| KEYBOARD_ONLY | 28 | 9.30% | 14.29% | 0.90× |
| INVESTIGATION_DISCOVERY | 20 | 6.64% | 5.00% | **0.31×** |
| RETRY_ROLLBACK | 20 | 6.64% | **35.00%** | **2.19×** |
| təkrarçılıq | 19 | 6.31% | **36.84%** | **2.31×** |
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

Rəqəmlər mövzu prevalence və mənfi concentration üçün **retrieval siqnalıdır**, aspect sentiment faizi deyil.

---

# 6. oyun müddəti qrup-ları

## 6.1. Overall rəy nəticəsi

| oyun müddəti | Reviews | müsbət | mənfi | müsbət ratio |
|---|---:|---:|---:|---:|
| 0–1h | 21 | 16 | 5 | 76.19% |
| 1–3h | 45 | 28 | 17 | **62.22%** |
| 3–10h | 79 | 60 | 19 | 75.95% |
| 10h+ | 156 | 149 | 7 | **95.51%** |

Midnight Protocol-da ən zəif rəy qrup-u **1–3 saat** aralığıdır.

Bu Hacknet-dən fərqli nümunə-dir. Hacknet-də ən aşağı satisfaction 0–1h qrup-da idi və sonra davamlı yüksəlirdi.

Midnight Protocol-da isə:

```text
0–1h   → 76.2%
1–3h   → 62.2%
3–10h  → 75.9%
10h+   → 95.5%
```

Bu, təlim hissəsi-dan sonra ilk dəfə sistemlərin tam qarşılıqlı əlaqə-a girdiyi hissədə xüsusi çətinlik olduğunu göstərən güclü siqnaldır.

Causation sübut olunmur; sevən oyunçuların daha uzun oynaması selection bias yaradır.

---

# 7. 1–3 saatlıq “danger zone”

məna yönümlü yoxlama həmin dip üçün mümkün səbəbləri göstərir.

1–3 saat aralığındakı mənfi rəy-lərdə tez-tez:

- RNG;
- trace;
- rollback/retry;
- loadout-un necə qurulacağını anlamamaq;
- required tool slot-ların çox tez dolması;
- terminal/keyboard çətinlik;
- təlim hissəsi-dan sonra difficulty spike;
- “hacking” gözləntisi ilə “board game” reallığı arasındakı fərq

görünür.

mövzu qrup-ları bunu dəstəkləyir:

### RNG_FAIRNESS

1–3h qrup:
- 9 mention
- 7 mənfi
- **77.8% mənfi**

### RETRY_ROLLBACK

1–3h qrup:
- 3 mention
- **3 mənfi**

### təkrarçılıq

1–3h qrup:
- 6 mention
- 4 mənfi
- **66.7% mənfi**

### URGENCY_TRACE

1–3h qrup:
- 2 mention
- **2 mənfi**

### TERMINAL_UI

1–3h qrup:
- 12 mention
- 5 mənfi
- **41.7% mənfi**

### TACTICAL_TURN_BASED

1–3h qrup:
- 11 mention
- 5 mənfi
- **45.5% mənfi**

Bu nümunə göstərir ki, Midnight Protocol-un problem nöqtəsi “ilk ekran qorxuducudur”dan daha çox:

> **təlim hissəsi sonrası oyunçu model-in core systems-lə toqquşduğu mərhələdir.**

**etibarlılıq: High**

---

# 8. Əsas güc: hacker rol hissi dərin tactical sistemlə birləşir

Explicit HACKER_FANTASY namizəd sayı cəmi 8-dir, amma hamısı müsbət rəy-dur.

Regex çox dar olduğu üçün bu 2.66% real prevalence kimi qəbul edilmir.

məna yönümlü yoxlama-də rol hissi daha geniş formada görünür:

- “feel like a hacker”;
- keyboard-only typing;
- futuristic network map;
- terminal;
- deck/program hazırlamaq;
- trace altında hərəkət;
- black/white/grey hat reputation;
- information oğurlamaq və qərar vermək.

son dövr 2025–2026 rəy-lər də bu hissi hələ əsas value proposition kimi göstərir.

yaradıcı intent də bunu birbaşa təsdiqləyir: keyboard-only giriş üsulu oyunun oyuna dalma hissi üçün əsas elementlərindən biri kimi nəzərdə tutulub.

**etibarlılıq: High**

---

# 9. Turn-based sistem: Hacknet probleminə real cavabdır, amma tam həll deyil

TACTICAL_TURN_BASED:

- 73 mentions
- 24.25% məlumat toplusu share
- mənfi ratio 16.44% — məlumat toplusu baseline-a çox yaxın.

Bu özü nə aydın müsbət, nə də aydın mənfi mövzu-dir.

məna yönümlü yoxlama göstərir ki, iki oyunçu qrupu var.

## Müsbət qəbul

Turn-based sistem:

- speed requirement-i azaldır;
- planlama imkanı verir;
- “hacking = sürətli typing” modelindən çıxır;
- network-u tactical puzzle-a çevirir;
- hərəkət büdcəsi yaradır.

Bəzi rəy-lər turn-based dizayn-i məhz Hacknet/Uplink tipli real-time stress-ə qarşı üstünlük hesab edir.

## Mənfi qəbul

Bəzi oyunçular isə:

- “hacking yox, chess/board game” kimi görür;
- typing-in turn-based sistemdə funksional mənasını zəif sayır;
- SysOp sisteminin oyunun genre expectation-ını dəyişdirdiyini düşünür;
- hərəkət büdcəsi-ni həddindən artıq məhdud hiss edir.

Əsas nəticə:

> **Midnight Protocol mexaniki dərinlik-i artırıb, amma bunun müqabilində genre expectation riskini böyüdüb.**

**etibarlılıq: High**

---

# 10. RNG (təsadüfi nəticə mexanizmi) və ədalətlilik — ən ciddi dizayn problemi

RNG_FAIRNESS:

- 36 mentions
- 11.96% məlumat toplusu share
- 13 mənfi rəy
- **36.11% mənfi**
- baseline-dan **2.26×** yüksək mənfi concentration.

Bu sadəcə mənfi reviewer complaint-i deyil.

Ən faydalı müsbət rəy belə RNG və rollback-u oyunun ən ciddi qüsuru kimi təsvir edir.

məna yönümlü yoxlama-də əsas problem random elementin mövcudluğu deyil.

Problem oyunçunun uğursuzluq-i öz qərarı ilə əlaqələndirə bilməməsidir.

mənfi geribildirim-də:

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

### dizayn prinsipi

> **Randomness oyunçuya yeni vəziyyət təqdim edə bilər; amma uğur/uduzma əsasən oyunçunun izah edə bildiyi qərarlardan gəlməlidir.**

**etibarlılıq: High**

---

# 11. Retry/rollback problemi RNG-ni böyüdür

RETRY_ROLLBACK:

- 20 mentions
- 35% mənfi
- baseline-dan **2.19×** yüksək.

RNG təkbaşına bu qədər zərərli olmazdı, əgər uğursuzluq recovery daha yaxşı olsaydı.

rəy-lərdə:

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

Bu, Midnight Protocol üçün ən vacib dizayn nəticələrindən biridir.

**etibarlılıq: High**

---

# 12. Trace/turn cap — tension və experimentation arasında konflikt

URGENCY_TRACE:

- 16 mentions
- 8 mənfi
- **50% mənfi**
- baseline-dan **3.14×** yüksək mənfi concentration.

nümunə sayı böyük deyil, amma bütün mənfi population-un yoxlama-i nümunə-i təsdiqləyir.

Bəzi oyunçular trace-i:

- pressure;
- tension;
- mission rhythm

kimi bəyənir.

Digərləri üçün isə:

- map-i araşdırmağa;
- optional məlumat toplamağa;
- stealth plan qurmağa;
- fərqli tool test etməyə

mane olur.

Xüsusilə turn-cap kimi əlavə limit gələndə oyunçu bunu:

> “öz planımı qururam”

deyil,

> “designer-in istədiyi templə gedirəm”

kimi hiss edə bilər.

### dizayn prinsipi

> **Urgency exploration və strategy-ni öldürəcək qədər sərt olmamalıdır; xüsusilə investigation/discovery oyunun dəyər hissəsidirsə.**

**etibarlılıq: High**

---

# 13. Keyboard-only — eyni anda əsas üstünlük və əsas UX riski

KEYBOARD_ONLY:

- 28 explicit mentions
- mənfi ratio 14.29% — məlumat toplusu baseline-a yaxın.

Bu rəqəm mexanika-in polarizing olduğunu gizlədir.

məna yönümlü yoxlama çox aydın iki istiqamət göstərir.

## Müsbət

- oyuna dalma hissi artır;
- oyunçu fiziki olaraq “hacker” roluna girir;
- typing command oyunçu intent-i thematic şəkildə ifadə edir;
- mouse-dan fərqli distinctive məhsul identity yaradır.

## Mənfi

- mouse ilə bir klik olacaq action uzun command-a çevrilir;
- typo;
- help discoverability;
- node name yadda saxlamaq;
- slow repeated giriş üsulu;
- keyboard-only olmasına baxmayaraq UI-nin vizual GUI kimi görünməsi

bəzi oyunçular üçün artificial çətinlik yaradır.

yaradıcı özü də keyboard-only UI-nin discoverability-ni azaltdığını etiraf edir.

### Əsas nəticə

> **giriş üsulu gimmick özünü yalnız rol hissi ilə yox, qarşılıqlı əlaqənin səmərəliliyi ilə də doğrultmalıdır.**

Əgər keyboard daha immersive, amma ardıcıl olaraq daha yavaşdırsa, yenilik effekti tükənəndən sonra çətinlik görünür.

**etibarlılıq: High**

---

# 14. Terminal/technical həqiqilik hissi Hacknet-dən fərqli işləyir

TERMINAL_UI:

- 57 mentions
- 24.56% mənfi
- baseline-dan **1.54×** yüksək.

REALISM_ACCURACY:

- 17 mentions
- yalnız 5.88% mənfi.

Bu paradoks görünür:

- oyunçular ümumiyyətlə real hacking simulator tələb etmir;
- amma command-line görünüşü müəyyən usability və həqiqilik hissi expectation yaradır.

müsbət rəy-lərdə çox aydın fikir var:

> “realistic deyil və məhz buna görə yaxşı oyundur.”

yaradıcı də “fun game first, hacking mövzu second” yanaşmasını açıq deyir.

Bu Hacknet-də tapdığımız seçilmiş həqiqilik hissi prinsipini ikinci oyunda da təsdiqləyir.

oyunlararası hypothesis artıq daha güclüdür:

> **Bu janrda tam realizm əsas tələb deyil; oyunçunun tanıdığı texniki işarələr və ardıcıl fiction kifayət qədər həqiqilik hissi yarada bilər.**

**etibarlılıq: High**

---

# 15. Loadout/build sistemi real dərinlik verir, amma dominant build problemi var

LOADOUT_BUILD:

- 82 mentions
- 27.24% məlumat toplusu share
- müsbət/mənfi ratio təxminən overall baseline ilə eynidir.

Bu mövzu-in özü polarizing deyil.

məna yönümlü yoxlama daha faydalıdır.

## Güclü tərəf

müsbət rəy-lərdə:

- stealth;
- aggression;
- bypass;
- hardware;
- program combinations;
- resource/slice management

real build seçim kimi təriflənir.

son dövr rəy-lərdə də “başqa approach üçün deck-i dəyişmək” əsas satisfaction amil kimi qalır.

## Problem

mənfi və mixed rəy-lərdə:

- bəzi basic tool-lar demək olar məcburidir;
- 5 slot çox tez dolur;
- mission requirements qabaqcadan aydın deyil;
- bəzi dominant configurations çox mission-da işləyir;
- çox sayda tool olsa da effective seçim azalır.

Bu çox vacib distinction-dır:

> **Feature count ≠ qərar dərinlik.**

10 tool seçimi verib 3-ü mandatory, 2-si dominantdırsa real seçim aşağıdır.

**etibarlılıq: High**

---

# 16. seçim/reputation sistemi oyunun ən güclü fərqləndiricilərindəndir

CHOICE_REPUTATION:

- 29 mentions
- 93.10% overall müsbət
- orta oyun müddəti: **25.17h**

məna yönümlü yoxlama və son dövr reviews:

- black/white/grey hat;
- bank hesabına toxunmaq/tunmamaq;
- mission nəticəsinin reputation-a təsiri;
- side mission açılması/bağlanması;
- endings;
- morally ambiguous qərarlar

kimi elementləri yüksək qiymətləndirir.

Bu Hacknet-dən əsas üstünlüklərdən biridir.

Hacknet əsasən hacker rol hissi və hekayə verir.

Midnight Protocol buna əlavə edir:

> **“mən necə hackerəm?”**

sualını.

Bu yalnız role-playing flavor deyil; programs, missions və narrative path ilə əlaqələnəndə oyun gedişi identity yaradır.

### Risk

Bəzi rəy-lər nəticə-ların həddindən artıq sərt/permanent olduğunu deyir.

Deməli:

> meaningful nəticə lazımdır, amma oyunçu-in qərarı anlamadan irreversibly cəzalandırılması qərar sərbəstliyi-ni zəiflədə bilər.

**etibarlılıq: High**

---

# 17. hekayə oyunun əsas oyunda qalma sistemidir

STORY_NARRATIVE:

- 136 mentions
- məlumat toplusu-in **45.18%**-i
- mənfi ratio yalnız 11.03%.

Bu, ən geniş mövzu-dir.

10h+ qrup-da hekayə namizəd-i olan:

- 100 rəy;
- yalnız 4 mənfi.

son dövr müsbət rəy-lərdə hekayə hələ də əsas praise səbəbidir.

Co-occurrence:

- hekayə + DEPTH_CHALLENGE: 71
- hekayə + LOADOUT_BUILD: 63
- hekayə + TACTICAL_TURN_BASED: 52
- hekayə + TERMINAL_UI: 39
- hekayə + oyuna dalma hissi: 31
- hekayə + SOUND: 30
- hekayə + CHOICE_REPUTATION: 24

Bu göstərir ki, hekayə oyun gedişi-dən ayrı qat deyil.

> **Narrative tactical oyun gedişi, loadout və seçim systems-ə context verir.**

mənfi rəy-lərin bir hissəsi oyun gedişi-dən bezsə belə hekayə-ni davam etmək üçün səbəb kimi qeyd edir.

**etibarlılıq: High**

---

# 18. oyuna dalma hissi və audio güclü, davamlı satisfaction amil-ləridir

oyuna dalma hissi və SOUND_AUDIO:

- hər biri 40 mentions
- hər ikisinin mənfi ratio-su 7.5%
- baseline-dan təxminən yarı qədər mənfi concentration.

Praise:

- minimalist cyberpunk UI;
- animation;
- node visualization;
- typing;
- music;
- geribildirim;
- hekayə presentation.

peşəkar rəy də presentation və interface-i əsas güclərdən sayır, soundtrack üçün isə variety-ni zəif nöqtə kimi qeyd edir.

Bu Hacknet ilə başqa ortaq principle-dir:

> interface-heavy oyunda audio/visual presentation sadəcə polish deyil, rol hissi-nin mexaniki hissəsidir.

**etibarlılıq: High**

---

# 19. Investigation/discovery az görünür, amma çox müsbətdir

INVESTIGATION_DISCOVERY:

- 20 mentions
- 19 müsbət
- 1 mənfi.

rəy-lərdə:

- side clues;
- optional məlumat;
- intranet;
- hidden secrets;
- real-world-style extra investigation;
- easter eggs

yüksək dəyər yaradır.

yaradıcı də fourth-wall secrets və curiosity-ni xüsusi dizayn məqsədi kimi qeyd edir.

Lakin bu sistem Hacknet-də olduğu qədər əsas oyun dövrü-un mərkəzində görünmür.

Midnight Protocol daha çox:

> tactical network puzzle + narrative RPG

kimidir.

Bu, Hacknet müqayisə-da vacibdir.

**etibarlılıq: Medium-High**

---

# 20. təkrarçılıq tam həll olunmayıb

təkrarçılıq:

- 19 mentions
- **36.84% mənfi**
- baseline-dan **2.31×** yüksək.

Midnight Protocol Hacknet-dən daha çox tactical dərinlik verir, amma təkrarçılıq yox olmur.

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

Bəzi long-play müsbət rəy-lər isə mission variety, bosses və special mexanikalar sayəsində bu təkrarçılıq-ın qırıldığını deyir.

Nəticə:

> **dərinlik təkrarçılıq riskini azalda bilər, amma fundamental action grammar çox dəyişmirsə onu tam aradan qaldırmır.**

**etibarlılıq: High**

---

# 21. “More dərinlik” avtomatik olaraq “better” deyil

Midnight Protocol Hacknet-in dayaz loop probleminə cavab olaraq daha çox sistem təqdim edir:

- hərəkət büdcəsi;
- loadout;
- resource slicing;
- ICE;
- SysOps;
- trace;
- reputation;
- mission seçimlər;
- hardware/program progression.

Buna baxmayaraq 1–3h qrup-da satisfaction düşür.

Bu bizim gələcək oyun üçün ən vacib dərslərdən biridir:

> **Sistem sayı deyil, oyunçunun hər anda etdiyi mənalı qərarların keyfiyyəti vacibdir.**

dərinlik:

- izah edilə bilən;
- öyrənilə bilən;
- qabaqcadan planlana bilən;
- uğursuzluq-dan geribildirim verən

olmalıdır.

Əks halda dərinlik mürəkkəblik/çətinlik kimi hiss olunur.

---

# 22. yaradıcı intent vs oyunçu outcome

## Intent: keyboard oyuna dalma hissi

yaradıcı:

- keyboard-u oyuna dalma hissi üçün “heart of the game” sayır;
- discoverability downside-ını qəbul edir.

oyunçu outcome:

- müsbət: çox güclü rol hissi və distinctive identity;
- mənfi: inefficient UI və repetitive typing.

**Intent achieved, kompromis realdır.**

---

## Intent: fun over realizm

yaradıcı:

- real hacking simulyasiyası məqsəd olmayıb;
- fun game first.

oyunçu outcome:

- müsbət rəy-lərin çoxu bunu qəbul edir;
- technical accuracy complaint Hacknet-dən daha az dominant görünür.

**Intent böyük ölçüdə achieved.**

---

## Intent: accessible turn-based strategy

yaradıcı:

- real-time prototipi stressli və əyləncəsiz sayıb turn-based-a keçib.

oyunçu outcome:

- bir qrup planlama və stress-in azalmasını çox sevir;
- digər qrup turn-based/chess modelini hacking expectation-a uyğun görmür;
- RNG və trace yeni fairness problem yaradır.

**Stress problemi azaldılıb, amma uğursuzluq/fairness problemi yaranıb.**

---

## Intent: simple action language, complex appearance

yaradıcı:

- 2-action board-game grammar;
- command-line presentation ilə complex feel.

oyunçu outcome:

- oyuna dalma hissi işləyir;
- bəzi technical/UX-oriented oyunçular bu qat-i “unnecessary typing” kimi görür.

**Perceived mürəkkəblik uğurludur, qarşılıqlı əlaqənin səmərəliliyi audience-dan asılıdır.**

---

# 23. Midnight Protocol-un ən güclü dizayn nailiyyətləri

1. **Hacker rol hissi-ni tactical qərar-making ilə birləşdirir.**
2. **Keyboard-only giriş üsulu güclü məhsul identity yaradır.**
3. **hekayə + seçim + reputation oyun gedişi context-i artırır.**
4. **Loadout/build sistemi Hacknet-dən daha çox qərar sərbəstliyi verir.**
5. **Turn-based sistem non-speed-based hacking rol hissi üçün alternativ yaradır.**
6. **Presentation və oyuna dalma hissi yüksək səviyyədədir.**
7. **seçilmiş həqiqilik hissi real simulation olmadan işləyir.**
8. **Side content və moral seçimlər “hacker identity” yaradır.**
9. **son dövr reviews göstərir ki, core strengths uzun müddət aktual qalıb.**

---

# 24. Əsas uğursuzluq nümunələr

1. **RNG uğursuzluq-i oyunçu bacarıq-dən ayıra bilir.**
2. **Retry/rollback/replanning modeli uğursuzluq-i daha ağrılı edir.**
3. **Trace/turn cap experimentation ilə toqquşa bilir.**
4. **Keyboard-only giriş üsulu bəzi action-ları lazımsız yavaşladır.**
5. **təlim hissəsi sonrası 1–3h mərhələsində mürəkkəblik spike görünür.**
6. **Loadout seçimlər bəzən mandatory slots və hidden mission needs səbəbilə azalır.**
7. **Turn-based board-game identity bəzi hacking-game expectation-ları ilə toqquşur.**
8. **Core action grammar yenə təkrarçılıq yarada bilir.**
9. **Bəzi nəticə-lar həddindən artıq permanent görünür.**
10. **Bugs/softlock/save issues az volume-da olsa da mənfi recommendation-a güclü təsir edir.**

---

# 25. Bizim gələcək oyun üçün dizayn dərsləri

## 25.1. Tactical dərinlik qur, amma uğursuzluq explainable olsun

Oyunçu bilməlidir:

- niyə uduzdu;
- hansı qərar səhv idi;
- növbəti dəfə nəyi dəyişə bilər.

“Pis roll gəldi” əsas geribildirim olmamalıdır.

---

## 25.2. Mission öncəsi planlama üçün kifayət qədər intel ver

Loadout meaningful olacaqsa:

> oyunçu nəyə hazırlaşdığını müəyyən dərəcədə bilməlidir.

Tam məlumat lazım deyil.

Amma blind build seçimləri bacarıq test yox, trial-and-error yarada bilər.

---

## 25.3. uğursuzluq recovery dizayn-in bir hissəsidir

Retry:

- tez;
- aydın;
- re-plan etməyə imkan verən;
- optional branch-ləri əsassız permanent bağlamayan

olmalıdır.

---

## 25.4. Urgency ilə curiosity-ni balanslaşdır

Əgər oyun gedişi:

- optional files;
- hidden məlumat;
- investigation;
- exploration

üzərində də qurulursa, timer/trace onları faktiki cəzalandırmamalıdır.

---

## 25.5. giriş üsulu rol hissi-ni dəstəkləsin, əməliyyatı yavaşlatmasın

Typing:

- hacker rol hissi üçün güclüdür.

Amma tez-tez təkrarlanan low-value action üçün:

- autocomplete;
- aliases;
- context-sensitive suggestions;
- history;
- shortcuts

olmalıdır.

---

## 25.6. More systems əvəzinə better qərar density

Hər 30–60 saniyədə oyunçu:

> “nə edim?”

deyə düşünməlidir,

> “hansı syntax-i yazmalıyam?”

deyil.

---

## 25.7. seçim + nəticə çox güclü imkan-dir

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

# 26. etibarlılıq matrix

| Nəticə | etibarlılıq |
|---|---|
| RNG (təsadüfi nəticə mexanizmi) və ədalətlilik əsas uğursuzluq amil-dir | High |
| Retry/recovery RNG problemini böyüdür | High |
| 1–3h xüsusi risk qrup-udur | High |
| hekayə əsas oyunda qalma amil-dir | High |
| Keyboard-only güclü oyuna dalma hissi + UX kompromis yaradır | High |
| Turn-based sistem real-time speed requirement-i uğurla azaldır | High |
| Hacker rol hissi güclü value proposition-dır | High |
| Loadout sistemi real qərar sərbəstliyi yaradır, amma mandatory/dominant build riski var | High |
| seçim/reputation əsas fərqləndiricidir | High |
| təkrarçılıq daha dərin sistemə baxmayaraq qalır | High |
| seçilmiş həqiqilik hissi oyunlararası principle-dir | High |
| Investigation/discovery daha da dərinləşdirilə bilən imkan-dir | Medium-High |
| Mod/Workshop long-tail böyük amil-dir | Low-Medium — məlumat toplusu dəlil azdır |

---

# 27. Məhdudiyyətlər

- 301 rəy bütün oyunçu population deyil.
- Steam rəy self-selection daşıyır.
- müsbət/mənfi recommendation aspect sentiment deyil.
- namizəd regex məna yönümlü classifier deyil.
- müsbət məna yönümlü yoxlama bütün 253 müsbət rəy-u əhatə etmir.
- mənfi population-un hamısı oxunsa da, qısa/zarafat rəy-lər analytical value daşımaya bilər.
- oyun müddəti correlation causation deyil.
- Steam mağaza display rəy sayı ilə API snapshot sayı fərqlənə bilər; daxili analiz üçün verified API snapshot istifadə olunur.
- Bəzi mənfi complaint-lər patch-lərlə sonradan qismən dəyişmiş ola bilər; rəy tarixi nəzərə alınmalıdır.

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

**Steam mağaza**  
https://store.steampowered.com/app/1162700/

**Game yaradıcı — Road to IGF 2022 / Sam Agten interview**  
https://www.gamedeveloper.com/design/hacking-answers-tactical-narrative-game-midnight-protocol

**Quarter to Three — Tom Chick rəy**  
https://www.quartertothree.com/fp/2022/01/16/midnight-protocol-hacks-into-the-sweet-spot-between-storytelling-and-strategy/

**Softpedia rəy**  
https://www.softpedia.com/reviews/games/pc/midnight-protocol-review-534571.shtml

---

# 29. Status

**Mərhələ:** Midnight Protocol full-corpus rəy təhlil — tamamlanıb  
**məlumat toplusu:** 301 verified English Steam rəy  
**mənfi məna yönümlü yoxlama:** 48/48 mənfi reviews  
**müsbət yoxlama:** faydalı + low-oyun müddəti + son dövr qrups  
**Növbəti:** `analysis/midnight-protocol/deep-research.md` və sonra Hacknet vs Midnight Protocol müqayisə.
