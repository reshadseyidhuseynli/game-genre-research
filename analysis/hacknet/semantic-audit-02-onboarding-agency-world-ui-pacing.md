# Hacknet — Semantic Audit 02: Onboarding, Agency, World Reactivity, UI və Pacing

## 1. Məqsəd

Bu sənəd Hacknet üçün aşağıdakı risk sahələrini daha dərindən ayırır:

1. onboarding və clarity;
2. player agency;
3. world reactivity;
4. UI/terminal ergonomics;
5. pacing.

Əvvəlki full-corpus scan-dən sonra taxonomy manual semantic audit ilə təmizlənib. Xüsusən generic `branch`, `waiting` və çox geniş immersion pattern-ləri false positive yaratdığı üçün çıxarılıb və rəqəmlər yenidən hesablanıb.

Bu sənəd final full-dataset semantic classification deyil. Məqsəd root-cause strukturu formalaşdırmaq və sonrakı aspect classifier üçün daha düzgün taxonomy yaratmaqdır.

---

# 2. Onboarding və clarity

Parent candidate:

- **462 review**
- overall positive ratio: **87.45%**
- negative enrichment: **2.14×**

Bu, onboarding-in Hacknet üçün real risk sahəsi olduğunu göstərir, amma manual audit vacib bir paradoks ortaya çıxarır:

> Eyni onboarding sistemi bəzi oyunçular üçün çox əlçatan və intuitivdir, başqa bir qrup üçün isə həddindən artıq guided və game-specific görünür.

---

## 2.1. Tutorial / help

Candidate:

- **213 review**
- 181 positive
- 32 negative
- positive ratio: **84.98%**
- negative enrichment: **2.56×**

Positive nümunələrdə:

- tutorial aydın hesab olunur;
- mexanikalar mərhələli açılır;
- basic computer bilikləri ilə başlamaq mümkündür;
- command-line qorxusu azaldılır.

Negative nümunələrdə isə tutorial iki fərqli səbəbdən problemə çevrilir:

### Yeni başlayan üçün

Bəzi missiya objective-ləri və game-specific qaydalar kifayət qədər aydın deyil.

### Texniki istifadəçi üçün

Oyun real terminal məntiqinə bənzədiyi üçün istifadəçi artıq bildiyi command davranışını gözləyir, amma Hacknet-in öz sadələşdirilmiş qaydaları fərqlənir.

Bu zaman tutorial sadəcə “azdır” problemi deyil.

Problem:

> oyunçu hansı biliklərinin transfer olunduğunu, hansılarının isə oyunun fictional rule-u ilə əvəz edildiyini dəqiq anlamır.

---

## 2.2. Unclear instructions

Candidate:

- **173 review**
- 27 negative
- positive ratio: **84.39%**
- negative enrichment: **2.66×**

Manual sample-larda görünən problemlər:

- missiya üçün “file-i oxumaq, göndərmək, password-u göndərmək” arasında hansı action-ın tələb olunduğu aydın deyil;
- real-world logic ilə oyun logic-i arasında fərq görünmür;
- oyunçu düzgün nəticəyə başqa yolla çatsa belə mission trigger yalnız developer-in gözlədiyi action-a reaksiya verir.

Bu, onboarding-dən daha geniş problemə işarə edir:

> **Instruction clarity ilə system flexibility birlikdə dizayn edilməlidir.**

Əgər oyun bir neçə məntiqli həllə imkan vermirsə, objective çox dəqiq olmalıdır.

Əgər objective daha açıqdırsa, sistem bir neçə həll yolunu qəbul etməlidir.

---

## 2.3. Too much hand-holding

Candidate:

- **41 review**
- positive ratio: **90.24%**
- negative enrichment: **1.66×**

Bu geniş population problemi kimi görünmür.

Amma technical / puzzle-oriented audience üçün mühüm expectation mismatch-dir.

Bəzi oyunçular Hacknet-ə:

> “özüm experiment edib sistemi çözəcəyəm”

gözləntisi ilə gəlir.

Oyun isə bir çox yerdə:

> “növbəti command budur”

strukturu verir.

Bu halda həddindən artıq guidance repetition hissini də gücləndirə bilər.

### Design dərsi

