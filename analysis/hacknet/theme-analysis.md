# Hacknet — rəy mövzu Analizi

## 1. Məqsəd

Bu sənəd Hacknet üçün 11,773 verified Steam rəy üzərində aparılan bütün rəy toplusu üzrə mövzu namizədi scan və onun məna yönümlü yoxlama nəticələrini saxlayır.

Bu sənədin rolu:

- rəy-lərdə hansı mövzuların geniş yayıldığını ölçmək;
- hansı mövzuların mənfi rəy-lərdə normadan daha çox toplandığını görmək;
- keyword nəticələrini məna yönümlü yoxlama ilə yoxlamaq;
- Hacknet üzrə dizayn/məhsul nəticələrini daha ölçülə bilən dəlil ilə gücləndirmək.

Bu sənəd **final full-məlumat toplusu aspekt üzrə münasibət classification deyil**.

Hazır metod iki mərhələdən ibarətdir:

1. bütün 11,773 rəy üzərində deterministik regex/keyword namizəd retrieval;
2. hər mövzu üçün recommendation və oyun müddəti qrupu-ları üzrə audit sample-larının məna yönümlü yoxlanması.

Full LLM classification infrastructure hazırda yoxdur. Buna görə aşağıdakı rəqəmlər “mövzu-i müsbət qiymətləndirən rəy faizi” kimi şərh edilməməlidir.

---

# 2. məlumat toplusu bazası

- Total verified rəylər: **11,773**
- müsbət rəys: **11,082**
- mənfi rəys: **691**
- məlumat toplusu overall müsbət rəy nisbəti: **94.13%**
- məlumat toplusu overall mənfi rəy nisbəti: **5.87%**
- Ən azı bir mövzu namizədi-i tutulan rəy: **6,009**
- namizəd coverage: **51.04%**

namizəd coverage-in 51% olması o demək deyil ki, qalan rəy-lər bu mövzular haqqında heç nə demir. Regex retrieval yalnız açıq lexical siqnalları tutur. Qısa, zarafat tipli və ya başqa sözlərlə eyni fikri bildirən rəy-lər qaça bilər.

---

# 3. Rəqəmləri necə oxumaq lazımdır?

Məsələn:

- REPETITION namizəd-i 517 rəy-da tapılıb;
- onların 120-si negative Steam rəy-dur;
- həmin qrupun mənfi rəy nisbəti 23.21%-dir.

Amma bu:

> “Repetition haqqında danışanların 23.21%-i repetition-dan narazıdır”

demək deyil.

Düzgün şərh:

> “Repetition söz və nümunə-ləri ilə tutulmuş rəy-lərdə negative Steam tövsiyəsi bütün məlumat toplusu-lə müqayisədə xeyli daha çox cəmlənib.”

Bu fərq dizayn siqnalıdır, aspekt üzrə münasibət-in özü deyil.

---

# 4. bütün rəy toplusu üzrə mövzu nəticələri

