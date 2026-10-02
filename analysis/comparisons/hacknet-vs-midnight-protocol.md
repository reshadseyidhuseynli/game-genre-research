# Hacknet vs Midnight Protocol — Dizayn və oyunçu Response Müqayisəsi

## 1. müqayisə Question

Bu müqayisənin əsas sualı:

> **Eyni geniş “terminal/hacking” rol hissi-si daxilində Hacknet-in sadə, real-time və əlçatanlıq-first modeli ilə Midnight Protocol-un daha dərin, turn-based və tactical modeli oyunçu təcrübəsini necə dəyişir?**

Məqsəd “hansı oyun daha yaxşıdır?” demək deyil.

Məqsəd:

- hansı problem hansı yanaşma ilə həll olunur;
- hansı yeni risk yaranır;
- hansı dizayn principle iki oyunda da təkrarlanır;
- gələcək yeni concept üçün hansı middle-ground daha güclü görünür

suallarına cavab verməkdir.

---

# 2. Niyə bu iki oyun müqayisə edilə bilər?

Ortaq əsaslar:

- hacker rol hissi;
- terminal/keyboard qarşılıqlı əlaqə;
- fictional computer environment;
- single-oyunçu;
- hekayə-driven structure;
- real texniki terminlərin seçilmiş istifadəsi;
- abstract hacking mexanikalar;
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

Bu fərq bizə **əlçatanlıq ↔ dərinlik** kompromis-unun real oyunçu response-a necə təsir etdiyini görməyə imkan verir.

---

# 3. məlumat toplusu snapshot

| Metrik | Hacknet | Midnight Protocol |
|---|---:|---:|
| Verified English Steam reviews | 11,773 | 301 |
| müsbət | 11,082 | 253 |
| mənfi | 691 | 48 |
| müsbət ratio | **94.13%** | **84.05%** |
| Avg oyun müddəti — müsbət rəy | 13.06h | 17.01h |
| Avg oyun müddəti — mənfi rəy | 4.40h | 5.59h |
| Median oyun müddəti | — | 11.70h |

məlumat toplusu ölçüləri çox fərqlidir. Buna görə absolute mention count-lar oyunlar arasında birbaşa müqayisə edilmir.

Əsas müqayisə:

- nümunə direction;
- baseline-a nisbət;
- məna yönümlü yoxlama;
- oyun müddəti qrup shape;
- yaradıcı intent.

---

# 4. oyun müddəti qrup müqayisəsi

| oyun müddəti | Hacknet müsbət | Midnight Protocol müsbət |
|---|---:|---:|
| 0–1h | **67.05%** | 76.19% |
| 1–3h | 86.59% | **62.22%** |
| 3–10h | 95.79% | 75.95% |
| 10h+ | 98.57% | 95.51% |

Bu table ən vacib müqayisə siqnallarından biridir.

## Hacknet

Ən böyük risk:

> **ilk saat**

Terminal və command vocabulary dərhal çətinlik yarada bilər.

Amma oyunu keçən reviewer qrup-larda recommendation sürətlə yüksəlir.

## Midnight Protocol

İlk saat Hacknet-dən daha yaxşı görünür.

Əsas risk:

> **1–3 saat**

Yəni təlim hissəsiın özü yox, tutorialdan sonra:

- loadout;
- RNG;
- trace;
- SysOp;
- limited slots;
- uğursuzluq/retry

birlikdə işləməyə başlayanda satisfaction düşür.

### Əsas dərs

> **First-time ilkin öyrətmə yalnız controls öyrətmək deyil. Core systems-in ilk dəfə bir-biri ilə qarşılaşdığı nöqtə ayrıca ilkin öyrətmə mərhələsidir.**

---

# 5. Hook və oyunçu Rol hissi

## Hacknet

Əsas rol hissi:

> “Terminalda hacker oluram.”

Çox sadə və dərhal başa düşülür.

Rol hissi-ni yaradan:

- terminal;
- commands;
- IP;
- ports;
- filesystem;
- trace;
- music;
- files.

## Midnight Protocol

Rol hissi daha layered-dir:

> “Keyboard ilə network daxilində tactical hacker oluram və hansı hacker olmaq istədiyimə qərar verirəm.”

Əlavə qat-lər:

- loadout;
- tactical network;
- hat reputation;
- moral decisions;
- programs/hardware.

### Nəticə

Hacknet rol hissi-ni **daha tez** satır.

Midnight Protocol rol hissi-ni **daha dərindən** sistemləşdirir.

