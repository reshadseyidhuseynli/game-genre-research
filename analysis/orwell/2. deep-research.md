# Orwell: Keeping an Eye On You — Dərin araşdırma

## Executive Summary

Orwell computer-interface və digital-investigation janrında vacib bir addım irəli gedir:

> **Player yalnız məlumat tapmır; hansı məlumatın “rəsmi həqiqət”ə çevriləcəyinə qərar verir.**

Bu, əvvəlki reference oyunlardan fərqli depth modelidir.

Verified Steam dataset:

- **8,549 review**
- 7,735 positive
- 814 negative
- **90.48% positive ratio**

Əsas nəticə:

> **Orwell-un ən güclü design nailiyyəti information selection ilə visible consequence arasında birbaşa əlaqə qurmasıdır. Əsas zəifliyi isə həmin qərardan əvvəl player-in discovery və interpretation freedom-unu auto-highlight və adviser guidance ilə həddindən artıq məhdudlaşdırmasıdır.**

Başqa sözlə:

```text
strong strategic/narrative agency
+
weak-to-moderate procedural investigation agency
```

Orwell bizə göstərir ki, moral choice üçün ayrıca “A/B dialogue option” lazım deyil.

Moral choice belə yarana bilər:

```text
raw information
→ context
→ interpretation
→ what do I reveal?
→ another actor reacts
→ world changes
```

Ən güclü tərəflər:

- privacy/surveillance fantasy;
- information selection;
- immediate və delayed consequence;
- character-specific data layers;
- moral ambiguity;
- player bias;
- story ilə mechanic-in eyni materialdan qurulması;
- interface-as-world.

Əsas zəifliklər:

- relevant text-in əvvəlcədən highlight olunması;
- adviser-in bəzən player əvəzinə interpretation etməsi;
- mandatory hidden progression data;
- contradictory evidence-in bəzən informed choice yox, blind choice yaratması;
- irreversible information decision;
- repetitive drag/upload loop;
- early-session “bu detective game deyil” expectation mismatch.

Ətraflı quantitative sənəd:

`analysis/orwell/theme-analysis.md`

---

# 1. Research Scope və Data Quality

Dataset snapshot: **2026-10-02**

- total reviews: 8,549
- positive: 7,735
- negative: 814
- positive ratio: 90.48%
- average playtime at review: 6.41h
- median playtime: 5.07h
- positive review average playtime: 6.62h
- negative review average playtime: 4.43h
- 108 review-da playtime-at-review missing-dir.

Əsas daxili sources:

- `data/processed/orwell/reviews.jsonl`
- `data/processed/orwell/statistics.json`
- `data/reports/orwell/summary.md`
- `analysis/orwell/theme-analysis.md`

External research:

- Osmotic Studios official pages;
- Game Developer design deep dive;
- Road to the IGF interview.

---

# 2. Product Snapshot

Steam App ID: **491950**

- Developer: Osmotic Studios
- Publisher: Daedalic Entertainment
- Release: 27 October 2016
- Single-player
- Adventure / Indie / Simulation
- Core premise: dövlət surveillance sistemi daxilində citizen-lərin public və private digital data-sını araşdırmaq.

Official product promise:

> yalnız sənin ötürdüyün məlumat security forces tərəfindən görüləcək və həmin məlumatlar real nəticə yaradacaq.

Bu promise research üçün çox vacibdir, çünki game mechanic birbaşa:

> **information → interpretation → action**

chain-i üzərində qurulub.

---

# 3. Orwell əslində necə oyundur?

Ən doğru qısa təsvir:

> **Text-heavy surveillance investigation game where player curates evidence rather than directly acting in the world.**

Core loop:

```text
person / event haqqında ilkin clue
→ public və private sources aç
→ datachunk-ları oxu
→ hansının relevant olduğunu qiymətləndir
→ seçilmiş məlumatı profile-a ötür
→ adviser həmin məlumatı interpretasiya edir
→ yeni document / action / consequence açılır
→ yeni context
→ növbəti seçim
```

Burada əsas gameplay verb:

> **tapmaqdan çox seçməkdir.**

Bu onu Cyber Manhunt və The Operator-dan fərqləndirir.

---

# 4. Player Fantasy

Orwell-un fantasy-si:

> **“Mən information gatekeeper-əm; sistem insanların həyatı haqqında yalnız mənim ötürdüyüm şeyləri bilir.”**

Bu fantasy dörd layer-dən ibarətdir.

## 4.1. Surveillance power

Player:
- social media;
- chats;
- calls;
- private files;
- account məlumatları;
- metadata

