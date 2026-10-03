# Risk reyestri — Digital investigation / interface-as-world

## 1. Məqsəd

Bu sənəd yeni konsept yaradılarkən və prototiplənərkən ən böyük məhsul/dizayn risklərini erkən görmək üçün istifadə olunur.

Hər risk üçün:
- nədir;
- hansı oyunlarda görünüb;
- niyə təhlükəlidir;
- erkən validation üsulu

verilir.

---

# 2. Risk cədvəli

| ID | Risk | Şiddət | Ehtimal | Erkən siqnal |
|---|---|---|---|---|
| R1 | Player knowledge ≠ system state | Çox yüksək | Yüksək | “Cavabı bilirəm, amma oyun qəbul etmir” |
| R2 | Scripted clue order | Çox yüksək | Yüksək | Bir exact route olmadan progression açılmır |
| R3 | Exact evidence acceptance | Çox yüksək | Orta-Yüksək | Məntiqli güclü dəlil reject olunur |
| R4 | Guidance agency-ni oğurlayır | Yüksək | Yüksək | NPC/system nə düşünməli olduğunu deyir |
| R5 | Auto relevance / highlighting | Yüksək | Orta | Oyunçu yalnız marker axtarır |
| R6 | Repetition | Çox yüksək | Çox yüksək | 30–60 dəqiqədə decision grammar görünür |
| R7 | Feature breadth without depth | Yüksək | Yüksək | Çox mechanic, az reuse |
| R8 | Familiar interface affordance mismatch | Yüksək | Yüksək | “Niyə normal phone/desktop bunu etmir?” |
| R9 | Weak external memory | Yüksək | Orta-Yüksək | Kağız/notepad məcburi olur |
| R10 | Cosmetic choices | Çox yüksək | Yüksək | Fərqli cavablar eyni state-ə gedir |
| R11 | Hidden consequence scoring | Yüksək | Orta | 4 saat sonra erkən gizli choice cəza verir |
| R12 | Weak consequence visibility | Yüksək | Orta-Yüksək | Oyunçu choice-un təsirini hiss etmir |
| R13 | Recovery friction | Yüksək | Yüksək | Retry üçün böyük material təkrarlanır |
| R14 | RNG/fairness | Orta-Yüksək | Orta | Uğursuzluq qərarla əlaqələndirilmir |
| R15 | Onboarding overload | Yüksək | Yüksək | İlk saatda fantasy əvəzinə qayda öyrənilir |
| R16 | Writing/localization gameplay bug | Çox yüksək | Orta-Yüksək | Clue wording səhv anlaşılır |
| R17 | Pacing / low actionable density | Yüksək | Yüksək | Çox oxu/dinləmə, az hypothesis change |
| R18 | Character shallowness | Yüksək | Orta-Yüksək | Oyunçu kiməsə care etmir |
| R19 | Theme-interface mismatch | Yüksək | Orta | Interface mövzunu daşımır |
| R20 | Marketing/gameplay mismatch | Çox yüksək | Orta | Oyunçu başqa janr gözləyir |
| R21 | Sequel/QoL regression | Yüksək | Orta | Əvvəlki həll edilmiş friction geri qayıdır |
| R22 | Single-use mechanics | Orta-Yüksək | Yüksək | Tutorial olunan mechanic bir dəfə görünür |
| R23 | Overly punitive moral answer key | Yüksək | Orta | Etik seçim “correct route” testinə çevrilir |
| R24 | Scope diffusion | Yüksək | Orta | World böyüyür, emotional anchor itir |
| R25 | Audio/polish breaks immersion | Orta | Orta | Volume/acting/UI bug rol hissini sındırır |

---

# 3. R1 — Player knowledge sistem tərəfindən tanınmır

### Görülüb
- Cyber Manhunt
- Need to Know
- Mainlining
- SIMULACRA
- SIMULACRA 3

### Failure
Oyunçu fact-i bilir, amma:
- doğru clue trigger;
- doğru file;
- doğru dialogue;
- doğru scan

olmadığı üçün progression açılmır.

### Niyə kritikdir?
Janrın əsas fantasy-si:
> “mən anladım.”

Sistem:
> “amma mənim nəzərdə tutduğum şəkildə yox.”

deyəndə fantasy dağılır.

### Validation
Critical fact-lar üçün:
- 3 fərqli oyunçu yolu yaz;
- hamısı system state-ə çata bilirmi?

---

# 4. R2 — Scripted clue order

### Görülüb
Cyber Manhunt, SIMULACRA, Mainlining.

### Siqnal
Playtest-də:
- tester əvvəlcədən düzgün nəticəyə gəlir;
- amma game sequence davam etmir.

### Mitigation
Progression:
- clue object deyil;
- semantic fact / condition

üzərindən işləsin.

---

# 5. R3 — Exact evidence acceptance

