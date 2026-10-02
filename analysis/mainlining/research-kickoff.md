# Mainlining — Araşdırma kickoff

## Status

Bu sənəd Mainlining üçün məlumat toplusu toplanmazdan əvvəl hazırlanmış kickoff sənədidir.

**Tier:** A — tam dərin araşdırma  
**Steam App ID:** `454950`

Cari mərhələ:

> **research kickoff → Steam dataset collection**

Final nəticələr bu sənəddə yazılmayacaq. Kickoff-un məqsədi hansı sualların yoxlanacağını əvvəlcədən müəyyən etmək və sonradan ilkin fərziyyələrlə real nəticələri müqayisə edə bilməkdir.

---

# 1. Niyə Mainlining növbəti əsas oyundur?

Hazırkı araşdırma artıq bir neçə fərqli model göstərib:

- **Hacknet** — terminal və haker rol hissi güclüdür, amma qərar dərinliyi və təkrarçılıq problemləri var;
- **Midnight Protocol** — daha çox taktiki qərar verir, amma sistem mürəkkəbliyi və fairness riski artır;
- **Cyber Manhunt** — məlumat axtarışı və insanları araşdırmaq maraqlıdır, amma scripted clue/progression oyunçunun bildiyini həmişə tanımır;
- **The Operator** — yüksək aydınlıq və cilalanmış alətlər verir, amma oyunçunu həddindən artıq yönləndirə bilir;
- **Orwell** — məlumat seçimi və görünən nəticə real agency yaradır, amma discovery/interpretation azadlığını məhdudlaşdırır;
- **Need to Know** — daha geniş agency vədi verir, amma bəzi seçimlər progression tərəfindən məcbur edilir və exact rule-matching reasoning-i zəiflədə bilir.

Mainlining bu xətlərin kəsişməsindədir:

> **hacking + digital investigation + evidence gathering + desktop-as-world + hüquqi/prosedur qərarı**

Əsas araşdırma sualı:

> **Mainlining Cyber Manhunt-un scripted investigation və Need to Know-un constrained-agency problemlərinə qarşı daha sərbəst “tap → əlaqələndir → sübut et → hərəkət et” modeli yarada bilirmi, yoxsa o da exact evidence və scripted solution probleminə düşür?**

---

# 2. Məhsul snapshot-u

Cari Steam mağaza məlumatı:

- Ad: **Mainlining**
- Developer: **Rebelephant**
- Steam-də cari publisher: **ReadGraves**
- Tarixi launch materiallarında publisher: **Merge Games**
- Release: **26 yanvar 2017**
- Steam App ID: **454950**
- Janr: Adventure / Indie / Simulation
- Store tags: Hacking, Point & Click, Puzzle, Typing, Programming, Story Rich və s.
- Current Steam display: təxminən **285 rəy, 77% müsbət**
- Base price: **$12.99**
- Single-player
- Demo mövcuddur

Kickstarter:

- goal: **£15,000**
- pledged: **£15,822**
- backer: **628**

Bu Kickstarter nəticəsi böyük viral hit siqnalı deyil, amma concept-in minimum crowdfunding validation aldığını göstərir.

---

# 3. Rəsmi məhsul vədi

Steam və ilkin məhsul materiallarında əsas fantasy:

> **MI7 agenti kimi şübhəlilərin kompüter və telefonlarını hack et, kimliklərini müəyyən et, dəlil topla və onları həbsə göndər.**

Oyun bütövlükdə uydurma desktop daxilində baş verir.

Əsas fəaliyyətlər:

- internet və profillərdə axtarış;
- display name / real identity əlaqələndirməsi;
- IP və location tapmaq;
- command prompt vasitəsilə sistemlərə girmək;
- file və message oxumaq;
- incriminating evidence tapmaq;
- suspect + location + evidence kombinasiyasını arrest system-ə təqdim etmək.

Rəsmi təsvir əlavə risk də qoyur:

> çox erkən hərəkət etsən daha böyük əlaqələri qaçıra bilərsən; çox geciksən suspect səni görüb qaça bilər.

Bu vacibdir, çünki kağız üzərində yalnız “doğru cavabı tap” yox, **nə vaxt commitment etmək** qərarı da vəd olunur.

---

# 4. Yaradıcı məqsədi — ilkin public-source siqnalları

Lead developer Sam Read oyunu “hacking sim point-and-click adventure” kimi təsvir edib.

Yaradıcı yanaşmada bir neçə əsas məqsəd görünür.

## 4.1. Hacker yox, dövlət cyber-investigatoru olmaq

Əksər hacking fantasy-lərində oyunçu sistemə qarşı çıxan hacker-dir.

Mainlining qəsdən digər tərəfi seçir:

> agentliyin içindən cybercrime araşdırmaq.

