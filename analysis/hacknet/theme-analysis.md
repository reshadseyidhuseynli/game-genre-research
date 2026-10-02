# Hacknet — Review Theme Analizi

## 1. Məqsəd

Bu sənəd Hacknet üçün 11,773 verified Steam review üzərində aparılan full-corpus theme candidate scan və onun semantic audit nəticələrini saxlayır.

Bu sənədin rolu:

- review-lərdə hansı mövzuların geniş yayıldığını ölçmək;
- hansı mövzuların negative review-lərdə normadan daha çox toplandığını görmək;
- keyword nəticələrini semantic audit ilə yoxlamaq;
- Hacknet üzrə design/product nəticələrini daha ölçülə bilən evidence ilə gücləndirmək.

Bu sənəd **final full-dataset aspect sentiment classification deyil**.

Hazır metod iki mərhələdən ibarətdir:

1. bütün 11,773 review üzərində deterministik regex/keyword candidate retrieval;
2. hər theme üçün recommendation və playtime cohort-ları üzrə audit sample-larının semantic yoxlanması.

Full LLM classification infrastructure hazırda yoxdur. Buna görə aşağıdakı rəqəmlər “theme-i müsbət qiymətləndirən review faizi” kimi şərh edilməməlidir.

---

# 2. Dataset bazası

- Total verified reviews: **11,773**
- Positive reviews: **11,082**
- Negative reviews: **691**
- Dataset overall positive ratio: **94.13%**
- Dataset overall negative ratio: **5.87%**
- Ən azı bir theme candidate-i tutulan review: **6,009**
- Candidate coverage: **51.04%**

Candidate coverage-in 51% olması o demək deyil ki, qalan review-lər bu mövzular haqqında heç nə demir. Regex retrieval yalnız açıq lexical siqnalları tutur. Qısa, zarafat tipli və ya başqa sözlərlə eyni fikri bildirən review-lər qaça bilər.

---

# 3. Rəqəmləri necə oxumaq lazımdır?

Məsələn:

- REPETITION candidate-i 517 review-da tapılıb;
- onların 120-si negative Steam review-dur;
- həmin qrupun negative review nisbəti 23.21%-dir.

Amma bu:

> “Repetition haqqında danışanların 23.21%-i repetition-dan narazıdır”

demək deyil.

Düzgün şərh:

> “Repetition söz və pattern-ləri ilə tutulmuş review-lərdə negative Steam recommendation bütün dataset-lə müqayisədə xeyli daha çox cəmlənib.”

Bu fərq dizayn siqnalıdır, aspect sentiment-in özü deyil.

---

# 4. Full-corpus theme nəticələri

| Theme | Mention | Dataset payı | Negative review payı | Dataset baseline-a nisbət | Semantic audit nəticəsi |
|---|---:|---:|---:|---:|---|
| STORY_NARRATIVE | 2,422 | 20.57% | 3.92% | 0.67× | Əsasən müsbət, amma story təkbaşına zəif core loop-u xilas etmir |
| TERMINAL_UI | 2,269 | 19.27% | 7.05% | 1.20× | İkiüzlü siqnal: fantasy-ni gücləndirir, technical/usability friction da yaradır |
| DEPTH_CHALLENGE | 1,534 | 13.03% | 6.26% | 1.07× | Qarışıq; hazır theme çox genişdir və depth/difficulty/puzzle ayrılmalıdır |
| SOUND_AUDIO | 1,116 | 9.48% | 3.58% | 0.61× | Güclü müsbət dəstək, xüsusilə atmosphere və tension üçün |
| REALISM_ACCURACY | 932 | 7.92% | 4.08% | 0.69× | Qarışıq: “real deyil, amma yaxşı abstraction-dır” fikri çox yayılıb |
| IMMERSION | 910 | 7.73% | 2.42% | 0.41× | Güclü müsbət driver; repetition onu poza bilir |
| INVESTIGATION_DISCOVERY | 610 | 5.18% | 3.93% | 0.67× | Əsasən müsbət; files/clues/exploration gameplay-i dərinləşdirir |
| UI_USABILITY | 534 | 4.54% | 8.80% | 1.50× | Interface fantasy-si güclü olsa da real usability complaint-ləri var |
| REPETITION | 517 | 4.39% | 23.21% | **3.95×** | Güclü mənfi theme; positive review-lərdə belə tez-tez caveat kimi görünür |
| BUGS_COMPATIBILITY | 502 | 4.26% | 27.29% | **4.65×** | Ən güclü negative concentration; launch/compatibility/save problemləri |
| ONBOARDING_CLARITY | 462 | 3.92% | 12.55% | **2.14×** | Qarışıq; tutorial bəzilərinə yaxşı işləyir, digərləri kritik nöqtələrdə ilişir |
| MOD_REPLAYABILITY | 405 | 3.44% | 2.22% | 0.38× | Güclü müsbət long-tail; orta playtime da çox yüksəkdir |
| HACKER_FANTASY | 401 | 3.41% | 1.75% | **0.30×** | Ən təmiz müsbət theme-lərdən biri |
| PLAYER_AGENCY | 154 | 1.31% | 16.23% | **2.77×** | Linear/forced path complaint-ləri; hidden exploration bunun əks müsbət nümunəsidir |
| LENGTH_CONTENT | 143 | 1.21% | 3.50% | 0.60× | Aşağı coverage; “qısa amma yaxşı” və “daha çox content istəyirəm” qarışıqdır |
| EDUCATIONAL_IMPACT | 107 | 0.91% | 2.80% | 0.48× | Müsbət, amma real cybersecurity təlimindən çox maraq/intro/inspiration rolundadır |
| WORLD_REACTIVITY | 48 | 0.41% | 20.83% | **3.55×** | Aşağı say, amma aydın complaint: log/consequence/world response dayazdır |
| PACING_WAITING | 46 | 0.39% | 13.04% | **2.22×** | Aşağı say; waiting/progress-bar və temp complaint-ləri var |

