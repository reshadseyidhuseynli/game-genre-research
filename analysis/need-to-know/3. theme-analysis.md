# Need to Know — Mövzu analizi

## 1. Məqsəd

Bu sənəd **Need to Know** üçün Steam rəy məlumat toplusu, deterministik mövzu namizədləri və məna yönümlü audit nəticələrini birləşdirir.

Need to Know Tier B müqayisə oyunudur. Əsas sual:

> **Orwell ilə oxşar müşahidə və məlumat-güc premise-i qurmasına baxmayaraq, Need to Know niyə daha zəif oyunçu reaksiyası alır və hansı dizayn fərqləri bunu izah edə bilər?**

Bu sənəddə üç qat ayrı saxlanılır:

1. **məlumat toplusu faktı** — Steam API məlumatından gəlir;
2. **xarici mənbə faktı** — mağaza, yaradıcı müsahibəsi və rəsmi saytdan gəlir;
3. **analitik nəticə / hipotez** — yuxarıdakı dəlillərin şərhidir.

---

## 2. Məlumat toplusu

Mənbə:

- Steam App ID: `490930`
- oyun açarı: `need-to-know`
- toplanma tarixi: 2026-10-02
- ingilisdilli rəy: **272**
- müsbət: **178**
- mənfi: **94**
- müsbət payı: **65.44%**
- median oyun müddəti: **7.99 saat**
- orta oyun müddəti: **12.64 saat**
- müsbət rəylərdə orta oyun müddəti: **15.13 saat**
- mənfi rəylərdə orta oyun müddəti: **7.92 saat**

Oyun müddəti qrupları:

| Oyun müddəti | Rəy sayı | Müsbət payı |
|---|---:|---:|
| 0–1 saat | 28 | **21.43%** |
| 1–3 saat | 45 | **48.89%** |
| 3–10 saat | 87 | **71.26%** |
| 10+ saat | 112 | **78.57%** |

Bu artım səbəb-nəticə kimi yozulmamalıdır. “Daha çox oynamaq oyunu sevdirdi” nəticəsi çıxmır; oyunu bəyənənlərin daha uzun qalması və narazı oyunçuların erkən çıxması da mümkündür.

Steam mağaza səhifəsi hazırda ayrıca **175 rəy / 74% müsbət** göstərir. Bu mağaza göstəricisi ilə API məlumat toplusu eyni filtr səthi deyil; buna görə bir-birinə qarışdırılmır və dəqiq fərqin səbəbi əlavə filtr-paritet yoxlaması olmadan təxmin edilmir.

---

## 3. Yoxlama vəziyyəti

Repo-dakı snapshot struktur baxımından ardıcıldır:

- manifest `completed: true`;
- termination: `empty_page`;
- 4 arxivlənmiş API səhifəsi;
- 272 raw rəy;
- 272 unique processed rəy;
- 0 duplicate;
- summary/statistics/processing artefaktları mövcuddur.

Tam reproducibility üçün lokalda:

```bash
python -m src.verify --game need-to-know
python -m src.theme_pipeline --game need-to-know
```

işlədilməli və generasiya olunan `data/processed/need-to-know/themes/` və `data/reports/need-to-know/theme-candidates.md` faylları push edilməlidir.

---

## 4. Audit metodu

### Mənfi rəylər

**94 mənfi rəyin hamısı** məna baxımından oxunub.

Bu vacibdir, çünki kiçik məlumat toplusunda əsas zəiflikləri yalnız regex namizədlərindən çıxarmaq risklidir.

### Müsbət rəylər

178 müsbət rəydən **34 fərqli rəy** məqsədli seçilib:

- ən faydalı rəylər;
- ən yeni rəylər;
- ən yüksək oyun müddətli rəylər.

Məqsəd yalnız “nə pisdir?” yox, “kim üçün və niyə işləyir?” sualını da cavablandırmaqdır.

### Deterministik mövzu namizədləri

Repo-dakı `config/theme_taxonomy.yaml` v5 qaydaları əsasında full-corpus scan yenidən hesablanıb.

Namizəd coverage:

- ən azı bir mövzuya düşən rəy: **211 / 272**
- coverage: **77.6%**

Bu göstəricilər **aspect sentiment deyil**. Məsələn bir rəy hekayəni tərifləyib UI-ni tənqid edə bilər; ümumi Steam recommendation həmin iki aspektin sentiment-i kimi qəbul edilmir.

---

## 5. Deterministik mövzu siqnalları

Ümumi mənfi baseline: **34.56%**.

