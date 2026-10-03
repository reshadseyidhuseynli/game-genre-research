# RESEARCH_MASTER_BRIEF.md

## 0. Bu sənəd nə üçündür?

Bu sənəd **Oyun Janrı Araşdırması** layihəsinin əsas kontekst və davamlılıq sənədidir.

Əgər əvvəlki ChatGPT söhbətinin konteksti itərsə, yeni chat açılsa və ya layihəni başqa bir AI və ya şəxs davam etdirsə, əvvəlcə bu fayl oxunmalıdır. Bu sənəd layihənin:

- məqsədini;
- araşdırma suallarını;
- əhatə dairəsini;
- istifadə edilən metodologiyanı;
- məlumat və dəlil qaydalarını;
- hər oyun üçün görüləcək işi;
- oyunlararası müqayisə üsulunu;
- yekun təqdimat sənədlərini;
- yekun hesabat strukturunu;
- cari vəziyyəti və növbəti addımı

müəyyən edir.

Bu layihənin məqsədi **indidən oyun ideyası seçmək deyil**. Məqsəd ideya yaratmazdan və dəqiqləşdirməzdən əvvəl bazarda mövcud olan oxşar oyunları sistemli şəkildə öyrənmək, işləyən və işləməyən nümunələri tapmaq və sonrakı konsept qərarlarını dəlil ilə dəstəkləməkdir.

---

## Dil standartı — məcburi qayda

Bütün araşdırma sənədlərinin əsas dili **Azərbaycan dili** olmalıdır.

Qaydalar:

- İzah mətni, başlıqlar, cədvəl sütunları və nəticələr Azərbaycan dilində yazılır.
- İngilis termini yalnız Azərbaycan dilində dəqiq və qısa qarşılığı olmadıqda və ya sənaye standartı kimi tanınması vacib olduqda saxlanılır.
- Belə termin ilk istifadədə Azərbaycan dilində izah edilir. Məsələn: `RNG (təsadüfi nəticə mexanizmi)`.
- Maşın tərəfindən istifadə edilən etiketlər, məsələn `RNG_FAIRNESS`, `LINEARITY_SCRIPTING`, `HACKER_FANTASY`, dəyişdirilmir; onların insan üçün izahı Azərbaycan dilində verilir.
- `player`, `review`, `story`, `core loop`, `depth`, `failure`, `evidence`, `onboarding`, `retention`, `driver`, `trade-off`, `opportunity` kimi ümumi sözlər izah mətnində İngilis dilində saxlanmamalıdır.
- Kod, fayl yolu, Steam etiketi, oyun adı, sitat və rəsmi məhsul ifadələri olduğu kimi qala bilər.
- Məqsəd süni tərcümə yox, rahat oxunan peşəkar Azərbaycan dilidir.

Bu qayda əvvəlki və gələcək bütün `analysis/` sənədlərinə tətbiq edilir.

# 1. Yeni sessiyada konteksti necə bərpa etmək lazımdır?

Yeni AI sessiyası və ya layihəni davam etdirən şəxs bu ardıcıllıqla başlamalıdır:

1. **Bu faylı tam oxu:** `RESEARCH_MASTER_BRIEF.md`
2. **məlumat pipeline qaydalarını oxu:** `AGENTS.md`
3. **Repo-nun texniki istifadəsini oxu:** `README.md`
4. `analysis/` qovluğunda hazır olan araşdırmaları yoxla.
5. `data/reports/` və `data/processed/` altında hansı oyunların datasının hazır olduğunu yoxla.
6. Bu sənədin sonundakı **Cari vəziyyət** bölməsini oxu.
7. Hazır milestone tamamlanmadan özbaşına yeni oyun və ya yeni araşdırma istiqamətinə keçmə.

## Oyun üzrə `analysis/<game>/` qovluğu üçün məcburi standart

Tamamlanmış hər tam araşdırma oyun qovluğunda **yalnız bu 4 fayl** saxlanmalıdır:

```text
analysis/<game>/
├── 4. research-kickoff.md
├── 3. theme-analysis.md
├── 2. deep-research.md
└── 1. presentation-brief.md
```

Rollar:

- `4. research-kickoff.md` — məlumat toplanmazdan əvvəl məqsəd, əsas suallar və ilkin fərziyyələr;
- `3. theme-analysis.md` — rəy məlumatları, mövzu statistikası və məna yönümlü yoxlamanın detallı dəlil qatı;
- `2. deep-research.md` — əsas yekun, ətraflı oyun hesabatı;
- `1. presentation-brief.md` — görüşlərdə 2–5 dəqiqəyə oyunu izah etmək üçün qısa, amma dolu təqdimat xülasəsi.

Araşdırma zamanı yaradılan aralıq yoxlama, korpus qeydləri və sınaq faylları son nəticələr bu dörd sənədə inteqrasiya edildikdən sonra `analysis/<game>/` qovluğunda saxlanmamalıdır. Lazım gəlsə onların tarixçəsi Git-də qalır.

Tövsiyə edilən oxu ardıcıllığı:
1. sürətli məlumat üçün `1. presentation-brief.md`;
2. ətraflı nəticə üçün `2. deep-research.md`;
3. rəqəmləri və rəy dəlillərini yoxlamaq üçün `3. theme-analysis.md`;
4. ilkin fərziyyələri görmək üçün `4. research-kickoff.md`.

Bütün repo üzrə daha ətraflı oxu bələdçisi: `analysis/README.md`.

Bu qaydanın məqsədi bütün oyunlarda eyni naviqasiya, sənəd strukturu və təqdimat formatı saxlamaqdır.

Sənədlərin rolu:

| Fayl / qovluq | Rolu |
|---|---|
| `RESEARCH_MASTER_BRIEF.md` | Layihənin məqsədi, metodologiyası, deliverable standartı və cari araşdırma istiqaməti |
| `AGENTS.md` | Kod, məlumat collection, reproducibility və pipeline qaydaları |
| `README.md` | Texniki setup və command-lar |
| `analysis/README.md` | Hesabatların rolu və tövsiyə edilən oxuma ardıcıllığı |
| `data/raw/<game>/` | Mənbədən gələn dəyişdirilməmiş xam məlumat |
| `data/processed/<game>/` | Təmizlənmiş və təhlil-ready məlumat |
| `data/reports/<game>/summary.md` | Avtomatik, deterministik statistik xülasə; interpretasiya etmir |
| `analysis/<game>/1. presentation-brief.md` | 2–5 dəqiqəlik yığcam oyun təqdimatı |
| `analysis/<game>/2. deep-research.md` | Həmin oyun üzrə keyfiyyət və kəmiyyət məlumatlarını birləşdirən ətraflı yekun araşdırma |
| `analysis/comparisons/` | Oxşar oyunların birbaşa müqayisəsi |
| `analysis/final/` | Yekun qərar sənədləri |

Əgər sənədlər arasında araşdırma məqsədi baxımından uyğunsuzluq varsa, bu master brief əsas götürülür. Kod/məlumat integrity məsələlərində isə `AGENTS.md` qaydaları qorunmalıdır.

---

# 2. Layihənin əsas məqsədi

Araşdırdığımız sahə geniş mənada belədir:

> **Computer-interface / uydurma əməliyyat sistemi / terminal / hacking / digital araşdırma / surveillance / found-device tipli oyunlar.**

Bu oyunlarda əsas oyun gedişi klassik 3D dünya və ya action sistemi deyil. Oyunçu əsasən:

- terminal;
- fictional desktop/OS;
- browser;
- email;
- chat;
- phone;
- database;
- file system;
- social network;
- surveillance alətlər;
- network map;
- log və digər rəqəmsal interfeyslər

vasitəsilə oynayır.

Hazırkı əsas reference istiqamətlərimiz **Hacknet** və **Cyber Manhunt** tipli oyunlardır.

Pure programming puzzle oyunları — məsələn yalnız kod yazmaq və ya elektronika/programlaşdırma tapmacası üzərində qurulan oyunlar — bu araşdırmanın əsas əhatə dairəsi-u deyil.

---

# 3. Biz hansı qərara hazırlaşırıq?

Bu araşdırmanın sonunda yeni oyun ideyaları yaradılmalı və ya mövcud ideyalar dəqiqləşdirilməlidir.

Yəni araşdırmanın əsas biznes/məhsul sualı belədir:

> **Bu geniş janrda hansı oyunçu rol hissi-si, oyun gedişi loop-u, UI modeli, narrative delivery üsulu və sistem dərinliyi işləyir; hansı yanaşmalar təkrarçılıq, confusion, dayaz oyun gedişi, yanlış expectation və zəif bazar response yaradır; hansı imkanlar daha ağıllı şəkildə hədəflənə bilər?**

Araşdırmanın məqsədi “filan oyunu kopyalayaq” nəticəsinə gəlmək deyil.

Məqsəd:

1. bazarda artıq sınanmış yanaşmaları anlamaq;
2. təkrarlanan uğur nümunələrini tapmaq;
3. təkrarlanan uğursuzluq nümunəsi-lərini tapmaq;
4. oyunçu expectation-ları anlamaq;
5. underserved / zəif həll olunmuş ehtiyacları tapmaq;
6. yeni concept üçün dizayn constraint və imkan-lər yaratmaq;
7. ideyaların yalnız zövqlə deyil, dəlil ilə qiymətləndirilməsinə imkan verməkdir.

---

# 4. Əsas araşdırma sualları

Hər oyun və bütün janr üzrə aşağıdakı suallara cavab axtarılır.

## 4.1. Attraction / purchase

- Oyun bir cümlədə hansı rol hissini satır?
- İnsan niyə mağaza page-də buna maraq göstərir?
- Trailer, screenshot və description hansı vədi verir?
- Oyun hansı auditoriyanı cəlb edir?
- Hansı bazar təqdimat işləyir?
- “Real hacking”, “araşdırma”, “hekayə”, “simulation”, “horror” və s. expectation-ları necə formalaşdırır?

## 4.2. First-session experience