**Baseline:** bütün dataset-də negative recommendation 5.87%-dir.

“Dataset baseline-a nisbət” yalnız negative-review concentration göstəricisidir. Məsələn 4× nəticə həmin theme-in səbəb olduğunu sübut etmir.

---

# 5. Ən vacib quantitative siqnallar

## 5.1. Repetition əsas design riskidir

REPETITION:

- 517 candidate review;
- dataset-in 4.39%-i;
- 120 negative review;
- 23.21% negative recommendation;
- dataset baseline-dan təxminən **3.95 dəfə** yüksək negative concentration.

Semantic audit-də ən vacib pattern:

Positive review-lər belə tez-tez bunu deyir:

> oyun ümumilikdə yaxşıdır, amma sistemləri hack etmək bir müddətdən sonra eyni sequence-ə çevrilir.

Negative review-lərdə isə bu daha sərtdir:

```text
probe
→ uyğun port tool-u
→ wait
→ porthack
→ files
→ repeat
```

Problemin özü terminal deyil.

Problem terminal interaction-ın bir müddətdən sonra **decision yox, muscle-memory sequence** olmasıdır.

### Co-occurrence

REPETITION candidate-lərinin:

- 244-ü TERMINAL_UI ilə birlikdədir — **47.2%**
- 230-u STORY_NARRATIVE ilə birlikdədir — **44.5%**
- 187-si DEPTH_CHALLENGE ilə birlikdədir — **36.2%**

Bu, repetition complaint-in core experience-dan kənar kiçik problem olmadığını göstərən əlavə siqnaldır. O, terminal loop, perceived depth və story experience ilə tez-tez eyni review daxilində müzakirə olunur.

**Confidence: High**

---

# 6. Bugs/compatibility ayrıca böyük failure driver-dir

BUGS_COMPATIBILITY:

- 502 candidate review;
- 4.26% dataset share;
- 137 negative review;
- 27.29% negative recommendation;
- baseline-dan **4.65 dəfə** yüksək negative concentration.

Audit nümunələrində:

- black screen / launch problemi;
- save corruption;
- softlock;
- crash;
- Mac compatibility;
- resolution;
- mission state problemləri

görünür.

Burada vacib distinction:

> Gameplay design complaint ilə technical reliability complaint eyni report-da qarışdırılmamalıdır.

Hacknet üçün bəzi negative recommendation-lər oyunun concept/gameplay-ni bəyənən, amma texniki problemlərə görə tövsiyə etməyən oyunçulardan gəlir.

Bu sonrakı cross-game comparison-larda ayrıca sütun olmalıdır.

**Confidence: High**

---

# 7. Hacker fantasy — məhsulun ən təmiz müsbət value proposition-larından biridir

