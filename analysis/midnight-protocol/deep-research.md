# Midnight Protocol — Dərin araşdırma

## Rəhbərlik üçün xülasə

Midnight Protocol terminal və hakerlik janrında Hacknet-dən fərqli bir problem həll etməyə çalışır: hacking-i sürətli əmrlərin icrası kimi yox, **növbə əsaslı taktiki qərar sistemi** kimi təqdim edir.

Oyun bunu üç əsas qat-i birləşdirərək edir:

```text
hacker fantasy
+
turn-based tactical network gameplay
+
story / moral choice / reputation
```

Verified Steam məlumat toplusu:

- 301 ingilisdilli rəy
- 253 müsbət
- 48 mənfi
- 84.05% müsbət rəy nisbəti

Əsas nəticə:

> **Midnight Protocol Hacknet-in dayaz “alət = key” probleminə real mexaniki dərinlik əlavə edir, amma bunun əvəzində RNG (təsadüfi nəticə mexanizmi) və ədalətlilik, yenidən cəhd/bərpa, alət dəsti qeyri-müəyyənlik, yalnız klaviatura ilə çətinlik və təlim hissəsi-sonrası mürəkkəblik problemləri yaradır.**

Oyunun ən güclü tərəfləri:

- özünü haker kimi hiss etmə;
- oyuna dalma hissi;
- hekayə;
- növbə əsaslı planlama;
- alət dəsti/quruluş seçimi;
- moral seçim və reputation;
- üslublu UI/audio;
- seçilmiş həqiqilik hissi.

Ən ciddi problemlər:

- RNG səbəbilə uğursuzluğun oyunçu bacarığı-dən ayrılması;
- rollback/yenidən cəhd modelinin bunu daha ağrılı etməsi;
- izlənmə sayğacı və gediş limiti-lərin experimentation ilə toqquşması;
- yalnız klaviatura ilə control-un bəzi action-ları süni şəkildə yavaşlatması;
- təlim hissəsi-dan sonra 1–3 saatlıq mərhələdə yüksək çətinlik;
- daha çox sistem olmasına baxmayaraq müəyyən mərhələdə təkrarçılıq;
- bəzi qərar/nəticələrin həddindən artıq sərt və geri dönməz hiss olunması.

Ən vacib məhsul lesson:

> **dərinlik təkrarçılıq problemini azalda bilər, amma dərinlik özü yaxşı dizayn demək deyil. Oyunçunun hər qərarı başa düşülən, planlana bilən və uğursuzluq zamanı izah edilə bilən olmalıdır.**

Hacknet ilə birlikdə baxanda artıq iki oyunlararası principle güclənir:

1. **tam realizm lazım deyil; seçilmiş həqiqilik hissi + ardıcıl rol hissi işləyir;**
2. **terminal/keyboard giriş rol hissini gücləndirir, amma qarşılıqlı əlaqənin səmərəliliyi pozulanda yenilik effekti çətinliyə çevrilir.**

Ətraflı rəy məlumatları:

`analysis/midnight-protocol/theme-analysis.md`

---

# 1. Araşdırmanın əhatəsi və məlumat keyfiyyəti

## 1.1. Steam məlumat toplusu

Snapshot: **2026-10-02**

- xam rəylər: 301
- təkrarsız rəylər: 301
- müsbət: 253
- mənfi: 48
- müsbət rəy nisbəti: 84.05%
- rəy yazılan andakı median oyun müddəti: 11.70h
- müsbət rəylərdə orta oyun müddəti: 17.01h
- mənfi rəylərdə orta oyun müddəti: 5.59h

Xam və emal olunmuş məlumatlar:

- `data/raw/midnight-protocol/`
- `data/processed/midnight-protocol/`
- `data/reports/midnight-protocol/summary.md`

## 1.2. məna yönümlü yoxlama

Oxunub:

- bütün 48 mənfi rəy;
- 50 ən faydalı müsbət rəy;
- 50 low-oyun müddəti rəy;
- 25 son dövr müsbət rəy.

Bu, mənfi uğursuzluq nümunəsi-ləri üçün yüksək etibarlılıq verir.

