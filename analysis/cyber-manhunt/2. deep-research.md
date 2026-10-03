# Cyber Manhunt — Dərin araşdırma

## Rəhbərlik üçün xülasə

Cyber Manhunt əvvəlki iki istinad oyunundan fərqli olaraq dərinliyi terminal əmrlərinin icrası və taktiki hərəkət büdcəsindən yox, **məlumat kəşfi, məntiqi nəticə çıxarma, sosial kontekst və hekayə yönümlü araşdırma** üzərindən qurur.

Yoxlanmış Steam məlumat toplusu:

- 847 rəy
- 681 müsbət
- 166 mənfi
- **80.40% müsbət rəy nisbəti**

Ən vacib nəticə:

> **Cyber Manhunt-un əsas gücü “internetdə iz axtaran rəqəmsal araşdırmaçı” rol hissidir; əsas zəifliyi isə oyunçunun öz məntiqi nəticə çıxarma və intuisiyası ilə irəliləməsi əvəzinə tez-tez əvvəlcədən təyin olunmuş ipucu ardıcıllığı və irəliləyiş şərtlərinə bağlanmasıdır.**

Oyun real dəyər yaradır:
- hekayə və iş üzrə maraq;
- şəxslər haqqında parçalanmış məlumat toplamaq;
- müxtəlif informasiya mənbələrini əlaqələndirmək;
- məxfilik və sosial zərər kimi real həyatdakı mövzuları oyun sisteminə daxil etmək;
- sadələşdirilmiş, amma tanınan kiber/sosial mexanikalar ilə əlçatanlıq yaratmaq.

Amma bu dəyər aşağıdakılarla zəifləyir:
- sərt xətti irəliləyiş;
- ipucu və dəlilin sistem tərəfindən qəbulu problemləri;
- lokallaşdırma və yazı keyfiyyəti;
- UI istifadəsində çətinlik;
- təkrarlanan məlumat iş axını;
- bəzi birdəfəlik mini-oyunlarda aydınlıq və vaxtlama problemi.

Ən ciddi məhsul siqnalı ilk sessiya qrupundadır:

- 0–1h: **27.78% müsbət**
- 1–3h: **44.07% müsbət**
- 10h+: **90.72% müsbət**

İlk 3 saatdakı 95 rəyin **62.11%-i mənfi**-dir. Bu seçim qərəzi daşıyır, amma Cyber Manhunt-un əsas problemi “oyun gec açılır”dan daha çox **ilk saatlarda oyunçu gözləntisi ilə oyunun real araşdırma qaydaları arasındakı uyğunsuzluq** kimi görünür.

Ətraflı kəmiyyət yönümlü sənəd:

`analysis/cyber-manhunt/theme-analysis.md`

---

# 1. Araşdırmanın əhatəsi və məlumat keyfiyyəti

Məlumat toplusunun kəsimi: **2026-10-02**

- xam rəylər: 847
- təkrarsız rəylər: 847
- müsbət: 681
- mənfi: 166
- median oyun müddəti: 9.27h
- orta müsbət rəy oyun müddəti: 12.07h
- orta mənfi rəy oyun müddəti: 6.33h
- çox qısa rəylər: 172

Əsas məlumat:

- `data/processed/cyber-manhunt/reviews.jsonl`
- `data/processed/cyber-manhunt/statistics.json`
- `data/reports/cyber-manhunt/summary.md`

Steam-in ingilisdilli kimi qaytardığı mətn toplusu daxilində bəzi başqa-dilli rəylər də var. Buna görə rəy sayı və tövsiyə statistikasını istifadə edirik, amma söz əsaslı mövzu faizi dəqiq “ingilisdilli oyunçular arasında yayılma” kimi təqdim edilmir.

---

# 2. Məhsul və bazar görünüşü

Steam App ID: **1216710**

- yaradıcı: Aluba Van+ / Aluba Studio
- Buraxılış: 2 February 2021
- Erkən Giriş: August 2020
- tək oyunçulu
- Demo mövcuddur
- Əsas təqdimat: hekayə yönümlü tapmaca oyunu
- Mövzular: böyük məlumat kütlələri, məxfilik, kiber zorakılıq, onlayn mühakimə, araşdırma.

Yaradıcı oyunu sadəcə “cəlbedici hakerlik” rol hissidir kimi yox, real internet davranışları və sosial zərər mövzuları üzərindən qurmaq istədiyini açıq şəkildə bildirir.

Bu Cyber Manhunt-u Hacknet və Midnight Protocol-dan ayırır:

```text
Hacknet → özünü haker kimi hiss etmə
Midnight Protocol → tactical özünü haker kimi hiss etmə
Cyber Manhunt → rəqəmsal araşdırmaçı və sosial/kiber müşahidəçi rol hissi
```

---

# 3. Oyunun mahiyyəti

Ən düzgün qısa təsvir:

> **Computer-interfeys daxilində oynanan hekayə-driven rəqəmsal araşdırma və sosial mühəndislik tapmaca oyunu.**

Əsas təcrübə:

```text
iş haqqında ilkin məlumat
→ açıq/məxfi məlumat axtar
→ şəxslər və əlaqələr haqqında profil qur
→ əlavə giriş imkanları aç
→ yeni məlumat tap
→ ipuclarını əlaqələndir
→ məntiqi düşünmə/puzzle mərhələsi
→ iş və hekayə nəticəsi
```

Burada ən vacib fərq budur:

> Access əldə etmək məqsəd deyil; yeni məlumat qat-ə keçid vasitəsidir.

Bu, bizim əvvəlki araşdırma-də axtardığımız dairəvi məlumat dövrü-a çox yaxındır.

---

# 4. Oyunçunun rol hissi

Cyber Manhunt-un əsas rol hissidir:

> **“Mən rəqəmsal izlərdən insanların kim olduğunu və nə baş verdiyini çıxara bilirəm.”**

Bu rol hissi üç hissədən yaranır.

## 4.1. Məlumat üstünlüyü

Oyunçu əvvəl az məlumat bilir, sonra hədəf şəxs haqqında çox şey öyrənir.

Bu irəliləyişin özü mükafat hissi yaradır.

## 4.2. Rəqəmsal müşahidə və maraq

rəylərdə “nosey”, “sleuth”, “araşdırma”, “digging through məlumat” tipli ifadələr görünür.

oyunçu yalnız məqsəd üçün yox, “burada başqa nə var?” marağı ilə davam edə bilir.

## 4.3. İnsan davranışını anlama

Oyun texniki sistemlə yanaşı insan davranışı, əlaqələr və məxfilik zəifliklərini də oyun gedişi materialına çevirir.

Bu Hacknet-in fayl sistemi curiosity-sini daha social direction-a aparır.

---

# 5. İnsanlar niyə başlayır?

Əsas ilkin cəlbedici amillər:

- Orwell tipli araşdırma rol hissi;
- hacker/detective premise;
- computer desktop interfeys;
- real həyatdakı məxfilik və cyber themes;
- hekayə mystery;
- unusual indie concept.

mağaza page və rəylərdən görünən gözlənti:

> “mən məlumatları özüm tapıb birləşdirəcəyəm.”

Əgər ilk saatda experience bundan çox:

> “düzgün highlighted clue-u tapıb növbəti trigger-i açacağam”

kimi hiss olunursa, disappointment çox tez yaranır.

---

# 6. İnsanlar niyə davam edir?

10h+ qrup-da müsbət rəy nisbəti **90.72%**-dir.

Bu causation deyil, amma uzun oynayan audience-in nəyi dəyərləndirdiyini nümunə-lar göstərir:

- iş-lərin bir-birinə bağlanması;
- dark hekayə;
- characters və motivations;
- məlumat accumulation;
- araşdırma atmosphere;
- puzzle variety;
- social themes;
- hekayə revelations.

Cyber Manhunt-un oyunda qalma sistemi əsasən:

> **curiosity + narrative tamamlanma hissi**

üzərindədir.

Bu Hacknet ilə oxşardır, amma məlumat chain burada daha explicit əsas oyun dövrü-dur.

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

- araşdırma-ın çox linear hiss olunması;
- ipuclarının oyunçuya “tapdırılması” əvəzinə UI tərəfindən göstərilməsi;
- translation;
- UI istifadəsində çətinlik;
- sadələşdirilmiş qarşılıqlı əlaqə;
- hekayə hook-un bəzi oyunçu-lər üçün gec işləməsi;
- “mən özüm düşünəcəyəm” gözlənti-ının zəif qarşılanması.

### Əsas dərs

> **Investigation game ilk saatda oyunçuya real bir məntiqi nəticə çıxarma victory verməlidir.**

təlim hissəsi yalnız interfeys göstərməməlidir.

oyunçu ilk sessiyada:

> “bunu mən tapdım”

hissini yaşamalıdır.

---

# 8. Core Loop və System dərinlik

