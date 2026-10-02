# Hacknet — Semantic Audit 01: Repetition və Technical Stability

## 1. Məqsəd

Bu sənəd `analysis/hacknet/theme-corpus-scan.md`-də ən güclü negative-association göstərən iki theme-i daha dərindən araşdırır:

1. `REPETITION`
2. `BUGS_COMPATIBILITY`

Məqsəd artıq sadəcə "bu söz neçə review-da keçir?" sualına yox, aşağıdakı suala cavab verməkdir:

> Oyunçu konkret olaraq nədən narazıdır və həmin narazılıq hansı dizayn/texniki kök səbəbdən yaranır?

Bu audit final full-dataset semantic classification deyil. Lakin full corpus retrieval + seçilmiş representative review-lərin manual semantik oxunması birlikdə istifadə olunur.

---

# 2. Evidence bazası

Full corpus:

- **11,773 verified Steam review**
- `REPETITION` candidate: **517**
- `BUGS_COMPATIBILITY` candidate: **502**

Manual semantic audit üçün:

### Repetition

- helpful positive review-lər
- helpful negative review-lər
- recent positive/negative review-lər
- müxtəlif playtime segmentlərindən nümunələr

ümumilikdə təxminən **23 representative review** ayrıca oxunub.

### Bugs / compatibility

Eyni prinsip ilə təxminən **24 representative review** ayrıca oxunub.

Bu sample-lar random population estimate deyil. Məqsəd root-cause discovery-dir.

---

# 3. Repetition — əsas nəticə

Full corpus candidate nəticəsi:

- mention: **517**
- corpus share: **4.39%**
- positive review: 397
- negative review: 120
- overall positive ratio: **76.79%**
- negative-review enrichment: **3.95×**

Bu artıq repetition-ın sadəcə bir neçə sərt review-un şikayəti olmadığını göstərir.

Amma manual audit daha vacib bir fərqi üzə çıxarır:

> Oyunçuların problemi "eyni command-ı çox yazmaq"dan daha dərindir. Əsas problem **eyni qərar strukturunun təkrar olunmasıdır**.

---

# 4. Repetition subtheme-ləri

## 4.1. Same command sequence

Deterministik subtheme candidate:

- **125 review**
- positive ratio: **64.00%**
- negative enrichment: **6.13×**

Manual review-lərdə təkrarlanan pattern:

```text
connect
→ probe
→ uyğun port cracker
→ digər cracker-lər
→ PortHack
→ filesystem
→ file tap / sil / götür
→ növbəti target
```

Problem command-ların özündə deyil.

Problem:

> target dəyişsə də problem-solving prosesi dəyişmir.

Oyunçu bir dəfə sistemi öyrəndikdən sonra sonrakı target-lərdə çox vaxt yeni hipotez qurmağa ehtiyac duymur.

### Design nəticəsi

**Surface variation** kifayət deyil.

Yeni server:

- başqa IP;
- başqa filename;
- başqa port sayı;
- başqa story context

daşısa da həll metodu eynidirsə, oyunçu onu yeni problem kimi yox, əvvəlki problemin skin-i kimi görür.

---

## 4.2. Mission similarity

Candidate:

- **53 review**
- positive ratio: **62.26%**
- negative enrichment: **6.43×**

Bu daha dar, amma çox güclü siqnaldır.

Manual nümunələrdə oyunçular:

- "same gameplay";
- "every PC";
- "every challenge";
- "same process"

tipli ifadələr istifadə edir.

Bu, repetition probleminin təkcə terminal micro-interaction deyil, **mission architecture** səviyyəsində də olduğunu göstərir.

### Design nəticəsi

Mission variety yalnız objective mətninin dəyişməsi deyil.

Missiyalar arasında fərq yaratmaq üçün ən azı bunlardan biri dəyişməlidir:

- informasiya mənbəyi;
- access route;
- risk modeli;
- tool seçimi;
- target behavior;
- time pressure;
- consequence;
- required reasoning;
- social layer;
- network topology.

---

## 4.3. Low decision depth

