# Hacknet vs Midnight Protocol vs Cyber Manhunt

## 1. Məqsəd

Bu comparison üç fərqli computer-interface design modelini müqayisə edir:

- **Hacknet** — execution/terminal depth
- **Midnight Protocol** — tactical/system depth
- **Cyber Manhunt** — information/deduction depth

Məqsəd “ən yaxşı oyunu” seçmək deyil. Məqsəd hansı depth modelinin hansı problemi həll etdiyini və hansı yeni risk yaratdığını anlamaqdır.

---

# 2. Dataset snapshot

| Metrik | Hacknet | Midnight Protocol | Cyber Manhunt |
|---|---:|---:|---:|
| Verified reviews | 11,773 | 301 | 847 |
| Positive ratio | **94.13%** | **84.05%** | **80.40%** |
| Avg positive playtime | 13.06h | 17.01h | 12.07h |
| Avg negative playtime | 4.40h | 5.59h | 6.33h |

Dataset ölçüləri çox fərqlidir. Absolute mention count-lar birbaşa müqayisə edilmir; əsasən pattern direction, relative negative concentration, cohort shape və semantic audit müqayisə olunur.

---

# 3. Early-session cohort müqayisəsi

| Playtime | Hacknet | Midnight Protocol | Cyber Manhunt |
|---|---:|---:|---:|
| 0–1h positive | 67.05% | 76.19% | **27.78%** |
| 1–3h positive | 86.59% | **62.22%** | **44.07%** |
| 3–10h positive | 95.79% | 75.95% | 80.49% |
| 10h+ positive | 98.57% | 95.51% | 90.72% |

Üç oyun üç fərqli onboarding problemi göstərir.

## Hacknet

Əsas risk ilk saatdır.

Player:
- terminaldan qorxa bilər;
- command vocabulary-ni anlamaya bilər;
- fantasy-ni dərhal qəbul etməyə bilər.

## Midnight Protocol

Əsas risk 1–3 saatdır.

Player initial controls-u başa düşür, amma sonra:
- loadout;
- trace;
- tactical systems;
- uncertainty;
- recovery

birlikdə friction yaradır.

## Cyber Manhunt

Ən sərt risk ilk 3 saatdır.

Player investigation gözləyir, amma early experience:
- scripted progression;
- clue-order dependency;
- localization;
- UI;
- sadə/repetitive search loop

ilə expectation mismatch yarada bilir.

### Cross-game principle

> **Onboarding yalnız controls öyrətmək deyil. Player-in oyunun “necə düşünülməli olduğunu” öyrəndiyi mərhələ ayrıca dizayn edilməlidir.**

---

# 4. Üç fərqli depth modeli

## 4.1. Hacknet — Execution Depth

Player skill əsasən:
- command flow;
- speed;
- terminal familiarity;
- basic exploration

üzərindədir.

Üstünlük:
- fantasy payoff sürətlidir;
- qaydalar sadədir;
- “hacker kimi hiss etmək” tez yaranır.

Risk:
- decision space tez görünür;
- tool-lar “key”ə çevrilir;
- eyni command sequence repetition yaradır.

---

## 4.2. Midnight Protocol — Tactical/System Depth

Player skill:
- planning;
- loadout;
- resource allocation;
- route;
- action economy;
- consequence

üzərindədir.

Üstünlük:
- Hacknet-dən daha çox meaningful choice;
- build identity;
- moral/reputation layer;
- daha çox tactical mastery.

Risk:
- complexity;
- opaque failure;
- RNG/fairness;
- retry/recovery friction;
- keyboard overhead.

---

## 4.3. Cyber Manhunt — Information/Deduction Depth

Player skill ideal halda:
- search;
- clue interpretation;
- relationship inference;
- hypothesis;
- reasoning

üzərində olmalıdır.

Üstünlük:
- technical complexity azdır;
- information özü reward olur;
- story və gameplay eyni materialdan qurulur;
- real-world relevance güclüdür.

Risk:
- player özü infer etmirsə gameplay checklist-ə çevrilir;
- scripted triggers knowledge state-i tanımır;
- search exact routing olur;
- clue collection UI hunt-a çevrilir.

---

# 5. Repetition — üçündə də eyni fundamental problem

Repetition forması dəyişir.

## Hacknet

```text
command sequence
→ port/tool
→ access
→ repeat
```

## Midnight Protocol

```text
move
→ deal with obstacle
→ manage pressure/resources
→ end turn
→ repeat
```

## Cyber Manhunt

```text
search
→ profile/data
→ clue
→ next person/account
→ repeat
```

### Genre-level hypothesis