kimi şəxsi dataya çıxış əldə edir.

## 4.2. Interpretation power

Player yalnız data oxumur.

O:
- hansı məlumatın relevant;
- hansı məlumatın misleading;
- hansı məlumatın şəxsi, amma case üçün lazımsız

olduğunu özü qiymətləndirir.

## 4.3. Narrative power

Seçilmiş data adviser-in target haqqında qurduğu picture-ı dəyişir.

## 4.4. Moral power

Player hər dəfə:

> “Bu məlumatı ötürməyə haqqım varmı?”

sualı ilə üzləşə bilər.

Bu mechanic player fantasy və social theme-i eyni anda daşıyır.

---

# 5. Developer Intent və sistemin yaranması

Daniel Marx-in design deep dive-ı Orwell-un ən dəyərli mənbələrindən biridir.

Development iteration belə gedib.

## 5.1. İlkin model: hər şey selectable

İlk prototype-da demək olar bütün text və şəkillər information ola bilərdi.

Problem:

- player overload;
- confusion;
- hansı detail-in relevant olduğunu anlamağın çətinliyi.

## 5.2. İkinci model: explicit tasks

Developer specific task-lar əlavə edib:

- name tap;
- relationship tap;
- hobby tap və s.

Problem:

- playtester-lər oyunu çox linear hiss edib;
- alternative solution olduğunu anlamayıb;
- investigation checklist-ə çevrilib.

## 5.3. Final kompromis: datachunks

Final design:

- yalnız bəzi predefined information selectable;
- onlar highlight edilir;
- task-list çıxarılır;
- player hansını upload etməyi özü seçir.

Bu çox vacib design history-dir.

Çünki review-lərdə gördüyümüz əsas friction də məhz bu kompromisin cost-udur.

> **Highlight confusion-u həll edir, amma discovery-ni azaldır.**

---

# 6. Early-session Risk

Playtime cohort-ları:

| Playtime | Positive ratio |
|---|---:|
| 0–1h | **54.34%** |
| 1–3h | **79.46%** |
| 3–10h | **93.26%** |
| 10h+ | **95.28%** |

Ən zəif nöqtə ilk saatdır.

Early negative feedback-də:

- gameplay “drag highlighted text” kimi görünür;
- real detective work expectation qarşılanmır;
- adviser çox yönləndirir;
- reading-heavy interaction player-a passiv görünür;
- system-in depth-i ilk saatda dərhal görünmür.

Bu çox vacib product lesson-dir:

> **Orwell-un ən yaxşı mechanic-i consequence-dır, amma player consequence hiss etməzdən əvvəl interface-i “sadə drag-and-drop” kimi qiymətləndirə bilər.**

### Design implication

İlk 30–60 dəqiqədə:
- meaningful ambiguous choice;
- visible consequence;
- context mistake;
- target state change

çox tez göstərilməlidir.

---

# 7. Information Selection — Orwell-un əsas fərqləndiricisi

Orwell digər digital-investigation oyunlarından burada ayrılır.

Player:
- bütün tapılan məlumatı avtomatik ötürmür;
- sensitive məlumatı gizlədə bilər;
- conflicting information arasında seçim edə bilər;
- bəzi faktların system-ə düşməsinin qarşısını ala bilər.

Developer design məqsədi:

> player-in “məlumat tapmaq”dan əlavə “məlumatı təhvil vermək” hərəkətini hiss etməsi.

Buna görə drag-and-drop özü də tematikdir.

Mouse gesture:

> literally handing information over

hissi üçün seçilib.

### Nəticə

Bu mechanic işləyir.

Amma iki condition tələb edir:

1. seçimlər həqiqətən optional olmalıdır;
2. player nəticə üçün kifayət qədər context bilməlidir.

Əks halda:

> “moral choice”

tez:

> “progression trigger seçimi”

hissinə çevrilir.

---

# 8. Consequence Visibility

Orwell-un ən güclü design nailiyyəti budur.

CONSEQUENCE_VISIBILITY candidate-lərində negative ratio baseline-dan aşağıdır.

WORLD_REACTIVITY də eyni istiqamətdədir.

Developer consequence feedback üçün adviser-i mərkəzi system kimi qurub.

Player datachunk ötürür.

Adviser:
- comment edir;
- suspect perception dəyişir;
- arrest;
- intervention;
- investigation direction

kimi action-lara səbəb ola bilir.

Bəzi consequence dərhal görünür.

Bəziləri daha sonra:
- chat;
- call;
- character behavior;
- story branch

kimi qayıdır.

### Design principle