- İlk 5, 15, 30 və 60 dəqiqədə oyunçu nə edir?
- ilk əyləncəli ana qədər vaxt nə qədərdir?
- ilkin öyrətmə necə işləyir?
- İlk saatlarda niyə insanlar qalır və ya çıxır?
- UI və command sistemi qorxuducudur, yoxsa rol hissini gücləndirir?

## 4.3. əsas oyun dövrü

- Oyunçu hər 2–5 dəqiqədə nə edir?
- Bu loop neçə dəfə təkrar olunur?
- Loop hansı yollarla dəyişir və dərinləşir?
- alət-lar real seçim yaradır, yoxsa sadəcə doğru “açarı” seçməkdir?
- Oyunçu problem həll edir, yoxsa məlum sequence-ni təkrar edir?

## 4.4. oyunçunun rol hissi və oyuna dalma hissi

- Oyunçu özünü kim kimi hiss etməlidir?
- UI bu rol hissini necə yaradır?
- Audio, visual geribildirim, typing, network, files, messages və s. bu hissə necə xidmət edir?
- Realizm nə qədər lazımdır?
- “Kifayət qədər real” ilə “oynamaq üçün sadələşdirilmiş” arasındakı balans necə qurulub?

## 4.5. Information / araşdırma loop

- Məlumat necə tapılır?
- Oyunçu hansı məlumatın vacib olduğunu necə anlayır?
- Məlumatlar bir-biri ilə əlaqələndirilirmi?
- Oyunçu hipotez qururmu?
- Tapdığı məlumat sonrakı oyun gedişi-i dəyişirmi?
- kəşf özü reward-durmu?

## 4.6. Narrative

- hekayə necə təqdim olunur?
- Email, file, log, chat, voice, cutscene və s. hansı rolu oynayır?
- hekayə oyun gedişi-in içindədir, yoxsa oyun gedişi-dən ayrıdır?
- hekayə təkrarçılıq-ı gizlədir, yoxsa mexanika özü kifayət qədər güclüdür?
- Yadda qalan narrative/oyun gedişi momentləri hansılardır?

## 4.7. Progression və pacing

- Yeni alət, mexanika, permission, hekayə qat nə vaxt açılır?
- Oyun nə vaxt monotonlaşmağa başlayır?
- Difficulty necə artır?
- Progression real yeni qərar yaradır, yoxsa sadəcə daha çox eyni action verir?
- Oyun uzunluğu əsas oyun dövrü-a uyğundurmu?

## 4.8. nəticə və dünyanın reaksiyası

- Səhv qərarın real nəticəsi varmı?
- Dünya oyunçunun fəaliyyətinə reaksiya verirmi?
- Log silmək, trace, reputation, identity, hacking və s. sistemlər həqiqətən vacibdirmi?
- Oyunçunun qərarları yeni vəziyyət yaradırmı?

## 4.9. çətinlik və uğursuzluq

- Ən çox mənfi rəy yazdıran səbəblər hansılardır?
- təkrarçılıq harada yaranır?
- UI çətinlik varmı?
- Instructions qeyri-müəyyəndirmi?
- Realizm expectation-u pozulurmu?
- Bugs, crashes, softlock, save corruption və compatibility problemi varmı?
- fasilədən sonra qayıdan oyunçu oyuna qayıdanda nəyi unudur?

## 4.10. Long-term value

- təkrar oynama dəyəri varmı?
- Multiple path / finals varmı?
- mod dəstəyi varmı?
- icma məzmun ömrü uzadırmı?
- Sequel-də nələr dəyişib və nəticə yaxşılaşıb/pisləşibmi?

---

# 5. Araşdırmanın əsas prinsipi

Bir oyunun yüksək Steam rəy faizi onun bütün dizayn qərarlarının yaxşı olduğunu göstərmir.

Eyni şəkildə aşağı satış estimate-i oyunun pis olduğunu avtomatik sübut etmir.

Ona görə araşdırma aşağıdakı mənbə-ları **triangulate** etməlidir:

```text
market/performance data
+ Steam review dataset
+ qualitative player feedback
+ Reddit/community discussions
+ gameplay/walkthrough evidence
+ professional reviews
+ developer interviews/postmortems
+ store positioning
= daha etibarlı design/product nəticəsi
```

Heç bir mənbə təkbaşına final nəticə sayılmamalıdır.

---

# 6. dəlil səviyyələri

## Səviyyə A — birbaşa fakt

Məsələn:

- release date;
- qiymət;
- rəy sayı;
- Steam tövsiyəsi ratio;
- yaradıcı-in açıq dediyi məlumat;
- oyunda bir mexanika-in mövcud olması.

Bunlar mənbə ilə birbaşa göstərilə bilər.

## Səviyyə B — güclü nümunə

Məsələn:

- müxtəlif Steam rəy nümunə-larında təkrarçılıq şikayətinin təkrar görünməsi;
- Reddit və peşəkar rəylərdə eyni problemin qeyd olunması;
- oyun müddəti segmentlərində aydın fərqin görünməsi.

Bu artıq sadə anecdote deyil, amma yenə də səbəb-nəticə kimi təqdim edilməməlidir.

## Səviyyə C — interpretasiya / hipotez

Məsələn:

> “Hacknet-in əsas commercial üstünlüyü realizm yox, özünü haker kimi hiss etmə-sinin əlçatanlıq ilə verilməsidir.”

Bu dəlil-dən çıxarılan məhsul/dizayn nəticəsidir.

Final hesabat-da A, B və C bir-biri ilə qarışdırılmamalıdır.

---

# 7. Araşdırma əhatə dairəsi-u və oyun seçimi

Məqsəd yalnız uğurlu oyunları öyrənmək deyil.

Ən dəyərli məlumat çox vaxt **oxşar konseptə sahib, amma fərqli nəticə göstərmiş oyunların müqayisəsindən** gəlir.

İlkin araşdırma universe:

## Güclü nəticə göstərmiş əsas reference-lər

- Hacknet
- Cyber Manhunt
- Cyber Manhunt 2
- The Operator
- Orwell: Keeping an Eye On You
- SIMULACRA
- Hypnospace Outlaw
- Welcome to the Game / Welcome to the Game II
- CaseCracker
- Emily is Away seriyası — hacking deyil, amma interface-as-world baxımından faydalıdır

## Orta / niche nəticə göstərmiş reference-lər

- Grey Hack
- NITE Team 4
- Song of Farca
- SIMULACRA 2
- CaseCracker2
- Scrutinized
- hackmud
- A Normal Lost Phone
- Another Lost Phone: Laura’s hekayə

## Zəif və ya underperform etmiş müqayisə nümunələri

- Midnight Protocol
- Mainlining
- Need to Know
- SIMULACRA 3
- NeuroNet: Mendax Proxy
- Keyword: A Spider’s Thread
- Tech Support: Error Unknown

Bu siyahı dəyişə bilər. Oyunların “successful / medium / weak” təsnifatı moral keyfiyyət hökmü deyil; bazar/rəy/traction kontekstində araşdırma grouping-dir və istifadə edilən metriklər hər hesabat-da ayrıca göstərilməlidir.

---

# 8. Prioritet müqayisə qrupları

Ən çox informasiya verəcəyi gözlənilən müqayisələr:

## 8.1. terminal və hakerlik

```text
Hacknet
vs
Midnight Protocol
vs
Mainlining
vs
NITE Team 4
```

Araşdırılan sual:

> Eyni “hacking/terminal” rol hissi-si niyə bəzi oyunlarda böyük auditoriya tapır, digərlərində daha məhdud qalır?

## 8.2. Digital araşdırma

```text
Cyber Manhunt
vs
The Operator
vs
Orwell
vs
Song of Farca
vs
Need to Know
```

Araşdırılan sual:

> Information-axtarış və araşdırma oyun gedişi-i nə vaxt satisfying məntiqi nəticə çıxarma olur, nə vaxt sadəcə text/məlumat oxumağa çevrilir?

## 8.3. Found-device / phone interface

```text
SIMULACRA
vs
SIMULACRA 2
vs
SIMULACRA 3
```

Bu xüsusilə dəyərlidir, çünki eyni franchise daxilində nəticə fərqləri var.

Araşdırılan sual:

> Eyni interface/rol hissi formulu sequel-lərdə necə dəyişib və hansı dəyişikliklər oyunçu reaksiyası ilə əlaqəlidir?

---


## 8.4. Araşdırma dərinliyi planı — əsas istinad

Bütün oyunlar eyni dərinlikdə araşdırılmayacaq. araşdırma vaxtını və dəlil keyfiyyətini balanslamaq üçün oyunlar üç tier-ə bölünür.

### Tier A — tam dərin araşdırma

Bu oyunlar final genre conclusions üçün əsas dəlil bazasını təşkil edir. Hər biri üçün mümkün qədər:

- full Steam rəy məlumat toplusu;
- verification;
- deterministic statistics;
- mövzu/aspect yoxlama;
- məna yönümlü yoxlama;
- external araşdırma;
- yaradıcı intent;
- peşəkar/icma mənbələr;
- `analysis/<game>/2. deep-research.md`

hazırlanmalıdır.

| Oyun | Səbəb | vəziyyət |
|---|---|---|
| Hacknet | Terminal/özünü haker kimi hiss etmə və əlçatanlıq baseline | **Tamamlanıb** |
| Midnight Protocol | taktiki/system-dərinlik contrast | **Tamamlanıb** |
| Cyber Manhunt | Information/məntiqi nəticə çıxarma və social-engineering modeli | **Tamamlanıb** |
| The Operator | Məqsədli dəlil təhlili və müasir araşdırma UX | **Tamamlanıb** |
| Orwell: Keeping an Eye On You | Müşahidə, məlumat seçimi və etika | **Tamamlanıb** |
| Mainlining | Hacking + araşdırma + seçim; underperforming comparator | **Tamamlanıb** |
| SIMULACRA | Found-device/phone araşdırma baseline | **Tamamlanıb** |
| SIMULACRA 3 | Eyni franchise daxilində weaker outcome müqayisə | **Tamamlanıb** |