| Mövzu | Mention | Mənfi | Mənfi payı | Baseline-a nisbət |
|---|---:|---:|---:|---:|
| STORY_NARRATIVE | 111 | 31 | 27.9% | 0.81× |
| ONBOARDING_CLARITY | 64 | 36 | **56.3%** | **1.63×** |
| UI_USABILITY | 59 | 29 | **49.2%** | **1.42×** |
| PUZZLE_CLARITY | 55 | 26 | **47.3%** | **1.37×** |
| BUGS_COMPATIBILITY | 48 | 23 | **47.9%** | **1.39×** |
| CLUE_EVIDENCE_QUALITY | 35 | 15 | 42.9% | 1.24× |
| REPETITION | 33 | 14 | 42.4% | 1.23× |
| PRIVACY_SURVEILLANCE | 31 | 6 | **19.4%** | **0.56×** |
| DEDUCTION_REASONING | 22 | 13 | **59.1%** | **1.71×** |
| PLAYER_AGENCY | 21 | 9 | 42.9% | 1.24× |
| MORAL_AMBIGUITY | 17 | 3 | **17.6%** | **0.51×** |
| LINEARITY_SCRIPTING | 14 | 6 | 42.9% | 1.24× |

Ən çox birlikdə görünən namizəd cütləri:

- `ONBOARDING_CLARITY + PUZZLE_CLARITY` — 44
- `STORY_NARRATIVE + UI_USABILITY` — 34
- `ONBOARDING_CLARITY + STORY_NARRATIVE` — 28
- `ONBOARDING_CLARITY + UI_USABILITY` — 26
- `BUGS_COMPATIBILITY + UI_USABILITY` — 22

Bu, xüsusən erkən sessiyada problemin “oyun çətindir”dən çox **qaydanı, aləti və interfeysi başa düşmək çətindir** formasında olduğunu göstərir.

---

## 6. Əsas güc: premise və mövzu işləyir

`PRIVACY_SURVEILLANCE` və `MORAL_AMBIGUITY` namizədləri baseline-dan xeyli aşağı mənfi konsentrasiyaya malikdir.

Müsbət rəylərdə təkrarlanan səbəblər:

- dövlət müşahidəsi mövzusunun maraqlı olması;
- adi insanların şəxsi məlumatlarını oxumağın narahatedici, amma cəlbedici hiss yaratması;
- clearance artdıqca daha güclü müşahidə alətlərinin açılması;
- sistemin tədricən avtoritarlaşmasını izləmək;
- hekayənin sadə “dövlət pisdir” mesajından daha mürəkkəb görünməsi;
- bəzi hədəflərin həqiqətən təhlükəli, bəzilərinin isə sistemin qurbanı olması;
- şəxsi profillərin oxunması və insan haqqında şəkil qurmaq;
- atmosfer, vizual üslub və musiqi.

### Analitik nəticə

> **Need to Know-un əsas problemi mövzu seçimi deyil. Müşahidə, güc və mənəvi qeyri-müəyyənlik oyunçu marağı yaradır.**

**Etibarlılıq: High**

---

## 7. Ən böyük erkən-session problemi: ilkin öyrətmə + UI

0–1 saat müsbət payının **21.43%** olması məlumat toplusundakı ən sərt siqnaldır.

Bütün mənfi rəylərin auditində erkən çıxış səbəbləri təkrarən bunlardır:

- alətlərin nə etdiyinin aydın olmaması;
- missiyanın necə başladılacağının anlaşılmaması;
- “safe”, “match”, “threat” kimi vəziyyətlərin zəif izahı;
- tutorial mətninin qaçırılması və geri açıla bilməməsi;
- vizual olaraq düyməyə bənzəməyən interaktiv elementlər;
- üst-üstə düşən pəncərələr;
- hərəkət edən xəritə;
- yavaş animasiyalar və keçidlər;
- launch dövründə crash/soft-lock/save problemləri.

Ən vacib fərq:

> **Oyunçu səhv qərar verdiyi üçün yox, sistemin ondan nə istədiyini anlamadığı üçün uğursuz ola bilir.**

Bu, ustalaşma hissi yaratmır.

**Etibarlılıq: High**

---

## 8. Dəlil qaydaları: “düşünmək” əvəzinə “sistemin exact cavabını tapmaq”

Mənfi rəylərdə ən stabil struktur tənqidlərdən biri:

- qayda mətni ilə qəbul edilən dəlilin uyğun gəlməməsi;
- mənaca doğru məlumatın sistem tərəfindən qəbul edilməməsi;
- “düzgün” dəlilin hansı formal işarələmə yolu ilə verilməsinin qeyri-müəyyən olması;
- qismən doğru reasoning üçün zəif və ya sıfır credit;
- səhv üçün cəzanın doğru cavabın mükafatından daha ağır hiss olunması;
- bəzən typo-nun puzzle məlumatına qarışması.

Bu səbəbdən bəzi oyunçular işi:

> insan haqqında nəticə çıxarmaq

kimi yox,

> əvvəlcədən müəyyən edilmiş keyword / rule match tapmaq

kimi qəbul edir.

### Analitik nəticə

> **Dəlil sistemində semantic correctness ilə system-accepted correctness arasındakı boşluq, araşdırma rol hissini yoxlama siyahısı işinə çevirir.**

**Etibarlılıq: High**

---

## 9. Əsas vəd-gərginliyi: “mənəvi seçim” vs məcburi yol

Rəsmi məhsul dili oyunçuya:

- məxfiliyi müdafiə etmək;
- Department-a xidmət etmək;
- underground qruplara məlumat sızdırmaq;
- məlumatı şəxsi qazanc üçün istifadə etmək

kimi geniş rol seçimi təqdim edir.

Rəsmi sayt həm də “meaningful moral choices” və “significant in-game consequences” vəd edir.

Mənfi rəylərdə, xüsusən uzun oynayanlarda isə təkrarlanan şikayət:

- müəyyən tərəflə işləməkdən imtina → game over;
- əlaqəni saxlamamaq → game over;
- dialoqda “yox” demək → sistemin yenə həmin əlaqəni yaratması;
- bir neçə seçimdən yalnız biri progression-a imkan verməsi;
- hekayənin oyunçunun mövqeyinə uyğunlaşmaq əvəzinə oyunçunu tələb olunan yola qaytarması.

Bu tənqid yalnız launch rəylərində deyil; sonrakı illərin rəylərində də görünür.

### Əsas fərq

> **Failure branch seçim deyil. Əgər bir seçim yalnız “davam et”, digəri “geri qayıdıb düzgün seçimi et” yaradırsa, oyunçu bunu qərar sərbəstliyi kimi hiss etməyə bilər.**

**Etibarlılıq: High**

---

## 10. Təkrarçılıq və uzunluq

Müsbət rəylərin bir hissəsi uzun oyun müddətini dəyər kimi görür.

Amma həm müsbət, həm mənfi uzun-session rəylərində:

- eyni məlumat-matching işinin çox təkrarlanması;
- yeni clearance səviyyələrinin gec açılması;
- home/data-selling hissələrinin filler kimi hiss olunması;
- çox sayda oxşar missiyanın hekayə beat-ləri arasını uzatması

təkrarlanır.

Rəsmi sayt “zero grinding” deyir; bəzi oyunçular isə təcrübəni məhz “grind”, “chore”, “busy work” kimi təsvir edir.

`REPETITION` namizədlərində orta oyun müddəti təxminən **18.9 saatdır**. Bu, təkrarçılığın yalnız refund pəncərəsindəki ilk təəssürat olmadığını göstərir.

### Analitik hipotez

> **Problem yalnız təkrarlanan klik deyil; eyni qərar qrammatikası çox uzun müddət dəyişmədən qalır.**

**Etibarlılıq: High**

---

## 11. Texniki problemləri zaman kontekstindən ayırmaq

Launch rəylərində:

- crash;
- soft-lock;
- save corruption;
- təkrarlanan intro;
- yoxa çıxan notification;
- resolution;
- klik və pəncərə davranışı

çox güclü görünür.

Amma bunu avtomatik “oyunun indiki vəziyyəti” kimi qəbul etmək düzgün deyil.

Dəlil:

- bəzi 2018–2021 müsbət rəylər post-launch patch-lərin tutorial və bug-ları yaxşılaşdırdığını deyir;
- ən faydalı launch mənfi rəylərindən biri sonradan developer-in dəyişiklik etdiyini və original rəyin current version-u tam əks etdirmədiyini açıq qeyd edir;
- bununla yanaşı, daha yeni rəylərdə də UI glitch, soft-lock və progression problemi nümunələri qalır.

### Nəticə

Texniki problemlər üçün ən düzgün model:

- **launch severity: yüksək**
- **sonrakı patch-lərlə yaxşılaşma: dəlilli**
- **tam yox olma: dəlillə təsdiqlənmir**

**Etibarlılıq: Medium-High**

