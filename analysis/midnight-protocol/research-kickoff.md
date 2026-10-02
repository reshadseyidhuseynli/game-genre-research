# Midnight Protocol — Research Kickoff

## Status

Bu sənəd Midnight Protocol üzrə per-game deep research başlamazdan əvvəl ilkin product/market və design-intent snapshot-ıdır.

Steam review dataset hələ repository-də toplanmayıb. Ona görə bu sənəddəki player-feedback nəticələri yalnız public store/community/professional mənbələrdən gələn **ilkin hipotezlərdir**.

Final nəticələr Steam review dataset və theme/aspect analysis-dan sonra hazırlanacaq.

---

# 1. Niyə Midnight Protocol növbəti oyundur?

Midnight Protocol Hacknet üçün ən informativ comparison target-lərdən biridir.

Ortaq cəhətlər:

- hacking fantasy;
- terminal/keyboard interaction;
- fictional computer environment;
- narrative-driven structure;
- information discovery;
- cyber terminology;
- single-player focus.

Əsas fərq:

> Hacknet real-time/command-sequence yönümlü adventure-hacking loop qurur, Midnight Protocol isə hacking-i turn-based tactical/network-crawling sisteminə çevirir.

Bu müqayisə aşağıdakı sualı test etməyə imkan verir:

> Hacknet-də gördüyümüz repetition və shallow-decision problemini daha tactical, turn-based və deck/program sistemi həll edə bilirmi; yoxsa bunun əvəzində yeni friction və RNG problemləri yaranır?

---

# 2. Product snapshot

Steam App ID: **1162700**

- Name: Midnight Protocol
- Developer: LuGus Studios
- Publisher: Iceberg Interactive
- Release: 13 October 2021
- Base US price: **$14.99**
- Steam review status, 2026-10-02: təxminən **238 review, 87% positive**
- Steam tags arasında: Hacking, Typing, Story Rich, Atmospheric, Turn-Based Strategy, Tactical RPG, Investigation
- Steam Workshop və level editor dəstəyi var.

Store positioning:

> tactical narrative-driven RPG with unique keyboard-only controls

Core promise:

- servers hack et;
- security systems-i keç;
- encrypted secrets tap;
- doxx olunmağının səbəbini araşdır;
- yalnız keyboard ilə fictional terminal mühitində oyna.

Bu positioning Hacknet-dən daha açıq şəkildə **tactical RPG / strategy** dilindən istifadə edir.

---

# 3. Developer intent — ən vacib faktlar

Game Developer-in Sam Agten ilə 2022 müsahibəsi çox yüksək dəyərli mənbədir.

## 3.1. Problem statement

Developer hacking oyunlarında iki ekstrem görürdü:

1. hacking sadə secondary minigame olur;
2. oyun çox simulationist olmağa çalışır və accessibility azalır.

Midnight Protocol bu iki ekstrem arasında daha çox design space olduğunu yoxlamaq üçün yaranıb.

Bu, bizim research sualımıza birbaşa uyğundur.

---

## 3.2. Keyboard-only control təsadüfi gimmick deyil

Developer keyboard-only input-u oyunun “heart”-ı kimi təsvir edir.

Məqsəd:

- oyunçunun real fiziki keyboard-unun hacker fantasy ilə birləşməsi;
- command input ilə intent-in birbaşa ifadə olunması;
- mouse-driven multi-step interaction əvəzinə typing;
- old-school terminal hissi.

Developer özü downside olaraq discoverability problemini qəbul edir.

Yəni dizayn trade-off əvvəldən şüurludur:

```text
immersion/fantasy
vs
discoverability/accessibility
```

Bu Hacknet-də tapdığımız terminal expectation problemi ilə comparison üçün xüsusilə dəyərlidir.

---

## 3.3. Realism məqsəd deyil

Developer açıq deyir ki:

- məqsəd real hacking simulyasiyası olmayıb;
- “fun game first, hacking theme second” yanaşması var;
- real-world terminology narrative üçün istifadə olunur;
- gameplay real hacking-i təmsil etmir;
- terminal input bəzi real Linux command davranışlarından ilham alır.

