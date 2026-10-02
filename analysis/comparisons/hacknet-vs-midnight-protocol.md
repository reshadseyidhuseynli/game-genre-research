# Hacknet vs Midnight Protocol — Dizayn və Player Response Müqayisəsi

## 1. Comparison Question

Bu müqayisənin əsas sualı:

> **Eyni geniş “terminal/hacking” fantasy-si daxilində Hacknet-in sadə, real-time və accessibility-first modeli ilə Midnight Protocol-un daha dərin, turn-based və tactical modeli oyunçu təcrübəsini necə dəyişir?**

Məqsəd “hansı oyun daha yaxşıdır?” demək deyil.

Məqsəd:

- hansı problem hansı yanaşma ilə həll olunur;
- hansı yeni risk yaranır;
- hansı design principle iki oyunda da təkrarlanır;
- gələcək yeni concept üçün hansı middle-ground daha güclü görünür

suallarına cavab verməkdir.

---

# 2. Niyə bu iki oyun müqayisə edilə bilər?

Ortaq əsaslar:

- hacker fantasy;
- terminal/keyboard interaction;
- fictional computer environment;
- single-player;
- story-driven structure;
- real texniki terminlərin seçilmiş istifadəsi;
- abstract hacking mechanics;
- network/system infiltration;
- indie production;
- computer interface-in oyunun özünə çevrilməsi.

Əsas fərq:

```text
Hacknet
real-time execution + simple tool loop

Midnight Protocol
turn-based planning + tactical/loadout system
```

Bu fərq bizə **accessibility ↔ depth** trade-off-unun real player response-a necə təsir etdiyini görməyə imkan verir.

---

# 3. Dataset snapshot

| Metrik | Hacknet | Midnight Protocol |
|---|---:|---:|
| Verified English Steam reviews | 11,773 | 301 |
| Positive | 11,082 | 253 |
| Negative | 691 | 48 |
| Positive ratio | **94.13%** | **84.05%** |
| Avg playtime — positive review | 13.06h | 17.01h |
| Avg playtime — negative review | 4.40h | 5.59h |
| Median playtime | — | 11.70h |

Dataset ölçüləri çox fərqlidir. Buna görə absolute mention count-lar oyunlar arasında birbaşa müqayisə edilmir.

Əsas comparison:

- pattern direction;
- baseline-a nisbət;
- semantic audit;
- playtime cohort shape;
- developer intent.

---

# 4. Playtime cohort müqayisəsi

| Playtime | Hacknet positive | Midnight Protocol positive |
|---|---:|---:|
| 0–1h | **67.05%** | 76.19% |
| 1–3h | 86.59% | **62.22%** |
| 3–10h | 95.79% | 75.95% |
| 10h+ | 98.57% | 95.51% |

Bu table ən vacib comparison siqnallarından biridir.

## Hacknet

Ən böyük risk:

> **ilk saat**

Terminal və command vocabulary dərhal friction yarada bilər.

Amma oyunu keçən reviewer cohort-larda recommendation sürətlə yüksəlir.

## Midnight Protocol

İlk saat Hacknet-dən daha yaxşı görünür.

Əsas risk:

> **1–3 saat**

Yəni tutorialın özü yox, tutorialdan sonra:

- loadout;
- RNG;
- trace;
- SysOp;
- limited slots;
- failure/retry

birlikdə işləməyə başlayanda satisfaction düşür.

### Əsas dərs

> **First-time onboarding yalnız controls öyrətmək deyil. Core systems-in ilk dəfə bir-biri ilə qarşılaşdığı nöqtə ayrıca onboarding mərhələsidir.**

---

# 5. Hook və Player Fantasy

## Hacknet

Əsas fantasy:

> “Terminalda hacker oluram.”

Çox sadə və dərhal başa düşülür.

Fantasy-ni yaradan:

- terminal;
- commands;
- IP;
- ports;
- filesystem;
- trace;
- music;
- files.

