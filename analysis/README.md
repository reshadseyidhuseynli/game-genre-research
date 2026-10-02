# Analysis qovluğu — Oxu bələdçisi

Bu qovluq layihənin oyunlar üzrə araşdırma nəticələrini saxlayır.

Bu sənədin məqsədi repo-ya daxil olan komanda üzvünə **hansı faylı nə üçün və hansı ardıcıllıqla oxumaq lazım olduğunu** bir baxışda göstərməkdir.

---

# 1. Ən qısa oxuma yolu

Əgər məqsəd komanda görüşündə oyun haqqında sürətli məlumat almaqdır:

1. `analysis/<game>/presentation-brief.md`
2. lazım olarsa uyğun `analysis/comparisons/` sənədi

Bu yol oyunun:
- nə olduğunu;
- əsas oyunçu rolunu;
- güclü və zəif tərəflərini;
- kommersiya nəticəsi haqqında məlum siqnalları;
- uğuru və ya zəifliyi izah edən əsas hipotezləri;
- bizim layihə üçün ən vacib dərsləri

qısa formada verir.

---

# 2. Bir oyun haqqında normal araşdırma oxuma ardıcıllığı

Bir oyunu daha yaxşı anlamaq üçün tövsiyə edilən ardıcıllıq:

## 1. `presentation-brief.md`

**Məqsəd:** 2–5 dəqiqəlik komanda təqdimatı və sürətli qərar hazırlığı.

Burada yalnız ən vacib məlumat saxlanılır:
- məhsulun qısa təsviri;
- Steam rəy göstəriciləri;
- oyunçu niyə başlayır və niyə davam edir;
- əsas müsbət və mənfi cəhətlər;
- kommersiya nəticəsinin siqnalları;
- uğuru/zəifliyi izah edən hipotezlər;
- bizim üçün götürüləcək və qaçılacaq məqamlar.

Bu fayl dərin metodologiyanı və bütün sübutları təkrar etmir.

## 2. `deep-research.md`

**Məqsəd:** oyun üzrə əsas yekun araşdırma sənədi.

Bu faylda:
- məhsul və bazar konteksti;
- oyunçu rol hissi;
- əsas oyun dövrü;
- ilk sessiya;
- hekayə;
- UI/UX;
- sistem dərinliyi;
- oyunçu davranışı;
- yaradıcı məqsədləri;
- uğur və zəiflik hipotezləri;
- dizayn dərsləri;
- açıq suallar

ətraflı birləşdirilir.

Bir oyun haqqında yalnız **bir ətraflı sənəd** oxunacaqsa, bu fayl seçilməlidir.

## 3. `theme-analysis.md`

**Məqsəd:** `deep-research.md` nəticələrinin rəy məlumatları ilə necə dəstəkləndiyini yoxlamaq.

Burada:
- rəy sayı;
- oyun müddəti qrupları;
- mövzu namizədləri;
- mənfi/müsbət rəy konsentrasiyası;
- məna yönümlü yoxlama;
- metodoloji məhdudiyyətlər

yer alır.

Bu fayl əsasən nəticələrin **dəlil qatıdır**. Rəhbərlik üçün ilk oxunacaq sənəd deyil.

## 4. `research-kickoff.md`

**Məqsəd:** araşdırma başlamazdan əvvəl hansı sualların yoxlanacağını və ilkin fərziyyələri saxlamaq.

Bu fayl:
- final nəticə deyil;
- araşdırmadan əvvəlki planı göstərir;
- sonradan hansı fərziyyələrin təsdiqləndiyini və ya dəyişdiyini görmək üçün tarixi kontekstdir.

Araşdırma tamamlandıqdan sonra adətən ən sonda oxunur.

---

# 3. Hər tam araşdırılmış oyun üçün standart

Tam dərin araşdırılmış oyunun qovluğu belə olmalıdır:

```text
analysis/<game>/
├── research-kickoff.md
├── theme-analysis.md
├── deep-research.md
└── presentation-brief.md
```

Başqa aralıq qeydlər bu qovluqda saxlanmamalıdır. Lazım olan nəticələr yuxarıdakı dörd sənədə inteqrasiya edilir, tarixçə isə Git-də qalır.

---

# 4. Digər hesabatların rolu

## `data/reports/<game>/summary.md`

Avtomatik yaradılan deterministik statistik xülasədir.

Burada interpretasiya yoxdur. Məlumat toplusunun ölçüsü, müsbət/mənfi rəy sayı, oyun müddəti və digər texniki statistika üçün istifadə olunur.

## `data/reports/<game>/theme-candidates.md`

Regex/açar söz əsaslı mövzu namizədlərinin avtomatik hesabatıdır.

Bu **yekun oyunçu münasibəti** deyil. `theme-analysis.md` üçün ilkin ölçmə qatıdır.

## `analysis/comparisons/`

İki və ya daha çox oyunun eyni problem üzərində birbaşa müqayisəsidir.

Fərdi oyun hesabatlarından sonra oxunmalıdır.

Hazır müqayisələr:
- `hacknet-vs-midnight-protocol.md`
- `hacknet-midnight-protocol-cyber-manhunt.md`
- `cyber-manhunt-vs-the-operator.md`
- `orwell-vs-need-to-know.md`

## `analysis/final/`

Araşdırmanın sonunda hazırlanacaq janr səviyyəli rəhbərlik sənədləridir.

Bunlar hazır olduqda yeni oyun ideyalarının yaradılması və qiymətləndirilməsi üçün əsas qərar paketi olacaq.

---

# 5. Məqsədə görə hansı faylı oxumalı?

| Məqsəd | Oxunacaq fayl |
|---|---|
| Görüşdə oyunu 2–5 dəqiqəyə izah etmək | `presentation-brief.md` |
| Oyunu tam anlamaq | `deep-research.md` |
| Rəqəmləri və rəy dəlillərini yoxlamaq | `theme-analysis.md` |
| Araşdırma başlamazdan əvvəl nə düşündüyümüzü görmək | `research-kickoff.md` |
| Xam statistikaya baxmaq | `data/reports/<game>/summary.md` |
| Oyunları bir-biri ilə müqayisə etmək | `analysis/comparisons/` |
| Janr üzrə yekun qərar materialını oxumaq | `analysis/final/` |

---

# 6. Komanda görüşü üçün tövsiyə edilən ardıcıllıq

Bir neçə oyun təqdim ediləcəksə:

1. hər oyun üçün `presentation-brief.md`;
2. oxşar oyun qrupu üçün uyğun müqayisə sənədi;
3. mübahisəli və ya daha dərin sual çıxarsa `deep-research.md`;
4. rəqəmin mənbəyi soruşularsa `theme-analysis.md` və `data/reports/`.

Beləliklə görüşdə uzun araşdırma sənədlərini əvvəldən sona oxumağa ehtiyac qalmır.

---

# 7. Kommersiya nəticələrinin təqdimat qaydası

Satış rəqəmi yalnız etibarlı açıq mənbə olduqda dəqiq rəqəm kimi yazılır.

Satış məlumatı açıq deyilsə:
- Steam rəy həcmi;
- müsbət rəy nisbəti;
- oyun müddəti;
- sequel/DLC/Workshop kimi davamlılıq siqnalları;
- mövcud rəsmi açıqlamalar

istifadə olunur.

Belə hallarda sənəddə “satışın səbəbi” fakt kimi yox, **kommersiya nəticəsini izah edən hipotez** kimi yazılmalıdır.

Məqsəd zəif dəlildən saxta dəqiqlik yaratmamaqdır.