Bu kompromis-dur, superiority deyil.

---

# 6. Realizm: hər iki oyun eyni fundamental nəticəyə gəlir

Hacknet yaradıcı intent:

> oyunçunu hacker kimi hiss etdirmək.

Midnight Protocol yaradıcı intent:

> fun game first, hacking mövzu second.

Hər iki oyunda:

- real terminology;
- terminal language;
- recognizable cyber concepts

istifadə edilir.

Amma heç biri full real-world hacking simulation deyil.

oyunçu geribildirim də bunu əsasən qəbul edir.

## oyunlararası principle

> **Bu janr üçün tam realizm tələb deyil. seçilmiş həqiqilik hissi + ardıcıl rol hissi daha sağlam hədəfdir.**

realizm yalnız:

- marketing “real simulator” expectation yaradanda;
- interface real sistemə çox bənzəyib davranışı fərqli olanda

problemə çevrilir.

**etibarlılıq: High**

---

# 7. Terminal / Keyboard kompromis

## Hacknet

Terminal:

- əsas rol hissi amil;
- GUI ilə birlikdə işləyir;
- technical user real Unix behavior gözləyə bilər.

Əsas complaint:

> “real terminal kimi görünür, amma real terminal kimi davranmır.”

## Midnight Protocol

Keyboard-only:

- daha güclü thematic commitment;
- distinctive məhsul identity;
- yaradıcı tərəfindən əsas oyuna dalma hissi source kimi dizayn edilib.

Əsas complaint:

> “click-lə daha sürətli edəcəyim şeyi niyə yazmalıyam?”

### oyunlararası nəticə

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
- rol hissi payoff sürətlidir.

Problem:

- nümunə tez görünür;
- tool = key olur;
- qərar density aşağı düşür.

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

- daha çox planlama;
- build;
- tactical route;
- resource management;
- nəticə.

Problem:

- mürəkkəblik;
- hidden information;
- RNG;
- repetitive low-value commands;
- retry cost.

### Əsas lesson

> **Hacknet-də problem “too little qərar”; Midnight Protocol-da risk “too much system çətinlik”.**

Gələcək concept üçün məqsəd “daha çox mexanika” deyil.

Məqsəd:

> **yüksək meaningful-qərar density.**

---

# 9. təkrarçılıq

## Hacknet

təkrarçılıq namizəd:

- 517 reviews;
- 23.21% mənfi rəy ratio;
- Hacknet baseline-dan **3.95×** yüksək mənfi concentration.

təkrarçılıq core uğursuzluq nümunə-dir.

## Midnight Protocol

təkrarçılıq namizəd:

- 19 reviews;
- 36.84% mənfi;
- Midnight baseline-dan **2.31×** yüksək.

Absolute mənfi rate daha yüksəkdir, amma relative-to-game baseline daha zəifdir.

Midnight Protocol təkrarçılıq-ı tam həll etmir, amma:

- loadout;
- mission-specific mexanikalar;
- SysOps;
- seçimlər;
- bosses;
- handcrafted levels

variation yaradır.

### Nəticə

> **System dərinlik təkrarçılıq-ı azalda bilir, amma fundamental action grammar dəyişmirsə tam yox etmir.**

**etibarlılıq: High**

---

# 10. dərinlik

## Hacknet

dərinlik daha çox:

- hekayə context;
- exploration;
- optional files

tərəfdən gəlir.

Hacking mexanika-in özü nisbətən sadədir.

## Midnight Protocol

dərinlik birbaşa oyun gedişi system-dən gəlir:

- hərəkət büdcəsi;
- loadout;
- memory/slices;
- stealth/aggression;
- route;
- trace;
- SysOp;
- ICE.

Bu Hacknet-in əsas mexaniki boşluğunu həll edir.

Amma əlavə risk:

- təlim hissəsi mürəkkəblik;
- bad RNG;
- dominant/məcburi tool-lar;
- wrong build;
- retry çətinlik.

### Principle

> **dərinlik əlavə ediləndə onun information cost-u, learning cost-u və uğursuzluq cost-u birlikdə dizayn edilməlidir.**

---

# 11. uğursuzluq modeli

Bu iki oyunun ən vacib fərqlərindən biridir.

## Hacknet

oyunçu uğursuzluq çox vaxt:

- speed;
- timing;
- əmrlərin icrası;
- trace

ilə əlaqələndirilə bilir.

oyunçu deyə bilir:

> “mən daha yaxşı etməliydim.”

## Midnight Protocol

uğursuzluq bəzən:

- random trace;
- SysOp movement;
- hidden ICE;
- wrong loadout due incomplete intel;
- percentage chance

ilə gəlir.

oyunçu deyə bilər:

> “bu dəfə roll pis idi.”

Bu mastery loop üçün daha təhlükəlidir.

### oyunlararası principle

> **uğursuzluq oyuncuya öz qərarı haqqında information verməlidir.**

Randomness:

- scenario yarada bilər;
- adaptation tələb edə bilər;

amma əsas nəticəni izah edən dominant faktor olmamalıdır.

---

# 12. Retry və Recovery

Hacknet uğursuzluq-dan sonra retry daha conventional hiss olunur.

Midnight Protocol-da isə:

- rollback;
- mission permanent outcome;
- loadout re-plan;
- no manual save;
- one-chance mission perception

daha çox complaint yaradır.

Bu çox vacib lesson-dir:

> **çətinlik dizayn ilə recovery dizayn bir sistemdir.**

Difficult mission yaxşı ola bilər.

Difficult mission + incomplete information + random uğursuzluq + weak recovery birlikdə frustration yaradır.

---

# 13. hekayə

## Hacknet

hekayə:

- mystery;
- email;
- files;
- hidden systems;
- scripted memorable moments.

Rol hissi-ni daşıyır və təkrarçılıq-a context verir.

## Midnight Protocol

hekayə:

- 45.18% namizəd əhatə;
- tactical oyun gedişi;
- seçim;
- reputation;
- side missions;
- endings

ilə daha sistemik inteqrasiya olunur.

### Ortaq nəticə

Hər iki oyunda hekayə “əlavə content” deyil.

> **hekayə core oyunda qalma sistemidir.**

### Fərq

Hacknet:

> hekayə-ni əsasən tapırsan.

Midnight Protocol:

> hekayə-ni tapırsan və qismən formalaşdırırsan.

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

Optional məlumat və secrets var.

Amma tactical board qat daha dominantdır.

seçim/reputation daha güclü olsa da organic snooping Hacknet-də daha təbii görünür.

### imkan

Gələcək oyun üçün ən güclü hybrid:

```text
Hacknet-style organic information exploration
+
Midnight Protocol-style meaningful choices/consequences
```

---

# 15. oyunçu qərar sərbəstliyi və nəticələr

## Hacknet

mövzu təhlil-də:

- PLAYER_AGENCY mənfi concentration: 2.77× baseline;
- WORLD_REACTIVITY: 3.55× baseline.

Aşağı volume, amma complaint aydındır:

- linearity;
- log-ların real nəticə yaratmaması;
- world response zəifliyi.

## Midnight Protocol

seçim/reputation:

- yüksək müsbət signal;
- long-play rəy-lərdə güclü satisfaction amil.

oyunçu:

- moral direction;
- mission;
- side content;
- reputation;
- endings

üzərində daha çox influence hiss edir.

### Nəticə

Midnight Protocol Hacknet-in əsas boşluqlarından birini real şəkildə həll edir:

> **oyunçu identity və nəticə.**

Amma bəzən nəticə həddindən artıq permanent hiss olunur.

Optimal sistem:

> meaningful, visible, recoverable-but-not-free nəticə.

---

# 16. İlkin öyrətmə

## Hacknet

ONBOARDING namizəd relative mənfi concentration:

**2.14× baseline**

Əsas problem:

- terminal vocabulary;
- nə etməli olduğunu bilməmək;
- returning-oyunçu memory.

## Midnight Protocol

Overall ONBOARDING namizəd baseline-a yaxındır.

Amma oyun müddəti qrup ciddi problem göstərir:

- 1–3h müsbət ratio yalnız 62.22%.

Burada problem basic təlim hissəsi deyil.

Problem:

> **systems ilkin öyrətmə.**

### oyunlararası principle

İlkin öyrətmə üç mərhələ olmalıdır:

1. **control ilkin öyrətmə** — hansı düymə/command;
2. **system ilkin öyrətmə** — mexanikalar necə qarşılıqlı əlaqə edir;
3. **strategy ilkin öyrətmə** — yaxşı qərar necə görünür.

Hər iki oyun fərqli mərhələdə problem yaşayır.

---

# 17. Audio və Atmosphere

Hər iki oyunda:

- sound/music;
- terminal geribildirim;
- cyber visual language

güclü müsbət signal verir.

