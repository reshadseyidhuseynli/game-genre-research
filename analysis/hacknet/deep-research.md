# Hacknet — Dərin araşdırma

## Sənədin məqsədi

Bu sənəd Hacknet oyununun sadəcə statistik xülasəsi deyil. Məqsəd oyunun **niyə maraq yaratdığını, oyunçuların hansı hissələri sevdiyini, hansı hissələrin onları itirdiyini və eyni janrda yeni oyun hazırlayarkən hansı dizayn qərarlarından dərs çıxarmaq lazım olduğunu** anlamaqdır.

Bu sənəddə üç məlumat tipi ayrılır:

- **Faktiki məlumat** — Steam review dataset-i, metadata və developer tərəfindən verilən məlumatlar.
- **Oyunçu rəylərindən müşahidə** — seçilmiş helpful, recent, low-playtime və high-playtime review nümunələrində təkrarlanan mövzular.
- **Dizayn nəticəsi / hipotez** — yuxarıdakı məlumatlardan çıxarılan, lakin digər oyunlarla müqayisə olunana qədər janr qaydası kimi qəbul edilməməli nəticələr.

Deterministik dataset xülasəsi ayrıca fayldadır:

`data/reports/hacknet/summary.md`

Bu sənəd isə həmin datanın **məna və game-design baxımından şərhidir**.

---

# 1. Araşdırmada istifadə olunan məlumatlar

## 1.1. Daxili Steam dataset-i

Repository-də Hacknet üçün:

- 11,773 English Steam review
- 11,773 unique review
- 11,082 positive review
- 691 negative review
- 94.13% positive ratio
- 27 review-da `playtime_at_review` məlumatı yoxdur
- 2,160 review çox qısadır
- 20 review boşdur

Dataset snapshot-ı 2026-10-01 — 2026-10-02 tarixlərində toplanıb.

Əsas fayllar:

- `data/processed/hacknet/reviews.jsonl`
- `data/processed/hacknet/reviews.csv`
- `data/processed/hacknet/statistics.json`
- `data/processed/hacknet/samples/helpful_positive.csv`
- `data/processed/hacknet/samples/helpful_negative.csv`
- `data/processed/hacknet/samples/recent_positive.csv`
- `data/processed/hacknet/samples/recent_negative.csv`
- `data/processed/hacknet/samples/low_playtime.csv`
- `data/processed/hacknet/samples/high_playtime.csv`

## 1.2. Xarici mənbələr

Araşdırmada əlavə olaraq bunlardan istifadə olunub:

- Hacknet developer Matt Trobbiani ilə müsahibələr
- Fellow Traveller rəsmi press kit
- Steam store və Steam community materialları
- Reddit /r/Hacknet müzakirələri
- GameSpot və digər professional review-lər
- Hacknet: Labyrinths haqqında materiallar

Mənbələrin tam siyahısı sənədin sonunda verilib.

## 1.3. Vacib məhdudiyyət

Hazırda bütün 11,773 review üçün avtomatik **theme classification** aparılmayıb.

Ona görə bu sənəddə:

> “Repetition review-lərin X%-ində qeyd olunub”

kimi dəqiq theme faizləri verilmir.

Hazırkı keyfiyyət nəticələri əsasən:

- ən helpful positive review-lər,
- ən helpful negative review-lər,
- ən yeni review-lər,
- çox aşağı playtime review-ləri,
- çox yüksək playtime review-ləri

və xarici community/professional mənbələr üzərində qurulub.

Bu, güclü pattern-ləri görmək üçün kifayətdir, amma sonrakı mərhələdə bütün dataset üzrə aspect/theme analysis aparılmalıdır.

---

# 2. Hacknet əslində necə oyundur?

Hacknet özünü “terminal-based hacking simulator” kimi təqdim edir, amma oyunçu təcrübəsi baxımından onu daha düzgün belə təsvir etmək olar:

> **Terminal interfeysi daxilində oynanan story-driven hacking adventure / investigation oyunu.**

Oyun real hacking-i tam simulyasiya etmir.

Əsas loop təxminən belədir:

1. email və ya missiya alınır;
2. hədəf sistem müəyyən edilir;
3. sistem scan/probe edilir;
4. açıq portlara uyğun hacking tool-ları işə salınır;
5. admin/root access əldə edilir;
6. filesystem araşdırılır;
7. fayl, password, log və ya başqa informasiya tapılır;
8. missiyaya uyğun olaraq fayl oxunur, silinir, dəyişdirilir və ya köçürülür;
9. növbəti node və ya story məlumatı açılır.

Mexaniki olaraq sadədir.

Hacknet-in əsas gücü mexanikanın özü yox, həmin mexanikanın yaratdığı **fantasy**-dir.

---

# 3. Oyunun ən vacib dizayn qərarı: “real hacker olmaq” yox, “özünü hacker kimi hiss etmək”

Developer Matt Trobbiani Hacknet-in başlanğıcını izah edərkən deyir ki, oyun 48 saatlıq “UIs and Interfaces” mövzulu game jam-dan yaranıb.

İlk mərhələdə mexanika tam müəyyən edilməmişdi. Onun əsas qaydası bu idi:

> etdiyim hər şey oyunçunun özünü hacker kimi hiss etməsinə xidmət etməlidir.

