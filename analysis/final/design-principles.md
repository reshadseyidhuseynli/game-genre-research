# Dizayn prinsipləri — Digital investigation / interface-as-world

## 1. Məqsəd

Bu sənəd tamamlanmış oyun araşdırmalarından çıxan nəticələri konsept və prototip qərarlarında istifadə edilə bilən qaydalara çevirir.

Bu prinsiplər:
- ideya deyil;
- feature checklist deyil;
- bütün oyunlar üçün məcburi formula deyil.

Onlar yeni konsept qurulanda:
> **nəyi qorumaq, nəyi test etmək və hansı failure mode-lardan qaçmaq lazım olduğunu**

göstərir.

---

# 2. P1 — Rol hissi bir cümlədə başa düşülməlidir

Yeni konsept üçün sual:

> **Oyunçu kimdir və ekranda əsasən nə edir?**

Yaxşı cavab nümunələri:
- “terminalda hakerəm”;
- “sahə agentlərini uzaqdan dəstəkləyən operatoram”;
- “itkin şəxsin telefonunu araşdırıram”;
- “dövlət müşahidə sistemində hansı məlumatın ötürüləcəyinə qərar verirəm”.

Əgər cavab:
- çox uzun;
- çox subsystem tələb edən;
- bir neçə ayrı fantasy-ni birləşdirən

formadadırsa ilkin məhsul identity-si zəifləyə bilər.

### Validation
5–10 saniyəlik store-card test:
- screenshot + 1 cümlə göstər;
- oyunçu rolunu düzgün təsvir edə bilirmi?

---

# 3. P2 — Interface menyu yox, dünya hərəkəti olmalıdır

Ən güclü reference-lərdə:
- terminal;
- phone;
- surveillance app;
- workstation

sadəcə HUD deyil.

Oyunçu:
> interface ilə dünyaya təsir edir.

Hər əsas UI action üçün sual:

> **Bu klik yalnız menu navigation-dır, yoxsa fiction daxilində real hərəkətdir?**

Daha çox ikinci variant olmalıdır.

---

# 4. P3 — Seçilmiş həqiqilik istifadə et

Tam realizm lazım deyil.

Lazımdır:
- rol hissini yaradan detal;
- inandırıcı termin;
- believable workflow;
- tanış interface behavior.

Lazım deyil:
- real-world tediousness;
- lazımsız syntax;
- uzun bürokratik friction;
- yalnız “realistic” olduğu üçün saxlanmış yavaş əməl.

### Rule
> **Real detail yalnız decision, immersion və ya clarity-yə xidmət edirsə saxlanmalıdır.**

---

# 5. P4 — Familiar interface-in əsas affordance-larını pozma

Terminal:
- history;
- editing;
- copy/paste.

Desktop:
- notes;
- windows;
- persistent workspace.

Phone:
- scroll;
- media control;
- app switching;
- contacts.

Search:
- tolerant queries;
- understandable results.

Əgər familiar shell istifadə olunur, basic expectation-lar prototype checklist-ə salınmalıdır.

---

# 6. P5 — Məlumat özü mükafat olmalıdır

Yeni clue yalnız:
> “qapını açan açar”

olmamalıdır.

Yaxşı məlumat:
- hekayəni dəyişir;
- personajı dəyişir;
- hypothesis-i dəyişir;
- social leverage verir;
- yeni risk yaradır.

### Test
Hər major clue üçün soruş:
> “Bu məlumatı tapmaqdan başqa oyunçu nə öyrəndi?”

---

# 7. P6 — Player knowledge first-class state olsun

Progression:
- konkret klik;
- konkret file;
- konkret dialogue trigger

üzərindən qurulmamalıdır.

Sistem semantic fact bilməlidir.

Məsələn:

```text
FACT:
Paul was at Location X.

SUPPORTED BY:
- photo metadata
- chat
- CCTV
```

Bir neçə source eyni fact-i sübut edə bilməlidir.

---

# 8. P7 — Evidence object yox, claim-support modeli istifadə et

“Doğru file” sistemi əvəzinə:

```text
claim
+ supporting evidence
+ confidence
```

modeli daha güclüdür.

Bu:
- alternative solution;
- partial success;
- better feedback;
- stronger deduction

yaradır.

---

# 9. P8 — Eyni nəticəyə bir neçə keçərli yol olmalıdır

Minimum:
- technical route;
- social route;
- observational route;
- documentary route

kimi müxtəlif yol tipləri düşünülə bilər.

Bütün fact-lar üçün 4 route lazım deyil.

Amma kritik progression fact-ları:
> yalnız bir pixel / bir exact query / bir exact line

