# SIMULACRA — Təqdimat xülasəsi

> **Görüş üçün qısa nəticə:** SIMULACRA-nın əsas uğuru “telefon ekranında horror” olmaq deyil. O, real həyatdan tanış telefon davranışlarını birbaşa araşdırma və hekayə mexanikasına çevirir. Oyunçular şəxsi məlumatı qazmağı və telefonun özünün qəribələşməsini sevirlər. Əsas zəifliklər yazı/aktyorluq, dialoqla həddindən artıq yönləndirmə, təkrarlanan bərpa puzzle-ları və bir neçə saatlıq run-ı gizli münasibət şərtləri ilə ending-ə bağlamaqdır.

## 1. Oyun nədir?

| Sahə | Məlumat |
|---|---|
| Yaradıcı | Kaigan Games OÜ |
| Naşir | Kaigan Games OÜ, Soft Source |
| Buraxılış | 26 oktyabr 2017 |
| Steam App ID | `712730` |
| Janr | Horror / Detective / Point & Click / Visual Novel / Puzzle |
| Cari Steam English görünüşü | təxminən 2.37k rəy, 93% müsbət |
| Research API snapshot | **3,209 rəy, 90.53% müsbət** |
| Median oyun müddəti | **4.67 saat** |

Steam mağaza görünüşü ilə research API snapshot-u eyni filtr səthi deyil.

---

## 2. Oyunçu burada nə edir?

Oyunçu Anna adlı itkin qadının telefonunu tapır.

Rol hissi:

> **“Başqa insanın rəqəmsal həyatını açaraq onun kim olduğunu və nə baş verdiyini tapıram.”**

Əsas dövr:

```text
telefonu araşdır
→ mesaj/foto/video/email tap
→ məlumatları əlaqələndir
→ kontaktlarla danış
→ yeni app/data aç
→ qərar ver
→ nəticə gör
```

---

## 3. Niyə oynanılır?

- bir cümlədə izah olunan güclü premise;
- telefon interface-i dərhal tanışdır;
- başqa insanın şəxsi məlumatını qazmaq maraq yaradır;
- mystery + horror + social drama qarışığı;
- mesaj, foto, video və app-lər arasında clue tapmaq;
- multiple endings;
- qısa oyun müddəti;
- streamer/YouTube üçün reaksiyalı horror anları.

---

## 4. Ən vacib rəqəmlər

Dataset:

- **3,209** ingilisdilli rəy
- **2,905 müsbət**
- **304 mənfi**
- **90.53% müsbət**
- median: **4.67h**

Oyun müddətinə görə:

| Müddət | Müsbət |
|---|---:|
| 0–1h | **59.81%** |
| 1–3h | **78.83%** |
| 3–10h | **92.45%** |
| 10h+ | **95.30%** |

Bu correlation-dır, causation deyil.

Əsas deterministik risk siqnalları:

- `PACING_WAITING` — 33.3% mənfi, aşağı həcm
- `LINEARITY_SCRIPTING` — **29.3%**
- `REPETITION` — **27.9%**
- `LOCALIZATION_WRITING` — **27.6%**
- `RNG_FAIRNESS` — **26.6%**
- `DIALOGUE_EXPOSITION` — **22.2%**
- `BUGS_COMPATIBILITY` — **20.0%**
- `PUZZLE_CLARITY` — **19.5%**
- `DEPTH_CHALLENGE` — **19.2%**

Ümumi mənfi baseline yalnız **9.47%**-dir.

---

## 5. Əsas müsbət cəhətlər

1. **Telefonun oyun dünyasının özü olması**
2. **Tanış telefon davranışları — aşağı onboarding cost**
3. **Şəxsi məlumatı qazmağın yaratdığı curiosity**
4. **App-lər arasında clue əlaqələndirməsi**
5. **Telefonun özünün glitch/horror mənbəyinə çevrilməsi**
6. **Multimedia — text + photo + video + audio**
7. **Choice / multiple endings**
8. **Qısa və əlçatan təcrübə**
9. Mobil cihazda daha da güclü ola bilən immersion

