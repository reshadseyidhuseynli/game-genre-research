# SIMULACRA 3 — Araşdırma kickoff

## Status

Bu sənəd SIMULACRA 3 üçün məlumat toplusu toplanmazdan əvvəl hazırlanmış tarixi kickoff sənədidir.

**Araşdırma artıq tamamlanıb.** Cari əsas sənədlər:

- `analysis/simulacra-3/theme-analysis.md`
- `analysis/simulacra-3/deep-research.md`
- `analysis/simulacra-3/presentation-brief.md`
- `analysis/comparisons/simulacra-vs-simulacra-3.md`

**Tier:** A — tam dərin araşdırma  
**Steam App ID:** `1925970`

Kickoff-un məqsədi ilkin sualları və fərziyyələri saxlamaqdır; final nəticə üçün yuxarıdakı sənədlər əsas istinaddır.

---

# 1. Niyə SIMULACRA 3 məcburi Tier A target-dir?

Master brief-də SIMULACRA 3 eyni franchise daxilində **weaker-outcome comparator** kimi müəyyən edilib.

Bu müqayisənin dəyəri çox yüksəkdir, çünki birinci SIMULACRA və üçüncü oyun:

- eyni found-phone əsas fantasy-sini;
- eyni studio xəttini;
- oxşar horror / investigation / choice təqdimatını

paylaşır, amma Steam oyunçu reaksiyası çox fərqlidir.

Cari mağaza göstəricisi:

### SIMULACRA

- Steam English reviews: təxminən **2.37k**
- müsbət: təxminən **93%**
- research API snapshot: **3,209 rəy / 90.53% müsbət**

### SIMULACRA 3

- Steam all reviews: təxminən **328**
- müsbət: təxminən **56%**
- status: **Mixed**

Bu rəqəmlər eyni filter səthi deyil və satış göstəricisi kimi istifadə olunmur.

Amma franchise daxilində kifayət qədər böyük satisfaction fərqi var ki, aşağıdakı sualı sistemli şəkildə yoxlamaq vacib olsun:

> **İlk SIMULACRA-nın yüksək nəticə göstərən phone-as-world formulundan SIMULACRA 3-də hansı dizayn və təqdimat elementləri dəyişib və həmin dəyişikliklərin hansıları daha zəif oyunçu reaksiyası ilə üst-üstə düşür?**

---

# 2. Məhsul snapshot-u

Cari Steam məlumatı:

- Ad: **SIMULACRA 3**
- Developer: **Kaigan Games**
- Publisher: **Soft Source**
- Release: **25 oktyabr 2022**
- Steam App ID: **1925970**
- Base price: **$9.99**
- Single-player
- Steam Cloud
- Partial controller support
- Steam Deck: Playable
- Steam all-review display: təxminən **328 rəy / 56% müsbət**
- əsas tags:
  - Immersive Sim
  - Interactive Fiction
  - Puzzle
  - Detective
  - Investigation
  - Horror
  - Psychological Horror
  - Choices Matter
  - Multiple Endings
  - FMV
  - Story Rich

Premise:

> Stonecreek şəhərində insanlar yoxa çıxır. Oyunçu yerli qəzetdə intern kimi jurnalist Ruby Myers-ə kömək edir və yoxa çıxmış Paul Castillo-nun telefonundan istifadə edərək işi araşdırır.

---

# 3. Birinci SIMULACRA-dan əsas struktur dəyişikliyi

Birinci oyunda:

```text
Anna-nın telefonu
→ Anna-nın şəxsi həyatı
→ dostlar / münasibətlər / şəxsi tarix
→ Anna nə oldu?
```

SIMULACRA 3-də ilkin məhsul təsvirinə görə:

```text
Paul-un telefonu
→ Stonecreek şəhəri
→ çoxsaylı yoxa çıxmalar
→ şəhər tarixi / Beldam
→ Ruby ilə paralel araşdırma
```

Əsas dəyişiklik:

> **bir insanın çox intim şəxsi mystery-sindən daha geniş town-scale investigation-a keçid.**

Bu, ilk yoxlanmalı hipotezdir.

### Hipotez

SIMULACRA-nın information reward-u:

> “Anna əslində kimdir?”

maraq hissindən gəlirdi.

SIMULACRA 3 scope-u böyüdəndə:

> **intimacy azalaraq lore / case breadth ilə əvəzlənmiş ola bilər.**

Bu final finding deyil; dataset ilə yoxlanmalıdır.

---

# 4. Rol hissi dəyişimi

### SIMULACRA

Oyunçunun kimliyi çox açıq saxlanır.

Rol:

> **“Telefon mənim əlimə keçib; mən özüm araşdırıram.”**

Bu self-insertion üçün əlverişlidir.

### SIMULACRA 3

Oyunçu:

> **yerli qəzetin internidir və Ruby Myers-ə kömək edir.**

Bu daha konkret peşəkar rol yaradır.

Potensial üstünlük:
- objective aydındır;
- real journalist-investigation fantasy yarana bilər;
- şəhər miqyaslı case üçün struktur verir.

Potensial risk:
- oyunçunun özünü “telefonu tapan şəxs” kimi hiss etməsi azalır;
- Ruby next-step giver-a çevrilə bilər;
- autonomy daha çox scripted partnership-ə bağlana bilər.

### Araşdırma sualı

> **Rolun daha konkret olması competence fantasy-ni artırır, yoxsa found-phone self-insertion immersion-unu zəiflədir?**

---

# 5. Interface-as-world baseline

Birinci SIMULACRA üzrə əsas nəticə:

> **Tanış phone interaction grammar onboarding cost-u azaldır və telefon həm narrative archive, həm investigation tool, həm də horror surface kimi işləyir.**

SIMULACRA 3 üçün yoxlanmalıdır:

- UI hələ telefon kimi təbii hiss olunurmu?
- daha çox feature/app interface-i daha funksional edib, yoxsa clutter yaradıb?
- navigation ilk oyundan yaxşıdırmı?
- real phone affordance-ları daha yaxşı saxlanılıb?
- controller/PC yönümlü dizayn phone-native hissi zəiflədibmi?
- app-lər həqiqətən ayrı reasoning funksiyası daşıyırmı?

---

# 6. Atlas mexanikası — əsas yeni test sahəsi

Public review materialında SIMULACRA 3-də **Atlas** adlı clue/progression mexanikası təsvir olunur.

İlkin model:

```text
phone-da clue tap
→ clue scan et
→ Atlas-a tətbiq et
→ location / chronology qur
→ yeni data aç
```

Bu bizim üçün çox vacibdir.

Birinci SIMULACRA-nın əsas gücü:

> məlumatı phone daxilində təbii tapmaq.

SIMULACRA 3 bunu daha formal investigation layer-ə çevirir.

Potensial üstünlük:
- clue-lar externalized olur;
- chronology və geography reasoning yaranır;
- knowledge-state daha görünən olur.

Potensial risk:
- discovery → “scan every clue” checklist-ə çevrilir;
- system acceptance yenə exact clue state tələb edir;
- phone-world ilə ayrıca meta-system arasında immersion parçalanır.

### Əsas test

> **Atlas oyunçunun knowledge graph-ını gücləndirir, yoxsa phone daxilində təbii inference-i formal checklist-ə çevirir?**

---

# 7. “Breadth vs intimacy” hipotezi

Birinci SIMULACRA:

- bir əsas missing person;
- şəxsi münasibətlər;
- birbaşa mesajlar;
- foto/video həyat tarixçəsi.

SIMULACRA 3:

- şəhər;
- jurnalist partnership;
- çoxsaylı itkinlər;
- town mythology;
- geography;
- daha geniş lore.

Bu iki müxtəlif information design modelidir.

### Model A — intimacy

```text
az target
→ çox şəxsi data
→ yüksək emosional density
```

### Model B — breadth

```text
daha geniş case/world
→ daha çox entity/location
→ daha böyük investigation graph
```

### Əsas sual

> **SIMULACRA 3 breadth artırarkən ilk oyunun intimacy reward-unı qoruyubmu?**

---

# 8. Platform fərqi xüsusi araşdırılmalıdır

Maraqlı xarici siqnal:

- Steam: təxminən **56% müsbət / Mixed**
- Apple App Store ABŞ səhifəsi: **4.5/5 / 226 rating**