> **Player choice-dan sonra world state dəyişməlidir; yalnız hidden variable dəyişməsi kifayət deyil.**

Bu Midnight Protocol və The Operator-dan çıxan choice/consequence principle-ni gücləndirir.

---

# 9. Context — Orwell-un ən dəyərli mechanic ideyası

Oyunun fundamental premise-i:

> **data fact deyil.**

Eyni sentence:
- joke;
- anger;
- sarcasm;
- outdated opinion;
- private confession;
- deliberate lie

ola bilər.

System isə onu context-dən çıxarıb “fact” kimi saxlaya bilər.

Developer bunu qəsdən design edib.

Məşhur erkən nümunə:
- casual conversation bir “crime fact” kimi system tərəfindən səhv interpretasiya oluna bilər;
- player onu upload edərsə adviser real action ata bilər.

Bu çox güclü mechanic modelidir:

```text
source
+
context
+
system interpretation
+
human interpretation
=
meaning
```

### Opportunity

Gələcək oyunda evidence yalnız value olmamalıdır.

Hər fact üçün:
- source;
- timestamp;
- reliability;
- context;
- relationship;
- interpretation confidence

ola bilər.

---

# 10. Contradictory Evidence

Developer qəsdən contradictory information istifadə edib, çünki:

- online identity parçalanmışdır;
- insanlar özlərini fərqli context-lərdə fərqli göstərir;
- source-lar bias daşıyır.

Bu concept güclüdür.

Amma review-lərdə problem görünür:

> player həmişə contradiction-u həll etmək üçün kifayət qədər evidence əldə etmir.

Bu zaman ambiguity:
- moral tension yox;
- random guess

kimi hiss oluna bilər.

### Fundamental distinction

> **Uncertainty player-in bilmədiyi şeydən gələ bilər; amma yaxşı decision üçün player nəyi bilmədiyini də bilməlidir.**

Gələcək design:
- known facts;
- conflicting claims;
- unknowns;
- source confidence

ayrı göstərilə bilər.

---

# 11. Information Irreversibility

Orwell-da upload permanence consequence hissi üçün vacibdir.

Developer əvvəl conflicting data-nı profile-da yanaşı müqayisə etməyə imkan verib, amma bu “uploaded information is permanent” hissini zəiflətdiyi üçün final sistemdə bir seçimin digərlərini bağlamasına keçib.

Bu thematic cəhətdən güclüdür:

> leaked information geri qaytarılmır.

Amma gameplay risk:

- player yeni evidence sonradan tapır;
- əvvəlki conclusion artıq səhv görünür;
- correction imkanı yoxdur.

### Better model hypothesis

Information özü silinməsin.

Amma player:
- correction;
- qualification;
- confidence update;
- source dispute

əlavə edə bilsin.

Bu həm permanence-ni saxlayar, həm epistemic fairness-i artırar.

---

# 12. Auto-highlighting

Orwell-un ən güclü negative design signal-larından biridir.

AUTO_HIGHLIGHTING candidate-lərində negative concentration baseline-dan təxminən 3.9× yüksəkdir.

Problem:

- article oxumaq optional olur;
- player yalnız colored phrase-lərə baxa bilər;
- relevance judgment system tərəfindən əvvəlcədən edilir;
- investigation discovery hissi azalır.

Bu interesting paradox-dur.

Developer highlighting-i player-a option space-i göstərmək üçün tətbiq edib.

Amma investigation game-də option space-in tam görünməsi:

> puzzle space-in bir hissəsini artıq həll edir.

### Design direction

Progressive assistance:

Level 0:
- heç nə highlight deyil.

Level 1:
- search/hint göstərir ki, bu page-də relevant data ola bilər.

Level 2:
- region highlight olunur.

Level 3:
- exact phrase göstərilir.

Beləliklə accessibility saxlanır, amma default experience deduction-a imkan verir.

---

# 13. Adviser System

Adviser Orwell-un ən güclü və ən riskli system-lərindən biridir.

## Güclü tərəf

Adviser:
- player data-nın real consequence-sını görünən edir;
- player-in yaratdığı target profile-a əsasən qərar verir;
- ayrı character-dir və öz bias-ı var;
- player ilə system arasında narrative bridge-dir.

## Risk

Adviser:
- next step-i deyəndə;
- evidence-i player əvəzinə interpretasiya edəndə;
- yanlış conclusion çıxarıb player-a correction imkanı verməyəndə

frustration yaradır.

### Key lesson

> **Reactive NPC yaxşıdır; interpretive authority player agency-ni əvəz etməməlidir.**

NPC:
- “Mən bunu belə başa düşdüm” deməlidir.

