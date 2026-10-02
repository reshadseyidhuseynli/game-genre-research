# Midnight Protocol — Dərin araşdırma

## Executive Summary

Midnight Protocol terminal/hacking janrında Hacknet-dən fərqli bir problem həll etməyə çalışır: hacking-i sürətli command execution kimi yox, **turn-based tactical decision system** kimi təqdim edir.

Oyun bunu üç əsas layer-i birləşdirərək edir:

```text
hacker fantasy
+
turn-based tactical network gameplay
+
story / moral choice / reputation
```

Verified Steam dataset:

- 301 English review
- 253 positive
- 48 negative
- 84.05% positive ratio

Əsas nəticə:

> **Midnight Protocol Hacknet-in shallow “tool = key” probleminə real mechanical depth əlavə edir, amma bunun əvəzində RNG/fairness, retry/recovery, loadout uncertainty, keyboard-only friction və tutorial-sonrası complexity problemləri yaradır.**

Oyunun ən güclü tərəfləri:

- hacker fantasy;
- immersion;
- story;
- turn-based planning;
- loadout/build seçimi;
- moral choice və reputation;
- stylish UI/audio;
- selective authenticity.

Ən ciddi problemlər:

- RNG səbəbilə failure-in player skill-dən ayrılması;
- rollback/retry modelinin bunu daha ağrılı etməsi;
- trace/turn-cap-lərin experimentation ilə toqquşması;
- keyboard-only control-un bəzi action-ları süni şəkildə yavaşlatması;
- tutorial-dan sonra 1–3 saatlıq mərhələdə yüksək friction;
- daha çox sistem olmasına baxmayaraq müəyyən mərhələdə repetition;
- bəzi decision/consequence-ların həddindən artıq sərt və irreversible hiss olunması.

Ən vacib product lesson:

> **Depth repetition problemini azalda bilər, amma depth özü yaxşı design demək deyil. Oyunçunun hər qərarı başa düşülən, planlana bilən və failure zamanı izah edilə bilən olmalıdır.**

Hacknet ilə birlikdə baxanda artıq iki cross-game principle güclənir:

1. **full realism lazım deyil; selective authenticity + coherent fantasy işləyir;**
2. **terminal/keyboard input fantasy-ni gücləndirir, amma interaction efficiency pozulanda novelty friction-a çevrilir.**

Ətraflı review data:

`analysis/midnight-protocol/theme-analysis.md`

---

# 1. Research Scope və Data Quality

## 1.1. Steam dataset

Snapshot: **2026-10-02**

- raw reviews: 301
- unique reviews: 301
- positive: 253
- negative: 48
- positive ratio: 84.05%
- median playtime at review: 11.70h
- average positive review playtime: 17.01h
- average negative review playtime: 5.59h

Raw/processed data:

- `data/raw/midnight-protocol/`
- `data/processed/midnight-protocol/`
- `data/reports/midnight-protocol/summary.md`

## 1.2. Semantic audit

Oxunub:

- bütün 48 negative review;
- 50 ən helpful positive review;
- 50 low-playtime review;
- 25 recent positive review.

Bu, negative failure pattern-ləri üçün yüksək confidence verir.

## 1.3. Xarici mənbələr

İstifadə olunub:

- Steam Store;
- Game Developer Sam Agten interview;
- Quarter to Three review;
- Softpedia review;
- əvvəlki kickoff external research.

## 1.4. Limitations

- Steam reviewer-lər bütün player population deyil;
- overall recommendation aspect sentiment deyil;
- candidate theme scan regex-based retrieval-dir;
- playtime correlation causation deyil;
- store display review count ilə Steam API snapshot fərqlənə bilər;
- bəzi launch-era problemlər patch-lərlə dəyişmiş ola bilər.

---

# 2. Product / Market Snapshot

Steam App ID: **1162700**

- Developer: LuGus Studios
- Publisher: Iceberg Interactive
- Release: 13 October 2021
- Base US price: $14.99
- Genres: Action, Adventure, Indie, RPG, Strategy
- Steam Workshop
- level editor
- Steam Cloud
- keyboard-only positioning

Steam store description:

> tactical narrative-driven RPG with unique keyboard-only controls

