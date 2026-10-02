# Hacknet — Full Corpus Theme Candidate Scan

## 1. Məqsəd

Bu sənəd Hacknet üçün verified **11,773 English Steam review** üzərində aparılan ilk full-corpus theme scan nəticələrini saxlayır.

Bu mərhələnin məqsədi final semantic classification vermək deyil. Məqsəd:

- bütün corpus-da hansı mövzuların tez-tez qeyd olunduğunu görmək;
- hansı mövzuların negative review-lərdə ümumi bazadan daha çox göründüyünü tapmaq;
- playtime və theme birlikdə necə dəyişir sualına ilkin cavab almaq;
- sonrakı manual/LLM aspect classification üçün audit prioritetlərini seçməkdir.

Deterministik taxonomy:

`config/theme_taxonomy.yaml`

Processor:

`src/processors/theme_candidates.py`

Bu sənəd `analysis/hacknet/deep-research.md` üçün quantitative dəstəkdir, amma hələ final aspect-sentiment report deyil.

---

# 2. Metod

Hər review-un `review_text_clean` sahəsi əvvəlcədən müəyyən edilmiş regex/keyword pattern-lərlə skan olunub.

Review bir neçə theme-ə eyni anda düşə bilər.

Məsələn:

> "Story was great, but the same commands became repetitive."

review-u həm `STORY_NARRATIVE`, həm də `REPETITION` candidate-i ola bilər.

Vacib məhdudiyyət:

> Theme-i qeyd edən review-un Steam recommendation-ı həmin theme haqqında sentiment demək deyil.

Məsələn positive review daxilində repetition tənqid oluna bilər.

Ona görə aşağıdakı `Overall positive ratio` sütunu yalnız belə oxunmalıdır:

> "Bu theme-i qeyd edən review-lərin neçə faizi ümumilikdə oyunu recommend edib?"

Bu, aspect-level positive sentiment deyil.

---

# 3. Corpus coverage

- Total review: **11,773**
- Ən azı bir theme candidate-i tapılan review: **6,086**
- Candidate coverage: **51.69%**
- Ümumi dataset positive ratio: **94.13%**
- Ümumi dataset negative ratio: **5.87%**

51.69% coverage zəif nəticə deyil, çünki taxonomy qəsdən yüksək recall üçün həddindən artıq geniş yazılmayıb.

Theme pattern-i tapılmayan review:

- çox qısa ola bilər;
- meme/joke ola bilər;
- eyni fikri taxonomy-də olmayan sözlərlə deyə bilər;
- heç bir product-research mövzusu daşımaya bilər.

Bu səbəbdən candidate coverage final theme coverage kimi şərh edilməməlidir.

---

# 4. Full-corpus nəticələri