## Midnight Protocol

Fantasy daha layered-dir:

> “Keyboard ilə network daxilində tactical hacker oluram və hansı hacker olmaq istədiyimə qərar verirəm.”

Əlavə layer-lər:

- loadout;
- tactical network;
- hat reputation;
- moral decisions;
- programs/hardware.

### Nəticə

Hacknet fantasy-ni **daha tez** satır.

Midnight Protocol fantasy-ni **daha dərindən** sistemləşdirir.

Bu trade-off-dur, superiority deyil.

---

# 6. Realizm: hər iki oyun eyni fundamental nəticəyə gəlir

Hacknet developer intent:

> oyunçunu hacker kimi hiss etdirmək.

Midnight Protocol developer intent:

> fun game first, hacking theme second.

Hər iki oyunda:

- real terminology;
- terminal language;
- recognizable cyber concepts

istifadə edilir.

Amma heç biri full real-world hacking simulation deyil.

Player feedback də bunu əsasən qəbul edir.

## Cross-game principle

> **Bu janr üçün full realism tələb deyil. Selective authenticity + coherent fantasy daha sağlam hədəfdir.**

Realism yalnız:

- marketing “real simulator” expectation yaradanda;
- interface real sistemə çox bənzəyib davranışı fərqli olanda

problemə çevrilir.

**Confidence: High**

---

# 7. Terminal / Keyboard trade-off

## Hacknet

Terminal:

- əsas fantasy driver;
- GUI ilə birlikdə işləyir;
- technical user real Unix behavior gözləyə bilər.

Əsas complaint:

> “real terminal kimi görünür, amma real terminal kimi davranmır.”

## Midnight Protocol

Keyboard-only:

- daha güclü thematic commitment;
- distinctive product identity;
- developer tərəfindən əsas immersion source kimi dizayn edilib.

Əsas complaint:

> “click-lə daha sürətli edəcəyim şeyi niyə yazmalıyam?”

### Cross-game nəticə

Terminal/keyboard iki ayrı problem yaradır:

```text
semantic authenticity
— command doğru davranırmı?

interaction efficiency
— command yazmaq buna dəyərmi?
```

Gələcək oyun hər ikisini ayrıca həll etməlidir.

---

# 8. Core Loop

## Hacknet

```text
probe
→ port tap
→ cracker
→ porthack
→ files
→ objective
```

Üstünlük:

- tez öyrənilir;
- fantasy payoff sürətlidir.

Problem:

- pattern tez görünür;
- tool = key olur;
- decision density aşağı düşür.

## Midnight Protocol

```text
intel
→ loadout
→ enter network
→ move
→ ICE/SysOp
→ resource/trace
→ objective/optional data
→ decision
→ exit
```

Üstünlük:

- daha çox planning;
- build;
- tactical route;
- resource management;
- consequence.

Problem:

- complexity;
- hidden information;
- RNG;
- repetitive low-value commands;
- retry cost.

### Əsas lesson

> **Hacknet-də problem “too little decision”; Midnight Protocol-da risk “too much system friction”.**

Gələcək concept üçün məqsəd “daha çox mechanic” deyil.

Məqsəd:

> **yüksək meaningful-decision density.**

---

# 9. Repetition

## Hacknet

REPETITION candidate:

- 517 reviews;
- 23.21% negative review ratio;
- Hacknet baseline-dan **3.95×** yüksək negative concentration.

Repetition core failure pattern-dir.

## Midnight Protocol

REPETITION candidate:

- 19 reviews;
- 36.84% negative;
- Midnight baseline-dan **2.31×** yüksək.

Absolute negative rate daha yüksəkdir, amma relative-to-game baseline daha zəifdir.

Midnight Protocol repetition-ı tam həll etmir, amma:

- loadout;
- mission-specific mechanics;
- SysOps;
- choices;
- bosses;
- handcrafted levels