Cyber Manhunt-un böyük üstünlüyü budur:

Dərinlik üçün çox sayda combat/tactical system lazım deyil.

Dərinlik məlumat relationships-dən yarana bilər.

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

Belə graph oyunçuya böyük qərar space verə bilər.

Amma current implementation tez-tez bu graph-i tam sərbəst buraxmır.

rəylərdə:
- “already knew cavab but game did not accept it”;
- “wrong clue source”;
- “same search later suddenly works”;
- “dəqiq dəlil required”

tipli complaint-lər təkrarlanır.

Bu systemic dərinlik-i scripted dərinlik-ə çevirir.

---

# 9. Linearity və Deduction Problemi

LINEARITY_SCRIPTING namizəd-lərində:

- **55.88% mənfi**
- məlumat toplusu baseline-dan **2.85×** yüksək mənfi concentration.

Bu ən güclü dizayn risklərdən biridir.

Investigation game-də oyunçu iki state daşıyır:

1. **game state**
2. **knowledge state**

Ən yaxşı detective dizayn-də bunlar mümkün qədər uyğunlaşır.

Cyber Manhunt-un zəif anlarında:

```text
player knows cavab
≠
game accepts cavab
```

olur.

### dizayn dərsi

> **oyunçunun həqiqətən bildiyi məlumat progress üçün valid olmalıdır, hətta onu designer-in nəzərdə tutduğu dəqiq route ilə tapmayıbsa.**

Bu gələcək concept üçün çox vacibdir.

---

# 10. Clue və dəlil dizayn

CLUE_EVIDENCE_QUALITY:

- 120 mentions
- **29.17% mənfi**

rəylərdə iki opposite problem var.

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

Core rol hissi güclüdür.

Problem search engine-in çox deterministic olmasıdır.

Əgər yalnız dəqiq expected query işləyirsə:

> search system deyil, disguised diajurnal qeydiue tree yaranır.

Gələcək dizayn üçün imkan:

- fuzzy query;
- multiple clue paths;
- partial results;
- noise;
- redundant dəlil;
- conflicting sources.

Bu məlumat oyun gedişi-ə real ustalaşma verə bilər.

---

# 12. Social Engineering

yaradıcı bu sahə üçün xüsusi araşdırma apardığını deyir.

oyunçu experience-də bu:
- hədəf şəxs behavior;
- relationship;
- trust;
- personal context

kimi human məlumat-u oyun gedişi materialına çevirir.

Bu çox güclü concept direction-dır.

Amma bəzi rəylər execution-u trial-and-error kimi qəbul edir.

### dizayn dərsi

> **Human qarşılıqlı əlaqə puzzle-i “correct diajurnal qeydiue option” yox, əvvəl topladığın məlumat-dan leverage istifadə etmək üzərində qurulmalıdır.**

Bu zaman araşdırma və social qarşılıqlı əlaqə eyni loop-a çevrilir.

---

# 13. hekayə və Writing

STORY_NARRATIVE:

- 315 mentions
- mənfi ratio demək olar məlumat toplusu baseline ilə eynidir.

Bu hekayə-nin əhəmiyyətsiz olması deyil.

hekayə həm müsbət, həm mənfi rəyin əsas müzakirə obyektidir.

müsbət:
- interconnected işs;
- dark themes;
- curiosity;
- emotional revelations.

mənfi:
- awkward localization;
- dayaz diajurnal qeydiue;
- preachy tone;
- inconsistent character writing;
- weak or forced moments.

LOCALIZATION_WRITING isə ayrıca çox güclü risk-dir:

- 188 mentions
- **36.17% mənfi**
- baseline-dan **1.85×** yüksək.

### Fundamental lesson

> **Text-driven game-də writing və localization mexanika qədər core production discipline-dir.**

Poor ifadələr:
- ipucu məntiqi-i;
- character believability-ni;
- puzzle instruction-u;
- emotional nəticə-i

bir anda zəiflədə bilir.

---

# 14. Puzzle Variety vs Puzzle aydınlıq

Cyber Manhunt təkrarçılıq-ı qırmaq üçün müxtəlif one-off puzzle və minigame-lər istifadə edir.

Bu müsbət rəylərdə variety kimi təriflənir.

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

Bu yayılma göstəricisi deyil.

Amma high-impact uğursuzluq nümunəsidir.

Bir neçə rəy-da oyunçu ümumi oyunu bəyəndiyini, amma bu mandatory segment səbəbilə tövsiyə-ı mənfi etdiyini deyir.