| Theme | Mənası | Mention | Corpus payı | Overall positive ratio | Negative-review enrichment* | Orta playtime |
|---|---|---:|---:|---:|---:|---:|
| STORY_NARRATIVE | Story və narrative | 2,422 | 20.57% | 96.08% | 0.67× | 14.43h |
| TERMINAL_UI | Terminal / command-line | 2,269 | 19.27% | 92.95% | 1.20× | 12.07h |
| DEPTH_CHALLENGE | Dərinlik / challenge / puzzle | 1,534 | 13.03% | 93.74% | 1.07× | 13.80h |
| IMMERSION | Immersion | 1,140 | 9.68% | 96.14% | 0.66× | 14.29h |
| SOUND_AUDIO | Soundtrack / audio | 1,116 | 9.48% | 96.42% | 0.61× | 14.59h |
| REALISM_ACCURACY | Realizm / texniki düzgünlük | 932 | 7.92% | 95.92% | 0.69× | 14.31h |
| INVESTIGATION_DISCOVERY | Araşdırma / kəşf | 610 | 5.18% | 96.07% | 0.67× | 15.63h |
| UI_USABILITY | UI/UX istifadə rahatlığı | 535 | 4.54% | 91.21% | 1.50× | 12.80h |
| REPETITION | Təkrarçılıq | 517 | 4.39% | 76.79% | **3.95×** | 11.64h |
| BUGS_COMPATIBILITY | Bug / compatibility | 502 | 4.26% | 72.71% | **4.65×** | 9.93h |
| ONBOARDING_CLARITY | Tutorial / aydınlıq | 462 | 3.92% | 87.45% | **2.14×** | 11.09h |
| MOD_REPLAYABILITY | Mod / Workshop / replay | 405 | 3.44% | 97.78% | 0.38× | 25.19h |
| HACKER_FANTASY | Hacker fantasy-si | 401 | 3.41% | **98.25%** | 0.30× | 11.45h |
| PACING_WAITING | Pacing / gözləmə | 311 | 2.64% | 90.03% | **1.70×** | 13.20h |
| PLAYER_AGENCY | Seçim / agency | 224 | 1.90% | 84.82% | **2.59×** | 11.79h |
| LENGTH_CONTENT | Oyun uzunluğu / content | 143 | 1.21% | 96.50% | 0.60× | 13.23h |
| EDUCATIONAL_IMPACT | Öyrənmə / texnologiyaya maraq | 107 | 0.91% | 97.20% | 0.48× | 15.94h |
| WORLD_REACTIVITY | Consequence / urgency / reactivity | 48 | 0.41% | 79.17% | **3.55×** | 19.70h |

* **Negative-review enrichment** = həmin theme-i qeyd edən review-lərdəki negative recommendation payının bütün dataset-in 5.87% negative bazasına nisbəti.

Məsələn `REPETITION = 3.95×` o deməkdir ki, repetition candidate-i olan review-lərdə negative recommendation ümumi dataset bazasından təxminən dörd dəfə çoxdur.

Bu metric correlation-dur, causation deyil.

---

# 5. Ən vacib quantitative siqnallar

## 5.1. Story və terminal discussion-un mərkəzidir

Ən geniş iki candidate:

- `STORY_NARRATIVE`: 20.57%
- `TERMINAL_UI`: 19.27%

və onların birlikdə göründüyü review sayı:

**833**

Bu, Hacknet haqqında player discussion-da story ilə interface-in ayrılmadığını göstərən güclü siqnaldır.

Bu, əvvəlki qualitative nəticəni dəstəkləyir:

> Hacknet-də terminal yalnız control scheme deyil; narrative experience-in bir hissəsidir.

Lakin bu nəticə hələ "story uğurun səbəbidir" demək deyil.

---

## 5.2. Ən güclü mənfi risk siqnalı bugs və repetition-dır

Ümumi negative rate yalnız **5.87%** olduğu halda:

### BUGS_COMPATIBILITY

- 502 mention
- 137 negative review
- overall positive ratio: 72.71%
- negative enrichment: **4.65×**

### REPETITION

- 517 mention
- 120 negative review
- overall positive ratio: 76.79%
- negative enrichment: **3.95×**

Bu iki theme hazırkı corpus scan-də ən güclü negative-association siqnalıdır.

Bu, qualitative sample-larda gördüyümüz iki problemi kəmiyyət baxımından da prioritet edir:

1. real texniki problemlər;
2. eyni hacking sequence-nin təkrar hissi.

---

## 5.3. World reactivity az qeyd olunur, amma qeyd olunanda risklidir

`WORLD_REACTIVITY` yalnız **48 review** tapıb.

Buna görə bu theme üçün prevalence barədə nəticə çıxarmaq olmaz; taxonomy burada çox dar ola bilər.

Amma həmin candidate-lərin:

- 10-u negative;
- positive ratio-su 79.17%;
- negative enrichment-i 3.55×

olub.

Bu, qualitative review-lərdə görülən:

- "logs are useless";
- "no urgency";
- "world is not alive";
- "enemy hackers yoxdur";
- consequence kifayət qədər real deyil