variation yaradır.

### Nəticə

> **System depth repetition-ı azalda bilir, amma fundamental action grammar dəyişmirsə tam yox etmir.**

**Confidence: High**

---

# 10. Depth

## Hacknet

Depth daha çox:

- story context;
- exploration;
- optional files

tərəfdən gəlir.

Hacking mechanic-in özü nisbətən sadədir.

## Midnight Protocol

Depth birbaşa gameplay system-dən gəlir:

- action economy;
- loadout;
- memory/slices;
- stealth/aggression;
- route;
- trace;
- SysOp;
- ICE.

Bu Hacknet-in əsas mexaniki boşluğunu həll edir.

Amma əlavə risk:

- tutorial complexity;
- bad RNG;
- dominant/məcburi tool-lar;
- wrong build;
- retry friction.

### Principle

> **Depth əlavə ediləndə onun information cost-u, learning cost-u və failure cost-u birlikdə dizayn edilməlidir.**

---

# 11. Failure modeli

Bu iki oyunun ən vacib fərqlərindən biridir.

## Hacknet

Player failure çox vaxt:

- speed;
- timing;
- command execution;
- trace

ilə əlaqələndirilə bilir.

Player deyə bilir:

> “mən daha yaxşı etməliydim.”

## Midnight Protocol

Failure bəzən:

- random trace;
- SysOp movement;
- hidden ICE;
- wrong loadout due incomplete intel;
- percentage chance

ilə gəlir.

Player deyə bilər:

> “bu dəfə roll pis idi.”

Bu mastery loop üçün daha təhlükəlidir.

### Cross-game principle

> **Failure oyuncuya öz qərarı haqqında information verməlidir.**

Randomness:

- scenario yarada bilər;
- adaptation tələb edə bilər;

amma əsas nəticəni izah edən dominant faktor olmamalıdır.

---

# 12. Retry və Recovery

Hacknet failure-dan sonra retry daha conventional hiss olunur.

Midnight Protocol-da isə:

- rollback;
- mission permanent outcome;
- loadout re-plan;
- no manual save;
- one-chance mission perception

daha çox complaint yaradır.

Bu çox vacib lesson-dir:

> **Challenge design ilə recovery design bir sistemdir.**

Difficult mission yaxşı ola bilər.

Difficult mission + incomplete information + random failure + weak recovery birlikdə frustration yaradır.

---

# 13. Story

## Hacknet

Story:

- mystery;
- email;
- files;
- hidden systems;
- scripted memorable moments.

Fantasy-ni daşıyır və repetition-a context verir.

## Midnight Protocol

Story:

- 45.18% candidate coverage;
- tactical gameplay;
- choice;
- reputation;
- side missions;
- endings

ilə daha sistemik inteqrasiya olunur.

### Ortaq nəticə

Hər iki oyunda story “əlavə content” deyil.

> **Story core retention sistemidir.**

### Fərq

Hacknet:

> story-ni əsasən tapırsan.

Midnight Protocol:

> story-ni tapırsan və qismən formalaşdırırsan.

---

# 14. Investigation və Discovery

## Hacknet

Əsas güclərdən biridir.

Filesystem curiosity:

- optional files;
- logs;
- emails;
- hidden IP;
- easter eggs.

Oyunçuda:

> “burada başqa nə var?”

hissi güclüdür.

## Midnight Protocol

Optional data və secrets var.

Amma tactical board layer daha dominantdır.

Choice/reputation daha güclü olsa da organic snooping Hacknet-də daha təbii görünür.

### Opportunity

Gələcək oyun üçün ən güclü hybrid:

```text
Hacknet-style organic information exploration
+
Midnight Protocol-style meaningful choices/consequences
```

---

# 15. Player Agency və Consequences

## Hacknet

Theme analysis-də:

- PLAYER_AGENCY negative concentration: 2.77× baseline;
- WORLD_REACTIVITY: 3.55× baseline.