Çox dar high-precision candidate:

- **12 review**
- 10 negative
- positive ratio: **16.67%**
- negative enrichment: **14.20×**

Say azdır, ona görə prevalence kimi istifadə edilməməlidir.

Lakin manual audit bu problemi açıq göstərir:

- "no strategy";
- "nothing to think about";
- "no puzzles";
- "no problem solving";
- hacking tool-larının "magic program" kimi işləməsi.

Bu theme repetition-ın əsas kök səbəblərindən biridir.

### Əsas insight

> Təkrarçılıq çox vaxt content azlığından yox, **decision density azlığından** yaranır.

Oyunçu hər target-də eyni optimal sequence-ni artıq bilirsə, interaction sayı çox olsa da qərar sayı azdır.

Bu yeni oyun üçün çox vacib design metric ola bilər:

> **Actions per minute** yox, **meaningful decisions per minute**.

---

## 4.4. Waiting / slow interaction

Candidate:

- **185 review**
- positive ratio: **89.73%**
- negative enrichment: **1.75×**

Bu, repetition qədər sərt negative driver deyil.

Amma manual sample-larda:

- tool animation gözləmək;
- file deletion-ın yavaş olması;
- eyni sequence zamanı progress gözləmək

təkrarın hissini daha da ağırlaşdırır.

### Design nəticəsi

Eyni interaction:

- qərar tələb edirsə → tension ola bilər;
- nəticəsi artıq məlumdursa və sadəcə gözləmək qalırsa → friction olur.

Deməli duration özü problem deyil.

**Known outcome + forced waiting** problemdir.

---

## 4.5. Positive review-lərdə də repetition açıq qəbul olunur

Ən vacib tapıntılardan biri budur.

Repetition candidate-lərinin **397-si positive review**-dur.

Manual positive nümunələrdə belə ifadələr görünür:

- repetitive olsa da story yaxşıdır;
- command-lar təkrar olur, amma immersion kompensasiya edir;
- routine olur, amma soundtrack və atmosphere oyunu daşıyır;
- hacking hissəsi təkrarlanır, investigation hissəsi daha maraqlıdır.

Bu, iki şeyi göstərir.

### Birinci

Repetition real problemdir.

Positive review yazan oyunçu belə onu görür.

### İkinci

Hacknet-də başqa value driver-lər həmin problemi bir müddət kompensasiya edə bilir:

- story;
- mystery;
- immersion;
- soundtrack;
- exploration;
- hacker fantasy.

### Product nəticəsi

> Uğurlu oyun olmaq üçün heç bir zəiflik olmamalıdır yanaşması səhvdir.

Daha real sual:

> Core weakness-i hansı daha güclü value layer-lər kompensasiya edir və bu kompensasiya nə qədər davam edir?

---

# 5. Repetition üçün əsas root-cause modeli

Hazırkı evidence əsasında Hacknet repetition problemi belə modelləşdirilə bilər:

```text
sadələşdirilmiş hacking abstraction
        ↓
tool-lar konkret port üçün "açar"a çevrilir
        ↓
optimal sequence tez öyrənilir
        ↓
target-lər arasında qərar strukturu az dəyişir
        ↓
player discovery → execution-a çevrilir
        ↓
forced waiting / repeated file work sürtünmə yaradır
        ↓
story və atmosphere müəyyən müddət kompensasiya edir
        ↓
bəzi oyunçular üçün fantasy dağılır və repetition görünür
```

Bu, Hacknet-dən çıxan ən vacib design model-lərindən biridir.

---

# 6. Technical stability — əsas nəticə

`BUGS_COMPATIBILITY` full corpus:

- mention: **502**
- corpus share: **4.26%**
- positive: 365
- negative: 137
- overall positive ratio: **72.71%**
- negative enrichment: **4.65×**

Bu, hazırkı scan-də negative review-lərlə ən güclü əlaqəli geniş theme-dir.

Burada vacib fərq:

> Bu problem game design zəifliyi deyil, amma player review outcome-a birbaşa təsir edir.

