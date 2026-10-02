# SIMULACRA 3 — Mövzu analizi

## 1. Məqsəd

Bu sənəd **SIMULACRA 3** üçün verified Steam review dataset-i, deterministik mövzu namizədləri və 110/110 mənfi rəy üzrə məna yönümlü audit nəticələrini birləşdirir.

Əsas sual:

> **İlk SIMULACRA-nın yüksək nəticə göstərən found-phone formulundan SIMULACRA 3-də nə dəyişib və həmin dəyişikliklərin hansıları daha zəif oyunçu reaksiyası ilə əlaqəlidir?**

---

## 2. Dataset

Snapshot:

- Steam App ID: `1925970`
- toplanma tarixi: **2026-10-02**
- ingilisdilli rəy: **267**
- müsbət: **157**
- mənfi: **110**
- müsbət payı: **58.80%**
- median rəy-anı oyun müddəti: **5.30 saat**
- orta oyun müddəti: **5.91 saat**
- müsbət rəylərdə orta: **6.10 saat**
- mənfi rəylərdə orta: **5.65 saat**
- duplicate: **0**

Oyun müddəti qrupları:

| Oyun müddəti | Rəy sayı | Müsbət payı |
|---|---:|---:|
| 0–1 saat | 16 | **37.50%** |
| 1–3 saat | 23 | **65.22%** |
| 3–10 saat | 205 | **58.05%** |
| 10h+ | 23 | **73.91%** |

İlk SIMULACRA baseline-ı:

- 3,209 rəy
- 90.53% müsbət
- median 4.67h

Bu iki dataset eyni toplama metodologiyası ilə repository-də saxlanılır və franchise daxilində ciddi satisfaction divergence göstərir.

---

## 3. Audit metodu

### Mənfi rəylər

**110/110 mənfi rəy** məna yönümlü oxunub.

Bu dataset-də mənfi rəy payı:

> **41.20%**

olduğu üçün mənfi mövzular fringe şikayət deyil; onlar məhsul reaksiyasının böyük hissəsini təşkil edir.

### Müsbət audit

**43 fərqli məqsədli müsbət rəy** oxunub:

- helpful;
- recent;
- high-playtime.

Məqsəd SIMULACRA 3-ün hansı audience üçün və hansı sistemlərdə işlədiyini də ayırmaqdır.

---

## 4. Deterministik mövzu siqnalları

Coverage:

- ən azı bir mövzu tutulan: **167 / 267**
- **62.55%**

Ümumi mənfi baseline: **41.20%**.

| Mövzu | Qeyd | Mənfi | Mənfi payı | Baseline-a nisbət |
|---|---:|---:|---:|---:|
| STORY_NARRATIVE | 116 | 58 | **50.0%** | 1.21× |
| DEPTH_CHALLENGE | 80 | 36 | 45.0% | 1.09× |
| PUZZLE_CLARITY | 77 | 33 | 42.9% | 1.04× |
| INVESTIGATION_DISCOVERY | 41 | 17 | 41.5% | 1.01× |
| IMMERSION | 34 | 16 | 47.1% | 1.14× |
| ENDING_CLOSURE | 30 | 13 | 43.3% | 1.05× |
| SOUND_AUDIO | 22 | 12 | **54.5%** | **1.32×** |
| LOCALIZATION_WRITING | 21 | 12 | **57.1%** | **1.39×** |
| UI_USABILITY | 15 | 8 | **53.3%** | **1.29×** |
| ONBOARDING_CLARITY | 13 | 7 | **53.8%** | **1.31×** |
| INFORMATION_SEARCH | 12 | 8 | **66.7%** | **1.62×** |
| REPETITION | 10 | 8 | **80.0%** | **1.94×** |
| WORLD_REACTIVITY | 7 | 5 | **71.4%** | **1.73×** |
| CONSEQUENCE_VISIBILITY | 4 | 3 | **75.0%** | **1.82×** |

Kiçik mention count-lar ehtiyatla şərh edilməlidir.

---

# 5. Əsas divergence: phone-as-person zəifləyib

İlk SIMULACRA-da telefon:

- Anna-nın şəxsi mesajlarını;
- münasibətlərini;
- fotolarını;
- videolarını;
- sosial izlərini;
- gündəlik həyatını

daşıyırdı.

Oyunçunun əsas discovery reward-u:

> **“Anna kimdir?”**

idi.

SIMULACRA 3-də mənfi rəylərdə təkrarlanan ən güclü fikir:

> Paul-un telefonu real bir insanın istifadə etdiyi zəngin şəxsi cihaz kimi hiss olunmur.

Təkrarlanan şikayətlər:

- az app;
- az kontakt;
- az secondary content;
- telefonun “personality”sinin olmaması;
- flavor content-in gameplay-a nadir hallarda bağlanması;
- Paul haqqında daha az şəxsi discovery;
- phone-un clue container kimi hiss olunması.

### Nəticə

> **Found-phone oyununda telefon yalnız level geometry deyil; cihaz sahibinin character modelidir.**

Bu qat zəifləyəndə interface-as-world immersion da zəifləyir.

**Etibarlılıq: High**

---

# 6. Breadth intimacy-ni əvəz edib

SIMULACRA 3 scope-u böyüdür:

- Stonecreek;
- town history;
- çoxsaylı yoxa çıxmalar;
- Beldam;
- location trail;
- geniş paranormal lore.

Müsbət audience bu istiqaməti sevir:

- şəhər mystery-si;
- folklore;
- Stonecreek world-building;
- paranormal investigation.

Mənfi audience isə hiss edir ki:

> geniş world-building bir insanı tanımağın yaratdığı şəxsi marağı əvəz edə bilməyib.

### Model

Birinci SIMULACRA:

```text
dar scope
→ yüksək şəxsi məlumat sıxlığı
→ güclü character intimacy
```

SIMULACRA 3:

```text
geniş scope
→ daha çox lore/location
→ daha aşağı şəxsi məlumat sıxlığı
```

### Principle

> **Investigation breadth character intimacy-nin substitutu deyil.**

**Etibarlılıq: High**

---

# 7. Atlas: yaxşı ideya, qarışıq sistem rolu

Atlas SIMULACRA 3-də ən çox müsbət qeyd alan yeni sistemlərdəndir.

Müsbət rəylərdə:

- location unlocking;
- xəritə üzərində clue tətbiqi;
- town exploration;
- chronology/geography hissi

bəyənilir.

Bu vacib inkişafdır:

> phone archive-dən formal knowledge representation-a keçid.

Amma mənfi auditdə üç problem görünür.

### 7.1. Diegetic məntiq

Bəzi oyunçular soruşur:

> niyə Paul bütün vacib məlumatı süni şəkildə Atlas arxasında puzzle kimi kilidləyib?

Yəni sistem funksional olsa da world logic ilə tam təbii hiss olunmaya bilər.

### 7.2. Investigation shortcut

Clue yanında scan/magnifying indicator:

> “özüm relevance tapıram”

hissini:

> “indicator görünənədək scroll edirəm”

modelinə çevirə bilir.

### 7.3. Complexity inconsistency

Bəzi oyunçular Atlas-ı:
- yaxşı;
- aydın;
- fun

hesab edir.

Digərləri:
- confusing;
- arbitrary;
- obscure

hesab edir.

### Nəticə

> **Knowledge graph sistemi yaxşı opportunity-dir, amma relevance discovery-ni avtomatik marker-lərə həddindən artıq bağlamaq deduction-u zəiflədə bilər.**

**Etibarlılıq: High**

---

# 8. Investigation discovery-nin keyfiyyəti niyə düşüb?

Deterministik `INFORMATION_SEARCH`:

- 12 mention;
- **66.7% mənfi**
- baseline-dan **1.62×**.

Həcmi kiçikdir, amma semantic audit çox güclü dəstək verir.

Mənfi rəylərdə:

- “telefonu həqiqətən araşdırmıram”;
- “correct icon-a basıram”;
- “məlumat tapmaq reward deyil”;
- “phone-un qalan hissəsi mənasızdır”;
- “birinci oyunda şəxsi məlumatı qazırdım, burada task yerinə yetirirəm”

kimi pattern-lər var.

### Əsas fərq

Birinci oyun:

> **information discovery özü gameplay reward idi.**

Üçüncü oyun:

> **information daha çox progression token-ə çevrilib.**

**Etibarlılıq: High**

---

# 9. Ruby: collaborator-dan tutorial character riskinə

SIMULACRA 3 daha konkret rol verir:

> jurnalist intern + Ruby Myers ilə əməkdaşlıq.

Müsbət tərəf:

- objective aydındır;
- player tək deyil;
- dialogue vasitəsilə context gəlir;
- bəzi oyunçular Ruby-ni daha relatable hesab edir.

Mənfi tərəf:

- Ruby tez-tez bütün run boyu dominant contact-dır;
- digər contact-lar daha az inkişaf edir;
- “tutorial character that never stops” hissi yaranır;
- phone-un social network-i daralır;
- player self-insertion azalır.

Birinci SIMULACRA-da Greg, Taylor, Ashley və digərləri:

> fərqli social motives

yaradırdı.

SIMULACRA 3-də Ruby:

> böyük hissədə tək social hub

olur.

### Principle

> **NPC guidance clarity yarada bilər, amma social graph-ı bir personaja sıxışdırarsa investigation world-u kiçilə bilər.**

**Etibarlılıq: High**

---

# 10. Character density və emotional stake

110 mənfi rəydə ən davamlı şikayətlərdən:

- personajlar bland;
- az personaj var;
- personajlar gec təqdim olunur;
- relationship azdır;
- ölən/qurtarılan insanlara attachment yaranmır;
- Paul özü kifayət qədər dərin tanınmır.

Bu franchise divergence üçün mərkəzi nəticədir.

İlk SIMULACRA-da hətta disliked personajlar:

> emosional reaksiya yaradırdı.

SIMULACRA 3-də:

> bəzi oyunçular “care etmirəm” deyir.

### Principle

> **Strong character reaction — hətta mənfi reaction — bland neutrality-dən daha çox narrative energy yaradır.**

---

# 11. Choice sistemi: daha çox görünüş, daha az hiss olunan təsir

Bir sıra müsbət rəylər:

- daha çox response;
- müəyyən ending variation;
- call input

kimi elementləri bəyənir.

Amma mənfi auditdə çoxlu oyunçu deyir:

- seçdiyim cavabdan sonra seçmədiyim cavabı da oyun deyir;
- dialogue nəticəsi dəyişmir;
- ending əsasən finala yaxın az sayda qərara bağlanır;
- çox seçim cosmetic hiss olunur;
- auto-selected responses urgency-ni öldürür.

`WORLD_REACTIVITY` və `CONSEQUENCE_VISIBILITY` az mention-lı olsa da yüksək mənfi konsentrasiya göstərir.

### Nəticə

> **Choice count agency deyil; oyunçunun bir variantı seçməklə başqa state-ləri bağlaması agency-dir.**

**Etibarlılıq: High**

---

# 12. İlk oyunun ending problemi burada başqa formada dəyişib

SIMULACRA 1:

- hidden relationship gate;
- “bir erkən seçim bütün ending-i korlayır” problemi.

SIMULACRA 3:

- bəzi oyunçular good ending-i ilk run-da rahat alır;
- choice path-ləri daha az fərqlənir;
- replay motivasiyası aşağıdır.

Yəni franchise bir riskdən digərinə keçir:

### SIMULACRA 1

> **too hidden / too punishing**

### SIMULACRA 3

> **too weakly differentiated / too low-stakes**

### Principle

> **Branching system həm fair, həm də meaningfully divergent olmalıdır.**

---

# 13. Replayability və fast-forward regression

Birinci SIMULACRA New Game+ ilə message sürətini artırırdı.

SIMULACRA 3 mənfi rəylərində təkrarlanan şikayətlər:

- fast-forward yoxdur;
- scene skip zəifdir;
- uzun video/dialogue təkrar baxılmalıdır;
- multiple ending olsa da replay baha başa gəlir.

Bu franchise regression kimi qəbul olunur, çünki feature əvvəlki oyunda var idi.

### Principle

> **Sequel-də əvvəl həll edilmiş friction-i geri gətirmək yeni problemdən daha sərt qəbul oluna bilər.**

**Etibarlılıq: High**

---

# 14. Horror: technology horror-dan generic paranormal horror-a

Birinci SIMULACRA-nın əsas güclü horror pattern-i:

> **tanış telefon qaydalarının korlanması.**

SIMULACRA 3 mənfi rəylərində isə:

- horror çox azdır;
- jumpscare azdır;
- ambience zəifdir;
- phone glitch azdır;
- antagonist “ghost/demon” kimi görünür;
- digital/social theme ilə əlaqə zəifləyib.

Əsas franchise tension:

> əvvəlki oyunlarda təhlükə digital həyatın içindən çıxırdı.

SIMULACRA 3-də:

> digital phone daha çox paranormal hadisəyə baxmaq üçün vasitə kimi işləyir.

### Nəticə

> **Horror theme ilə interaction medium eyni mənbədən gəlməyəndə phone-as-world konsepti zəifləyə bilər.**

**Etibarlılıq: High**

