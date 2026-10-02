# İmkan xəritəsi — Digital investigation / interface-as-world

## 1. Məqsəd

Bu sənəd araşdırmadan çıxan “həll olunmamış məhsul imkanlarını” xəritələndirir.

Bu:
- hazır oyun ideyaları siyahısı deyil;
- concept pitch deyil;
- feature backlog deyil.

Məqsəd:

> **Bazarda və araşdırılmış reference-lərdə hansı vacib oyunçu ehtiyaclarının tam həll olunmadığını göstərməkdir.**

---

# 2. İmkan xəritəsinin əsas oxları

İmkanlar beş sahədə qruplaşdırılır:

1. **Reasoning / knowledge**
2. **Agency / consequence**
3. **Interface / immersion**
4. **Human / social investigation**
5. **Replay / accessibility / usability**

---

# 3. O1 — Semantic investigation engine

## Problem

Bir çox oyunda:

```text
oyunçu fact-i bilir
≠
sistem bunu tanıyır
```

Görülüb:
- Cyber Manhunt
- Mainlining
- Need to Know
- SIMULACRA
- SIMULACRA 3

## İmkan

Progression:
- exact file;
- exact click;
- exact dialogue

deyil,

> **semantic fact state**

üzərindən işləyə bilər.

### Məsələn

```text
FACT:
Person X was at Location Y.

VALID SUPPORT:
- CCTV
- receipt
- chat
- GPS
```

## Dəyər

- alternative routes;
- stronger agency;
- less trial-and-error;
- more replayability;
- better failure feedback.

## Risk

Semantic system texniki baxımdan çətindir və yanlış positive acceptance yarada bilər.

## Prioritet

**Çox yüksək**

---

# 4. O2 — Player-built knowledge graph

## Problem

Current games iki ekstrem arasında qalır:

### Heç bir organization yoxdur
- player external notes istifadə edir.

### System hər şeyi özü əlaqələndirir
- observation/deduction azalır.

## İmkan

Graph:
- entity;
- fact;
- source;
- time;
- place;
- relationship

saxlasın.

Amma link-i:
> player yaratsın.

## Dəyər

- external memory;
- visible reasoning;
- satisfying “case board”;
- semantic submission.

## Risk

UI complexity.

## Prioritet

**Çox yüksək**

---

# 5. O3 — Claim + evidence gameplay

## Problem

Current games:
- “suspect seç”;
- “file seç”;
- “datachunk ötür”

modelində qalır.

## İmkan

Oyunçu:

```text
claim
→ evidence set
→ confidence
→ action
```

qurur.

## Dəyər

- reasoning explicit olur;
- partial correctness mümkündür;
- feedback daha yaxşı olur;
- multiple valid solution support edilir.

## Prioritet

**Çox yüksək**

---

# 6. O4 — Multi-route fact discovery

## Problem

Bir çox investigation oyunu özünü open investigation kimi təqdim edir, amma:
- critical clue üçün bir route var.

## İmkan

Major fact-lar:
- technical;
- social;
- visual;
- documentary

route-lardan biri ilə tapıla bilər.

## Dəyər

- agency;
- replay;
- player identity;
- “özüm tapdım” hissi.

## Risk

Content production cost.

## Prioritet

**Yüksək**

---

# 7. O5 — Social information as gameplay resource

## Problem

Personaj data-sı tez-tez:
- lore;
- password clue

olaraq qalır.

## İmkan

Personal detail:
- trust;
- bluff;
- threat;
- empathy;
- contradiction;
- reputation;
- social engineering

üçün işləsin.

## Dəyər

Human story və system depth eyni layer-də birləşir.

## Reference siqnalları
- Cyber Manhunt
- SIMULACRA
- Orwell

## Prioritet

**Yüksək**

---

# 8. O6 — Consequence web

## Problem

Choices:
- cosmetic;
- hidden ending score;
- one-off fail

ola bilir.

## İmkan

Decision:
- relationship;
- source availability;
- future evidence;
- trust;
- public/system state

dəyişsin.

### Model

```text
choice
→ local reaction
→ information space changes
→ later consequence
```

## Dəyər

Agency real hiss olunur.

## Prioritet

**Çox yüksək**

---

# 9. O7 — Investigation through changing information space

## Problem

Əksər oyunlarda məlumat bazası statikdir:
- player sadəcə onu açır.

## İmkan

Player action-dan sonra:
- message silinir;
- source yalan məlumat verir;
- account bağlanır;
- personaj davranışı dəyişir;
- new leak çıxır;
- public narrative dəyişir.

## Dəyər

World reactivity və urgency artır.

## Risk

State explosion.

## Prioritet

**Yüksək**

---

# 10. O8 — Interface-native threat

## Problem

Pressure:
- timer;
- random jumpscare;
- arbitrary trace meter

kimi ayrıca layer olur.