üzərindən açılmamalıdır.

---

# 10. P9 — Guidance procedure-a kömək etsin, interpretation-a yox

Guide/NPC/system:
- tool-u izah edə bilər;
- objective verə bilər;
- missing step barədə işarə edə bilər.

Amma:
- hansı clue vacibdir;
- kim yalan danışır;
- hansı nəticə doğrudur

sualını həll etməməlidir.

### Rule
> **Guide “nə edə bilərsən?” desin, “nə düşünməlisən?” yox.**

---

# 11. P10 — External memory core feature-dir

Investigation oyununda persistent workspace lazımdır.

Minimum düşünüləcək elementlər:
- pinned facts;
- notes;
- source link;
- timeline;
- entity relation;
- search history.

Amma system:
- auto-answer;
- auto-theory

verməməlidir.

### Rule
> **Yadda saxla və təşkil et; interpretasiya etmə.**

---

# 12. P11 — Controlled noise saxla

Əgər hər content relevant-dirsə:
> relevance tapmaq gameplay deyil.

Əgər çox noise varsa:
> frustration yaranır.

Sağlam model:
- believable incidental content;
- strong organization;
- optional detail;
- clear revisit tools.

Bu xüsusilə:
- phone;
- email;
- social profile;
- file system

tipli dünyalarda vacibdir.

---

# 13. P12 — Character data mechanic resource olsun

Personaj haqqında məlumat:
- yalnız lore deyil.

O, istifadə edilə bilər:
- trust;
- social engineering;
- contradiction;
- leverage;
- ethical context;
- evidence.

Beləliklə:
> character writing gameplay-dan ayrılmır.

---

# 14. P13 — Decision grammar dəyişməlidir

Yeni level/case yalnız:
- yeni ad;
- yeni şəkil;
- yeni mətn

verməməlidir.

Ən azı bir şey dəyişməlidir:
- objective;
- tool availability;
- source reliability;
- risk;
- consequence;
- time structure;
- social relationship;
- valid solution route.

### Rule
> **Content dəyişməsi yox, qərar strukturu dəyişməsi repetition-i qırır.**

---

# 15. P14 — Mechanic depth reuse + recombination-dan gəlir

Yeni mechanic:
- tutorial;
- bir use;
- yox olur

modelindədirsə system mastery yaratmır.

Core mechanic:
- ən azı bir neçə dəfə;
- fərqli context-də;
- başqa mechanics ilə birlikdə

istifadə olunmalıdır.

---

# 16. P15 — Choice sayını yox, state divergence-i ölç

Dialogue variant sayı:
> agency metric deyil.

Hər major choice üçün bax:
- hansı münasibət dəyişir?
- hansı məlumat gəlir?
- hansı route bağlanır/açılır?
- hansı risk yaranır?
- hansı ending state dəyişir?

### Rule
> **Əgər bütün cavablar eyni state-ə gedirsə choice kosmetikdir.**

---

# 17. P16 — Consequence iki mərhələli olsun

Sağlam consequence:

```text
choice
→ immediate local response
→ delayed larger effect
```

Immediate:
- oyunçu sistemin eşitdiyini anlayır.

Delayed:
- uncertainty və drama qalır.

Bu Orwell-in güclü tərəflərindən biridir.

---

# 18. P17 — Moral ambiguity designer answer key olmamalıdır

Moral choice:
- iki legitim mövqe;
- fərqli cost;
- incomplete information;
- visible context

yaratmalıdır.

Zəif model:
- “good ending” üçün gizli etik cavab.

### Rule
> **Player öz seçimini sonradan müdafiə edə bilməlidir, hətta nəticə pis olsa belə.**

---

# 19. P18 — Failure cavabı yox, problem sahəsini göstərsin

Wrong answer feedback:
- identity problem;
- timeline conflict;
- evidence insufficient;
- source unreliable

kimi istiqamət verə bilər.

Amma:
- exact answer

verməməlidir.

Bu trial-and-error-ı reasoning-ə qaytarır.

---

# 20. P19 — Recovery experimentation-a uyğun olmalıdır

Əgər oyun:
- branch;
- moral choice;
- tactical plan;
- evidence submission

təklif edirsə,

recovery:
- checkpoint;
- rollback;
- branch replay;
- fast-forward;
- save

ilə uyğun olmalıdır.

### Rule
> **Long-run consequence + no recovery yalnız yüksək information certainty olduqda istifadə edilməlidir.**

---

# 21. P20 — İlk saat core fantasy-nin miniaturu olmalıdır

İlk sessiyada:
- ən yaxşı mechanic;
- əsas rol;
- bir real “aha!”;
- bir görünən consequence