HACKER_FANTASY:

- 401 explicit candidate mention;
- 98.25% overall positive review ratio;
- negative concentration yalnız 1.75%;
- baseline negative rate-in təxminən 0.30 misli.

Bu theme çox dar regex ilə tutulur, ona görə 3.41% share real prevalence kimi qəbul edilməməlidir. Əksinə, bu yalnız açıq şəkildə “feel like a hacker / become a hacker / hackerman” deyən review-lərdir.

Semantic audit çox ardıcıldır:

- “makes you feel like a hacker”;
- “Hollywood hacker fantasy”;
- terminal + ports + trace + commands;
- real hacking bilmədən fantasy-ni yaşamaq.

Maraqlı nüans:

Negative review belə bəzən Hacknet-in hacker fantasy-ni yaxşı yaratdığını etiraf edir, amma repetition və dayazlıq səbəbilə final recommendation mənfi olur.

Bu çox vacibdir:

> **Hook uğurludur; uzunmüddətli problem hook-un içindəki core loop-un kifayət qədər inkişaf etməməsidir.**

**Confidence: High**

---

# 8. Immersion güclü driver-dir, amma kövrəkdir

IMMERSION:

- 910 candidate review;
- 7.73% share;
- 97.58% overall positive ratio;
- negative concentration 2.42%.

Audit-də immersion aşağıdakılardan yaranır:

- terminal;
- fictional OS;
- real terminlər;
- story;
- trace pressure;
- sistemə “icazəsiz daxil olma” hissi;
- audio/visual feedback.

Negative audit nümunələri isə göstərir ki, immersion çox vaxt əvvəlcə işləyir, sonra:

- repetition;
- challenge çatışmazlığı;
- obvious scripted loop;
- shallow system logic

onu sındırır.

Deməli immersion statik art asset deyil.

> **Immersion sistemin inandırıcılığına bağlıdır; oyunçu sistemin pattern-ini çox tez görəndə fantasy zəifləyir.**

**Confidence: High**

---

# 9. Story çox görünür və əsasən müsbət kontekstdədir

STORY_NARRATIVE ən çox tutulan theme-dir:

- 2,422 review;
- 20.57% dataset share;
- 96.08% overall positive ratio.

STORY ilə TERMINAL_UI 833 review-da birlikdə görünür.

Bu iki sistemin bir-birindən ayrı olmadığını gücləndirir:

> Hacknet-in story-si terminal/fake OS içində yaşandığı üçün interface özü narrative delivery mexanizmidir.

Digər güclü co-occurrence:

- STORY + SOUND: 625
- STORY + IMMERSION: 394
- STORY + INVESTIGATION: 348

Investigation candidate-lərinin 57%-dən çoxu story ilə birlikdədir.

Bu pattern göstərir ki, Hacknet-də “story”, “files araşdırmaq” və “hacking interface” ayrıca feature-lər kimi yox, eyni experience stack-in hissələri kimi qəbul edilir.

Amma audit-də negative nümunələr də var:

- plot linear görünür;
- writing bəzən zəif sayılır;
- story core loop repetition-ını həmişə daşıya bilmir.

**Confidence: High**

---

# 10. Soundtrack support system deyil, experience multiplier-dir

SOUND_AUDIO:

- 1,116 candidate review;
- 9.48% share;
- 96.42% overall positive ratio.

Sound mention-larının 56%-i STORY ilə birlikdədir.

Audit-də soundtrack:

- atmosphere;
- urgency;
- typing rhythm;
- trace tension;
- “cool hacker” hissi

ilə əlaqələndirilir.

Bu, interface-heavy oyunlar üçün vacib design nəticəsidir:

> 3D action və character animation az olduqda audio feedback və music daha çox emosional yük daşıyır.

**Confidence: High**

---

# 11. Terminal həm əsas üstünlük, həm də riskdir

TERMINAL_UI:

- 2,269 review;
- 19.27% share;
- 92.95% overall positive ratio;
- negative concentration baseline-dan yalnız bir qədər yüksəkdir: 1.20×.

Bu theme-in semantic audit-i iki fərqli audience göstərir.

## Müsbət tərəf

- typing özü satisfying-dir;
- terminal “hacker” fantasy-si yaradır;
- real Unix flavor-u authenticity verir;
- GUI-dən fərqli experience yaradır.

## Mənfi tərəf