System:
- player-a “bu həqiqətdir” deməməlidir.

---

# 14. Player Agency

Orwell strategic agency-də güclüdür.

Player:
- nəyi reveal;
- nəyi hide;
- hansı contradictory data-nı seçmək

haqqında qərar verir.

Bu The Operator-dan real şəkildə daha güclüdür.

Amma procedural agency hələ məhduddur.

Player:
- non-highlighted detail-i manually record edə bilmir;
- istədiyi person-u sərbəst investigate edə bilmir;
- game-in əvvəlcədən seçdiyi information universe daxilində işləyir.

### Agency modeli

```text
Discovery agency      → Medium/Low
Interpretation agency → Medium
Selection agency      → High
Consequence agency    → High
```

Bu decomposition gələcək oyunların müqayisəsində istifadə olunmalıdır.

---

# 15. Privacy və Surveillance

Privacy theme Orwell-da mechanic-in özündə yaşayır.

Developer concept-i Snowden disclosures-dan sonrakı public surveillance debate-dən çıxarıb.

Player:
- public persona;
- private conversations;
- şəxsi files;
- metadata

arasında dərinləşir.

Developer bunu müxtəlif “privacy levels” kimi qurub.

Bu çox güclü narrative structure-dir:

```text
public self
→ social/private self
→ hidden/private self
```

Hər layer character haqqında əvvəlki interpretation-u dəyişə bilər.

### Design lesson

> **Information depth yalnız daha çox fact deyil; daha private və daha context-rich layer-ə keçid ola bilər.**

---

# 16. Moral Ambiguity

Orwell explicit “good vs evil” menu-dan qaçmağa çalışır.

Developer-in məqsədi:

- player özü right/wrong müəyyən etsin;
- choices uncomfortable olsun;
- information bias və player bias toqquşsun.

Review data ümumən bunu müsbət qəbul edir.

Ən güclü positive experience:

> player düzgün cavabı tapmır; özü hansı cost-u qəbul etdiyini seçir.

Ən güclü negative experience:

> game artıq hansı moral nəticəyə gəlməli olduğunu diktə edir.

### Principle

> **Moral ambiguity mechanic-də olmalıdır, müəllifin lecture-ında yox.**

---

# 17. Reading və Story

Orwell çox text-heavy-dir.

Amma READING_LOAD özü baseline-a yaxın negative ratio göstərir.

Bu çox faydalı finding-dir.

Deməli:

> player oxumağa qarşı deyil, dəyərsiz oxumağa qarşıdır.

Reading:
- clue;
- character insight;
- contradiction;
- decision input

verirsə qəbul olunur.

Reading yalnız:
- exposition;
- delay;
- already-highlighted answer ətrafındakı filler

kimi görünürsə friction artır.

---

# 18. Repetition

Orwell-un action grammar-i sadədir:

```text
open
→ read
→ highlight/datachunk
→ drag
→ wait
→ adviser
→ repeat
```

REPETITION candidate-lərində negative concentration yüksəkdir.

Story variation və moral consequence loop-u bir müddət daşıyır.

Amma cognitive challenge dəyişməsə:
- page dəyişir;
- character dəyişir;
- actual interaction eyni qalır.

### Cross-game conclusion

Bu artıq dördüncü əsas reference-də eyni pattern-dir:

> **Repetition action animation-dan yox, decision grammar-in dəyişməməsindən yaranır.**

---

# 19. Developer Intent vs Player Outcome

| Developer intent | Player outcome |
|---|---|
| Information-u literally “hand over” etmək | Güclü thematic interaction |
| Hər micro-choice meaningful olsun | Böyük ölçüdə uğurlu |
| Consequence hiss olunsun | Güclü və görünən feedback |
| Explicit right/wrong olmasın | Ümumən uğurlu |
| Player overwhelm olmasın | Highlight accessibility verir |
| Task-list linearity-dən qaçmaq | Qismən uğurlu |
| Adviser consequence bridge olsun | Uğurlu, amma hand-holding riski |
| Contradiction ambiguity yaratsın | Güclü concept, bəzən blind choice |

---

# 20. Əvvəlki oyunlarla comparison

## Hacknet

Əsas agency:
- access və exploration.

Orwell əlavə edir:
- information revelation decision.

## Midnight Protocol

Əsas agency:
- tactical action və identity.

Orwell:
- information curation və indirect consequence.

## Cyber Manhunt

Əsas problem:
- clue/progression route.

Orwell:
- clue-lar daha aydın, amma auto-highlight deduction-u azaldır.

## The Operator