şikayətlərinin ayrıca semantic audit edilməsini əsaslandırır.

Bu theme-in keyword taxonomy-si genişləndirilməlidir.

---

## 5.4. Player agency də ayrıca problem namizədidir

`PLAYER_AGENCY`:

- 224 mention
- 34 negative
- 84.82% overall positive
- **2.59× negative enrichment**

Bu nəticə əvvəlki "tool = key" və linear workflow müşahidəsi ilə uyğun gəlir.

Sonrakı semantic audit zamanı fərqləndirmək lazımdır:

- story choice;
- hacking approach choice;
- mission choice;
- route/branch;
- "fake choice" şikayətləri.

Hazırkı taxonomy bunları birlikdə tutur.

---

## 5.5. Onboarding/clarity problemi realdır

`ONBOARDING_CLARITY`:

- 462 mention
- 58 negative
- 87.45% overall positive
- **2.14× negative enrichment**

Bu da full dataset-in əvvəlki playtime statistikası ilə birlikdə əhəmiyyətlidir:

- 0–1h segment positive ratio: 67.05%
- 1–3h: 86.59%
- 3–10h: 95.79%
- 10h+: 98.57%

Bu, səbəb-nəticə sübut etmir.

Amma early-session research üçün onboarding/clarity-ni prioritet mövzu etməyə kifayət qədər evidence verir.

---

# 6. Positive-associated theme-lər

Bəzi candidate-lər negative review-lərdə bazadan xeyli az görünür.

## Hacker fantasy

- 401 mention
- 394 positive
- 7 negative
- positive ratio: **98.25%**
- negative enrichment: **0.30×**

Bu, Hacknet-in əsas value proposition-u barədə əvvəlki qualitative nəticəni gücləndirir.

Vacib qeyd:

Taxonomy yalnız "feel like a hacker", "hackerman", "wannabe hacker" kimi explicit ifadələri tutur.

Deməli 3.41% corpus share:

> yalnız açıq şəkildə hacker fantasy-dən danışan review-lərin minimum candidate ölçüsüdür.

Həqiqi fantasy prevalence bundan daha yüksək ola bilər.

---

## Mod / replayability

- 405 mention
- positive ratio: **97.78%**
- orta playtime: **25.19 saat**

Bu theme-in orta playtime-ı bütün digər böyük theme-lərdən nəzərəçarpacaq yüksəkdir.

Bu, mod/Workshop community content-in long-tail engagement ilə əlaqəli ola biləcəyini göstərir.

Amma causation iddia edilmir:

> uzun oynayan insanlar modlardan danışmağa daha meylli də ola bilər.

---

## Soundtrack / audio

- 1,116 mention
- 96.42% overall positive
- negative enrichment 0.61×

Soundtrack yalnız kiçik niche theme deyil; corpus-un təxminən **9.5%-ində** explicit audio/sound mention tapılıb.

Bu, interface-heavy oyunlarda audio-nun əhəmiyyəti barədə əvvəlki nəticəni ciddi şəkildə gücləndirir.

---

## Immersion

- 1,140 mention
- 96.14% overall positive
- negative enrichment 0.66×

Bu da Hacknet-in əsas məqsədinin — oyunçunu hacker kimi hiss etdirməyin — player discussion-da əhəmiyyətli olduğunu göstərir.

---

## Investigation / discovery

- 610 mention
- 96.07% overall positive
- orta playtime: 15.63h

Bu theme yalnız hacking action-dan fərqli olaraq:

- exploration;
- clue;
- secret;
- investigation;
- discovery

dilini tutur.

Positive association Hacknet-in ən güclü hissəsinin sadəcə port açmaq yox, məlumat və sirr tapmaq ola biləcəyi hipotezini dəstəkləyir.

---

# 7. Realizm nəticəsi ilk baxışda paradoksaldır

`REALISM_ACCURACY`:

- 932 mention
- 95.92% overall positive
- yalnız 38 negative review

Bu rəqəmə baxıb:

> "oyunçular Hacknet-i realistik hesab edir"

nəticəsi çıxarmaq səhv olar.

Eyni theme həm:

> "real hacking-ə kifayət qədər oxşayır"

deyən positive review-u,

həm də:

> "bu real hacking deyil"

deyən negative review-u tutur.

Buna görə REALISM theme-i **aspect polarity classification** üçün ən vacib audit case-lərindən biridir.

Qualitative nümunələr göstərir ki:

- bəzi oyunçular selected authenticity-ni sevir;
- technical auditoriyanın bir hissəsi isə marketing və shell behavior-dan narazıdır.

Bu mövzuda overall Steam recommendation xüsusilə yararsız proxy-dir.

---

# 8. Theme co-occurrence

Ən çox birlikdə görünən theme cütlükləri:

| Theme A | Theme B | Review sayı |
|---|---|---:|
| STORY_NARRATIVE | TERMINAL_UI | 833 |
| DEPTH_CHALLENGE | STORY_NARRATIVE | 726 |
| SOUND_AUDIO | STORY_NARRATIVE | 625 |
| DEPTH_CHALLENGE | TERMINAL_UI | 573 |
| IMMERSION | STORY_NARRATIVE | 509 |
| REALISM_ACCURACY | TERMINAL_UI | 491 |
| SOUND_AUDIO | TERMINAL_UI | 437 |
| IMMERSION | TERMINAL_UI | 429 |
| REALISM_ACCURACY | STORY_NARRATIVE | 390 |
| TERMINAL_UI | UI_USABILITY | 353 |
| DEPTH_CHALLENGE | SOUND_AUDIO | 350 |
| INVESTIGATION_DISCOVERY | STORY_NARRATIVE | 348 |
| DEPTH_CHALLENGE | IMMERSION | 301 |
| STORY_NARRATIVE | UI_USABILITY | 296 |
| IMMERSION | SOUND_AUDIO | 282 |
| INVESTIGATION_DISCOVERY | TERMINAL_UI | 281 |
| DEPTH_CHALLENGE | REALISM_ACCURACY | 278 |
| DEPTH_CHALLENGE | INVESTIGATION_DISCOVERY | 250 |
| REPETITION | TERMINAL_UI | 244 |
| MOD_REPLAYABILITY | STORY_NARRATIVE | 234 |
| REPETITION | STORY_NARRATIVE | 230 |
| ONBOARDING_CLARITY | TERMINAL_UI | 223 |

Burada iki xüsusilə vacib nəticə var.

### Story çox sayda başqa experience layer-i ilə birlikdə müzakirə olunur

Story:

- terminal;
- challenge;
- sound;
- immersion;
- investigation

ilə yüksək co-occurrence göstərir.

Bu, Hacknet-də narrative-in ayrıca layer yox, bütün experience-i birləşdirən sistemlərdən biri olması hipotezini gücləndirir.

### Repetition terminal və story ilə birlikdə görünür

- REPETITION + TERMINAL_UI: **244**
- REPETITION + STORY_NARRATIVE: **230**

Bu, repetition şikayətinin oyunun əsas identity layer-lərindən ayrı olmadığını göstərir.

Başqa sözlə:

> Oyunçunun sevdiyi terminal/story fantasy-si core loop-un təkrarçılığını tam aradan qaldırmır.

---

# 9. Playtime ilə bağlı ilkin siqnallar

Full corpus-un əvvəlki segment ölçüləri:

| Segment | Bütün review-lər |
|---|---:|
| 0–1h | 783 |
| 1–3h | 1,081 |
| 3–10h | 5,131 |
| 10h+ | 4,751 |

Bəzi theme-lərin segment paylanması:

## BUGS_COMPATIBILITY

- 0–1h: 60
- 1–3h: 40
- 3–10h: 203
- 10h+: 196