## 1.3. Xarici mənbələr

İstifadə olunub:

- Steam mağaza;
- Game yaradıcı Sam Agten interview;
- Quarter to Three rəy;
- Softpedia rəy;
- əvvəlki kickoff external araşdırma.

## 1.4. Limitations

- Steam rəy müəllifi-lər bütün oyunçu population deyil;
- overall recommendation aspekt üzrə münasibət deyil;
- namizəd mövzu yoxlama regex-based retrieval-dir;
- oyun müddəti correlation causation deyil;
- mağaza display rəy count ilə Steam API snapshot fərqlənə bilər;
- bəzi launch-era problemlər patch-lərlə dəyişmiş ola bilər.

---

# 2. Məhsul və bazar görünüşü

Steam App ID: **1162700**

- yaradıcı: LuGus Studios
- Publisher: Iceberg Interactive
- Release: 13 October 2021
- Base US price: $14.99
- Genres: Action, Adventure, Indie, RPG, strategiya
- Steam Workshop
- level editor
- Steam Cloud
- yalnız klaviatura ilə təqdimat

Steam mağaza description:

> taktiki narrative-driven RPG with unique yalnız klaviatura ilə controls

mağaza promise üç hissəyə bölünür:

1. hacking rol hissi;
2. taktiki RPG;
3. hekayə/seçim.

Bu Hacknet-dən vacib şəkildə fərqlənir.

Hacknet əsasən:

> “terminal hacking simulator / hacker experience”

kimi oxunur.

Midnight Protocol isə:

> “hacking mövzu içində taktiki RPG”

kimi daha düzgün anlaşılır.

Bu distinction düzgün kommunikasiya edilməsə expectation mismatch yaranır.

---

# 3. Midnight Protocol əslində necə oyundur?

Ən düzgün qısa təsvir:

> **yalnız klaviatura ilə interface daxilində oynanan növbə əsaslı taktiki network RPG və narrative puzzle game.**

Oyun real hacking simulator deyil.

Core mission loop:

```text
mission seç
→ available intel oxu
→ programs/hardware loadout qur
→ network-ə daxil ol
→ node-lar arasında hərəkət et
→ ICE / SysOp / trace idarə et
→ objective və optional data tap
→ qərar ver
→ network-dən çıx
→ reputation/story nəticəsi al
→ yeni tool / mission / branch aç
```

Hər turn-də əsas grammar sadədir:

- move;
- interact;
- ability/program;
- end turn.

Dərinlik həmin sadə grammar ətrafında qurulur.

---

# 4. Əsas oyunçunun rol hissi

Midnight Protocol-un rol hissi-si sadəcə:

> “hacker olum”

deyil.

Daha düzgün:

> **“hazırlıq görən, network daxilində taktiki qərarlar verən və hansı hacker olmaq istədiyinə özü qərar verən operator olum.”**

rol hissi üç qat-də qurulur.

## 4.1. Physical rol hissi

Real keyboard istifadə olunur.

Oyunçu command yazır.

Bu physical giriş fictional activity ilə uyğun gəlir.

## 4.2. taktiki rol hissi

Oyunçu:

- alət dəsti hazırlayır;
- route seçir;
- trace idarə edir;
- ICE və SysOp threat-lərini qiymətləndirir;
- resource bölür.

## 4.3. Identity rol hissi

Oyunçu:

- white/grey/black hat reputation;
- moral seçim;
- target haqqında optional məlumat;
- side mission;
- bank/məlumat/privacy qərarları

ilə “necə hacker” olduğunu formalaşdırır.

Hacknet-də birinci qat çox güclüdür.

Midnight Protocol ikinci və üçüncü qat-i daha çox inkişaf etdirir.

---

# 5. İnsanlar niyə başlayır?

## 5.1. Distinctive yalnız klaviatura ilə ilkin cəlbedicilik

Screenshot və mağaza description-da dərhal fərqlənir.

“Only keyboard”:

- qeyri-adi görünür;
- özünü haker kimi hiss etmə-ni bir cümlədə izah edir;
- conventional game controls-dan fərqlənir.