## İmkan

Threat interface davranışından çıxsın.

Məsələn:
- remote access detected;
- files mutate;
- account revoked;
- messages altered;
- source compromised;
- system becomes unreliable.

## Dəyər

Theme + mechanics cohesion.

## References
- SIMULACRA 1-in güclü anları;
- Hacknet trace fantasy;
- SIMULACRA 3 house set-piece.

## Prioritet

**Yüksək**

---

# 11. O9 — Persistent investigation workspace

## Problem

Player:
- çox fact;
- çox source;
- çox tarix

saxlamalıdır.

## İmkan

Native workspace:
- notes;
- pins;
- history;
- timeline;
- source bookmarks;
- search recall.

## Dəyər

Cognitive load:
> memory-dən reasoning-ə keçir.

## Guardrail

Auto-solve etmə.

## Prioritet

**Çox yüksək**

---

# 12. O10 — Productive noise system

## Problem

Investigation content ya:
- çox curated,
ya da:
- həddindən artıq cluttered.

## İmkan

Believable noise:
- irrelevant personal data;
- side threads;
- dead ends;
- optional context.

Amma:
- organization;
- search;
- recall tools

güclü olsun.

## Dəyər

Relevance discovery real olur.

## Prioritet

**Orta-Yüksək**

---

# 13. O11 — Adaptive guidance without answer leakage

## Problem

Players ya:
- ilişib qalır,
ya da:
- guide NPC cavabı deyir.

## İmkan

Hint ladder:

1. tool reminder;
2. missing category;
3. source direction;
4. relation hint;
5. near-answer hint.

Oyunçu özü seçsin:
- nə qədər yardım istəyir.

## Dəyər

Broad audience + preserved agency.

## Prioritet

**Yüksək**

---

# 14. O12 — Role-specific interface modes

## Problem

Bir interface bütün playstyle-ları eyni edir.

## İmkan

Same case, different competence route:

- analyst;
- social engineer;
- technical operator;
- field coordinator.

Bu class system olmaq məcburiyyətində deyil.

Player behavior:
> hansı tools və routes daha rahatdır?

deyə fərqlənə bilər.

## Dəyər

Replay + identity.

## Risk

Scope explosion.

## Prioritet

**Orta**

---

# 15. O13 — Explainable failure

## Problem

“Wrong” yalnız fail-dir.

## İmkan

System:
- identity weak;
- timeline conflict;
- evidence insufficient;
- source unreliable

kimi feedback verir.

## Dəyər

Failure learning olur.

## Prioritet

**Yüksək**

---

# 16. O14 — Branch replay / selective rollback

## Problem

Narrative investigation-da replay cost yüksəkdir.

## İmkan

Completed run-dan sonra:
- branch map;
- chapter replay;
- dialogue fast-forward;
- evidence-state checkpoint.

## Dəyər

Multiple ending həqiqətən istifadə olunur.

## Prioritet

**Orta-Yüksək**

---

# 17. O15 — Dynamic social trust

## Problem

Relationship çox vaxt:
- hidden score

olur.

## İmkan

Trust:
- hansı məlumatı verdin;
- hansı sirri saxladın;
- nəyi sübut etdin;
- necə davrandın

əsasında observable behavior kimi dəyişsin.

## Dəyər

Choice consequence daha legible olur.

## Prioritet

**Yüksək**

---

# 18. O16 — Contradiction-first investigation

## Problem

Games çox vaxt:
- clue collection

üzərindədir.

## İmkan

Core verb:

> **iki məlumatın niyə uyğun gəlmədiyini tap.**

Məsələn:
- alibi vs GPS;
- public post vs private message;
- official record vs photo.

## Dəyər

Reasoning daha explicit olur.

## References
- Orwell contradiction potential;
- Cyber Manhunt relationship data;
- Mainlining evidence logic.

## Prioritet

**Yüksək**

---

# 19. O17 — Confidence, uncertainty və source reliability

## Problem

Clue çox vaxt binary:
- var / yoxdur;
- doğru / yanlış.

## İmkan

Source-lar:
- reliable;
- biased;
- incomplete;
- manipulated

ola bilər.

Player:
> certainty qurur.

## Dəyər

Moral və investigative ambiguity sistemləşir.

## Risk

Over-complexity.

## Prioritet

**Orta-Yüksək**

---

# 20. O18 — Character intimacy + broad case scope

## Problem

SIMULACRA 3 göstərir:
- breadth intimacy-ni yeyə bilər.

## İmkan

Wide case olsa belə hər chapter:
- bir human anchor;
- rich personal archive;
- recurring relationship

saxlasın.

## Dəyər

World scale + emotional stake.

## Prioritet

**Yüksək**

---

# 21. O19 — Mastery-driven mechanic variety

## Problem

The Operator / SIMULACRA 3:
- çox single-use mechanic.