> **Repetition interface-dən gəlmir. Oyunçunun verdiyi qərarın strukturu dəyişməyəndə yaranır.**

Bu artıq üç fərqli mechanic modelində təkrarlanır.

**Confidence: High**

---

# 6. “More Depth” problemi

Araşdırma göstərir ki, sadə cavab:

> “daha çox mechanic əlavə et”

deyil.

Hacknet-də az system depth repetition yaradır.

Midnight Protocol-da çox system interaction:
- learning cost;
- failure opacity;
- fairness risk

yaradır.

Cyber Manhunt-da information miqdarı çox ola bilər, amma player-in inference freedom-u azdırsa real deduction depth yaranmır.

### Principle

> **Depth feature sayına yox, meaningful decision density-yə görə ölçülməlidir.**

Yaxşı qərar:
- fərqli nəticələr yaradır;
- player onu anlayır;
- əvvəlki məlumatdan istifadə edir;
- future state-i dəyişir;
- bir neçə mümkün approach içindən seçilir.

---

# 7. Realism və Authenticity

Üç oyunda da eyni nəticə güclənir.

## Hacknet

Full technical realism yoxdur, amma terminal vocabulary authenticity yaradır.

## Midnight Protocol

Developer açıq şəkildə fun-first abstraction seçib.

## Cyber Manhunt

Real social/privacy patterns və human behavior authenticity yaradır.

### Cross-game principle

> **Full simulation vacib deyil. Selective authenticity və coherent cause/effect daha vacibdir.**

Risk isə budur:

> interface nə qədər real sistemə oxşayırsa, həmin sistemin real behavior expectation-u bir o qədər artır.

---

# 8. Story-nin rolu

Üç oyunda story optional ornament deyil.

## Hacknet

Story simple loop-a context və mystery verir.

## Midnight Protocol

Story tactical systems və moral choices-a meaning verir.

## Cyber Manhunt

Story investigation data-sının özüdür.

### Principle

> **Computer-interface oyunlarında narrative delivery ilə gameplay data mümkün qədər eyni materialdan qurulanda immersion artır.**

Email, logs, profiles, messages və files:
- lore;
- clue;
- objective;
- consequence

funksiyalarını eyni anda daşıya bilər.

---

# 9. Player Agency

## Hacknet

Əsasən linear və scripted.

Player agency daha çox:
- exploration;
- optional files;
- execution style

səviyyəsindədir.

## Midnight Protocol

Ən güclü agency modeli:
- loadout;
- moral direction;
- reputation;
- branch;
- mission outcome.

## Cyber Manhunt

High-level story choice var, amma micro-level investigation bəzən həddindən artıq scripted-dir.

### Əsas lesson

Agency iki səviyyədə ölçülməlidir:

1. **strategic agency** — hansı nəticəni istəyirəm?
2. **procedural agency** — ora necə çatıram?

Midnight Protocol birincidə güclüdür.

Cyber Manhunt-un əsas opportunity-si ikincidədir.

---

# 10. Failure və Recovery

## Hacknet

Failure çox vaxt explainable:
- speed;
- timing;
- execution.

## Midnight Protocol

Failure bəzən:
- uncertainty;
- randomness;
- wrong preparation

ilə bağlıdır və retry cost problemi böyüdür.

## Cyber Manhunt

Failure çox vaxt “combat failure” deyil.

Əsas failure:
- stuck olmaq;
- doğru clue-u sistemin qəbul etməməsi;
- puzzle instruction-u başa düşməmək;
- timer;
- UI state.

### Principle

> **Failure player-a nəyi səhv düşündüyünü öyrətməlidir.**

Investigation game üçün “stuck state” əsl failure state-dir.

---

# 11. UI-nin rolu

Üç oyunda UI fərqli funksiya daşıyır.

## Hacknet

UI = fantasy surface.

## Midnight Protocol

UI = command/tactical control surface.

## Cyber Manhunt

UI = external working memory.

Bu üçüncü model çox vacibdir.

Investigation UI:
- facts;
- sources;
- people;
- relationships;
- history;
- contradictions

idarə edir.

### Principle

> **Information-heavy oyunda UI complexity player cognitive load-un bir hissəsidir.**

---

# 12. Ən güclü elementlərin kombinasiyası

Araşdırmadan hazırda ən dəyərli üç komponent görünür.

## Hacknet-dən

- immediate fantasy;
- organic snooping;
- interface immersion;
- memorable rule-breaking moments.

## Midnight Protocol-dan

- meaningful preparation;
- player identity;
- consequence;
- tactical choice.

## Cyber Manhunt-dan

- information graph;
- human/social layer;
- evidence-based discovery;
- real-world relevance.

Bunları sadəcə feature stack etmək düzgün deyil.