| mövzu | Mention | məlumat toplusu payı | mənfi rəy payı | məlumat toplusu baseline-a nisbət | məna yönümlü yoxlama nəticəsi |
|---|---:|---:|---:|---:|---|
| STORY_NARRATIVE | 2,422 | 20.57% | 3.92% | 0.67× | Əsasən müsbət, amma hekayə təkbaşına zəif əsas oyun dövrü-u xilas etmir |
| TERMINAL_UI | 2,269 | 19.27% | 7.05% | 1.20× | İkiüzlü siqnal: rol hissi-ni gücləndirir, technical/usability çətinlik da yaradır |
| DEPTH_CHALLENGE | 1,534 | 13.03% | 6.26% | 1.07× | Qarışıq; hazır mövzu çox genişdir və dərinlik/difficulty/puzzle ayrılmalıdır |
| SOUND_AUDIO | 1,116 | 9.48% | 3.58% | 0.61× | Güclü müsbət dəstək, xüsusilə atmosphere və tension üçün |
| REALISM_ACCURACY | 932 | 7.92% | 4.08% | 0.69× | Qarışıq: “real deyil, amma yaxşı abstraction-dır” fikri çox yayılıb |
| IMMERSION | 910 | 7.73% | 2.42% | 0.41× | Güclü müsbət amil; repetition onu poza bilir |
| INVESTIGATION_DISCOVERY | 610 | 5.18% | 3.93% | 0.67× | Əsasən müsbət; files/ipucus/exploration oyun gedişi-i dərinləşdirir |
| UI_USABILITY | 534 | 4.54% | 8.80% | 1.50× | Interface rol hissi-si güclü olsa da real usability complaint-ləri var |
| REPETITION | 517 | 4.39% | 23.21% | **3.95×** | Güclü mənfi mövzu; müsbət rəy-lərdə belə tez-tez caveat kimi görünür |
| BUGS_COMPATIBILITY | 502 | 4.26% | 27.29% | **4.65×** | Ən güclü negative concentration; launch/compatibility/save problemləri |
| ONBOARDING_CLARITY | 462 | 3.92% | 12.55% | **2.14×** | Qarışıq; tutorial bəzilərinə yaxşı işləyir, digərləri kritik nöqtələrdə ilişir |
| MOD_təkrar oynama dəyəri | 405 | 3.44% | 2.22% | 0.38× | Güclü müsbət long-tail; orta oyun müddəti da çox yüksəkdir |
| HACKER_FANTASY | 401 | 3.41% | 1.75% | **0.30×** | Ən təmiz müsbət mövzu-lərdən biri |
| PLAYER_AGENCY | 154 | 1.31% | 16.23% | **2.77×** | Linear/forced path complaint-ləri; hidden exploration bunun əks müsbət nümunəsidir |
| LENGTH_məzmun | 143 | 1.21% | 3.50% | 0.60× | Aşağı coverage; “qısa amma yaxşı” və “daha çox məzmun istəyirəm” qarışıqdır |
| EDUCATIONAL_IMPACT | 107 | 0.91% | 2.80% | 0.48× | Müsbət, amma real cybersecurity təlimindən çox maraq/intro/inspiration rolundadır |
| WORLD_REACTIVITY | 48 | 0.41% | 20.83% | **3.55×** | Aşağı say, amma aydın complaint: log/nəticə/world response dayazdır |
| PACING_WAITING | 46 | 0.39% | 13.04% | **2.22×** | Aşağı say; waiting/progress-bar və temp complaint-ləri var |

**Baseline:** bütün məlumat toplusu-də negative recommendation 5.87%-dir.

“məlumat toplusu baseline-a nisbət” yalnız negative-rəy concentration göstəricisidir. Məsələn 4× nəticə həmin mövzu-in səbəb olduğunu sübut etmir.

---

# 5. Ən vacib quantitative siqnallar

## 5.1. Repetition əsas dizayn riskidir

REPETITION:

- 517 namizəd rəy;
- məlumat toplusu-in 4.39%-i;
- 120 mənfi rəy;
- 23.21% negative recommendation;
- məlumat toplusu baseline-dan təxminən **3.95 dəfə** yüksək negative concentration.

məna yönümlü yoxlama-də ən vacib nümunə:

müsbət rəy-lər belə tez-tez bunu deyir:

> oyun ümumilikdə yaxşıdır, amma sistemləri hack etmək bir müddətdən sonra eyni sequence-ə çevrilir.

mənfi rəy-lərdə isə bu daha sərtdir:

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

REPETITION namizəd-lərinin:

- 244-ü TERMINAL_UI ilə birlikdədir — **47.2%**
- 230-u STORY_NARRATIVE ilə birlikdədir — **44.5%**
- 187-si DEPTH_CHALLENGE ilə birlikdədir — **36.2%**

Bu, repetition complaint-in core experience-dan kənar kiçik problem olmadığını göstərən əlavə siqnaldır. O, terminal loop, perceived dərinlik və hekayə experience ilə tez-tez eyni rəy daxilində müzakirə olunur.

**etibarlılıq: High**

---

# 6. Bugs/compatibility ayrıca böyük uğursuzluq amil-dir

BUGS_COMPATIBILITY:

- 502 namizəd rəy;
- 4.26% məlumat toplusu share;
- 137 mənfi rəy;
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

> oyun gedişi dizayn complaint ilə technical reliability complaint eyni report-da qarışdırılmamalıdır.

