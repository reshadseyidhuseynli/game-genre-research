# Cyber Manhunt — Dərin araşdırma

## Executive Summary

Cyber Manhunt əvvəlki iki reference oyundan fərqli olaraq dərinliyi terminal execution və tactical hərəkət büdcəsi-dən yox, **information discovery, deduction, social context və narrative investigation** üzərindən qurur.

Verified Steam məlumat toplusu:

- 847 rəy
- 681 müsbət
- 166 mənfi
- **80.40% müsbət ratio**

Ən vacib nəticə:

> **Cyber Manhunt-un əsas gücü “internet sleuth / digital investigator” fantasy-sidir; əsas zəifliyi isə oyunçunun öz inference və intuition-u ilə irəliləməsi əvəzinə tez-tez əvvəlcədən təyin olunmuş clue order və progression trigger-lərinə bağlanmasıdır.**

Oyun real dəyər yaradır:
- hekayə və case curiosity;
- şəxslər haqqında parçalanmış məlumat toplamaq;
- müxtəlif informasiya mənbələrini əlaqələndirmək;
- privacy və social harm kimi real-world mövzuları oyun sisteminə daxil etmək;
- sadələşdirilmiş, amma tanınan cyber/social mexanikalar ilə əlçatanlıq yaratmaq.

Amma bu dəyər aşağıdakılarla zəifləyir:
- sərt linear progression;
- clue/dəlil acceptance problemləri;
- localization/writing keyfiyyəti;
- UI çətinlik;
- repetitive information iş axını;
- bəzi one-off minigame-lərdə aydınlıq və timing problemi.

Ən ciddi məhsul siqnalı early-session cohort-dadır:

- 0–1h: **27.78% müsbət**
- 1–3h: **44.07% müsbət**
- 10h+: **90.72% müsbət**

İlk 3 saatdakı 95 rəy-un **62.11%-i mənfi**-dir. Bu selection bias daşıyır, amma Cyber Manhunt-un əsas problemi “oyun gec açılır”dan daha çox **ilk saatlarda oyunçu expectation ilə actual investigation grammar arasındakı mismatch** kimi görünür.

Ətraflı quantitative sənəd:

`analysis/cyber-manhunt/theme-analysis.md`

---

# 1. araşdırma əhatə dairəsi və məlumat Quality

məlumat toplusu snapshot: **2026-10-02**

- raw reviews: 847
- unique reviews: 847
- müsbət: 681
- mənfi: 166
- median oyun müddəti: 9.27h
- orta müsbət rəy oyun müddəti: 12.07h
- orta mənfi rəy oyun müddəti: 6.33h
- very short reviews: 172

Əsas məlumat:

- `data/processed/cyber-manhunt/reviews.jsonl`
- `data/processed/cyber-manhunt/statistics.json`
- `data/reports/cyber-manhunt/summary.md`

Steam-in English kimi qaytardığı corpus daxilində bəzi başqa-dilli rəy-lər də var. Buna görə rəy count və recommendation statistikasını istifadə edirik, amma lexical mövzu faizi exact “English population prevalence” kimi təqdim edilmir.

---

# 2. məhsul və bazar Snapshot

Steam App ID: **1216710**

- yaradıcı: Aluba Van+ / Aluba Studio
- Release: 2 February 2021
- Early Access: August 2020
- Single-oyunçu
- Demo mövcuddur
- Əsas positioning: hekayə-oriented puzzle game
- Mövzular: big məlumat, privacy, cyber violence, online judgment, investigation.

yaradıcı oyunu sadəcə “cool hacking” fantasy-si kimi yox, real internet davranışları və social harm mövzuları üzərindən qurmaq istədiyini açıq şəkildə bildirir.

Bu Cyber Manhunt-u Hacknet və Midnight Protocol-dan ayırır:

```text
Hacknet → hacker fantasy
Midnight Protocol → tactical hacker fantasy
Cyber Manhunt → digital investigator + social/cyber observer fantasy
```

---

# 3. Oyunun mahiyyəti

Ən düzgün qısa təsvir:

> **Computer-interface daxilində oynanan hekayə-driven digital investigation və social-engineering puzzle game.**

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

> Access əldə etmək məqsəd deyil; yeni information qat-ə keçid vasitəsidir.

Bu, bizim əvvəlki araşdırma-də axtardığımız circular information loop-a çox yaxındır.