Bu Orwell və Need to Know-la mövzu baxımından əlaqəlidir, amma gündəlik iş daha çox **cinayət dəlili toplamaq** üzərindədir.

## 4.2. Hacking əsas məqsəd yox, araşdırma alətidir

İlkin creator materiallarına görə hacking:

- suspect data-sına giriş;
- identity;
- evidence;
- location

tapmaq üçün vasitədir.

Bu bizim üçün vacib testdir:

> **hakerlik rol hissi araşdırmaya xidmət edəndə command repetition azalırmı, yoxsa Hacknet-in “eyni əmri təkrar et” problemi yenə yaranır?**

## 4.3. Real desktop davranışına yaxın görünmək

Developer müsahibəsində maraqlı UX problemi qeyd olunur:

> real əməliyyat sisteminə bənzəyən interface istifadəçilərin real Windows vərdişlərini oyuna daşımasına səbəb olur.

Bu Hacknet-dəki semantik həqiqilik problemi ilə birbaşa əlaqəlidir.

Əsas test:

> **fictional OS nə qədər real görünürsə, oyunçu real OS davranışını nə qədər çox gözləyir?**

## 4.4. Moral commentary əsas məqsəd deyil

Sam Read ilkin müsahibədə oyunun surveillance/censorship haqqında sərt siyasi thesis-dən çox:

- hacking;
- araşdırma;
- dark humour

üzərində olduğunu vurğulayıb.

Bu Orwell və Need to Know-la vacib contrast-dır:

- Orwell-da ethical interpretation core mechanic-dir;
- Need to Know-da power/privacy dilemma geniş promise-dir;
- Mainlining-də ethics daha çox **qanuni/prosedur sərhəd və hacking üsulu** səviyyəsində ola bilər.

---

# 5. İlkin əsas oyun dövrü modeli

Public material əsasında provisional loop:

```text
case briefing
→ online araşdırma
→ identity/IP tap
→ hack / phishing / access
→ files/messages oxu
→ suspect + evidence + location əlaqələndir
→ daha çox əlaqə varmı qərar ver
→ arrest submission
→ case consequence / next case
```

Bu loop üç əvvəlki problemi eyni anda test edə bilər.

### Hacknet problemi

```text
access action repetition
```

### Cyber Manhunt problemi

```text
oyunçunun bildiyi faktı sistem yalnız exact scripted route-dan qəbul edir
```

### Need to Know problemi

```text
semantic olaraq məntiqli qərar sistemin exact acceptance rule-u ilə üst-üstə düşmür
```

Mainlining datasetində xüsusi olaraq yoxlanmalıdır:

> **oyun bir neçə məntiqli evidence-i qəbul edir, yoxsa yalnız developer-in əvvəlcədən işarələdiyi exact file / person / location kombinasiyasını?**

---

# 6. Public review-lərdən ilkin risk siqnalları

Bunlar final finding deyil; dataset audit üçün hypothesis source-dur.

Steam Community-də həm köhnə, həm yeni mənfi rəylərdə aşağıdakılar görünür:

- terminalın real command line gözləntilərinə cavab verməməsi;
- sürətli typing zamanı input itməsi;
- copy/paste və command editing rahatlığının zəifliyi;
- eyni hack əmrlərinin təkrarlanması;
- evidence submission zamanı yalnız konkret file-in qəbul edilməsi;
- alternativ, məntiqli dəlilin rədd edilməsi;
- suspect / location / evidence üçlüyünün hansı hissəsinin səhv olduğunu izah etməyən feedback;
- trial-and-error;
- bəzi progression və window-management bug-ları;
- zəif replay value;
- seçimlərin hekayəyə az təsiri.

Müsbət review siqnalları:

- desktop-as-world immersion;
- detective/hacker fantasy;
- pixel-art və parody software;
- hekayə;
- araşdırma hissi;
- qeydlər aparmaq və məlumat əlaqələndirmək;
- hacking ilə point-and-click investigation qarışığının unikallığı.

Əsas kickoff hipotezi:

> **Mainlining-in ən yaxşı hissəsi access/hacking deyil, identity + evidence + location əlaqələndirməsi ola bilər; ən böyük riski isə həmin inference-in sonunda exact developer-tagged answer tələb etməsidir.**

---

# 7. Əsas araşdırma sualları

## 7.1. Araşdırma və məntiqi nəticə çıxarma

- Oyunçu həqiqətən özü hypothesis qururmu?
- Suspect identity-ni bir neçə source-dan əlaqələndirmək lazımdırmı?
- Bir fakt üçün birdən çox keçərli dəlil yolu varmı?
- Oyunçunun artıq bildiyi məlumat game state tərəfindən tanınırmı?
- “Aha!” momentləri yaranırmı?