Bu, Hacknet-i anlamaq üçün ən vacib məlumatdır.

Yəni prioritet belə olmayıb:

```text
real hacking simulation
→ gameplay
→ presentation
```

Əksinə:

```text
"hacker kimi hiss etmək"
→ uyğun interface
→ uyğun command-lar
→ uyğun story
→ uyğun səs/musiqi
→ uyğun hacking abstraction
```

Bu yanaşma Steam review-lərində də çox aydın görünür.

Bir çox positive review oyunun realistik olub-olmamasını deyil, aşağıdakı hissləri tərifləyir:

- “özümü hacker kimi hiss etdim”;
- terminalda sürətlə command yazmaq;
- sistemlərə icazəsiz daxil olmaq;
- başqasının şəxsi fayllarını araşdırmaq;
- trace altında işləmək;
- gizli məlumat tapmaq;
- sistemdə gözlənilməz şeylərlə qarşılaşmaq.

Bu bizim üçün çox vacib nəticədir:

> Bu janrda texniki realizm özü məhsul deyil. Məhsul oyunçunun yaşadığı fantasy-dir.

---

# 4. İnsanlar niyə Hacknet oynayıblar?

Hazırkı materiallardan bir neçə əsas motiv görünür.

## 4.1. “Hacker olmaq” fantasy-si

Ən güclü hook budur.

Oyunçu real cybersecurity biliyinə sahib olmadan:

- terminal açır;
- IP-lərlə işləyir;
- port scan edir;
- SSH/FTP kimi tanış texniki terminlər görür;
- filesystem daxilində gəzir;
- command yazır;
- sistemlərə daxil olur.

Bu elementlər kifayət qədər real terminologiya verir ki, fantasy inandırıcı görünsün.

Eyni zamanda mexanika kifayət qədər sadələşdirilib ki, real Linux/cybersecurity təcrübəsi olmayan oyunçu da oynaya bilsin.

Bu balans Hacknet-in geniş auditoriyaya çıxmasına kömək edib.

---

## 4.2. Gizli məlumat tapmaq və başqasının kompüterini “qurdalamaq”

Positive review-lərdə təkrarlanan maraqlı elementlərdən biri sadəcə sistemi hack etmək yox, içəridə **nə olduğunu görməkdir**.

Oyunçu:

- personal files,
- email,
- IRC logs,
- password-lar,
- şirkət məlumatları,
- qəribə serverlər,
- easter egg-lər,
- gizli story parçaları

tapır.

Bu zaman reward yalnız “mission complete” olmur.

Reward:

> “Burada nə tapacağam?”

maraq hissidir.

Bu Hacknet-i sırf port-opening simulator olmaqdan çıxarır və investigation elementinə yaxınlaşdırır.

---

## 4.3. Story və mystery

Bit-in ölümü və onun arxasındakı hadisələr oyunçuya mexanikanı davam etdirmək üçün səbəb verir.

Community materiallarında tez-tez:

- story-nin gözlənildiyindən yaxşı olması;
- final sequence;
- müəyyən xüsusi missiyaların yadda qalması;
- oyunun çox qısa hiss olunması

qeyd olunur.

2026-cı ildəki recent positive review-lərdən birində Project Junebug ayrıca illərlə yadda qalan missiya kimi göstərilir.

Bu vacib fərqdir:

> Oyunçu eyni hacking mexanikasını təkrar edir, amma narrative context həmin təkrarın bir hissəsini mənalı saxlayır.

---

## 4.4. Atmosfer

Atmosfer bir neçə sistemin birlikdə işləməsindən yaranır:

- terminal görünüşü;
- virtual OS;
- animasiyalar;
- IP/network vizuallaşdırması;
- trace timer;
- qaranlıq/cyber estetika;
- elektron soundtrack;
- email və log-lar.

Professional review və Steam rəylərində soundtrack xüsusilə tez-tez təriflənir.

Musiqi yalnız fon deyil. Trace və hacking sequence-lərində temp və gərginlik hissini gücləndirir.

---

## 4.5. Oyun ilə interfeys arasında sərhədin pozulması

Hacknet-in ən yadda qalan anlarından bəziləri oyunçunun gözlədiyi “oyun qaydalarını” pozur.

Məsələn review-lərdə insanlar xüsusilə bunları xatırlayırlar:

- `openCDTray` command-ının real kompüterin CD tray-ini açması;
- sistemin “çökməsi”;
- oyunçunun öz sisteminin hack olunması hissi;
- UI elementlərinin itməsi;
- bəzi situasiyalarda oyunun xaricində real terminaldan istifadə etməyə yaxınlaşdırılan hadisələr.

Bu hadisələr daimi mechanic deyil.

Elə buna görə güclüdür.

Oyun uzun müddət müəyyən qayda qurur, sonra həmin qaydanı gözlənilmədən pozur.

Nəticə:

> oyunçu “bu sadəcə fake terminal deyil” hissini qısa müddətə yaşayır.

Bu tip hadisələr review-lərdə illər sonra belə xatırlanır.

---

# 5. Statistikada görünən ən vacib siqnal: ilk saatlar risklidir

Dataset-də playtime segmentləri belədir:

| Playtime | Review sayı | Positive ratio |
|---|---:|---:|
| 0–1 saat | 783 | 67.05% |
| 1–3 saat | 1,081 | 86.59% |
| 3–10 saat | 5,131 | 95.79% |
| 10+ saat | 4,751 | 98.57% |
| unknown | 27 | 85.19% |

Positive review yazanların review anındakı orta playtime-ı:

**13.06 saat**

Negative review yazanların:

**4.40 saat**

Bu datadan birbaşa:

> “oyun 3 saatdan sonra yaxşılaşır”

nəticəsi çıxarmaq olmaz.

Burada selection bias var: oyunu sevən insan təbii olaraq daha uzun oynayır.

Amma yenə də güclü məhsul siqnalı var:

> Hacknet üçün ən böyük itki riski ilk 1–3 saatdadır.

Low-playtime negative sample-larda görünən problemlər:

- oyun açılmır / texniki problem;
- command-ları yadda saxlamaq istəmir;
- nə etməli olduğunu başa düşmür;
- terminal qorxuducu görünür;
- gameplay dərhal boring gəlir;
- real hacking gözləntisi ilə gəlib məyus olur.

Bizim gələcək oyunda ilk sessiya ayrıca araşdırılmalıdır.

---

# 6. Oyunçuların ən çox bəyəndiyi xüsusiyyətlər

Aşağıdakı sıralama bütün dataset üzrə dəqiq frequency ranking deyil. Bu, hazırkı qualitative sample-larda ən çox təkrarlanan güclü mövzulardır.

## 6.1. Immersion — “mən hackerəm” hissi

Ən əsas üstünlük budur.

Oyun:

- minimal klassik game UI istifadə edir;
- əsas interaction-u OS daxilində saxlayır;
- terminalı gameplay-in özünə çevirir;
- texniki terminlərdən atmosfer üçün istifadə edir.

Developer məqsədi ilə oyunçu reaksiyası burada bir-birinə uyğun gəlir.

Bu, product-market fit-in mərkəzidir.

---

## 6.2. Terminalın accessibility ilə balanslaşdırılması

Hacknet real shell deyil.

Bu bəzi technical istifadəçiləri əsəbiləşdirir.

Amma digər tərəfdən bu sadələşdirmə oyunu:

- programmer olmayan;
- Linux bilməyən;
- hacking təcrübəsi olmayan

insanlar üçün əlçatan edir.

Bəzi oyunçular hətta Hacknet-dən sonra Linux terminalına maraq göstərdiklərini və `cd`, `cat` kimi basic anlayışları daha rahat başa düşdüklərini yazırlar.

Burada yaxşı dizayn prinsipi görünür:

> real sistemin bütün mürəkkəbliyini yox, onun tanınan “qrammatikasını” götürmək.

---

## 6.3. Exploration və curiosity

Ən yaxşı Hacknet anları çox vaxt:

> “mənə bunu etməyim deyilməmişdi, amma görəsən burada nə var?”

tipli davranışdan doğur.

Serverlərdə əlavə fayllar, log-lar və easter egg-lər dünyanı daha canlı göstərir.

Ən helpful positive review-lərdən biri oyunçunun əsas vaxtının mission-u sürətlə bitirməyə yox, serverləri “qurdalamağa” getdiyini xüsusi qeyd edir.

Bu bizim üçün çox dəyərli pattern-dir.

---

## 6.4. Story + gameplay eyni interfeysdədir

Story üçün ayrıca cutscene dünyasına keçid azdır.

Narrative əsasən:

- email;
- text files;
- logs;
- hacked systems;
- network nodes

vasitəsilə gəlir.

Yəni story və gameplay ayrı sistemlər deyil.

Oyunçu story-ni **oynamaqla tapır**.

Computer-interface janrı üçün bu xüsusilə güclü yanaşmadır.

---

## 6.5. Soundtrack

Soundtrack community və professional review-lərdə ardıcıl olaraq güclü tərəf kimi görünür.

Musiqi:

- typing ritmini;
- trace gərginliyini;
- “cyber” atmosferini;
- dramatik momentləri

gücləndirir.

Burada dərs sadəcə “yaxşı soundtrack lazımdır” deyil.

Daha düzgün nəticə:

> Interface əsaslı oyunda vizual hərəkət az olduğu üçün audio feedback və musiqi normal oyundan daha böyük yük daşıyır.

---

## 6.6. Yadda qalan “rule-breaking” momentlər

Normal loop-un xaricinə çıxan xüsusi hadisələr yüksək emosional dəyərə malikdir.

Məsələn:

- oyunçunun hack olunması;
- UI-nin pozulması;
- sistem faylları ilə qeyri-adi interaction;
- real kompüterlə zarafat xarakterli interaction;
- xüsusi story sequence-lər.

Bu hadisələrin az olması onların təsirini artırır.

---

# 7. Oyunçuların ən çox bəyənmədiyi xüsusiyyətlər

## 7.1. Əsas problem: repetition

Hazırkı negative sample-larda ən aydın və təkrarlanan şikayət budur.

Loop çox vaxt belə açılır:

```text
probe
→ port tap
→ uyğun cracker aç
→ gözlə
→ port aç
→ porthack
→ filesystem
→ lazım olan faylı tap
→ növbəti server
```