Aşağı volume, amma complaint aydındır:

- linearity;
- log-ların real consequence yaratmaması;
- world response zəifliyi.

## Midnight Protocol

Choice/reputation:

- yüksək positive signal;
- long-play review-lərdə güclü satisfaction driver.

Player:

- moral direction;
- mission;
- side content;
- reputation;
- endings

üzərində daha çox influence hiss edir.

### Nəticə

Midnight Protocol Hacknet-in əsas boşluqlarından birini real şəkildə həll edir:

> **player identity və consequence.**

Amma bəzən consequence həddindən artıq permanent hiss olunur.

Optimal sistem:

> meaningful, visible, recoverable-but-not-free consequence.

---

# 16. Onboarding

## Hacknet

ONBOARDING candidate relative negative concentration:

**2.14× baseline**

Əsas problem:

- terminal vocabulary;
- nə etməli olduğunu bilməmək;
- returning-player memory.

## Midnight Protocol

Overall ONBOARDING candidate baseline-a yaxındır.

Amma playtime cohort ciddi problem göstərir:

- 1–3h positive ratio yalnız 62.22%.

Burada problem basic tutorial deyil.

Problem:

> **systems onboarding.**

### Cross-game principle

Onboarding üç mərhələ olmalıdır:

1. **control onboarding** — hansı düymə/command;
2. **system onboarding** — mechanic-lər necə interaction edir;
3. **strategy onboarding** — yaxşı qərar necə görünür.

Hər iki oyun fərqli mərhələdə problem yaşayır.

---

# 17. Audio və Atmosphere

Hər iki oyunda:

- sound/music;
- terminal feedback;
- cyber visual language

güclü positive signal verir.

Hacknet-də soundtrack xüsusilə iconic praise alır.

Midnight Protocol-da presentation çox bəyənilir, amma soundtrack variety üçün complaint var.

### Principle

> **Computer-interface janrında audiovisual feedback normal UI polish deyil; gameplay fantasy-nin bir hissəsidir.**

---

# 18. Memorable Moments

## Hacknet

Yadda qalan:

- öz sisteminin hack olunması;
- UI loss;
- openCDTray;
- Project Junebug;
- final sequences.

## Midnight Protocol

Yadda qalan:

- story twists;
- special handcrafted missions;
- fourth-wall secrets;
- game/save-file ilə oynayan easter egg-lər;
- unusual boss/SysOp encounters.

### Principle

Hər iki oyun göstərir:

> **normal rule set-i nadir hallarda pozan momentlər uzunmüddətli yaddaş yaradır.**

Memorable-event density content quantity-dən ayrıca design metric kimi düşünülə bilər.

---

# 19. Product Positioning

## Hacknet

Risk:

“hacking simulator” dili technical realism expectation yarada bilər.

## Midnight Protocol

Store daha düzgün olaraq:

- tactical;
- narrative-driven;
- RPG;
- keyboard-only

deyir.

Buna baxmayaraq bəzi player-lər yenə hacking game mental model-i ilə gəlir və:

> “bu chess/board game-dir”

deyə disappointment yaşayır.

### Principle

> **Store promise yalnız theme-ni yox, dominant cognitive activity-ni izah etməlidir.**

Məsələn:

- typing?
- deduction?
- tactics?
- story?
- management?

Player hansı işi ən çox edəcəyini bilməlidir.

---

# 20. Successful Pattern-lər

Hər iki oyunda təkrarlanan:

## 20.1. Clear fantasy

Hacker olmaq güclü hook-dur.

## 20.2. Interface-as-world

UI gameplay və fiction-dır.

## 20.3. Selective authenticity

Real terminology full simulation-dan daha faydalı ola bilər.

## 20.4. Story integration

Narrative abstract mechanic-ə meaning verir.

## 20.5. Audio/visual feedback

Static computer interface-i emosional experience-ə çevirir.