Technical istifadəçilər real shell mental model-i ilə gəlir və bunları gözləyir:

- normal wildcard;
- normal autocomplete;
- copy/paste;
- file management;
- consistent paths;
- expected command behavior.

Bunlar işləməyəndə sadələşdirmə “accessible abstraction” kimi yox, “broken terminal” kimi qəbul edilə bilər.

Nəticə:

> **Real sistemə nə qədər çox oxşayırsansa, həmin sistemin real davranışına olan expectation da artır.**

**Confidence: High**

---

# 12. Realism nəticəsini sadə positive/negative kimi oxumaq olmaz

REALISM_ACCURACY:

- 932 candidate review;
- 7.92% share;
- 95.92% overall positive ratio.

Bu ilk baxışda “realism çox bəyənilir” kimi görünə bilər.

Semantic audit bunu təsdiqləmir.

Əslində çox positive review belə deyir:

- real hacking deyil;
- hacking həddindən artıq abstract-dır;
- amma real hacking oyun üçün çox tedious olardı;
- seçilmiş Unix/port/terminal vocabulary kifayət qədər authenticity yaradır.

Digər tərəfdə technical negative review-lər:

- inaccurate Unix behavior;
- fake tools;
- yanlış proxy/log/file-system logic

şikayət edir.

Deməli əsas prinsip:

> **Hacknet-in uğurlu balansı realism deyil, selective authenticity + accessibility-dir.**

Marketing bu distinction-u düzgün qurmalıdır.

**Confidence: High**

---

# 13. Investigation/discovery core loop-u dərinləşdirən hissədir

INVESTIGATION_DISCOVERY:

- 610 candidate review;
- 5.18% share;
- 96.07% overall positive ratio;
- orta playtime 15.63 saat.

Candidate-lərin 57%-i STORY ilə birlikdədir.

Semantic audit-də ən yaxşı nümunələr:

- files içində clue tapmaq;
- mission üçün lazım olmayan məlumatı araşdırmaq;
- IP/header kimi əlavə detail-dən yeni node tapmaq;
- insanların private data-sına baxmaq;
- mystery-ni özün birləşdirmək.

Bu hissələr basic cracking sequence-dən fərqli olaraq real curiosity və decision yaradır.

> **Hacknet-in daha çox dərinləşdirilə biləcək istiqaməti “daha real exploit” yox, information discovery və inference layer-dir.**

**Confidence: Medium-High**

---

# 14. Onboarding həm uğurlu, həm də risklidir

ONBOARDING_CLARITY:

- 462 candidate review;
- 12.55% negative;
- baseline-dan **2.14×** yüksək negative concentration.

Positive review-lərdə:

- tutorial kifayət qədər rahatdır;
- `help` command işləyir;
- non-technical player terminala daxil ola bilir.

Negative review-lərdə:

- konkret critical event-də nə etməli olduğu aydın deyil;
- tutorial normal state-i öyrədir, exceptional state-i yox;
- help list kontekstsizdir;
- uzun fasilədən sonra command-ları xatırlamaq çətindir.

Bu iki nəticə zidd deyil.

Hacknet initial onboarding-i yaxşı edə bilər, amma:

> **situational onboarding və returning-player recovery zəif qala bilər.**

Bizim oyun üçün tutorial yalnız başlanğıc sequence olmamalıdır.

**Confidence: Medium-High**

---

# 15. Player agency və world reactivity — aşağı volume, yüksək risk siqnalı

PLAYER_AGENCY:

- 154 mentions;
- 16.23% negative;
- baseline-dan **2.77×** yüksək.

WORLD_REACTIVITY:

- cəmi 48 mentions;
- 20.83% negative;
- baseline-dan **3.55×** yüksək.

Bu theme-lərin retrieval coverage-i dar olduğu üçün prevalence haqqında güclü nəticə çıxarmaq olmaz.

Amma semantic audit consistent complaint göstərir:

- linear path;
- no meaningful consequence;
- logs bəzən əhəmiyyətsizdir;
- hacked world kifayət qədər cavab vermir;
- bəzi “choice” hissləri real sistemik nəticə yaratmır.

Eyni zamanda positive review-lərdə hidden server, optional clue və gözlənilməz “sən hack olunursan” sequence-i yüksək dəyər yaradır.

Bu contrast vacibdir:

> Oyunçular scripted surprise-i sevir, amma sistemik reactivity daha zəifdir.

