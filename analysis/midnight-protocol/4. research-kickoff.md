# Midnight Protocol — araşdırma Kickoff

## Status

Bu sənəd Midnight Protocol araşdırma başlamazdan əvvəl hazırlanmış ilkin kickoff sənədidir və historical planlama context kimi saxlanılır.

araşdırma artıq tamamlanıb.

Əsas yekun sənədlər:

- `analysis/midnight-protocol/deep-research.md`
- `analysis/midnight-protocol/theme-analysis.md`
- `analysis/comparisons/hacknet-vs-midnight-protocol.md`

Aşağıdakı bölmələr məlumat toplusu-dən əvvəl qurulmuş hipotezləri göstərir və final nəticə kimi istifadə edilməməlidir.

---

# 1. Niyə Midnight Protocol növbəti oyundur?

Midnight Protocol Hacknet üçün ən informativ müqayisə target-lərdən biridir.

Ortaq cəhətlər:

- hacking fantasy;
- terminal/keyboard qarşılıqlı əlaqə;
- fictional computer environment;
- narrative-driven structure;
- information discovery;
- cyber terminology;
- single-oyunçu focus.

Əsas fərq:

> Hacknet real-time/command-sequence yönümlü adventure-hacking loop qurur, Midnight Protocol isə hacking-i turn-based tactical/network-crawling sisteminə çevirir.

Bu müqayisə aşağıdakı sualı test etməyə imkan verir:

> Hacknet-də gördüyümüz təkrarçılıq və dayaz-qərar problemini daha tactical, turn-based və deck/program sistemi həll edə bilirmi; yoxsa bunun əvəzində yeni çətinlik və RNG problemləri yaranır?

---

# 2. məhsul snapshot

Steam App ID: **1162700**

- Name: Midnight Protocol
- yaradıcı: LuGus Studios
- Publisher: Iceberg Interactive
- Release: 13 October 2021
- Base US price: **$14.99**
- Steam rəy status, 2026-10-02: təxminən **238 rəy, 87% müsbət**
- Steam tags arasında: Hacking, Typing, hekayə Rich, Atmospheric, Turn-Based Strategy, Tactical RPG, Investigation
- Steam Workshop və level editor dəstəyi var.

mağaza positioning:

> tactical narrative-driven RPG with unique keyboard-only controls

Core promise:

- servers hack et;
- security systems-i keç;
- encrypted secrets tap;
- doxx olunmağının səbəbini araşdır;
- yalnız keyboard ilə fictional terminal mühitində oyna.

Bu positioning Hacknet-dən daha açıq şəkildə **tactical RPG / strategy** dilindən istifadə edir.

---

# 3. yaradıcı intent — ən vacib faktlar

Game yaradıcı-in Sam Agten ilə 2022 müsahibəsi çox yüksək dəyərli mənbədir.

## 3.1. Problem statement

yaradıcı hacking oyunlarında iki ekstrem görürdü:

1. hacking sadə secondary minigame olur;
2. oyun çox simulationist olmağa çalışır və əlçatanlıq azalır.

Midnight Protocol bu iki ekstrem arasında daha çox dizayn space olduğunu yoxlamaq üçün yaranıb.

Bu, bizim araşdırma sualımıza birbaşa uyğundur.

---

## 3.2. Keyboard-only control təsadüfi gimmick deyil

yaradıcı keyboard-only giriş üsulu-u oyunun “heart”-ı kimi təsvir edir.

Məqsəd:

- oyunçunun real fiziki keyboard-unun hacker fantasy ilə birləşməsi;
- command giriş üsulu ilə intent-in birbaşa ifadə olunması;
- mouse-driven multi-step qarşılıqlı əlaqə əvəzinə typing;
- old-school terminal hissi.

yaradıcı özü downside olaraq discoverability problemini qəbul edir.

Yəni dizayn kompromis əvvəldən şüurludur:

```text
immersion/fantasy
vs
discoverability/accessibility
```

Bu Hacknet-də tapdığımız terminal expectation problemi ilə müqayisə üçün xüsusilə dəyərlidir.

---

## 3.3. realizm məqsəd deyil

yaradıcı açıq deyir ki:

- məqsəd real hacking simulyasiyası olmayıb;
- “fun game first, hacking mövzu second” yanaşması var;
- real-world terminology narrative üçün istifadə olunur;
- oyun gedişi real hacking-i təmsil etmir;
- terminal giriş üsulu bəzi real Linux command davranışlarından ilham alır.

Bu Hacknet-də tapdığımız **seçilmiş həqiqilik hissi** prinsipinə çox yaxındır.

