# Digital Investigation / Interface-as-World — Yekun janr araşdırma hesabatı

> **Rəhbərlik üçün əsas deliverable**  
> Research snapshot: **3 oktyabr 2026**  
> Məqsəd: yeni oyun ideyası yaratmazdan əvvəl bazar, oyunçu ehtiyacları, işləyən/işləməyən dizayn nümunələri, imkanlar və risklər üçün qərar bazası yaratmaq.

---

# 1. Rəhbərlik üçün xülasə

Bu araşdırma terminal, hacking, digital investigation, surveillance, fictional OS və found-device tipli oyunların hansı səbəblə işlədiyini və hansı səbəblə zəiflədiyini sistemli şəkildə araşdırdı.

Dərin araşdırılmış əsas oyunlar:

- Hacknet
- Midnight Protocol
- Cyber Manhunt
- The Operator
- Orwell: Keeping an Eye On You
- Mainlining
- SIMULACRA
- SIMULACRA 3

Focused comparator:

- Need to Know

Əsas nəticə:

> **Bu janrın əsas məhsul dəyəri “hacking”, “terminal” və ya “telefon” deyil. Oyunçu məlumatı özü müşahidə edib əlaqələndirmək, öz nəticəsini çıxarmaq və sistemin həmin reasoning-i tanıdığını görmək istəyir.**

Ən güclü oyunlarda dörd şey üst-üstə düşür:

1. **Bir cümlədə başa düşülən rol fantasy-si**
2. **Interface-in oyunun dünyasının özü olması**
3. **Məlumatın özünün mükafat olması**
4. **Oyunçu qərarının görünən nəticə yaratması**

Ən təkrarlanan uğursuzluq isə belədir:

> **oyunçu doğru nəticəyə gəlir, amma sistem yalnız developer-in əvvəlcədən seçdiyi exact clue, exact file, exact query və ya exact progression trigger-i qəbul edir.**

Bu problem müxtəlif formalarda:
- Cyber Manhunt;
- Mainlining;
- Need to Know;
- SIMULACRA;
- SIMULACRA 3

araşdırmalarında təkrarlandı.

## Rəhbərlik üçün ən vacib 10 nəticə

1. **Rol fantasy-si feature sayından vacibdir.**
2. **Interface-as-world modeli kommersiya baxımından işləyə bilir.**
3. **Tam realizm lazım deyil; seçilmiş həqiqilik daha sağlamdır.**
4. **Məlumat özü progression reward ola bilər.**
5. **Player knowledge semantic state kimi modelləşdirilməlidir.**
6. **Guidance procedure-a kömək etməli, interpretation-u oğurlamamalıdır.**
7. **Dərinlik feature sayından yox, meaningful decision density-dən gəlir.**
8. **Choice sayı agency deyil; real state divergence agency-dir.**
9. **Theme və interface eyni sosial məna daşıyanda immersion güclənir.**
10. **Ən böyük açıq imkan semantic investigation + player-built knowledge graph + multiple valid evidence route + visible consequence kombinasiyasıdır.**

## Bazar baxımından əsas nəticə

Strong reference-lər göstərir ki bu niş:
- yalnız hacker audience-ə bağlı deyil;
- professional investigation;
- surveillance;
- phone mystery

formatlarında da sağlam traction yarada bilir.

2026-10-03 Steam mağaza görünüşü:

- Hacknet — **94% / ~7.66k English**
- Orwell — **90% / ~4.87k English**
- The Operator — **89% / ~3.64k English**
- SIMULACRA — **93% / ~2.37k English**

Bu, interface-heavy məhsulun özlüyündə bazar maneəsi olmadığını göstərir.

---

# 2. Araşdırmanın məqsədi və əhatəsi

## 2.1. Biznes / məhsul məqsədi

Yeni oyun ideyasını əvvəlcədən seçmək yox.

Əvvəl:

- bazarı başa düşmək;
- uğurlu/orta/zəif məhsulları müqayisə etmək;
- oyunçu ehtiyaclarını çıxarmaq;
- təkrarlanan failure mode-ları tapmaq;
- gələcək concept-lərin hansı riskləri erkən test etməli olduğunu müəyyən etmək.

Araşdırmadan sonra ideya generation ayrıca product-discovery mərhələsi kimi başlayacaq.

---

## 2.2. Oyun seti

### Tier A
- Hacknet
- Midnight Protocol
- Cyber Manhunt
- The Operator
- Orwell
- Mainlining
- SIMULACRA
- SIMULACRA 3

### Focused comparator
- Need to Know

### Məcburi müqayisələr
- Hacknet vs Midnight Protocol
- Cyber Manhunt vs The Operator
- Cyber Manhunt vs Mainlining
- Orwell vs Need to Know
- SIMULACRA vs SIMULACRA 3

Əlavə:
- Mainlining vs SIMULACRA
- Cyber Manhunt vs SIMULACRA
- üç-oyun hacking/digital-investigation comparison-ları.

---

## 2.3. Məlumat mənbələri

- Steam review API dataset-ləri;
- Steam store metadata;
- deterministik topic/aspect scan;
- bütün və ya geniş mənfi rəy auditləri;
- helpful/recent/high-playtime müsbət rəy auditləri;
- developer/publisher materialları;
- müsahibələr;
- açıq satış/franchise məlumatları;
- oyunlararası comparison.

---

## 2.4. Metodun əsas qaydası

Üç informasiya növü ayrılıb:

### Dataset faktı
Məsələn:
- rəy sayı;
- positive ratio;
- playtime cohort.

### Xarici fakt
Məsələn:
- release;
- developer;
- verified satış məlumatı.

### Analitik nəticə
Məsələn:
> “scope artımı intimacy-ni zəiflədib.”

Bu, dəlillərin interpretasiyasıdır; causal fact kimi təqdim edilmir.

---

## 2.5. Nə ölçülmür?

Bu research:
- tam bazar ölçüsü;
- bütün platformalarda gəlir;
- user acquisition CAC;
- publisher müqavilələri;
- hər region üzrə sales;
- gələcək satış forecast-u

hesablamır.

Steam review sayı:
> satışın birbaşa ekvivalenti deyil.

---

# 3. Bazar mənzərəsi

## 3.1. Alt-janrlar

Araşdırılan sahə beş əsas məhsul ailəsinə bölünür.

### A. Terminal / hacker competence
Reference:
- Hacknet

Rol:
> “Terminalda hakerəm.”

Əsas dəyər:
- competence;
- technical theater;
- secret access.

---

### B. Taktiki hacking / system planning
Reference:
- Midnight Protocol

Rol:
> “Şəbəkəyə daxil olub loadout və resurslarla plan qururam.”

Əsas dəyər:
- hazırlıq;
- risk;
- taktiki seçim.

---

### C. Digital investigation / OSINT-like
References:
- Cyber Manhunt
- Mainlining
- The Operator

Rol:
> “Rəqəmsal izlərdən nə baş verdiyini tapıram.”

Əsas dəyər:
- search;
- evidence;
- relation;
- hypothesis.

---

### D. Surveillance / information selection
References:
- Orwell
- Need to Know

Rol:
> “Başqalarının şəxsi məlumatına çıxışım var və hansı məlumatın istifadə ediləcəyinə qərar verirəm.”

Əsas dəyər:
- privacy;
- authority;
- ethics;
- consequence.

---

### E. Found-device / personal-phone investigation
References:
- SIMULACRA
- SIMULACRA 3

Rol:
> “Başqa insanın şəxsi telefonunu araşdırıram.”

Əsas dəyər:
- intimacy;
- private data;
- mystery;
- device authenticity.

---

# 4. Market snapshot