### Görülüb
Mainlining, Need to Know.

### Problem
Bir faktı sübut edən bir neçə source var, amma yalnız biri keçərlidir.

### Mitigation
Evidence equivalence:
```text
fact_supported_by = any(valid_source_set)
```

### Test
Tester “daha güclü” dəlil təqdim edəndə reject olmamalıdır.

---

# 6. R4 — Guidance agency-ni oğurlayır

### Görülüb
The Operator, Cyber Manhunt, SIMULACRA 3.

### Siqnal
Tester:
> “Mən tapmadım, oyun mənə dedi.”

deyir.

### Mitigation
Guidance levels:
1. interface help;
2. procedural hint;
3. source category hint;
4. semantic answer — default verilməməlidir.

---

# 7. R5 — Auto relevance / highlighting

### Görülüb
Orwell, SIMULACRA 3.

### Risk
Observation:
> marker scan-a

çevrilir.

### Mitigation
Highlight:
- seen state;
- bookmarked state

üçün istifadə olunsun.

Relevance:
- player qərarı olsun.

---

# 8. R6 — Repetition

### Görülüb
Demək olar bütün set-də.

### Əsas səbəb
Content dəyişir, decision grammar dəyişmir.

### Validation
60 dəqiqəlik mechanic map:
- hər 10 dəqiqədə hansı qərar tipi var?

Əgər eyni pattern:
> 70%+ vaxtı

tutur, risk yüksəkdir.

---

# 9. R7 — Feature breadth without depth

### Görülüb
Need to Know, The Operator, SIMULACRA 3.

### Siqnal
Çox:
- app;
- tool;
- mini-game

var, amma hər biri:
- bir dəfə;
- bir cavab;
- az consequence.

### Mitigation
Core mechanic budget:
- az mechanic;
- çox recombination.

---

# 10. R8 — Familiar interface affordance mismatch

### Görülüb
Mainlining, SIMULACRA, Hacknet.

### Test
Real interface istifadəçiləri ilə:
> “İlk olaraq hansı əməli gözlədin?”

soruş.

Ən çox gözlənən basic action-lar yoxdursa:
- ya əlavə et;
- ya visual metaphor-u uzaqlaşdır.

---

# 11. R9 — Weak external memory

### Görülüb
Mainlining, Cyber Manhunt; SIMULACRA 3-də bəzi puzzle-lar.

### Risk
Cognitive load reasoning deyil, yadda saxlama olur.

### Mitigation
- notes;
- pins;
- source history;
- timeline;
- entity list.

### Guardrail
Auto-conclusion etmə.

---

# 12. R10 — Cosmetic choices

### Görülüb
SIMULACRA 3, Need to Know, The Operator-da bəzi sahələr.

### Test
Major choice-lar üçün state diff log:
- variables changed;
- source changed;
- relationship changed;
- content changed.

Əgər çox choice:
> 0–1 state fərqi

yaradırsa cosmetic risk var.

---

# 13. R11 — Hidden consequence scoring

### Görülüb
SIMULACRA 1.

### Risk
Oyunçu:
- risk dərəcəsini bilmədən choice edir;
- saatlar sonra cəza alır;
- nəticəni unfair sayır.

### Mitigation
Local feedback:
- trust shift;
- suspicion;
- visible reaction.

Exact future outcome yenə gizli qala bilər.

---

# 14. R12 — Weak consequence visibility

### Görülüb
SIMULACRA 3, The Operator-da agency complaints.

### Mitigation
Consequence ladder:
1. immediate reaction;
2. mid-term state;
3. final outcome.

Choice ən azı birinci səviyyədə görünməlidir.

---

# 15. R13 — Recovery friction

### Görülüb
Midnight Protocol, SIMULACRA 1/3.

### Risk
Experimentation ölür.

### Mitigation
- checkpoint;
- branch replay;
- fast-forward;
- selective rollback.

### Metric
Wrong branch-dan meaningful new decision-a geri dönmə vaxtı.

---

# 16. R14 — RNG/fairness

### Görülüb
Midnight Protocol.

### Risk
Player competence hissi zəifləyir.

### Mitigation
- probability visible;
- randomness bounded;
- mitigation tool;
- failure reason.

Investigation core-da RNG-dən ehtiyatla istifadə et.

---

# 17. R15 — Onboarding overload

### Görülüb
Cyber Manhunt, Mainlining, SIMULACRA 3, Midnight Protocol.

### Test
First-session:
- neçə yeni noun?
- neçə tool?
- neçə rule?

### Guardrail
İlk 20–30 dəqiqədə:
- core fantasy;
- core loop;
- ilk insight

mütləq görünməlidir.

---

# 18. R16 — Writing/localization gameplay bug

### Görülüb
Cyber Manhunt, SIMULACRA, SIMULACRA 3.

### Risk
Text:
- clue;
- instruction;
- character;
- choice

