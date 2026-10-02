# Cyber Manhunt — Dərin araşdırma

## Executive Summary

Cyber Manhunt əvvəlki iki reference oyundan fərqli olaraq dərinliyi terminal execution və tactical action economy-dən yox, **information discovery, deduction, social context və narrative investigation** üzərindən qurur.

Verified Steam dataset:

- 847 review
- 681 positive
- 166 negative
- **80.40% positive ratio**

Ən vacib nəticə:

> **Cyber Manhunt-un əsas gücü “internet sleuth / digital investigator” fantasy-sidir; əsas zəifliyi isə oyunçunun öz inference və intuition-u ilə irəliləməsi əvəzinə tez-tez əvvəlcədən təyin olunmuş clue order və progression trigger-lərinə bağlanmasıdır.**

Oyun real dəyər yaradır:
- story və case curiosity;
- şəxslər haqqında parçalanmış məlumat toplamaq;
- müxtəlif informasiya mənbələrini əlaqələndirmək;
- privacy və social harm kimi real-world mövzuları oyun sisteminə daxil etmək;
- sadələşdirilmiş, amma tanınan cyber/social mechanics ilə accessibility yaratmaq.

Amma bu dəyər aşağıdakılarla zəifləyir:
- sərt linear progression;
- clue/evidence acceptance problemləri;
- localization/writing keyfiyyəti;
- UI friction;
- repetitive information workflow;
- bəzi one-off minigame-lərdə clarity və timing problemi.

Ən ciddi product siqnalı early-session cohort-dadır:

- 0–1h: **27.78% positive**
- 1–3h: **44.07% positive**
- 10h+: **90.72% positive**

İlk 3 saatdakı 95 review-un **62.11%-i negative**-dir. Bu selection bias daşıyır, amma Cyber Manhunt-un əsas problemi “oyun gec açılır”dan daha çox **ilk saatlarda player expectation ilə actual investigation grammar arasındakı mismatch** kimi görünür.

Ətraflı quantitative sənəd:

`analysis/cyber-manhunt/theme-analysis.md`

---

# 1. Research Scope və Data Quality

Dataset snapshot: **2026-10-02**

- raw reviews: 847
- unique reviews: 847
- positive: 681
- negative: 166
- median playtime: 9.27h
- average positive review playtime: 12.07h
- average negative review playtime: 6.33h
- very short reviews: 172

Əsas data:

- `data/processed/cyber-manhunt/reviews.jsonl`
- `data/processed/cyber-manhunt/statistics.json`
- `data/reports/cyber-manhunt/summary.md`

Steam-in English kimi qaytardığı corpus daxilində bəzi başqa-dilli review-lər də var. Buna görə review count və recommendation statistikasını istifadə edirik, amma lexical theme faizi exact “English population prevalence” kimi təqdim edilmir.

---

# 2. Product və Market Snapshot

Steam App ID: **1216710**

- Developer: Aluba Van+ / Aluba Studio
- Release: 2 February 2021
- Early Access: August 2020
- Single-player
- Demo mövcuddur
- Əsas positioning: story-oriented puzzle game
- Mövzular: big data, privacy, cyber violence, online judgment, investigation.

Developer oyunu sadəcə “cool hacking” fantasy-si kimi yox, real internet davranışları və social harm mövzuları üzərindən qurmaq istədiyini açıq şəkildə bildirir.

Bu Cyber Manhunt-u Hacknet və Midnight Protocol-dan ayırır:

```text
Hacknet → hacker fantasy
Midnight Protocol → tactical hacker fantasy
Cyber Manhunt → digital investigator + social/cyber observer fantasy
```

---

# 3. Oyunun mahiyyəti

Ən düzgün qısa təsvir:

> **Computer-interface daxilində oynanan story-driven digital investigation və social-engineering puzzle game.**

Core experience:

```text
case haqqında ilkin məlumat
→ public/private məlumat axtar
→ şəxslər və əlaqələr haqqında profil qur
→ əlavə access imkanları aç
→ yeni məlumat tap
→ clue-ları əlaqələndir
→ reasoning/puzzle mərhələsi
→ case və story nəticəsi
```

Burada ən vacib fərq budur:

> Access əldə etmək məqsəd deyil; yeni information layer-ə keçid vasitəsidir.