## 20.6. Curiosity

Gizli məlumat və secret-lər hacker fantasy-yə çox uyğundur.

---

# 21. Fərqli failure pattern-lər

## Hacknet

```text
simple loop
→ pattern recognition
→ shallow decision
→ repetition
```

## Midnight Protocol

```text
deeper systems
→ information/cognitive load
→ uncertainty + RNG
→ failure
→ weak recovery
→ frustration
```

Bu research üçün ən vacib nəticədir.

---

# 22. Design Space xəritəsi

```text
                     MORE SYSTEMIC DEPTH
                            ↑
                            |
          Midnight Protocol|
                            |
                            |
ACCESSIBLE ----------------+---------------- COMPLEX
                            |
             Hacknet       |
                            |
                            ↓
                     LESS SYSTEMIC DEPTH
```

Bu sadə xəritədə ideal gələcək concept mütləq ortada deyil.

Amma araşdırma göstərir ki, bizim hədəf:

- Hacknet-dən daha çox decision depth;
- Midnight Protocol-dan daha az opaque friction

ola bilər.

---

# 23. Gələcək concept üçün optimal istiqamət hipotezi

Hazırkı iki oyun evidence-i əsasında:

> **“Easy to understand, hard to master” hacker/digital-investigation experience.**

Core properties:

### Immediate fantasy

İlk 5–10 dəqiqədə oyunçu:

> “mən bunu edirəm”

hissini alır.

### Low syntax tax

Commands fantasy verir, amma syntax memory əsas skill deyil.

### High information decision density

Dərinlik:

- clue;
- identity;
- permissions;
- relationships;
- network;
- trade-offs

üzərindən gəlir.

### Explainable failure

Player failure səbəbini başa düşür.

### Recon before commitment

Blind loadout azdır.

### Meaningful consequences

World/player options dəyişir.

### Flexible recovery

Səhv qərar mənalıdır, amma game-dən çıxmağa məcbur etmir.

### Curiosity rewarded

Optional exploration timer ilə davamlı cəzalandırılmır.

---

# 24. Transferable Design Principles

## Principle 1 — Fantasy first, simulation second

İki oyun da bunu təsdiqləyir.

## Principle 2 — Complexity görünə bilər, amma interaction sadə qalmalıdır

Visual/system fantasy dərin görünə bilər.

Player action grammar aydın olmalıdır.

## Principle 3 — Depth = decision quality, feature count deyil

Daha çox tool və system avtomatik dərinlik yaratmır.

## Principle 4 — Failure explainable olmalıdır

RNG dominant failure driver olmamalıdır.

## Principle 5 — Recovery challenge-in bir hissəsidir

Retry ayrıca UX deyil.

## Principle 6 — Information discovery core mechanic ola bilər

Sadəcə “lore” kimi yox.

## Principle 7 — Consequence player identity yaradır

Choice görünən future state yaratmalıdır.

## Principle 8 — Keyboard/terminal yalnız high-value action üçün istifadə edilməlidir

Repeated trivial command thematic tax-a çevrilə bilər.

## Principle 9 — Onboarding tutorialdan sonra davam edir

Systems və strategy ayrıca öyrədilməlidir.

## Principle 10 — Memorable rule-breaking moments planlaşdır

Bu genre buna xüsusilə uyğundur.

---

# 25. Opportunity Map

| Opportunity | Hacknet evidence | Midnight evidence | Potential value |
|---|---|---|---|
| Deeper information investigation | Güclü curiosity, dayaz breach loop | Investigation müsbətdir, tactical layer dominantdır | High |
| Meaningful consequence | Zəif reactivity complaint | Choice/reputation güclüdür | High |
| Deterministic tactical depth | Hacknet depth azdır | MP depth yaxşı, RNG risklidir | High |
| Recon-driven loadout | Tool-key loop | Blind/wrong loadout complaint | High |
| Hybrid keyboard UX | Terminal fantasy, shell friction | Keyboard fantasy, efficiency friction | High |
| Returning-player support | Command memory problemi | Complex system memory riski | Medium-High |
| Dynamic world response | Hacknet zəifdir | MP daha çox narrative consequence verir | High |
| Creator/community content | Hacknet mod long-tail | MP Workshop/level editor mövcuddur, evidence zəifdir | Medium |