Əsas problem:
- çox guidance və predetermined narrative.

Orwell:
- daha çox strategic choice verir;
- consequence daha real görünür;
- amma adviser və mandatory data yenə guidance yaradır.

---

# 21. Əsas cross-game advancement

Orwell research-dən sonra digital-investigation loop üçün yeni mərhələ yaranır:

Əvvəl:

```text
discover
→ connect
→ hypothesize
```

İndi:

```text
discover
→ verify
→ contextualize
→ decide what to reveal
→ consequence
→ changed information space
```

Bu bizim final opportunity analysis üçün çox vacibdir.

---

# 22. Bizim üçün saxlanmalı design dərsləri

## Saxlamağa dəyər

1. Information selection as core choice.
2. Immediate + delayed consequence feedback.
3. Source/context ambiguity.
4. Public → private → hidden character layers.
5. NPC interpretation as world response.
6. Moral choice without explicit dialogue menu.
7. Interface action ilə thematic action-un eyni olması.
8. Player bias-in gameplay materialına çevrilməsi.

## Qaçmalı risklər

1. Exact phrase auto-highlight.
2. Mandatory hidden progression data.
3. Adviser-in conclusion-u player əvəzinə verməsi.
4. Contradiction üçün kifayət qədər evidence olmaması.
5. New evidence gəldikdən sonra correction imkanının olmaması.
6. Drag/upload loop-un monotonlaşması.
7. “Political message”in mechanic-dən çox exposition ilə verilməsi.
8. First-hour depth-in gec görünməsi.

---

# 23. Opportunity-lər

## 23.1. Evidence provenance

Hər fact:
- source;
- timestamp;
- reliability;
- context

daşısın.

## 23.2. Qualify, don't erase

Player səhv data-nı silməsin.

Amma:
- corrected;
- disputed;
- outdated;
- low-confidence

kimi status verə bilsin.

## 23.3. Multiple interpreters

Tək adviser əvəzinə:
- legal;
- intelligence;
- field;
- political

actor-lar eyni data-nı fərqli interpretasiya edə bilər.

Bu system bias-ı gameplay-ə çevirə bilər.

## 23.4. Consequence chain

Bir data selection:
- target behavior;
- media;
- law enforcement;
- other suspects;
- future evidence

üzərində chain reaction yarada bilər.

## 23.5. Hidden relevance, visible uncertainty

System exact clue-u göstərməsin.

Amma:
- source quality;
- unresolved contradiction;
- missing context

haqqında meta-information versin.

## 23.6. Player-authored hypothesis

Player system-ə yalnız raw fact yox:
- claim;
- confidence;
- supporting evidence

göndərə bilsin.

Bu deduction + choice + consequence-u birləşdirər.

---

# 24. Confidence Matrix

| Nəticə | Confidence |
|---|---|
| Information selection Orwell-un əsas fərqləndiricisidir | High |
| Consequence visibility əsas strength-dir | High |
| Privacy/surveillance theme mechanic-lə inteqrasiya olunub | High |
| Auto-highlighting deduction-u zəiflədir | High |
| Adviser feedback güclüdür, interpretation guidance risklidir | High |
| Contradictory evidence yaxşı concept, insufficient context risklidir | High |
| Moral ambiguity ümumən işləyir | High |
| Reading volume özü əsas problem deyil | Medium-High |
| Information irreversibility informed choice tələb edir | Medium-High |
| Procedural agency strategic agency-dən zəifdir | High |
| First-hour product understanding risklidir | High |

---

# 25. Açıq suallar

1. Need to Know information selection-a daha çox action freedom əlavə edirmi?
2. Orwell-un weaker competitor-i niyə daha aşağı review satisfaction alıb?
3. Information selection sistemini daha systemic etsək content production cost-u nə qədər artır?
4. Multiple advisers agency-ni artırar, yoxsa cognitive load-u?
5. Context/reliability UI nə qədər explicit olmalıdır?
6. Player-authored hypothesis system real fun yaradar, yoxsa form doldurma hissinə çevrilər?
7. Surveillance theme olmadan eyni mechanic başqa setting-də işləyərmi?

---

# 26. Mənbələr

## Daxili

- `data/processed/orwell/statistics.json`
- `data/processed/orwell/reviews.jsonl`
- `data/reports/orwell/summary.md`
- `analysis/orwell/theme-analysis.md`

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

**Mərhələ:** Orwell per-game deep research — əsas mərhələ tamamlanıb  
**Dataset:** 8,549 verified Steam reviews  
**Növbəti:** Need to Know focused comparator və Orwell vs Need to Know comparison.