| Oyun | İl | Cari Steam siqnalı* | Research positive | Rol | Interface | Nəticə |
|---|---:|---|---:|---|---|---|
| Hacknet | 2015 | 94% / 7.66k English | 94.13% | hacker | terminal | Güclü |
| Orwell | 2016 | 90% / 4.87k English | 90.48% | surveillance analyst | surveillance UI | Güclü |
| Mainlining | 2017 | 77% / 285 | 75.66% | digital detective | desktop | Orta |
| SIMULACRA | 2017 | 93% / 2.37k English | 90.53% | found-phone investigator | phone | Güclü |
| Need to Know | 2018 | 74% / 175 | 65.44% | surveillance employee | bureaucratic OS | Zəif/contrast |
| Cyber Manhunt | 2021 | 80% / 816 English | 80.40% | digital investigator | browser/database | Orta |
| Midnight Protocol | 2021 | 87% / 238 | 84.05% | tactical hacker | keyboard/network | Niş, sağlam |
| SIMULACRA 3 | 2022 | 56% / 328 | 58.80% | journalist/phone investigator | phone + Atlas | Zəif/contrast |
| The Operator | 2024 | 89% / 3.64k English | 89.71% | FDI operator | workstation | Güclü |

\* Store review surface research API filter-i ilə eyni deyil.

---

# 5. Açıq kommersiya siqnalları

## Hacknet

Fellow Traveller press kit:
- ilk il **200,000+ copies**.

Bu:
- terminal interface;
- aşağı istehsal miqyası;
- strong fantasy

kombinasiyasının real kommersiya traction-u yarada bildiyini göstərir.

---

## Orwell

2017 GamesBeat məlumatı:
- original Orwell **130,000+ copies** satmışdı;
- bu nəticə Season Two üçün kifayət etmişdi.

Surveillance/ethical investigation:
> yalnız “art game” nişi deyil; davamlı franchise traction-u yarada bilib.

---

## The Operator

Verified sales rəqəmi yoxdur.

Amma:
- 2024 release;
- 3k+ English reviews;
- ~89% sentiment;
- recent review activity

güclü modern market siqnalıdır.

---

## SIMULACRA

Original:
- yüksək sentiment;
- franchise continuation;
- PC + mobile presence.

SIMULACRA 3:
- eyni franchise;
- xeyli zəif sentiment.

Dərs:
> brand core experience regression-u kompensasiya etmir.

---

# 6. Oyunçu ehtiyacları və əsas fantasy-lər

## Need 1 — Competence

Oyunçu istəyir:
> “Mən bunu bacarıram.”

Hacknet:
- command fluency.

The Operator:
- analyst competence.

Mainlining:
- evidence competence.

Əsas principle:
> difficulty özü competence deyil; sistem oyunçunun düzgün reasoning-ni tanımalıdır.

---

## Need 2 — Secret access

Oyunçu:
- başqa server;
- şəxsi mesaj;
- dövlət database;
- şəxsi telefon

kimi normalda bağlı məlumat sahəsinə daxil olur.

Bu voyeuristic/forbidden-access hissi güclü hook-dur.

---

## Need 3 — Discovery

Əsas sual:
> “Orada başqa nə var?”

Bu:
- retention;
- exploration;
- narrative

driver-ıdır.

---

## Need 4 — “Aha!” moment

Janrın premium emosional payoff-larından biri:

> iki ayrı faktı birləşdirib nəticəni özün tapmaq.

Əgər system bunu player-dan əvvəl edir:
- satisfaction azalır.

---

## Need 5 — Peşəkar rol

Hacker;
operator;
analyst;
investigator;
surveillance officer.

Role clarity:
- onboarding-i;
- store positioning-i;
- immersion-u

gücləndirir.

---

## Need 6 — Human intimacy

Xüsusilə:
- Cyber Manhunt;
- SIMULACRA;
- Orwell

göstərir ki şəxsi məlumat:
> yalnız clue deyil.

O:
- empathy;
- suspicion;
- leverage;
- moral context