### Principle

> **Mandatory side-system əsas əsas oyun dövrü qədər cilalanmış olmalıdır; yoxsa bir neçə dəqiqəlik zəif mexanika saatlarla qurulan goodwill-i məhv edə bilər.**

---

# 16. təkrarçılıq

təkrarçılıq:

- 57 mentions
- **43.86% mənfi**
- baseline-dan **2.24×** yüksək.

Cyber Manhunt sübut edir ki:

> məlumat oyun gedişi özü avtomatik variation yaratmır.

Əgər hər hədəf şəxs:

```text
profile
→ search
→ account
→ clue
→ next profile
```

strukturuna çevrilirsə, məzmun dəyişsə də cognitive task eyni qala bilər.

Bu artıq üç oyunda təkrarlanan principle-dir:

> **təkrarçılıq action skin-dən yox, qərar structure-dan gəlir.**

---

# 17. UI/UX

UI araşdırma game-də xüsusilə vacibdir.

oyunçu eyni anda:
- müxtəlif şəxsləri;
- məlumat parçalarını;
- timelines;
- relationships;
- məqsəds

idarə edir.

Yəni UI:

> **oyunçunun external working memory-sidir.**

rəylərdə scroll, hover, click detection, layout və platform-specific issues məntiqi düşünmə cost-u artırır.

Gələcək concept üçün:
- dəlil board;
- search hihekayə;
- pinned facts;
- relationship graph;
- back/forward hihekayə;
- open tabs;
- automatic provenance

kimi sistemlər ciddi dəyər yarada bilər.

---

# 18. realizm və həqiqilik hissi

REALISM_ACCURACY:

- 36 mentions
- yalnız **8.33% mənfi**.

yaradıcı real social events və subject-matter araşdırma istifadə edib.

oyunçu-lər tam technical realizm tələb etmir.

Onlara daha çox lazım olan:

- tanınan behavior;
- plausible məlumat chain;
- human mistakes;
- məxfilik leakage jurnal qeydiic;
- ardıcıl cause/effect.

Bu artıq üç oyun üzrə güclənən oyunlararası prinsip-dir:

> **seçilmiş həqiqilik hissi tam simulation-dan daha effektiv ola bilər.**

---

# 19. Ethical və Social Themes

yaradıcı-in əsas məqsədlərindən biri:
- məxfilik;
- onlayn mühakimə;
- digital harm;
- real social nəticələr

haqqında oyunçu-i düşündürməkdir.

Bu mövzular müsbət rəylərdə meaningful sayılır.

Amma bəzi mənfi rəylər:
- moralizing;
- stereotypes;
- forced message

şikayəti edir.

### dizayn dərsi

> **Ethical message oyunçunun öz məntiqi nəticə çıxarma-indən doğanda daha güclüdür; designer nəticəni birbaşa diktə edəndə preachy riski artır.**

---

# 20. yaradıcı Intent vs oyunçu Outcome

| Intent | Outcome |
|---|---|
| Real-world social resonance | Güclü concept, amma ingilis dili writing keyfiyyəti təsiri azalda bilir |
| Accessible cyber-araşdırma | əlçatanlıq yüksəkdir, amma bəzi oyunçu üçün dərinlik çox scripted-dir |
| Social-engineering həqiqilik hissi | mövzu güclüdür, mexanika dərinlik mixed-dir |
| hekayə-driven puzzle | hekayə oyunda qalma yaradır, puzzle aydınlıq inconsistent-dir |
| Realistic relevance | tam realizm tələb olunmadan yaxşı işləyir |

---

# 21. Əsas uğur faktorları

## 21.1. Güclü və fərqli rol hissi

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

# 22. Əsas uğursuzluq nümunələr

1. **Scripted progression oyunçu knowledge-i tanımır.**
2. **Localization/writing text-heavy oyun gedişi-i birbaşa zəiflədir.**
3. **Clue collection bəzən UI hunt-a çevrilir.**
4. **Search real axtarış sahəsi əvəzinə expected query routing olur.**
5. **təkrarçılıq iş məzmun dəyişsə belə qalır.**
6. **One-off puzzle-lər əlavə ilkin öyrətmə cost yaradır.**
7. **Timer bəzi məntiqi düşünmə segmentlərini trial-and-error-a çevirir.**
8. **UI istifadəsində çətinlik working-memory yükünü artırır.**
9. **Ethical message bəzən preachy hiss olunur.**

---

# 23. Bizim gələcək oyun üçün dizayn dərsləri