Bu Hacknet-də tapdığımız **selective authenticity** prinsipinə çox yaxındır.

Deməli iki fərqli developer komandası oxşar nəticəyə gəlib:

> tam realism-dən çox, real texniki işarələrlə qurulan inandırıcı fantasy.

Bu cross-game principle ola bilər, amma player data ilə ayrıca yoxlanmalıdır.

---

## 3.4. Onboarding ən çətin hissələrdən biri olub

Developer terminalın qorxuducu ola bildiyini və:

- program management;
- resource system;
- terminal interaction

kimi sistemlərin onboarding-i çətinləşdirdiyini deyir.

Tutorial/demo oyunun ən çox iteration edilən hissələrindən biri olub və convention playtest-lərindən geniş feedback toplanıb.

Bu bizim üçün güclü comparison sualı yaradır:

> Hacknet və Midnight Protocol hər ikisi hacker fantasy üçün terminal istifadə edir, amma terminalın yaratdığı onboarding cost-u necə idarə edirlər?

---

## 3.5. Board-game design əsas struktur təsiridir

Midnight Protocol-un hacking sistemi board-game thinking-dən yaranıb.

Core turn language sadə saxlanılıb:

- hər turn iki action;
- move;
- current node ilə interact;
- ability istifadə et.

Sonrakı sistemlər bu sadə grammar üzərində qurulur.

Developer-in maraqlı design ideyası:

> player action-ları sadədir, amma command-line presentation onları daha mürəkkəb və “hacker-like” hiss etdirir.

Bu bizim Hacknet analizindəki bir fikri təkrarlayır:

> perceived complexity və actual mechanical complexity eyni şey deyil.

---

## 3.6. Real-time prototip turn-based olub

İlk design real-time düşünülüb.

Early playtest göstərib ki, bu versiya:

- stressli;
- əyləncəsiz

hiss olunur.

Nəticədə turn-based sistemə keçilib.

Bu Hacknet ilə çox vacib contrast-dır:

- Hacknet trace və timing ilə real-time pressure yaradır;
- Midnight Protocol planning üçün turn-based breathing room verir.

Comparison-da bu dəyişmənin:

- tension;
- mastery;
- repetition;
- fairness;
- accessibility

üzərində təsiri ayrıca araşdırılmalıdır.

---

## 3.7. Development zamanı narrative focus artıb

Developer bildirir ki, layihə irəlilədikcə:

- daha çox complex program/network əlavə etməkdənsə;
- narrative və hacking theme-in qeyri-adi istifadəsinə

daha çox fokus verilib.

Fourth-wall secrets və easter egg-lər də bu curiosity hissinə xidmət edir.

Bu Hacknet ilə başqa güclü ortaq pattern-dir:

> hacking fantasy yalnız “hack mechanic” ilə deyil, curiosity/discovery content-i ilə yaşayır.

---

# 4. Public review-lərdən ilkin müsbət siqnallar

Professional və community source-larda təkrarlanan ilkin müsbət mövzular:

## 4.1. Keyboard fantasy

Keyboard-only interaction bir çox reviewer üçün:

- tactile;
- satisfying;
- immersive;
- “feel like a hacker”

effekti yaradır.

Bu Hacknet-dəki HACKER_FANTASY nəticəsi ilə çox yaxın görünür.

## 4.2. Daha tactical decision-making

Review-lərdə:

- program/deck seçimi;
- stealth vs aggression;
- trace management;
- movement;
- network risk;
- resource planning

Hacknet-in “tool = port key” strukturundan daha strateji görünür.

Bunun review dataset-də həqiqətən satisfaction driver olub-olmadığını yoxlamaq lazımdır.

## 4.3. Narrative + mechanic integration

Public reviews story-ni və hacking loop-u birlikdə müsbət qeyd edir.

Reputation və decision system-ləri də narrative outcome ilə əlaqələndirilir.

## 4.4. Turn-based planning

Bəzi oyunçular real-time hacking stress-i əvəzinə plan qurmağa imkan verən turn-based sistemi üstünlük hesab edir.

