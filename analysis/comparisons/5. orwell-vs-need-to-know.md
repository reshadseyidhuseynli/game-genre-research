# Orwell vs Need to Know — Məlumat seçimi, surveillance və qərar sərbəstliyi müqayisəsi

## 1. Müqayisə sualı

Əsas sual:

> **Oxşar surveillance / privacy premise-i daxilində Orwell daha dar və məqsədli sistemlə niyə daha güclü oyunçu reaksiyası alır, Need to Know isə daha geniş feature və agency vədinə baxmayaraq daha çox sürtünmə yaradır?**

Bu müqayisə “qalib” seçmir.

Məqsəd:

- hansı dizayn modeli hansı rol hissini yaradır;
- hansı sistem real qərar sərbəstliyi verir;
- hansı hallarda seçim sadəcə UI səthi kimi qalır;
- consequence necə görünən olur;
- məlumat əsaslı gameplay nə vaxt deduction, nə vaxt checklist işinə çevrilir

suallarına cavab verməkdir.

---

## 2. Niyə müqayisə edilə bilirlər?

Ortaq əsaslar:

- surveillance və privacy mövzusu;
- dövlət / qurum daxilində məlumat işi;
- insanların şəxsi rəqəmsal həyatına giriş;
- text və informasiya əsaslı interfeys;
- əxlaqi dilemma;
- “məlumat gücdür” fantasy-si;
- fictional desktop / data workflow;
- hekayənin şəxsi məlumat üzərindən çatdırılması;
- texniki bacarıqdan çox interpretasiya və qərar.

Əsas fərq:

### Orwell

```text
məlumatı tap
→ kontekstdə qiymətləndir
→ nəyi ötürəcəyini seç
→ adviser reaksiya verir
→ dünya dəyişir
```

### Need to Know

```text
qaydanı oxu
→ profildə uyğun dəlili tap
→ işarələ / təsnif et
→ score / compliance al
→ clearance və side systems
→ növbəti missiya
```

Orwell-un əsas feli **seçmək və ötürmək**, Need to Know-un əsas feli isə çox vaxt **uyğunlaşdırmaq və təsnif etmək** olur.

---

## 3. Məlumat toplusu snapshot-u

| Metrik | Orwell | Need to Know |
|---|---:|---:|
| Verified/API English reviews | 8,549 | 272 |
| Müsbət | 7,735 | 178 |
| Mənfi | 814 | 94 |
| Müsbət payı | **90.48%** | **65.44%** |
| Median oyun müddəti | 5.07h | 7.99h |
| 0–1h müsbət | **54.34%** | **21.43%** |
| 1–3h müsbət | yüksək | **48.89%** |
| 3–10h müsbət | **93.26%** | **71.26%** |
| 10h+ müsbət | **95.28%** | **78.57%** |

Məlumat toplusu ölçüləri çox fərqlidir. Buna görə absolute mention count birbaşa müqayisə edilmir.

Əsas müqayisə:

- baseline-a nisbət;
- pattern direction;
- semantic audit;
- oyun müddəti qrupları;
- məhsul vədi;
- oyunçu təcrübəsinin həmin vədlə uyğunluğu.

---

## 4. İlk saat: ən böyük fərqlərdən biri

Orwell-un 0–1 saat qrupunda da risk var, amma müsbət pay təxminən **54%**-dir.

Need to Know-da isə:

> **21.43%**

Bu çox böyük fərqdir.

### Orwell-da ilk saat problemi

- gameplay əvvəlcə “highlight olunmuş mətni sürükləmək” kimi görünə bilər;
- əsas moral/consequence dəyəri tam açılmaya bilər;
- auto-highlight discovery-ni zəiflədir.

### Need to Know-da ilk saat problemi

- nə etməli olduğu aydın deyil;
- tool və UI öyrənilməsi çətindir;
- fail condition erkən və qeyri-şəffaf ola bilər;
- launch dövründə bug-lar təcrübəni daha da ağırlaşdırıb.

### Əsas fərq