Store promise üç hissəyə bölünür:

1. hacking fantasy;
2. tactical RPG;
3. story/choice.

Bu Hacknet-dən vacib şəkildə fərqlənir.

Hacknet əsasən:

> “terminal hacking simulator / hacker experience”

kimi oxunur.

Midnight Protocol isə:

> “hacking theme içində tactical RPG”

kimi daha düzgün anlaşılır.

Bu distinction düzgün kommunikasiya edilməsə expectation mismatch yaranır.

---

# 3. Midnight Protocol əslində necə oyundur?

Ən düzgün qısa təsvir:

> **Keyboard-only interface daxilində oynanan turn-based tactical network RPG və narrative puzzle game.**

Oyun real hacking simulator deyil.

Core mission loop:

```text
mission seç
→ available intel oxu
→ programs/hardware loadout qur
→ network-ə daxil ol
→ node-lar arasında hərəkət et
→ ICE / SysOp / trace idarə et
→ objective və optional data tap
→ qərar ver
→ network-dən çıx
→ reputation/story nəticəsi al
→ yeni tool / mission / branch aç
```

Hər turn-də əsas grammar sadədir:

- move;
- interact;
- ability/program;
- end turn.

Dərinlik həmin sadə grammar ətrafında qurulur.

---

# 4. Əsas player fantasy

Midnight Protocol-un fantasy-si sadəcə:

> “hacker olum”

deyil.

Daha düzgün:

> **“hazırlıq görən, network daxilində tactical qərarlar verən və hansı hacker olmaq istədiyinə özü qərar verən operator olum.”**

Fantasy üç layer-də qurulur.

## 4.1. Physical fantasy

Real keyboard istifadə olunur.

Oyunçu command yazır.

Bu physical input fictional activity ilə uyğun gəlir.

## 4.2. Tactical fantasy

Oyunçu:

- loadout hazırlayır;
- route seçir;
- trace idarə edir;
- ICE və SysOp threat-lərini qiymətləndirir;
- resource bölür.

## 4.3. Identity fantasy

Oyunçu:

- white/grey/black hat reputation;
- moral choice;
- target haqqında optional məlumat;
- side mission;
- bank/data/privacy qərarları

ilə “necə hacker” olduğunu formalaşdırır.

Hacknet-də birinci layer çox güclüdür.

Midnight Protocol ikinci və üçüncü layer-i daha çox inkişaf etdirir.

---

# 5. İnsanlar niyə başlayır?

## 5.1. Distinctive keyboard-only hook

Screenshot və store description-da dərhal fərqlənir.

“Only keyboard”:

- qeyri-adi görünür;
- hacker fantasy-ni bir cümlədə izah edir;
- conventional game controls-dan fərqlənir.

Bu yaxşı marketing hook-dur.

## 5.2. Hacking genre audience

Review-lərdə davamlı müqayisələr var:

- Hacknet;
- Uplink;
- NITE Team 4;
- Netrunner;
- Zachtronics.

Deməli product mövcud niche audience-in tanıdığı mental model-ə düşür.

## 5.3. Story premise

Player character Data əvvəl doxx olunub.

Core mystery:

> kim və niyə?

Bu dərhal player goal yaradır.

## 5.4. Tactical novelty

Hacking game üçün turn-based model qeyri-adidir.

Bu həm novelty, həm də riskdir.

---

# 6. İnsanlar niyə davam edir?

Review evidence-ə görə əsas retention səbəbləri:

1. story;
2. tactical system mastery;
3. new programs/hardware;
4. moral choices/reputation;
5. side missions;
6. discovery/secrets;
7. build experimentation;
8. hacker fantasy;
9. atmosphere.

STORY_NARRATIVE candidate-i:

- 136 review
- dataset-in 45.18%-i.

10h+ cohort-da story mention edən 100 review-dan yalnız 4-ü negative-dir.

Bu çox güclü retention siqnalıdır.

---

# 7. Onboarding və ilk sessiya

## 7.1. İlk saat tam disaster deyil

0–1h:

- 21 reviews
- 76.19% positive.

Yəni interface dərhal bütün oyunçuları itirmir.

Bir çox early review:

- keyboard-only control-un tez başa düşüldüyünü;
- tutorial-ın faydalı olduğunu;
- visual presentation-ın güclü olduğunu

deyir.

## 7.2. Əsas problem 1–3h-dır

1–3h:

- 45 reviews
- yalnız 62.22% positive.

Bu dataset-də ən zəif cohort-dur.

Bu çox vacibdir.

Tutorial ilk mechanics-i izah edə bilir.

Problem daha sonra başlayır:

- real loadout decisions;
- trace;
- randomness;
- SysOp;
- limited slots;
- failure/retry;
- harder missions

birlikdə işə düşəndə.

Yəni:

> **initial onboarding ilə systems onboarding eyni şey deyil.**

## 7.3. Developer intent ilə uyğunluq

Developer Sam Agten onboarding-in çox çətin olduğunu və tutorial/demo-nun ən çox iteration edilən hissə olduğunu deyir.

Bu review pattern ilə uyğun gəlir.

Ancaq lesson budur:

> Tutorial command-ları öyrətməklə bitmir. Oyunçuya sistemlər arasındakı decision model-i də öyrətmək lazımdır.

---

# 8. Core Loop və System Depth

Midnight Protocol Hacknet-dən daha dərin core loop qurur.

Əlavə decision layer-ləri:

- deck/loadout;
- limited slots;
- memory/slices;
- stealth vs aggression;
- ICE;
- SysOp;
- route;
- trace;
- optional objectives;
- reputation consequences.

Bu real improvement-dir.

Amma iki problem qalır.

## 8.1. Mandatory tools real choice-ni azalda bilər

Bir review-da oyunçu 5 slot-dan:

- cloak;
- sniffer;
- dagger

kimi tool-ların praktiki olaraq məcburi olduğunu qeyd edir.

Əgər 5 slot-dan 3-ü mandatory-dirsə:

> 5 seçim yoxdur.

Real decision space daha kiçikdir.

## 8.2. Dominant build problemi

Long-play positive review-lərdə belə qeyd olunur ki:

- çox program var;
- amma effektiv bir configuration tapdıqdan sonra çox mission üçün onu dəyişməyə ehtiyac azalır.

Bu classic build-system problemidir:

> content variety var, strategic necessity azdır.

---

# 9. Turn-based model nəyi həll edir?

Developer əvvəl real-time model düşünüb.

Playtest nəticəsində:

- stressli;
- fun olmayan

hiss etdiyi üçün turn-based-a keçib.

Bu qərarın real üstünlükləri review-lərdə görünür.

## 9.1. Speed requirement azalır

Oyunçu typing sürəti ilə deyil, planla yarışır.

## 9.2. Düşünmə vaxtı artır

Network state-i analiz etmək olur.

## 9.3. Accessibility artır

Non-technical və slow typist player üçün daha əlçatandır.

## 9.4. Tactical identity yaranır

Oyun Hacknet clone olmaqdan çıxır.

---

# 10. Turn-based model hansı yeni problemi yaradır?

## 10.1. “Hacking yox, board game” expectation mismatch

Bütün negative review audit-də ən aydın theme-lərdən biri budur.

Bəzi oyunçu üçün:

- nodes = board spaces;
- programs = abilities/cards;
- SysOps = enemy pieces;
- two actions = board-game action economy.

Bu onlar üçün hacking fantasy-ni zəiflədir.

Əsas problem mechanic-in keyfiyyəti yox, expectation-dır.

Store page tactical RPG deyir, amma “hacking” word-u daha güclü prior expectation yarada bilər.

## 10.2. Typing-in gameplay funksiyası azalır

Real-time Hacknet-də typing:

- speed;
- execution;
- pressure

ilə bağlıdır.

Turn-based Midnight Protocol-da isə typing bəzən sadəcə UI layer-dir.

Bu bəzi reviewer-lərdə belə sual yaradır:

> əgər time pressure yoxdur, niyə click etmək əvəzinə bunu yazmalıyam?

Deməli input thematicdir, amma mechanical necessity hər zaman güclü deyil.

---

# 11. RNG və fairness

Bu oyunun əsas dizayn problemi budur.

RNG_FAIRNESS:

- 36 mentions
- 13 negative
- 36.11% negative
- overall baseline-dan 2.26× yüksək.

Bütün 48 negative review audit-i də bunu təsdiqləyir.

Ən çox qeyd olunan nümunələr:

- trace chance;
- cloak probability;
- SysOp movement;
- hidden ICE;
- critical-like events;
- mission state uncertainty.

Problem randomness özü deyil.

Problem:

> oyunçu failure-i skill feedback kimi istifadə edə bilmir.

Hacknet-də uğursuzluq tez-tez:

> “daha sürətli olmalıydım”

kimi anlaşılır.

Midnight Protocol-da bəzi failure-lər:

> “daha yaxşı roll gəlməli idi”

kimi anlaşılır.

Bu mastery satisfaction-a zərbə vurur.

---

# 12. Retry / rollback / recovery

RNG problemindən sonra ikinci böyük risk budur.

RETRY_ROLLBACK:

- 20 mentions
- 35% negative.

Complaint-lər:

- mission restart;
- rollback;
- wrong loadout ilə ilişmək;
- re-plan etmək imkanı;
- manual save;
- failed mission-in permanent bağlanması;
- game restart ilə workaround.

Əsas design principle:

> **Failure cost-u challenge ilə proporsional olmalıdır.**

Əgər player:

- bütün relevant info-ya sahib deyil;
- random outcome yaşayır;
- sonra permanent content itirirsə

sistem unfair hiss olunur.

---

# 13. Trace və urgency

Trace əvvəlcə yaxşı tension yaradır.

Bu hacker fantasy üçün vacibdir.

Amma Midnight Protocol-da trace eyni zamanda:

- action budget;
- exploration budget;
- optional content budget

olur.

Bəzi review-lərdə trace:

- interesting;
- exciting;
- strategic

kimi görünür.

Digərlərində isə:

- experimentation-ı cəzalandırır;
- exploration-ı məhdudlaşdırır;
- mandatory cloak slot yaradır;
- luck dependency artırır.

URGENCY_TRACE candidate-lərinin 50%-i negative review-dur.

Bu volume aşağıdır, amma semantic audit güclüdür.

---

# 14. Repetition

Midnight Protocol Hacknet-dən daha çox variation və build depth verir.

Amma repetition yenə mövcuddur.

REPETITION:

- 19 mentions;
- 36.84% negative;
- baseline-dan 2.31× yüksək.

Əsas recurring grammar:

```text
move
→ inspect/sniff
→ deal with ICE
→ manage trace
→ end
→ repeat
```

Mission-specific twist-lər bunu qırır.

Bəzi long-play positive review-lər:

- boss-like encounters;
- handcrafted missions;
- special one-off mechanics;
- side missions

sayəsində late game-in daha güclü olduğunu qeyd edir.

Bu 10h+ cohort-un çox yüksək 95.51% positive ratio-su ilə uyğun gəlir.

Amma bu causation deyil.

---

# 15. UI/UX və Keyboard-only

## 15.1. Niyə işləyir?

Developer-in məqsədi:

> fiziki keyboard-u fantasy-nin hissəsinə çevirmək.

Review-lərdə bu açıq şəkildə işləyir.

Positive feedback:

- typing satisfying;
- keyboard hacker fantasy-ni artırır;
- mouse olmaması distinctive hiss edir;
- “in the zone” state yaradır.

## 15.2. Niyə işləmir?

Negative feedback:

- click-lə daha sürətli ediləcək action-lar;
- node name yazmaq;
- repeated “end”;
- typo;
- help output discoverability;
- command alias problemləri;
- menu navigation;
- command context.

Ən vacib nəticə:

> **immersive interaction ilə efficient interaction eyni şey deyil.**

Gələcək oyunda hər input hər ikisini mümkün qədər təmin etməlidir.

---

# 16. Realism və Authenticity

Developer açıq deyir:

> real hacking simulyasiyası məqsəd deyil.

Review-lərin böyük hissəsi bunu qəbul edir.

Positive player-lər tez-tez:

- “real deyil”;
- “gameified”;
- “puzzle/strategy”

deyib yenə oyunu çox bəyənirlər.

Deməli Hacknet-də tapılan principle burada da görünür:

> **technical realism requirement deyil; coherent selective authenticity daha vacibdir.**

Real terms, terminal, network graph, programs və cybersecurity references fantasy-ni dəstəkləyir.

---

# 17. Narrative və Content Design

Story oyunun ən böyük üstünlüklərindən biridir.

Narrative delivery:

- email;
- messages;
- mission data;
- side stories;
- decisions;
- reputation;
- network findings.

Review-lərdə story:

- gripping;
- surprising;
- morally interesting;
- memorable

kimi təsvir olunur.

Bəzi negative feedback:

- twist-lərin kifayət qədər grounding olmaması;
- late story-nin qarışıqlaşması;
- müəyyən choice consequence-ların ağır olması

ilə bağlıdır.

Amma overall story signal çox güclüdür.

---

# 18. Choice, Reputation və Hacker Identity

Midnight Protocol-un Hacknet-dən ən vacib fərqi budur.

Player:

- bank hesabına toxuna bilər;
- privacy-ni qoruya bilər;
- black/white/grey hat direction seçə bilər;
- mission qəbul/reject edə bilər;
- side content aça və bağlaya bilər;
- endings-ə təsir edə bilər.

Bu:

> “hacker kimi hiss edirəm”

fantasy-sini:

> “mən necə hackerəm?”

səviyyəsinə çıxarır.

Bu çox güclü design opportunity-dir.

---

# 19. Investigation və Discovery

Midnight Protocol-da:

- intranet;
- optional intel;
- side information;
- hidden clues;
- secrets;
- easter eggs

var.

Developer curiosity-ni “real hacker” davranışının ən həqiqi tərəflərindən biri kimi görür.

Bu Hacknet ilə ortaqdır.

Amma difference:

Hacknet-də filesystem curiosity daha organic görünür.

Midnight Protocol-da tactical mission grammar daha dominantdır.

Bu gələcək oyun üçün opportunity göstərir:

> Hacknet-in organic information exploration-u + Midnight Protocol-un meaningful choices-i birləşdirilə bilər.

---

# 20. Audio / Visual Presentation

Positive feedback güclüdür.

Praise:

- minimalist UI;
- node animations;
- cyberpunk visual language;
- sound feedback;
- atmosphere;
- procedural/music feel.

Professional review-lərdə soundtrack variety bəzi hallarda zəiflik kimi qeyd olunur.

Lakin ümumi təqdimat oyunun ən güclü elementlərindəndir.

Bu genre üçün artıq ikinci dəfə eyni principle görünür:

> **audio/visual polish fake computer interface-i “software”dən “world”ə çevirir.**

---

# 21. Technical Issues

BUGS_COMPATIBILITY candidate sayı:

- 12;
- 4 negative;
- 33.33% negative.

Volume böyük deyil.

Amma report-larda:

- softlock;
- audio bug;
- localization text scaling;
- mission state;
- control/alias edge cases

görünür.

Hacknet ilə müqayisədə technical complaints əsas dominant failure deyil.

---

# 22. Audience Segments

## 22.1. Hacker fantasy audience

Axtardığı:

- keyboard;
- terminal;
- cyber aesthetic;
- “I’m in” fantasy.

Midnight Protocol burada güclüdür.

## 22.2. Tactical/puzzle audience

Axtardığı:

- planning;
- loadout;
- action economy;
- build;
- mission optimization.

Bu Midnight Protocol-un Hacknet-dən daha yaxşı xidmət etdiyi audience-dir.

## 22.3. Narrative RPG audience

Axtardığı:

- characters;
- mystery;
- choice;
- reputation;
- endings.

Oyunun çox güclü ikinci audience-i budur.

## 22.4. Real-hacking/simulation audience

Bu audience risklidir.

Midnight Protocol özünü simulator-dan daha çox tactical RPG kimi position etdiyi üçün Hacknet-dən daha yaxşı expectation management edir.

Amma bəzi reviewer yenə:

> “bu hacking deyil, board game-dir”

deyir.

---

# 23. Developer Intent vs Player Outcome