---

# 5. Public source-lardan ilkin risk siqnalları

Bunlar final nəticə deyil. Steam dataset ilə test ediləcək hipotezlərdir.

## 5.1. Keyboard-only friction

Review-lərdə:

- typo;
- command context;
- mouse olmaması;
- shortcut öyrənmək

friction kimi görünür.

Burada eyni sistem həm immersion driver, həm usability riskidir.

Bu Hacknet-də də görünən paradoksun daha ekstrem versiyası ola bilər.

---

## 5.2. Interface repetition

Bəzi professional review-lər bir müddətdən sonra eyni sparse computer interface-ə baxmağın yorucu olduğunu qeyd edir.

Bu Hacknet-dəki repetition-dan fərqli problem ola bilər:

- Hacknet: action sequence repetition;
- Midnight Protocol: visual/interface sameness + tactical loop repetition.

Dataset bunu ayırmağa kömək etməlidir.

---

## 5.3. RNG və retry/save-scumming

Steam-də helpful negative feedback-də turn-based system ilə bağlı ciddi complaint görünür:

- RNG bəzən unwinnable və ya ədalətsiz hiss olunur;
- failure mastery yox, “better roll” gözləməyə çevrilə bilər;
- mission repeat bəzi oyunçulara save-scumming kimi görünür.

Bu Hacknet-in failure modelindən kəskin fərqdir.

Comparison question:

> Real-time skill failure-ni aradan qaldırarkən Midnight Protocol system/RNG fairness problemi yaradıbmı?

---

## 5.4. Turn caps

Bəzi oyunçular trace/resource puzzle-ni sevsə də mission turn-cap-lərin:

- experimentation;
- slow tactical play;
- “stay in the network” fantasy

ilə toqquşduğunu yazır.

Bu urgency-nin necə tətbiq edilməsinin ayrıca design problemi olduğunu göstərir.

---

## 5.5. No manual save / missed content

Community review-lərdə:

- branching;
- side mission;
- dialogue choices

olmasına baxmayaraq manual save olmaması complaint kimi görünür.

Bu çox maraqlı design contradiction-dır:

```text
meaningful choices
+
missable content
+
limited save control
=
choice anxiety / frustration
```

Player agency üçün yalnız seçim vermək kifayət deyil; recovery model də vacibdir.

---

## 5.6. Soundtrack variety

Bir neçə review soundtrack-in funksional, amma az variety-li olduğunu qeyd edir.

Hacknet-də audio güclü satisfaction driver olduğu üçün bu comparison-da ayrıca izlənməlidir.

---

# 6. Hacknet ilə ilkin contrast

| Mövzu | Hacknet | Midnight Protocol — ilkin hipotez |
|---|---|---|
| Hacker fantasy | Terminal + real-time typing | Keyboard-only + tactical command typing |
| Core hacking | Port/tool sequence | Turn-based network crawler |
| Pressure | Real-time trace | Turn/action economy + trace |
| Decision depth | Tez-tez shallow tool-key loop | Deck/program/resource decisions daha dərin görünür |
| Main repetition risk | Eyni command sequence | Interface sameness / repeated tactical structure ola bilər |
| Realism | Selective authenticity | Developer açıq şəkildə fun-first abstraction seçib |
| Story | Files/email/mystery | Narrative RPG + reputation/choices |
| Agency | Məhdud və əsasən scripted | Reputation/path/mission choices daha güclü görünür |
| Failure | Speed/timing və scripted events | Tactical failure + RNG/retry riski |
| Input | Terminal + GUI birlikdə | Keyboard-only |
| Accessibility | GUI müəyyən safety net verir | Keyboard-only discoverability cost-u daha yüksək ola bilər |

Bu cədvəl hələ final comparison deyil.

---

# 7. Əsas research sualları

Midnight Protocol dataset-i toplandıqdan sonra prioritet suallar:

1. **Keyboard-only control** player feedback-də immersion driver-dır, friction-dır, yoxsa ikisi də?
2. **Turn-based tactical system** Hacknet-dəki repetition problemini həll edirmi?
3. Deck/program system həqiqətən **meaningful build choice** yaradırmı?
4. RNG/failure fairness nə qədər böyük complaint-dir?
5. Turn caps və trace pressure tension yaradır, yoxsa experimentation-ı öldürür?
6. Reputation və moral choice-lar real **player agency/consequence** yaradırmı?
7. Narrative core loop-u gücləndirir, yoxsa mechanic-dan ayrı qalır?
8. Investigation/discovery nə qədər əhəmiyyətlidir?
9. Onboarding və command discoverability negative review-lərdə nə qədər görünür?
10. Niyə çox müsbət critical/player response olmasına baxmayaraq Steam review volume Hacknet-dən çox aşağıdır?
11. Problem game quality, discoverability, positioning, niche complexity, launch timing, marketing reach, yoxsa başqa faktordur?
12. Workshop/level editor long-tail yaradıb, yoxsa community scale çox kiçik qalıb?

---

# 8. Dataset toplandıqdan sonra metod

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

Reusable semantic taxonomy:

`config/aspect_taxonomy.yaml`

Midnight Protocol üçün yeni aspect-lər yalnız data tələb edərsə əlavə edilməlidir.

---

# 9. İlkin comparison hipotezi

Hazırda yalnız external evidence əsasında ən dəyərli hipotez budur:

> **Midnight Protocol Hacknet-in shallow hacking loop problemini daha tactical və systemic mechanics ilə həll etməyə çalışır, amma bunun müqabilində daha yüksək cognitive/onboarding cost, keyboard-only friction və RNG/retry riskləri yaradır.**

Əgər Steam dataset bunu təsdiqləsə, bizim gələcək oyun üçün çox vacib principle çıxacaq:

> **Depth artırmaq repetition-u azalda bilər, amma depth-in özü accessibility və fairness cost-u yaradır. Əsas məsələ “daha çox sistem” deyil, optimal decision density-dir.**

Bu nəticə hələ provisional-dır.

---

# 10. Public sources

## [W1] Steam Store — Midnight Protocol

https://store.steampowered.com/app/1162700/

App ID, release, developer/publisher, tags, review status, store positioning və feature-lər.

## [W2] Game Developer — Road to IGF 2022 interview

https://www.gamedeveloper.com/design/hacking-answers-tactical-narrative-game-midnight-protocol

Ən vacib developer-intent mənbəyi: board-game inspiration, keyboard-only design, realism philosophy, onboarding iteration, turn-based transition, narrative focus.

## [W3] Softpedia review

https://www.softpedia.com/reviews/games/pc/midnight-protocol-review-534571.shtml

Keyboard-only immersion/friction, hacking mechanics, narrative və soundtrack haqqında professional review.

## [W4] Quarter to Three

https://www.quartertothree.com/fp/2022/01/16/midnight-protocol-hacks-into-the-sweet-spot-between-storytelling-and-strategy/

Keyboard interaction və tactile/kinesthetic hacker fantasy haqqında review.

## [W5] Last Word on Gaming review

https://lastwordongaming.com/2021/10/18/midnight-protocol-this-hacking-rpg-will-make-you-feel-cool/

Hacker fantasy, turn-based system, interface repetition və learning curve haqqında review.

## [W6] Steam Community reviews

https://steamcommunity.com/app/1162700/reviews/?browsefilter=toprated&l=english

Player feedback: RNG, turn caps, keyboard controls, depth, save system.

## [W7] Steam Community discussions

https://steamcommunity.com/app/1162700/discussions/

Onboarding, controls, waiting, tutorial və quality-of-life complaint nümunələri.

## [W8] SteamDB

https://steamdb.info/app/1162700/

Current/base price və public store history context.

---

# 11. Növbəti konkret addım

Repository config-də artıq:

```yaml
key: midnight-protocol
name: Midnight Protocol
steam_app_id: 1162700
```

əlavə olunub.

İndi Steam dataset toplanmalı və verify edilməlidir.

Dataset push edildikdən sonra bu kickoff sənədi final `deep-research.md` üçün input olacaq.
