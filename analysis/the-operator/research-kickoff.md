# The Operator — Research Kickoff

## Status

Bu sənəd The Operator dataset-dən əvvəl hazırlanmış kickoff sənədidir və historical planning context kimi saxlanılır.

Research artıq tamamlanıb. Cari nəticələr üçün:

- `analysis/the-operator/deep-research.md`
- `analysis/the-operator/theme-analysis.md`
- `analysis/comparisons/cyber-manhunt-vs-the-operator.md`

istifadə olunmalıdır.

## Niyə növbəti target budur?

Cyber Manhunt araşdırması göstərdi ki, digital-investigation oyunlarında əsas risklər:
- scripted clue order;
- player knowledge-in game state tərəfindən tanınmaması;
- weak evidence UX;
- investigation-ın checklist-ə çevrilməsi;
- story və UI-nin deduction-u əvəz etməsidir.

The Operator bu sualları test etmək üçün güclü reference-dir, çünki onun əsas fantasy-si “field agent” olmaq yox, **arxa planda məlumat analiz edən operator** olmaqdır.

## Product snapshot

Steam App ID: **1771980**

- Developer: Bureau 81
- Publisher: Bureau 81, indienova
- Release: 22 July 2024
- Single-player
- Steam English review display: təxminən **89% positive**
- Store tags: Detective, Investigation, Puzzle, Mystery, Simulation, Crime, Narrative.

Official positioning:

> player FDI operator kimi field agent-lərə kömək edir, software və database-lərdən istifadə edib clue-ları analiz edir və cinayət işlərini həll edir.

## Developer intent

Developer Bastien Giafferi The Operator-u X-Files və Her Story təsirlərinin qarışığı kimi izah edir.

Core inspiration:

> əsas agent olmaq əvəzinə “chair arxasındakı” analyst/operator rolunu oynamaq.

Game Developer müsahibəsində interface və analysis tools-un story beat-lərlə birlikdə dizayn edildiyi vurğulanır.

Bu bizim research üçün çox vacibdir, çünki Cyber Manhunt-da UI tez-tez clue tapma friction-i yaradırdı. The Operator isə UI-ni investigation sisteminin mərkəzi kimi nəzərdə tutur.

Developer ayrıca immersion üçün fictional desktop və terminal kimi secondary tools da daxil edib; terminal əvvəlcə daha böyük rol üçün nəzərdə tutulsa da final design-də əsas mechanic yox, world-completeness elementi kimi saxlanıb.

## Əsas research sualları

1. Player həqiqətən deduction edir, yoxsa story yalnız doğru tool-u seçməyə yönəldir?
2. Evidence system player-in artıq bildiyi nəticəni qəbul edirmi?
3. UI external working memory kimi Cyber Manhunt-dan daha yaxşı işləyirmi?
4. Cases player-a bir neçə valid reasoning route verir?
5. Investigation puzzle-ləri fair və explainable-dırmı?
6. Story mystery-ni gücləndirir, yoxsa autonomy-ni məhdudlaşdırır?
7. Game length və pacing repetition problemini necə idarə edir?
8. Analyst/operator fantasy hacker fantasy-dən daha geniş audience cəlb edirmi?
9. Player hansı anda “mən tapdım” hissini yaşayır?
10. Cyber Manhunt-un early-session risk pattern-i burada da görünürmü?

## İlkin comparison hipotezi

Cyber Manhunt:

```text
information discovery
→ strong fantasy
→ strict scripted progression
→ deduction friction
```

The Operator üçün test ediləcək model:

```text
specialized analysis tools
→ focused evidence comparison
→ explicit reasoning
→ potentially lower search ambiguity
```

Əgər player response bunu təsdiqləsə, vacib principle çıxacaq:

> Investigation depth üçün böyük açıq search space şərt deyil; əsas məsələ player-in evidence üzərində real inference etməsidir.

## Public sources

**Steam Store**  
https://store.steampowered.com/app/1771980/

**Game Developer — The Operator is a crime solving game delivered entirely with UI**  
https://www.gamedeveloper.com/design/the-operator-is-a-crime-solving-game-delivered-entirely-with-ui

**Gamereactor interview — Bastien Giafferi**  
https://www.gamereactor.eu/video/694403/Bureau%2B81s%2BBastien%2BGiafferi%2Bon%2Bbeing%2Bthe%2Bguy%2Bbehind%2Bthe%2Bchair%2Bin%2BThe%2BOperator/

## Növbəti addım

Config artıq əlavə olunub:

```yaml
key: the-operator
name: The Operator
steam_app_id: 1771980
```

Verified dataset sonradan toplanıb: **3,781 review**. Kickoff hipotezləri final research-də test edilib və bu sənəd artıq source of truth deyil.
