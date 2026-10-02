# Need to Know — Focused Research Kickoff

## Status

Bu sənəd Need to Know üçün focused comparative research istiqamətini müəyyən edir.

Need to Know Tier A deyil, **Tier B — Focused Comparative Research** target-dir.

Əsas məqsəd:

> **Orwell-un information-selection / surveillance / consequence modelinin oxşar premise-də niyə daha yüksək player satisfaction yaratdığını anlamaq.**

## Product snapshot

Steam App ID: **490930**

- Developer: Monomyth Games
- Publisher: Monomyth Games
- Release: 28 August 2018
- Single-player
- Current public Steam display: təxminən **175 review, 74% positive**
- Store positioning: surveillance thriller / political simulation / investigation.

Official promise:

- NSA-like Department of Liberty daxilində işləmək;
- citizen-lərin private data-sını araşdırmaq;
- guilt / danger qiymətləndirmək;
- privacy-ni qorumaq və ya surveillance state-i gücləndirmək;
- underground group-lara məlumat sızdırmaq;
- şəxsi fayda üçün classified information istifadə etmək;
- clearance level artdıqca daha güclü surveillance powers açmaq;
- qərarların mission outcomes-a təsir etməsi.

Bu promise Orwell-dan daha geniş agency və progression vəd edir.

## Niyə Orwell üçün yaxşı comparator-dır?

Orwell-un əsas loop-u:

    discover
    → contextualize
    → choose what to reveal
    → adviser acts
    → consequence

Need to Know isə kağız üzərində daha geniş model vəd edir:

    investigate
    → classify / decide guilt
    → choose action
    → gain clearance / powers
    → surveillance scope expands
    → consequence

Əgər daha geniş agency promise daha aşağı player satisfaction ilə nəticələnibsə, vacib sual yaranır:

> Problem concept-də deyil, execution-da harada yaranıb?

## Əsas research sualları

1. Need to Know-un əsas gameplay loop-u nə qədər aydındır?
2. Player qərarları həqiqətən alternative outcome yaradırmı?
3. Store promise ilə actual agency arasında mismatch varmı?
4. Surveillance power progression real mastery yaradırmı?
5. Clearance system gameplay depth yaradır, yoxsa sadəcə content gate-dir?
6. Mission-lər bir-birindən kifayət qədər fərqlənirmi?
7. Privacy vs security dilemma Orwell qədər organic hiss olunurmu?
8. Player choice-ları game-over və ya forced progression ilə ləğv olunurmu?
9. Tutorial/onboarding problemləri varmı?
10. Technical bugs/stability player sentiment-ə nə qədər təsir edib?
11. Early launch problemləri sonrakı patch-lərlə həll olunubmu?
12. Story və character quality mechanic-i daşıya bilirmi?
13. Repetition Orwell-dan daha yüksəkdirmi?
14. Need to Know-un daha geniş feature set-i həqiqətən daha yüksək meaningful-decision density yaradırmı?

## İlkin public-source siqnalları

Steam store daha geniş player freedom vəd edir:
- support privacy;
- support surveillance;
- leak data;
- personal gain;
- use increasing powers.

Ancaq public Steam Community feedback-də ən azı bəzi player-lər müəyyən story branch-lərdə advertised choice-in real olmadığını və progression üçün məcburi action tələb edildiyini bildirir.

Bu hələ final finding deyil.

Dataset audit bunu yoxlamalıdır.

## Research scope

Tier B olduğuna görə default workflow:

1. full Steam review dataset toplamaq — dataset kiçik olduğu üçün ucuzdur;
2. verify;
3. basic statistics;
4. bütün negative review-ləri manual audit etmək mümkün olarsa etmək;
5. helpful/recent positive review sample;
6. Orwell v5 taxonomy ilə full-corpus scan;
7. Need-to-Know-specific theme yalnız data tələb edərsə əlavə etmək;
8. qısa focused report:
   `analysis/need-to-know/focused-research.md`
9. comparison:
   `analysis/comparisons/orwell-vs-need-to-know.md`

Need to Know üçün default olaraq ayrıca böyük `deep-research.md` tələb olunmur. Research nəticəsi gözlənilməz yeni major pattern göstərərsə Tier A səviyyəsinə qaldırıla bilər.

## Public sources

**Steam Store**  
https://store.steampowered.com/app/490930/

**Official website**  
https://needtoknowgame.com/

**Kickstarter**  
https://www.kickstarter.com/projects/monomythgames/need-to-know-the-mass-surveillance-thriller-game

**Steam Community review example — launch/version caveat**  
https://steamcommunity.com/id/Colonial_Dagger/recommended/490930

## Növbəti addım

Config repository-yə əlavə olunub:

    key: need-to-know
    name: Need to Know
    steam_app_id: 490930

Növbəti mərhələ verified Steam review dataset collection-dır.