Tier A siyahısı araşdırma-in əsas məcburi oyun setidir. Oyun yalnız ciddi məlumat-access problemi və ya əhatə dairəsi dəyişməsi səbəbilə çıxarıla bilər; səbəb master brief-də qeyd edilməlidir.

### Tier B — Məqsədli müqayisəli araşdırma

Bu oyunlara tam dərin araşdırma yalnız əlavə dəlil lazım olarsa tətbiq edilir. Default metod:

- Məhsul və bazar görünüşü;
- mağaza təqdimat;
- targeted Steam rəy nümunə və ya kiçik məlumat toplusu;
- əsas müsbət/mənfi nümunələr;
- relevant yaradıcı/peşəkar/icma mənbə-lar;
- mövcud Tier A hipotezlərini test edən qısa focused hesabat.

| Oyun | Əsas araşdırma rolu |
|---|---|
| Cyber Manhunt 2 | Original-dakı lokallaşdırma/linearity problemlərinin sequel-də necə dəyişdiyini yoxlamaq |
| Need to Know | Orwell üçün weaker surveillance/bureaucracy comparator |
| Song of Farca | Remote araşdırma, surveillance və dialogue/seçim |
| Grey Hack | Simulation-heavy hacking və realizm/əlçatanlıq ekstremi |
| NITE Team 4 | Daha peşəkar/realistic cyber-operation rol hissi |
| Hypnospace Outlaw | Fictional internet, exploration və information archaeology |
| CaseCracker | Case-solving, ipucu relationship və məntiqi nəticə çıxarma structure |
| Welcome to the Game II | Browser/interface rol hissi, pressure və sistemli threat |

Tier B oyunu gözlənilmədən çox vacib yeni nümunə göstərərsə **Tier A-ya yüksəldilə bilər**.

### Tier C — Sürətli istinad / kontekst

Bu oyunlar əsas dəlil bazası deyil. Onlardan konkret sualı cavablandırmaq, bazar/context nümunəsi vermək və ya müəyyən mexanika-i yoxlamaq üçün istifadə olunur.

- SIMULACRA 2
- CaseCracker2
- Emily is Away seriyası
- Scrutinized
- hackmud
- A Normal Lost Phone
- Another Lost Phone: Laura’s hekayə
- NeuroNet: Mendax Proxy
- Keyword: A Spider’s Thread
- Tech Support: Error Unknown
- Welcome to the Game (birinci oyun, lazım olduqda sequel context üçün)

Quick-reference araşdırma adətən:
- mağaza/bazar snapshot;
- 10–30 yüksək-informasiya rəy;
- 1–3 external mənbə;
- konkret araşdırma sualına qısa qeyd

ilə məhdudlaşır.

### Tier dəyişmə qaydası

Tier-lər tam sərt deyil, amma özbaşına dəyişdirilməməlidir.

Oyun yalnız bu hallarda yuxarı tier-ə qaldırılır:
1. mövcud genre principle-i ciddi şəkildə təkzib edir;
2. əvvəl görmədiyimiz yeni oyunçunun rol hissi və ya uğursuzluq mode göstərir;
3. əsas müqayisə üçün boşluğu doldurur;
4. final imkan/risk qərarını material şəkildə dəyişə bilər.

Oyun aşağı tier-ə yalnız:
- məlumat əlçatmazdır;
- digər oyunla demək olar eyni dəlil verir;
- araşdırma saturation artıq həmin sualı kifayət qədər cavablandırıb

hallarında keçirilə bilər.

# 9. Araşdırma metodu — hər oyun üçün addımlar

Hər oyun mümkün qədər eyni metodla araşdırılmalıdır ki, sonradan müqayisə mənalı olsun.

## Mərhələ 1 — bazar və məhsul snapshot

Topla:

- release date;
- yaradıcı/publisher;
- current/base price;
- Steam rəy sayı;
- müsbət/mənfi rəy nisbəti;
- estimated owners/sales varsa;
- estimate mənbəyi;
- rəy volume;
- Steam tags;
- mağaza description;
- screenshots/trailer təqdimat;
- DLC/sequel/mod dəstəyi;
- təxmini oyun uzunluğu;
- platformlar.

Qayda:

> Owner/sales estimate heç vaxt exact sales kimi təqdim edilməməlidir.

Mümkün olduqda bir neçə estimate mənbəyi triangulate edilməlidir.

---

## Mərhələ 2 — Steam rəy məlumat toplusu

Mümkün qədər bütün English public rəyləri topla.

Minimum metaməlumat:

- rəy id;
- recommendation;
- rəy text;
- creation/update date;
- oyun müddəti at rəy;
- total oyun müddəti;
- faydalı votes;
- purchase/free/refund flags;
- author rəy count və mövcud digər metaməlumat.

Raw məlumat immutable saxlanmalıdır.

Processed məlumat raw məlumat-dan yenidən yaradıla bilməlidir.

---

## Mərhələ 3 — Deterministik preprocessing

- normalization;
- deduplication;
- empty/very-short flag;
- oyun müddəti conversion;
- oyun müddəti segmentation;
- basic statistics;
- deterministic faydalı/son dövr/low/high oyun müddəti nümunələr;
- verification.

Bu mərhələdə interpretation edilməməlidir.

çıxış:

`data/reports/<game>/summary.md`

---

## Mərhələ 4 — Qualitative taxonomy kəşf

Əvvəlcə rəylərin seçilmiş, müxtəlif nümunə-ları oxunmalıdır:

- faydalı müsbət;
- faydalı mənfi;
- son dövr müsbət;
- son dövr mənfi;
- low oyun müddəti;
- high oyun müddəti;
- lazım olduqda random/stratified nümunə.

Məqsəd əvvəlcədən hazırlanmış mövzu siyahısını kor-koranə tətbiq etmək yox, **oyunun öz datasından taxonomy çıxarmaqdır**.

İlkin ümumi mövzu nümunələri:

- oyunçunun rol hissi;
- oyuna dalma hissi;
- UI;
- terminal;
- hekayə;
- mystery;
- araşdırma;
- exploration;
- kəşf;
- soundtrack;
- atmosphere;
- puzzle;
- difficulty;
- ilkin öyrətmə;
- təkrarçılıq;
- dərinlik;
- realizm;
- texniki düzgünlük;
- oyunçunun qərar sərbəstliyi və təsiri;
- nəticələr;
- pacing;
- length;
- təkrar oynama dəyəri;
- mod dəstəyi;
- bugs;
- compatibility;
- final.

Hər oyun üçün taxonomy genişlənə və ya dəyişə bilər.

---

## Mərhələ 5 — Aspect-based rəy təhlil

Sadəcə rəyin overall müsbət/mənfi olması kifayət deyil.

Məsələn:

> “hekayə əladır, amma hacking çox repetitive-dir.”

belə kodlanmalıdır:

```text
STORY       → positive
REPETITION  → negative
HACKING_LOOP → negative
```

Hər rəy:

- 0..N mövzu;
- hər mövzu üçün sentiment: müsbət / mənfi / mixed / neutral;
- lazım olsa etibarlılıq

daşıya bilər.

Mümkün qədər full məlumat toplusu classification edilir.

Əgər full-məlumat toplusu LLM classification texniki və ya cost səbəbindən mümkün deyilsə:

1. stratified nümunə yaradılır;
2. taxonomy həmin nümunə üzərində tətbiq edilir;
3. keyword-assisted genişlənmə aparılır;
4. nəticənin nümunə-based olduğu hesabat-da açıq yazılır.

Heç vaxt nümunə nəticəsi full population faizi kimi təqdim edilmir.

---

## Mərhələ 6 — Classification keyfiyyət yoxlaması

Avtomatik classification kor-koranə qəbul edilməməlidir.

Minimum yoxlama:

- müsbət və mənfi;
- low və high oyun müddəti;
- common və rare mövzu-lər

üzrə stratified manual yoxlama.

Səhv nümunə görünərsə taxonomy/prompt düzəldilir və classification təkrarlanır.

Model/prompt versiyası mümkün olduqda saxlanmalıdır.

---

## Mərhələ 7 — oyun müddəti və qrup təhlil

Araşdır:

- 0–1h;
- 1–3h;
- 3–10h;
- 10h+;
- son dövr vs historical;
- faydalı vs ordinary;
- refunded varsa;
- technical complaint vs dizayn complaint.

Əsas suallar:

- erkən churn-a bənzər mənfi geribildirim nədir?
- uzun oynayanların şikayəti nədir?
- uzun oynayanlar hansı dəyərə görə qalır?
- illər keçdikcə complaint profile dəyişirmi?

Correlation səbəb-nəticə kimi təqdim edilməməlidir.

---

## Mərhələ 8 — Reddit və icma araşdırma

Axtar:

- “worth playing”;
- “best part”;
- “worst part”;
- “repetitive”;
- “final”;
- “what do you wish was different?”;
- “games like X”;
- “why did you stop playing?”;
- sequel müqayisə;
- texniki auditoriya reaction.

Xüsusilə yüksək dəyərli cümlələr:

- “I wish the game had…”
- “I loved X but hated Y…”
- “I stopped because…”
- “The part I still remember is…”

icma materialı Steam rəyləri ilə cross-check edilməlidir.

---

## Mərhələ 9 — oyun gedişi / walkthrough araşdırma

İstifadəçi bu araşdırma layihəsində oyunları özü almaq və oynamaq məcburiyyətində deyil.

Buna görə oyun gedişi dəlil ayrıca vacibdir.

İstifadə edilə bilər:

- first 30/60 minutes oyun gedişi;
- full walkthrough;
- longplay;
- no-commentary oyun gedişi;
- video transcript;
- retrospective/rəy.

Analiz ediləcək:

- ilk qarşılıqlı əlaqə;
- təlim hissəsi;
- ilk əyləncəli ana qədər vaxt;
- mexanika introduction timeline;
- neçə dəqiqədən bir yeni sistem açılır;
- qarşılıqlı əlaqə density;
- reading vs doing balansı;
- uğursuzluq/yenidən cəhd;
- UI çətinlik;
- memorable sequence-lər.

Video/transcript dəlil rəy fikri ilə qarışdırılmamalıdır.

---

## Mərhələ 10 — peşəkar rəylər

peşəkar rəylərin rolu:

- structure/pacing;
- oyun dizaynı language;
- broader müqayisə;
- launch-period problemləri

haqqında əlavə context verməkdir.

peşəkar rəy oyunçu datasını əvəz etmir.

---

## Mərhələ 11 — yaradıcı interview / postmortem

Mümkün olduqda araşdır:

- yaradıcı-in ilkin məqsədi;
- prototype necə yaranıb;
- target audience;
- hansı mexanika dəyişdirilib;
- development constraints;
- hansı geribildirim-ə reaksiya verilib;
- sequel/DLC-də niyə dəyişiklik edilib;
- launch nəticələri barədə açıqlama.

Ən dəyərli müqayisələrdən biri budur:

```text
developer intent
vs
player experienced outcome
```

---

## Mərhələ 12 — mağaza təqdimat analizi

Araşdır:

- oyun özünü hansı cümlə ilə satır;
- screenshot-lar nə göstərir;
- trailer-də hansı qarşılıqlı əlaqə prioritetdir;
- tags hansı expectation yaradır;
- “realistic”, “simulation”, “hekayə-rich” və s. sözlər oyunçu expectation-a necə təsir edir.

Marketing expectation ilə actual oyun gedişi arasında mismatch ayrıca qeyd olunmalıdır.

---

## Mərhələ 13 — Per-game synthesis

Bütün dəlil birləşdirilərək:

`analysis/<game>/2. deep-research.md`

hazırlanır.

Bu sənəd sadəcə mənbə summary deyil; **dizayn/məhsul interpretation** olmalıdır.

---

## Mərhələ 14 — Təqdimat xülasəsi

Dərin araşdırma tamamlandıqdan sonra:

`analysis/<game>/1. presentation-brief.md`

hazırlanmalıdır.

Bu fayl 2–5 dəqiqəlik təqdimat üçün nəzərdə tutulur və aşağıdakı suallara qısa cavab verməlidir:

1. Oyun nədir və əsas rol hissi nədir?
2. Əsas bazar/rəy göstəriciləri hansılardır?
3. Oyunçu niyə başlayır?
4. Oyunçu niyə davam edir?
5. Ən güclü tərəflər hansılardır?
6. Ən zəif tərəflər hansılardır?
7. Kommersiya nəticəsi haqqında hansı faktiki siqnallar var?
8. Uğuru və ya zəif nəticəni izah edən əsas hipotezlər hansılardır?
9. Bizim layihə üçün nəyi götürmək, nədən qaçmaq lazımdır?
10. Oyunu bir cümlədə necə yekunlaşdırmaq olar?

Satış rəqəmi açıq və etibarlı mənbədən məlum deyilsə, uydurma və ya estimate dəqiq satış kimi yazılmamalıdır. Steam rəy həcmi və digər siqnallar ayrıca göstərilməli, səbəb izahları **hipotez** kimi işarələnməlidir.

---

## 10.0. Hər oyun üçün standart dörd fayl

Tier A oyunları və tam araşdırılan digər oyunlar üçün `analysis/<game>/` qovluğu eyni dörd fayldan ibarət olmalıdır:

```text
analysis/<game>/
├── 4. research-kickoff.md
├── 3. theme-analysis.md
├── 2. deep-research.md
└── 1. presentation-brief.md
```

Bu faylların rolları fərqlidir:

### `4. research-kickoff.md`

Araşdırmadan əvvəl cavablandırılacaq sualları, ilkin hipotezləri, oyunun niyə seçildiyini və hansı müqayisə üçün istifadə ediləcəyini müəyyən edir.

Bu sənəd son nəticə deyil.

Araşdırma tamamlandıqdan sonra kickoff faylı tarixi plan sənədi kimi saxlanılır və status hissəsində əsas nəticə sənədlərinə keçid verilir.

Əgər oyun araşdırması bu standart formalaşmamışdan əvvəl aparılıbsa, sonradan yaradılan kickoff faylı açıq şəkildə **retrospektiv şəkildə bərpa edilmiş** sənəd kimi işarələnməlidir. Sonradan əldə edilmiş nəticələr guya əvvəlcədən bilinirmiş kimi təqdim edilməməlidir.

### `3. theme-analysis.md`

Steam rəyləri və digər geniş rəy məlumatları üzərində aparılan kəmiyyət və məna yönümlü təhlili saxlayır:

- mövzu namizədləri;
- rəy nisbətləri;
- oyun müddəti qrupları;
- məna yönümlü yoxlama;
- əsas müsbət və mənfi nümunələr;
- metodoloji məhdudiyyətlər.

Bu fayl dəlil və ölçmə qatıdır.

### `2. deep-research.md`

Həmin oyun üzrə əsas yekun araşdırma sənədidir.

Burada:

- məlumat toplusu;
- açıq mənbələr;
- yaradıcı məqsədləri;
- oyunçu rəyləri;
- oyun dizaynı;
- məhsul nəticələri

birləşdirilir və istifadə edilə bilən nəticələr çıxarılır.

Bir oyun haqqında ətraflı yalnız bir sənəd oxunacaqsa, `2. deep-research.md` seçilməlidir.

### `1. presentation-brief.md`

Yığcam təqdimat xülasəsidir.

Mütləq ehtiva etməlidir:
- bir cümləlik əsas nəticə;
- oyun və bazar/rəy göstəriciləri;
- əsas rol hissi;
- oyunçunun başlama və davam etmə motivləri;
- güclü və zəif tərəflər;
- kommersiya nəticəsinin faktiki siqnalları;
- uğur/zəiflik izah hipotezləri;
- bizim layihə üçün götürüləcək və qaçılacaq məqamlar.

Bu fayl yeni dəlil mənbəyi deyil; `2. deep-research.md`, `3. theme-analysis.md` və yoxlanmış məlumatlardan yığcamlaşdırılır.

---

# 10. Hər oyun üçün deep-araşdırma hesabat standartı

Hər `analysis/<game>/2. deep-research.md` mümkün qədər eyni peşəkar strukturu izləməlidir.

## 1. Yekun xülasə

1–2 səhifəlik qısa nəticə:

- oyun nədir;
- nəyi düzgün edir;
- əsas problem nədir;
- niyə oyunçular oynayır;
- bizim üçün ən vacib 3–5 dərs.

Yalnız bu bölmə oxunsa belə əsas mənzərə aydın olmalıdır.

## 2. Araşdırmanın əhatəsi və məlumat keyfiyyəti

- hansı məlumat toplusu istifadə olunub;
- rəy sayı;
- tarix aralığı;
- external mənbə-lar;
- limitations;
- classification əhatə;
- etibarlılıq.

## 3. Məhsul və bazar görünüşü

- release;
- yaradıcı/publisher;
- price;
- traction göstəriciləri;
- rəy göstəriciləri;
- təqdimat;
- target audience hipotezi.

## 4. Oyunun mahiyyəti

- bir cümləlik description;
- oyunçunun rol hissi;
- game loop;
- primary interactions;
- progression.

## 5. Attraction: insanlar niyə başlayır?

- ilkin cəlbedicilik;
- rol hissi;
- mağaza promise;
- visual identity;
- yenilik effekti;
- audience motivation.

## 6. oyunda qalma: insanlar niyə davam edir?

- hekayə;
- kəşf;
- progression;
- mastery;
- tension;
- collection;
- curiosity;
- social/icma məzmun.

## 7. ilkin öyrətmə və ilk sessiya

- first 5/15/30/60 min;
- çətinlik;
- early mənfi mövzular;
- learning curve.

## 8. əsas oyun dövrü və sistem dərinliyi

- loop breakdown;
- qərar sıxlığı;
- mexanika variation;
- progression;
- təkrarçılıq onset;
- mənalı seçim.

## 9. UI/UX və oyuna dalma hissi

- interface-as-world;
- usability;
- həqiqilik hissi;
- audio/visual geribildirim;
- technical-user expectation.

## 10. Narrative və məzmun dizayn

- delivery method;
- yazı keyfiyyəti;
- characters;
- mystery;
- memorable moments;
- oyun gedişi-hekayə integration.

## 11. oyunçu geribildirim — Quantitative

mövzu/aspect cədvəlləri:

- mention count;
- müsbət;
- mənfi;
- mixed;
- segmentlər;
- mümkün olduqda oyun müddəti fərqləri.

## 12. oyunçu geribildirim — Qualitative

Ən vacib nümunələr:

- nə bəyənilir;
- nə bəyənilmir;
- representative examples;
- oyunçu language.

Uzun quote-lar yox, qısa dəlil və paraphrase üstünlük təşkil etməlidir.

## 13. Technical / Compatibility Issues

dizayn complaint ilə texniki complaint qarışdırılmamalıdır.

## 14. Audience Segments

Məsələn:

- casual rol hissi audience;
- araşdırma audience;
- technical/cyber audience;
- narrative audience.

Hansı audience üçün oyun işləyir və harada expectation mismatch yaranır?

## 15. Yaradıcı məqsədi ilə oyunçu təcrübəsinin müqayisəsi

yaradıcı məqsədi məlumdursa, real oyunçu geribildirim ilə müqayisə et.

## 16. Uğurun / zəifliyin izah hipotezləri

Burada correlation və causation ayrılmalıdır.

“Bunun səbəbi budur” əvəzinə dəlil tam deyilsə:

> “Mövcud dəlil bunu güclü izah hipotezi kimi göstərir.”

## 17. Bizim üçün dizayn dərsləri

İki kateqoriya:

### Saxlamağa / öyrənməyə dəyər

### Qaçmalı olduğumuz risklər

## 18. imkan-lər