yaradır.

---

## Need 7 — Authority və consequence

Oyunçu:
- yalnız tapmaq yox;
- məlumatla nə edəcəyinə qərar vermək istəyir.

Orwell bu ehtiyacı ən yaxşı reference-lərdən biri kimi göstərir.

---

# 7. Bu oyunları nə işlək edir?

## 7.1. Bir cümləlik promise

Güclü:
- Hacknet
- Orwell
- The Operator
- SIMULACRA

hamısı bir cümlədə satıla bilir.

Bu:
- acquisition;
- onboarding;
- word-of-mouth

üçün böyük üstünlükdür.

---

## 7.2. Interface = world

Oyunçunun klikləri:
- menu action yox;
- world action-dır.

Bu həm immersion, həm də production efficiency yaradır.

---

## 7.3. Selected authenticity

Tam realizm yox.

Kifayət qədər:
- terminology;
- workflow;
- visual grammar

rol hissini satır.

---

## 7.4. Information-as-reward

Yaxşı clue:
- yeni objective açmaqla kifayətlənmir;
- story və ya character haqqında mənalı bilik verir.

---

## 7.5. Memorable rule-break moments

Hacknet:
- adi command loop-dan fərqlənən xüsusi hadisələr.

SIMULACRA:
- phone corruption.

The Operator:
- xüsusi investigation set-pieces.

Bu anlar:
> routine loop-u emosional olaraq yüksəldir.

---

## 7.6. Audio və feedback

Hacknet:
- soundtrack.

The Operator:
- voice/audio.

SIMULACRA:
- phone soundscape.

Interface-heavy oyunlarda:
> audio world-building yükünü böyük ölçüdə daşıyır.

---

## 7.7. Consequence

Orwell:
- action → visible impact.

Bu:
- agency-ni real edir;
- moral choice-u mechanic edir.

---

# 8. Əsas uğursuzluq pattern-ləri

| Problem | Oyunçuya təsir | Nümunələr | Dizayn nəticəsi |
|---|---|---|---|
| Player knowledge tanınmır | “Mən bilirəm, oyun qəbul etmir” | Cyber Manhunt, Mainlining, Need to Know | semantic knowledge state |
| Scripted clue order | investigation checklist olur | Cyber Manhunt, SIMULACRA | multiple valid routes |
| Exact evidence | trial-and-error | Mainlining | evidence equivalence |
| Over-guidance | agency azalır | The Operator, SIMULACRA 3 | procedure help, not answer |
| Auto relevance | observation ölür | Orwell, SIMULACRA 3 | player-curated relevance |
| Repetition | novelty bitir | Hacknet, Mainlining, Cyber Manhunt | decision grammar variation |
| Feature breadth without depth | çox mechanic, az mastery | Need to Know, SIMULACRA 3 | reuse + recombination |
| Familiar UI friction | immersion qırılır | Mainlining, SIMULACRA | basic affordance parity |
| Cosmetic choice | “choices matter” inandırmır | SIMULACRA 3 | state divergence |
| Hidden consequence | unfair ending hissi | SIMULACRA | local feedback |
| Recovery friction | replay/experiment azalır | Midnight Protocol, SIMULACRA series | rollback/fast-forward |
| Writing/localization | puzzle correctness zədələnir | Cyber Manhunt, SIMULACRA | writing QA = gameplay QA |
| Low actionable density | pacing zəifləyir | SIMULACRA 3 | decision/info density |
| Theme-interface mismatch | identity zəifləyir | SIMULACRA 3 | semantic fit |
| Market expectation mismatch | yanlış audience gəlir | Mainlining, Midnight Protocol | dominant verb positioning |

---

# 9. Ən vacib comparison-lar

## 9.1. Hacknet vs Midnight Protocol

Hacknet:
- sadə;
- aydın;
- geniş traction.

Midnight Protocol:
- taktiki baxımdan daha dərin;
- daha çətin izah olunur;
- daha dar audience.