## 7.2. Evidence acceptance

Bu oyun üçün ən kritik suallardan biridir.

- Eyni cinayəti sübut edən birdən çox file qəbul olunurmu?
- Yalnız bir exact evidence developer tərəfindən tag olunubmu?
- Evidence doğru, location səhv olduqda feedback bunu ayırırmı?
- Partial correctness göstərilirmi?
- Wrong submission oyunçuya nə öyrədir?

## 7.3. Hacking loop

- Hacking command-ları real qərar yaradırmı?
- Yoxsa hər case:
  ping → IP → hack → files
  kimi eyni ardıcıllığa düşür?
- Yeni alətlər action grammar-i dəyişir, yoxsa yalnız yeni açardır?
- Typing rol hissi verir, yoxsa interaction tax yaradır?

## 7.4. Desktop / fictional OS

- Interface immersion yaradırmı?
- Real desktop-a bənzədiyi üçün real davranış gözləntisi yaranırmı?
- Window management faydalıdırmı?
- Notes, files və browser external working memory kimi işləyirmi?
- Copy/paste, history, editing kimi adi affordance-ların olmaması frustration yaradırmı?

## 7.5. Qərar sərbəstliyi

- Suspect-ləri hansı ardıcıllıqla araşdırmaq mümkündür?
- Həbsə nə vaxt keçmək meaningful qərardırmı?
- Alternativ suspect / evidence route-ları varmı?
- Dialogue və digər seçimlər real state dəyişirmi?
- Bir case-də səhv adamı arrest etmək nə yaradır?

## 7.6. Consequence

- Wrong arrest real consequence yaradırmı?
- Missed lead sonrakı case-i dəyişirmi?
- “Too early / too late” store promise-i actual system-dir, yoxsa narrative framing?
- Oyunçu öz qərarının dünya təsirini görürmü?

## 7.7. Story və pacing

- Story investigation-u daşıyırmı?
- Case structure variety yaradırmı?
- Story linearity problem kimi görünürmü?
- Reading və exposition decision density-ni aşağı salırmı?

## 7.8. İlkin öyrətmə

- İlk case investigation grammar-ni öyrədir?
- Terminal syntax yaddaşı əsas baryerdirmi?
- Failure-dan sonra oyunçu niyə səhv etdiyini anlayırmı?
- İlk 1–3 saat satisfaction profili necədir?

## 7.9. Texniki vəziyyət

- Launch bug-ları ilə sonrakı rəylər arasında fərq varmı?
- Input loss və window/progression bug-ları yeni rəylərdə də qalırmı?
- Platform fərqi varmı?

## 7.10. Məhsul mövqeyi

- “hacking game” expectation-u yanlış auditoriya gətirirmi?
- Oyun əslində hacking simulator-dan çox detective point-and-click-dirmi?
- Store dominant cognitive activity-ni düzgün izah edirmi?

---

# 8. Mövcud oyunlarla test ediləcək hipotezlər

## Hipotez 1 — Mainlining Cyber Manhunt-dan daha organic investigation yaradır

Səbəb:

- desktop browser;
- manual IP / identity araşdırması;
- files;
- notes;
- command prompt.

Test:

- `DEDUCTION_REASONING`
- `INFORMATION_SEARCH`
- `CLUE_EVIDENCE_QUALITY`
- `LINEARITY_SCRIPTING`

## Hipotez 2 — Exact evidence acceptance eyni scripted problem-in başqa formasıdır

Cyber Manhunt-da problem:

> exact clue/progression order.

Need to Know-da problem:

> exact rule/evidence acceptance.

Mainlining-də public review hypothesis:

> exact evidence file + exact location + exact suspect.

Əgər təsdiqlənərsə, üç oyunlu recurring principle güclənəcək:

> **Investigation game oyunçu knowledge state-i tanımalıdır; developer-selected interaction state-i yox.**

## Hipotez 3 — Desktop immersion UX expectation-u yüksəldir

Hacknet-də real terminal görünüşü real shell davranışı expectation-u yaratmışdı.

Mainlining-də eyni problem bütün OS səviyyəsində yarana bilər.

Test:

- `TERMINAL_UI`
- `UI_USABILITY`
- typing/editing/copy-paste şikayətləri
- immersion praise

## Hipotez 4 — Hacking yalnız access layer olduqda daha sağlam ola bilər

Əgər:

- hacking qısa;
- investigation dominant;
- information nəticə üçün istifadə olunur

olarsa, Hacknet-in repetition problemi azala bilər.

Əks halda eyni command sequence sadəcə hər case-in giriş ritualına çevriləcək.

## Hipotez 5 — Consequence zəifdirsə deduction dəyəri düşür

Əgər wrong arrest:

- ciddi state dəyişmir;
- yalnız retry yaradır;
- feedback vermir