Oyun hansı problemi tam həll etməyib?

- daha yaxşı reactivity;
- deeper araşdırma;
- alternative paths;
- better ilkin öyrətmə;
- stronger nəticə;
- better returning-oyunçu support;
- və s.

Bu bölmə hələ konkret yeni oyun ideyası yazmamalıdır.

## 19. Açıq suallar

Nəyi hələ bilmirik?

## 20. mənbələr və dəlil Notes

Daxili məlumat toplusu və Açıq mənbələr.

---

# 11. Oyunlararası müqayisə hesabat standartı

Path:

`analysis/comparisons/<game-a>-vs-<game-b>.md`

və ya 3–4 oyun üçün topic-based müqayisə.

Struktur:

## 1. müqayisə Question

Nəyi anlamaq üçün müqayisə edirik?

## 2. Why These Games Are Comparable

Ortaq rol hissi, mexanika, audience və ya interface.

## 3. Məhsul və bazar görünüşü

Eyni metriklərlə yan-yana.

## 4. ilkin cəlbedicilik və təqdimat

## 5. əsas oyun dövrü

## 6. ilkin öyrətmə

## 7. dərinlik və təkrarçılıq

## 8. Narrative Integration

## 9. UI/UX

## 10. nəticə / Reactivity

## 11. oyunçu geribildirim Differences

Eyni taxonomy mümkün qədər istifadə olunmalıdır.

## 12. Audience Expectation Differences

## 13. Why Outcomes May Have Diverged

Yalnız dəlil-supported hipotezlər.

## 14. Transferable Lessons

Bu müqayisədən bizim layihəyə nə keçir?

---

# 12. oyunlararası genre synthesis

Path:

`analysis/final/3. genre-synthesis.md`

Bu sənəd individual oyunları təkrar xülasə etməməlidir.

Məqsəd **oyunlar arasında təkrarlanan nümunələri** çıxarmaqdır.

Struktur:

## 1. Yekun xülasə

## 2. Genre / Category Definition

Bu bazarda əslində hansı subcategory-lər var?

Məsələn:

- terminal hacking;
- digital araşdırma;
- surveillance;
- found phone/device;
- uydurma əməliyyat sistemi/internet;
- interface narrative.

## 3. oyunçu Jobs / Fantasies

Oyunçu nə yaşamaq istəyir?

## 4. Purchase amillər

Nə click və interest yaradır?

## 5. Satisfaction amillər

Nə müsbət geribildirim yaradır?

## 6. oyunda qalma amillər

Nə oyunçunu davam etdirməyə sövq edir?

## 7. Repeated uğursuzluq Modes

Məsələn:

- repetitive fake hacking;
- too much reading without qarşılıqlı əlaqə;
- no mənalı nəticə;
- confusing ilkin öyrətmə;
- dayaz “alət = key” systems;
- fake seçim;
- weak final;
- technical instability;
- marketing expectation mismatch.

Bu siyahı əvvəlcədən nəticə deyil; araşdırma ilə təsdiqlənməlidir.

## 8. Successful vs Weak nümunə müqayisə

## 9. Audience Segments

## 10. UI/UX Principles

## 11. Narrative Principles

## 12. System/oyun gedişi Principles

## 13. ilkin öyrətmə Principles

## 14. məzmun/Pacing Principles

## 15. bazar təqdimat Principles

## 16. imkan xəritəsi

Bazarda hansı boşluqlar var?

## 17. risk Map

Yeni oyunda ən böyük risklər hansılardır?

## 18. dizayn prinsipləri

Yalnız bir neçə oyunda yox, oyunlararası dəlil ilə dəstəklənən qaydalar.

## 19. Açıq suallar

## 20. dəlil / Methodology Appendix

---

# 13. FINAL hesabat

Əsas peşəkar deliverable:

`analysis/final/1. executive-genre-research-report.md`

Sonradan eyni sənəd PDF/slide deck formasına çevrilə bilər.

Bu sənəd araşdırma arxivindən fərqlənməlidir.

Məqsəd:

> 20–40 dəqiqə ərzində bazarı, oyunçu ehtiyaclarını, işləyən/işləməyən nümunələri və concept development üçün əsas constraint-ləri anlamağa imkan vermək.

Final hesabat aşağıdakı struktura sahib olmalıdır.

---

## 1. Yekun xülasə

Maksimum yüksək informasiya sıxlığı.

Cavab verməlidir:

- nə araşdırdıq;
- nə öyrəndik;
- oyunçular bu janra niyə gəlir;
- əsas satisfaction amillər nədir;
- əsas uğursuzluq modes nədir;
- ən böyük imkan-lər hansıdır;
- yeni concept yaradarkən hansı 5–10 prinsip nəzərə alınmalıdır.

Bu bölmə öz-özünə oxuna bilən olmalıdır.

---

## 2. araşdırma Objective və əhatə dairəsi

- biznes/məhsul qərarı;
- araşdırılan oyun sayı;
- time period;
- mənbə-lar;
- metod;
- nələr əhatə dairəsi-dan kənardır.

---

## 3. bazar mənzərəsi

Vizual/cədvəl şəklində:

- subgenre-lər;
- əsas oyunlar;
- release ili;
- price;
- rəy volume;
- sentiment;
- owner/sales estimate range;
- primary rol hissi;
- primary interface.

Məqsəd bazarın “xəritəsini” göstərməkdir.

---

## 4. oyunçu Needs və Core Fantasies

Məsələn araşdırma təsdiqləyərsə:

- hacker kimi hiss etmək;
- gizli məlumat tapmaq;
- ağıllı problem solver olmaq;
- başqa insanların digital həyatını araşdırmaq;
- təhlükəli/illegal sistemlərə giriş hissi;
- məlumat parçalarını birləşdirmək;
- sirri açmaq;
- nəzarət/operator rolu.

Hər rol hissi dəlil və oyun nümunələri ilə göstərilməlidir.

---

## 5. What Makes These Games Work

oyunlararası dəlil əsasında:

- ilkin cəlbedicilik;
- oyuna dalma hissi;
- məlumat kəşfi;
- sistem dərinliyi;
- narrative integration;
- mənalı nəticə;
- memorable moments;
- audio/visual geribildirim;
- progression;
- pacing.

Burada konkret oyunlardan nümunələr istifadə olunur.

---

## 6. Why These Games Fail or Underperform

Təkrarlanan uğursuzluq nümunəsi-lər.

Hər nümunə üçün:

| Problem | oyunçu impact | dəlil | Example games | dizayn implication |
|---|---|---|---|---|

---

## 7. Successful vs Underperforming Comparisons

Ən vacib pair/group nəticələrinin qısa executive versiyası.

Məsələn:

- Hacknet vs Midnight Protocol;
- Cyber Manhunt vs Mainlining;
- Orwell vs Need to Know;
- SIMULACRA vs SIMULACRA 3.

Məqsəd “winner seçmək” deyil; outcome divergence-i anlamaqdır.

---

## 8. Audience Segmentation

Hansı oyunçu type-lar var?

Hər segment üçün:

- motivation;
- tolerance;
- desired dərinlik;
- preferred interface;
- risk;
- representative games.

---

## 9. dizayn prinsipləri for Concept Development

Bu bölmə final araşdırma-in əsas məhsullarından biridir.

Hər prinsip:

```text
Principle
→ Evidence
→ Why it matters
→ What to do
→ What to avoid
```

formatında yazılmalıdır.

Bu prinsiplər yeni ideyanın dizayn brief-i üçün giriş olacaq.

---

## 10. imkan xəritəsi

Hələ konkret oyun ideyası deyil.

Məsələn imkan-lər belə kateqoriyalaşdırıla bilər:

- underserved rol hissi;
- qarşılıqlı əlaqə imkan;
- narrative imkan;
- system-dərinlik imkan;
- multiplayer/social imkan;
- məzmun-production imkan;
- creator/mod imkan;
- bazar-təqdimat imkan.

Hər imkan üçün:

- hansı problemə cavab verir;
- hansı oyunlarda boşluq görünür;
- hansı auditoriyaya xidmət edir;
- implementation risk nədir.

---

## 11. risk reyestri

Yeni concept üçün əvvəlcədən görünən risklər:

| risk | dəlil | Impact | Early validation method |
|---|---|---|---|

Məsələn:

- yenilik effekti tez bitir;
- command loop repetitive olur;
- çox reading;
- false realizm expectation;
- məzmun production cost;
- ilkin öyrətmə mürəkkəblik;
- weak təkrar oynama dəyəri;
- UI çətinlik.

---

## 12. ideyaların qiymətləndirilməsi çərçivəsi

Araşdırmadan sonra yaranacaq hər yeni oyun ideyası eyni rubric ilə yoxlanmalıdır.

Rubric final araşdırma nəticələrindən yaradılacaq.

Mümkün sahələr:

- rol hissi aydınlıq;
- ilkin cəlbedicilik;
- ilk əyləncəli ana qədər vaxt;
- mexanika dərinlik;
- təkrarçılıq resistance;
- narrative/oyun gedişi integration;
- kəşf;
- nəticə;
- audience aydınlıq;
- production feasibility;
- məzmun scalability;
- differentiation;
- bazar təqdimat.

Bu mərhələdə rubric-in çəkiləri araşdırma bitmədən təsadüfi təyin edilməməlidir.

---

## 13. Recommended Next məhsul-kəşf Steps

araşdırma bitəndən sonra:

1. imkan-lərdən concept variants yarat;
2. concept-ləri evaluation framework ilə müqayisə et;
3. 2–3 yüksək potensiallı concept seç;
4. çox kiçik prototype qur;
5. target audience ilə test et;
6. first-session və rol hissi validation apar;
7. yalnız bundan sonra böyük production qərarı ver.

---

## 14. Methodology və Limitations

Bu da görünən olmalıdır.

- Steam rəy bias;
- public-məlumat limitations;
- owner estimate qeyri-müəyyənlik;
- self-selection;
- rəy ≠ all oyunçular;
- correlation ≠ causation;
- game-playing yerine video/walkthrough dəlil istifadə edilməsi;
- LLM classification limitations.