Bunlar fərqli rating sistemləri, audience və platformlardır və **birbaşa müqayisə edilə bilməz**.

Amma hipotez yaratmaq üçün vacibdir:

> **Phone-as-world oyunları real mobil cihazda daha uyğun audience və daha güclü form-factor immersion əldə edə bilərmi?**

Birinci SIMULACRA review-lərində də:

> mobil cihazın PC-dən daha immersiv olduğu

fikri təkrarlanmışdı.

SIMULACRA 3 araşdırmasında platform-fit ayrıca qeyd edilməlidir.

---

# 9. Public-source ilkin risk namizədləri

Bunlar final nəticə deyil.

Steam-dəki daha zəif aggregate və digər açıq review materiallarından ilkin yoxlanmalı sahələr:

- ilk oyuna nisbətən daha zəif immersion;
- telefon UI-nin daha clunky hiss olunması;
- daha az interaktiv phone layer;
- character immediacy-nin azalması;
- uzun video-call sequence-lər;
- pacing;
- Atlas clue tətbiqinin friction-i;
- town-scale scope-un şəxsi mystery-ni zəiflətməsi;
- acting / character writing;
- sequel expectation-u;
- multiple endings və consequence;
- bug / launch polish.

Bunlar dataset audit zamanı ya təsdiqlənməli, ya da rədd edilməlidir.

---

# 10. Əsas araşdırma sualları

## 10.1. Phone immersion

- Telefon həqiqətən cihaz kimi hiss olunurmu?
- İlk oyundan hansı phone affordance-lar dəyişib?
- UI daha yaxşıdır, yoxsa daha ağırdır?
- PC vs mobile difference rəylərdə görünürmü?
- phone içində “boş” və ya dekorativ app-lər varmı?

## 10.2. Information intimacy

- Paul real insan kimi formalaşırmı?
- Telefon onun şəxsiyyətini nə qədər yaxşı daşıyır?
- Oyunçu Paul barədə curiosity hiss edirmi?
- Yoxsa telefon sadəcə şəhər işi üçün clue container-dir?

## 10.3. Breadth

- Stonecreek world-building investigation-u dərinləşdirirmi?
- çoxlu location/entity daha yaxşı knowledge graph yaradırmı?
- daha geniş scope working-memory yükünü artırırmı?

## 10.4. Atlas

- clue-ları özün müəyyən edirsənmi?
- hər şey scan-able marker kimi görünürmü?
- chronology/geography reasoning realdırmı?
- exact clue acceptance problemi varmı?
- Atlas knowledge state-i vizuallaşdırırmı?

## 10.5. Ruby partnership

- Ruby faydalı collaborator-dur?
- oyunçunun reasoning-inə reaksiya verir?
- next-step dispenser-dir?
- uzun video call-lar pacing-i pozurmu?
- qərar sərbəstliyini artırır, yoxsa azaldır?

## 10.6. Player verbs

Birinci oyun üçün Kaigan-ın sonrakı dizayn fəlsəfəsində güclü principle:

> narrative action mümkün qədər interface daxilində real player action olsun.

SIMULACRA 3-də yoxlanmalıdır:

- clue-u real göndərirsən?
- scan edirsən?
- xəritədə tətbiq edirsən?
- personajla informasiya mübadiləsi real action-dır?
- yoxsa əsasən dialogue seçimi?

## 10.7. Puzzle dərinliyi

- birinci oyundakı recurring text/image reconstruction dəyişibmi?
- Atlas yeni reasoning grammar yaradırmı?
- puzzle variety real cognitive variety-dir?
- difficulty fairness necədir?

## 10.8. Horror delivery

- interface corruption qalırmı?
- town mythology phone horror ilə necə bağlanır?
- jumpscare yenə dominantdırmı?
- qorxu clue sisteminə inteqrasiya olunubmu?
- video call / live action horror daha güclüdürmü?

## 10.9. Writing və acting

Birinci oyunun əsas risklərindən idi.

Yoxlanmalıdır:
- personaj credibility;
- dialogue naturalness;
- localisation;
- acting;
- FMV;
- Ruby/Paul relationship;
- town cast.

