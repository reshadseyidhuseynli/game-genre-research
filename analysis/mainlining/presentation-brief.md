# Mainlining — Təqdimat xülasəsi

> **Görüş üçün qısa nəticə:** Mainlining ən yaxşı halda “hacking oyunu” yox, rəqəmsal detektiv point-and-click oyunudur. Gücü desktop içində clue-ları özün birləşdirib suspect + evidence + location nəticəsinə gəlməkdir. Əsas zəifliyi isə odur ki, oyunçu məntiqli cavab versə belə sistem çox vaxt yalnız developer-in konkret seçdiyi evidence obyektini qəbul edir; bu, deduction-u trial-and-error-a çevirə bilir.

## 1. Oyun nədir?

| Sahə | Məlumat |
|---|---|
| Yaradıcı | Rebelephant |
| Cari publisher | ReadGraves |
| Buraxılış | 26 yanvar 2017 |
| Steam App ID | `454950` |
| Janr | Adventure / Indie / Simulation / Point & Click / Hacking |
| Cari Steam store | 285 rəy, 77% müsbət |
| Research API snapshot | 304 rəy, 75.66% müsbət |
| Median oyun müddəti | 4.82 saat |

Kickstarter:
- £15,822 / £15,000;
- 628 backer.

Steam store göstəricisi ilə API snapshot eyni filtr səthi deyil.

---

## 2. Oyunçu kimdir?

Oyunçu MI7 agentidir.

Rol hissi:

> **“Rəqəmsal izlərdən cinayətkarın kim olduğunu, harada olduğunu və onu hansı dəlillə həbs edə biləcəyimi özüm tapıram.”**

Əsas dövr:

```text
case
→ internetdə axtarış
→ IP / identity tap
→ hack
→ file/chat/email oxu
→ suspect + evidence + location qur
→ arrest
→ nəticə
```

---

## 3. Niyə oynanılır?

- desktop-as-world formatı;
- hacker/detective fantasy-si;
- məlumat parçalarını birləşdirmək;
- real proqramları xatırladan parody tətbiqlər;
- pixel art;
- hekayə və yumor;
- ağır texniki bilik tələb etməyən hacking;
- point-and-click puzzle strukturu.

Ən yaxşı hiss:

> **“Cavabı oyun mənə demədi; mən məlumatlardan özüm çıxardım.”**

---

## 4. Ən vacib rəqəmlər

Dataset:

- 304 rəy
- 230 müsbət
- 74 mənfi
- **75.66% müsbət**
- 0 duplicate

Oyun müddətinə görə:

| Müddət | Müsbət |
|---|---:|
| 0–1h | **34.78%** |
| 1–3h | **62.50%** |
| 3–10h | **80.10%** |
| 10h+ | **96.88%** |

Bu correlation-dır, causation deyil.

Əsas deterministik siqnallar:

- `REPETITION` — **66.7% mənfi**
- `BUGS_COMPATIBILITY` — **52.5% mənfi**
- `ONBOARDING_CLARITY` — **47.1% mənfi**
- `TERMINAL_UI` — **39.4% mənfi**
- `UI_USABILITY` — **37.8% mənfi**
- `CLUE_EVIDENCE_QUALITY` — **34.0% mənfi**
- `DEPTH_CHALLENGE` — yalnız **13.9% mənfi**
- `INVESTIGATION_DISCOVERY` — **20.4% mənfi**

Yəni problem “araşdırma maraqsızdır” deyil.

---

## 5. Əsas müsbət cəhətlər

1. **Desktop içində araşdırma rol hissi**
2. **Clue və identity əlaqələndirməsi**
3. **Yüngül və əlçatan hacking**
4. **“Özüm tapdım” competence hissi**
5. **Pixel art və OS parody-ləri**
6. **E-poçt/chat/file üzərindən hekayə**
7. **Yumor və atmosfer**
8. Bəzi case-lərdə bir neçə mümkün arrest/outcome