## İmkan

Az sayda core mechanic:
- yeni vəziyyətlərdə;
- kombinasiya ilə;
- artan complexity-də

qayıtsın.

## Dəyər

Novelty + mastery birlikdə.

## Prioritet

**Yüksək**

---

# 22. O20 — Store-promise validation

## Problem

Marketing/gameplay mismatch review penalty yaradır.

## İmkan

Concept development zamanı:
- store capsule mock;
- short trailer storyboard;
- 3-sentence description

test edilir.

Sonra actual prototype ilə:
> dominant expected verb == dominant actual verb?

yoxlanılır.

## Prioritet

**Yüksək**

---

# 23. Ən güclü kombinasiya imkanları

## Kombinasiya A — Knowledge-first investigator

```text
rich sources
→ self-directed relevance
→ player-built graph
→ claim + evidence
→ consequence
```

Əsas reference:
- Cyber Manhunt
- Mainlining
- Orwell

---

## Kombinasiya B — Personal device + semantic investigation

```text
believable personal device
→ intimate data
→ multiple contacts
→ semantic fact state
→ social action
→ device/world reaction
```

Əsas reference:
- SIMULACRA
- SIMULACRA 3 Atlas opportunity

---

## Kombinasiya C — Operator + branching consequence

```text
focused professional tools
→ clear objective
→ multiple valid interpretations
→ field action
→ visible consequence
```

Əsas reference:
- The Operator
- Orwell

---

## Kombinasiya D — Tactical information pressure

```text
investigation
→ incomplete information
→ preparation choice
→ timed/turn pressure
→ recoverable failure
```

Əsas reference:
- Midnight Protocol
- Hacknet pressure fantasy

---

# 24. İmkanların prioritet matrisi

| İmkan | Oyunçu dəyəri | Fərqlənmə | Texniki risk | Prioritet |
|---|---|---|---|---|
| Semantic knowledge state | Çox yüksək | Çox yüksək | Yüksək | **A** |
| Player-built knowledge graph | Çox yüksək | Yüksək | Orta-Yüksək | **A** |
| Claim + evidence | Çox yüksək | Yüksək | Orta | **A** |
| Consequence web | Çox yüksək | Yüksək | Yüksək | **A** |
| Multi-route solving | Yüksək | Yüksək | Yüksək | **A** |
| Persistent workspace | Yüksək | Orta | Orta | **A** |
| Social evidence/leverage | Yüksək | Yüksək | Orta-Yüksək | **A** |
| Interface-native threat | Yüksək | Yüksək | Orta | **A/B** |
| Adaptive hints | Yüksək | Orta | Orta | **B** |
| Source confidence | Orta-Yüksək | Yüksək | Yüksək | **B** |
| Role-specific routes | Orta-Yüksək | Yüksək | Çox yüksək | **B/C** |

---

# 25. Hansı imkanlar birlikdə prototiplənməlidir?

İlk vertical prototype üçün ən güclü dəst:

1. semantic fact state;
2. 2–3 source type;
3. player-built notes/graph;
4. claim + evidence submission;
5. ən azı 2 valid solution route;
6. immediate visible consequence.

Bu prototip:
- böyük hekayə;
- çox app;
- FMV;
- combat;
- çox personaj

olmadan da əsas janr opportunity-ni test edə bilər.

---

# 26. Hansı imkanlar əvvəl prototiplənməməlidir?

İlk prototipdə risklidir:

- böyük open internet;
- 20+ tools;
- procedural content;
- çox branch;
- complex reputation;
- full fake OS;
- böyük town;
- çox FMV.

Bunlar semantic investigation loop işlədikdən sonra əlavə edilməlidir.

---

# 27. Əsas məhsul hipotezi

Research-in ən güclü opportunity hipotezi:

> **Bazarda bir çox oyun information collection verir, amma oyunçunun öz qurduğu knowledge modelini semantic şəkildə qəbul edən, bir neçə məntiqli həll yoluna imkan verən və həmin reasoning-in dünyada görünən nəticə yaratdığı sistem az görünür.**

Bu yeni concept yaratmaq üçün ən güclü araşdırma boşluqlarından biridir.

Bu hələ concept deyil.

---

# 28. Yekun

Ən böyük imkan:
> daha çox hacking realism və ya daha çox apps deyil.

Ən böyük imkan:

> **oyunçunun öz reasoning-ni birinci dərəcəli gameplay object-ə çevirməkdir.**

Yəni:
- nə bildin;
- niyə buna inanırsan;
- hansı source-a əsaslanırsan;
- bununla nə edirsən;
- dünya necə dəyişir

sistemin özündə görünməlidir.

Bu sənəd:
- `genre-synthesis.md`
- `design-principles.md`
- `risk-register.md`

ilə birlikdə concept-evaluation mərhələsinin əsas input-udur.