rolunu eyni anda oynayır.

### QA
Localization test:
- puzzle-aware reviewer;
- context screenshot;
- variable/reference consistency.

---

# 19. R17 — Low actionable information density

### Görülüb
SIMULACRA 3, bəzi Cyber Manhunt/Need to Know hissələri.

### Metric
5 dəqiqəlik interval üzrə:
- new fact;
- new decision;
- changed hypothesis;
- action consequence.

Çox text, sıfır dəyişiklik:
> pacing risk.

---

# 20. R18 — Character shallowness

### Görülüb
SIMULACRA 3.

### Risk
Human-centered investigation:
- emotional stake itirir.

### Validation
30–45 dəqiqədən sonra tester-dən:
- 3 personajın motive-i;
- münasibəti;
- fərqli xüsusiyyəti

soruş.

Cavab verə bilmirsə character density zəifdir.

---

# 21. R19 — Theme-interface mismatch

### Görülüb
SIMULACRA 3 franchise comparison-da.

### Test
Interface-i dəyişəndə theme yenə eyni gücdə işləyirsə:
- medium/theme coupling zəif ola bilər.

Bu həmişə problem deyil.

Amma interface-as-world məhsulda cohesion opportunity itir.

---

# 22. R20 — Marketing/gameplay mismatch

### Görülüb
Mainlining, Midnight Protocol, SIMULACRA 3 sequel expectation.

### Validation
Store-copy blind test:
- “Bu oyunda vaxtın çoxunu nə edəcəyini düşünürsən?”

Cavab actual playtime verb ilə uyğun gəlməlidir.

---

# 23. R21 — Sequel/QoL regression

### Görülüb
SIMULACRA 3.

### Mitigation
Sequel regression checklist:
- save;
- skip;
- speed;
- search;
- notes;
- navigation;
- accessibility.

Previous version ilə feature parity audit.

---

# 24. R22 — Single-use mechanics

### Görülüb
The Operator, SIMULACRA 3.

### Mitigation
Hər core mechanic:
- intro;
- reuse;
- combination;
- mastery payoff

görməlidir.

Əks halda onu set-piece kimi planlaşdır və tutorial cost-u minimum saxla.

---

# 25. R23 — Moral answer key

### Görülüb
SIMULACRA 1, Need to Know riskləri.

### Mitigation
Design review:
- hər moral choice üçün iki legitim argument yaz.
- yalnız birinə “correct” label vermə.

---

# 26. R24 — Scope diffusion

### Görülüb
SIMULACRA 3.

### Risk
World böyüyür:
- care azalır.

### Mitigation
Hər geniş scope layer üçün:
- personal anchor;
- immediate stake;
- recurring human relationship.

---

# 27. R25 — Audio/polish breaks immersion

### Görülüb
SIMULACRA 3, Hacknet-də texniki risk, digər UI-heavy oyunlar.

### Risk
Interface-as-world-də:
- kiçik polish bug belə fiction break yaradır.

### QA
- headset pass;
- volume normalization;
- tab/window state;
- resume;
- save;
- display scaling.

---

# 28. Prototip mərhələsi üçün top 10 red flag

Aşağıdakılardan 3+ eyni build-də görünürsə concept/system reconsider edilməlidir:

1. Tester “nə etməli olduğumu tapmaq çətindir” yox, “oyun nəyi qəbul etdiyini anlamıram” deyir.
2. Doğru reasoning reject olunur.
3. Tester marker/icon gözləyir, content oxumur.
4. Xarici notepad məcburi olur.
5. 30 dəqiqədən sonra loop tam proqnozlaşdırılır.
6. Choice-lar arasında real fərq yoxdur.
7. Səhv qərarın səbəbi bilinmir.
8. Guide NPC hypothesis-i özü verir.
9. Store promise-dən fərqli dominant activity çıxır.
10. Oyunun ən yaxşı mechanic-i ilk saatda görünmür.

---

# 29. Risk prioriteti

## Prototype-dan əvvəl
- R1 knowledge state
- R4 guidance
- R6 repetition
- R10 agency
- R19 theme/interface
- R20 positioning

## Vertical slice
- R8 affordance
- R9 memory
- R15 onboarding
- R17 pacing
- R18 character
- R22 mechanic reuse

## Production
- R13 recovery
- R16 writing/localization
- R21 regression
- R25 polish/audio

---

# 30. Yekun

Ən təhlükəli risk:

> **oyunçunun özünü ağıllı hiss etməli olduğu janrda sistemin onun reasoning-ni tanımamasıdır.**

Bu baş verəndə:
- investigation → trigger hunt;
- deduction → trial-and-error;
- agency → dialogue cosmetics;
- realism → UI friction

olur.

Risk reyestri konsept qiymətləndirmə və prototip test planı ilə birlikdə istifadə edilməlidir.