---

# 15. Social commentary-nin azalması

Birinci oyun:

- dating;
- online identity;
- social media;
- digital persona.

SIMULACRA 2:
- influencer culture;
- fame;
- social media.

SIMULACRA 3:
- gentrification;
- town folklore;
- local myth;
- ghost-like antagonist.

Bəzi oyunçular yeni mövzunu bəyənir.

Amma franchise fan-larının böyük hissəsi üçün:

> digital-social commentary franchise identity-nin öz hissəsi idi.

### Principle

> **Series identity yalnız mechanic deyil; recurring thematic contract da ola bilər.**

---

# 16. Puzzle dizaynı: iki əks şikayət

Mənfi auditdə puzzle-lar həm:

- həddindən artıq asan;
- hand-held;
- obvious

həm də:

- obscure;
- confusing;
- hint-less;
- arbitrary

kimi tənqid olunur.

Bu ziddiyyət bir problemə işarə edir:

> difficulty curve deyil, puzzle language consistency zəifdir.

Əgər bir puzzle:
- relevance marker ilə hand-held,
digəri:
- heç bir sistem dilinə uyğun olmayan hidden rule

istifadə edirsə, oyunçuda transferable learning yaranmır.

### Principle

> **Puzzle difficulty-dən əvvəl puzzle grammar consistent olmalıdır.**

---

# 17. Single-use mechanic riski

Mənfi rəylərdə:

- yeni mexanika öyrədilir;
- yalnız bir dəfə işlədilir;
- sonra başqa mexanika gəlir

şikayəti var.

Məsələn:
- trace;
- dark-mode-like interaction;
- interactive video;
- Vanguard;
- house camera sequence.

Bəzi sequence-lər ayrıca bəyənilir.

Amma sistem mastery-si yaratmır.

### Principle

> **Set-piece variety mastery-nin əvəzi deyil.**

Bu The Operator-da görülən “single-use mechanics” tension-u ilə uyğun gəlir.

---

# 18. House / camera sequence: ən yaxşı yeni set-piece

Həm müsbət, həm mənfi rəylərdə belə:

> Paul-un evi / security camera hissəsi

tez-tez yaxşı nümunə kimi ayrılır.

Niyə?

- real-time tension;
- interface action;
- spatial threat;
- oyunçunun diqqəti;
- telefon/remote-view role fantasy

bir yerdə işləyir.

Bu sequence SIMULACRA 3-ün ümumi zəifliyindən fərqli olaraq:

> **player action ilə horror action-ı yenidən birləşdirir.**

### Opportunity

Bu franchise üçün ən yaxşı gələcək istiqamət:

> static phone reading-dən çox interface-native active investigation sequence-ləridir.

---

# 19. Writing və acting

`LOCALIZATION_WRITING`:

- 21 mention;
- 57.1% mənfi;
- baseline-dan 1.39×.

Mənfi audit:
- typos;
- flat dialogue;
- over-exposition;
- character voice zəifliyi;
- acting inconsistency;
- obvious green screen;
- abrupt edit.

Müsbət audience isə bəzi aktyorları və story-ni yaxşı qiymətləndirir.

Bu tam universal failure deyil.

Amma franchise context-də əsas problem:

> production ambition yüksəlib, credibility eyni templə yüksəlməyib.

---

# 20. Audio və polish

`SOUND_AUDIO`:

- 22 mention;
- 54.5% mənfi.

Təkrarlanan şikayətlər:
- dialogue çox sakit;
- başqa video çox yüksək;
- ambience az;
- əvvəlki oyunlardakı background horror sound-ları yoxdur;
- audio mix inconsistent.

Horror oyunda audio yalnız polish deyil.

> **threat perception system**-dir.

Bu qat zəifləyəndə horror intensity də düşür.

---

# 21. UI usability və phone personality

Mənfi rəylərdə:

- UI daha az intuitiv;
- phone “real istifadə olunmuş cihaz” kimi hiss olunmur;
- app count az;
- bəzi call funksiyaları artıq heç nə etmir;
- Easter egg / random response-lar azalıb;
- Atlas çox dominantdır.

Bu “content quantity”dən daha böyük məsələdir.

Birinci oyunun phone illusion-u:
- lazımsız görünən məlumat;
- random detail;
- işləməyən, amma believable functionality;
- incidental content

ilə yaranırdı.

### Principle

> **Diegetic interface-də “lazımsız” detail bəzən immersion üçün məhsuldar lazımsızlıqdır.**