0–1 saat qrupunda bugs candidate rate təxminən **7.7%**-dir.

Bu, digər böyük segmentlərdən nəzərəçarpacaq yüksəkdir.

Early experience-in bir hissəsi real game-design yox, launch/compatibility friction ola bilər.

## ONBOARDING_CLARITY

- 0–1h: 49
- 1–3h: 49
- 3–10h: 186
- 10h+: 178

0–1h segmentində candidate rate təxminən **6.3%**-dir və sonrakı segmentlərə nisbətən daha yüksəkdir.

Bu, first-session clarity-nin ayrıca audit edilməsini dəstəkləyir.

## STORY_NARRATIVE

- 0–1h: 50
- 1–3h: 95
- 3–10h: 1,018
- 10h+: 1,254

Story mention share playtime artdıqca çox yüksəlir.

Bu iki cür izah oluna bilər:

1. story daha uzun oynadıqca daha vacib olur;
2. oyunu sevib uzun oynayan insanlar daha uzun və story-oriented review yazır.

Bu iki izahı hazırkı data ilə ayırmaq mümkün deyil.

## MOD_REPLAYABILITY

- 0–1h: 8
- 1–3h: 5
- 3–10h: 135
- 10h+: 257

Bu, mod/replay discussion-un əsasən long-playtime audience-də olduğunu göstərir.

---

# 10. Bu scan hansı əvvəlki nəticələri gücləndirdi?

`analysis/hacknet/deep-research.md` daxilindəki aşağıdakı hipotezlər artıq full-corpus retrieval evidence ilə daha güclü dəstək alır:

## Güclənən positive hypotheses

- Hacker fantasy əsas value proposition-dur.
- Story experience-in mərkəzi hissəsidir.
- Terminal/UI yalnız control layer deyil.
- Immersion güclü driver-dir.
- Soundtrack interface-heavy experience-də böyük rol oynayır.
- Investigation/discovery Hacknet-in sadə hacking loop-dan daha dəyərli hissələrindən biridir.
- Mod/Workshop long-tail engagement üçün əhəmiyyətli ola bilər.

## Güclənən risk hypotheses

- Repetition əsas design riskidir.
- Technical bugs/compatibility first-session və recommendation-a ciddi zərbə vura bilir.
- Onboarding/clarity early-session riskidir.
- Player agency ayrıca araşdırılmalıdır.
- World reactivity/consequence complaint-ləri az sayda olsa da mənfi association yüksəkdir.
- UI/terminal authenticity technical expectation yaratdığı üçün usability və realism ayrıca audit tələb edir.

---

# 11. Nəyi hələ demək olmaz?

Bu corpus scan əsasında aşağıdakı cümlələr hələ yazılmamalıdır:

> "20.57% oyunçu story-ni sevir."

Yanlışdır. 20.57% review story-related keyword daşıyır.

> "76.79% oyunçu repetition-dan razıdır."

Yanlışdır. Bu, repetition keyword-u olan review-lərin overall recommendation ratio-sudur.

> "World reactivity yalnız 0.41% oyunçu üçün vacibdir."

Yanlışdır. Taxonomy bu theme üçün çox dar və yüksək precision yönümlüdür.

> "Mod support 25 saat oynamağa səbəb olur."

Yanlışdır. Correlation var, causation sübut olunmayıb.

---

# 12. Taxonomy keyfiyyəti haqqında nəticə

İlkin taxonomy useful retrieval layer-dir, amma final classification üçün bərabər keyfiyyətdə deyil.

## Nisbətən yüksək confidence retrieval

- STORY_NARRATIVE
- TERMINAL_UI
- SOUND_AUDIO
- REPETITION
- BUGS_COMPATIBILITY
- ONBOARDING_CLARITY
- MOD_REPLAYABILITY

## Semantic audit xüsusilə vacibdir

