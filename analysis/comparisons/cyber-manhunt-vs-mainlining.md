# Cyber Manhunt vs Mainlining — Rəqəmsal araşdırma və sistemin oyunçu biliyini tanıması

## 1. Məqsəd

Bu müqayisənin məqsədi “hansı oyun daha yaxşıdır?” sualına cavab vermək deyil.

Əsas sual:

> **Cyber Manhunt və Mainlining rəqəmsal araşdırmada oyunçunun bildiyini hansı nöqtədə sistem tərəfindən qəbul edir, hansı nöqtədə isə əvvəlcədən müəyyən edilmiş interaction state tələb edir?**

Bu iki oyun çox faydalı contrast yaradır:

- Cyber Manhunt daha geniş məlumat mənbələri və social-engineering sistemi qurur;
- Mainlining daha manual desktop və evidence-submission modeli verir.

Amma hər ikisində eyni fundamental risk fərqli mərhələdə görünür.

---

## 2. Dataset müqayisəsi

| Metrik | Cyber Manhunt | Mainlining |
|---|---:|---:|
| Rəy sayı | 847 | 304 |
| Müsbət | 681 | 230 |
| Mənfi | 166 | 74 |
| Müsbət payı | **80.40%** | **75.66%** |
| Median oyun müddəti | **9.27h** | **4.82h** |
| 0–1h müsbət | 27.78% | **34.78%** |
| 1–3h müsbət | 44.07% | **62.50%** |
| 3–10h müsbət | 80.49% | 80.10% |
| 10h+ müsbət | 90.72% | **96.88%** |

Dataset ölçüləri fərqlidir. Rəqəmlər birbaşa “keyfiyyət balı” kimi istifadə edilmir.

Vacib siqnal:

> Mainlining ilk 3 saatda Cyber Manhunt-dan daha az sərt qəbul problemi yaşayır, amma ümumi müsbət pay yenə daha aşağıdır.

Bu, Mainlining-in əsas probleminin təkcə onboarding olmadığını göstərir.

---

## 3. Əsas rol hissi

### Cyber Manhunt

> **“İnsanların internetdə buraxdığı izləri tapıb kim olduqlarını, nə etdiklərini və bir-biri ilə necə bağlı olduqlarını açacağam.”**

Əsas fantasy:

- information search;
- social engineering;
- privacy intrusion;
- case progression;
- narrative revelation.

### Mainlining

> **“Şəxsi məlumatı tapıb suspect-in kim olduğunu, harada olduğunu və hansı dəlillə həbs ediləcəyini özüm sübut edəcəyəm.”**

Əsas fantasy:

- desktop investigation;
- hacking access;
- identity;
- location;
- evidence;
- arrest.

### Əsas fərq

Cyber Manhunt:

> **information chain qurmaq**

Mainlining:

> **evidence package qurmaq**

---

## 4. Oyunçunun bilik vəziyyəti

Investigation oyununda iki state var:

1. **game state**
2. **oyunçunun knowledge state-i**

İdeal halda:

```text
oyunçu bilir
≈
sistem bilir ki oyunçu bilir
```

Hər iki oyunun problemli anlarında bu ayrılır.

### Cyber Manhunt

```text
oyunçu cavabı artıq bilir
≠
required clue / search / trigger açılmayıb
```

### Mainlining

```text
oyunçu suspect + crime-i düzgün anlayır
≠
required evidence / location object seçilməyib
```

Bu iki problem eyni kökdən gəlir:

> **designer interaction state oyunçunun knowledge state-indən daha vacib olur.**

---

## 5. Cyber Manhunt — route strictness

Cyber Manhunt-da `LINEARITY_SCRIPTING`:

- 34 mention;
- **55.88% mənfi**;
- baseline-dan **2.85×** yüksək.

Semantic audit-də təkrarlanan pattern:

- cavab məlumdur;
- amma əvvəl başqa clue tapılmalıdır;
- query sonra işləyir, əvvəl işləmir;
- eyni məlumat başqa source-dan gəlsə belə progress açılmır.

Bu:

> **“cavaba necə çatdın?”**

sualını həddindən artıq sərtləşdirir.

---

## 6. Mainlining — answer strictness

Mainlining-də lexical `LINEARITY_SCRIPTING` yüksək risk kimi çıxmır.

Amma semantic audit başqa problem göstərir:

- bir neçə məntiqli dəlil var;
- yalnız konkret file qəbul olunur;
- bir neçə məntiqli location var;
- sistem yalnız konkret cavabı qəbul edir;
- yanlış kombinasiyada hansı komponentin səhv olduğu bilinmir.