Bu yaxşı marketing ilkin cəlbedicilik-dur.

## 5.2. Hacking genre audience

rəylərdə davamlı müqayisələr var:

- Hacknet;
- Uplink;
- NITE Team 4;
- Netrunner;
- Zachtronics.

Deməli məhsul mövcud niche audience-in tanıdığı mental model-ə düşür.

## 5.3. hekayə premise

oyunçu character məlumat əvvəl doxx olunub.

Core mystery:

> kim və niyə?

Bu dərhal oyunçu goal yaradır.

## 5.4. taktiki yenilik effekti

Hacking game üçün növbə əsaslı model qeyri-adidir.

Bu həm yenilik effekti, həm də riskdir.

---

# 6. İnsanlar niyə davam edir?

rəy dəlil-ə görə əsas oyunda qalma səbəbləri:

1. hekayə;
2. taktiki system mastery;
3. new programs/hardware;
4. moral seçimlər/reputation;
5. side missions;
6. kəşf/secrets;
7. quruluş experimentation;
8. özünü haker kimi hiss etmə;
9. atmosphere.

STORY_NARRATIVE namizəd-i:

- 136 rəy
- məlumat toplusun 45.18%-i.

10h+ cohort-da hekayə mention edən 100 rəydən yalnız 4-ü mənfi-dir.

Bu çox güclü oyunda qalma siqnalıdır.

---

# 7. ilkin öyrətmə və ilk sessiya

## 7.1. İlk saat tam disaster deyil

0–1h:

- 21 rəylər
- 76.19% müsbət.

Yəni interface dərhal bütün oyunçuları itirmir.

Bir çox early rəy:

- yalnız klaviatura ilə control-un tez başa düşüldüyünü;
- təlim hissəsi-ın faydalı olduğunu;
- visual presentation-ın güclü olduğunu

deyir.

## 7.2. Əsas problem 1–3h-dır

1–3h:

- 45 rəylər
- yalnız 62.22% müsbət.

Bu məlumat toplusu-də ən zəif cohort-dur.

Bu çox vacibdir.

təlim hissəsi ilk mexanikalar-i izah edə bilir.

Problem daha sonra başlayır:

- real alət dəsti decisions;
- trace;
- təsadüfilik;
- SysOp;
- limited slots;
- uğursuzluq/yenidən cəhd;
- harder missions

birlikdə işə düşəndə.

Yəni:

> **initial ilkin öyrətmə ilə systems ilkin öyrətmə eyni şey deyil.**

## 7.3. yaradıcı intent ilə uyğunluq

yaradıcı Sam Agten ilkin öyrətmə-in çox çətin olduğunu və təlim hissəsi/demo-nun ən çox iteration edilən hissə olduğunu deyir.

Bu rəy nümunə ilə uyğun gəlir.

Ancaq lesson budur:

> təlim hissəsi command-ları öyrətməklə bitmir. Oyunçuya sistemlər arasındakı qərar model-i də öyrətmək lazımdır.

---

# 8. əsas oyun dövrü və sistem dərinliyi

Midnight Protocol Hacknet-dən daha dərin əsas oyun dövrü qurur.

Əlavə qərar qat-ləri:

- deck/alət dəsti;
- limited slots;
- memory/slices;
- stealth vs aggression;
- ICE;
- SysOp;
- route;
- trace;
- optional objectives;
- reputation nəticələr.

Bu real improvement-dir.

Amma iki problem qalır.

## 8.1. Mandatory alətlər real seçim-ni azalda bilər

Bir rəydə oyunçu 5 slot-dan:

- cloak;
- sniffer;
- dagger

kimi alət-ların praktiki olaraq məcburi olduğunu qeyd edir.

Əgər 5 slot-dan 3-ü mandatory-dirsə:

> 5 seçim yoxdur.

Real qərar space daha kiçikdir.

## 8.2. Dominant quruluş problemi

Long-play müsbət rəylərdə belə qeyd olunur ki:

- çox program var;
- amma effektiv bir configuration tapdıqdan sonra çox mission üçün onu dəyişməyə ehtiyac azalır.

Bu classic quruluş-system problemidir:

> məzmun variety var, strategic necessity azdır.

---

# 9. növbə əsaslı model nəyi həll edir?

yaradıcı əvvəl real-time model düşünüb.

Playtest nəticəsində:

- stressli;
- fun olmayan

hiss etdiyi üçün növbə əsaslı-a keçib.

Bu qərarın real üstünlükləri rəylərdə görünür.

## 9.1. Speed requirement azalır

Oyunçu typing sürəti ilə deyil, planla yarışır.

## 9.2. Düşünmə vaxtı artır

Network state-i analiz etmək olur.

## 9.3. əlçatanlıq artır

Non-technical və slow typist oyunçu üçün daha əlçatandır.

## 9.4. taktiki identity yaranır

Oyun Hacknet clone olmaqdan çıxır.

---

# 10. növbə əsaslı model hansı yeni problemi yaradır?

## 10.1. “Hacking yox, board game” expectation mismatch

Bütün mənfi rəy yoxlama-də ən aydın mövzu-lərdən biri budur.

Bəzi oyunçu üçün:

- nodes = board spaces;
- programs = abilities/cards;
- SysOps = enemy pieces;
- two actions = board-game hərəkət büdcəsi.

Bu onlar üçün hacking rol hissini zəiflədir.

Əsas problem mexanika-in keyfiyyəti yox, expectation-dır.

mağaza page taktiki RPG deyir, amma “hacking” word-u daha güclü prior expectation yarada bilər.

## 10.2. Typing-in oyun gedişi funksiyası azalır

Real-time Hacknet-də typing:

- speed;
- execution;
- pressure

ilə bağlıdır.

növbə əsaslı Midnight Protocol-da isə typing bəzən sadəcə UI qat-dir.

Bu bəzi rəy müəllifi-lərdə belə sual yaradır:

> əgər time pressure yoxdur, niyə click etmək əvəzinə bunu yazmalıyam?

Deməli giriş thematicdir, amma mexaniki necessity hər zaman güclü deyil.

---

# 11. RNG və fairness

Bu oyunun əsas dizayn problemi budur.

RNG_FAIRNESS:

- 36 mentions
- 13 mənfi
- 36.11% mənfi
- overall baseline-dan 2.26× yüksək.

Bütün 48 mənfi rəy yoxlama-i də bunu təsdiqləyir.

Ən çox qeyd olunan nümunələr:

- trace chance;
- cloak probability;
- SysOp movement;
- hidden ICE;
- critical-like events;
- mission state qeyri-müəyyənlik.

Problem təsadüfilik özü deyil.

Problem:

> oyunçu uğursuzluq-i bacarıq geribildirim kimi istifadə edə bilmir.

Hacknet-də uğursuzluq tez-tez:

> “daha sürətli olmalıydım”

kimi anlaşılır.

Midnight Protocol-da bəzi uğursuzluq-lər:

> “daha yaxşı roll gəlməli idi”

kimi anlaşılır.

Bu mastery satisfaction-a zərbə vurur.

---

# 12. yenidən cəhd / rollback / bərpa

RNG problemindən sonra ikinci böyük risk budur.

yenidən cəhd_ROLLBACK:

- 20 mentions
- 35% mənfi.

Complaint-lər:

- mission restart;
- rollback;
- wrong alət dəsti ilə ilişmək;
- re-plan etmək imkanı;
- manual save;
- failed mission-in permanent bağlanması;
- game restart ilə workaround.

Əsas dizayn principle:

> **uğursuzluq cost-u çətinlik ilə proporsional olmalıdır.**

Əgər oyunçu:

- bütün relevant info-ya sahib deyil;
- random outcome yaşayır;
- sonra permanent məzmun itirirsə

sistem unfair hiss olunur.

---

# 13. Trace və urgency

Trace əvvəlcə yaxşı tension yaradır.

Bu özünü haker kimi hiss etmə üçün vacibdir.

Amma Midnight Protocol-da trace eyni zamanda:

- action budget;
- exploration budget;
- optional məzmun budget

olur.

Bəzi rəylərdə trace:

- interesting;
- exciting;
- strategic

kimi görünür.