İlk dəfə bu sequence fantasy yaradır.

Onuncu dəfə oyunçu artıq sistemi “görmür”.

O, sadəcə pattern görür.

Bu nöqtədə:

> “server hack edirəm”

hissi:

> “yenə eyni command sequence-ni yazıram”

hissinə çevrilir.

Bu, bizim üçün Hacknet-dən çıxan ən vacib mənfi dərsdir.

---

## 7.2. Tool-lar problem həll etmə vasitəsindən “açar”a çevrilir

Bir çox negative review-un əsas narazılığı real hacking-in olmaması deyil.

Problem budur ki:

- FTP port açıqdır → FTP tool işlət;
- SSH açıqdır → SSH tool işlət;
- sonra PortHack.

Yəni tool seçimi çox vaxt qərar deyil.

Sadəcə uyğun lock üçün uyğun key-dir.

Bu da player agency-ni azaldır.

Daha güclü dizaynda tool:

> “hansı düyməni basmalıyam?”

deyil,

> “bu problemi hansı yanaşma ilə həll edə bilərəm?”

sualını yaratmalıdır.

---

## 7.3. Dünya kifayət qədər reaktiv deyil

Bəzi review-lər xüsusilə bunu qeyd edir:

- log silmək öyrədilir, amma çox vaxt real consequence yoxdur;
- düşmən hacker activity-si azdır;
- server hack etməyin dünyada görünən təsiri məhduddur;
- böyük hissədə dünya oyunçunun əməlindən sonra dəyişmir.

Bu səbəbdən bəzi sistemlər əvvəlcə dərin görünür, sonra oyunçu anlayır ki, əslində çoxu dekorativdir.

Bu immersion üçün təhlükəlidir.

Əgər oyun bir mechanic-in vacib olduğunu deyirsə, oyunçu sonradan onun vacib olmadığını kəşf etməməlidir.

---

## 7.4. Technical audience ilə “real hacking” marketing-i arasında problem

Ən sərt negative review-lərin əhəmiyyətli hissəsi software/network/Linux təcrübəsi olan oyunçulardan gəlir.

Şikayətlər:

- shell real Unix kimi davranmır;
- basic command-lar yoxdur;
- wildcard davranışı qeyri-dəqiqdir;
- file management çox məhduddur;
- hacking proqramları “magic tool” kimi işləyir;
- real security workflow-a bənzəmir.

Maraqlısı budur ki, developer özü əsas məqsədi realizm yox, hiss kimi izah edir.

Deməli burada gameplay problemindən əlavə **expectation problem** də var.

Steam/marketing dilində “real hacking” vurğusu technical auditoriyada daha yüksək gözlənti yaradır.

Bizim oyun üçün nəticə:

> Əgər məhsul fantasy-dir, onu “real simulator” kimi satmaq risklidir.

“Terminal hacking thriller”, “digital investigation game”, “fictional hacking OS” kimi positioning daha sağlam ola bilər.

---

## 7.5. Terminalın özü technical istifadəçini bəzən daha çox əsəbiləşdirir

Paradoks:

Terminal istifadə etməyən oyunçu Hacknet terminalını “real” qəbul edə bilər.

Linux/Unix bilən oyunçu isə real terminal vərdişlərini avtomatik tətbiq etməyə çalışır.

Məsələn:

- wildcard;
- autocomplete;
- `cp`;
- `mkdir`;
- daha dərin path navigation;
- local/remote process məntiqi.

Bunlar işləməyəndə:

> “oyun sadələşdirilib”

hissi yox,

> “terminal səhv işləyir”

hissi yarana bilər.

Yəni interface nə qədər real sistemə oxşayırsa, istifadəçi onun real sistem davranışını bir o qədər gözləyir.

---

## 7.6. Resuming problemi

Community discussion və recent review-lərdə maraqlı problem görünür:

Oyunçu bir neçə saat oynayır, sonra uzun fasilə verir.

Qayıdanda:

- command-ları unudur;
- hansı tool-un nə etdiyini unudur;
- story context-i unudur;
- `help` sistemi kifayət etmir.

Bəzi oyunçular buna görə oyunu sıfırdan başlayırlar.

Bu tip oyunlarda conventional controls-dan fərqli olaraq oyunçu **mini-language** öyrənir.

Ona görə “returning player onboarding” ayrıca dizayn edilməlidir.

---

## 7.7. Texniki problemlər xüsusilə zərərlidir

Recent negative review-lərdə:

- startup problemi;
- Mac freeze;
- save corruption;
- softlock;
- resolution/4K problemi;
- mission sequence bug-ları

görünür.

Bu istənilən oyun üçün pisdir, amma Hacknet kimi oyun üçün əlavə problem yaradır:

Oyunun özündə də:

- crash;
- terminal;
- OS failure;
- hack olunma

gameplay elementi olduğuna görə real bug ilə intentional event arasındakı sərhəd bulanıqlaşa bilər.

---

## 7.8. Bəzi oyunçular üçün story kifayət qədər güclü deyil

Story böyük positive driver-dir, amma universal deyil.

Negative sample-larda onu:

- linear;
- predictable;
- shallow;
- “gameplay-i daşımaq üçün kifayət etmir”