---

## 6. Əsas mənfi cəhətlər

### Yazı və personajlar

- qeyri-təbii İngilis dili;
- typo/grammar;
- bəzi personajların karikatura kimi görünməsi;
- oyunçunun demək istəmədiyi dialoq variantları;
- voice acting-in audience-i bölməsi.

### Araşdırma azadlığı

Başlanğıcda:

> “telefonu özüm araşdırıram”

hissi var.

Sonra:

> “Greg/Taylor nə deyirsə onu edirəm”

hissi arta bilir.

### Puzzle təkrarçılığı

- cümlə bərpası;
- şəkil bərpası

tez-tez təkrarlanır və real deduction-dan zəifdir.

### Horror

Ən yaxşı horror:

> normal telefon qaydasının pozulması.

Ən zəif horror:

> qəfil çox yüksək səsli jumpscare.

### Ending sistemi

Bir neçə saatlıq run:
- çox erkən;
- gizli;
- kiçik görünən

relationship qərarına görə pis ending-ə kilidlənə bilir.

---

## 7. Oyun niyə bu qədər yaxşı qəbul olunub?

Qəti satış səbəbi kimi yox, dəlillə dəstəklənən hipotezlər:

1. **High-concept premise** — dərhal başa düşülür.
2. Telefon interaction-u artıq öyrənilmiş davranışdır.
3. Mystery ilə şəxsi məlumat marağı eyni dövrə düşür.
4. Horror interface-in özündən gələ bilir.
5. Qısa run giriş baryerini azaldır.
6. Multiple endings replay və video content verir.
7. Mobil və PC audience-i əhatə edir.
8. Sara Is Missing əvvəlcədən concept validation və audience yaradıb.

---

## 8. Mainlining-dən əsas fərqi

**Mainlining:**

> rəqəmsal iş desktop-u

Əsas hiss:
> “işi sübut etdim.”

**SIMULACRA:**

> şəxsi telefon

Əsas hiss:
> “bu insanın həyatını rəqəmsal izlərdən tanıdım.”

Mainlining-də UI:
- competence tool.

SIMULACRA-da UI:
- tool;
- character portrait;
- narrative archive;
- horror source.

Əsas dərs:

> **Interface-as-world modeli yalnız görünüş deyil; həmin interface-in sosial mənası da gameplay-a keçir.**

---

## 9. Cyber Manhunt-dan əsas fərqi

Cyber Manhunt:

> target haqqında məlumatı müxtəlif sistemlərdən kənardan yığırsan.

SIMULACRA:

> target-in öz şəxsi cihazının içindəsən.

Cyber Manhunt:
- daha geniş texniki/social-engineering alətləri.

SIMULACRA:
- daha az alət;
- daha yüksək şəxsi və emosional informasiya sıxlığı.

---

## 10. Bizim layihə üçün 10 dərs

1. **Tanış real-world interface onboarding-i azalda bilər.**
2. UI yalnız menyu yox, oyun dünyasının özü ola bilər.
3. Şəxsi məlumat özü reward ola bilər.
4. Familiar interface istifadə edirsənsə əsas affordance-ları saxla.
5. Discovery-ni dialogue quest routing-ə çevirmə.
6. Multimedia source-lar bir-biri ilə inference yaratmalıdır.
7. Horror ən güclü olanda interface qaydasının özünü pozur.
8. Jumpscare intensity/accessibility ayrıca idarə edilməlidir.
9. “Choices Matter” üçün ending logic oyunçu üçün oxuna bilən olmalıdır.
10. Replay istəyirsənsə branch delta və rollback imkanını artır.

---

## 11. Bir cümləlik yekun

> **SIMULACRA göstərir ki, ən güclü fictional interface oyunçunun artıq real həyatdan bildiyi cihazı istifadə edib onun normal qaydalarını həm araşdırma, həm hekayə, həm də horror üçün dəyişdirə bilən interface-dir.**

Ətraflı:
- `theme-analysis.md`
- `deep-research.md`