Orwell-un erkən problemi:

> **“Bu sistem hələ niyə maraqlıdır?”**

Need to Know-un erkən problemi:

> **“Bu sistem məndən nə istəyir?”**

İkincisi daha fundamental qəbul baryeridir.

---

## 5. Problem framing

### Orwell

Oyunçu adətən anlayır:

- hansı şəxs araşdırılır;
- hansı məlumat parçaları mövcuddur;
- hansı məlumatı profile-a ötürə bilər;
- seçimdən sonra adviser/world reaksiya verəcək.

Sistem relevance-i həddindən artıq highlight edir, amma problem space aydındır.

### Need to Know

Oyunçu:

- qaydanı oxuyur;
- çoxsaylı profillər arasında məlumat axtarır;
- hansı dəlilin formal olaraq hansı rule-a bağlanacağını tapmalıdır;
- bəzən sistemin qəbul etdiyi cavabla məna səviyyəsində razılaşmır.

### Nəticə

> **Orwell problem space-i həddindən artıq daraldır; Need to Know isə bəzən problem space-i kifayət qədər aydın etmir.**

Optimal model:

> **goal və qayda aydın, interpretation isə oyunçuya açıq olmalıdır.**

---

## 6. Məlumatın rolu

### Orwell

Məlumat özü qərar materialıdır.

Bir datachunk:

- context;
- character;
- bias;
- consequence

yarada bilər.

Əsas sual:

> “Bunu sistemə verməliyəmmi?”

### Need to Know

Məlumatın böyük hissəsi:

- rule-a uyğun gəlir / gəlmir;
- threat / safe classification-a xidmət edir;
- score/compliance nəticəsi yaradır.

Əsas sual çox vaxt:

> “Bu rule-a hansı dəlil match olur?”

### Dizayn fərqi

Orwell:

> **məlumatın mənası üzərində qərar**

Need to Know:

> **məlumatın kateqoriyaya uyğunluğu üzərində qərar**

Birinci model narrative və etik consequence üçün daha zəngin material yaradır.

---

## 7. Agency decomposition

Qərar sərbəstliyini dörd qata ayırmaq faydalıdır.

| Agency növü | Orwell | Need to Know |
|---|---|---|
| Discovery agency | Aşağı-Orta | Orta |
| Interpretation agency | Orta | Aşağı-Orta |
| Selection agency | **Yüksək** | Orta |
| Consequence agency | **Yüksək** | Aşağı-Orta / qeyri-bərabər |

### Orwell

Oyunçu:

- nəyi ötürəcəyini seçir;
- bəzi məlumatı gizlədə bilir;
- həmin seçim adviser-in target modelini dəyişir;
- world state-də görünən reaksiya ala bilir.

### Need to Know

Oyunçu:

- daha çox sistem və seçim səthi görür;
- amma bəzi story/relationship seçimləri progression tərəfindən məcbur edilir;
- “yox” demək bəzən alternativ world state yox, retry/game over yaradır.

### Əsas nəticə

> **Feature breadth agency breadth demək deyil.**

---

## 8. Selection vs classification

Bu iki oyunun ən fundamental fərqidir.

### Orwell

Core verb:

> **select**

Sən məlumatı profile-a daxil etməklə sistemin nə bildiyini formalaşdırırsan.

### Need to Know

Core verb çox vaxt:

> **classify**

Sən əvvəlcədən verilmiş qaydalara görə insanı və dəlili uyğunlaşdırırsan.

Selection:

- intent;
- omission;
- bias;
- consequence

yaradır.

Classification:

- correctness;
- rule adherence;
- performance

yaradır.

Hər ikisi maraqlı ola bilər.

Amma Need to Know özünü daha çox moral choice / freedom oyunu kimi satdığı üçün classification-dominant loop expectation mismatch yaradır.

---

## 9. Consequence visibility

Orwell-un əsas güclərindən biridir.

Məlumat ötürəndə:

- adviser comment edir;
- target perception dəyişir;
- arrest/intervention kimi action yarana bilir;
- chat/call/story state dəyişə bilir.