---

# 26. Risk Register

| Risk | Hacknet | Midnight Protocol | Gələcək validation |
|---|---|---|---|
| Repetition | High evidence | High evidence | 30–60 min repeated-loop playtest |
| Syntax/UI friction | Medium-High | High | novice + technical user testing |
| Complexity cliff | Lower | High | post-tutorial cohort test |
| RNG unfairness | Low | High | deterministic-vs-random prototype |
| Weak consequences | High | Lower | consequence visibility test |
| Blind planning | Low | High | recon/loadout UX test |
| Story masking weak mechanics | Medium | Medium | mechanics-only prototype |
| Technical stability | High negative driver | Medium | long-session/save-state QA |

---

# 27. Nəyi hələ bilmirik?

- Midnight Protocol-un aşağı market traction səbəbi;
- keyboard-only control-un conversion-a real təsiri;
- Steam demo conversion;
- Workshop usage;
- current patch-lərdə launch-era RNG/retry complaint-lərin nə qədər qaldığı;
- Hacknet və Midnight Protocol audience overlap-ının ölçüsü;
- broader digital-investigation games-də eyni principles-in işləyib-işləmədiyi.

Bu suallar üçün növbəti oyunlar lazımdır.

---

# 28. Comparison nəticəsi

Hacknet və Midnight Protocol birlikdə çox aydın design tension göstərir.

Hacknet deyir:

> **Fantasy-ni tez ver, controls sadə saxla.**

Amma nəticə:

> repetition və shallow decision riski.

Midnight Protocol deyir:

> **Fantasy-ni tactical depth və meaningful choice ilə dərinləşdir.**

Amma nəticə:

> complexity, fairness və recovery riski.

Bizim üçün əsas nəticə:

> **Optimal hacker/interface game nə Hacknet qədər mexaniki sadə, nə də Midnight Protocol qədər opaque tactical friction-a bağlı olmalıdır. Dərinlik information, choice, consequence və sistem əlaqələrindən gəlməli; input və failure isə mümkün qədər aydın qalmalıdır.**

Bu hələ genre-level final prinsip deyil.

Növbəti oyunlar — xüsusilə Cyber Manhunt, Mainlining və The Operator — bu hipotezin terminal hacking-dən digital investigation istiqamətinə keçəndə də işləyib-işləmədiyini test etməlidir.

---

# 29. Mənbələr

## Hacknet

- `analysis/hacknet/deep-research.md`
- `analysis/hacknet/theme-analysis.md`
- `data/processed/hacknet/statistics.json`

## Midnight Protocol

- `analysis/midnight-protocol/deep-research.md`
- `analysis/midnight-protocol/theme-analysis.md`
- `data/processed/midnight-protocol/statistics.json`

## Developer / public

Hacknet sources:
- `analysis/hacknet/deep-research.md` source section

Midnight Protocol:
- https://www.gamedeveloper.com/design/hacking-answers-tactical-narrative-game-midnight-protocol
- https://store.steampowered.com/app/1162700/
- https://www.quartertothree.com/fp/2022/01/16/midnight-protocol-hacks-into-the-sweet-spot-between-storytelling-and-strategy/
- https://www.softpedia.com/reviews/games/pc/midnight-protocol-review-534571.shtml

---

# Status

**Comparison:** tamamlanıb  
**Games:** Hacknet + Midnight Protocol  
**Növbəti research məqsədi:** terminal-hacking nəticələrini digital-investigation oyunlarında test etmək.
