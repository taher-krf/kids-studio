# Video smoke test package v0.1 — V-01…V-05 (prepared, NOT executed)

**Status: PREPARED. NOT EXECUTED. EXECUTION IS AN OWNER ACTION.** Prepared 2026-09-26 under the 3D-first working direction (`DEC-0020`). This is the image-to-video smoke test defined in the [3D benchmark reference brief](BENCHMARK_3D_REFERENCE_PACKAGE_V0.4.md) §5: it proves the minimum motion case before any weighted benchmark. **It is not the benchmark, not a renderer decision, and not a production authorization.** Final Canon v1.0 remains blocked (`DEC-0017`).

**Test environment:** the owner's existing **Google AI Pro** access — Gemini / Flow first. **Zero additional spend.** Flow (or Gemini video) is the *first smoke-test environment only*; nothing here locks it as the production renderer. If the existing access cannot produce a needed clip, record the gap — do not purchase anything.

## 0. Common rules

- **Source of truth:** the six Round 1.5 masters (register: [ROUND_1_5_BASELINE_MANIFEST.json](../05_visual_system/ROUND_1_5_BASELINE_MANIFEST.json)). Conditioning stills come only from there or from Round 2 sheets derived from them.
- **Clip storage:** owner's local asset workspace, `Round 01\_smoke\` — **no video bytes in the repository**.
- **File naming:** `V<nn>_<subject>_<yyyymmdd>_t<take>.<ext>` — e.g. `V01_mulu_idle_20260927_t01.mp4`. Keep every take; log each one.
- **One variable per take:** same still, same instruction; change one thing between takes.
- **Provenance row per take** (R-X1): tool + version + model, settings, full instruction text, seed if exposed.
- **Timing references:** 24 fps design timings per [Visual Development v0.3 §5](../05_visual_system/VISUAL_DEVELOPMENT_V0.3.md); judge the intent, not the exact frame count, at smoke-test level.
- **Every clip is also eyeballed at 48 px** (thumbnail readability in motion) and checked for childhood-gate safety (nothing scary or uncanny).
- **Logging:** one result row per take (template in §7); record D-codes observed; a failed take is evidence, not waste.

## 1. Test cards

### V-01 — Mulu idle bob

| Field | Value |
| --- | --- |
| Source still | `Mulu/R1.5_MULU_3D_MASTER.jfif` |
| Goal | prove the idle: continuous gentle bob, 1.5–2 s cycle, ~2% of body height; he is never fully still |
| Duration | 2 s (loopable if the tool allows) |
| Motion instruction | "The cloud character floats in place with a gentle, continuous vertical bob. Nothing else moves. The camera is locked. The character's design, proportions, colours and face stay exactly the same." |
| Negative constraints | no arms, hands, legs or feet growing; no squash beyond ±15%; no new puffs; no camera move; no background change; no eye style change |
| Continuity checks | first and last frames match the master (returns to model); flat base stays flat; underside band stays cool |
| Drift checks | D01, D02, D03, D04 (Top Puff side!), D05, D06, D07 |
| Pass when | bob is continuous and gentle; zero D01–D07 across frames; design identical at loop point |
| Fail examples | limbs appear; puff detaches; camera drifts; bob becomes a bounce with overshoot |

### V-02 — Mulu sad drizzle

| Field | Value |
| --- | --- |
| Source still | **PREREQUISITE GAP:** the intended source (R1.5-02 sad Mulu variant) was not produced in Round 1.5. Produce the sad master first (Round 2 checklist item M-2). Do not substitute the rain-off-shell two-shot — it is a composition, not a clean single-character still. |
| Goal | prove the water grammar in motion: sad drizzle falls straight down from the flat base as small teardrops, 5–10 drops in loose columns |
| Duration | 2 s |
| Motion instruction | "Light drizzle: small teardrops fall straight down from the cloud's flat bottom edge. The cloud stays still apart from its gentle bob. The camera is locked." |
| Negative constraints | no sweat-drop on the head; no tears from the eyes; no streaks, spray or mist; no storm or lightning; drops never come from the sides or top |
| Continuity checks | drop count stays small and countable; body tint may go grey-blue (sad) but nothing else changes |
| Drift checks | D08, D09 (plus D01–D06) |
| Pass when | every drop originates at the flat base and falls straight down as a teardrop; no sweat-drop grammar anywhere |