---

# 4. oyunçu Fantasy

Cyber Manhunt-un əsas fantasy-si:

> **“Mən rəqəmsal izlərdən insanların kim olduğunu və nə baş verdiyini çıxara bilirəm.”**

Bu fantasy üç hissədən yaranır.

## 4.1. Information power

Oyunçu əvvəl az məlumat bilir, sonra target haqqında çox şey öyrənir.

Bu progression özü reward yaradır.

## 4.2. Digital voyeurism / curiosity

rəy-lərdə “nosey”, “sleuth”, “investigation”, “digging through information” tipli language görünür.

oyunçu yalnız objective üçün yox, “burada başqa nə var?” marağı ilə davam edə bilir.

## 4.3. Human-system understanding

Oyun texniki sistemlə yanaşı insan davranışı, əlaqələr və privacy zəifliklərini də oyun gedişi materialına çevirir.

Bu Hacknet-in filesystem curiosity-sini daha social direction-a aparır.

---

# 5. İnsanlar niyə başlayır?

Əsas hook-lar:

- Orwell tipli investigation fantasy;
- hacker/detective premise;
- computer desktop interface;
- real-world privacy və cyber themes;
- hekayə mystery;
- unusual indie concept.

mağaza page və rəy-lərdən görünən expectation:

> “mən məlumatları özüm tapıb birləşdirəcəyəm.”

Əgər ilk saatda experience bundan çox:

> “düzgün highlighted clue-u tapıb növbəti trigger-i açacağam”

kimi hiss olunursa, disappointment çox tez yaranır.

---

# 6. İnsanlar niyə davam edir?

10h+ cohort-da müsbət ratio **90.72%**-dir.

Bu causation deyil, amma uzun oynayan audience-in nəyi dəyərləndirdiyini nümunə-lar göstərir:

- case-lərin bir-birinə bağlanması;
- dark hekayə;
- characters və motivations;
- information accumulation;
- investigation atmosphere;
- puzzle variety;
- social themes;
- hekayə revelations.

Cyber Manhunt-un oyunda qalma sistemi əsasən:

> **curiosity + narrative closure**

üzərindədir.

Bu Hacknet ilə oxşardır, amma information chain burada daha explicit əsas oyun dövrü-dur.

---

# 7. İlkin öyrətmə və Early-session Risk

## 7.1. 0–1h

- 36 rəy
- yalnız 10 müsbət
- **27.78% müsbət**

## 7.2. 1–3h

- 59 rəy
- 26 müsbət
- **44.07% müsbət**

## 7.3. İlk 3 saat

- 95 rəy
- 59 mənfi
- **62.11% mənfi**

Bu üç oyunda gördüyümüz ən sərt early-rəy profile-dir.

nümunə yoxlama early mənfi geribildirim-i əsasən bunlara bağlayır:

- investigation-ın çox linear hiss olunması;
- clue-ların oyunçuya “tapdırılması” əvəzinə UI tərəfindən göstərilməsi;
- translation;
- UI çətinlik;
- sadələşdirilmiş qarşılıqlı əlaqə;
- hekayə hook-un bəzi oyunçu-lər üçün gec işləməsi;
- “mən özüm düşünəcəyəm” expectation-ının zəif qarşılanması.

### Əsas dərs

> **Investigation game ilk saatda oyunçuya real bir inference victory verməlidir.**

təlim hissəsi yalnız interface göstərməməlidir.

oyunçu ilk sessiyada:

> “bunu mən tapdım”

hissini yaşamalıdır.

---

# 8. Core Loop və System dərinlik

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

Belə graph oyunçu-a böyük qərar space verə bilər.

Amma current implementation tez-tez bu graph-i tam sərbəst buraxmır.

rəy-lərdə:
- “already knew answer but game did not accept it”;
- “wrong clue source”;
- “same search later suddenly works”;
- “exact dəlil required”

tipli complaint-lər təkrarlanır.

Bu systemic dərinlik-i scripted dərinlik-ə çevirir.

---

# 9. Linearity və Deduction Problemi

LINEARITY_SCRIPTING namizəd-lərində:

- **55.88% mənfi**
- məlumat toplusu baseline-dan **2.85×** yüksək mənfi concentration.

Bu ən güclü dizayn risk-lərdən biridir.

Investigation game-də oyunçu iki state daşıyır:

1. **game state**
2. **knowledge state**

Ən yaxşı detective dizayn-də bunlar mümkün qədər uyğunlaşır.

Cyber Manhunt-un zəif anlarında:

```text
player knows answer
≠
game accepts answer
```

olur.

### dizayn lesson

> **oyunçu-in həqiqətən bildiyi məlumat progress üçün valid olmalıdır, hətta onu designer-in nəzərdə tutduğu exact route ilə tapmayıbsa.**

Bu gələcək concept üçün çox vacibdir.

---

# 10. Clue və dəlil dizayn

CLUE_EVIDENCE_QUALITY:

- 120 mentions
- **29.17% mənfi**

rəy-lərdə iki opposite problem var.

## Too explicit

Relevant text highlight olur.

oyunçu özü relevance müəyyən etmir.

## Too strict

oyunçu obvious dəlil görür, amma game onu collect etmir.

Bu iki problem birlikdə qəribə nəticə yaradır:

> oyun həm çox kömək edir, həm də lazım olmayan yerdə həddindən artıq sərt olur.

Ideal sistem:

- dəlil discoverable olsun;
- relevance avtomatik tam həll edilməsin;
- bir faktı bir neçə yoldan tapmaq mümkün olsun;
- duplicate dəlil eyni knowledge state-i aça bilsin.

---

# 11. Search və Information Discovery

INFORMATION_SEARCH:

- 93 mentions
- **30.11% mənfi**

Core fantasy güclüdür.

Problem search engine-in çox deterministic olmasıdır.

Əgər yalnız exact expected query işləyirsə:

> search system deyil, disguised dialogue tree yaranır.

Gələcək dizayn üçün imkan:

- fuzzy query;
- multiple clue paths;
- partial results;
- noise;
- redundant dəlil;
- conflicting sources.

Bu information oyun gedişi-ə real mastery verə bilər.

---

# 12. Social Engineering

yaradıcı bu sahə üçün xüsusi araşdırma apardığını deyir.

oyunçu experience-də bu:
- target behavior;
- relationship;
- trust;
- personal context

kimi human information-u oyun gedişi materialına çevirir.

Bu çox güclü concept direction-dır.

Amma bəzi rəy-lər execution-u trial-and-error kimi qəbul edir.

### dizayn lesson

> **Human qarşılıqlı əlaqə puzzle-i “correct dialogue option” yox, əvvəl topladığın information-dan leverage istifadə etmək üzərində qurulmalıdır.**

Bu zaman investigation və social qarşılıqlı əlaqə eyni loop-a çevrilir.

---

# 13. hekayə və Writing

STORY_NARRATIVE:

- 315 mentions
- mənfi ratio demək olar məlumat toplusu baseline ilə eynidir.

Bu hekayə-nin əhəmiyyətsiz olması deyil.

hekayə həm müsbət, həm mənfi rəy-un əsas müzakirə obyektidir.

müsbət:
- interconnected cases;
- dark themes;
- curiosity;
- emotional revelations.

mənfi:
- awkward localization;
- dayaz dialogue;
- preachy tone;
- inconsistent character writing;
- weak or forced moments.

LOCALIZATION_WRITING isə ayrıca çox güclü risk-dir:

- 188 mentions
- **36.17% mənfi**
- baseline-dan **1.85×** yüksək.

### Fundamental lesson

> **Text-driven game-də writing və localization mexanika qədər core production discipline-dir.**

Poor language:
- clue logic-i;
- character believability-ni;
- puzzle instruction-u;
- emotional nəticə-i

bir anda zəiflədə bilir.

---

# 14. Puzzle Variety vs Puzzle aydınlıq

Cyber Manhunt təkrarçılıq-ı qırmaq üçün müxtəlif one-off puzzle və minigame-lər istifadə edir.

Bu müsbət rəy-lərdə variety kimi təriflənir.

Amma PUZZLE_CLARITY:

- 181 mentions
- **29.28% mənfi**

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

Bir mexanika yalnız bir dəfə istifadə olunacaqsa onun learning cost-u xüsusilə diqqətlə hesablanmalıdır.

---

# 15. Public Opinion Minigame

Explicit volume aşağıdır:

- 13 mentions
- 7 mənfi
- **53.85% mənfi**

Bu prevalence göstəricisi deyil.

Amma high-impact uğursuzluq nümunəsidir.

