# Orwell: Keeping an Eye On You — Research Kickoff

## Status

Bu sənəd Orwell dataset-dən əvvəl hazırlanmış kickoff sənədidir və historical planning context kimi saxlanılır.

Research artıq tamamlanıb. Cari source of truth:

- `analysis/orwell/deep-research.md`
- `analysis/orwell/theme-analysis.md`

Need to Know focused comparator ayrıca növbəti mərhələdir.

## Niyə növbəti Tier A target budur?

Hacknet, Midnight Protocol, Cyber Manhunt və The Operator birlikdə artıq üç əsas depth modelini göstərdi:

- execution/terminal depth;
- tactical/system depth;
- information/deduction depth.

Orwell növbəti vacib sualı test edir:

> **Investigation depth yalnız məlumatı tapmaqdan yox, hansı məlumatı sistemə vermək və onun consequence-nı qəbul etməkdən yarana bilərmi?**

Bu surveillance/information-selection xəttidir.

## Product snapshot

Steam App ID: **491950**

- Name: Orwell: Keeping an Eye On You
- Developer: Osmotic Studios
- Publisher: Daedalic Entertainment
- Release: 27 October 2016
- Single-player
- Store positioning: investigation, surveillance, choices/consequences, dystopian narrative.
- Current public Steam English review display: təxminən **90% positive**.

Official premise:

Player governmental security system daxilində citizen-lərin public və private digital data-sını araşdırır. Vacib design twist budur ki, bütün tapılan məlumat avtomatik istifadə edilmir; player hansı information-un security forces-a ötürüləcəyinə qərar verir və bu seçimlərin nəticələri olur.

## Niyə research üçün dəyərlidir?

Cyber Manhunt və The Operator əsasən:

> “Doğru məlumatı tapa bilirəmmi?”

sualına fokuslanır.

Orwell isə əlavə edir:

> **“Tapdığım məlumatdan hansını təqdim etməliyəm?”**

Bu information selection-ı gameplay decision-a çevirir.

Beləliklə investigation loop:

information discovery → interpretation → selection → consequence

modelinə keçir.

## Əsas research sualları

1. Information selection real player agency yaradırmı?
2. Player bir data point-in context-dən çıxarıla biləcəyini hiss edirmi?
3. Contradictory information necə idarə olunur?
4. Consequence kifayət qədər görünəndirmi?
5. Ethical tension gameplay-dən doğur, yoxsa yalnız narrative mesaj kimi qalır?
6. Player information-u gizlətmək və ya ötürmək arasında meaningful trade-off görürmü?
7. Search/research hissəsi Cyber Manhunt qədər scripted görünürmü?
8. Evidence interface player knowledge-i yaxşı idarə edirmi?
9. Reading load nə qədər yüksəkdir?
10. Repetition information-selection loop-da necə yaranır?
11. Choice-lar ending və character outcomes-a real təsir edirmi?
12. Game player-a “correct moral answer” diktə edir, yoxsa ambiguity saxlayır?

## Cyber Manhunt / The Operator ilə ilkin contrast

Cyber Manhunt:
- geniş information gathering;
- sərt clue/progression riski.

The Operator:
- focused evidence;
- yüksək clarity;
- weak procedural/narrative agency riski.

Orwell üçün əsas test:

> focused data selection + consequence player-a daha çox real agency verirmi?

## Yeni aspect ehtimalları

Dataset tələb edərsə aşağıdakı aspect-lər ayrıca genişləndirilə bilər:

- INFORMATION_SELECTION
- CONTEXT_AMBIGUITY
- PRIVACY_SURVEILLANCE
- CONSEQUENCE_VISIBILITY
- CONTRADICTORY_EVIDENCE
- READING_LOAD
- MORAL_AMBIGUITY

Bunlar review sample audit-dən əvvəl final taxonomy-yə əlavə edilməməlidir.

## Public source

Steam Store:  
https://store.steampowered.com/app/491950/

## Növbəti addım

Config repository-yə əlavə olunub:

    key: orwell
    name: Orwell: Keeping an Eye On You
    steam_app_id: 491950

Verified dataset sonradan toplanıb: **8,549 review**. Kickoff hipotezləri final research-də test edilib və bu sənəd artıq source of truth deyil.