kimi qiymətləndirən oyunçular da var.

Burada vacib nəticə:

> Story zəif core loop-u sonsuza qədər gizlədə bilmir.

Story repetition-a müəyyən müddət dözümlülük yaradır, amma mexanika inkişaf etmirsə problem yenidən üzə çıxır.

---

# 8. Hacknet hansı auditoriyada daha yaxşı işləyir?

Hazırkı materiallardan ən azı üç player tipi görünür.

## 8.1. Hacker fantasy axtaran oyunçu

Bu oyunçu üçün əsas sual:

> “Bu nə qədər realdır?”

deyil.

> “Məni hacker kimi hiss etdirirmi?”

dir.

Hacknet bu auditoriyada çox güclüdür.

---

## 8.2. Story / mystery / investigation oyunçusu

Bu oyunçu:

- files oxumağı;
- məlumatları birləşdirməyi;
- gizli server tapmağı;
- dünyada olan hadisənin arxasını araşdırmağı

sevir.

Bizim gələcək konseptimiz üçün bu auditoriya xüsusilə vacibdir, çünki Cyber Manhunt və The Operator kimi oyunlarla da overlap edir.

---

## 8.3. Technical / Linux / cybersecurity auditoriyası

Bu qrup ən maraqlı və ən riskli qrupdur.

Onların bir hissəsi:

- terminləri;
- Unix flavor-u;
- port nömrələrini;
- terminal estetikasını

çox sevir.

Digər hissəsi isə məhz real sistemləri bildiyi üçün oyunun abstraction-larını daha sərt tənqid edir.

Deməli bu auditoriyanı hədəfləmək istəyiriksə:

- ya sistemlər daha dərin olmalıdır;
- ya da marketing açıq şəkildə “real hacking simulator” gözləntisini azaltmalıdır.

---

# 9. Hacknet-in uğurunu izah edən əsas faktorlar

Bunlar səbəb-nəticə olaraq tam sübut edilmiş deyil, amma mövcud evidence ilə güclü izah hipotezləridir.

## 9.1. Bir cümlədə başa düşülən güclü fantasy

> “Terminalda hacker olursan.”

Concept screenshot-la belə başa düşülür.

Bu indie oyun üçün çox böyük üstünlükdür.

---

## 9.2. Interface özü oyundur

Hacknet-də UI gameplay-dən ayrı layer deyil.

Terminal, network map, filesystem və email:

- həm interface-dir;
- həm game mechanic-dir;
- həm world-building-dir;
- həm narrative delivery sistemidir.

Bir sistem bir neçə işi eyni anda görür.

Bu kiçik komanda üçün çox effektiv dizayndır.

---

## 9.3. Realizm yox, seçilmiş authenticity

Hacknet real hacking-in bütün kompleksliyini götürmür.

Onun əvəzinə ən tanınan işarələri götürür:

- command line;
- Unix-like command-lar;
- IP;
- ports;
- protocols;
- root/admin access;
- filesystem;
- logs.

Bu “kifayət qədər real” görüntü yaradıb, amma böyük auditoriyanı complexity ilə uzaqlaşdırmır.

---

## 9.4. Narrative context mexanikanın dəyərini artırır

Bir faylı `cat` ilə oxumaq gameplay olaraq maraqlı deyil.

Amma həmin faylda:

- sirr;
- başqa şəxsin söhbəti;
- password;
- story twist;
- təhlükəli informasiya

olanda eyni action maraqlı olur.

Deməli interface-game dizaynında **content writing** core mechanic qədər vacib ola bilər.

Bu bizim komanda üçün də yaxşı uyğunluqdur, çünki story writer və designer-in işi gameplay-in mərkəzinə daxil ola bilər.

---

## 9.5. Güclü memorable moments

Hacknet hər dəqiqə yeni mechanic vermir.

Amma müəyyən nöqtələrdə çox yadda qalan hadisələr yaradır.

Bu momentlər Steam review-lərdə illər sonra belə danışılır.

Bu, “content quantity” ilə “memorable event density” arasındakı fərqi göstərir.

---

## 9.6. Audio/visual polish sadə mexanikanı daha güclü hiss etdirir

Command özü:

```text
SSHCrack 22
```

çox sadə action-dır.

Amma:

- progress;
- animasiya;
- səs;
- music;
- trace pressure;
- terminal feedback

onu daha dramatik hiss etdirir.

Bu janrda “juice” xüsusilə vacibdir.

---

## 9.7. Mod/Workshop uzunömürlülük verir

High-playtime review-lərdə community campaign və extension framework ayrıca qeyd olunur.

Base game qısa və finite olsa da, custom campaigns oyunun ömrünü uzadır.

Bu ilk versiya üçün lazım olan feature deyil, amma content-heavy interface oyunları üçün sonradan çox güclü leverage ola bilər.

---

# 10. Developer prosesindən bizim üçün dərslər

Matt Trobbiani-nin müsahibələrindən bir neçə xüsusilə vacib dərs çıxır.

## 10.1. Oyun böyük design document-dən yox, kiçik prototype-dan başlayıb

Hacknet əvvəlcə 48 saatlıq game jam layihəsi olub.

Əsas test olunan şey:

> “bu interface oyunçuya hacker hissi verirmi?”

olub.

Bu bizim layihə üçün çox uyğun yanaşmadır.

İlk prototype:

- böyük story;
- 30 mission;
- backend ecosystem;
- progression tree

qurmamalıdır.

Əvvəl yoxlanmalı sual:

> 10–15 dəqiqəlik experience oyunçuya həqiqətən maraqlı digital investigator / hacker hissi verirmi?

---

## 10.2. İlk feedback ideyanın davam etməsinə səbəb olub

Developer-in dediyinə görə game jam/public build və convention feedback-i müsbət olduğu üçün layihəni üç il inkişaf etdirməyə davam edib.

Bu “əvvəl build et, sonra üç il ümid et” modeli deyil.

Əvvəl kiçik experience yaradılıb və onun insanlar üzərində işləyib-işləmədiyinə baxılıb.

---

## 10.3. Iteration sürəti polish üçün vacib olub

Trobbiani öz development setup-ında sürətli compile/iteration-ı çox vacib sayır və Hacknet effektlərinin yüzlərlə kiçik iteration ilə tune edildiyini deyir.

Interface-heavy oyun üçün bu xüsusilə əhəmiyyətlidir.

Çünki:

- typing feedback;
- animasiya sürəti;
- progress timing;
- sound timing;
- window transition;
- trace pressure

kağız üzərində dizayn edilə bilməz.

Onları hiss etmək üçün davamlı playtest lazımdır.

---

# 11. Hacknet-in əsas dizayn paradoksu

Hacknet-in uğuru və əsas problemi eyni sistemdən gəlir.

Sadələşdirilmiş hacking:

**üstünlükdür**, çünki:

- yeni oyunçu başa düşür;
- sürətli oynanır;
- fantasy dərhal yaranır.

Amma eyni sadələşdirmə:

**problemdir**, çünki:

- bir neçə saatdan sonra pattern görünür;
- tool-lar qərar yox, düymə olur;
- technical oyunçu sistemin dayazlığını görür;
- repetition artır.

Bunu belə ifadə etmək olar:

```text
Accessibility
    ↓
Simple repeatable rules
    ↓
Fast fantasy payoff
    ↓
Pattern becomes obvious
    ↓
Repetition
```

Bizim oyunun əsas dizayn problemlərindən biri bu zənciri qırmaq olacaq.

---

# 12. Öz oyunumuz üçün çıxarılan ilkin qaydalar

Bunlar hələ bütün janr üzrə qaydalar deyil.

Hazırda yalnız Hacknet-dən çıxarılan design hypotheses-dir.

## Qayda 1 — Fantasy-ni əvvəl müəyyən et

Əvvəl:

> oyunçu nə edəcək?

yox,

> oyunçu özünü kim kimi hiss etməlidir?

sualına cavab ver.

Hacknet üçün cavab “hacker” idi.

Bizim oyun üçün bu daha konkret ola bilər:

- digital investigator;
- hacker;
- intelligence analyst;
- cyber detective;
- surveillance operator;
- social engineer.

---

## Qayda 2 — UI sadəcə görünüş olmamalıdır

Fake OS sadəcə skin olsa, novelty tez bitəcək.

UI daxilindəki hər element mümkün qədər:

- gameplay;
- information;
- story;
- decision

daşımalıdır.

---

## Qayda 3 — Eyni hack sequence-ni təkrar etmə

Əgər hər target belədirsə:

```text
scan → tool A → tool B → root
```

oyunçu çox tez sistemi decode edəcək.

Target-lər arasında yalnız:

- daha çox port;
- daha uzun timer;
- başqa password

dəyişməsi kifayət deyil.

Problem strukturu dəyişməlidir.

---

## Qayda 4 — Tool-lar “key” yox, seçim yaratmalıdır

Yaxşı tool:

> FTP varsa FTPHack işlət

qədər deterministik olmamalıdır.

Mümkün qədər bir neçə yanaşma olmalıdır:

- technical exploit;
- social information;
- credential reuse;
- metadata;
- phishing;
- physical clue;
- indirect access;
- başqa şəxsin hesabı.

Bu, Cyber Manhunt kimi oyunlarla müqayisədə ayrıca araşdırılmalıdır.

---

## Qayda 5 — Information discovery-ni core loop-a daxil et

Hacknet-in ən maraqlı hissələrindən biri filesystem daxilində məlumat tapmaqdır.

Biz bunu daha da gücləndirə bilərik:

```text
tap
→ əlaqələndir
→ hipotez qur
→ istifadə et
→ consequence gör
```

Bu, sadəcə:

```text
tap
→ mission objective-ə ver
```

olmamalıdır.

---

## Qayda 6 — Oyunçunun etdiyi şey dünyada nəticə yaratmalıdır

Əgər:

- log silmək;
- identity gizlətmək;
- trace;
- məlumat oğurlamaq

mechanic kimi göstərilirsə, onların consequence-i olmalıdır.

Əks halda oyunçu sistemin fake olduğunu hiss edir.

---

## Qayda 7 — Realizm sözündən ehtiyatla istifadə et

Real terminology faydalıdır.

“Real hacking simulator” vədi isə təhlükəlidir.