Bu:

> **“cavabı hansı obyektlə təqdim etdin?”**

sualını həddindən artıq sərtləşdirir.

### Vacib taxonomy dərsi

`LINEARITY_SCRIPTING` aşağı görünməsi Mainlining-in “az scripted” olduğunu avtomatik sübut etmir.

Semantic problem:

> **scripted progression yox, scripted acceptance**

formasında ola bilər.

Bu gələcək taxonomy üçün vacibdir.

---

## 7. Clue və evidence müqayisəsi

### Cyber Manhunt

Əsas risk:

- clue çox aydın;
- və ya clue qəbul sistemi çox sərt.

`CLUE_EVIDENCE_QUALITY`:

- 120 mention;
- 29.17% mənfi.

### Mainlining

`CLUE_EVIDENCE_QUALITY`:

- 53 mention;
- 34.0% mənfi.

Amma Mainlining-də problem final submission-a daha çox yığılır.

### Fərq

Cyber Manhunt:

> **clue discovery / progression validity**

Mainlining:

> **proof sufficiency / submission validity**

Gələcək oyun üçün hər ikisi ayrıca modelləşdirilməlidir.

---

## 8. Deduction hissi

### Cyber Manhunt

Ən yaxşı anlar:

- fərqli profillər;
- şəkillər;
- hesablar;
- sosial əlaqələr;
- telefon və internet məlumatları

arasında inference qurmaqdır.

Əsas failure:

> game inference-i artıq etmiş kimi olsa da scripted trigger tələb edir.

### Mainlining

Ən yaxşı anlar:

- alias;
- IP;
- real ad;
- location;
- incriminating file

arasında əlaqə qurmaqdır.

Əsas failure:

> inference düzgündür, amma evidence object sistemin gözlədiyi deyil.

### Cross-game principle

> **Deduction satisfaction yalnız cavabı tapmaqdan yox, sistemin həmin cavabı legitim şəkildə tanımasından gəlir.**

---

## 9. Search azadlığı

### Cyber Manhunt

Search daha geniş görünür:

- müxtəlif saytlar;
- social platform-lar;
- məlumat xidmətləri;
- bir neçə hacking/social engineering mexanikası.

Amma exact query dependency yarana bilir.

### Mainlining

Search daha az genişdir:

- browser;
- IP;
- terminal;
- files;
- database.

Amma daha “manual” hiss edə bilir.

Müsbət Mainlining rəylərində:

> paper notes, adlar, IP-lər, əlaqələr

özün saxladığın üçün competence hissi güclüdür.

### Trade-off

Cyber Manhunt:

> geniş informasiya səthi, daha sərt routing riski.

Mainlining:

> dar informasiya səthi, daha çox manual competence hissi.

---

## 10. UI və external working memory

### Cyber Manhunt

Problem:

- çoxsaylı şəxslər;
- scroll/hover;
- relationship;
- search history;
- clue management.

Opportunity:

- evidence board;
- pinned facts;
- provenance;
- relationship graph.

### Mainlining

Problem:

- pəncərə idarəsi;
- notepad limitləri;
- qeydlərin silinməsi;
- case-lər arasında file/history persistence olmaması;
- terminal editing.

### Ortaq nəticə

> **Information game UI-si yalnız input surface deyil; external memory architecture-dır.**

Oyunçunun beynində saxlamalı olduğu məlumatı UI sistemli şəkildə daşımalıdır.

---

## 11. Hacking-in rolu

### Cyber Manhunt

Hacking:

- information source unlock edir;
- social-engineering ilə birləşir;
- bəzi mini-game variation yaradır.

### Mainlining

Hacking:

- çox vaxt access ritualıdır;
- ping → hack → list → download ardıcıllığı təkrarlanır.

### Nəticə

Cyber Manhunt hacking-i daha müxtəlif context-lərə bağlayır.

Mainlining isə investigation fokusunu qorumaq üçün hacking-i sadələşdirir, amma onu həddindən artıq təkrarlanan prosedura çevirə bilir.

### Principle

> **Hacking dərinliyi command complexity deyil; access qərarının sonrakı information state-ə təsiridir.**

---

## 12. Təkrarçılıq

Cyber Manhunt:

- `REPETITION` 43.86% mənfi;
- baseline-dan 2.24×.

Mainlining:

- `REPETITION` 66.7% mənfi;
- baseline-dan 2.74×.

Hər iki oyun göstərir:

> yeni case və yeni story avtomatik olaraq yeni gameplay yaratmır.

Cyber Manhunt-da:

```text
profile
→ search
→ account
→ clue
```

Mainlining-də:

```text
website
→ IP
→ hack
→ download
→ evidence
```

təkrar ola bilir.

### Principle

> **Case variety cognitive task variety ilə ölçülməlidir.**

---

## 13. İlkin öyrətmə və ilk saat

Cyber Manhunt:

- 0–1h: 27.78%
- 1–3h: 44.07%

Mainlining:

- 0–1h: 34.78%
- 1–3h: 62.50%

Mainlining burada daha yaxşı görünür.

Ehtimal olunan səbəblər:

- interaction set daha kiçikdir;
- ilk case mental model-i daha tez göstərir;
- technical system daha sadədir;
- main loop tez aydınlaşır.

Amma Mainlining-də sonrakı problem:

> qaydanı başa düşmək yox, qaydaya etibar etməkdir.

Bu fərq vacibdir.

### Cyber Manhunt

> “Nə etməliyəm / hansı trigger lazımdır?”

### Mainlining

> “Niyə mənim məntiqli cavabım qəbul edilmir?”

---

## 14. Failure feedback

Cyber Manhunt-da:

- progress açılmır;
- clue qəbul edilmir;
- oyunçu required route-u tapmalıdır.

Mainlining-də:

- arrest wrong olur;
- hansı hissənin wrong olduğu aydın deyil;
- başqa kombinasiyalar sınanır.

Hər ikisi trial-and-error yarada bilər.

Amma Mainlining daha yaxşı formal hypothesis UI-si qurur:

```text
person + evidence + location
```

Bu modelin özü çox dəyərlidir.

Problem yalnız feedback və semantic acceptance-dır.

### Opportunity

Bu submission model saxlanıla bilər, amma:

- component confidence;
- alternative evidence;
- source reliability;
- contradiction

ilə zənginləşdirilməlidir.

---

## 15. Story və tematik dərinlik

### Cyber Manhunt

- social harm;
- cyber violence;
- privacy;
- internet behavior;
- daha ağır dramatik ton.

### Mainlining

- dövlət surveillance;
- cybercrime;
- dark humour;
- parody;
- daha yüngül və satirik ton.

Cyber Manhunt hekayəni daha çox retention engine kimi istifadə edir.

Mainlining-də story + desktop immersion + competence fantasy daha balanslıdır.

Bu səbəbdən Mainlining-in daha qısa olması əsas loop üçün uyğun ola bilər.

---

## 16. Realizm

Hər iki oyunda tam texniki realizm əsas success driver deyil.

Cyber Manhunt-da `REALISM_ACCURACY` mənfi konsentrasiya aşağıdır.

Mainlining-də də eyni istiqamət görünür.

Oyunçular:

- hacking-in sadələşdirilməsini;
- saxta proqramları;
- gameified access-i

qəbul edə bilirlər.

Əsas tələb:

> **daxili məntiq ardıcıl olsun.**

### Mainlining nümunəsi

Real command line olmaması problem olmaya bilər.

Amma:

- wrong IP üçün wrong error;
- düzgün evidence-in qəbul edilməməsi;
- itən keystroke

daxili etibarı pozur.

---

## 17. Agency müqayisəsi

### Cyber Manhunt

Əsas güc:

- information discovery;
- bəzi story judgment;
- social-engineering leverage.

Əsas limit:

- scripted progression.

### Mainlining

Əsas güc:

- hansı suspect / evidence / location hypothesis-i təqdim etmək;
- bəzi case-lərdə bir neçə arrest.

Əsas limit:

- uzunmüddətli story state az dəyişir;
- exact evidence acceptance.

### Əsas fərq

Cyber Manhunt-un satisfaction fantasy-si:

> **“mən əlaqəni tapdım.”**

Mainlining-in satisfaction fantasy-si:

> **“mən işi sübut etdim.”**

Gələcək oyun ikisini birləşdirə bilər:

> **“mən əlaqəni tapdım, hypothesis qurdum, sübut etdim və nəticəsini gördüm.”**

---

## 18. Məhsul vədi

Cyber Manhunt store identity-si:

- story-rich puzzle;
- big data;
- hacking;
- privacy;
- social problems.

Bu real core loop-a nisbətən yaxındır.

Mainlining store:

- judgement;
- case completion timing;
- 500 criminals;
- broad investigation choice

kimi daha geniş freedom hissi yaradır.

Mənfi rəylərdə isə Mainlining-in xətti və mission-scoped olması expectation mismatch yaradır.

### Principle

> **Investigation azadlığı marketinqdə yalnız source count ilə yox, action freedom ilə göstərilməlidir.**

---

## 19. Niyə nəticələr fərqlənir? — hipotezlər