Bu bizim gələcək concept üçün böyük opportunity ola bilər.

**Confidence: Medium**

---

# 16. Mod support uzunmüddətli dəyəri ciddi artırır

MOD_REPLAYABILITY:

- 405 candidate review;
- 97.78% overall positive ratio;
- average playtime: **25.19 saat** — theme-lər arasında ən yüksək göstəricilərdən biri;
- 257 mention 10h+ cohort-dadır.

Bu causation deyil: uzun oynayan oyunçu mod haqqında daha çox yaza bilər.

Amma evidence istiqaməti güclüdür:

- Workshop/custom extensions əlavə content verir;
- base-game loop finite olsa da community content ömrü uzadır;
- story/interface engine başqa hekayələri daşıya bilir.

Bizim oyun üçün launch feature kimi şərt deyil, amma content-heavy UI oyunlarında creator tools yüksək leverage yarada bilər.

**Confidence: Medium-High**

---

# 17. Educational impact — “təlim” yox, gateway effekti

EDUCATIONAL_IMPACT:

- 107 explicit candidate review;
- 97.20% overall positive ratio;
- orta playtime 15.94 saat.

Audit göstərir ki, iki fikir paralel yaşayır:

1. oyun real hacking öyrətmir;
2. basic terminal vocabulary və computer/security marağı yarada bilir.

Ona görə:

> Hacknet-i educational simulator kimi yox, technology-interest gateway kimi düşünmək daha düzgündür.

Bu positioning həm expectation mismatch-i azaldır, həm də positive secondary value-ni qoruyur.

**Confidence: Medium**

---

# 18. Taxonomy audit nəticəsi

Current retrieval taxonomy faydalıdır, amma final semantic taxonomy üçün bəzi theme-lər bölünməlidir.

## Bölünməli theme-lər

### DEPTH_CHALLENGE

Hazırda bir yerdə üç fərqli sual var:

- SYSTEM_DEPTH
- PUZZLE_PROBLEM_SOLVING
- DIFFICULTY

Final aspect taxonomy-də ayrılmalıdır.

### TERMINAL_UI

Ən azı iki ayrı aspect lazımdır:

- TERMINAL_FANTASY / TERMINAL_INTERACTION
- UI_USABILITY / SHELL_LIMITATIONS

### REALISM_ACCURACY

İki fərqli şeyi ayırmaq lazımdır:

- AUTHENTICITY — “kifayət qədər real hiss”
- TECHNICAL_ACCURACY — real Unix/security davranışının düzgünlüyü

### WORLD_REACTIVITY

Final taxonomy-də belə ayrılma faydalıdır:

- CONSEQUENCES
- WORLD_REACTIVITY / PERSISTENCE
- TRACE / URGENCY

---

# 19. Final aspect taxonomy üçün tövsiyə

Növbəti mərhələdə semantic coding üçün aşağıdakı aspect-lər daha düzgündür:

```text
HACKER_FANTASY
IMMERSION
TERMINAL_INTERACTION
UI_USABILITY
TECHNICAL_ACCURACY
AUTHENTICITY

STORY
WRITING
INVESTIGATION
DISCOVERY_EXPLORATION
MEMORABLE_MOMENTS

SYSTEM_DEPTH
PUZZLE_PROBLEM_SOLVING
DIFFICULTY
REPETITION
PACING_WAITING

ONBOARDING
RETURNING_PLAYER_SUPPORT

PLAYER_AGENCY
CONSEQUENCES
WORLD_REACTIVITY
URGENCY_TRACE

SOUNDTRACK_AUDIO

LENGTH_CONTENT
REPLAYABILITY
MOD_SUPPORT

BUGS
COMPATIBILITY
SAVE_SOFTLOCK

EDUCATIONAL_GATEWAY
```

Bu taxonomy digər oyunlarla müqayisədə də mümkün qədər reusable saxlanmalıdır.

---

# 20. Hacknet üçün evidence-backed design nəticələri

## 20.1. Hook düzgündür

Hacker fantasy explicit mention-larda çox güclü müsbət siqnaldır.

**Dərs:** fantasy-ni azaltmaq yox, onu daha uzun müddət daşıya biləcək sistem qurmaq lazımdır.

## 20.2. Core loop-un novelty-si tez görünə bilər

Repetition negative concentration-u çox yüksəkdir və terminal/depth ilə güclü co-occurrence edir.

