# Midnight Protocol — Theme Candidate Corpus Scan

> Bu report final semantic classification deyil. Regex/keyword qaydaları ilə tapılan
> review namizədlərini və həmin review-lərin Steam recommendation/playtime paylanmasını göstərir.
> Theme-in positive ratio-su aspect sentiment deyil; həmin theme-i qeyd edən review-lərin
> overall Steam recommendation ratio-sudur.

## Coverage

- Total reviews: 301
- Reviews with at least one theme candidate: 226
- Candidate coverage: 75.08%
- Taxonomy version: 2

## Theme statistics

| Theme | Azərbaycan dilində | Mentions | Share | Positive reviews | Negative reviews | Overall positive ratio | Avg playtime at review |
|---|---|---:|---:|---:|---:|---:|---:|
| STORY_NARRATIVE | Story və narrative | 136 | 45.18% | 121 | 15 | 88.97% | 20.40h |
| DEPTH_CHALLENGE | Dərinlik, challenge və problem həlli | 112 | 37.21% | 88 | 24 | 78.57% | 20.14h |
| LOADOUT_BUILD | Loadout, deck və build seçimi | 82 | 27.24% | 69 | 13 | 84.15% | 19.21h |
| TACTICAL_TURN_BASED | Turn-based taktika və action economy | 73 | 24.25% | 61 | 12 | 83.56% | 18.02h |
| TERMINAL_UI | Terminal və command-line interfeysi | 57 | 18.94% | 43 | 14 | 75.44% | 16.96h |
| UI_USABILITY | UI/UX və istifadə rahatlığı | 41 | 13.62% | 33 | 8 | 80.49% | 13.21h |
| IMMERSION | Immersion və atmosferə daxil olma | 40 | 13.29% | 37 | 3 | 92.50% | 19.79h |
| SOUND_AUDIO | Soundtrack və audio | 40 | 13.29% | 37 | 3 | 92.50% | 18.73h |
| RNG_FAIRNESS | RNG, luck və fairness | 36 | 11.96% | 23 | 13 | 63.89% | 16.79h |
| CHOICE_REPUTATION | Moral seçim, reputation və branching | 29 | 9.63% | 27 | 2 | 93.10% | 25.17h |
| KEYBOARD_ONLY | Keyboard-only control | 28 | 9.30% | 24 | 4 | 85.71% | 13.51h |
| INVESTIGATION_DISCOVERY | Araşdırma, kəşf və clue tapma | 20 | 6.64% | 19 | 1 | 95.00% | 19.17h |
| RETRY_ROLLBACK | Retry, rollback və mission recovery | 20 | 6.64% | 13 | 7 | 65.00% | 16.98h |
| REPETITION | Təkrarçılıq | 19 | 6.31% | 12 | 7 | 63.16% | 11.09h |
| ONBOARDING_CLARITY | Onboarding, tutorial və aydınlıq | 18 | 5.98% | 15 | 3 | 83.33% | 10.01h |
| REALISM_ACCURACY | Realizm və texniki düzgünlük | 17 | 5.65% | 16 | 1 | 94.12% | 12.28h |
| URGENCY_TRACE | Trace, turn cap və urgency | 16 | 5.32% | 8 | 8 | 50.00% | 13.40h |
| MOD_REPLAYABILITY | Mod, Workshop və replayability | 14 | 4.65% | 11 | 3 | 78.57% | 13.21h |
| BUGS_COMPATIBILITY | Bug və compatibility | 12 | 3.99% | 8 | 4 | 66.67% | 17.51h |
| PACING_WAITING | Pacing, gözləmə və temp | 9 | 2.99% | 8 | 1 | 88.89% | 13.07h |
| PLAYER_AGENCY | Seçim və player agency | 9 | 2.99% | 8 | 1 | 88.89% | 25.30h |
| HACKER_FANTASY | Hacker fantasy-si | 8 | 2.66% | 8 | 0 | 100.00% | 19.31h |
| WORLD_REACTIVITY | Consequence, urgency və dünyanın reaktivliyi | 8 | 2.66% | 8 | 0 | 100.00% | 20.85h |
| LENGTH_CONTENT | Oyun uzunluğu və content miqdarı | 7 | 2.33% | 7 | 0 | 100.00% | 17.48h |
| EDUCATIONAL_IMPACT | Öyrənmə və texnologiyaya maraq yaratma | 0 | 0.00% | 0 | 0 | n/a | n/a |

## Top theme co-occurrences

| Theme A | Theme B | Reviews |
|---|---|---:|
| DEPTH_CHALLENGE | STORY_NARRATIVE | 71 |
| LOADOUT_BUILD | STORY_NARRATIVE | 63 |
| STORY_NARRATIVE | TACTICAL_TURN_BASED | 52 |
| DEPTH_CHALLENGE | LOADOUT_BUILD | 48 |
| DEPTH_CHALLENGE | TACTICAL_TURN_BASED | 41 |
| STORY_NARRATIVE | TERMINAL_UI | 39 |
| DEPTH_CHALLENGE | TERMINAL_UI | 37 |
| LOADOUT_BUILD | TACTICAL_TURN_BASED | 36 |
| LOADOUT_BUILD | TERMINAL_UI | 34 |
| IMMERSION | STORY_NARRATIVE | 31 |
| SOUND_AUDIO | STORY_NARRATIVE | 30 |
| STORY_NARRATIVE | UI_USABILITY | 30 |
| DEPTH_CHALLENGE | SOUND_AUDIO | 26 |
| RNG_FAIRNESS | STORY_NARRATIVE | 26 |
| DEPTH_CHALLENGE | IMMERSION | 24 |
| LOADOUT_BUILD | SOUND_AUDIO | 24 |
| CHOICE_REPUTATION | STORY_NARRATIVE | 24 |
| IMMERSION | LOADOUT_BUILD | 23 |
| DEPTH_CHALLENGE | UI_USABILITY | 23 |
| TACTICAL_TURN_BASED | UI_USABILITY | 22 |
| CHOICE_REPUTATION | LOADOUT_BUILD | 22 |
| LOADOUT_BUILD | UI_USABILITY | 22 |
| KEYBOARD_ONLY | STORY_NARRATIVE | 22 |
| KEYBOARD_ONLY | UI_USABILITY | 20 |
| TACTICAL_TURN_BASED | TERMINAL_UI | 20 |
| DEPTH_CHALLENGE | RNG_FAIRNESS | 20 |
| LOADOUT_BUILD | RNG_FAIRNESS | 19 |
| SOUND_AUDIO | TACTICAL_TURN_BASED | 19 |
| SOUND_AUDIO | TERMINAL_UI | 18 |
| CHOICE_REPUTATION | DEPTH_CHALLENGE | 18 |

## Interpretation rules

- Bu nəticələr theme prevalence üçün ilkin retrieval siqnalıdır.
- Bir review theme keyword-u daşısa da həmin aspect-i tərifləməyə və ya tənqid etməyə bilər.
- Overall positive/negative recommendation aspect sentiment kimi istifadə edilməməlidir.
- Theme-lər üzrə generated positive/negative sample CSV-ləri manual/LLM audit üçün istifadə olunmalıdır.
- Final rəqəmlər audit edilmiş aspect classification-dan sonra analysis/<game>/deep-research.md faylına keçirilməlidir.