### Nəticə

> **Dərinlik acquisition clarity-ni əvəz etmir.**

Yeni konsept:
- həm simple hook;
- həm deeper decision layer

yaratmalıdır.

---

## 9.2. Cyber Manhunt vs Mainlining

Cyber Manhunt:
- cavaba necə çatdığını həddindən artıq idarə edir.

Mainlining:
- cavabı necə təqdim etdiyini həddindən artıq idarə edir.

### Nəticə

> **Knowledge state click path və evidence object-dən ayrı modelləşdirilməlidir.**

---

## 9.3. Cyber Manhunt vs The Operator

Cyber Manhunt:
- geniş;
- daha çox source;
- daha sərbəst görünür.

The Operator:
- focused;
- curated;
- polished;
- daha aydın.

### Nəticə

> **Focused clarity broad-but-brittle investigation-dan daha sağlam məhsul nəticəsi verə bilər.**

Gələcək opportunity:
- The Operator clarity-si;
- Cyber Manhunt autonomy-si.

---

## 9.4. Orwell vs Need to Know

Orwell:
- daha az system;
- daha aydın consequence;
- stronger agency perception.

Need to Know:
- daha çox feature;
- daha çox procedural friction;
- exact acceptance.

### Nəticə

> **Feature count depth deyil.**

---

## 9.5. SIMULACRA vs SIMULACRA 3

SIMULACRA:
- personal phone;
- character intimacy;
- interface horror.

SIMULACRA 3:
- broader town;
- Atlas;
- daha formal investigation.

### Nəticə

> **Scope growth original fantasy regression-u kompensasiya etmir.**

Atlas özü:
- yaxşı opportunity-dir.

Problem:
> player observation-u əvəz edəndə.

---

# 10. Audience segmentation

## Segment A — Fantasy-first hacker

Motivasiya:
- cool technical role;
- secret access;
- terminal identity.

İstədiyi dərinlik:
- orta.

Tolerance:
- abstraction yüksək.

Reference:
- Hacknet.

Risk:
- repetition.

---

## Segment B — Systems/tactics player

Motivasiya:
- planning;
- optimization;
- loadout.

Reference:
- Midnight Protocol.

Tolerance:
- yüksək complexity.

Risk:
- onboarding/RNG/recovery.

---

## Segment C — Deduction-first investigator

Motivasiya:
- clues;
- hypothesis;
- self-directed solving.

References:
- Cyber Manhunt;
- Mainlining;
- The Operator.

Risk:
- scripted acceptance.

---

## Segment D — Narrative / ethical investigator

Motivasiya:
- privacy;
- moral ambiguity;
- authority;
- consequence.

References:
- Orwell;
- Need to Know.

Risk:
- moral answer key;
- UI bureaucracy.

---

## Segment E — Intimacy / mystery player

Motivasiya:
- personal secrets;
- character discovery;
- found-device authenticity.

Reference:
- SIMULACRA.

Risk:
- device personality və character density.

---

# 11. Concept development üçün əsas dizayn prinsipləri

## Principle 1
**Rol fantasy-si bir cümlədə başa düşülməlidir.**

Evidence:
- Hacknet;
- Orwell;
- The Operator;
- SIMULACRA.

Nə et:
- role + verb + interface eyni promise-də.

Qaç:
- feature list pitch.

---

## Principle 2
**Interface world action olmalıdır.**

Nə et:
- hər core click fiction daxilində real action olsun.

Qaç:
- diegetic skin üzərində generic menu gameplay.

---

## Principle 3
**Player knowledge first-class state olsun.**

Nə et:
- semantic fact model.

Qaç:
- exact file/query/trigger progression.

---

## Principle 4
**Bir fact üçün bir neçə keçərli source qəbul et.**

Nə et:
- evidence equivalence.

Qaç:
- “developer-in seçdiyi düzgün file”.

---