Onboarding yalnız instruction vermək deyil.

Yaxşı onboarding oyunçunu:

```text
instruction
→ guided practice
→ partial autonomy
→ full autonomy
```

ardıcıllığı ilə buraxmalıdır.

---

## 2.4. Returning-player problemi

Dar candidate:

- **19 review**
- positive ratio: **89.47%**

Say az olduğuna görə prevalence nəticəsi çıxarmaq olmaz.

Amma əvvəlki community research və sample-lar ilə birlikdə problem real görünür:

- command-lar unudulur;
- tool-un rolu unudulur;
- story context itir;
- uzun fasilədən sonra restart daha rahat görünə bilər.

Bu janr üçün ayrıca design requirement kimi saxlanmalıdır:

> **Returning player recovery**

Mümkün sistemlər:

- searchable command palette;
- recent commands;
- contextual help;
- mission recap;
- evidence notebook;
- “last time you did…” summary.

---

# 3. Player agency

Refined parent candidate:

- **154 review**
- overall positive ratio: **83.77%**
- negative enrichment: **2.77×**

İlkin scan 224 candidate göstərirdi. Manual audit zamanı generic `branch` sözü XNA/software branch kimi false positive yaratdığı üçün çıxarıldı.

Bu düzəlişdən sonra signal daha kiçik, amma daha təmizdir.

---

## 3.1. Linearity

Candidate:

- **104 review**
- 18 negative
- positive ratio: **82.69%**
- negative enrichment: **2.95×**

Manual review-lərdə iki fərqli linearity var.

### Narrative linearity

- story əsasən bir istiqamətdə gedir;
- real branching məhduddur;
- choice hissi bəzi oyunçular üçün zəifdir.

### Mechanical linearity

Daha vacib problem budur:

> target üçün həll yolu əvvəlcədən müəyyən edilib və alternative approach azdır.

Bu, repetition ilə birbaşa əlaqəlidir.

Eyni target:

- credential reuse;
- social engineering;
- exploit;
- indirect host;
- stolen session;
- metadata clue

kimi fərqli həll yollarına imkan versə, mechanical agency yüksələr.

---

## 3.2. Choice və freedom

Dar candidate:

- **54 review**
- 8 negative
- positive ratio: **85.19%**
- negative enrichment: **2.52×**

Bu signal göstərir ki, choice mövzusu negative review-lərdə ümumi bazadan daha çox görünür.

Amma hazırkı evidence əsasında:

> “oyunçular branching story istəyir”

nəticəsini vermək olmaz.

Manual review-lərdə daha güclü complaint çox vaxt:

> “mən düzgün məntiqi həll tapmışam, amma oyun yalnız bir scripted action-ı qəbul edir”

tipindədir.

### Əsas nəticə

Bizim gələcək oyun üçün **mechanical agency** narrative choice-dan daha prioritet araşdırılmalıdır.

---

# 4. World reactivity

Parent candidate yalnız:

- **48 review**
- positive ratio: **79.17%**
- negative enrichment: **3.55×**

Bu theme yüksək precision, aşağı recall xarakterlidir.

Yəni mention sayı azdır, amma complaint-lər ciddi görünür.

---

## 4.1. Log consequence

Candidate:

- **22 review**
- positive ratio: **81.82%**
- negative enrichment: **3.10×**

Hacknet oyunçuya log silməyi öyrədir.

Bu mechanic-in fantasy mesajı:

> “iz buraxsan tutulacaqsan.”

Amma bəzi oyunçular sonradan anlayır ki, log silməməyin consequence-i gözlənildiyi qədər güclü deyil.

Bu çox vacib immersion qaydasıdır:

> **Oyun bir sistemin vacib olduğunu deyirsə, həmin sistem həqiqətən vacib olmalıdır.**

Əks halda oyunçu mechanic-in dekorativ olduğunu hiss edir.

---

## 4.2. Urgency

Candidate:

- **13 review**
- positive ratio: **76.92%**
- negative enrichment: **3.93×**

Say çox azdır.

Amma manual nümunələrdə “trace”, “security”, “hacker world” kimi elementlərin verdiyi təhlükə vədinə baxmayaraq dünya bəzən statik hiss olunur.

### Design opportunity