Hacknet üçün bəzi negative recommendation-lər oyunun concept/oyun gedişi-ni bəyənən, amma texniki problemlərə görə tövsiyə etməyən oyunçulardan gəlir.

Bu sonrakı cross-game müqayisə-larda ayrıca sütun olmalıdır.

**etibarlılıq: High**

---

# 7. özünü haker kimi hiss etmə — məhsulun ən təmiz müsbət value proposition-larından biridir

HACKER_FANTASY:

- 401 explicit namizəd mention;
- 98.25% overall müsbət rəy nisbəti;
- negative concentration yalnız 1.75%;
- baseline negative rate-in təxminən 0.30 misli.

Bu mövzu çox dar regex ilə tutulur, ona görə 3.41% share real prevalence kimi qəbul edilməməlidir. Əksinə, bu yalnız açıq şəkildə “feel like a hacker / become a hacker / hackerman” deyən rəy-lərdir.

məna yönümlü yoxlama çox ardıcıldır:

- “makes you feel like a hacker”;
- “Hollywood özünü haker kimi hiss etmə”;
- terminal + ports + trace + commands;
- real hacking bilmədən rol hissi-ni yaşamaq.

Maraqlı nüans:

mənfi rəy belə bəzən Hacknet-in özünü haker kimi hiss etmə-ni yaxşı yaratdığını etiraf edir, amma repetition və dayazlıq səbəbilə final recommendation mənfi olur.

Bu çox vacibdir:

> **ilkin cəlbedicilik uğurludur; uzunmüddətli problem ilkin cəlbedicilik-un içindəki əsas oyun dövrü-un kifayət qədər inkişaf etməməsidir.**

**etibarlılıq: High**

---

# 8. Immersion güclü amil-dir, amma kövrəkdir

IMMERSION:

- 910 namizəd rəy;
- 7.73% share;
- 97.58% overall müsbət rəy nisbəti;
- negative concentration 2.42%.

Audit-də immersion aşağıdakılardan yaranır:

- terminal;
- fictional OS;
- real terminlər;
- hekayə;
- trace pressure;
- sistemə “icazəsiz daxil olma” hissi;
- audio/visual geribildirim.

Negative audit nümunələri isə göstərir ki, immersion çox vaxt əvvəlcə işləyir, sonra:

- repetition;
- çətinlik çatışmazlığı;
- obvious scripted loop;
- shallow system logic

onu sındırır.

Deməli immersion statik art asset deyil.

> **Immersion sistemin inandırıcılığına bağlıdır; oyunçu sistemin nümunə-ini çox tez görəndə rol hissi zəifləyir.**

**etibarlılıq: High**

---

# 9. hekayə çox görünür və əsasən müsbət kontekstdədir

STORY_NARRATIVE ən çox tutulan mövzu-dir:

- 2,422 rəy;
- 20.57% məlumat toplusu share;
- 96.08% overall müsbət rəy nisbəti.

hekayə ilə TERMINAL_UI 833 rəy-da birlikdə görünür.

Bu iki sistemin bir-birindən ayrı olmadığını gücləndirir:

> Hacknet-in hekayə-si terminal/fake OS içində yaşandığı üçün interface özü narrative delivery mexanizmidir.

Digər güclü co-occurrence:

- hekayə + SOUND: 625
- hekayə + IMMERSION: 394
- hekayə + araşdırma: 348

araşdırma namizəd-lərinin 57%-dən çoxu hekayə ilə birlikdədir.

Bu nümunə göstərir ki, Hacknet-də “hekayə”, “files araşdırmaq” və “hacking interface” ayrıca feature-lər kimi yox, eyni experience stack-in hissələri kimi qəbul edilir.

Amma audit-də negative nümunələr də var:

- plot linear görünür;
- yazı keyfiyyəti bəzən zəif sayılır;
- hekayə əsas oyun dövrü repetition-ını həmişə daşıya bilmir.

**etibarlılıq: High**

---

# 10. Soundtrack support system deyil, experience multiplier-dir

SOUND_AUDIO:

- 1,116 namizəd rəy;
- 9.48% share;
- 96.42% overall müsbət rəy nisbəti.

Sound mention-larının 56%-i hekayə ilə birlikdədir.

Audit-də soundtrack:

- atmosphere;
- urgency;
- typing rhythm;
- trace tension;
- “cool hacker” hissi