## Principle 5
**External memory təşkil etsin, cavab verməsin.**

Nə et:
- notes;
- timeline;
- graph;
- provenance.

Qaç:
- auto-conclusion.

---

## Principle 6
**Guidance procedure üçündür.**

Nə et:
- “tool belə işləyir.”

Qaç:
- “bu personaj yalan danışır.”

---

## Principle 7
**Dərinlik meaningful decision density-dir.**

Nə et:
- reuse + recombination.

Qaç:
- çox single-use mechanic.

---

## Principle 8
**Choice real state divergence yaratmalıdır.**

Nə et:
- relationship;
- information;
- availability;
- consequence change.

Qaç:
- cosmetic dialogue.

---

## Principle 9
**Theme interface-in sosial mənası ilə uyğun olsun.**

Nə et:
- phone → intimacy;
- surveillance → authority/privacy;
- terminal → hacker competence.

Qaç:
- interface-i yalnız vizual gimmick kimi seçmək.

---

## Principle 10
**Recovery experimentation-a imkan verməlidir.**

Nə et:
- fast-forward;
- checkpoint;
- branch replay.

Qaç:
- saatlıq content-i təkrar etdirmək.

---

# 12. İmkan xəritəsi

## Opportunity A — Semantic investigation engine

Ən yüksək prioritet.

Player:
- fact tapır;
- müxtəlif evidence ilə support edir;
- system bunu semantic olaraq tanıyır.

Dəyər:
- agency;
- alternate route;
- less trial-and-error.

Risk:
- implementation complexity.

---

## Opportunity B — Player-built knowledge graph

System:
- note;
- entity;
- time;
- source

saxlayır.

Player:
- relation qurur.

Dəyər:
- reasoning visible olur.

---

## Opportunity C — Claim + evidence

Player:
> “X belədir, çünki A + B.”

Bu:
- reasoning-i first-class gameplay edir.

---

## Opportunity D — Social evidence

Character data:
- lore yox;
- leverage;
- trust;
- contradiction;
- evidence.

---

## Opportunity E — Consequence web

Decision:
- local reaction;
- future information space;
- relationship;
- outcome

dəyişir.

---

## Opportunity F — Interface-native pressure

Threat:
- timer overlay deyil;
- system davranışının dəyişməsidir.

---

## Opportunity G — Persistent workspace

- notes;
- history;
- pins;
- timeline;
- source provenance.

---

# 13. Risk reyestri — executive version

## Çox yüksək

### Knowledge-state mismatch
Ən fundamental janr riski.

### Repetition
Decision grammar dəyişməsə novelty sürətlə ölür.

### Cosmetic choices
Agency promise pozulur.

### Marketing/gameplay mismatch
Yanlış audience və yanlış expectation.

---

## Yüksək

### Over-guidance
Player reasoning oğurlanır.

### Familiar-interface mismatch
Real mental model ilə toqquşur.

### Weak external memory
Cognitive load wrong place-ə düşür.

### Recovery friction
Experiment və replay ölür.

### Onboarding overload
Fantasy payoff gecikir.

### Writing/localization
Puzzle correctness problemidir.

### Character shallowness
Human investigation emotional stake itirir.

### Theme-interface mismatch
Identity zəifləyir.

---

# 14. Concept evaluation framework

Yeni ideyalar 10 sahədə müqayisə olunmalıdır:

| Kateqoriya | Çəki |
|---|---:|
| Rol fantasy-si | 15% |
| Core loop | 15% |
| Knowledge autonomy | 15% |
| Agency/consequence | 12% |
| Interface cohesion | 10% |
| Information/character depth | 10% |
| Repetition/mastery | 8% |
| Onboarding | 6% |
| Market clarity | 5% |
| Feasibility | 4% |

Hard gates:

- Role clarity ≤2/5
- Core loop ≤2/5
- Knowledge autonomy ≤2/5
- Store promise mismatch
- Core value yalnız full production-da test oluna bilir