göstərilməlidir.

Tutorial bitəndən sonra “əsl oyun başlayır” modeli risklidir.

---

# 22. P21 — Actionable information density pacing metric-i olsun

Pacing üçün yalnız:
- söz sayı;
- cutscene müddəti

ölçmə.

Daha faydalı:

```text
meaningful clues
+ decisions
+ hypothesis changes
----------------------
time
```

Bu aşağıdırsa:
- exposition;
- waiting;
- filler

hissi yaranır.

---

# 23. P22 — Theme interface-in sosial mənası ilə uyğun olsun

Terminal:
- hacking.

Phone:
- personal life.

Surveillance system:
- privacy/authority.

Professional workstation:
- competence/procedure.

Theme və interface semantik olaraq uyğun olduqda:
- immersion;
- explanation efficiency;
- product identity

güclənir.

---

# 24. P23 — Horror varsa interaction layer-də yaşasın

Horror:
- random loud sound yox;
- interface rule break;
- data corruption;
- unreliable system;
- altered behavior;
- threat through normal workflow

kimi işləyə bilər.

### Rule
> **Qorxu əsas gameplay action-ın içindən çıxmalıdır.**

---

# 25. P24 — Writing QA gameplay QA-dır

Text-heavy oyunlarda:
- typo;
- localization;
- terminology;
- character voice;
- ambiguous wording

birbaşa puzzle correctness-ə təsir edir.

QA planına ayrıca:
- clue semantics;
- dialogue intent;
- translated puzzle logic

daxil edilməlidir.

---

# 26. P25 — Store promise dominant fəaliyyəti düzgün adlandırsın

Əgər oyun:
- detective game-dirsə,
yalnız hacking simulator kimi satılmamalıdır.

Əgər sequel:
- formula-nı ciddi dəyişirsə,
audience expectation nəzərə alınmalıdır.

### Rule
> **Market positioning ən çox etdiyin hərəkəti və yaşadığın fantasy-ni satmalıdır.**

---

# 27. P26 — Sequel-də əvvəlki QoL inherited baseline-dır

Əgər əvvəlki oyun:
- fast-forward;
- save;
- notes;
- skip;
- search

problemini həll edibsə,

sequel-də bu optional extra deyil.

Regression:
> xüsusilə sərt qəbul olunur.

---

# 28. P27 — Scope artanda emotional anchor da artmalıdır

Daha çox:
- location;
- character;
- world lore

əlavə ediləndə əsas insan/story anchor itə bilər.

### Rule
> **World breadth artdıqca player-in care etdiyi konkret person/goal daha da aydın olmalıdır.**

---

# 29. P28 — Strong character voice bland neutrality-dən üstündür

Personaj:
- distinct motive;
- language;
- contradiction;
- relationship

daşımalıdır.

Goal:
- hamının sevilməsi deyil.

Goal:
> oyunçunun onu yadda saxlaması və haqqında fikir formalaşdırmasıdır.

---

# 30. P29 — Knowledge graph cavabı tapmamalıdır

Graph:
- relationship;
- chronology;
- source;
- location

göstərə bilər.

Amma:
- auto-link all;
- auto-highlight relevance;
- auto-conclusion

deduction-u oğurlaya bilər.

### Rule
> **Player link yaratsın; sistem link-i saxlasın.**

---

# 31. P30 — Prototipdə ölçüləcək əsas metriklər

Yeni concept üçün:

### Role comprehension
- 30 saniyədə “mən kiməm?” cavabı.

### First insight time
- ilk real aha moment-ə qədər vaxt.

### Knowledge autonomy
- oyunçu hint olmadan neçə critical fact qurur?

### Alternative route rate
- eyni fact neçə fərqli yolla tapılır?

### State divergence
- major choice sonrası real state fərqi.

### Actionable density
- meaningful action / dəqiqə.

### Recall
- oyunçu 30 dəqiqə sonra əsas fact-ları xatırlayır?

### External-memory dependence
- oyundan kənar qeyd lazımdır?

### Recovery cost
- səhv qərardan sonra geri qayıtma vaxtı.

---

# 32. Yekun

Ən vacib dizayn qaydası:

> **Oyunçuya çox alət, çox ekran və çox məlumat vermək investigation yaratmır. Investigation oyunçuya müşahidə etməyə, özü nəticə çıxarmağa, həmin nəticəni sistemə təqdim etməyə və dünyanın onu tanıdığını görməyə imkan verəndə yaranır.**

Bu sənəd:
- `genre-synthesis.md`
- per-game deep research
- comparison sənədləri

üzərində qurulub.