ilə əlaqələndirilir.

Bu, interface-heavy oyunlar üçün vacib dizayn nəticəsidir:

> 3D action və character animation az olduqda audio geribildirim və music daha çox emosional yük daşıyır.

**etibarlılıq: High**

---

# 11. Terminal həm əsas üstünlük, həm də riskdir

TERMINAL_UI:

- 2,269 rəy;
- 19.27% share;
- 92.95% overall müsbət rəy nisbəti;
- negative concentration baseline-dan yalnız bir qədər yüksəkdir: 1.20×.

Bu mövzu-in məna yönümlü yoxlama-i iki fərqli audience göstərir.

## Müsbət tərəf

- typing özü satisfying-dir;
- terminal “hacker” rol hissi-si yaradır;
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

**etibarlılıq: High**

---

# 12. Realism nəticəsini sadə positive/negative kimi oxumaq olmaz

REALISM_ACCURACY:

- 932 namizəd rəy;
- 7.92% share;
- 95.92% overall müsbət rəy nisbəti.

Bu ilk baxışda “realism çox bəyənilir” kimi görünə bilər.

məna yönümlü yoxlama bunu təsdiqləmir.

Əslində çox müsbət rəy belə deyir:

- real hacking deyil;
- hacking həddindən artıq abstract-dır;
- amma real hacking oyun üçün çox tedious olardı;
- seçilmiş Unix/port/terminal vocabulary kifayət qədər authenticity yaradır.

Digər tərəfdə technical mənfi rəy-lər:

- inaccurate Unix behavior;
- fake alətlər;
- yanlış proxy/log/file-system logic

şikayət edir.

Deməli əsas prinsip:

> **Hacknet-in uğurlu balansı realism deyil, selective authenticity + accessibility-dir.**

Marketing bu distinction-u düzgün qurmalıdır.

**etibarlılıq: High**

---

# 13. araşdırma/kəşf əsas oyun dövrü-u dərinləşdirən hissədir

INVESTIGATION_DISCOVERY:

- 610 namizəd rəy;
- 5.18% share;
- 96.07% overall müsbət rəy nisbəti;
- orta oyun müddəti 15.63 saat.

namizəd-lərin 57%-i hekayə ilə birlikdədir.

məna yönümlü yoxlama-də ən yaxşı nümunələr:

- files içində ipucu tapmaq;
- mission üçün lazım olmayan məlumatı araşdırmaq;
- IP/header kimi əlavə detail-dən yeni node tapmaq;
- insanların private data-sına baxmaq;
- mystery-ni özün birləşdirmək.

Bu hissələr basic cracking sequence-dən fərqli olaraq real curiosity və decision yaradır.

> **Hacknet-in daha çox dərinləşdirilə biləcək istiqaməti “daha real exploit” yox, məlumat kəşfi və inference layer-dir.**

**etibarlılıq: Medium-High**

---

# 14. ilkin öyrətmə həm uğurlu, həm də risklidir

ONBOARDING_CLARITY:

- 462 namizəd rəy;
- 12.55% negative;
- baseline-dan **2.14×** yüksək negative concentration.

müsbət rəy-lərdə:

- tutorial kifayət qədər rahatdır;
- `help` command işləyir;
- non-technical oyunçu terminala daxil ola bilir.

mənfi rəy-lərdə:

- konkret critical event-də nə etməli olduğu aydın deyil;
- tutorial normal state-i öyrədir, exceptional state-i yox;
- help list kontekstsizdir;
- uzun fasilədən sonra command-ları xatırlamaq çətindir.

Bu iki nəticə zidd deyil.

Hacknet initial ilkin öyrətmə-i yaxşı edə bilər, amma:

> **situational ilkin öyrətmə və returning-oyunçu bərpa zəif qala bilər.**

Bizim oyun üçün tutorial yalnız başlanğıc sequence olmamalıdır.

**etibarlılıq: Medium-High**

---

# 15. oyunçunun qərar sərbəstliyi və təsiri və dünyanın reaksiyası — aşağı volume, yüksək risk siqnalı

PLAYER_AGENCY:

- 154 mentions;
- 16.23% negative;
- baseline-dan **2.77×** yüksək.