Final genre research-də technical complaint-lər design complaint-lərdən ayrıca saxlanmalıdır.

---

# 7. Technical problem subtheme-ləri

## 7.1. Launch / display / setup problemi

Candidate:

- **53 review**
- positive: 25
- negative: 28
- positive ratio: **47.17%**
- negative enrichment: **9.00×**
- orta playtime: **5.34 saat**

Manual review-lərdə:

- black screen;
- game launch etmir;
- settings.txt tələb olunur;
- XNA branch workaround;
- resolution problemi;
- 4K / tiny screen;
- compatibility workaround

görünür.

Bu subtheme negative recommendation üçün çox güclü riskdir.

### Əsas insight

First-session üçün ən yaxşı onboarding belə faydasızdır əgər oyun açılmır.

Market analysis zamanı:

> early negative review

həmişə design failure demək deyil.

Buna görə first-hour sentiment araşdırılarkən technical startup friction ayrıca çıxılmalıdır.

---

## 7.2. Crash / freeze

Candidate:

- **172 review**
- negative: 55
- positive ratio: **68.02%**
- negative enrichment: **5.45×**
- orta playtime: **8.60 saat**

Manual recent review-lərdə xüsusilə:

- Mac crash;
- freeze;
- memory leak;
- force quit

şikayətləri görünür.

Maraqlı məqam:

> bəzi positive review-lər də "oyun əladır, amma Mac-də crash edir" deyir.

Bu, Steam thumbs-up/down-un aspect sentiment üçün niyə kifayət etmədiyinə yenə nümunədir.

---

## 7.3. Softlock / progression break

Candidate:

- **79 review**
- negative: 20
- positive ratio: **74.68%**
- negative enrichment: **4.31×**
- orta playtime: **11.17 saat**

Manual nümunələrdə iki fərqli tip görünür.

### Sistem/mission softlock

- mission sequence pozulur;
- progression dayanır;
- mission incomplete qalır.

### Player-induced softlock

- oyunçu gələcək üçün lazım olan password/IP/log faylını silir;
- oyun bunu əvvəlcədən qorumaq və ya recover etmək üçün kifayət qədər guard etmir.

İkinci tip bizim üçün design baxımından xüsusilə maraqlıdır.

### Design nəticəsi

Diegetic filesystem istifadə edəndə:

> "real sistemdə bunu silə bilərsən"

realizmi ilə

> "oyunçunu recover olunmaz vəziyyətə salmamalıyıq"

game-design prinsipi arasında balans lazımdır.

Mümkün həllər:

- recoverable recycle/archive;
- mission-critical dependency protection;
- alternate evidence route;
- restore point;
- warning;
- fail-forward design.

---

## 7.4. Save corruption

Dar candidate:

- **9 review**
- negative enrichment: **5.68×**

Say kiçikdir, prevalence nəticəsi çıxarmaq olmaz.

Amma manual helpful negative review-də save corruption birbaşa recommendation-ı dəyişdirən problem kimi görünür.

Bu tip problem az istifadəçidə baş versə belə high-severity ola bilər.

### Research qaydası

Risk yalnız frequency ilə qiymətləndirilməməlidir.

```text
risk = frequency × severity
```

Save loss az tezlikli, amma çox yüksək severity-li problemdir.

---

# 8. Bugs haqqında positive review-lər nə deyir?

365 bug candidate-i olan review yenə də positive-dir.

Bu ilk baxışda qəribə görünə bilər.

Manual audit göstərir ki, bir neçə pattern var:

### Minor bug

> "few bugs, nothing game-breaking"

### Strong product love

> oyunçu oyunu çox sevir və bug-a baxmayaraq recommend edir.

### Platform-specific caveat

> Windows-da yaxşıdır, Mac-də crash edir.

### Historical issue

> əvvəl problem olub, sonradan işləyib.

Deməli:

> BUG mention = BUG complaint severity

deyil.

Sonrakı semantic classification-da minimum severity ayrıca tutulmalıdır:

- minor;
- disruptive;
- game-breaking;
- data-loss.

---