Bu bölmə hesabat-un etibarlılığı üçün vacibdir.

---

## 15. Appendix

- game list;
- per-game hesabat links;
- müqayisə hesabat links;
- taxonomy;
- məlumat dictionary;
- mənbə list;
- əlavə cədvəllər.

---

# 14. Final hesabat-un keyfiyyət standartı

Yekun sənədlər “ChatGPT cavabı” kimi görünməməlidir.

Onlar peşəkar araşdırma deliverable kimi hazırlanmalıdır.

## Yazı standartı

- əsas dil Azərbaycan dili;
- zəruri industry terminləri English formada qala bilər;
- eyni fikir təkrar edilməməlidir;
- nəticə ilə dəlil ayrılmalıdır;
- hər vacib nəticənin mənbəsi olmalıdır;
- çox uzun rəy quote-ları istifadə edilməməlidir;
- raw məlumat əsas mətni boğmamalıdır;
- ən vacib məlumat yuxarıda olmalıdır;
- detail appendix və per-game hesabat-lara ötürülməlidir.

## Vizual standart

Final mərhələdə hesabat-da mümkün olduqda:

- müqayisə tables;
- mövzu charts;
- oyunçu-segment diagrams;
- imkan xəritəsi;
- risk matrix;
- bazar mənzərəsi;
- dəlil heatmap

istifadə olunmalıdır.

## etibarlılıq

Vacib nəticələr üçün lazım olduqda:

- High etibarlılıq;
- Medium etibarlılıq;
- Low etibarlılıq

işarəsi istifadə edilə bilər.

etibarlılıq dəlil breadth və consistency-yə əsaslanmalıdır, “model hissinə” yox.

---

# 15. Nə etməməliyik?

- Yalnız Steam müsbət rəy nisbəti-ya baxıb nəticə çıxarma.
- Bir viral Reddit postunu ümumi oyunçu opinion kimi təqdim etmə.
- Owner estimate-i exact sales kimi göstərmə.
- “Successful game-də bu feature var, deməli feature uğurun səbəbidir” kimi səbəb-nəticə qurma.
- Əvvəlcədən sevdiyimiz ideyanı doğrulamaq üçün dəlil seçmə.
- Bütün texniki auditoriya-i eyni hesab etmə.
- mənfi rəyləri yalnız “oyunçunun başa düşməməsi” kimi dismiss etmə.
- müsbət rəyləri də avtomatik dizayn validation sayma.
- Oyunları yalnız feature checklist ilə müqayisə etmə; rol hissi və oyunçu experience əsasdır.
- araşdırma bitmədən konkret yeni concept-ə emosional bağlanma.

---

# 16. Araşdırmanın “Tamamlanma meyarı” şərti

araşdırma mərhələsi o zaman tamamlanmış sayılır ki:

1. əsas representative oyunların per-game deep araşdırma-i var;
2. ən vacib successful-vs-underperforming müqayisə-lar hazırdır;
3. recurring müsbət və mənfi mövzu-lər oyunlararası səviyyədə müəyyən edilib;
4. oyunçunun rol hissi və audience segmentləri aydındır;
5. bazar təqdimat nümunələri çıxarılıb;
6. dizayn prinsipləri dəlil ilə dəstəklənir;
7. imkan xəritəsi hazırlanıb;
8. risk reyestri hazırlanıb;
9. ideyaların qiymətləndirilməsi çərçivəsi hazırlanıb;
10. `analysis/final/1. executive-genre-research-report.md` peşəkar şəkildə tamamlanıb.

Bundan sonra ideya generation/selection ayrıca mərhələ kimi başlayır.

---


## 16.1. Praktik stop condition — araşdırmanı nə vaxt dayandırırıq?

Tamamlanma meyarı yalnız “bütün siyahını oxuduq” demək deyil. araşdırma aşağıdakı dörd şərt birlikdə ödənəndə bağlanır:

### A. Məcburi əhatə

- bütün **Tier A** oyunları tamamlanıb və ya çıxarılma səbəbi sənədləşdirilib; tamamlanmış hər Tier A oyunda standart dörd fayl, o cümlədən `1. presentation-brief.md`, hazırdır;
- terminal və hakerlik, digital araşdırma, surveillance/information-selection və found-device/interface istiqamətlərinin hər birində ən azı bir güclü reference və bir contrast nümunəsi var.

### B. Məcburi müqayisə-lar

Minimum aşağıdakı müqayisə-lar olmalıdır:

- Hacknet vs Midnight Protocol — **tamamlanıb**;
- Cyber Manhunt vs The Operator — **tamamlanıb**;
- Cyber Manhunt vs Mainlining — **tamamlanıb**;
- Orwell vs Need to Know — **tamamlanıb**;
- SIMULACRA vs SIMULACRA 3 — **tamamlanıb**.

Lazım olduqda 3+ oyunlu thematic müqayisə-lar ayrıca hazırlanır.

### C. araşdırma saturation

Son 2–3 yeni deep/focused oyun:
- yeni major oyunçunun rol hissi;
- yeni recurring uğursuzluq mode;
- final dizayn prinsipləri-i ciddi dəyişən yeni dəlil

gətirmirsə və əsas nəticələr təkrar təsdiqlənirsə, əlavə oyunların marginal araşdırma value-su aşağı sayılır.

Bu nöqtədən sonra yeni oyun əlavə etmək əvəzinə synthesis və qərar-support sənədlərinə keçilir.

### D. Final qərar-support package

Aşağıdakı final fayllar hazır olmadan araşdırma bitmiş sayılmır:

```text
analysis/final/
├── 2. market-landscape.md
├── 3. genre-synthesis.md
├── 4. design-principles.md
├── 5. opportunity-map.md
├── 6. risk-register.md
├── 7. concept-evaluation-framework.md
└── 1. executive-genre-research-report.md
```

Bu faylların rolu:

- `2. market-landscape.md` — bazar/subgenre xəritəsi və representative games;
- `3. genre-synthesis.md` — oyunlararası recurring nümunələr;
- `4. design-principles.md` — dəlil-backed dizayn qaydaları;
- `5. opportunity-map.md` — həll olunmamış oyunçu/məhsul imkan-ləri;
- `6. risk-register.md` — yeni concept üçün əsas risklər və validation üsulları;
- `7. concept-evaluation-framework.md` — sonradan yaradılan ideyaları müqayisə etmək üçün rubric;
- `1. executive-genre-research-report.md` — əsas peşəkar yekun hesabat.

**Yeni oyun ideyasının yaradılması araşdırma Tamamlanma meyarı-a daxil deyil.** Idea generation bu package tamamlandıqdan sonra ayrıca məhsul-kəşf mərhələsidir.

# 17. Cari vəziyyət — 2026-10-03

## Tamamlanan

### Phase 2 mövzu namizədi infrastructure

Hacknet üçün bütün rəy toplusu üzrə mövzu/aspect analizindən əvvəl yoxlama edilə bilən deterministik retrieval mərhələsi əlavə olunub:

- `config/theme_taxonomy.yaml`
- `src/processors/theme_candidates.py`
- `src/reports/theme_candidate_report.py`

Bu mərhələ final məna yönümlü classification deyil. Məqsədi bütün rəy corpus-da mövzu namizədlərini tapmaq, oyun müddəti və overall recommendation paylanmasını ölçmək və hər mövzu üçün manual/LLM yoxlama nümunə-ları yaratmaqdır.

Generated çıxış-lar script lokalda işə salındıqdan sonra:

- `data/processed/hacknet/themes/candidates.jsonl`
- `data/processed/hacknet/themes/statistics.json`
- `data/processed/hacknet/themes/samples/<theme>_positive.csv`
- `data/processed/hacknet/themes/samples/<theme>_negative.csv`
- `data/processed/hacknet/themes/samples/<theme>_audit.csv`
- `data/reports/hacknet/theme-candidates.md`

olacaq.

Vahid command:

`python -m src.theme_pipeline --game hacknet`

`positive/negative` nümunə-lar faydalı rəyləri prioritetləşdirir. `audit` nümunə-lar isə recommendation və oyun müddəti qrupu-ları arasında deterministik balans yaradır ki, validation yalnız viral/faydalı rəylərə bağlı qalmasın.


### araşdırma infrastructure

Steam üçün reproducible araşdırma pipeline qurulub:

- metaməlumat collection;
- paginated ingilisdilli Steam rəyi collection;
- immutable raw pages;
- resume;
- normalization;
- deduplication;
- oyun müddəti segmentation;
- statistics;
- nümunələr;
- deterministic hesabat;
- integrity verification;
- cross-platform line-final handling.

### Hacknet məlumat toplusu

Hacknet Steam App ID: `365450`

Verified məlumat toplusu:

- xam rəylər: **11,773**
- təkrarsız rəylər: **11,773**
- müsbət: **11,082**
- mənfi: **691**
- müsbət rəy nisbəti: **94.13%**

Verification uğurla keçir.

Əsas məlumat:

`data/processed/hacknet/`

Deterministik hesabat:

`data/reports/hacknet/summary.md`

### Hacknet deep araşdırma

Hacknet üzrə əsas per-game araşdırma mərhələsi tamamlanıb:

- `analysis/hacknet/2. deep-research.md`
- `analysis/hacknet/3. theme-analysis.md`
- `config/aspect_taxonomy.yaml`

11,773 rəy üzrə bütün rəy toplusu üzrə mövzu namizədi yoxlama və məna yönümlü yoxlama aparılıb. Əsas dəlil-backed nəticələr:

- özünü haker kimi hiss etmə və oyuna dalma hissi güclü satisfaction amil-ləridir;
- hekayə, terminal və kəşf eyni experience stack-in hissələri kimi işləyir;
- təkrarçılıq əsas oyun dizaynı riskidir;
- bugs/compatibility ayrıca böyük mənfi-rəy amil-dir;
- seçilmiş həqiqilik hissi tam realizm-dən daha sağlam görünür;
- qərar sərbəstliyi/nəticə/dünyanın reaksiyası gələcək müqayisə-larda əsas imkan suallarıdır.