Digərlərində isə:

- experimentation-ı cəzalandırır;
- exploration-ı məhdudlaşdırır;
- mandatory cloak slot yaradır;
- luck dependency artırır.

URGENCY_TRACE namizəd-lərinin 50%-i mənfi rəy-dur.

Bu volume aşağıdır, amma məna yönümlü yoxlama güclüdür.

---

# 14. təkrarçılıq

Midnight Protocol Hacknet-dən daha çox variation və quruluş dərinlik verir.

Amma təkrarçılıq yenə mövcuddur.

təkrarçılıq:

- 19 mentions;
- 36.84% mənfi;
- baseline-dan 2.31× yüksək.

Əsas recurring grammar:

```text
move
→ inspect/sniff
→ deal with ICE
→ manage trace
→ end
→ repeat
```

Mission-specific twist-lər bunu qırır.

Bəzi long-play müsbət rəylər:

- boss-like encounters;
- handcrafted missions;
- special one-off mexanikalar;
- side missions

sayəsində late game-in daha güclü olduğunu qeyd edir.

Bu 10h+ cohort-un çox yüksək 95.51% müsbət rəy nisbəti-su ilə uyğun gəlir.

Amma bu causation deyil.

---

# 15. UI/UX və yalnız klaviatura ilə

## 15.1. Niyə işləyir?

yaradıcı-in məqsədi:

> fiziki keyboard-u rol hissinin hissəsinə çevirmək.

rəylərdə bu açıq şəkildə işləyir.

müsbət geribildirim:

- typing satisfying;
- keyboard özünü haker kimi hiss etmə-ni artırır;
- mouse olmaması distinctive hiss edir;
- “in the zone” state yaradır.

## 15.2. Niyə işləmir?

mənfi geribildirim:

- click-lə daha sürətli ediləcək action-lar;
- node name yazmaq;
- repeated “end”;
- typo;
- help çıxış discoverability;
- command alias problemləri;
- menu navigation;
- command context.

Ən vacib nəticə:

> **immersive qarşılıqlı əlaqə ilə efficient qarşılıqlı əlaqə eyni şey deyil.**

Gələcək oyunda hər giriş hər ikisini mümkün qədər təmin etməlidir.

---

# 16. realizm və həqiqilik hissi

yaradıcı açıq deyir:

> real hacking simulyasiyası məqsəd deyil.

rəylərin böyük hissəsi bunu qəbul edir.

müsbət oyunçu-lər tez-tez:

- “real deyil”;
- “gameified”;
- “puzzle/strategiya”

deyib yenə oyunu çox bəyənirlər.

Deməli Hacknet-də tapılan principle burada da görünür:

> **technical realizm requirement deyil; ardıcıl seçilmiş həqiqilik hissi daha vacibdir.**

Real terms, terminal, network graph, programs və cybersecurity references rol hissini dəstəkləyir.

---

# 17. Narrative və məzmun dizayn

hekayə oyunun ən böyük üstünlüklərindən biridir.

Narrative delivery:

- email;
- messages;
- mission məlumat;
- side stories;
- decisions;
- reputation;
- network findings.

rəylərdə hekayə:

- gripping;
- surprising;
- morally interesting;
- memorable

kimi təsvir olunur.

Bəzi mənfi geribildirim:

- twist-lərin kifayət qədər grounding olmaması;
- late hekayə-nin qarışıqlaşması;
- müəyyən seçim nəticələrin ağır olması

ilə bağlıdır.

Amma overall hekayə signal çox güclüdür.

---

# 18. seçim, Reputation və Hacker Identity

Midnight Protocol-un Hacknet-dən ən vacib fərqi budur.

oyunçu:

- bank hesabına toxuna bilər;
- privacy-ni qoruya bilər;
- black/white/grey hat direction seçə bilər;
- mission qəbul/reject edə bilər;
- side məzmun aça və bağlaya bilər;
- finals-ə təsir edə bilər.

Bu:

> “hacker kimi hiss edirəm”

rol hissi-sini:

> “mən necə hackerəm?”

səviyyəsinə çıxarır.

Bu çox güclü dizayn imkan-dir.