Deməli iki fərqli yaradıcı komandası oxşar nəticəyə gəlib:

> tam realizm-dən çox, real texniki işarələrlə qurulan inandırıcı fantasy.

Bu oyunlararası principle ola bilər, amma oyunçu məlumat ilə ayrıca yoxlanmalıdır.

---

## 3.4. İlkin öyrətmə ən çətin hissələrdən biri olub

yaradıcı terminalın qorxuducu ola bildiyini və:

- program management;
- resource system;
- terminal qarşılıqlı əlaqə

kimi sistemlərin ilkin öyrətmə-i çətinləşdirdiyini deyir.

təlim hissəsi/demo oyunun ən çox iteration edilən hissələrindən biri olub və convention playtest-lərindən geniş geribildirim toplanıb.

Bu bizim üçün güclü müqayisə sualı yaradır:

> Hacknet və Midnight Protocol hər ikisi hacker fantasy üçün terminal istifadə edir, amma terminalın yaratdığı ilkin öyrətmə cost-u necə idarə edirlər?

---

## 3.5. Board-game dizayn əsas struktur təsiridir

Midnight Protocol-un hacking sistemi board-game thinking-dən yaranıb.

Core turn language sadə saxlanılıb:

- hər turn iki action;
- move;
- current node ilə interact;
- ability istifadə et.

Sonrakı sistemlər bu sadə grammar üzərində qurulur.

yaradıcı-in maraqlı dizayn ideyası:

> oyunçu action-ları sadədir, amma command-line presentation onları daha mürəkkəb və “hacker-like” hiss etdirir.

Bu bizim Hacknet analizindəki bir fikri təkrarlayır:

> perceived mürəkkəblik və actual mexaniki mürəkkəblik eyni şey deyil.

---

## 3.6. Real-time prototip turn-based olub

İlk dizayn real-time düşünülüb.

Early playtest göstərib ki, bu versiya:

- stressli;
- əyləncəsiz

hiss olunur.

Nəticədə turn-based sistemə keçilib.

Bu Hacknet ilə çox vacib contrast-dır:

- Hacknet trace və timing ilə real-time pressure yaradır;
- Midnight Protocol planlama üçün turn-based breathing room verir.

müqayisə-da bu dəyişmənin:

- tension;
- mastery;
- təkrarçılıq;
- fairness;
- əlçatanlıq

üzərində təsiri ayrıca araşdırılmalıdır.

---

## 3.7. Development zamanı narrative focus artıb

yaradıcı bildirir ki, layihə irəlilədikcə:

- daha çox complex program/network əlavə etməkdənsə;
- narrative və hacking mövzu-in qeyri-adi istifadəsinə

daha çox fokus verilib.

Fourth-wall secrets və easter egg-lər də bu curiosity hissinə xidmət edir.

Bu Hacknet ilə başqa güclü ortaq nümunə-dir:

> hacking fantasy yalnız “hack mexanika” ilə deyil, curiosity/discovery content-i ilə yaşayır.

---

# 4. Public rəy-lərdən ilkin müsbət siqnallar

peşəkar və icma source-larda təkrarlanan ilkin müsbət mövzular:

## 4.1. Keyboard fantasy

Keyboard-only qarşılıqlı əlaqə bir çox reviewer üçün:

- tactile;
- satisfying;
- immersive;
- “feel like a hacker”

effekti yaradır.

Bu Hacknet-dəki HACKER_FANTASY nəticəsi ilə çox yaxın görünür.

## 4.2. Daha tactical qərar-making

rəy-lərdə:

- program/deck seçimi;
- stealth vs aggression;
- trace management;
- movement;
- network risk;
- resource planlama

Hacknet-in “tool = port key” strukturundan daha strateji görünür.

Bunun rəy məlumat toplusu-də həqiqətən satisfaction amil olub-olmadığını yoxlamaq lazımdır.

## 4.3. Narrative + mexanika integration

Public reviews hekayə-ni və hacking loop-u birlikdə müsbət qeyd edir.

Reputation və qərar sistemi-ləri də narrative outcome ilə əlaqələndirilir.

## 4.4. Turn-based planlama

Bəzi oyunçular real-time hacking stress-i əvəzinə plan qurmağa imkan verən turn-based sistemi üstünlük hesab edir.

---

# 5. Public source-lardan ilkin risk siqnalları

Bunlar final nəticə deyil. Steam məlumat toplusu ilə test ediləcək hipotezlərdir.

## 5.1. Keyboard-only çətinlik

rəy-lərdə:

- typo;
- command context;
- mouse olmaması;
- shortcut öyrənmək