### V-03 — Tekla small steps + dead stop

| Field | Value |
| --- | --- |
| Source still | `Tekla/R1.5_TEKLA_3D_MASTER.jfif` |
| Goal | prove her travel grammar: quick small steps (~6 frames each), then a **dead stop with no overshoot** |
| Duration | 2 s |
| Motion instruction | "The character takes a few quick small steps to one side, then stops dead with no overshoot or wobble. Arms stay folded. The camera is locked." |
| Negative constraints | shell never deforms; exactly three bands; apron, pocket and ruler stay put; no spin, no roll, no jump; no facial restyle |
| Continuity checks | band count stable across frames (D11); ruler still in pocket (D15); ears unchanged; feet stay big and flat |
| Drift checks | D11, D12, D14, D15 |
| Pass when | steps read as quick and small; the stop is instant and clean; zero drift on shell, apron, ruler |
| Fail examples | elastic overshoot; shell squashes like fabric; ruler vanishes; ears grow (rabbit drift) |

### V-04 — Tekla Curl

| Field | Value |
| --- | --- |
| Source still | `Tekla/R1.5_TEKLA_3D_MASTER.jfif` (start) — **PREREQUISITE GAP:** the target-state reference (R1.5-04 Curl ball / Peek) was not produced in Round 1.5. Until Round 2 item T-2 exists, run this test **exploratory-only** (start still + instruction, no end-state conditioning) and mark results as such. |
| Goal | prove the transformation: egg → ball in 6–8 frames, ending on the small "click"; shell never deforms; ear tips land at the seam |
| Duration | 1.5 s |
| Motion instruction | "The character tucks forward and closes into a neat round banded ball, like a closing book, ending perfectly still. The shell stays rigid. The camera is locked." |
| Negative constraints | no squash-stretch shell; no spin blur or speed lines; no rolling away; the ball shows three bands; no limbs sticking out at the end |
| Continuity checks | ball diameter ~0.56 TH; three bands visible on the ball; the apron disappears inside the ball |
| Drift checks | D11, D12, D15 |
| Pass when | the curl completes in 6–8 frames into a stable banded ball; shell rigid throughout; readable as a tuck, not a morph |

### V-05 — Hilltop ambience

| Field | Value |
| --- | --- |
| Source still | `Hilltop/R1.5_HILLTOP_3D_MASTER.jfif` |
| Goal | prove the world can breathe without breaking: grass, wind chimes and stream move gently; geography holds |
| Duration | 3 s |
| Motion instruction | "Gentle ambient motion only: a light breeze in the grass and the tree, the wind chimes sway softly, the stream flows. The camera is locked. Nothing enters or leaves the frame." |
| Negative constraints | no camera drift or zoom; no new objects, characters or animals; no weather change; the umbrella bed, door, board, bench, chair, garden and bridge stay in place; at most three things react to the wind |
| Continuity checks | tree stage-left, garden + bench/chair right, stream at the foot, umbrella bed above the door, two-square board — all fixed (D18); no text appears (D19) |
| Drift checks | D18, D19, D20; three-thing rule (D10) |
| Pass when | ambience reads in 3 s with geography and props identical at start and end |

## 2. Result log template (one row per take)

Keep as `Round 01\_smoke\SMOKE_TEST_LOG.csv` (local) and summarize outcomes back into the repository when the run completes.

| Field | Entry |
| --- | --- |
| test_id | V-01…V-05 |
| take_file | `V01_mulu_idle_20260927_t01.mp4` |
| date / reviewer | |
| tool + version + model | (e.g. Flow via Google AI Pro; exact model label) |
| source_still | filename from the R1.5 register |
| instruction_text | full text used |
| seed / settings | if exposed, else UNKNOWN |
| pass_fail_per_criterion | goal / motion / negatives / continuity / drift: pass or fail each |
| d_codes_observed | e.g. D04 at 0.8 s |
| 48px_check | reads / fails |
| verdict | PASS / FAIL / MIXED |
| notes | |

## 3. After the run

- Summarize per-test verdicts into the repository (ledger `RES` entry + state update); clips stay local.
- Any V-test failing for **design** reasons (not tool reasons) feeds the Round 2 watch items before model sheets are finalized.
- The weighted benchmark (B1–B10) still requires its own owner authorization with approaches and a spend limit — this smoke test does not grant it.