WORLD_REACTIVITY:

- cəmi 48 mentions;
- 20.83% negative;
- baseline-dan **3.55×** yüksək.

Bu mövzu-lərin retrieval coverage-i dar olduğu üçün prevalence haqqında güclü nəticə çıxarmaq olmaz.

Amma məna yönümlü yoxlama consistent complaint göstərir:

- linear path;
- no mənalı nəticə;
- logs bəzən əhəmiyyətsizdir;
- hacked world kifayət qədər cavab vermir;
- bəzi “seçim” hissləri real sistemik nəticə yaratmır.

Eyni zamanda müsbət rəy-lərdə hidden server, optional ipucu və gözlənilməz “sən hack olunursan” sequence-i yüksək dəyər yaradır.

Bu contrast vacibdir:

> Oyunçular scripted surprise-i sevir, amma sistemik reactivity daha zəifdir.

Bu bizim gələcək concept üçün böyük imkan ola bilər.

**etibarlılıq: Medium**

---

# 16. mod dəstəyi uzunmüddətli dəyəri ciddi artırır

MOD_təkrar oynama dəyəri:

- 405 namizəd rəy;
- 97.78% overall müsbət rəy nisbəti;
- average oyun müddəti: **25.19 saat** — mövzu-lər arasında ən yüksək göstəricilərdən biri;
- 257 mention 10h+ cohort-dadır.

Bu causation deyil: uzun oynayan oyunçu mod haqqında daha çox yaza bilər.

Amma dəlil istiqaməti güclüdür:

- Workshop/custom extensions əlavə məzmun verir;
- base-game loop finite olsa da community məzmun ömrü uzadır;
- hekayə/interface engine başqa hekayələri daşıya bilir.

Bizim oyun üçün launch feature kimi şərt deyil, amma məzmun-heavy UI oyunlarında creator alətlər yüksək leverage yarada bilər.

**etibarlılıq: Medium-High**

---

# 17. Educational impact — “təlim” yox, gateway effekti

EDUCATIONAL_IMPACT:

- 107 explicit namizəd rəy;
- 97.20% overall müsbət rəy nisbəti;
- orta oyun müddəti 15.94 saat.

Audit göstərir ki, iki fikir paralel yaşayır:

1. oyun real hacking öyrətmir;
2. basic terminal vocabulary və computer/security marağı yarada bilir.

Ona görə:

> Hacknet-i educational simulator kimi yox, technology-interest gateway kimi düşünmək daha düzgündür.

Bu təqdimat həm expectation mismatch-i azaldır, həm də positive secondary value-ni qoruyur.

**etibarlılıq: Medium**

---

# 18. Taxonomy audit nəticəsi

Current retrieval taxonomy faydalıdır, amma final məna yönümlü taxonomy üçün bəzi mövzu-lər bölünməlidir.

## Bölünməli mövzu-lər

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

- nəticələr
- WORLD_REACTIVITY / PERSISTENCE
- TRACE / URGENCY

---

# 19. Final aspect taxonomy üçün tövsiyə

Növbəti mərhələdə məna yönümlü coding üçün aşağıdakı aspect-lər daha düzgündür:

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

# 20. Hacknet üçün dəlil-backed dizayn nəticələri

## 20.1. ilkin cəlbedicilik düzgündür

özünü haker kimi hiss etmə explicit mention-larda çox güclü müsbət siqnaldır.

**Dərs:** rol hissi-ni azaltmaq yox, onu daha uzun müddət daşıya biləcək sistem qurmaq lazımdır.

## 20.2. əsas oyun dövrü-un novelty-si tez görünə bilər

Repetition negative concentration-u çox yüksəkdir və terminal/dərinlik ilə güclü co-occurrence edir.

**Dərs:** yeni target sadəcə yeni port və daha uzun wait olmamalıdır.

## 20.3. Information oyun gedişi hacking oyun gedişi-dən daha çox expansion potential göstərir

araşdırma/kəşf nümunə-i hekayə ilə güclü bağlıdır və audit-də curiosity yaradır.

**Dərs:** access əldə etmək məqsəd yox, daha maraqlı information problem-in giriş qapısı ola bilər.

## 20.4. Selective authenticity real simulation-dan daha sağlamdır