olarsa idea birbaşa böyük production-a keçməməlidir.

---

# 15. Prototype üçün minimum validation

İlk prototip böyük fake OS olmamalıdır.

Test üçün kifayətdir:

- 1 case;
- 2–3 source type;
- 1 knowledge workspace;
- 1 claim;
- 2 valid evidence route;
- 1 visible consequence.

Ölç:

1. oyunçu rolunu anlayır?
2. ilk “aha” neçə dəqiqədə olur?
3. hint olmadan fact qurur?
4. doğru alternative reasoning qəbul olunur?
5. consequence görünür?
6. external note lazımdır?
7. loop 30–45 dəqiqədə repetitive olur?

---

# 16. Market / positioning constraint-ləri

## 16.1. Dominant verb satılmalıdır

Əgər oyun:
- araşdırma oyunudursa,
“hacking simulator” kimi overpromise etmə.

---

## 16.2. Interface screenshot-da məhsulu anlatmalıdır

Strong reference-lər:
- Hacknet;
- Orwell;
- The Operator;
- SIMULACRA

store visual-dan role fantasy-ni hiss etdirə bilir.

---

## 16.3. Complexity pitch-in yerini tutmamalıdır

“Çox system var”
> market differentiation deyil.

“Bu rolu yaşayırsan”
> daha güclü premise-dir.

---

## 16.4. Qısa runtime problem deyil

3–10 saat bandı bu bazarda normaldır.

Problem:
- content value;
- replay friction;
- weak payoff.

---

# 17. Research saturation

Araşdırma artıq əhatə edir:

- terminal;
- tactical hacking;
- broad digital investigation;
- focused operator;
- surveillance;
- desktop detective;
- personal phone;
- strong vs weak franchise outcome.

Son oyunlarda:
- yeni fundamental problem çıxmaqdan çox əvvəlki pattern-lər təkrar təsdiqlənib.

### Qərar

> **Əlavə full Tier B araşdırma default olaraq lazım deyil.**

Yeni reference:
- yalnız konkret concept yaradıldıqdan sonra;
- həmin concept üçün dəlil boşluğu yaranarsa

focused şəkildə əlavə edilməlidir.

---

# 18. Tövsiyə edilən növbəti product-discovery addımları

Research mərhələsi burada bağlanır.

Növbəti mərhələ:

## Addım 1 — Opportunity-lərdən concept variants yarat

Hələ “bir idea seçmək” yox.

Məsələn fərqli axis:
- professional operator;
- personal device;
- surveillance;
- social engineering;
- tactical pressure.

---

## Addım 2 — Hər concept üçün one-line fantasy yaz

Əgər 1 cümlədə aydın deyilsə:
- idea ya həddindən artıq genişdir;
- ya core role hələ tapılmayıb.

---

## Addım 3 — Evaluation framework ilə score et

Weighted score:
- discussion language-dir;
- avtomatik winner deyil.

---

## Addım 4 — 2–3 fərqli concept seç

Eyni idea-nın kosmetik variantları yox.

Fərqli:
- role;
- core loop;
- information model

olan variantlar.

---

## Addım 5 — Cheapest falsification prototype

Hər concept üçün:
> “bunu uğursuz edə biləcək ən böyük hipotezi ən ucuz necə test edə bilərik?”

---

## Addım 6 — Target audience test

İlk test:
- UI polish yox;
- role;
- reasoning;
- consequence.

---

## Addım 7 — Yalnız sonra production scope

Full fake OS;
FMV;
large content;
procedural systems

sonra.

---

# 19. Research nəticələrindən yaranan ilkin məhsul constraint-ləri

Yeni concept aşağıdakıları həll etməlidir:

### Must
- aydın role fantasy;
- self-directed reasoning;
- system-recognized knowledge;
- visible consequence;
- strong external memory;
- consistent interface behavior.