Need to Know-da nəticə daha çox:

- score;
- compliance;
- clearance;
- relationship meter;
- bəzən game over

kimi görünür.

Bəzi mission nəticələri və story beat-ləri var, amma rəy auditində oyunçuların bir hissəsi “mənim seçimim nəyi dəyişdi?” sualına zəif cavab aldığını bildirir.

### Principle

> **Consequence hidden variable yox, oyunçunun hiss etdiyi changed state olmalıdır.**

---

## 10. Failure modeli

### Orwell

Əsas risk:

- insufficient context;
- yanlış datachunk;
- irreversible choice.

Amma oyunçu çox vaxt qərarının consequence-ını görür.

### Need to Know

Failure daha çox:

- exact rule misunderstanding;
- tool misuse;
- UI confusion;
- acceptance-rule opacity;
- relationship maintenance;
- progression-compatible olmayan seçim

ilə bağlı ola bilir.

### Əsas fərq

Orwell-da failure daha çox:

> **“mən bu məlumatı səhv qiymətləndirdim”**

kimi hiss oluna bilər.

Need to Know-da failure tez-tez:

> **“sistemin formal qaydasını düzgün tapmadım”**

kimi hiss olunur.

Birincisi reasoning mastery-ni, ikincisi prosedur memorization-u gücləndirir.

---

## 11. Moral ambiguity

Hər iki oyunun güclü mövzusudur.

### Orwell

Moral ambiguity:

- konkret məlumatı ötürmək / gizlətmək;
- kontekstdən çıxarmaq;
- şəxsi məlumatı dövlət qərarına çevirmək

kimi micro-decision-larda yaranır.

### Need to Know

Moral ambiguity:

- Department;
- underground groups;
- şəxsi qazanc;
- data selling;
- career/status

kimi daha geniş sistemlərdə qurulur.

Need to Know nəzəri olaraq daha geniş etik məkan yaradır.

Amma progression constraint-ləri həmin məkanın bir hissəsini bağlayanda promise zəifləyir.

### Principle

> **Moral ambiguity yalnız “iki tərəf göstərmək” deyil; oyunçu hər iki mövqedə davam edə bilməlidir.**

---

## 12. UI və cognition

### Orwell

UI problemi:

- auto-highlight relevance-i qabaqcadan verir;
- adviser interpretasiya yükünün bir hissəsini alır.

Yəni problem:

> **oyunçu az düşünür.**

### Need to Know

UI problemi:

- pəncərə clutter;
- unclear controls;
- müqayisə friction-u;
- evidence/rule münasibətinin zəif görünməsi.

Yəni problem:

> **oyunçu düşünmək əvəzinə interfeyslə mübarizə aparır.**

Bu iki ekstrem gələcək dizayn üçün çox dəyərlidir.

Optimal:

> **UI cognitive load-u daşısın, reasoning-i əvəz etməsin.**

---

## 13. Onboarding

### Orwell

Onboarding əsasən interaction grammar-i tez göstərir.

Problem:

- sistemin dərin dəyəri gec görünür.

### Need to Know

Onboarding-də həm control, həm system model problemi var.

Oyunçu:

- aləti;
- mission flow-u;
- classification logic-i;
- fail səbəbini

eyni anda öyrənməyə məcbur ola bilir.

### Cross-game principle

Onboarding üç mərhələ olmalıdır:

1. **control** — nəyi necə edirəm?
2. **system** — qaydalar necə işləyir?
3. **judgment** — yaxşı qərar necə görünür?

Need to Know ilk iki mərhələdə, Orwell isə daha çox üçüncü mərhələnin payoff-ını erkən göstərməkdə risk yaşayır.

---

## 14. Təkrarçılıq

Hər iki oyunda təkrarçılıq var.

### Orwell

```text
open
→ read
→ highlight / select
→ upload
→ repeat
```

### Need to Know

```text
rule
→ profile
→ match
→ classify
→ repeat
```

Fərq:

Orwell eyni action grammar-i:

- character context;
- contradictory evidence;
- moral consequence

ilə dəyişməyə çalışır.

Need to Know isə daha çox feature və mission variation əlavə edir, amma əsas classification grammar-i uzun müddət qalır.

### Principle

> **Təkrarçılığı feature sayı yox, qərar strukturunun dəyişməsi azaldır.**

---

## 15. Content length və pacing

Orwell daha qısa məhsuldur.

Bu, onun sadə interaction grammar-i üçün üstünlükdür:

- novelty bitməzdən əvvəl hekayə bağlanır;
- consequence density nisbətən yüksək qalır.

Need to Know daha uzun təcrübədir.

Bu, progression və world-building üçün üstünlük yarada bilər.

Amma eyni loop uzandıqca:

- grind;
- filler;
- chore

hissi yaranır.

### Nəticə

> **Eyni mexanikanın nə qədər yaxşı olması ilə onun neçə saat daşıya bilməsi ayrı suallardır.**

---

## 16. Məhsul vədi və expectation

### Orwell

Store promise əsasən real core mechanic-i izah edir:

- məlumatı topla;
- yalnız sənin ötürdüyün məlumat istifadə ediləcək;
- nəticə yaranacaq.

### Need to Know

Store promise daha genişdir:

- privacy-ni müdafiə et;
- police state qur;
- leak et;
- şəxsi qazanc götür;
- qərarların nəticəsini gör.

Rəy auditində ən ağır tənqidlərdən biri məhz budur:

> **“Your call” deyilən şey bəzən real seçim deyil.**

### Principle

> **Store promise dominant player freedom-u şişirtməməlidir.**

Expectation mismatch məhsul keyfiyyətindən ayrıca satisfaction driver-dir.

---

## 17. Yaradıcı məqsədi vs nəticə

### Orwell

Yaradıcı məqsədi:

- information selection;
- ambiguity;
- consequence;
- player bias.

Outcome:

- böyük ölçüdə uğurlu;
- auto-highlight və adviser guidance agency-ni qismən zəiflədir.

### Need to Know

Yaradıcı məqsədi:

- watcher olmaq;
- güc və vicdan;
- broad moral freedom;
- career/status temptation.

Outcome:

- premise və moral theme işləyir;
- story bəyənilir;
- amma broad freedom promise bəzi progression constraint-ləri ilə ziddiyyətə düşür.

### Əsas fərq

Orwell:

> **məhdud promise, daha güclü delivery**

Need to Know:

> **geniş promise, qeyri-bərabər delivery**

---

## 18. Niyə oyunçu nəticələri fərqlənmiş ola bilər?

Bu causal hökm deyil; dəlil-backed hipotezlərdir.

### Hipotez 1 — Daha aydın core verb

Orwell:

> “məlumatı seç və ötür”

Need to Know:

> “qaydaları anla, dəlili tap, düzgün formal şəkildə təsnif et, side systems-i də idarə et”

Birinci daha sadə mental model yaradır.

### Hipotez 2 — Daha yüksək consequence density

Orwell-da decision → reaction chain daha qısadır.

Need to Know-da decision nəticəsi bəzən score/relationship/progression qatında itir.

### Hipotez 3 — Erkən friction

Need to Know 0–1h cohort-u çox zəifdir.

Orwell da erkən risk yaşayır, amma fundamental usability daha sağlamdır.

### Hipotez 4 — Promise–delivery mismatch

Need to Know broad agency satır.

Bəzi kritik choices isə real branch deyil.

### Hipotez 5 — Length amplifies repetition

Need to Know daha uzun content scope-u ilə əsas loop-un zəifliklərini böyüdür.

---

## 19. Bizim layihə üçün transferable dərslər

### 1. Az, amma real seçim çox, amma saxta seçimdən güclüdür

Bir seçim future state dəyişirsə, sayından daha vacibdir.

### 2. Consequence mümkün qədər tez görünməlidir

Action → reaction məsafəsi uzandıqca agency hissi zəifləyir.