çətinlik kimi görünür.

Burada eyni sistem həm oyuna dalma hissi amil, həm usability riskidir.

Bu Hacknet-də də görünən paradoksun daha ekstrem versiyası ola bilər.

---

## 5.2. Interface təkrarçılıq

Bəzi peşəkar rəy-lər bir müddətdən sonra eyni sparse computer interface-ə baxmağın yorucu olduğunu qeyd edir.

Bu Hacknet-dəki təkrarçılıq-dan fərqli problem ola bilər:

- Hacknet: action sequence təkrarçılıq;
- Midnight Protocol: visual/interface sameness + tactical loop təkrarçılıq.

məlumat toplusu bunu ayırmağa kömək etməlidir.

---

## 5.3. RNG və retry/save-scumming

Steam-də faydalı mənfi geribildirim-də turn-based system ilə bağlı ciddi complaint görünür:

- RNG bəzən unwinnable və ya ədalətsiz hiss olunur;
- uğursuzluq mastery yox, “better roll” gözləməyə çevrilə bilər;
- mission repeat bəzi oyunçulara save-scumming kimi görünür.

Bu Hacknet-in uğursuzluq modelindən kəskin fərqdir.

müqayisə question:

> Real-time bacarıq uğursuzluq-ni aradan qaldırarkən Midnight Protocol system/RNG fairness problemi yaradıbmı?

---

## 5.4. Turn caps

Bəzi oyunçular trace/resource puzzle-ni sevsə də mission turn-cap-lərin:

- experimentation;
- slow tactical play;
- “stay in the network” fantasy

ilə toqquşduğunu yazır.

Bu urgency-nin necə tətbiq edilməsinin ayrıca dizayn problemi olduğunu göstərir.

---

## 5.5. No manual save / missed content

icma rəy-lərdə:

- branching;
- side mission;
- dialogue seçimlər

olmasına baxmayaraq manual save olmaması complaint kimi görünür.

Bu çox maraqlı dizayn contradiction-dır:

```text
meaningful choices
+
missable content
+
limited save control
=
choice anxiety / frustration
```

oyunçu qərar sərbəstliyi üçün yalnız seçim vermək kifayət deyil; recovery model də vacibdir.

---

## 5.6. Soundtrack variety

Bir neçə rəy soundtrack-in funksional, amma az variety-li olduğunu qeyd edir.

Hacknet-də audio güclü satisfaction amil olduğu üçün bu müqayisə-da ayrıca izlənməlidir.

---

# 6. Hacknet ilə ilkin contrast

| Mövzu | Hacknet | Midnight Protocol — ilkin hipotez |
|---|---|---|
| Hacker fantasy | Terminal + real-time typing | Keyboard-only + tactical command typing |
| Core hacking | Port/tool sequence | Turn-based network crawler |
| Pressure | Real-time trace | Turn/hərəkət büdcəsi + trace |
| qərar dərinlik | Tez-tez dayaz tool-key loop | Deck/program/resource decisions daha dərin görünür |
| Main təkrarçılıq risk | Eyni əmr ardıcıllığı | Interface sameness / repeated tactical structure ola bilər |
| realizm | seçilmiş həqiqilik hissi | yaradıcı açıq şəkildə fun-first abstraction seçib |
| hekayə | Files/email/mystery | Narrative RPG + reputation/seçimlər |
| qərar sərbəstliyi | Məhdud və əsasən scripted | Reputation/path/mission seçimlər daha güclü görünür |
| uğursuzluq | Speed/timing və scripted events | Tactical uğursuzluq + RNG/retry riski |
| giriş üsulu | Terminal + GUI birlikdə | Keyboard-only |
| əlçatanlıq | GUI müəyyən safety net verir | Keyboard-only discoverability cost-u daha yüksək ola bilər |

Bu cədvəl hələ final müqayisə deyil.

---

# 7. Əsas araşdırma sualları

Midnight Protocol məlumat toplusu-i toplandıqdan sonra prioritet suallar:

1. **Keyboard-only control** oyunçu geribildirim-də oyuna dalma hissi amil-dır, çətinlik-dır, yoxsa ikisi də?
2. **Turn-based tactical system** Hacknet-dəki təkrarçılıq problemini həll edirmi?
3. Deck/program system həqiqətən **meaningful build seçim** yaradırmı?
4. RNG/uğursuzluq fairness nə qədər böyük complaint-dir?
5. Turn caps və trace pressure tension yaradır, yoxsa experimentation-ı öldürür?
6. Reputation və etik seçim-lar real **oyunçu qərar sərbəstliyi/nəticə** yaradırmı?
7. Narrative əsas oyun dövrü-u gücləndirir, yoxsa mexanika-dan ayrı qalır?
8. Investigation/discovery nə qədər əhəmiyyətlidir?
9. İlkin öyrətmə və command discoverability mənfi rəy-lərdə nə qədər görünür?
10. Niyə çox müsbət critical/oyunçu response olmasına baxmayaraq Steam rəy volume Hacknet-dən çox aşağıdır?
11. Problem game quality, discoverability, positioning, niche mürəkkəblik, launch timing, marketing reach, yoxsa başqa faktordur?
12. Workshop/level editor long-tail yaradıb, yoxsa icma scale çox kiçik qalıb?

---

# 8. məlumat toplusu toplandıqdan sonra metod

Hacknet ilə eyni pipeline:

```text
Steam metadata
→ English review collection
→ verification
→ preprocessing
→ basic statistics
→ candidate theme scan
→ semantic audit
→ external research synthesis
→ per-game deep research
→ Hacknet vs Midnight Protocol comparison
```

Reusable məna yönümlü taxonomy:

`config/aspect_taxonomy.yaml`

Midnight Protocol üçün yeni aspect-lər yalnız məlumat tələb edərsə əlavə edilməlidir.

---

# 9. İlkin müqayisə hipotezi

Hazırda yalnız external dəlil əsasında ən dəyərli hipotez budur:

> **Midnight Protocol Hacknet-in dayaz hacking loop problemini daha tactical və systemic mexanikalar ilə həll etməyə çalışır, amma bunun müqabilində daha yüksək cognitive/ilkin öyrətmə cost, keyboard-only çətinlik və RNG/retry riskləri yaradır.**

Əgər Steam məlumat toplusu bunu təsdiqləsə, bizim gələcək oyun üçün çox vacib principle çıxacaq:

> **dərinlik artırmaq təkrarçılıq-u azalda bilər, amma dərinlik-in özü əlçatanlıq və fairness cost-u yaradır. Əsas məsələ “daha çox sistem” deyil, optimal qərar density-dir.**

Bu nəticə hələ provisional-dır.

---

# 10. Public sources

## [W1] Steam mağaza — Midnight Protocol

https://store.steampowered.com/app/1162700/

App ID, release, yaradıcı/publisher, tags, rəy status, mağaza positioning və feature-lər.

## [W2] Game yaradıcı — Road to IGF 2022 interview

https://www.gamedeveloper.com/design/hacking-answers-tactical-narrative-game-midnight-protocol

Ən vacib yaradıcı-intent mənbəyi: board-game inspiration, keyboard-only dizayn, realizm philosophy, ilkin öyrətmə iteration, turn-based transition, narrative focus.

## [W3] Softpedia rəy

https://www.softpedia.com/reviews/games/pc/midnight-protocol-review-534571.shtml

Keyboard-only oyuna dalma hissi/çətinlik, hacking mexanikalar, narrative və soundtrack haqqında peşəkar rəy.

## [W4] Quarter to Three

https://www.quartertothree.com/fp/2022/01/16/midnight-protocol-hacks-into-the-sweet-spot-between-storytelling-and-strategy/

Keyboard qarşılıqlı əlaqə və tactile/kinesthetic hacker fantasy haqqında rəy.

## [W5] Last Word on Gaming rəy

https://lastwordongaming.com/2021/10/18/midnight-protocol-this-hacking-rpg-will-make-you-feel-cool/

Hacker fantasy, turn-based system, interface təkrarçılıq və learning curve haqqında rəy.

## [W6] Steam icma reviews

https://steamcommunity.com/app/1162700/reviews/?browsefilter=toprated&l=english

oyunçu geribildirim: RNG, turn caps, keyboard controls, dərinlik, save system.

## [W7] Steam icma discussions

https://steamcommunity.com/app/1162700/discussions/

İlkin öyrətmə, controls, waiting, təlim hissəsi və quality-of-life complaint nümunələri.

## [W8] SteamDB

https://steamdb.info/app/1162700/

Current/base price və public mağaza history context.

---

# 11. araşdırma tamamlandıqdan sonrakı qeyd

Repository config-də artıq:

```yaml
key: midnight-protocol
name: Midnight Protocol
steam_app_id: 1162700
```

əlavə olunub.

Steam məlumat toplusu sonradan toplanıb və verify edilib: **301 English rəy**.

Bu kickoff-da qurulan əsas hipotezlər final araşdırma-də test edilib. Cari nəticələr üçün `analysis/midnight-protocol/deep-research.md` istifadə olunmalıdır.