Bir neçə rəy-da oyunçu ümumi oyunu bəyəndiyini, amma bu mandatory segment səbəbilə recommendation-ı mənfi etdiyini deyir.

### Principle

> **Mandatory side-system əsas əsas oyun dövrü qədər polished olmalıdır; yoxsa bir neçə dəqiqəlik zəif mexanika saatlarla qurulan goodwill-i məhv edə bilər.**

---

# 16. təkrarçılıq

təkrarçılıq:

- 57 mentions
- **43.86% mənfi**
- baseline-dan **2.24×** yüksək.

Cyber Manhunt sübut edir ki:

> information oyun gedişi özü avtomatik variation yaratmır.

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

> **təkrarçılıq action skin-dən yox, qərar structure-dan gəlir.**

---

# 17. UI/UX

UI investigation game-də xüsusilə vacibdir.

oyunçu eyni anda:
- müxtəlif şəxsləri;
- məlumat parçalarını;
- timelines;
- relationships;
- objectives

idarə edir.

Yəni UI:

> **oyunçu-in external working memory-sidir.**

rəy-lərdə scroll, hover, click detection, layout və platform-specific issues reasoning cost-u artırır.

Gələcək concept üçün:
- dəlil board;
- search history;
- pinned facts;
- relationship graph;
- back/forward history;
- open tabs;
- automatic provenance

kimi sistemlər ciddi dəyər yarada bilər.

---

# 18. realizm və həqiqilik hissi

REALISM_ACCURACY:

- 36 mentions
- yalnız **8.33% mənfi**.

yaradıcı real social events və subject-matter araşdırma istifadə edib.

oyunçu-lər full technical realizm tələb etmir.

Onlara daha çox lazım olan:

- tanınan behavior;
- plausible information chain;
- human mistakes;
- privacy leakage logic;
- ardıcıl cause/effect.

Bu artıq üç oyun üzrə güclənən oyunlararası principle-dir:

> **seçilmiş həqiqilik hissi full simulation-dan daha effektiv ola bilər.**

---

# 19. Ethical və Social Themes

yaradıcı-in əsas məqsədlərindən biri:
- privacy;
- online judgment;
- digital harm;
- real social nəticələr

haqqında oyunçu-i düşündürməkdir.

Bu mövzular müsbət rəy-lərdə meaningful sayılır.

Amma bəzi mənfi rəy-lər:
- moralizing;
- stereotypes;
- forced message

şikayəti edir.

### dizayn lesson

> **Ethical message oyunçu-in öz inference-indən doğanda daha güclüdür; designer nəticəni birbaşa diktə edəndə preachy riski artır.**

---

# 20. yaradıcı Intent vs oyunçu Outcome

| Intent | Outcome |
|---|---|
| Real-world social resonance | Güclü concept, amma English writing keyfiyyəti təsiri azalda bilir |
| Accessible cyber-investigation | əlçatanlıq yüksəkdir, amma bəzi oyunçu üçün dərinlik çox scripted-dir |
| Social-engineering həqiqilik hissi | mövzu güclüdür, mexanika dərinlik mixed-dir |
| hekayə-driven puzzle | hekayə oyunda qalma yaradır, puzzle aydınlıq inconsistent-dir |
| Realistic relevance | tam realizm tələb olunmadan yaxşı işləyir |

---

# 21. Əsas uğur faktorları

## 21.1. Güclü və fərqli fantasy

“İnsanların rəqəmsal həyatını araşdırmaq” dərhal başa düşülür.

## 21.2. Information özü reward-dur

Yeni məlumat tapmaq progression hissi verir.

## 21.3. hekayə və oyun gedişi eyni materialdan qurulur

Email, profile, chat və məlumat həm mexanika, həm narrative-dir.

## 21.4. Real-world relevance

Privacy və digital harm hekayə-ni abstract cyber fiction-dan çıxarır.

## 21.5. Low technical barrier

oyunçu peşəkar technical knowledge olmadan oynaya bilir.

---

# 22. Əsas uğursuzluq nümunə-lər