Urgency yalnız timer ilə yaradılmamalıdır.

Daha sistemik urgency:

- exploit bağlanır;
- target password dəyişir;
- NPC sistemi offline edir;
- başqa hacker target-ə çatır;
- stolen credential revoke olunur;
- investigation target-i davranışını dəyişir.

Bu, fake pressure-dan daha güclü reactivity yarada bilər.

---

## 4.3. World feels alive / consequences

Candidate:

- **34 review**
- 8 negative
- positive ratio: **76.47%**
- negative enrichment: **4.01×**

Bu azsaylı, amma yüksək-riskli signal-dır.

Manual review-lərdən gələn complaint:

- dünya oyunçunun fəaliyyətinə az reaksiya verir;
- server-lər “content container” kimi hiss oluna bilir;
- NPC və target-lərin müstəqil fəaliyyəti zəifdir.

Bu, yeni oyun üçün böyük opportunity-dir:

> **Computer-interface game-in arxasında yaşayan dünya hissi yaratmaq.**

---

# 5. UI və terminal ergonomics

Broad `UI_USABILITY`:

- **535 review**
- positive ratio: **91.21%**
- negative enrichment: **1.50×**

Bu theme həm praise, həm complaint daşıdığı üçün broad rəqəm özü çox şey demir.

Manual audit daha vacib iki layer göstərir.

---

## 5.1. UI fantasy və presentation

Positive review-lərdə:

- terminal görünüşü;
- command typing;
- pseudo-graphical UI;
- network map;
- minimal “traditional game UI”

çox vaxt immersion-ın əsas hissəsi kimi təriflənir.

Yəni Hacknet-də UI:

> sadəcə usability layer deyil, **fantasy delivery system**-dir.

Bu bizim janr üçün fundamental prinsipdir.

---

## 5.2. Terminal ergonomics

Daha dar candidate:

- **83 review**
- 15 negative
- positive ratio: **81.93%**
- negative enrichment: **3.08×**

Manual complaint-lər:

- terminal scroll yoxdur;
- autocomplete davranışı gözlənilən deyil;
- GUI cluttered/unintuitive ola bilir;
- file management məhduddur;
- real shell istifadəçisi öz vərdişlərini transfer etməyə çalışanda friction yaranır.

### Əsas paradoks

Interface nə qədər real terminala oxşayırsa:

> istifadəçi ondan bir o qədər real terminal davranışı gözləyir.

Deməli visual authenticity özü interaction contract yaradır.

### Yeni oyun üçün nəticə

İki sağlam istiqamətdən biri seçilməlidir:

### A. Real-system inspired

Familiar command behavior mümkün qədər gözlənilən kimi işləyir.

və ya

### B. Açıq fictional OS

Interface real shell-dən ilhamlanır, amma öz qaydalarını açıq və consistent qurur.

Ən riskli variant:

> görünüş real shell kimidir, davranış isə səbəbsiz fərqlidir.

---

# 6. Pacing

Taxonomy audit-dən əvvəl broad candidate:

**311**

idi.

False positive-lər çıxarılandan sonra refined candidate:

- **46 review**
- 6 negative
- positive ratio: **86.96%**
- negative enrichment: **2.22×**

Bu çox vacib metodoloji düzəlişdir.

Əvvəl generic:

- `waiting`
- `slow`

kimi sözlər:

> “can't wait to play”

kimi positive cümlələri də pacing problemi saya bilirdi.

Taxonomy təmizlənəndə böyük hissə yox oldu.

### Nəticə

> Pacing Hacknet üçün ayrıca ən böyük failure mode kimi görünmür.

Daha doğru model:

> forced waiting çox vaxt **repetition problemindən doğan ikinci dərəcəli friction**-dır.

Oyunçu hələ qərar verirsə timer tension yarada bilər.

Oyunçu artıq doğru sequence-ni bilirsə eyni timer waiting-ə çevrilir.

---

# 7. Risklər arasında əlaqə

Bu audit göstərir ki, bir neçə complaint əslində eyni kök sistemdən çıxır.

```text
single intended solution
        ↓
low mechanical agency
        ↓
same command sequence
        ↓
repetition
        ↓
known outcome
        ↓
waiting becomes friction
```