Bu, bizim əvvəlki research-də axtardığımız circular information loop-a çox yaxındır.

---

# 4. Player Fantasy

Cyber Manhunt-un əsas fantasy-si:

> **“Mən rəqəmsal izlərdən insanların kim olduğunu və nə baş verdiyini çıxara bilirəm.”**

Bu fantasy üç hissədən yaranır.

## 4.1. Information power

Oyunçu əvvəl az məlumat bilir, sonra target haqqında çox şey öyrənir.

Bu progression özü reward yaradır.

## 4.2. Digital voyeurism / curiosity

Review-lərdə “nosey”, “sleuth”, “investigation”, “digging through information” tipli language görünür.

Player yalnız objective üçün yox, “burada başqa nə var?” marağı ilə davam edə bilir.

## 4.3. Human-system understanding

Oyun texniki sistemlə yanaşı insan davranışı, əlaqələr və privacy zəifliklərini də gameplay materialına çevirir.

Bu Hacknet-in filesystem curiosity-sini daha social direction-a aparır.

---

# 5. İnsanlar niyə başlayır?

Əsas hook-lar:

- Orwell tipli investigation fantasy;
- hacker/detective premise;
- computer desktop interface;
- real-world privacy və cyber themes;
- story mystery;
- unusual indie concept.

Store page və review-lərdən görünən expectation:

> “mən məlumatları özüm tapıb birləşdirəcəyəm.”

Əgər ilk saatda experience bundan çox:

> “düzgün highlighted clue-u tapıb növbəti trigger-i açacağam”

kimi hiss olunursa, disappointment çox tez yaranır.

---

# 6. İnsanlar niyə davam edir?

10h+ cohort-da positive ratio **90.72%**-dir.

Bu causation deyil, amma uzun oynayan audience-in nəyi dəyərləndirdiyini sample-lar göstərir:

- case-lərin bir-birinə bağlanması;
- dark story;
- characters və motivations;
- information accumulation;
- investigation atmosphere;
- puzzle variety;
- social themes;
- story revelations.

Cyber Manhunt-un retention sistemi əsasən:

> **curiosity + narrative closure**

üzərindədir.

Bu Hacknet ilə oxşardır, amma information chain burada daha explicit core loop-dur.

---

# 7. Onboarding və Early-session Risk

## 7.1. 0–1h

- 36 review
- yalnız 10 positive
- **27.78% positive**

## 7.2. 1–3h

- 59 review
- 26 positive
- **44.07% positive**

## 7.3. İlk 3 saat

- 95 review
- 59 negative
- **62.11% negative**

Bu üç oyunda gördüyümüz ən sərt early-review profile-dir.

Sample audit early negative feedback-i əsasən bunlara bağlayır:

- investigation-ın çox linear hiss olunması;
- clue-ların oyunçuya “tapdırılması” əvəzinə UI tərəfindən göstərilməsi;
- translation;
- UI friction;
- sadələşdirilmiş interaction;
- story hook-un bəzi player-lər üçün gec işləməsi;
- “mən özüm düşünəcəyəm” expectation-ının zəif qarşılanması.

### Əsas dərs

> **Investigation game ilk saatda oyunçuya real bir inference victory verməlidir.**

Tutorial yalnız interface göstərməməlidir.

Player ilk sessiyada:

> “bunu mən tapdım”

hissini yaşamalıdır.

---

# 8. Core Loop və System Depth

Cyber Manhunt-un böyük üstünlüyü budur:

Dərinlik üçün çox sayda combat/tactical system lazım deyil.

Dərinlik information relationships-dən yarana bilər.

Məsələn:

```text
person
↕
alias
↕
friend
↕
account
↕
location
↕
event
```

Belə graph player-a böyük decision space verə bilər.

Amma current implementation tez-tez bu graph-i tam sərbəst buraxmır.

Review-lərdə:
- “already knew answer but game did not accept it”;
- “wrong clue source”;
- “same search later suddenly works”;
- “exact evidence required”

tipli complaint-lər təkrarlanır.

Bu systemic depth-i scripted depth-ə çevirir.

---

# 9. Linearity və Deduction Problemi

LINEARITY_SCRIPTING candidate-lərində:

- **55.88% negative**
- dataset baseline-dan **2.85×** yüksək negative concentration.