---

## 12. Hekayə niyə əsas oyunda qalma amili kimi görünür?

`STORY_NARRATIVE`:

- 111 mention;
- 27.9% mənfi;
- baseline-dan aşağı.

Uzun müsbət rəylərdə ən güclü təriflər:

- siyasi thriller hissi;
- personajlar;
- clearance yüksəldikcə sistemin dəyişməsi;
- dövlətin həm real təhlükələri dayandırması, həm də gücü sui-istifadə edə bilməsi;
- oyunçunun öz xarakterinin daha kompromisli hala gəlməsi;
- dünya quruculuğu.

Hətta mənfi rəylərin bir qismi oyun gedişindən yorulduğunu, amma hekayəni görmək üçün davam etdiyini bildirir.

### Analitik nəticə

> **Need to Know-da hekayə zəif əsas oyun dövrünü müəyyən müddət daşıya bilir, amma onu tam kompensasiya etmir.**

**Etibarlılıq: High**

---

## 13. Yaradıcı məqsədi vs oyunçu nəticəsi

Yaradıcı müsahibələrində əsas məqsəd:

- oyunçunu “izlənən” yox, “izləyən” etmək;
- güc verərək right/wrong sərhədini bulanıqlaşdırmaq;
- şəxsi məlumatı pozmağın oyunçunun öz hərəkəti kimi emosional ağırlıq yaratması;
- karyera, pul və statusun mənəvi kompromislə rəqabət etməsi;
- müşahidə debatında birtərəfli mövqe tutmamaq.

Bu niyyətin bir hissəsi işləyir:

- premise güclüdür;
- surveillance və moral ambiguity müsbət siqnal verir;
- hekayə və dünya quruculuğu dəyərlidir.

Əsas uyğunsuzluq:

> **oyun oyunçuya mənəvi mövqe seçdirdiyini deyir, amma bəzi kritik sistemlər həmin mövqelərdən yalnız bir neçəsini progression-compatible edir.**

Bu, sadəcə “az branch” problemi deyil.

Bu, **məhsul vədi ↔ sistem davranışı** uyğunsuzluğudur.

---

## 14. Bizim layihə üçün dərslər

1. **Geniş seçim vədi verməkdənsə az, amma real davam edən seçim ver.**
2. **Oyunçu semantik olaraq doğru nəticə çıxarıbsa, UI ritualını səhv etdiyi üçün tam cəzalandırma.**
3. **İlkin öyrətmə yalnız düymələri yox, “niyə bu cavab doğrudur?” modelini öyrətməlidir.**
4. **Məlumatla işləyən oyunda UI oyunçunun iş yaddaşıdır; pəncərə idarəsi özü düşmənə çevrilməməlidir.**
5. **Dövlət/bürokratiya işi qəsdən monoton ola bilər, amma monotonluqla darıxdırıcılığı qarışdırma.**
6. **Mənəvi qeyri-müəyyənlik üçün hər iki tərəfin davam edən nəticəsi olmalıdır.**
7. **Game over “səhv mənəvi mövqe seçdin” əvəzi kimi istifadə olunmamalıdır.**
8. **Yeni güclər yalnız feature açmamalı, qərar qrammatikasını dəyişməlidir.**
9. **Qərar nəticəsi görünən, məntiqi və oyunçunun niyyəti ilə əlaqəli olmalıdır.**
10. **Launch texniki borcu ilə fundamental dizayn problemini eyni səbəb kimi təqdim etmə.**

---

## 15. Mənbələr

### Repo məlumatları

- `data/reports/need-to-know/summary.md`
- `data/processed/need-to-know/statistics.json`
- `data/processed/need-to-know/reviews.jsonl`
- `data/raw/need-to-know/reviews_manifest.json`
- `config/theme_taxonomy.yaml`

### Xarici mənbələr

- Steam Store — https://store.steampowered.com/app/490930/
- Need to Know official site — https://needtoknowgame.com/
- Kickstarter — https://www.kickstarter.com/projects/monomythgames/need-to-know-the-mass-surveillance-thriller-game
- Adelaide Review creator interview — https://www.adelaidereview.com.au/latest/opinion/2016/05/10/adelaide-game-developers-find-global-audience-need-to-know/

## Status

**Məna yönümlü audit:** tamamlanıb  
**Deterministik scan:** v5 taxonomy ilə hesablanıb, rəsmi pipeline artefaktlarının lokal generasiyası/push-u gözlənilir  
**Növbəti:** `deep-research.md` və Orwell müqayisəsi
