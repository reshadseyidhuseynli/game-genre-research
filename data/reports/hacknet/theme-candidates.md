# Hacknet — Theme Candidate Corpus Scan

> Bu report final semantic classification deyil. Regex/keyword qaydaları ilə tapılan
> review namizədlərini və həmin review-lərin Steam recommendation/playtime paylanmasını göstərir.
> Theme-in positive ratio-su aspect sentiment deyil; həmin theme-i qeyd edən review-lərin
> overall Steam recommendation ratio-sudur.

## Coverage

- Total reviews: 11773
- Reviews with at least one theme candidate: 6009
- Candidate coverage: 51.04%
- Taxonomy version: 1

## Theme statistics

| Theme | Azərbaycan dilində | Mentions | Share | Positive reviews | Negative reviews | Overall positive ratio | Avg playtime at review |
|---|---|---:|---:|---:|---:|---:|---:|
| STORY_NARRATIVE | Story və narrative | 2422 | 20.57% | 2327 | 95 | 96.08% | 14.43h |
| TERMINAL_UI | Terminal və command-line interfeysi | 2269 | 19.27% | 2109 | 160 | 92.95% | 12.07h |
| DEPTH_CHALLENGE | Dərinlik, challenge və problem həlli | 1534 | 13.03% | 1438 | 96 | 93.74% | 13.80h |
| SOUND_AUDIO | Soundtrack və audio | 1116 | 9.48% | 1076 | 40 | 96.42% | 14.59h |
| REALISM_ACCURACY | Realizm və texniki düzgünlük | 932 | 7.92% | 894 | 38 | 95.92% | 14.31h |
| IMMERSION | Immersion və atmosferə daxil olma | 910 | 7.73% | 888 | 22 | 97.58% | 13.36h |
| INVESTIGATION_DISCOVERY | Araşdırma, kəşf və clue tapma | 610 | 5.18% | 586 | 24 | 96.07% | 15.63h |
| UI_USABILITY | UI/UX və istifadə rahatlığı | 534 | 4.54% | 487 | 47 | 91.20% | 12.78h |
| REPETITION | Təkrarçılıq | 517 | 4.39% | 397 | 120 | 76.79% | 11.64h |
| BUGS_COMPATIBILITY | Bug və compatibility | 502 | 4.26% | 365 | 137 | 72.71% | 9.93h |
| ONBOARDING_CLARITY | Onboarding, tutorial və aydınlıq | 462 | 3.92% | 404 | 58 | 87.45% | 11.09h |
| MOD_REPLAYABILITY | Mod, Workshop və replayability | 405 | 3.44% | 396 | 9 | 97.78% | 25.19h |
| HACKER_FANTASY | Hacker fantasy-si | 401 | 3.41% | 394 | 7 | 98.25% | 11.45h |
| PLAYER_AGENCY | Seçim və player agency | 154 | 1.31% | 129 | 25 | 83.77% | 11.32h |
| LENGTH_CONTENT | Oyun uzunluğu və content miqdarı | 143 | 1.21% | 138 | 5 | 96.50% | 13.23h |
| EDUCATIONAL_IMPACT | Öyrənmə və texnologiyaya maraq yaratma | 107 | 0.91% | 104 | 3 | 97.20% | 15.94h |
| WORLD_REACTIVITY | Consequence, urgency və dünyanın reaktivliyi | 48 | 0.41% | 38 | 10 | 79.17% | 19.70h |
| PACING_WAITING | Pacing, gözləmə və temp | 46 | 0.39% | 40 | 6 | 86.96% | 11.56h |

## Top theme co-occurrences

| Theme A | Theme B | Reviews |
|---|---|---:|
| STORY_NARRATIVE | TERMINAL_UI | 833 |
| DEPTH_CHALLENGE | STORY_NARRATIVE | 726 |
| SOUND_AUDIO | STORY_NARRATIVE | 625 |
| DEPTH_CHALLENGE | TERMINAL_UI | 573 |
| REALISM_ACCURACY | TERMINAL_UI | 491 |
| SOUND_AUDIO | TERMINAL_UI | 437 |
| IMMERSION | STORY_NARRATIVE | 394 |
| REALISM_ACCURACY | STORY_NARRATIVE | 390 |
| TERMINAL_UI | UI_USABILITY | 353 |
| DEPTH_CHALLENGE | SOUND_AUDIO | 350 |
| INVESTIGATION_DISCOVERY | STORY_NARRATIVE | 348 |
| IMMERSION | TERMINAL_UI | 314 |
| STORY_NARRATIVE | UI_USABILITY | 296 |
| INVESTIGATION_DISCOVERY | TERMINAL_UI | 281 |
| DEPTH_CHALLENGE | REALISM_ACCURACY | 278 |
| DEPTH_CHALLENGE | INVESTIGATION_DISCOVERY | 250 |
| REPETITION | TERMINAL_UI | 244 |
| MOD_REPLAYABILITY | STORY_NARRATIVE | 234 |
| REPETITION | STORY_NARRATIVE | 230 |
| DEPTH_CHALLENGE | IMMERSION | 225 |
| IMMERSION | SOUND_AUDIO | 225 |
| ONBOARDING_CLARITY | TERMINAL_UI | 223 |
| DEPTH_CHALLENGE | UI_USABILITY | 195 |
| BUGS_COMPATIBILITY | STORY_NARRATIVE | 189 |
| ONBOARDING_CLARITY | STORY_NARRATIVE | 189 |
| DEPTH_CHALLENGE | REPETITION | 187 |
| REALISM_ACCURACY | SOUND_AUDIO | 187 |
| SOUND_AUDIO | UI_USABILITY | 158 |
| INVESTIGATION_DISCOVERY | SOUND_AUDIO | 158 |
| DEPTH_CHALLENGE | ONBOARDING_CLARITY | 154 |

## Interpretation rules

- Bu nəticələr theme prevalence üçün ilkin retrieval siqnalıdır.
- Bir review theme keyword-u daşısa da həmin aspect-i tərifləməyə və ya tənqid etməyə bilər.
- Overall positive/negative recommendation aspect sentiment kimi istifadə edilməməlidir.
- Theme-lər üzrə generated positive/negative sample CSV-ləri manual/LLM audit üçün istifadə olunmalıdır.
- Final rəqəmlər audit edilmiş aspect classification-dan sonra analysis/<game>/deep-research.md faylına keçirilməlidir.