### 3. Semantic reasoning prosedurdan üstün olmalıdır

Oyunçu doğru düşündüyü halda UI ritualına görə tam uduzmamalıdır.

### 4. UI external memory olsun

Faktları, source-u, contradiction-u və hypothesis-i daşımalıdır.

### 5. UI cavabı deməsin

Orwell-un auto-highlight problemi buna nümunədir.

### 6. Moral seçim fail filterinə çevrilməməlidir

Mənfi nəticə ilə də dünya davam etməlidir.

### 7. Geniş feature set = dərin sistem deyil

Dərinlik meaningful decision density-dir.

### 8. Onboarding system model-i öyrətməlidir

Controls öyrətmək kifayət deyil.

### 9. Uzunluq decision variety ilə əsaslandırılmalıdır

Eyni grammar 20 saat davam edirsə, content çoxluğu üstünlük olmaya bilər.

### 10. Store promise real gameplay freedom-u dürüst izah etməlidir

Marketing expectation dizayn sisteminin bir hissəsidir.

---

## 20. İmkan istiqaməti

Bu müqayisədən ən maraqlı opportunity:

```text
aydın case goal
→ broad but bounded information space
→ oyunçu-built interpretation
→ explicit evidence support
→ choose what to reveal / do
→ visible immediate consequence
→ changed information space
```

Burada:

- Orwell-un information selection və consequence modeli saxlanır;
- Need to Know-un power progression və broader world ambition-u saxlanır;
- Orwell-un auto-highlight hand-holding-i azalır;
- Need to Know-un exact-rule və forced-branch problemi çıxarılır.

Bu hələ konkret oyun ideyası deyil.

---

## 21. Risk xəritəsi

| Risk | Orwell | Need to Know | Gələcək validation |
|---|---|---|---|
| Early-session confusion | Medium | **High** | ilk 30 dəqiqə novice test |
| Həddindən artıq guidance | **High** | Low-Medium | progressive hint A/B |
| UI friction | Medium | **High** | multi-source evidence usability |
| Saxta seçim | Medium | **High** | branch persistence test |
| Weak consequence visibility | Low | Medium-High | action→reaction timing |
| Təkrarçılıq | High | **High** | 60–120 dəq loop test |
| Insufficient context | Medium | Medium | evidence sufficiency test |
| Overlong content | Low-Medium | **High** | decision-variety timeline |
| Technical instability | Medium | High launch / mixed later | save/soft-lock QA |

---

## 22. Müqayisə nəticəsi

Orwell göstərir:

> **Məlumatın özünü seçim materialına çevirmək və nəticəni tez göstərmək, az interaction ilə belə güclü agency yarada bilər.**

Need to Know göstərir:

> **Daha çox feature, daha çox sistem və daha çox seçim səthi real agency yaratmır; əgər sistem yalnız bir yolu davam etdirməyə icazə verirsə və oyunçu semantic reasoning əvəzinə acceptance rule axtarırsa, genişlik dərinliyə çevrilmir.**

Birlikdə əsas prinsip:

> **Digital-investigation / surveillance oyununda ən vacib dizayn metriklərindən biri “meaningful decision density”dir: oyunçunun başa düşdüyü, öz niyyətinə görə verdiyi və nəticəsini real world state-də gördüyü qərarların sıxlığı.**

---

## 23. Mənbələr

### Orwell

- `analysis/orwell/theme-analysis.md`
- `analysis/orwell/deep-research.md`
- `analysis/orwell/presentation-brief.md`
- `data/reports/orwell/summary.md`

### Need to Know

- `analysis/need-to-know/theme-analysis.md`
- `analysis/need-to-know/deep-research.md`
- `analysis/need-to-know/presentation-brief.md`
- `data/reports/need-to-know/summary.md`

## Status

**Müqayisə:** tamamlanıb  
**Əsas finding:** dar, consequence-rich selection model geniş, amma progression-constrained choice modelindən daha güclü agency hissi yarada bilər  
**Növbəti əsas Tier A:** Mainlining