Hacknet-də soundtrack xüsusilə iconic praise alır.

Midnight Protocol-da presentation çox bəyənilir, amma soundtrack variety üçün complaint var.

### Principle

> **Computer-interface janrında audiovisual geribildirim normal UI polish deyil; oyun gedişi rol hissi-nin bir hissəsidir.**

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

- hekayə twists;
- special handcrafted missions;
- fourth-wall secrets;
- game/save-file ilə oynayan easter egg-lər;
- unusual boss/SysOp encounters.

### Principle

Hər iki oyun göstərir:

> **normal rule set-i nadir hallarda pozan momentlər uzunmüddətli yaddaş yaradır.**

Memorable-event density content quantity-dən ayrıca dizayn metric kimi düşünülə bilər.

---

# 19. məhsul Positioning

## Hacknet

Risk:

“hacking simulator” dili technical realizm expectation yarada bilər.

## Midnight Protocol

mağaza daha düzgün olaraq:

- tactical;
- narrative-driven;
- RPG;
- keyboard-only

deyir.

Buna baxmayaraq bəzi oyunçu-lər yenə hacking game mental model-i ilə gəlir və:

> “bu chess/board game-dir”

deyə disappointment yaşayır.

### Principle

> **mağaza promise yalnız mövzu-ni yox, dominant cognitive activity-ni izah etməlidir.**

Məsələn:

- typing?
- deduction?
- tactics?
- hekayə?
- management?

oyunçu hansı işi ən çox edəcəyini bilməlidir.

---

# 20. Successful nümunələr

Hər iki oyunda təkrarlanan:

## 20.1. Clear rol hissi

Hacker olmaq güclü hook-dur.

## 20.2. Interface-as-world

UI oyun gedişi və fiction-dır.

## 20.3. seçilmiş həqiqilik hissi

Real terminology full simulation-dan daha faydalı ola bilər.

## 20.4. hekayə integration

Narrative abstract mexanika-ə meaning verir.

## 20.5. Audio/visual geribildirim

Static computer interface-i emosional experience-ə çevirir.

## 20.6. Curiosity

Gizli məlumat və secret-lər hacker rol hissi-yə çox uyğundur.

---

# 21. Fərqli uğursuzluq nümunələr

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

Bu araşdırma üçün ən vacib nəticədir.

---

# 22. dizayn Space xəritəsi

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

- Hacknet-dən daha çox qərar dərinlik;
- Midnight Protocol-dan daha az opaque çətinlik

ola bilər.

---

# 23. Gələcək concept üçün optimal istiqamət hipotezi

Hazırkı iki oyun dəlil-i əsasında:

> **“Easy to understand, hard to master” hacker/digital-investigation experience.**

Core properties:

### Immediate rol hissi

İlk 5–10 dəqiqədə oyunçu:

> “mən bunu edirəm”

hissini alır.

### Low syntax tax

Commands rol hissi verir, amma syntax memory əsas bacarıq deyil.

### High information qərar density

Dərinlik:

- clue;
- identity;
- permissions;
- relationships;
- network;
- kompromiss

üzərindən gəlir.

### Explainable uğursuzluq

oyunçu uğursuzluq səbəbini başa düşür.

### Recon before commitment

Blind loadout azdır.

### Meaningful nəticələr

World/oyunçu options dəyişir.

### Flexible recovery

Səhv qərar mənalıdır, amma game-dən çıxmağa məcbur etmir.

### Curiosity rewarded

Optional exploration timer ilə davamlı cəzalandırılmır.

---

# 24. Transferable dizayn Principles

## Principle 1 — Rol hissi first, simulation second

İki oyun da bunu təsdiqləyir.

## Principle 2 — mürəkkəblik görünə bilər, amma qarşılıqlı əlaqə sadə qalmalıdır

Visual/system rol hissi dərin görünə bilər.

oyunçu action grammar aydın olmalıdır.

## Principle 3 — dərinlik = qərar quality, feature count deyil

Daha çox tool və system avtomatik dərinlik yaratmır.

## Principle 4 — uğursuzluq explainable olmalıdır

RNG dominant uğursuzluq amil olmamalıdır.

## Principle 5 — Recovery çətinlik-in bir hissəsidir

Retry ayrıca UX deyil.

## Principle 6 — Information discovery core mexanika ola bilər

Sadəcə “lore” kimi yox.

## Principle 7 — nəticə oyunçu identity yaradır

seçim görünən future state yaratmalıdır.

