# Cyber Manhunt — Research Kickoff

## Status

Bu sənəd Cyber Manhunt dataset-dən əvvəl hazırlanmış kickoff sənədidir və historical planning context kimi saxlanılır.

Research artıq tamamlanıb. Cari nəticələr üçün:

- `analysis/cyber-manhunt/deep-research.md`
- `analysis/cyber-manhunt/theme-analysis.md`
- `analysis/comparisons/hacknet-midnight-protocol-cyber-manhunt.md`

istifadə olunmalıdır.

---

# 1. Niyə Cyber Manhunt növbəti oyundur?

Hacknet və Midnight Protocol əsasən **hacking fantasy + computer-interface interaction** xəttini araşdırdı.

Cyber Manhunt research-i başqa vacib istiqamətə keçirir:

> **digital investigation + social engineering + information discovery + privacy/consequence**

Bu çox vacib keçiddir.

Hazır iki oyundan çıxan əsas opportunity:

```text
Hacknet:
organic discovery güclü
but agency/consequence zəif

Midnight Protocol:
agency/consequence güclü
but tactical friction/RNG yüksək
```

Cyber Manhunt aşağıdakı sualı test etməyə imkan verir:

> **Dərinliyi command və tactical combat-dan yox, məlumat toplamaq, əlaqələndirmək, social engineering və deduction-dan yaratmaq daha yaxşı işləyə bilərmi?**

---

# 2. Product snapshot

Steam App ID: **1216710**

- Name: Cyber Manhunt
- Developer: Aluba Van+ / əvvəl Aluba Studio
- Publisher: 摸鱼游戏, Aluba Van+
- Early Access: August 2020
- Full release: 2 February 2021
- Base US price: $9.99
- Current Steam English review display: təxminən **816 review, 80% positive**
- Recent review display: təxminən **76% positive**
- Single-player
- Demo available
- DLC content mövcuddur

Steam tags:

- Puzzle
- Hacking
- Mystery
- Detective
- Story Rich
- Investigation
- Crime
- Immersive Sim
- Psychological Horror
- Linear

Bu dəfə “hacking” store identity-nin yalnız bir hissəsidir.

Dominant player activity daha çox:

> **information investigation**

kimi görünür.

---

# 3. Official positioning

Steam oyunu belə təsvir edir:

> story-oriented puzzle game focusing on big data, hacking, citizen privacy, and social problems.

Core systems arasında rəsmi səhifə bunları göstərir:

- picture analysis;
- phishing;
- information search;
- tracking;
- puzzle solving;
- hacking;
- social engineering;
- story decisions.

Bu research üçün vacibdir, çünki player interaction yalnız “server-i aç” deyil.

Loop daha çox belə görünür:

```text
target haqqında az məlumat
→ internet/profile search
→ clue tap
→ identity/data əlaqələndir
→ password/contact/address çıxar
→ phishing/social engineering
→ cihaz/account access
→ daha şəxsi data
→ story nəticəsi
```

Bu, bizim axtardığımız **information → access → information** circular loop-a çox yaxındır.

---

# 4. Developer intent

Official Steam description və developer materiallarında bir neçə güclü məqsəd görünür.

## 4.1. Real sosial problemlər

Game theme:

- big data;
- privacy loss;
- cyber violence;
- doxxing / personal information exposure;
- online judgment;
- social engineering.

Developer yalnız “cool hacking” fantasy yaratmaq istəməyib.

Məqsəd həm də:

> oyunçunun real internet davranışı və privacy haqqında düşünməsi

olub.

Bu Hacknet və Midnight Protocol-dan fərqlidir.

---

## 4.2. Real hadisələrdən inspiration

Developer bir çox plot-un real social events-dən ilham aldığını yazır.

Bu narrative-in:

- relatability;
- discomfort;
- ethical tension

yaratmasına xidmət edir.

---

## 4.3. Social engineering core design-dir

Developer komandası:

- security/hacking mütəxəssislərindən məlumat topladığını;
- ayrıca social-engineering discussion group qurduğunu;
- Kevin Mitnick-in *The Art of Deception* kitabını araşdırdığını

deyir.

Araşdırılan sahələr arasında:

- psychology;
- social engineering;
- phrase/communication techniques;
- information leakage

olub.

Bu çox vacib design difference-dir:

> Cyber Manhunt hacking-i yalnız software-system problemi kimi yox, **human-information problem** kimi görür.

---

# 5. Creative inspirations

Official store materialında developer aşağıdakı oyun və media təsirlərini qeyd edir:

- This War of Mine
- Papers, Please
- Orwell
- Who Am I: No System Is Safe
- Searching

Burada iki design xətti görünür.

## 5.1. Games that make player think outside the game

This War of Mine və Papers, Please:

> mechanic + ethical/social meaning

modelidir.

## 5.2. Screenlife / information storytelling

Searching:

> computer/phone details vasitəsilə story tapmaq.

Bu bizim research scope-la birbaşa üst-üstə düşür.

---

# 6. Hacknet və Midnight Protocol ilə ilkin contrast

| Mövzu | Hacknet | Midnight Protocol | Cyber Manhunt — ilkin model |
|---|---|---|---|
| Core fantasy | Hacker | Tactical hacker | Hacker / digital investigator |
| Main action | Commands + breach | Tactical network movement | Search + connect information + social engineering |
| Main depth | Story/exploration | Tactical systems | Information relationships |
| Failure risk | Repetition | RNG/friction | Linear puzzle / clue ambiguity hipotezi |
| Story | Mystery | Narrative RPG | Social thriller / case structure |
| Agency | Limited | Strong reputation/choices | Story judgment/consequence araşdırılmalıdır |
| Realism | Selective technical authenticity | Gameified tactical authenticity | Social-engineering / information authenticity |
| Interface | Terminal + OS | Keyboard-only terminal/network | Browser/database/profile/device-style tools |
| Main skill | Command execution + exploration | Planning/build | Deduction/search/inference |

Bu cədvəl dataset-dən əvvəl provisional-dır.

---

# 7. Əsas research sualları

## 7.1. Information discovery

- Oyunçu həqiqətən clue tapır, yoxsa sadəcə highlighted information-a klik edir?
- Məlumatları özü əlaqələndirir, yoxsa oyun avtomatik nəticə çıxarır?
- “Aha!” momentləri varmı?
- Investigation real deduction hissi yaradırmı?

## 7.2. Social engineering

- Phishing və human manipulation mechanic-ləri maraqlıdırmı?
- Onlar sadəcə mini-game-dir, yoxsa information loop-un hissəsidir?
- Oyunçu target haqqında öyrəndiyi məlumatı sonradan istifadə edirmi?

## 7.3. Core loop repetition

- Hər case eyni:
  search → password → hack → data
  strukturuna çevrilirmi?
- Yeni case-lər yeni reasoning tələb edir, yoxsa yalnız yeni story content?

## 7.4. Story vs gameplay

- Story gameplay-i mənalı edir?
- Yoxsa player əsasən text oxuyur və mechanic sadəcə keçid rolunu oynayır?
- Case structure pacing-i necə təsir edir?

## 7.5. Player agency

- Oyunçu həqiqətən qərar verir?
- “good/evil judgment” gameplay və story-yə nə qədər təsir edir?
- Case outcome-ları dəyişirmi?

## 7.6. Ethical tension

- Privacy-ni pozmaq oyunda sadəcə “cool hacker action” kimi görünür?
- Yoxsa oyunçu öz hərəkətinin etik tərəfini hiss edir?
- Ethical discomfort satisfaction yaradır, yoxsa preachy görünür?

## 7.7. UI/UX

- Multi-window/interface investigation rahatdırmı?
- Information overload yaranırmı?
- Notes/evidence management necə işləyir?
- Oyunçunun özü xarici note saxlamağa ehtiyac duyurmu?