| Developer intent | Player outcome |
|---|---|
| Keyboard immersion | Güclü fantasy yaradır, amma UX friction realdır |
| Fun over realism | Böyük ölçüdə uğurludur |
| Turn-based planning | Speed stress azalır, tactical identity yaranır |
| Simple board-game grammar | Öyrənilə bilir, amma system layering 1–3h friction yaradır |
| Deep build options | Real choice var, amma mandatory/dominant build riskləri qalır |
| Narrative focus | Güclü retention driver-dir |
| Curiosity/secrets | Positive, amma core tactical loop qədər dominant deyil |

---

# 24. Uğurun izah hipotezləri

## 24.1. Distinctive concept

Keyboard-only tactical hacking RPG asanlıqla fərqlənir.

## 24.2. Strong experience stack

```text
typing
+ tactics
+ story
+ choices
+ cyber presentation
```

bir-birini dəstəkləyir.

## 24.3. Real player agency

Hacknet-dən fərqli olaraq player identity və mission choice daha sistemikdir.

## 24.4. Narrative tactical gameplay-i mənalı edir

Abstract nodes sadəcə puzzle deyil; story context daşıyır.

## 24.5. Long-session audience üçün yüksək satisfaction

10h+ review-lərin 95.51%-i positive-dir.

Bu selection bias daşısa da, oyunu qəbul edən audience-də deep satisfaction olduğunu göstərir.

---

# 25. Niyə daha böyük hit olmayıb? — açıq hipotez

Bu sualın tam cavabı dataset-də yoxdur.

Steam store current display ilə verified API review snapshot arasında da count fərqi var, ona görə traction comparison ehtiyatla aparılmalıdır.

Mövcud evidence bir neçə mümkün izah verir:

## 25.1. Concept izahı çətindir

“Hacking game” deyəndə bəzi oyunçu Hacknet/Uplink gözləyir.

“Tactical RPG” deyəndə isə terminal/keyboard niche görünür.

Product iki audience arasında qalır.

## 25.2. Keyboard-only yüksək-friction hook ola bilər

Fərqləndirir, amma eyni zamanda audience-i daraldır.

## 25.3. İlk 1–3 saat risklidir

Potential player tutorial-dan sonra core system complexity ilə üzləşir.

## 25.4. Tactical board-game identity hacking audience-in bir hissəsinə uyğun deyil

Product quality yaxşı olsa da TAM daha dar ola bilər.

## 25.5. Discoverability/marketing

Recent review-lərdə “niyə bu oyun bu qədər bilinmir?” fikri görünür.

Amma bunun səbəbini public review data ilə sübut etmək mümkün deyil.

**Confidence: Low-Medium**

---

# 26. Bizim üçün saxlanmalı design dərsləri

## Saxlamağa dəyər

### 1. Fantasy + systems integration

Hacker fantasy yalnız skin deyil.

Interaction-la bağlanmalıdır.

### 2. Moral identity

Player “hacker” olmaqdan əlavə “necə hacker” olduğunu seçə bilər.

### 3. Tactical planning

Speed skill yeganə challenge forması olmamalıdır.

### 4. Loadout preparation

Mission öncəsi qərar gameplay-in hissəsi ola bilər.

### 5. Narrative consequence

Choice story və future options-a təsir edə bilər.

### 6. Selective authenticity

Real jargon və coherent logic kifayətdir.

### 7. Keyboard as fantasy device

Fiziki input theme ilə uyğun gələndə immersion artır.

---

# 27. Qaçmalı olduğumuz risklər

## 1. Hidden information + irreversible failure

Bu fairness-i dağıda bilər.

## 2. RNG nəticəni skill-dən çox müəyyən etməsi

Failure learnable qalmalıdır.

## 3. Mandatory build masquerading as choice

Tool sayı depth demək deyil.

## 4. Repeated command overhead

Thematic input mechanical tax-a çevrilməməlidir.

## 5. Tutorial sonrası complexity cliff

İlk tutorial keçildikdən sonra onboarding davam etməlidir.

## 6. Timer/trace curiosity-ni öldürməsi

Investigation üçün nəfəs sahəsi lazımdır.

## 7. Genre expectation mismatch

Store promise actual core loop-u düzgün anlatmalıdır.

---

# 28. Opportunity-lər