## Principle 8 — Keyboard/terminal yalnız high-value action üçün istifadə edilməlidir

Repeated trivial command thematic tax-a çevrilə bilər.

## Principle 9 — İlkin öyrətmə tutorialdan sonra davam edir

Systems və strategy ayrıca öyrədilməlidir.

## Principle 10 — Memorable rule-breaking moments planlaşdır

Bu genre buna xüsusilə uyğundur.

---

# 25. imkan Map

| imkan | Hacknet dəlil | Midnight dəlil | Potential value |
|---|---|---|---|
| Deeper information investigation | Güclü curiosity, dayaz breach loop | Investigation müsbətdir, tactical qat dominantdır | High |
| Meaningful nəticə | Zəif reactivity complaint | seçim/reputation güclüdür | High |
| Deterministic tactical dərinlik | Hacknet dərinlik azdır | MP dərinlik yaxşı, RNG risklidir | High |
| Recon-driven loadout | Tool-key loop | Blind/wrong loadout complaint | High |
| Hybrid keyboard UX | Terminal rol hissi, shell çətinlik | Keyboard rol hissi, efficiency çətinlik | High |
| Returning-oyunçu support | Command memory problemi | Complex system memory riski | Medium-High |
| Dynamic world response | Hacknet zəifdir | MP daha çox narrative nəticə verir | High |
| Creator/icma content | Hacknet mod long-tail | MP Workshop/level editor mövcuddur, dəlil zəifdir | Medium |

---

# 26. Risk Register

| Risk | Hacknet | Midnight Protocol | Gələcək validation |
|---|---|---|---|
| təkrarçılıq | High dəlil | High dəlil | 30–60 min repeated-loop playtest |
| Syntax/UI çətinlik | Medium-High | High | novice + technical user testing |
| mürəkkəblik cliff | Lower | High | post-təlim hissəsi qrup test |
| RNG unfairness | Low | High | deterministic-vs-random prototype |
| Weak nəticələr | High | Lower | nəticə visibility test |
| Blind planlama | Low | High | recon/loadout UX test |
| hekayə masking weak mexanikalar | Medium | Medium | mexanikalar-only prototype |
| Technical stability | High mənfi amil | Medium | long-session/save-state QA |

---

# 27. Nəyi hələ bilmirik?

- Midnight Protocol-un aşağı bazar traction səbəbi;
- keyboard-only control-un conversion-a real təsiri;
- Steam demo conversion;
- Workshop usage;
- current patch-lərdə launch-era RNG/retry complaint-lərin nə qədər qaldığı;
- Hacknet və Midnight Protocol audience overlap-ının ölçüsü;
- broader digital-investigation games-də eyni principles-in işləyib-işləmədiyi.

Bu suallar üçün növbəti oyunlar lazımdır.

---

# 28. müqayisə nəticəsi

Hacknet və Midnight Protocol birlikdə çox aydın dizayn tension göstərir.

Hacknet deyir:

> **Rol hissi-ni tez ver, controls sadə saxla.**

Amma nəticə:

> təkrarçılıq və dayaz qərar riski.

Midnight Protocol deyir:

> **Rol hissi-ni tactical dərinlik və meaningful seçim ilə dərinləşdir.**

Amma nəticə:

> mürəkkəblik, fairness və recovery riski.

Bizim üçün əsas nəticə:

> **Optimal hacker/interface game nə Hacknet qədər mexaniki sadə, nə də Midnight Protocol qədər opaque tactical çətinlik-a bağlı olmalıdır. Dərinlik information, seçim, nəticə və sistem əlaqələrindən gəlməli; giriş üsulu və uğursuzluq isə mümkün qədər aydın qalmalıdır.**

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

## yaradıcı / public

Hacknet sources:
- `analysis/hacknet/deep-research.md` source section

Midnight Protocol:
- https://www.gamedeveloper.com/dizayn/hacking-answers-tactical-narrative-game-midnight-protocol
- https://mağaza.steampowered.com/app/1162700/
- https://www.quartertothree.com/fp/2022/01/16/midnight-protocol-hacks-into-the-sweet-spot-between-storytelling-and-strategy/
- https://www.softpedia.com/reviews/games/pc/midnight-protocol-rəy-534571.shtml

---

# Status

**müqayisə:** tamamlanıb  
**Games:** Hacknet + Midnight Protocol  
**Növbəti araşdırma məqsədi:** terminal-hacking nəticələrini digital-investigation oyunlarında test etmək.