## 23.1. oyunçu knowledge first-class state olmalıdır

Eyni fakt müxtəlif mənbələrdən tapıla bilər.

## 23.2. Multiple valid routes lazımdır

Investigation bir correct click epizod olmamalıdır.

## 23.3. Search system real exploration hissi verməlidir

Exact query dependency minimum olmalıdır.

## 23.4. Information → hypothesis → action → nəticə loop qur

Sadəcə məlumat → next məqsəd yox.

## 23.5. Writing oyun gedişi budget-in hissəsidir

Writer və localization process production-un mərkəzində olmalıdır.

## 23.6. UI dəlil workspace kimi dizayn olunmalıdır

Notes və relationship management sonradan əlavə olunan convenience feature deyil.

## 23.7. təkrarçılıq cognitive task səviyyəsində ölçülməlidir

Yeni hekayə məzmun eyni məntiqi düşünmə task-ı gizlətməməlidir.

## 23.8. Timer yalnız öyrənilmiş mexanika-də istifadə olunmalıdır

Investigation thinking time-a ehtiyac duyur.

---

# 24. imkan Map

## 24.1. Organic məlumat graph

Static progression chain əvəzinə networked dəlil.

## 24.2. Redundant dəlil paths

Eyni nəticəyə müxtəlif məlumat mənbələrdan gəlmək.

## 24.3. Real hypothesis system

oyunçu öz theory-sini qurur və sistem bunu test etməyə imkan verir.

## 24.4. Social nəticə

Tapdığın məlumat yalnız puzzle açmır, person/world state dəyişir.

## 24.5. Better dəlil UX

Searchable notebook, pinned facts, provenance və contradiction tracking.

## 24.6. Human-system oyun gedişi

Technical giriş ilə interpersonal leverage-i birləşdirmək.

---

# 25. Hacknet və Midnight Protocol ilə ilkin synthesis

Üç oyunun dərinlik modeli fərqlidir:

```text
Hacknet
execution depth

Midnight Protocol
tactical/system depth

Cyber Manhunt
məlumat/məntiqi nəticə çıxarma depth
```

Hər üçündə eyni problem başqa formada görünür:

```text
repeated cognitive task
→ pattern becomes visible
→ rol hissi weakens
```

Bu artıq genre-level dizayn principle üçün güclü dəlil-dir.

Ən maraqlı hybrid istiqamət:

> **Hacknet-in oyuna dalma hissi və organic snooping-i + Midnight Protocol-un meaningful nəticə-u + Cyber Manhunt-un məlumat graph/məntiqi nəticə çıxarma rol hissidir.**

Amma bu feature stacking kimi edilməməlidir.

Core dizayn əvvəlcə bir əsas rol hissi və bir əsas qərar loop ətrafında qurulmalıdır.

---

# 26. Açıq suallar

1. Cyber Manhunt 2 original-dakı linearity və dəlil-state problemlərini nə qədər həll edib?
2. Original-da ingilis dili localization improvement patch-ləri rəy qrup-larında ölçülə bilərmi?
3. The Operator eyni məlumat-driven loop-u daha az scripted hiss etdirirmi?
4. Orwell daha az mexanika ilə daha güclü məntiqi nəticə çıxarma/ethical tension yaradırmı?
5. Mainlining məlumat-search və hakerlik arasında necə balans qurur?
6. Search sərbəstlik artanda oyunçu çaşqınlıq nə qədər artır?

---

# 27. Mənbələr

## Daxili

- `data/processed/cyber-manhunt/statistics.json`
- `data/processed/cyber-manhunt/reviews.jsonl`
- `data/reports/cyber-manhunt/summary.md`
- `analysis/cyber-manhunt/theme-analysis.md`
- `config/aspect_taxonomy.yaml`

## Xarici

**Steam mağazası — Cyber Manhunt**  
https://store.steampowered.com/app/1216710/

**GamerSky — Aluba Studio müsahibə**  
https://club.gamersky.com/activity/435462?club=163

**indienova — Cyber Manhunt project page**  
https://indienova.com/g/cyber-manhunt

---

# Status

**Mərhələ:** Cyber Manhunt per-game deep araşdırma — əsas mərhələ tamamlanıb  
**məlumat toplusu:** 847 verified Steam-provided ingilis dili reviews  
**Növbəti:** Hacknet + Midnight Protocol + Cyber Manhunt oyunlararası müqayisə və sonra növbəti rəqəmsal araşdırma hədəf şəxs.