Technical istifadəçi həmin anda real-world behavior gözləməyə başlayır.

Fantasy ilə authenticity arasında fərq açıq saxlanmalıdır.

---

## Qayda 8 — İlk 30–60 dəqiqə ayrıca məhsuldur

Hacknet dataset-ində ən aşağı satisfaction 0–1 saat segmentindədir.

Bizim prototype testinin əsas suallarından biri bu olmalıdır:

- ilk 5 dəqiqədə fantasy yaranır?
- ilk 15 dəqiqədə oyunçu meaningful action edir?
- ilk 30 dəqiqədə yeni bir discovery baş verir?
- oyunçu command-ları öyrənərkən özünü dərsdə hiss edir, yoxsa oyunda?

---

## Qayda 9 — Returning player üçün recovery sistemi lazımdır

Bu janr oyunçuya xüsusi command vocabulary öyrədir.

Oyunçu 2 həftə fasilə verdikdə sıfırdan başlamağa məcbur olmamalıdır.

Mümkün həllər:

- contextual command suggestions;
- searchable help;
- mission recap;
- “last time you did…”;
- recent commands;
- notebook;
- pinned evidence;
- interactive refresher.

---

## Qayda 10 — Bir neçə böyük “impossible moment” planlaşdır

Hacknet-də ən yadda qalan hadisələr normal loop-u pozan hadisələrdir.

Biz də əvvəlcədən 3–5 belə moment dizayn edə bilərik.

Məsələn:

- NPC sənin sisteminə daxil olur;
- fake OS-un bir hissəsi dəyişir;
- əvvəldən etibar etdiyin data saxta çıxır;
- başqa oyunçunun əvvəlki action-u sistemdə görünür;
- desktop-da “olmamalı” bir application yaranır;
- oyunçu özü izlənildiyini anlayır.

Bunlar random twist yox, sistemlə əlaqəli olmalıdır.

---

## Qayda 11 — Audio core design elementidir

Computer UI oyununda:

- character animation;
- 3D world;
- combat spectacle

azdır.

Bunun əvəzinə:

- keyboard sound;
- connection sound;
- alert;
- trace;
- progress;
- background ambience;
- music transition

oyunun “fiziki” hissini yaradır.

Audio sonradan əlavə ediləcək kosmetika kimi planlaşdırılmamalıdır.

---

## Qayda 12 — Story writer gameplay komandasının mərkəzində olmalıdır

Hacknet göstərir ki, eyni mechanic-in maraqlı olub-olmaması çox vaxt içində tapdığın məlumatdan asılıdır.

Deməli writer yalnız cutscene yazmır.

Writer:

- email;
- logs;
- files;
- conversations;
- identities;
- secrets;
- misinformation;
- clues

vasitəsilə gameplay content yaradır.

Bu bizim mövcud komanda quruluşuna uyğun güclü üstünlükdür.

---

# 13. Hacknet-də həll olunmamış opportunity-lər

Hacknet-dən sonra eyni istiqamətdə yeni oyun üçün açıq görünən sahələr:

## 13.1. Daha reaktiv dünya

Hack nəticəsində:

- news dəyişə bilər;
- NPC davranışı dəyişə bilər;
- şirkət cavab tədbiri görə bilər;
- digər hacker fəaliyyət göstərə bilər;
- istifadə olunan exploit bağlana bilər;
- oyunçunun reputation-u dəyişə bilər.

---

## 13.2. Hacking + investigation-ın daha dərindən birləşdirilməsi

Hacknet-də investigation var, amma core breach loop çox vaxt ayrıca qalır.

Daha yaxşı model:

```text
information → access
access → new information
new information → social leverage
social leverage → alternate access
```

şəklində circular ola bilər.

---

## 13.3. Meaningful choice

Target-ə yalnız bir doğru sequence əvəzinə:

- hansı sistemi əvvəl araşdırmaq;
- kimə inanmaq;
- məlumatı kimə vermək;
- hansı exploit-i yandırmaq;
- nəyi gizlətmək;
- nəyi leak etmək

kimi qərarlar ola bilər.

---

## 13.4. Real technical depth yox, systemic depth

Bizim məqsəd real Linux implement etmək olmamalıdır.

Dərinlik başqa yerdən gələ bilər:

- məlumat əlaqələri;
- insanlar;
- permissions;
- identity;
- trust;
- reputation;
- network topology;
- consequence;
- time pressure;
- incomplete information.

Bu həm daha əlçatan, həm də daha oyunvari dərinlik yarada bilər.

---

# 14. Hacknet haqqında indiki əsas nəticə

Hacknet-in əsas uğuru onun “hacking simulator” olmasında deyil.

Əsas uğur budur:

> **Sadə interaction-ları, güclü fictional OS, real texniki terminlərin seçilmiş istifadəsi, story, exploration, soundtrack və bir neçə çox yadda qalan hadisə ilə birləşdirərək oyunçuya hacker fantasy-si satır.**

Əsas zəifliyi də bunun əks tərəfidir:

> **Oyunçu core hacking sequence-nin strukturunu başa düşəndə sistemin arxasındakı sadəlik görünür və fantasy repetition-a çevrilə bilir.**

Bizim gələcək oyun üçün hədəf Hacknet-i daha “real” etmək olmamalıdır.