Başqa əlaqə:

```text
real-looking terminal
        ↓
real-system expectation
        ↓
game-specific behavior
        ↓
confusion / UI friction
        ↓
technical audience dissatisfaction
```

Başqa əlaqə:

```text
game teaches logs / trace matter
        ↓
weak consequence
        ↓
system feels decorative
        ↓
world reactivity drops
        ↓
immersion weakens
```

Bu əlaqələr feature-by-feature analysis-dən daha vacibdir.

---

# 8. Yeni oyun üçün çıxan design prinsipləri

## Prinsip 1 — Tutorial autonomy-yə keçməlidir

Tutorial-un məqsədi oyunçunu bütün oyun boyu guided saxlamaq deyil.

Məqsəd:

> minimum vocabulary-ni öyrədib oyunçunu öz reasoning-i ilə buraxmaqdır.

---

## Prinsip 2 — Objective və accepted solution uyğun olmalıdır

Əgər sistem yalnız bir həll qəbul edirsə, objective dəqiq olmalıdır.

Əgər objective açıqdırsa, sistem bir neçə məntiqli həlli qəbul etməlidir.

---

## Prinsip 3 — Mechanical agency narrative agency-dən ayrıca ölçülməlidir

Branching story olması gameplay freedom demək deyil.

Yeni concept evaluation zamanı ayrıca soruşulmalıdır:

> Eyni problemi neçə meaningful üsulla həll etmək olar?

---

## Prinsip 4 — Taught mechanic real consequence yaratmalıdır

Oyunçuya:

- log silmək;
- trace-dən qorunmaq;
- identity gizlətmək;
- permission idarə etmək

öyrədilirsə, bu sistemlər real decision yaratmalıdır.

Dekorativ complexity əlavə etmək olmaz.

---

## Prinsip 5 — UI-nin görünüşü interaction vədi yaradır

Real-looking terminal:

> “real terminal vərdişlərim burada qismən işləyəcək”

gözləntisi yaradır.

Bu expectation ya qarşılanmalı, ya da fictional OS dili əvvəlcədən aydınlaşdırılmalıdır.

---

## Prinsip 6 — Waiting yalnız uncertainty varsa faydalıdır

Timer və progress animation:

- risk varsa → tension;
- seçim varsa → planning window;
- nəticə məlumdursa → friction.

---

## Prinsip 7 — Returning player ayrıca persona deyil, lifecycle state-dir

Oyunçu eyni adamdır, sadəcə 2 həftə fasilədən sonra onun knowledge state-i dəyişib.

Interface-game-lərdə bu state üçün recovery UX əvvəlcədən planlaşdırılmalıdır.

---

# 9. Confidence

## High confidence

- Onboarding/clarity negative reviews-də bazadan daha çox görünür.
- Linearity/mechanical agency problemi repetition ilə əlaqəlidir.
- Terminal ergonomics technical audience üçün real friction yaradır.
- Broad pacing regex-in ilkin nəticəsi şişirdilmişdi; refined pacing daha kiçik riskdir.

## Medium confidence

- Weak world reactivity immersion-ı azaldır.
- Mechanical agency narrative choice-dan daha vacib opportunity-dir.
- Objective ambiguity ilə single-solution mission design birlikdə frustration yaradır.

## Low / further validation needed

- Returning-player probleminin prevalence-i.
- World reactivity-nin bütün audience üçün nə qədər vacib olması.
- Agency complaint-lərinin hansı faizi story, hansı faizi gameplay approach haqqındadır.

---

# 10. Növbəti audit

Risk side artıq kifayət qədər strukturlanıb.

Növbəti mərhələ value-driver semantic audit olmalıdır:

1. `HACKER_FANTASY`
2. `STORY_NARRATIVE`
3. `IMMERSION`
4. `SOUND_AUDIO`
5. `INVESTIGATION_DISCOVERY`
6. `MOD_REPLAYABILITY`
7. `EDUCATIONAL_IMPACT`

Əsas sual dəyişir:

> “Nə problem yaradır?”

sualından:

> **“Oyunçu Hacknet-dən konkret hansı dəyəri alır və bu dəyər hansı dizayn mexanizmi ilə yaranır?”**

sualına keçirik.