## 28.1. Hacknet immersion + Midnight agency

Ən güclü opportunity:

- Hacknet-in organic filesystem/information discovery-si;
- Midnight Protocol-un choice/reputation/consequence sistemi.

## 28.2. Explainable tactical hacking

Tactical depth saxla, amma randomness minimum və readable olsun.

## 28.3. Recon-before-loadout

Mission haqqında əvvəlcədən:

- partial intel;
- target behavior;
- known defenses;
- uncertainty level

ver.

Player risk seçsin.

## 28.4. Flexible failure recovery

Retry:

- re-plan;
- loadout change;
- checkpoint;
- optional consequence

ilə işləyə bilər.

## 28.5. Hybrid input

Keyboard fantasy saxlanıla bilər, amma:

- autocomplete;
- history;
- aliases;
- click-equivalent optional shortcuts;
- context-aware suggestions

friction-i azalda bilər.

## 28.6. Information → decision → consequence loop

```text
discover information
→ interpret
→ choose
→ act
→ world changes
```

bu janr üçün çox güclü systemic core ola bilər.

---

# 29. Hacknet ilə ilkin yekun fərq

Hacknet:

> daha sadə, daha dərhal fantasy, daha az systemic choice.

Midnight Protocol:

> daha dərin tactical/identity systems, amma daha yüksək cognitive və fairness risk.

Bunu belə xülasə etmək olar:

```text
Hacknet
fast fantasy payoff
↓
simple loop
↓
repetition risk

Midnight Protocol
deeper decision model
↓
higher cognitive/system load
↓
fairness + onboarding + friction risk
```

Bizim gələcək concept üçün hədəf bu iki ekstrem arasında optimal nöqtə tapmaqdır.

---

# 30. Açıq suallar

1. Midnight Protocol-un aşağı review volume-unun əsas market səbəbi nədir?
2. Keyboard-only input audience-i nə qədər daraldıb?
3. Demo conversion haqqında public data varmı?
4. Workshop/level editor real long-tail yaradıbmı?
5. Turn-based və optional real-time mode arasında usage pattern məlumdurmu?
6. RNG complaint-lərin hansı hissəsi son patch-lərdən əvvəlki versiyaya aiddir?
7. Eyni tactical depth daha deterministic sistemlə daha geniş audience tapa bilərdimi?
8. Choice/reputation sistemi başqa interface-game-lərdə də eyni dəyəri verirmi?

Bu suallar cross-game research-də izlənməlidir.

---

# 31. Mənbələr

## Daxili repository

**[D1]** `data/processed/midnight-protocol/statistics.json`

**[D2]** `data/reports/midnight-protocol/summary.md`

**[D3]** `data/processed/midnight-protocol/samples/helpful_positive.csv`

**[D4]** `data/processed/midnight-protocol/samples/helpful_negative.csv`

**[D5]** `data/processed/midnight-protocol/samples/low_playtime.csv`

**[D6]** `data/processed/midnight-protocol/samples/recent_positive.csv`

**[D7]** `analysis/midnight-protocol/theme-analysis.md`

**[D8]** `config/aspect_taxonomy.yaml`

## Xarici

**[W1] Steam Store — Midnight Protocol**  
https://store.steampowered.com/app/1162700/

**[W2] Game Developer — Hacking for answers in tactical narrative game Midnight Protocol**  
https://www.gamedeveloper.com/design/hacking-answers-tactical-narrative-game-midnight-protocol

**[W3] Quarter to Three — Midnight Protocol hacks into the sweet spot between storytelling and strategy**  
https://www.quartertothree.com/fp/2022/01/16/midnight-protocol-hacks-into-the-sweet-spot-between-storytelling-and-strategy/

**[W4] Softpedia — Midnight Protocol Review**  
https://www.softpedia.com/reviews/games/pc/midnight-protocol-review-534571.shtml

---

# Status

**Mərhələ:** Midnight Protocol per-game deep research — əsas mərhələ tamamlanıb  
**Dataset:** 301 verified English Steam review  
**Negative reviews audited:** 48/48  
**Full-corpus candidate coverage:** 75.08%  
**Növbəti:** `analysis/comparisons/hacknet-vs-midnight-protocol.md`