---

# 19. araşdırma və kəşf

Midnight Protocol-da:

- intranet;
- optional intel;
- side information;
- hidden ipucus;
- secrets;
- easter eggs

var.

yaradıcı curiosity-ni “real hacker” davranışının ən həqiqi tərəflərindən biri kimi görür.

Bu Hacknet ilə ortaqdır.

Amma difference:

Hacknet-də filesystem curiosity daha organic görünür.

Midnight Protocol-da taktiki mission grammar daha dominantdır.

Bu gələcək oyun üçün imkan göstərir:

> Hacknet-in organic information exploration-u + Midnight Protocol-un mənalı seçims-i birləşdirilə bilər.

---

# 20. Audio / Visual Presentation

müsbət geribildirim güclüdür.

Praise:

- minimalist UI;
- node animations;
- cyberpunk visual language;
- sound geribildirim;
- atmosphere;
- procedural/music feel.

peşəkar rəylərdə soundtrack variety bəzi hallarda zəiflik kimi qeyd olunur.

Lakin ümumi təqdimat oyunun ən güclü elementlərindəndir.

Bu genre üçün artıq ikinci dəfə eyni principle görünür:

> **audio/visual polish fake computer interface-i “software”dən “world”ə çevirir.**

---

# 21. Technical Issues

BUGS_COMPATIBILITY namizəd sayı:

- 12;
- 4 mənfi;
- 33.33% mənfi.

Volume böyük deyil.

Amma hesabat-larda:

- softlock;
- audio bug;
- lokallaşdırma text scaling;
- mission state;
- control/alias edge cases

görünür.

Hacknet ilə müqayisədə technical complaints əsas dominant uğursuzluq deyil.

---

# 22. Audience Segments

## 22.1. özünü haker kimi hiss etmə audience

Axtardığı:

- keyboard;
- terminal;
- cyber aesthetic;
- “I’m in” rol hissi.

Midnight Protocol burada güclüdür.

## 22.2. taktiki/puzzle audience

Axtardığı:

- planlama;
- alət dəsti;
- hərəkət büdcəsi;
- quruluş;
- mission optimization.

Bu Midnight Protocol-un Hacknet-dən daha yaxşı xidmət etdiyi audience-dir.

## 22.3. Narrative RPG audience

Axtardığı:

- characters;
- mystery;
- seçim;
- reputation;
- finals.

Oyunun çox güclü ikinci audience-i budur.

## 22.4. Real-hacking/simulation audience

Bu audience risklidir.

Midnight Protocol özünü simulator-dan daha çox taktiki RPG kimi position etdiyi üçün Hacknet-dən daha yaxşı expectation management edir.

Amma bəzi rəy müəllifi yenə:

> “bu hacking deyil, board game-dir”

deyir.

---

# 23. Yaradıcı məqsədi ilə oyunçu təcrübəsinin müqayisəsi

| yaradıcı intent | oyunçu outcome |
|---|---|
| Keyboard oyuna dalma hissi | Güclü rol hissi yaradır, amma UX çətinlik realdır |
| Fun over realizm | Böyük ölçüdə uğurludur |
| növbə əsaslı planlama | Speed stress azalır, taktiki identity yaranır |
| Simple board-game grammar | Öyrənilə bilir, amma system layering 1–3h çətinlik yaradır |
| Deep quruluş options | Real seçim var, amma mandatory/dominant quruluş riskləri qalır |
| Narrative focus | Güclü oyunda qalma amil-dir |
| Curiosity/secrets | müsbət, amma core taktiki loop qədər dominant deyil |

---

# 24. Uğurun izah hipotezləri

## 24.1. Distinctive concept

yalnız klaviatura ilə taktiki hacking RPG asanlıqla fərqlənir.

## 24.2. Strong experience stack

```text
typing
+ tactics
+ story
+ choices
+ cyber presentation
```

bir-birini dəstəkləyir.

## 24.3. Real oyunçunun qərar sərbəstliyi və təsiri

Hacknet-dən fərqli olaraq oyunçu identity və mission seçim daha sistemikdir.