1. **Scripted progression oyunçu knowledge-i tanımır.**
2. **Localization/writing text-heavy oyun gedişi-i birbaşa zəiflədir.**
3. **Clue collection bəzən UI hunt-a çevrilir.**
4. **Search real search space əvəzinə expected query routing olur.**
5. **təkrarçılıq case content dəyişsə belə qalır.**
6. **One-off puzzle-lər əlavə ilkin öyrətmə cost yaradır.**
7. **Timer bəzi reasoning segmentlərini trial-and-error-a çevirir.**
8. **UI çətinlik working-memory yükünü artırır.**
9. **Ethical message bəzən preachy hiss olunur.**

---

# 23. Bizim gələcək oyun üçün dizayn dərsləri

## 23.1. oyunçu knowledge first-class state olmalıdır

Eyni fakt müxtəlif mənbələrdən tapıla bilər.

## 23.2. Multiple valid routes lazımdır

Investigation bir correct click sequence olmamalıdır.

## 23.3. Search system real exploration hissi verməlidir

Exact query dependency minimum olmalıdır.

## 23.4. Information → hypothesis → action → nəticə loop qur

Sadəcə information → next objective yox.

## 23.5. Writing oyun gedişi budget-in hissəsidir

Writer və localization process production-un mərkəzində olmalıdır.

## 23.6. UI dəlil workspace kimi dizayn olunmalıdır

Notes və relationship management sonradan əlavə olunan convenience feature deyil.

## 23.7. təkrarçılıq cognitive task səviyyəsində ölçülməlidir

Yeni hekayə content eyni reasoning task-ı gizlətməməlidir.

## 23.8. Timer yalnız öyrənilmiş mexanika-də istifadə olunmalıdır

Investigation thinking time-a ehtiyac duyur.

---

# 24. imkan Map

## 24.1. Organic information graph

Static progression chain əvəzinə networked dəlil.

## 24.2. Redundant dəlil paths

Eyni nəticəyə müxtəlif məlumat source-lardan gəlmək.

## 24.3. Real hypothesis system

oyunçu öz theory-sini qurur və sistem bunu test etməyə imkan verir.

## 24.4. Social nəticə

Tapdığın information yalnız puzzle açmır, person/world state dəyişir.

## 24.5. Better dəlil UX

Searchable notebook, pinned facts, provenance və contradiction tracking.

## 24.6. Human-system oyun gedişi

Technical access ilə interpersonal leverage-i birləşdirmək.

---

# 25. Hacknet və Midnight Protocol ilə ilkin synthesis

Üç oyunun dərinlik modeli fərqlidir:

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

Bu artıq genre-level dizayn principle üçün güclü dəlil-dir.

Ən maraqlı hybrid istiqamət:

> **Hacknet-in oyuna dalma hissi və organic snooping-i + Midnight Protocol-un meaningful nəticə-u + Cyber Manhunt-un information graph/deduction fantasy-si.**

Amma bu feature stacking kimi edilməməlidir.

Core dizayn əvvəlcə bir əsas fantasy və bir əsas qərar loop ətrafında qurulmalıdır.

---

# 26. Açıq suallar

1. Cyber Manhunt 2 original-dakı linearity və dəlil-state problemlərini nə qədər həll edib?
2. Original-da English localization improvement patch-ləri rəy cohort-larında ölçülə bilərmi?
3. The Operator eyni information-driven loop-u daha az scripted hiss etdirirmi?
4. Orwell daha az mexanika ilə daha güclü deduction/ethical tension yaradırmı?
5. Mainlining information-search və hacking arasında necə balans qurur?
6. Search freedom artanda oyunçu confusion nə qədər artır?

---

# 27. Mənbələr

## Daxili

- `data/processed/cyber-manhunt/statistics.json`
- `data/processed/cyber-manhunt/reviews.jsonl`
- `data/reports/cyber-manhunt/summary.md`
- `analysis/cyber-manhunt/theme-analysis.md`
- `config/aspect_taxonomy.yaml`

## Xarici

**Steam mağaza — Cyber Manhunt**  
https://store.steampowered.com/app/1216710/

**GamerSky — Aluba Studio interview**  
https://club.gamersky.com/activity/435462?club=163

**indienova — Cyber Manhunt project page**  
https://indienova.com/g/cyber-manhunt

---

# Status

**Mərhələ:** Cyber Manhunt per-game deep araşdırma — əsas mərhələ tamamlanıb  
**məlumat toplusu:** 847 verified Steam-provided English reviews  
**Növbəti:** Hacknet + Midnight Protocol + Cyber Manhunt oyunlararası müqayisə və sonra növbəti digital-investigation target.