Realism audit-i göstərir ki, oyunçular tam realism tələb etmir.

**Dərs:** real terminologiya və məntiq götür, amma oyun üçün lazım olmayan complexity-ni simulyasiya etmə.

## 20.5. Real görünən interface contract yaradır

Terminal real görünürsə, technical user onun real davranışını gözləyir.

**Dərs:** ya standard behavior-a yaxın ol, ya da fictional abstraction olduğunu aydın göstər.

## 20.6. nəticə promise varsa, sistem onu yerinə yetirməlidir

Log, trace və hacking risk kimi təqdim edilirsə, oyunçu onların real nəticə yaratmasını gözləyir.

**Dərs:** decorative systems immersion-ı uzun müddətdə zəiflədə bilər.

## 20.7. Audio dizayn core sistemdir

Sound/hekayə/immersion birlikdə güclü görünür.

**Dərs:** computer-interface oyunda audio production başlanğıcdan oyun gedişi dizayn-a daxil edilməlidir.

## 20.8. fasilədən sonra qayıdan oyunçu ayrıca use-case-dir

Command vocabulary normal control scheme deyil.

**Dərs:** recap, contextual help, recent commands, notes/dəlil sistemi lazımdır.

## 20.9. Technical stability araşdırma nəticələrində ayrıca saxlanmalıdır

Bugs ən yüksək negative concentration verir.

**Dərs:** bir oyunun “niyə mənfi rəy alması” ilə “dizayn niyə işləmir” eyni sual deyil.

---

# 21. Cari Etibarlılıq cədvəli

| Nəticə | etibarlılıq |
|---|---|
| Repetition əsas dizayn uğursuzluq nümunəsi-dir | High |
| özünü haker kimi hiss etmə əsas value proposition-dır | High |
| Immersion əsas satisfaction amil-dir | High |
| hekayə experience-in əsas hissəsidir | High |
| Soundtrack experience-i gücləndirir | High |
| Technical bugs mənfi rəys-a ciddi təsir edir | High |
| Full realism tələb olunmur; selective authenticity işləyir | High |
| Terminal technical audience üçün expectation riski yaradır | High |
| araşdırma/kəşf daha dərin oyun gedişi üçün imkan-dir | Medium-High |
| mod dəstəyi uzunömürlülüyü artırır | Medium-High |
| ilkin öyrətmə-in problem nöqtələri situational/returning-oyunçu xarakterlidir | Medium-High |
| qərar sərbəstliyi/nəticə/dünyanın reaksiyası böyük imkan-dir | Medium |
| Educational value daha çox gateway/inspiration-dır | Medium |
| Pacing/waiting ayrıca böyük problem-dir | Low-Medium — retrieval sayı azdır |

---

# 22. Məhdudiyyətlər

1. namizəd retrieval məna yönümlü model deyil.
2. mövzu frequency lexical coverage-dən asılıdır.
3. Overall Steam tövsiyəsi aspekt üzrə münasibət deyil.
4. Audit sample-lar helpful və cohort-balanced seçimlərdən ibarətdir; population-random survey deyil.
5. rəy yazanlar bütün oyunçu population-u təmsil etmir.
6. oyun müddəti ilə sentiment əlaqəsi self-selection daşıyır.
7. Co-occurrence causation deyil.
8. Bəzi uzun rəy-lər birdən çox mövzu-i eyni anda daşıyır.

Buna görə bu sənədin rəqəmləri **dizayn dəlil** kimi istifadə olunur, exact population psychology kimi yox.

---

# 23. Növbəti addım

Hacknet üçün bütün rəy toplusu üzrə retrieval + məna yönümlü yoxlama artıq kifayət qədər güclü bazadır.

Növbəti addımlar:

1. final məna yönümlü aspect taxonomy-ni ayrıca config kimi sabitləşdirmək;
2. Hacknet `deep-research.md` sənədinə bu quantitative nəticələrin executive versiyasını əlavə etmək;
3. Hacknet report-u master brief-dəki per-game professional struktura yaxınlaşdırmaq;
4. bundan sonra **Midnight Protocol** üçün eyni data/araşdırma metoduna keçmək;
5. sonra Hacknet vs Midnight Protocol müqayisəsi aparmaq.