Əsas sual:

> **Bir dominant core loop daxilində bunların hansı minimum kombinasiyası ən yüksək decision density yaradır?**

---

# 13. Gələcək concept üçün hazırkı istiqamət hipotezi

Hələ final idea deyil.

Hazır evidence belə bir design territory-ni maraqlı göstərir:

> **Accessible digital-investigation fantasy with systemic information discovery and meaningful consequence.**

Yəni:

- Hacknet qədər tez başa düşülən;
- Midnight Protocol qədər mənalı qərar verən;
- Cyber Manhunt qədər information-driven;
- amma hər üçünün əsas friction-lərindən qaçan.

Potential core:

```text
discover
→ connect
→ hypothesize
→ choose action
→ consequence
→ changed information space
```

Bu “hack → next mission”dan daha sistemik ola bilər.

---

# 14. Transferable Principles

## Principle 1 — Fantasy first

Player özünü kim kimi hiss edir?

## Principle 2 — Depth = meaningful decisions

Feature sayı metric deyil.

## Principle 3 — Player knowledge real state olmalıdır

Investigation sistemləri exact trigger-dən asılı qalmamalıdır.

## Principle 4 — Multiple routes repetition-ı azaldır

Eyni objective bir neçə approach ilə həll oluna bilməlidir.

## Principle 5 — Failure explainable olmalıdır

Randomness və opaque triggers mastery-ni öldürür.

## Principle 6 — UI player cognition-un extension-ıdır

Information-heavy design-də xüsusilə.

## Principle 7 — Story gameplay data-sında yaşamalıdır

Separate exposition minimum olmalıdır.

## Principle 8 — Selective authenticity kifayətdir

Full realism tələb deyil.

## Principle 9 — Consequence identity yaradır

Action future state-i dəyişməlidir.

## Principle 10 — Early-session real victory lazımdır

İlk 30–60 dəqiqədə player öz inference/skill-i ilə meaningful nəticə əldə etməlidir.

---

# 15. Risk Register

| Risk | Hacknet | Midnight Protocol | Cyber Manhunt |
|---|---|---|---|
| Repetition | High | High | High |
| Syntax/UI friction | Medium | High | Medium-High |
| Complexity cliff | Low-Medium | High | Medium |
| Opaque failure | Low | High | High |
| Weak procedural agency | High | Medium | High |
| Weak strategic agency | High | Lower | Medium |
| Story dependency | High | High | High |
| Localization sensitivity | Medium | Medium | **Very High** |
| Technical instability | High review impact | Medium | Medium |
| Player knowledge not recognized | Low | Medium | **High** |

---

# 16. Opportunity Map

| Opportunity | Evidence |
|---|---|
| Systemic information graph | Cyber Manhunt clue/search friction |
| Meaningful consequence | Midnight Protocol choice/reputation |
| Organic exploration | Hacknet snooping/discovery |
| Explainable deterministic challenge | Midnight RNG/fairness issue |
| Multiple evidence routes | Cyber Manhunt linearity issue |
| Hybrid low-friction interface | Hacknet/MP input friction |
| Strong evidence workspace | Cyber Manhunt UI load |
| Returning-player support | Hacknet command memory + complex investigation context |
| Memorable system-breaking moments | Hacknet və Midnight positive recall |

---

# 17. Növbəti research sualı

Bu üç oyun artıq hacking/interface design-in üç əsas depth istiqamətini göstərir.

Növbəti mərhələ üçün ən informasiya dəyərli oyunlar:

- **The Operator** — modern digital investigation və evidence workflow;
- **Mainlining** — hacking + investigation + choice;
- **Orwell** — information selection + ethics + surveillance.

Əsas sual:

> **Cyber Manhunt-un scripted investigation problemini başqa digital-investigation oyunları necə həll edir?**

Bu cavabdan sonra genre-level principles daha etibarlı şəkildə formalaşdırıla bilər.

---

# 18. Mənbələr

## Hacknet
- `analysis/hacknet/deep-research.md`
- `analysis/hacknet/theme-analysis.md`

## Midnight Protocol
- `analysis/midnight-protocol/deep-research.md`
- `analysis/midnight-protocol/theme-analysis.md`
- `analysis/comparisons/hacknet-vs-midnight-protocol.md`

## Cyber Manhunt
- `analysis/cyber-manhunt/deep-research.md`
- `analysis/cyber-manhunt/theme-analysis.md`

# Status

**Comparison:** tamamlanıb  
**Games:** Hacknet + Midnight Protocol + Cyber Manhunt  
**Növbəti:** digital-investigation reference ilə scripted-vs-systemic investigation hipotezini test etmək.