**Dərs:** yeni target sadəcə yeni port və daha uzun wait olmamalıdır.

## 20.3. Information gameplay hacking gameplay-dən daha çox expansion potential göstərir

Investigation/discovery pattern-i story ilə güclü bağlıdır və audit-də curiosity yaradır.

**Dərs:** access əldə etmək məqsəd yox, daha maraqlı information problem-in giriş qapısı ola bilər.

## 20.4. Selective authenticity real simulation-dan daha sağlamdır

Realism audit-i göstərir ki, oyunçular tam realism tələb etmir.

**Dərs:** real terminologiya və məntiq götür, amma oyun üçün lazım olmayan complexity-ni simulyasiya etmə.

## 20.5. Real görünən interface contract yaradır

Terminal real görünürsə, technical user onun real davranışını gözləyir.

**Dərs:** ya standard behavior-a yaxın ol, ya da fictional abstraction olduğunu aydın göstər.

## 20.6. Consequence promise varsa, sistem onu yerinə yetirməlidir

Log, trace və hacking risk kimi təqdim edilirsə, oyunçu onların real consequence yaratmasını gözləyir.

**Dərs:** decorative systems immersion-ı uzun müddətdə zəiflədə bilər.

## 20.7. Audio design core sistemdir

Sound/story/immersion birlikdə güclü görünür.

**Dərs:** computer-interface oyunda audio production başlanğıcdan gameplay design-a daxil edilməlidir.

## 20.8. Returning player ayrıca use-case-dir

Command vocabulary normal control scheme deyil.

**Dərs:** recap, contextual help, recent commands, notes/evidence sistemi lazımdır.

## 20.9. Technical stability research nəticələrində ayrıca saxlanmalıdır

Bugs ən yüksək negative concentration verir.

**Dərs:** bir oyunun “niyə negative review alması” ilə “design niyə işləmir” eyni sual deyil.

---

# 21. Cari confidence matrix

| Nəticə | Confidence |
|---|---|
| Repetition əsas design failure pattern-dir | High |
| Hacker fantasy əsas value proposition-dır | High |
| Immersion əsas satisfaction driver-dir | High |
| Story experience-in əsas hissəsidir | High |
| Soundtrack experience-i gücləndirir | High |
| Technical bugs negative reviews-a ciddi təsir edir | High |
| Full realism tələb olunmur; selective authenticity işləyir | High |
| Terminal technical audience üçün expectation riski yaradır | High |
| Investigation/discovery daha dərin gameplay üçün opportunity-dir | Medium-High |
| Mod support uzunömürlülüyü artırır | Medium-High |
| Onboarding-in problem nöqtələri situational/returning-player xarakterlidir | Medium-High |
| Agency/consequence/world reactivity böyük opportunity-dir | Medium |
| Educational value daha çox gateway/inspiration-dır | Medium |
| Pacing/waiting ayrıca böyük problem-dir | Low-Medium — retrieval sayı azdır |

---

# 22. Məhdudiyyətlər

1. Candidate retrieval semantic model deyil.
2. Theme frequency lexical coverage-dən asılıdır.
3. Overall Steam recommendation aspect sentiment deyil.
4. Audit sample-lar helpful və cohort-balanced seçimlərdən ibarətdir; population-random survey deyil.
5. Review yazanlar bütün player population-u təmsil etmir.
6. Playtime ilə sentiment əlaqəsi self-selection daşıyır.
7. Co-occurrence causation deyil.
8. Bəzi uzun review-lər birdən çox theme-i eyni anda daşıyır.

Buna görə bu sənədin rəqəmləri **design evidence** kimi istifadə olunur, exact population psychology kimi yox.

---

# 23. Növbəti addım

Hacknet üçün full-corpus retrieval + semantic audit artıq kifayət qədər güclü bazadır.

Növbəti addımlar:

1. final semantic aspect taxonomy-ni ayrıca config kimi sabitləşdirmək;
2. Hacknet `deep-research.md` sənədinə bu quantitative nəticələrin executive versiyasını əlavə etmək;
3. Hacknet report-u master brief-dəki per-game professional struktura yaxınlaşdırmaq;
4. bundan sonra **Midnight Protocol** üçün eyni data/research metoduna keçmək;
5. sonra Hacknet vs Midnight Protocol müqayisəsi aparmaq.