---

# 22. Onboarding paradoksu

0–1h müsbət:

- SIMULACRA: **59.81%**
- SIMULACRA 3: **37.50%**

Birinci oyunda phone grammar dərhal işləyirdi.

Üçüncü oyunda:

- rol setup-u;
- Atlas;
- town system;
- guidance;
- puzzle grammar

daha çox izah tələb edir.

Yəni daha çox formal system:

> familiar phone onboarding advantage-nı qismən itirir.

### Principle

> **Familiar shell içində unfamiliar meta-system əlavə edəndə onboarding üstünlüyü avtomatik qorunmur.**

---

# 23. Sequel expectation penalty

110 mənfi rəyin çox böyük hissəsi birbaşa:

> “1 və 2 ilə müqayisədə…”

deyir.

Bu vacibdir.

SIMULACRA 3 yalnız standalone məhsul kimi qiymətləndirilmir.

O, əvvəlki oyunların:
- horror intensity;
- phone richness;
- app variety;
- character density;
- choice reactivity;
- replay feature-ləri

ilə müqayisə olunur.

### Nəticə

> **Sequel minimum baseline-i sıfırdan yox, əvvəlki məhsulun həll etdiyi problemlərdən başlayır.**

---

# 24. Müsbət audience kimdir?

Müsbət audit göstərir ki SIMULACRA 3 aşağıdakı audience üçün işləyə bilər:

- paranormal mystery sevən;
- horror-dan çox detective puzzle istəyən;
- Stonecreek lore-unı maraqlı tapan;
- daha az jumpscare istəyən;
- Atlas/location mechanic-i sevən;
- franchise müqayisəsini əsas etməyən;
- exposition-heavy mystery-dən narahat olmayan.

Bu çox vacibdir:

> məhsul “heç kim üçün işləmir” deyil.

Əsas problem:
- positioning;
- franchise contract;
- system cohesion.

---

# 25. Uğur pattern-ləri

1. Atlas kimi spatial knowledge layer.
2. Stonecreek world-building.
3. Paranormal investigation audience üçün daha uyğun ton.
4. House/security-camera sequence.
5. Bəzi daha aktiv interactive-video anları.
6. Daha konkret journalist role.
7. Bəzi oyunçular üçün daha likable Ruby/Paul.
8. Qısa runtime.
9. Phone mystery fundamental hook-unun hələ işləməsi.

---

# 26. Uğursuzluq pattern-ləri

1. Phone personality və personal-data density itkisi.
2. Az və zəif inkişaf etmiş character graph.
3. Ruby-nin həddən artıq central guidance rolu.
4. Information discovery-nin marker/checklist hissinə keçməsi.
5. Digital horror → generic paranormal horror shift.
6. Social commentary contract-ının zəifləməsi.
7. Puzzle grammar inconsistency.
8. Single-use mechanics.
9. Choices-in cosmetic hiss olunması.
10. Replay üçün fast-forward/skip regression.
11. Audio mixing və polish.
12. UI friction.
13. Exposition-heavy pacing.
14. Ending payoff.
15. Sequel expectation mismatch.

---

# 27. Bizim layihə üçün dərslər

1. **Found-device-də device owner character olmalıdır.**
2. Breadth artıranda intimacy ayrıca qorunmalıdır.
3. Knowledge graph relevance discovery-ni əvəz etməməlidir.
4. Guidance collaborator olmalıdır, quest marker yox.
5. Social graph character density yaradır; bir NPC-yə yığma.
6. Diegetic “flavor” content həmişə waste deyil.
7. Horror medium-un öz qaydalarından çıxanda daha coherent olur.
8. Choice sayı deyil, state divergence agency yaradır.
9. Puzzle grammar consistency difficulty-dən vacibdir.
10. Set-piece variety mastery yaratmır.
11. Sequel əvvəl həll edilmiş usability problemlərini geri qaytarmamalıdır.
12. Familiar interface + unfamiliar meta-system onboarding cost-u yenidən artırır.
13. Franchise thematic contract mechanic qədər vacib ola bilər.
14. Active interface-native sequence-lər passiv exposition-dan daha güclüdür.
15. Information reward progression token yox, discovery kimi hiss olunmalıdır.

---

# 28. Status

**110/110 mənfi audit:** tamamlanıb  
**Müsbət məqsədli audit:** 43 fərqli rəy  
**Deterministik v5 scan:** tamamlanıb  
**Növbəti:** `deep-research.md` və franchise comparison