Hacknet nəticələri artıq növbəti oyun üzərində test edilməlidir.

### Midnight Protocol deep araşdırma

Midnight Protocol üzrə əsas araşdırma mərhələsi tamamlanıb:

- verified Steam məlumat toplusu: **301 ingilisdilli rəy**
- müsbət: **253**
- mənfi: **48**
- `analysis/midnight-protocol/3. theme-analysis.md`
- `analysis/midnight-protocol/2. deep-research.md`

Bütün 48 mənfi rəy məna yönümlü yoxlama edilib. Əsas nəticələr:

- növbə əsaslı taktiki model Hacknet-dən daha çox qərar dərinlik yaradır;
- RNG (təsadüfi nəticə mexanizmi) və ədalətlilik və yenidən cəhd/rollback əsas uğursuzluq amil-ləridir;
- 1–3h qrup xüsusi risk nöqtəsidir;
- yalnız klaviatura ilə control həm oyuna dalma hissi amil, həm UX çətinlik-dır;
- seçim/reputation Hacknet-də zəif olan oyunçunun qərar sərbəstliyi və təsiri/nəticə problemini xeyli yaxşı həll edir;
- seçilmiş həqiqilik hissi prinsipi ikinci oyunda da təsdiqlənir.

### Hacknet vs Midnight Protocol

müqayisə tamamlanıb:

`analysis/comparisons/1. hacknet-vs-midnight-protocol.md`

Əsas oyunlararası tension:

```text
Hacknet:
fast rol hissi payoff
→ simple loop
→ repetition risk

Midnight Protocol:
deeper decision model
→ higher system/cognitive load
→ fairness + recovery + friction risk
```

### Cyber Manhunt deep araşdırma

Cyber Manhunt üzrə əsas araşdırma mərhələsi tamamlanıb:

- verified Steam məlumat toplusu: **847 rəy**
- müsbət: **681**
- mənfi: **166**
- `analysis/cyber-manhunt/3. theme-analysis.md`
- `analysis/cyber-manhunt/2. deep-research.md`

Əsas nəticələr:

- 0–3h qrup çox yüksək risk daşıyır: 95 rəyin 59-u mənfi-dir;
- LINEARITY_SCRIPTING ən güclü dizayn risklərindən biridir;
- lokallaşdırma/yazı keyfiyyəti text-heavy oyun gedişi-ə birbaşa təsir edir;
- araşdırma rol hissi güclüdür, amma exact ipucu/progression dependency məntiqi nəticə çıxarma hissini zəiflədir;
- information-driven oyun gedişi də təkrarçılıq-dan immun deyil;
- tam realizm tələb olunmur, seçilmiş həqiqilik hissi üçüncü oyunda da işləyir.

### The Operator deep araşdırma

The Operator üzrə əsas araşdırma mərhələsi tamamlanıb:

- verified Steam məlumat toplusu: **3,781 rəy**
- müsbət: **3,392**
- mənfi: **389**
- `analysis/the-operator/3. theme-analysis.md`
- `analysis/the-operator/2. deep-research.md`
- `analysis/comparisons/3. cyber-manhunt-vs-the-operator.md`

Əsas nəticələr:

- focused dəlil alətlər Cyber Manhunt-dan daha yüksək aydınlıq yaradır;
- interface/audio “operator” rol hissi-sini çox güclü dəstəkləyir;
- linearlıq və zəif oyunçunun qərar sərbəstliyi və təsiri əsas dizayn riskidir;
- final və tamamlanma hissi və qısa məzmun recommendation-a ciddi təsir edir;
- bir dəfə istifadə olunan mexanikalar variety yaradır, amma mastery yaratmır;
- aydınlıq və qərar sərbəstliyi birlikdə dizayn edilməlidir.

### Orwell deep araşdırma

Orwell üzrə əsas araşdırma mərhələsi tamamlanıb:

- verified Steam məlumat toplusu: **8,549 rəy**
- müsbət: **7,735**
- mənfi: **814**
- `analysis/orwell/3. theme-analysis.md`
- `analysis/orwell/2. deep-research.md`

Əsas nəticələr:

- information selection + nəticə visibility əsas strength-dir;
- privacy/surveillance və moral ambiguity ümumən müsbət amil-dir;
- auto-highlighting və adviser guidance məntiqi nəticə çıxarma/qərar sərbəstliyi-ni zəiflədən əsas risklərdir;
- contradictory dəlil mənalı qeyri-müəyyənlik yarada bilir, amma insufficient context blind seçim-a çevrilə bilər;
- geri dönməz information qərar yalnız informed commitment olduqda sağlamdır;
- strategic qərar sərbəstliyi procedural araşdırma qərar sərbəstliyi-dən güclüdür.

### Three-game müqayisə

Tamamlanıb:

`analysis/comparisons/2. hacknet-midnight-protocol-cyber-manhunt.md`

Üç dərinlik modeli müqayisə olunur:

- Hacknet — execution dərinlik;
- Midnight Protocol — taktiki/sistem dərinliyi;
- Cyber Manhunt — information/məntiqi nəticə çıxarma dərinlik.

Əsas oyunlararası hypothesis:

> dərinlik feature sayından deyil, mənalı qərar sıxlığı-dən gəlir; təkrarçılıq isə interface növündən yox, qərar structure dəyişməyəndə yaranır.

Cyber Manhunt üçün v3 taxonomy ilə deterministik mövzu çıxış-ların lokal pipeline vasitəsilə generasiyası hələ push edilməlidir.

---


## 17.1. Hazır faylların mərkəzləşdirilmiş inventory-si

Bu bölmə yeni sessiyada “nə hazırdır?” sualının əsas istinad-udur.

### Project / methodology

- ✅ `RESEARCH_MASTER_BRIEF.md`
- ✅ `AGENTS.md`
- ✅ `README.md`
- ✅ `analysis/README.md`
- ✅ `config/games.yaml`
- ✅ `config/theme_taxonomy.yaml`
- ✅ `config/aspect_taxonomy.yaml`

### Hacknet — complete

- ✅ `data/reports/hacknet/summary.md`
- ✅ `data/reports/hacknet/theme-candidates.md`
- ✅ `data/processed/hacknet/themes/statistics.json`
- ✅ `analysis/hacknet/4. research-kickoff.md` — ilkin araşdırma planı; tamamlandıqdan sonra tarixi kontekst kimi saxlanılır
- ✅ `analysis/hacknet/3. theme-analysis.md`
- ✅ `analysis/hacknet/2. deep-research.md`
- ✅ `analysis/hacknet/1. presentation-brief.md`

### Midnight Protocol — complete

- ✅ `data/reports/midnight-protocol/summary.md`
- ✅ `data/reports/midnight-protocol/theme-candidates.md`
- ✅ `data/processed/midnight-protocol/themes/statistics.json`
- ✅ `analysis/midnight-protocol/3. theme-analysis.md`
- ✅ `analysis/midnight-protocol/2. deep-research.md`
- ✅ `analysis/midnight-protocol/1. presentation-brief.md`
- ℹ️ `analysis/midnight-protocol/4. research-kickoff.md` — historical planlama context, superseded

### Cyber Manhunt — complete

- ✅ `data/reports/cyber-manhunt/summary.md`
- ✅ `data/reports/cyber-manhunt/theme-candidates.md`
- ✅ `data/processed/cyber-manhunt/themes/statistics.json`
- ✅ `analysis/cyber-manhunt/3. theme-analysis.md`
- ✅ `analysis/cyber-manhunt/2. deep-research.md`
- ✅ `analysis/cyber-manhunt/1. presentation-brief.md`
- ℹ️ `analysis/cyber-manhunt/4. research-kickoff.md` — historical planlama context, superseded

### Completed comparisons

- ✅ `analysis/comparisons/1. hacknet-vs-midnight-protocol.md`
- ✅ `analysis/comparisons/2. hacknet-midnight-protocol-cyber-manhunt.md`
- ✅ `analysis/comparisons/3. cyber-manhunt-vs-the-operator.md`
- ✅ `analysis/comparisons/4. cyber-manhunt-vs-mainlining.md`
- ✅ `analysis/comparisons/5. orwell-vs-need-to-know.md`
- ✅ `analysis/comparisons/6. mainlining-vs-simulacra.md`
- ✅ `analysis/comparisons/7. cyber-manhunt-vs-simulacra.md`

### The Operator — complete

- ✅ verified Steam məlumat toplusu: **3,781 rəy**
- ✅ `data/reports/the-operator/summary.md`
- ✅ `data/reports/the-operator/theme-candidates.md`
- ✅ `data/processed/the-operator/themes/statistics.json`
- ✅ `analysis/the-operator/3. theme-analysis.md`
- ✅ `analysis/the-operator/2. deep-research.md`
- ✅ `analysis/the-operator/1. presentation-brief.md`
- ✅ `analysis/comparisons/3. cyber-manhunt-vs-the-operator.md`
- ℹ️ `analysis/the-operator/4. research-kickoff.md` — historical planlama context, superseded

### Orwell — complete

- ✅ verified Steam məlumat toplusu: **8,549 rəy**
- ✅ `data/reports/orwell/summary.md`
- ✅ deterministik v5 mövzu faylları repository-dədir (`data/processed/orwell/themes/`, `data/reports/orwell/theme-candidates.md`)
- ✅ `analysis/orwell/3. theme-analysis.md`
- ✅ `analysis/orwell/2. deep-research.md`
- ✅ `analysis/orwell/1. presentation-brief.md`
- ℹ️ `analysis/orwell/4. research-kickoff.md` — historical planlama context, superseded

### Need to Know — focused comparator tamamlanıb