### Strongly preferred
- multiple solution route;
- player-built knowledge graph;
- social/character information gameplay;
- reusable mechanic grammar;
- theme-interface alignment.

### Avoid
- exact clue;
- exact evidence;
- answer-giving guide;
- single-use feature sprawl;
- cosmetic choice;
- hidden long-term punishment;
- weak replay/recovery;
- market overpromise.

---

# 20. Methodology və limitations

## Review bias

Steam review yazanlar bütün oyunçuların representative sample-ı deyil.

---

## Playtime correlation

Uzun oynayanların daha müsbət olması:
- uzun oynamağın oyunu sevdirməsini sübut etmir.

Əks istiqamət mümkündür:
- oyunu sevən daha uzun oynayır.

---

## Sales visibility

Bir çox indie oyun üçün verified sales yoxdur.

Buna görə:
- review volume;
- sentiment;
- sequel/expansion;
- publisher/developer statement

proxy kimi istifadə olunub.

---

## Store filters

Steam:
- English;
- all languages;
- purchasers;
- all review types

fərqli count verir.

Research dataset və current store count eyni səth deyil.

---

## Causality

Review theme ilə negative recommendation correlation:
- həmin mechanic-in tək causal səbəb olduğunu sübut etmir.

Interpretasiya:
- semantic audit;
- comparison;
- external context

ilə birlikdə verilib.

---

## Scope

Bu research:
- interface-heavy single-player digital investigation

üçün güclüdür.

Aşağıdakılar ayrıca study tələb edə bilər:
- multiplayer social deduction;
- real-time PvP hacking;
- sandbox programming simulators;
- mobile-only F2P;
- ARG/live-service.

---

# 21. Final qərar

Araşdırma nəticəsində “hazır oyun ideyası” seçilməyib.

Bu məqsədli qərardır.

Research-in yekun məhsulu:

> **idea deyil, idea yaratmaq və pis qərarı erkən görmək üçün qərar infrastrukturu**dur.

Ən güclü product opportunity:

> **oyunçunun topladığı məlumatı özünün əlaqələndirdiyi, semantic knowledge state qurduğu, bir neçə keçərli evidence yolu ilə claim yaratdığı və həmin reasoning-in dünyada görünən consequence yaratdığı interface-as-world investigation sistemi.**

Bu hypothesis:
- bazar reference-lərində tam həll olunmur;
- bir neçə oyun failure mode-u birbaşa həll edir;
- kiçik prototiplə test edilə bilir.

Research mərhələsi bundan sonra concept generation / evaluation mərhələsinə təhvil verilir.

---

# 22. Əsas repo sənədləri

## Bazar
- `analysis/final/market-landscape.md`

## Oyunlararası nəticə
- `analysis/final/genre-synthesis.md`

## Dizayn
- `analysis/final/design-principles.md`

## İmkanlar
- `analysis/final/opportunity-map.md`

## Risk
- `analysis/final/risk-register.md`

## İdea qiymətləndirmə
- `analysis/final/concept-evaluation-framework.md`

## Per-game
- `analysis/<game>/presentation-brief.md`
- `analysis/<game>/deep-research.md`
- `analysis/<game>/theme-analysis.md`

## Comparisons
- `analysis/comparisons/`

---

# 23. Xarici bazar mənbələri

Cari market snapshot 2026-10-03 tarixində yenidən yoxlanıb.

Əsas:
- Steam store pages
- Fellow Traveller Hacknet press kit
- GamesBeat Orwell sales/Season Two report

Third-party sales estimates yalnız:
- rəsmi olmayan estimate kimi;
- əsas nəticə üçün deyil

istifadə olunub.

---

# 24. Son cümlə

> **Bu janrda ən güclü məhsul oyunçuya çox məlumat göstərən məhsul deyil; oyunçuya həmin məlumatdan öz modelini qurmağa imkan verən və sonra “bəli, mən sənin nə bildiyini və niyə buna inandığını başa düşürəm” deyə bilən sistemdir.**