## 10.10. Choice və consequence

- choices həqiqətən run state dəyişirmi?
- ending şərtləri oxuna biləndirmi?
- gizli relationship gate-ləri yenə varmı?
- consequence daha tez görünürmü?
- “good ending” üçün designer moral answer problemi qalırmı?

## 10.11. Replayability

- multiple ending üçün ikinci run nə qədər fərqlidir?
- skip / rollback / save imkanları yaxşılaşıbmı?
- branch delta ilk oyundan böyükdürmü?

## 10.12. Pacing

- phone browsing / Atlas / video call nisbəti nədir?
- passiv gözləmə nə qədərdir?
- story beat-lər arasındakı interaction density necədir?
- qısa runtime-a baxmayaraq “drag” hissi varmı?

---

# 11. Birinci SIMULACRA-dan götürülən baseline

SIMULACRA üçün artıq dəlil-backed baseline var:

### Güclü
- phone-as-world;
- familiar grammar;
- information search;
- voyeuristic curiosity;
- interface corruption horror;
- low onboarding;
- short commitment;
- visible choice/consequence.

### Zəif
- writing/localization;
- voice acting;
- dialogue routing;
- recurring reconstruction puzzles;
- jumpscare overuse;
- hidden ending gates;
- replay friction;
- missing phone affordance.

SIMULACRA 3 üçün əsas məsələ:

> **bu zəifliklərin hansıları həll olunub, hansıları qalır və hansı yeni problemlər əlavə olunub?**

---

# 12. Əsas kickoff hipotezləri

## Hipotez 1 — Scope böyüdükcə intimacy zəifləyib

Town-wide mystery daha çox lore verir, amma bir şəxsin phone history-si ilə emosional yaxınlığı azalda bilər.

## Hipotez 2 — Atlas knowledge management problemini həll etmək istəyib

Bu yaxşı direction ola bilər.

Amma exact scan/apply routing yaradırsa əvvəlki oyunlarda gördüyümüz:

> player knowledge ≠ accepted system state

problemini yenidən yarada bilər.

## Hipotez 3 — Concrete journalist role self-insertion-u azaldıb

Birinci oyunun “sən kimsən?” boşluğu daha geniş self-insertion verirdi.

Intern/journalist rolu objective clarity-ni artırıb, amma personal found-phone horror hissini zəiflədə bilər.

## Hipotez 4 — Bigger production həmişə bigger immersion deyil

Daha çox:
- FMV;
- world-building;
- apps;
- sequences

ola bilər.

Amma interface density və character intimacy azalırsa ümumi immersion düşə bilər.

## Hipotez 5 — Platform fit nəticə fərqini qismən izah edə bilər

Steam və App Store reaksiyası fərqlidir.

Bu causal nəticə deyil.

Yoxlanmalıdır:
- PC control;
- phone form factor;
- review audience;
- technical performance;
- expectation differences.

## Hipotez 6 — İlk oyunun novelty-si sequel-də artıq yoxdur

2017-də found-phone premise özü yenilik idi.

2022-də üçüncü entry:
- daha yüksək expectation;
- daha az novelty;
- franchise comparison

ilə qiymətləndirilir.

Bu səbəbdən sequel yalnız eyni formula ilə kifayətlənməyə bilər.

---

# 13. Taxonomy üzrə ilkin istiqamət

v5-də relevant:

- `IMMERSION`
- `STORY_NARRATIVE`
- `INVESTIGATION_DISCOVERY`
- `CLUE_EVIDENCE_QUALITY`
- `DEDUCTION_REASONING`
- `INFORMATION_SEARCH`
- `UI_USABILITY`
- `PUZZLE_CLARITY`
- `PLAYER_AGENCY`
- `CONSEQUENCE_VISIBILITY`
- `CHOICE_REPUTATION`
- `REPETITION`
- `ENDING_CLOSURE`
- `SAVE_REPLAY`
- `LINEARITY_SCRIPTING`
- `DIALOGUE_EXPOSITION`
- `PACING_WAITING`
- `BUGS_COMPATIBILITY`
- `LOCALIZATION_WRITING`
- `SOUND_AUDIO`