Bu ən güclü design risk-lərdən biridir.

Investigation game-də player iki state daşıyır:

1. **game state**
2. **knowledge state**

Ən yaxşı detective design-də bunlar mümkün qədər uyğunlaşır.

Cyber Manhunt-un zəif anlarında:

```text
player knows answer
≠
game accepts answer
```

olur.

### Design lesson

> **Player-in həqiqətən bildiyi məlumat progress üçün valid olmalıdır, hətta onu designer-in nəzərdə tutduğu exact route ilə tapmayıbsa.**

Bu gələcək concept üçün çox vacibdir.

---

# 10. Clue və Evidence Design

CLUE_EVIDENCE_QUALITY:

- 120 mentions
- **29.17% negative**

Review-lərdə iki opposite problem var.

## Too explicit

Relevant text highlight olur.

Player özü relevance müəyyən etmir.

## Too strict

Player obvious evidence görür, amma game onu collect etmir.

Bu iki problem birlikdə qəribə nəticə yaradır:

> oyun həm çox kömək edir, həm də lazım olmayan yerdə həddindən artıq sərt olur.

Ideal sistem:

- evidence discoverable olsun;
- relevance avtomatik tam həll edilməsin;
- bir faktı bir neçə yoldan tapmaq mümkün olsun;
- duplicate evidence eyni knowledge state-i aça bilsin.

---

# 11. Search və Information Discovery

INFORMATION_SEARCH:

- 93 mentions
- **30.11% negative**

Core fantasy güclüdür.

Problem search engine-in çox deterministic olmasıdır.

Əgər yalnız exact expected query işləyirsə:

> search system deyil, disguised dialogue tree yaranır.

Gələcək design üçün opportunity:

- fuzzy query;
- multiple clue paths;
- partial results;
- noise;
- redundant evidence;
- conflicting sources.

Bu information gameplay-ə real mastery verə bilər.

---

# 12. Social Engineering

Developer bu sahə üçün xüsusi research apardığını deyir.

Player experience-də bu:
- target behavior;
- relationship;
- trust;
- personal context

kimi human information-u gameplay materialına çevirir.

Bu çox güclü concept direction-dır.

Amma bəzi review-lər execution-u trial-and-error kimi qəbul edir.

### Design lesson

> **Human interaction puzzle-i “correct dialogue option” yox, əvvəl topladığın information-dan leverage istifadə etmək üzərində qurulmalıdır.**

Bu zaman investigation və social interaction eyni loop-a çevrilir.

---

# 13. Story və Writing

STORY_NARRATIVE:

- 315 mentions
- negative ratio demək olar dataset baseline ilə eynidir.

Bu story-nin əhəmiyyətsiz olması deyil.

Story həm positive, həm negative review-un əsas müzakirə obyektidir.

Positive:
- interconnected cases;
- dark themes;
- curiosity;
- emotional revelations.

Negative:
- awkward localization;
- shallow dialogue;
- preachy tone;
- inconsistent character writing;
- weak or forced moments.

LOCALIZATION_WRITING isə ayrıca çox güclü risk-dir:

- 188 mentions
- **36.17% negative**
- baseline-dan **1.85×** yüksək.

### Fundamental lesson

> **Text-driven game-də writing və localization mechanic qədər core production discipline-dir.**

Poor language:
- clue logic-i;
- character believability-ni;
- puzzle instruction-u;
- emotional consequence-i

bir anda zəiflədə bilir.

---

# 14. Puzzle Variety vs Puzzle Clarity

Cyber Manhunt repetition-ı qırmaq üçün müxtəlif one-off puzzle və minigame-lər istifadə edir.

Bu positive review-lərdə variety kimi təriflənir.

Amma PUZZLE_CLARITY:

- 181 mentions
- **29.28% negative**

Risk:

```text
new mechanic
+
weak explanation
+
timer
=
trial-and-error
```

Bir mechanic yalnız bir dəfə istifadə olunacaqsa onun learning cost-u xüsusilə diqqətlə hesablanmalıdır.

---

# 15. Public Opinion Minigame

Explicit volume aşağıdır:

- 13 mentions
- 7 negative
- **53.85% negative**

Bu prevalence göstəricisi deyil.

Amma high-impact failure nümunəsidir.