---

## 6. Əsas mənfi cəhətlər

### Exact evidence problemi

Oyunçu daha güclü dəlil tapsa belə:

> sistem yalnız konkret file-i qəbul edə bilir.

Bu, ən vacib struktur problemdir.

### Səhv feedback

Arrest:

```text
suspect + evidence + location
```

kombinasiyasıdır.

Səhv olanda sistem çox vaxt hansının səhv olduğunu demir.

Nəticə:

> reasoning → trial-and-error.

### Terminal/UI

- copy/paste yoxdur;
- cursor editing zəifdir;
- sürətli typing itə bilir;
- command history zəifdir;
- qeyri-dəqiq error mesajları;
- pəncərə idarəsi və notepad məhduddur.

### Təkrarçılıq

```text
website
→ ping
→ hack
→ list
→ download
→ repeat
```

Yeni case həmişə yeni qərar forması yaratmır.

### Bug-lar

Crash/freeze/input/save/progression problemləri yalnız launch rəylərində deyil, daha yeni rəylərdə də görünür.

---

## 7. Oyun əslində hacking simulyasiyasıdırmı?

Tam deyil.

Müsbət audience bunu qəbul edir:

> **“Bu Hacknet deyil; hacking elementli point-and-click detektiv oyunudur.”**

Narazı audience isə store tags və təqdimatdan daha dərin hacking gözləyir.

Əsas dərs:

> **Məhsulun dominant fəaliyyəti marketinqdə düzgün adlandırılmalıdır.**

---

## 8. Mainlining-in ən vacib dizayn problemi

Üç oyun artıq eyni problemi göstərir:

### Cyber Manhunt
```text
oyunçu cavabı bilir
≠
scripted clue trigger yoxdur
```

### Need to Know
```text
oyunçu məntiqli qiymətləndirir
≠
exact rule/evidence qəbul edilmir
```

### Mainlining
```text
oyunçu cinayəti sübut edir
≠
exact evidence/person/location kombinasiyası deyil
```

Cross-game principle:

> **Investigation sistemi oyunçunun click history-sini yox, knowledge state-ni tanımalıdır.**

---

## 9. Cyber Manhunt-dan əsas fərqi

**Cyber Manhunt**
- daha geniş məlumat mənbələri;
- social engineering;
- daha uzun və hekayə-ağır;
- əsas risk: scripted clue progression.

**Mainlining**
- daha manual desktop hissi;
- daha az hand-holding;
- daha qısa;
- əsas risk: final evidence submission-un exact olması.

Əsas fərq:

> **Cyber Manhunt cavaba hansı yolla çatdığını həddindən artıq idarə edir; Mainlining isə cavabı necə formal təqdim etdiyini həddindən artıq idarə edir.**

---

## 10. Bizim layihə üçün 10 dərs

1. **Knowledge state first-class state olsun.**
2. Eyni faktı sübut edən birdən çox source qəbul et.
3. Evidence file ID deyil, semantic fact olsun.
4. Wrong answer hansı komponentin problemli olduğunu hiss etdirsin.
5. Failure tam cavabı deməsin, amma öyrətsin.
6. Terminal varsa basic editing/history/copy affordance-ları ver.
7. Fictional OS oyunçunun external memory-si olsun.
8. Notes, source və case history persistent olsun.
9. Hacking access ritualı deyil, qərar sistemi olsun.
10. Marketinqdə sandbox/free investigation yalnız sistem həqiqətən bunu verirsə vəd edilsin.

---

## 11. Bir cümləlik yekun

> **Mainlining göstərir ki, digital investigation üçün ən güclü fantasy “mən özüm tapdım” hissidir; sistem həmin nəticəni tanımayanda bütün detektiv fantasy çox tez “designer-in gizli cavabını tap” tapşırığına çevrilir.**

Ətraflı:
- `theme-analysis.md`
- `deep-research.md`