## 24.4. Narrative taktiki oyun gedişi-i mənalı edir

Abstract nodes sadəcə puzzle deyil; hekayə context daşıyır.

## 24.5. Long-session audience üçün yüksək satisfaction

10h+ rəylərin 95.51%-i müsbət-dir.

Bu seçim qərəzi daşısa da, oyunu qəbul edən audience-də deep satisfaction olduğunu göstərir.

---

# 25. Niyə daha böyük hit olmayıb? — açıq hipotez

Bu sualın tam cavabı məlumat toplusu-də yoxdur.

Steam mağaza current display ilə verified API rəy snapshot arasında da count fərqi var, ona görə traction müqayisə ehtiyatla aparılmalıdır.

Mövcud dəlil bir neçə mümkün izah verir:

## 25.1. Concept izahı çətindir

“Hacking game” deyəndə bəzi oyunçu Hacknet/Uplink gözləyir.

“taktiki RPG” deyəndə isə terminal/keyboard niche görünür.

məhsul iki audience arasında qalır.

## 25.2. yalnız klaviatura ilə yüksək-çətinlik ilkin cəlbedicilik ola bilər

Fərqləndirir, amma eyni zamanda audience-i daraldır.

## 25.3. İlk 1–3 saat risklidir

Potential oyunçu təlim hissəsi-dan sonra core system mürəkkəblik ilə üzləşir.

## 25.4. taktiki board-game identity hacking audience-in bir hissəsinə uyğun deyil

məhsul quality yaxşı olsa da TAM daha dar ola bilər.

## 25.5. Discoverability/marketing

son dövr rəylərdə “niyə bu oyun bu qədər bilinmir?” fikri görünür.

Amma bunun səbəbini public rəy məlumatları ilə sübut etmək mümkün deyil.

**etibarlılıq: Low-Medium**

---

# 26. Bizim üçün saxlanmalı dizayn dərsləri

## Saxlamağa dəyər

### 1. rol hissi + systems integration

özünü haker kimi hiss etmə yalnız skin deyil.

qarşılıqlı əlaqə-la bağlanmalıdır.

### 2. Moral identity

oyunçu “hacker” olmaqdan əlavə “necə hacker” olduğunu seçə bilər.

### 3. taktiki planlama

Speed bacarıq yeganə çətinlik forması olmamalıdır.

### 4. alət dəsti preparation

Mission öncəsi qərar oyun gedişi-in hissəsi ola bilər.

### 5. Narrative nəticə

seçim hekayə və future options-a təsir edə bilər.

### 6. seçilmiş həqiqilik hissi

Real jargon və ardıcıl logic kifayətdir.

### 7. Keyboard as rol hissi device

Fiziki giriş mövzu ilə uyğun gələndə oyuna dalma hissi artır.

---

# 27. Qaçmalı olduğumuz risklər

## 1. Hidden information + geri dönməz uğursuzluq

Bu fairness-i dağıda bilər.

## 2. RNG nəticəni bacarıq-dən çox müəyyən etməsi

uğursuzluq learnable qalmalıdır.

## 3. Mandatory quruluş masquerading as seçim

alət sayı dərinlik demək deyil.

## 4. Repeated command overhead

Thematic giriş mexaniki tax-a çevrilməməlidir.

## 5. təlim hissəsi sonrası mürəkkəblik cliff

İlk təlim hissəsi keçildikdən sonra ilkin öyrətmə davam etməlidir.

## 6. Timer/trace curiosity-ni öldürməsi

araşdırma üçün nəfəs sahəsi lazımdır.

## 7. Genre expectation mismatch

mağaza promise actual əsas oyun dövrü-u düzgün anlatmalıdır.

---

# 28. imkan-lər

## 28.1. Hacknet oyuna dalma hissi + Midnight qərar sərbəstliyi

Ən güclü imkan:

- Hacknet-in organic filesystem/məlumat kəşfi-si;
- Midnight Protocol-un seçim/reputation/nəticə sistemi.

## 28.2. Explainable taktiki hacking

taktiki dərinlik saxla, amma təsadüfilik minimum və readable olsun.

## 28.3. Recon-before-alət dəsti