## 7.8. Onboarding

- Oyun investigation grammar-ni necə öyrədir?
- Early cases tutorial kimi işləyir?
- Difficulty clue ambiguity-dənmi, mechanic complexity-dənmi gəlir?

## 7.9. Translation/writing

English dataset üçün ayrıca vacibdir:

- localization story comprehension-a təsir edirmi?
- awkward writing puzzle həllini çətinləşdirirmi?
- character dialogue və social themes nə qədər yaxşı ötürülür?

## 7.10. Recent sentiment

Steam current display-də:

- all-time English ~80%;
- recent ~76%.

Dataset toplandıqdan sonra yoxlanmalıdır:

> newer feedback-də hansı complaint-lər artıb?

---

# 8. Yeni taxonomy ehtimalları

Cyber Manhunt datası aşağıdakı yeni aspect-ləri tələb edə bilər:

```text
DEDUCTION
CLUE_QUALITY
INFORMATION_SEARCH
SOCIAL_ENGINEERING
PHISHING
EVIDENCE_MANAGEMENT
CASE_VARIETY
ETHICAL_TENSION
PRIVACY_THEME
LOCALIZATION_WRITING
PUZZLE_LOGIC
LINEARITY
```

Bunlar dataset oxunmadan final taxonomy-yə əlavə edilməməlidir.

Əvvəl sample audit aparılacaq.

---

# 9. Əsas comparison hypotheses

## Hipotez 1

> Information-based depth Hacknet/Midnight Protocol-dakı command/tactical repetition-dan daha davamlı ola bilər.

Test:

- case variety;
- investigation praise;
- repetition complaints.

## Hipotez 2

> Social engineering player-a “human system hacking” fantasy-si verir və full technical simulation-a ehtiyacı azaldır.

Test:

- social engineering praise;
- realism complaint;
- player fantasy language.

## Hipotez 3

> Deduction yalnız oyunçu özü inference edəndə satisfying olur.

Əgər game:

- clue-u tapır;
- avtomatik əlaqələndirir;
- nəticəni özü deyirsə

interaction “search checklist”ə çevrilə bilər.

## Hipotez 4

> Strong story investigation loop-un repetition-ını gizlədə bilər, amma həll etməz.

Bu Hacknet nəticəsi ilə müqayisə ediləcək.

## Hipotez 5

> Privacy və cyber-violence themes player consequence hissini artırır.

Midnight Protocol-da moral identity gameplay system vasitəsilə gəlir.

Cyber Manhunt-da bu daha çox narrative/social consequence vasitəsilə gələ bilər.

---

# 10. Dataset workflow

Config artıq repository-yə əlavə olunub:

```yaml
key: cyber-manhunt
name: Cyber Manhunt
steam_app_id: 1216710
```

Növbəti mərhələ:

```text
Steam collection
→ verification
→ basic statistics
→ helpful/recent/low/high samples
→ taxonomy discovery
→ candidate scan
→ all-negative semantic audit if dataset size allows
→ positive stratified audit
→ deep-research
→ comparison with Midnight Protocol / Hacknet
```

---

# 11. Public sources

## [W1] Steam Store

https://store.steampowered.com/app/1216710/

Rəsmi positioning, gameplay systems, themes, creative inspirations, developer/publisher/release məlumatı.

## [W2] Gamersky / developer interview — Aluba Studio

https://club.gamersky.com/activity/435462

Developer origin, team, social-engineering research, privacy theme və real-life inspiration haqqında material.

## [W3] Indienova project page

https://indienova.com/g/cyber-manhunt

Developer project description və development materialları.

---

# 12. Status

**Mərhələ:** kickoff — superseded  
**Steam target:** 1216710  
**Verified dataset:** 847 reviews  
**Current source of truth:** `analysis/cyber-manhunt/deep-research.md`