Daha yaxşı hədəf:

> **Hacknet-in immersion və fantasy gücünü saxlayıb, onun repetition, dayaz decision-making və zəif world reactivity problemlərini həll etməkdir.**

Bu hipotezi növbəti oyunlarla müqayisə etməliyik.

Xüsusilə:

- Hacknet vs Midnight Protocol
- Hacknet vs NITE Team 4
- Hacknet vs Mainlining
- Hacknet vs Cyber Manhunt

müqayisələri bu nəticələrin Hacknet-ə məxsus, yoxsa janr səviyyəsində olduğunu göstərəcək.

---

# 15. Növbəti data mərhələsi

Hacknet üzrə növbəti texniki addım bütün 11,773 review-u aspect/theme səviyyəsində təsnif etməkdir.

İlkin taxonomy bu sənəddən belə başlaya bilər:

```text
HACKER_FANTASY
IMMERSION
TERMINAL
UI
STORY
MYSTERY
INVESTIGATION
EXPLORATION
DISCOVERY
SOUNDTRACK
ATMOSPHERE
PUZZLE
DIFFICULTY
ONBOARDING
REPETITION
DEPTH
REALISM
TECHNICAL_ACCURACY
PLAYER_AGENCY
CONSEQUENCES
PACING
LENGTH
REPLAYABILITY
MOD_SUPPORT
BUGS
COMPATIBILITY
ENDING
```

Hər review birdən çox theme daşıya bilər.

Məsələn:

```text
"Story was great, but every server used the same commands."
```

belə kodlanmalıdır:

```text
STORY           → positive
REPETITION      → negative
TERMINAL_LOOP   → negative
```

Sadə positive/negative sentiment bu araşdırma üçün kifayət deyil.

---

# Mənbələr

## Daxili repository mənbələri

**[D1]** `data/processed/hacknet/statistics.json`  
Hacknet Steam review dataset-in əsas statistikası.

**[D2]** `data/reports/hacknet/summary.md`  
Dataset collection və deterministic xülasə.

**[D3]** `data/processed/hacknet/samples/helpful_positive.csv`

**[D4]** `data/processed/hacknet/samples/helpful_negative.csv`

**[D5]** `data/processed/hacknet/samples/recent_positive.csv`

**[D6]** `data/processed/hacknet/samples/recent_negative.csv`

**[D7]** `data/processed/hacknet/samples/low_playtime.csv`

**[D8]** `data/processed/hacknet/samples/high_playtime.csv`

## Xarici mənbələr

**[W1] Hacknet developer interview — GeekOut UK**  
https://geekoutsw.wordpress.com/2016/05/18/hacknet-developer-interview/

Developer burada Hacknet-in 48 saatlıq “UIs and Interfaces” game jam-dan başladığını və əsas məqsədin oyunçunu hacker kimi hiss etdirmək olduğunu izah edir.

**[W2] Interview with Hacknet Creator Matt Trobbiani — AdamFowlerIT**  
https://adamfowlerit.com/2016/04/interview-hacknet-creator-matt-trobbiani/

Prototype feedback, üç illik development prosesi, iteration və educational use haqqında məlumat.

**[W3] Hacknet — Fellow Traveller Press Kit**  
https://www.fellowtravellerpresskit.com/hacknet

Rəsmi description, features, developer məlumatı və ilk il ərzində 200,000-dən çox satış barədə məlumat.

**[W4] Hacknet Steam Store**  
https://store.steampowered.com/app/365450/Hacknet/

Rəsmi positioning, tag-lər və store description.

**[W5] Hacknet Steam Community — negative reviews**  
https://steamcommunity.com/app/365450/negativereviews/

Repetition, technical accuracy və gameplay depth haqqında community nümunələri.

**[W6] GameSpot — Hacknet / Labyrinths materialları**  
https://www.gamespot.com/games/hacknet/  
https://www.gamespot.com/reviews/hacknet-labyrinths-review/1900-6416654/

Immersion, soundtrack, puzzle loop və repetition haqqında professional review materialları.

**[W7] Reddit /r/Hacknet — shortcomings discussion**  
https://www.reddit.com/r/Hacknet/comments/107p74i/

Oyunun qısa olması, command-ları fasilədən sonra unutmaq və Workshop content barədə community müzakirəsi.

**[W8] Reddit /r/Hacknet — appreciation discussion**  
https://www.reddit.com/r/Hacknet/comments/1s4kkpk/

Story, atmosphere və repetition-ın eyni anda necə qəbul edildiyinə dair nümunə.

**[W9] Reddit /r/Hacknet — learning discussion**  
https://www.reddit.com/r/Hacknet/comments/1vgxxbg/hacknet_for_learning/

Hacknet-in real hacking öyrətməsindən daha çox basic terminal/Linux familiarity yaratdığı barədə community fikirləri.

---

# Status

**Mərhələ:** Hacknet qualitative deep research — ilkin versiya  
**Dataset:** Verified 11,773 Steam review  
**Tamamlanıb:** quantitative baseline + qualitative sample analysis + external research + initial design lessons  
**Növbəti:** bütün review-lər üzrə avtomatlaşdırılmış theme/aspect classification və sonra comparison research