Mission haqqında əvvəlcədən:

- partial intel;
- target behavior;
- known defenses;
- qeyri-müəyyənlik level

ver.

oyunçu risk seçsin.

## 28.4. Flexible uğursuzluq bərpa

yenidən cəhd:

- re-plan;
- alət dəsti change;
- checkpoint;
- optional nəticə

ilə işləyə bilər.

## 28.5. Hybrid giriş

Keyboard rol hissi saxlanıla bilər, amma:

- autocomplete;
- history;
- aliases;
- click-equivalent optional shortcuts;
- context-aware suggestions

çətinlik-i azalda bilər.

## 28.6. Information → qərar → nəticə loop

```text
discover information
→ interpret
→ choose
→ act
→ world changes
```

bu janr üçün çox güclü sistemli core ola bilər.

---

# 29. Hacknet ilə ilkin yekun fərq

Hacknet:

> daha sadə, daha dərhal rol hissi, daha az sistemli seçim.

Midnight Protocol:

> daha dərin taktiki/identity systems, amma daha yüksək cognitive və fairness risk.

Bunu belə xülasə etmək olar:

```text
Hacknet
fast fantasy payoff
↓
simple loop
↓
repetition risk

Midnight Protocol
deeper decision model
↓
higher cognitive/system load
↓
fairness + onboarding + friction risk
```

Bizim gələcək concept üçün hədəf bu iki ekstrem arasında optimal nöqtə tapmaqdır.

---

# 30. Açıq suallar

1. Midnight Protocol-un aşağı rəy volume-unun əsas bazar səbəbi nədir?
2. yalnız klaviatura ilə giriş audience-i nə qədər daraldıb?
3. Demo conversion haqqında public məlumat varmı?
4. Workshop/level editor real long-tail yaradıbmı?
5. növbə əsaslı və optional real-time mode arasında usage nümunə məlumdurmu?
6. RNG complaint-lərin hansı hissəsi son patch-lərdən əvvəlki versiyaya aiddir?
7. Eyni taktiki dərinlik daha deterministic sistemlə daha geniş audience tapa bilərdimi?
8. seçim/reputation sistemi başqa interface-game-lərdə də eyni dəyəri verirmi?

Bu suallar oyunlararası araşdırma-də izlənməlidir.

---

# 31. Mənbələr

## Daxili repository

**[D1]** `data/processed/midnight-protocol/statistics.json`

**[D2]** `data/reports/midnight-protocol/summary.md`

**[D3]** `data/processed/midnight-protocol/samples/helpful_positive.csv`

**[D4]** `data/processed/midnight-protocol/samples/helpful_negative.csv`

**[D5]** `data/processed/midnight-protocol/samples/low_playtime.csv`

**[D6]** `data/processed/midnight-protocol/samples/recent_positive.csv`

**[D7]** `analysis/midnight-protocol/theme-analysis.md`

**[D8]** `config/aspect_taxonomy.yaml`

## Xarici

**[W1] Steam mağaza — Midnight Protocol**  
https://store.steampowered.com/app/1162700/

**[W2] Game yaradıcı — Hacking for answers in taktiki narrative game Midnight Protocol**  
https://www.gamedeveloper.com/design/hacking-answers-tactical-narrative-game-midnight-protocol

**[W3] Quarter to Three — Midnight Protocol hacks into the sweet spot between storytelling and strategiya**  
https://www.quartertothree.com/fp/2022/01/16/midnight-protocol-hacks-into-the-sweet-spot-between-storytelling-and-strategy/

**[W4] Softpedia — Midnight Protocol rəy**  
https://www.softpedia.com/reviews/games/pc/midnight-protocol-review-534571.shtml

---

# vəziyyət

**Mərhələ:** Midnight Protocol per-game deep araşdırma — əsas mərhələ tamamlanıb  
**məlumat toplusu:** 301 verified ingilisdilli Steam rəyi  
**mənfi rəys audited:** 48/48  
**bütün rəy toplusu üzrə namizəd əhatə:** 75.08%  
**Növbəti:** `analysis/comparisons/hacknet-vs-midnight-protocol.md`