# 9. Repetition və bugs-u bir-birindən ayırmaq niyə vacibdir?

Hər ikisi negative review ilə güclü əlaqəlidir.

Amma product action tam fərqlidir.

## Repetition

Həll tələb edir:

- mechanic redesign;
- mission variety;
- deeper decisions;
- alternate approaches;
- systemic reactivity.

## Bugs / compatibility

Həll tələb edir:

- QA;
- platform support;
- save safety;
- startup reliability;
- recovery design.

Final genre report-da bunlar eyni "people disliked" listinə atılmamalıdır.

---

# 10. Yeni oyun üçün konkret dərslər

## Dərs 1 — Eyni fantasy-ni təkrar action ilə qarışdırma

Oyunçu hər dəfə hacker fantasy-si yaşaya bilər.

Amma eyni command sequence-nin təkrarı fantasy-ni getdikcə interface choreography-yə çevirir.

Hədəf:

> eyni fantasy, müxtəlif problem strukturları.

---

## Dərs 2 — Tool "key" yox, strategy component olmalıdır

Hacknet-in ən çox tənqid olunan formulu:

```text
port X açıqdır
→ X üçün tool-u işə sal
```

Yeni sistemdə tool mümkün qədər:

- trade-off;
- risk;
- cost;
- alternative route;
- information requirement

yaratmalıdır.

---

## Dərs 3 — Content variety ilə decision variety eyni deyil

100 fərqli server yaradıla bilər.

Amma 100-ü də eyni decision tree-dirsə, content əslində 100 variant deyil.

Production zamanı ayrıca izlənməli metric:

> **unique problem structures**

olmalıdır.

---

## Dərs 4 — Known-outcome waiting-i minimum et

Animation və progress bar fantasy-yə xidmət etdiyi qədər saxlanmalıdır.

Oyunçu nəticəni artıq bilirsə, uzun gözləmə tension yox, friction yaradır.

---

## Dərs 5 — Diegetic freedom softlock yaratmamalıdır

Oyunçuya:

- fayl silmək;
- sistemi dəyişmək;
- log pozmaq

azadlığı verilibsə, mission architecture bunu daşımalıdır.

Fail-forward və recovery mexanizmləri əvvəlcədən dizayn olunmalıdır.

---

## Dərs 6 — Platform stability product experience-in bir hissəsidir

Xüsusilə fictional-computer oyununda real:

- crash;
- black screen;
- freeze

oyunun intentional:

- BSOD;
- hack;
- interface failure

momentləri ilə qarışa bilər.

Bu janrda stability normal oyundan belə daha kritik ola bilər.

---

# 11. Confidence

## High confidence

- Repetition real və recurring complaint-dir.
- Eyni command/tool sequence repetition-ın əsas formalarından biridir.
- Bug/compatibility recommendation riskini ciddi artırır.
- Launch/display və crash problemləri xüsusilə zərərlidir.

## Medium confidence

- Repetition-ın əsas kök səbəbi low decision density-dir.
- Story/immersion/sound repetition-ı müəyyən müddət kompensasiya edir.
- Mission similarity command-level repetition qədər vacibdir.

## Hələ validation tələb edir

- Hansı repetition subtype ən çox churn yaradır?
- Technical audience bu problemə casual audience-dən nə qədər həssasdır?
- Repetition hansı playtime nöqtəsində kritik həddə çatır?
- DLC/mod content repetition problemində nə qədər fərq yaradır?

---

# 12. Növbəti audit

Növbəti risk batch:

1. `ONBOARDING_CLARITY`
2. `PLAYER_AGENCY`
3. `WORLD_REACTIVITY`
4. `UI_USABILITY`
5. `PACING_WAITING`

Bundan sonra value-driver batch:

1. `HACKER_FANTASY`
2. `STORY_NARRATIVE`
3. `IMMERSION`
4. `SOUND_AUDIO`
5. `INVESTIGATION_DISCOVERY`

Bu audit-lər tamamlandıqdan sonra Hacknet üçün semantic taxonomy final formaya gətiriləcək.