Bir neçə review-da player ümumi oyunu bəyəndiyini, amma bu mandatory segment səbəbilə recommendation-ı negative etdiyini deyir.

### Principle

> **Mandatory side-system əsas core loop qədər polished olmalıdır; yoxsa bir neçə dəqiqəlik zəif mechanic saatlarla qurulan goodwill-i məhv edə bilər.**

---

# 16. Repetition

REPETITION:

- 57 mentions
- **43.86% negative**
- baseline-dan **2.24×** yüksək.

Cyber Manhunt sübut edir ki:

> information gameplay özü avtomatik variation yaratmır.

Əgər hər target:

```text
profile
→ search
→ account
→ clue
→ next profile
```

strukturuna çevrilirsə, content dəyişsə də cognitive task eyni qala bilər.

Bu artıq üç oyunda təkrarlanan principle-dir:

> **Repetition action skin-dən yox, decision structure-dan gəlir.**

---

# 17. UI/UX

UI investigation game-də xüsusilə vacibdir.

Player eyni anda:
- müxtəlif şəxsləri;
- məlumat parçalarını;
- timelines;
- relationships;
- objectives

idarə edir.

Yəni UI:

> **player-in external working memory-sidir.**

Review-lərdə scroll, hover, click detection, layout və platform-specific issues reasoning cost-u artırır.

Gələcək concept üçün:
- evidence board;
- search history;
- pinned facts;
- relationship graph;
- back/forward history;
- open tabs;
- automatic provenance

kimi sistemlər ciddi dəyər yarada bilər.

---

# 18. Realism və Authenticity

REALISM_ACCURACY:

- 36 mentions
- yalnız **8.33% negative**.

Developer real social events və subject-matter research istifadə edib.

Player-lər full technical realism tələb etmir.

Onlara daha çox lazım olan:

- tanınan behavior;
- plausible information chain;
- human mistakes;
- privacy leakage logic;
- coherent cause/effect.

Bu artıq üç oyun üzrə güclənən cross-game principle-dir:

> **Selective authenticity full simulation-dan daha effektiv ola bilər.**

---

# 19. Ethical və Social Themes

Developer-in əsas məqsədlərindən biri:
- privacy;
- online judgment;
- digital harm;
- real social consequences

haqqında player-i düşündürməkdir.

Bu mövzular positive review-lərdə meaningful sayılır.

Amma bəzi negative review-lər:
- moralizing;
- stereotypes;
- forced message

şikayəti edir.

### Design lesson

> **Ethical message player-in öz inference-indən doğanda daha güclüdür; designer nəticəni birbaşa diktə edəndə preachy riski artır.**

---

# 20. Developer Intent vs Player Outcome

| Intent | Outcome |
|---|---|
| Real-world social resonance | Güclü concept, amma English writing keyfiyyəti təsiri azalda bilir |
| Accessible cyber-investigation | Accessibility yüksəkdir, amma bəzi player üçün depth çox scripted-dir |
| Social-engineering authenticity | Theme güclüdür, mechanic depth mixed-dir |
| Story-driven puzzle | Story retention yaradır, puzzle clarity inconsistent-dir |
| Realistic relevance | Full realism tələb olunmadan yaxşı işləyir |

---

# 21. Əsas uğur faktorları

## 21.1. Güclü və fərqli fantasy

“İnsanların rəqəmsal həyatını araşdırmaq” dərhal başa düşülür.

## 21.2. Information özü reward-dur

Yeni məlumat tapmaq progression hissi verir.

## 21.3. Story və gameplay eyni materialdan qurulur

Email, profile, chat və data həm mechanic, həm narrative-dir.

## 21.4. Real-world relevance

Privacy və digital harm story-ni abstract cyber fiction-dan çıxarır.

## 21.5. Low technical barrier

Player professional technical knowledge olmadan oynaya bilir.

---

# 22. Əsas failure pattern-lər

1. **Scripted progression player knowledge-i tanımır.**
2. **Localization/writing text-heavy gameplay-i birbaşa zəiflədir.**
3. **Clue collection bəzən UI hunt-a çevrilir.**
4. **Search real search space əvəzinə expected query routing olur.**
5. **Repetition case content dəyişsə belə qalır.**
6. **One-off puzzle-lər əlavə onboarding cost yaradır.**
7. **Timer bəzi reasoning segmentlərini trial-and-error-a çevirir.**
8. **UI friction working-memory yükünü artırır.**
9. **Ethical message bəzən preachy hiss olunur.**