SIMULACRA 3 semantic audit-də ayrıca izlənəcək anlayışlar:

```text
FOUND_DEVICE_IMMERSION
PHONE_UI_NATIVE
INFORMATION_INTIMACY
ATLAS_KNOWLEDGE_GRAPH
VIDEO_CALL_PACING
SCOPE_BREADTH
PLATFORM_FIT
SEQUEL_EXPECTATION
```

Bunlar hələ taxonomy machine label kimi əlavə edilmir.

---

# 14. Məcburi comparison

SIMULACRA 3 tamamlandıqdan sonra:

`analysis/comparisons/simulacra-vs-simulacra-3.md`

məcburi sənəddir.

Müqayisə aşağıdakı oxlarla aparılmalıdır:

| Ox | SIMULACRA baseline | SIMULACRA 3 test |
|---|---|---|
| Interface | şəxsi phone | phone + expanded systems |
| Scope | bir missing person | town-wide disappearances |
| Role | self-insert finder | journalist intern |
| Information | intimate personal data | personal + town/lore |
| Progression | apps + dialogue | apps + Atlas + Ruby |
| Horror | interface corruption | interface + town myth |
| Choice | relationship/endings | choice/endings |
| Replay | hidden gates risk | yoxlanacaq |
| Writing | əsas risk | yoxlanacaq |
| Acting | əsas risk | yoxlanacaq |
| UI | tanış, amma limitli | yoxlanacaq |
| Outcome | yüksək positive | Mixed |

SIMULACRA 2 yalnız lazım olan franchise kontekstində Tier C olaraq istifadə ediləcək.

---

# 15. Tier A iş axını

1. kickoff;
2. Steam dataset collection;
3. verification;
4. statistics;
5. deterministic theme candidates;
6. bütün mənfi rəylər mümkündürsə full semantic audit;
7. stratified positive audit;
8. external research;
9. creator intent / franchise context;
10. `theme-analysis.md`;
11. `deep-research.md`;
12. `presentation-brief.md`;
13. `simulacra-vs-simulacra-3.md`;
14. master brief yenilənməsi.

---

# 16. Lokal pipeline

Config:

```yaml
key: simulacra-3
name: SIMULACRA 3
steam_app_id: 1925970
```

Lokal:

```bash
py -m src.pipeline --game simulacra-3
py -m src.verify --game simulacra-3
py -m src.theme_pipeline --game simulacra-3
```

Generated artefaktlar push edildikdən sonra semantic audit başlayacaq.

---

# 17. Public sources

## [W1] Steam

https://store.steampowered.com/app/1925970/SIMULACRA_3/

App ID, buraxılış, developer/publisher, store positioning, cari Steam review göstəricisi.

## [W2] Apple App Store

https://apps.apple.com/us/app/simulacra-3/id1607060727

Mobil məhsul təsviri, feature-lər və platform review siqnalı.

## [W3] Kakuchopurei review

https://www.kakuchopurei.com/2022/10/simulacra-3-review-kkp/

Atlas mexanikasının public description-u və game flow haqqında ilkin xarici mənbə.

## [W4] Rojak Daily — Kaigan Games interview

https://gempak.com/en/rojakdaily/lifestyle/these-3-friends-selffunded-their-first-game-now-their-game-franchise-sold-12m-copies-81300

Studio/franchise konteksti və franchise-in geniş kommersiya traction-u.

## [W5] SIMULACRA creator-design baseline

Əvvəlki SIMULACRA araşdırmasındakı:
- Game Developer phone-UX deep dive;
- Destructoid Jeremy Ooi interview;
- 2025 Kaigan “player verbs” interview

franchise design baseline kimi istifadə ediləcək.

---

# 18. Status

**Mərhələ:** araşdırma tamamlanıb  
**Tier:** A  
**Steam target:** **1925970**  
**Verified dataset:** **267 rəy**  
**Müsbət:** **157**  
**Mənfi:** **110**  
**Müsbət pay:** **58.80%**  
**Deterministik v5 theme artefaktları:** tamamlanıb  
**Məna yönümlü audit:** 110/110 mənfi + 43 məqsədli müsbət rəy  
**Məcburi franchise comparison:** tamamlanıb