- DEPTH_CHALLENGE — bir neçə fərqli anlayışı birlikdə tutur
- REALISM_ACCURACY — həm praise, həm complaint eyni keyword-lardan istifadə edir
- PLAYER_AGENCY — story choice və gameplay choice qarışır
- PACING_WAITING — normal "wait" ifadələri false positive yarada bilər
- IMMERSION — "in the game" pattern-i genişdir

## Aşağı recall ehtimalı yüksəkdir

- HACKER_FANTASY — yalnız explicit fantasy ifadələri
- WORLD_REACTIVITY — çox dar phrase-lər
- EDUCATIONAL_IMPACT — implied learning-i tutmur
- INVESTIGATION_DISCOVERY — filesystem snooping-in bütün dilini tutmur

Bu səbəbdən taxonomy final report-a olduğu kimi daşınmamalıdır.

---

# 13. Növbəti mərhələ: semantic aspect audit

İndi full-corpus keyword scan-dən sonra ən düzgün addım:

## Priority 1 — negative-risk themes

Əvvəl manual/LLM audit:

1. BUGS_COMPATIBILITY
2. REPETITION
3. WORLD_REACTIVITY
4. PLAYER_AGENCY
5. ONBOARDING_CLARITY
6. UI_USABILITY
7. PACING_WAITING

Məqsəd:

- true positive / false positive;
- complaint subtype;
- aspect sentiment;
- root cause

çıxarmaqdır.

## Priority 2 — value-driver themes

Sonra:

1. HACKER_FANTASY
2. STORY_NARRATIVE
3. IMMERSION
4. SOUND_AUDIO
5. INVESTIGATION_DISCOVERY
6. MOD_REPLAYABILITY
7. EDUCATIONAL_IMPACT

Məqsəd:

> Oyunçular konkret nəyi sevir?

sualına keyword deyil, semantic cavab verməkdir.

## Priority 3 — ambiguous themes

- REALISM_ACCURACY
- DEPTH_CHALLENGE
- TERMINAL_UI

bunlar praise və complaint-i çox qarışdırdığı üçün subtheme-lərə bölünməlidir.

---

# 14. Aspect classification üçün təklif olunan schema

Sonrakı semantic classification row-u minimum belə olmalıdır:

```json
{
  "review_id": "123",
  "aspects": [
    {
      "theme": "REPETITION",
      "subtheme": "same_hacking_sequence",
      "sentiment": "negative",
      "confidence": "high"
    },
    {
      "theme": "STORY_NARRATIVE",
      "subtheme": "mystery",
      "sentiment": "positive",
      "confidence": "high"
    }
  ]
}
```

Mümkün sentiment:

- positive
- negative
- mixed
- neutral

Confidence:

- high
- medium
- low

Bu mərhələdə review-un Steam thumbs-up/down dəyəri yalnız əlavə feature olacaq; aspect sentiment-i əvəz etməyəcək.

---

# 15. Cari nəticə

Full 11,773-review corpus scan ilkin qualitative Hacknet analizinin əsas istiqamətlərini təkzib etmədi; əksinə onların bir neçəsini daha güclü prioritetləşdirdi.

Ən vacib indiki nəticə:

> **Hacknet-in discussion mərkəzi story + terminal + immersion üçlüyüdür; ən güclü design-risk siqnalı isə repetition-dır. Bugs ayrıca texniki risk kimi daha da güclü negative association göstərir.**

Yeni oyun üçün bundan hələ birbaşa feature list çıxarmaq lazım deyil.

Növbəti addım:

> bu candidate-ləri semantic aspect səviyyəsində ayırmaq və "nə qeyd olunur?" sualından "konkret olaraq nə bəyənilir və nə bəyənilmir?" sualına keçməkdir.

---

## Status

- Corpus: **11,773 verified Steam review**
- Scan coverage: **6,086 review / 51.69%**
- Method: deterministic regex/keyword candidate retrieval
- Final semantic classification: **hələ aparılmayıb**
- Next: priority theme semantic audit + aspect classification