---

# 23. Bizim gələcək oyun üçün design dərsləri

## 23.1. Player knowledge first-class state olmalıdır

Eyni fakt müxtəlif mənbələrdən tapıla bilər.

## 23.2. Multiple valid routes lazımdır

Investigation bir correct click sequence olmamalıdır.

## 23.3. Search system real exploration hissi verməlidir

Exact query dependency minimum olmalıdır.

## 23.4. Information → hypothesis → action → consequence loop qur

Sadəcə information → next objective yox.

## 23.5. Writing gameplay budget-in hissəsidir

Writer və localization process production-un mərkəzində olmalıdır.

## 23.6. UI evidence workspace kimi dizayn olunmalıdır

Notes və relationship management sonradan əlavə olunan convenience feature deyil.

## 23.7. Repetition cognitive task səviyyəsində ölçülməlidir

Yeni story content eyni reasoning task-ı gizlətməməlidir.

## 23.8. Timer yalnız öyrənilmiş mechanic-də istifadə olunmalıdır

Investigation thinking time-a ehtiyac duyur.

---

# 24. Opportunity Map

## 24.1. Organic information graph

Static progression chain əvəzinə networked evidence.

## 24.2. Redundant evidence paths

Eyni nəticəyə müxtəlif data source-lardan gəlmək.

## 24.3. Real hypothesis system

Player öz theory-sini qurur və sistem bunu test etməyə imkan verir.

## 24.4. Social consequence

Tapdığın information yalnız puzzle açmır, person/world state dəyişir.

## 24.5. Better evidence UX

Searchable notebook, pinned facts, provenance və contradiction tracking.

## 24.6. Human-system gameplay

Technical access ilə interpersonal leverage-i birləşdirmək.

---

# 25. Hacknet və Midnight Protocol ilə ilkin synthesis

Üç oyunun depth modeli fərqlidir:

```text
Hacknet
execution depth

Midnight Protocol
tactical/system depth

Cyber Manhunt
information/deduction depth
```

Hər üçündə eyni problem başqa formada görünür:

```text
repeated cognitive task
→ pattern becomes visible
→ fantasy weakens
```

Bu artıq genre-level design principle üçün güclü evidence-dir.

Ən maraqlı hybrid istiqamət:

> **Hacknet-in immersion və organic snooping-i + Midnight Protocol-un meaningful consequence-u + Cyber Manhunt-un information graph/deduction fantasy-si.**

Amma bu feature stacking kimi edilməməlidir.

Core design əvvəlcə bir əsas fantasy və bir əsas decision loop ətrafında qurulmalıdır.

---

# 26. Açıq suallar

1. Cyber Manhunt 2 original-dakı linearity və evidence-state problemlərini nə qədər həll edib?
2. Original-da English localization improvement patch-ləri review cohort-larında ölçülə bilərmi?
3. The Operator eyni information-driven loop-u daha az scripted hiss etdirirmi?
4. Orwell daha az mechanic ilə daha güclü deduction/ethical tension yaradırmı?
5. Mainlining information-search və hacking arasında necə balans qurur?
6. Search freedom artanda player confusion nə qədər artır?

---

# 27. Mənbələr

## Daxili

- `data/processed/cyber-manhunt/statistics.json`
- `data/processed/cyber-manhunt/reviews.jsonl`
- `data/reports/cyber-manhunt/summary.md`
- `analysis/cyber-manhunt/theme-analysis.md`
- `config/aspect_taxonomy.yaml`

## Xarici

**Steam Store — Cyber Manhunt**  
https://store.steampowered.com/app/1216710/

**GamerSky — Aluba Studio interview**  
https://club.gamersky.com/activity/435462?club=163

**indienova — Cyber Manhunt project page**  
https://indienova.com/g/cyber-manhunt

---

# Status

**Mərhələ:** Cyber Manhunt per-game deep research — əsas mərhələ tamamlanıb  
**Dataset:** 847 verified Steam-provided English reviews  
**Növbəti:** Hacknet + Midnight Protocol + Cyber Manhunt cross-game comparison və sonra növbəti digital-investigation target.