- ✅ Steam məlumat toplusu: **272 ingilisdilli rəy**
- ✅ müsbət: **178**
- ✅ mənfi: **94**
- ✅ müsbət pay: **65.44%**
- ✅ `data/reports/need-to-know/summary.md`
- ✅ `analysis/need-to-know/4. research-kickoff.md`
- ✅ `analysis/need-to-know/3. theme-analysis.md`
- ✅ `analysis/need-to-know/2. deep-research.md`
- ✅ `analysis/need-to-know/1. presentation-brief.md`
- ✅ `analysis/comparisons/5. orwell-vs-need-to-know.md`
- ✅ lokal reproducibility run tamamlanıb
- ✅ deterministik theme artefaktları repository-dədir (`data/processed/need-to-know/themes/`, `data/reports/need-to-know/theme-candidates.md`)

Əsas nəticə:
- surveillance/privacy premise-i və moral ambiguity özü problem deyil;
- ən böyük risklər early onboarding/UI, semantic reasoning ilə exact rule acceptance arasındakı fərq, təkrarçılıq və progression tərəfindən məcbur edilən seçimlərdir;
- Orwell daha az seçim səthi ilə daha aydın consequence chain qurduğu üçün real agency hissi daha güclü görünür.

### Mainlining — complete

- ✅ verified Steam məlumat toplusu: **304 rəy**
- ✅ müsbət: **230**
- ✅ mənfi: **74**
- ✅ müsbət pay: **75.66%**
- ✅ deterministik v5 mövzu artefaktları
- ✅ 74/74 mənfi rəy üzrə məna yönümlü audit
- ✅ 39 məqsədli müsbət rəy auditi
- ✅ `analysis/mainlining/4. research-kickoff.md`
- ✅ `analysis/mainlining/3. theme-analysis.md`
- ✅ `analysis/mainlining/2. deep-research.md`
- ✅ `analysis/mainlining/1. presentation-brief.md`
- ✅ `analysis/comparisons/4. cyber-manhunt-vs-mainlining.md`

Əsas nəticələr:
- Mainlining-in əsas gücü real hacking deyil, **desktop daxilində məlumatı əlaqələndirib işi özün həll etmək competence fantasy-sidir**;
- ən böyük dizayn problemi logical evidence ilə system-accepted exact evidence arasındakı fərqdir;
- arrest feedback suspect/evidence/location komponentlərindən hansının səhv olduğunu kifayət qədər aydın göstərmir;
- `REPETITION`, `BUGS_COMPATIBILITY`, `TERMINAL_UI` və `UI_USABILITY` əsas mənfi risklərdir;
- Cyber Manhunt exact clue route, Need to Know exact rule acceptance, Mainlining isə exact evidence acceptance ilə eyni knowledge-state problemini fərqli formada təkrarlayır;
- investigation sistemi designer-in click history-sini yox, oyunçunun təsdiqlənə bilən knowledge state-ni modelləşdirməlidir.

### SIMULACRA — complete

- ✅ verified Steam məlumat toplusu: **3,209 rəy**
- ✅ müsbət: **2,905**
- ✅ mənfi: **304**
- ✅ müsbət pay: **90.53%**
- ✅ deterministik v5 mövzu artefaktları
- ✅ 304/304 mənfi rəy üzrə məna yönümlü audit
- ✅ 45 məqsədli müsbət rəy auditi
- ✅ `analysis/simulacra/4. research-kickoff.md`
- ✅ `analysis/simulacra/3. theme-analysis.md`
- ✅ `analysis/simulacra/2. deep-research.md`
- ✅ `analysis/simulacra/1. presentation-brief.md`
- ✅ `analysis/comparisons/6. mainlining-vs-simulacra.md`
- ✅ `analysis/comparisons/7. cyber-manhunt-vs-simulacra.md`

Əsas nəticələr:
- phone-as-world formatı tanış interaction qrammatikası sayəsində ilkin öyrətmə yükünü xeyli azaldır;
- şəxsi məlumatı araşdırmaq həm funksional clue, həm də emosional maraq mükafatı yaradır;
- ən güclü horror nümunələri jumpscare-dan yox, tanış interface qaydalarının pozulmasından gəlir;
- yazı/lokallaşdırma, dialoqla həddindən artıq yönləndirmə, təkrarlanan reconstruction puzzle-ları və gizli ending şərtləri əsas risklərdir;
- interface-as-world modelində realizm vizual oxşarlıqdan çox oyunçunun tanıdığı əsas affordance-ların qorunmasıdır.

### SIMULACRA 3 — complete

- ✅ verified Steam məlumat toplusu: **267 rəy**
- ✅ müsbət: **157**
- ✅ mənfi: **110**
- ✅ müsbət pay: **58.80%**
- ✅ deterministik v5 mövzu artefaktları
- ✅ 110/110 mənfi rəy üzrə məna yönümlü audit
- ✅ 43 məqsədli müsbət rəy auditi
- ✅ `analysis/simulacra-3/4. research-kickoff.md`
- ✅ `analysis/simulacra-3/3. theme-analysis.md`
- ✅ `analysis/simulacra-3/2. deep-research.md`
- ✅ `analysis/simulacra-3/1. presentation-brief.md`
- ✅ `analysis/comparisons/8. simulacra-vs-simulacra-3.md`

Əsas nəticələr:
- SIMULACRA 3 daha geniş town-scale scope və Atlas kimi formal investigation sistemi əlavə edir, amma ilk oyunun şəxsi phone intimacy-sini zəiflədir;
- phone personality, character/social graph, digital horror və choice reactivity aşağı düşür;
- Atlas knowledge organization üçün güclü istiqamətdir, lakin relevance marker-ləri observation işini avtomatlaşdıra bilər;
- house/security-camera sequence interface-native active investigation üçün güclü müsbət nümunədir;
- sequel-də əvvəl həll edilmiş QoL problemlərinin geri qayıtması və franchise thematic contract-ın dəyişməsi satisfaction-a əlavə risk yaradır.

### Final package

Hazırda yaradılmayıb:

- ✅ `analysis/final/2. market-landscape.md`
- ✅ `analysis/final/3. genre-synthesis.md`
- ✅ `analysis/final/4. design-principles.md`
- ✅ `analysis/final/5. opportunity-map.md`
- ✅ `analysis/final/6. risk-register.md`
- ✅ `analysis/final/7. concept-evaluation-framework.md`
- ✅ `analysis/final/1. executive-genre-research-report.md`

Bu inventory hər major milestone-dan sonra yenilənməlidir.

# 18. Hazırkı növbəti addım

**Araşdırma mərhələsi tamamlanıb.**

Məcburi Tier A oyunları:
- ✅ tamamlanıb

Minimum məcburi müqayisələr:
- ✅ tamamlanıb

Final research package:
- ✅ `analysis/final/2. market-landscape.md`
- ✅ `analysis/final/3. genre-synthesis.md`
- ✅ `analysis/final/4. design-principles.md`
- ✅ `analysis/final/5. opportunity-map.md`
- ✅ `analysis/final/6. risk-register.md`
- ✅ `analysis/final/7. concept-evaluation-framework.md`
- ✅ `analysis/final/1. executive-genre-research-report.md`

Praktik stop condition ödənib:
- terminal/hacking, digital investigation, surveillance və found-device istiqamətlərində həm güclü, həm contrast nümunələr var;
- recurring failure mode-lar bir neçə oyunda təkrar təsdiqlənib;
- yeni full Tier B araşdırmanın marginal dəyəri aşağıdır;
- market landscape əlavə fundamental boşluq aşkar etməyib;
- yekun hesabat hazırdır.

## Növbəti mərhələ — Product Discovery / Concept Generation

Bu artıq research mərhələsi deyil.

Tövsiyə edilən ardıcıllıq:

1. `analysis/final/5. opportunity-map.md` əsasında bir neçə fərqli concept variant yarat;
2. hər biri üçün one-line fantasy + core loop + information model yaz;
3. `analysis/final/7. concept-evaluation-framework.md` ilə müqayisə et;
4. hard gate-ləri keçən 2–3 fərqli concept saxla;
5. hər concept üçün ən böyük hipotezi ən ucuz prototiplə təkzib etməyə çalış;
6. target audience ilə role comprehension, first insight, semantic acceptance və consequence test et;
7. yalnız bundan sonra böyük production scope barədə qərar ver.

Research-in ən güclü opportunity hypothesis-i:

> **oyunçunun öz reasoning-ni semantic knowledge state kimi quran, bir neçə keçərli evidence yolunu qəbul edən, player-built knowledge graph istifadə edən və qərarın informasiya dünyasında görünən consequence yaratdığı interface-as-world investigation sistemi.**

Yeni reference oyun yalnız konkret concept üçün dəlil boşluğu yaranarsa focused şəkildə araşdırılmalıdır.

---

# 19. araşdırma-in uzunmüddətli iş axını-u

```text
Hacknet
  ↓
full theme/aspect analysis
  ↓
final per-game deep research
  ↓
Midnight Protocol
  ↓
same methodology
  ↓
Hacknet vs Midnight Protocol
  ↓
Cyber Manhunt
  ↓
Mainlining / The Operator
  ↓
comparison
  ↓
Orwell / Need to Know
  ↓
SIMULACRA series
  ↓
other representative games
  ↓
cross-game synthesis
  ↓
genre design principles
  ↓
opportunity map + risk map
  ↓
executive final report
  ↓
concept generation
  ↓
concept evaluation
  ↓
prototype validation
```

---

# 20. Son prinsip

Bu araşdırma-in uğuru çox məlumat toplamaqda deyil.

Əsas nəticə bu olmalıdır:

> **Yeni oyun ideyaları artıq “məncə belə maraqlı olar” səviyyəsində yox, oyunçu davranışı, əvvəlki oyunların uğur və uğursuzluqları, bazar təqdimatı və sistem dizaynı barədə dəlil ilə qiymətləndirilə bilsin.**

Final hesabat ideyanı bizim əvəzimizə yaratmayacaq.

O, **daha yaxşı ideya yaratmaq və pis qərarları erkən görmək üçün qərar infrastrukturu** yaradacaq.