sistem “investigation”dan “answer guessing”ə çevrilə bilər.

## Hipotez 6 — Mainlining “agency”dən çox “competence fantasy” verə bilər

Oyunçu:

- düzgün adamı tapır;
- düzgün dəlili tapır;
- düzgün location tapır;

amma story direction-u az dəyişir.

Bu halda məhsulun dəyəri:

> “mən seçdim”

yox,

> **“mən özüm tapdım”**

hissindən gələcək.

Bu ayrıca ölçülməlidir.

---

# 9. Taxonomy üzrə ilkin yoxlama

Mövcud v5 taxonomy böyük hissəni artıq əhatə edir:

- `HACKER_FANTASY`
- `IMMERSION`
- `TERMINAL_UI`
- `STORY_NARRATIVE`
- `INVESTIGATION_DISCOVERY`
- `REPETITION`
- `DEPTH_CHALLENGE`
- `REALISM_ACCURACY`
- `ONBOARDING_CLARITY`
- `UI_USABILITY`
- `BUGS_COMPATIBILITY`
- `PLAYER_AGENCY`
- `LINEARITY_SCRIPTING`
- `CLUE_EVIDENCE_QUALITY`
- `DEDUCTION_REASONING`
- `PUZZLE_CLARITY`
- `INFORMATION_SEARCH`

Dataset tələb edərsə yeni theme namizədləri düşünülə bilər:

```text
EVIDENCE_ACCEPTANCE
COMMAND_INPUT_FRICTION
ARREST_FEEDBACK
CASE_VARIETY
DESKTOP_WORKFLOW
```

Amma bunlar rəylər oxunmadan taxonomy-yə əlavə edilməməlidir.

---

# 10. Tier A iş axını

Mainlining tam Tier A pipeline-dan keçməlidir:

1. research kickoff;
2. Steam dataset collection;
3. verification;
4. statistik analiz;
5. deterministik mövzu namizədləri;
6. mövzu nümunələrinin məna yönümlü yoxlanması;
7. mümkün olduğu halda bütün mənfi rəylərin auditi;
8. müsbət rəylərin faydalı/recent/playtime-stratified auditi;
9. xarici mənbə araşdırması;
10. yaradıcı məqsədi;
11. `theme-analysis.md`;
12. `deep-research.md`;
13. `presentation-brief.md`;
14. uyğun comparison report;
15. `RESEARCH_MASTER_BRIEF.md` status/inventory yenilənməsi.

İlk comparison target:

> **Cyber Manhunt vs Mainlining**

Əlavə olaraq lazım gələrsə:

> **Mainlining vs Need to Know**

exact-evidence / agency mövzusunda üçlü synthesis üçün istifadə edilə bilər.

---

# 11. Məlumat toplusu komandası

Config:

```yaml
key: mainlining
name: Mainlining
steam_app_id: 454950
```

Dataset toplamaq üçün:

```bash
python -m src.pipeline --game mainlining
```

Sonra:

```bash
python -m src.verify --game mainlining
python -m src.theme_pipeline --game mainlining
```

Pipeline nəticələri push edildikdən sonra məna yönümlü audit və dərin araşdırma davam etdirilməlidir.

---

# 12. Public sources

## [W1] Steam

https://store.steampowered.com/app/454950/Mainlining/

Məhsul positioning, release, developer/publisher, tags və cari review display.

## [W2] Kickstarter

https://www.kickstarter.com/projects/mainlining/mainlining

Crowdfunding, ilkin pitch və məhsul fantasy-si.

## [W3] PC Gamer — Sam Read interview

https://www.pcgamer.com/heading-down-the-rabbit-hole-in-hacking-sim-mainlining/

“Hacking sim point-and-click adventure” positioning və dövlət-agent perspektivi.

## [W4] PCGamesN — developer interview

https://www.pcgamesn.com/mainlining/mainlining-has-you-hacking-the-hacktivists-from-the-comfort-of-somebody-elses-desktop

Desktop design, character-through-text yanaşması və real OS istifadəçi vərdişlərinin UX expectation-a təsiri.

## [W5] itch.io project page

https://samreadgraves.itch.io/mainlining

İlkin gameplay description: evidence, arrest timing və 500+ criminal framing.

## [W6] Steam Community reviews

https://steamcommunity.com/app/454950/reviews/?browsefilter=toprated

Final finding deyil; kickoff risk namizədləri və sonrakı semantic audit üçün public preview.

---

# 13. Status

**Mərhələ:** kickoff tamamlanıb  
**Tier:** A  
**Steam target:** 454950  
**Config:** repository-yə əlavə olunub  
**Dataset:** hələ repository-də yoxdur  
**Növbəti:** `python -m src.pipeline --game mainlining`