### Hipotez 1 — Mainlining daha yaxşı ilk mental model verir

İlk 3 saat rəqəmləri bunu dəstəkləyir.

### Hipotez 2 — Cyber Manhunt daha uzun story/information progression verir

Median:
- Cyber Manhunt: 9.27h
- Mainlining: 4.82h.

Bu daha çox retention materialı yaradır.

### Hipotez 3 — Mainlining-in semantic evidence problemi trust-u sındırır

İşin sonunda oyunçu öz reasoning-inə yox, answer key-ə güvənməyə başlayır.

### Hipotez 4 — Mainlining-in texniki polish problemi uzunmüddətlidir

Yeni rəylərdə də freeze/input/evidence şikayətləri var.

### Hipotez 5 — Cyber Manhunt daha geniş variety verir

Hətta bəzi one-off mini-game-lər zəif olsa da interaction set daha genişdir.

### Hipotez 6 — Mainlining daha düzgün audience-də çox yaxşı işləyir

10h+ cohort müsbət payı 96.88%-dir.

Bu causation deyil, amma uyğun audience üçün desktop/puzzle formatının güclü olduğunu göstərir.

---

## 20. Üç oyunlu recurring principle

Cyber Manhunt + Need to Know + Mainlining birlikdə artıq güclü bir dizayn qaydası yaradır.

### Cyber Manhunt

> exact clue path

### Need to Know

> exact rule interpretation / marking

### Mainlining

> exact evidence object

Üçündə də:

```text
human reasoning
≠
system acceptance
```

olduqda satisfaction düşür.

### Genre-level principle

> **Digital-investigation oyununda sistem “designer-in nəzərdə tutduğu click sequence”i yox, oyunçunun dünyadan çıxardığı təsdiqlənə bilən faktları modelləşdirməlidir.**

Bu final design principles sənədi üçün əsas namizəddir.

---

## 21. Gələcək oyun üçün birləşdirilmiş model

```text
broad information space
→ multiple valid discovery routes
→ persistent knowledge graph
→ player hypothesis
→ semantic evidence bundle
→ action
→ visible consequence
→ changed information space
```

Burada:

- Cyber Manhunt-un məlumat zənginliyi;
- Mainlining-in hypothesis/arrest submission modeli;
- Orwell-un visible consequence modeli

birləşir.

Qaçılmalı olanlar:

- exact clue;
- exact file;
- auto-answer;
- weak feedback;
- reset olunan investigation memory.

---

## 22. Bizim layihə üçün konkret dərslər

1. **Knowledge state interaction state-dən üstün olmalıdır.**
2. Bir faktın bir neçə valid source-u olsun.
3. Search exact query-yə bağlanmasın.
4. Evidence semantic requirement-lə yoxlanılsın.
5. Hypothesis component-lərə bölünsün.
6. Failure feedback reasoning-i inkişaf etdirsin.
7. UI persistent notebook / graph / provenance versin.
8. Hacking yeni informasiya riskləri yaratsın.
9. New case yeni cognitive grammar açsın.
10. Store promise real azadlıqla uyğun olsun.

---

## 23. Nəticə

Cyber Manhunt göstərir:

> **geniş məlumat məkanı güclü investigation fantasy yaradır, amma scripted route həmin fantasy-ni zəiflədə bilər.**

Mainlining göstərir:

> **manual və az yönləndirilən araşdırma competence hissini gücləndirir, amma final answer acceptance insan məntiqindən uzaqlaşanda həmin competence hissi dərhal dağılır.**

Birlikdə:

> **Ən yaxşı digital-investigation sistemi oyunçunun cavaba necə çatdığını məcbur etmir və cavabı hansı konkret UI obyektlə verdiyinə həddindən artıq bağlanmır; o, oyunçunun həqiqətən nə bildiyini və həmin bilikdən hansı hypothesis çıxardığını modelləşdirir.**

---

## 24. Mənbələr

### Cyber Manhunt

- `analysis/cyber-manhunt/theme-analysis.md`
- `analysis/cyber-manhunt/deep-research.md`
- `data/processed/cyber-manhunt/statistics.json`

### Mainlining

- `analysis/mainlining/theme-analysis.md`
- `analysis/mainlining/deep-research.md`
- `data/processed/mainlining/statistics.json`
- `data/processed/mainlining/themes/statistics.json`

## Status

**Müqayisə:** tamamlanıb  
**Əsas finding:** Cyber Manhunt route-u, Mainlining answer acceptance-ı həddindən artıq sərtləşdirir; hər iki halda əsas risk sistemin oyunçunun knowledge state-ni tanımamasıdır.
