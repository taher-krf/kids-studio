# 3D Benchmark Reference Package v0.4 — Brief for the Next Phase

**Status: BRIEF. SPECIFIES FUTURE WORK. THE BENCHMARK IS NOT AUTHORIZED TO RUN. NO TOOL, RENDERER OR PURCHASE IS SELECTED.** Proposed as `PROP-0009` under the owner-communicated **3D-first working direction** (2026-09-26). It adapts the [benchmark reference package v0.3](BENCHMARK_REFERENCE_PACKAGE_V0.3.md) — which stays the governing spec for shot lists, weights and acceptance logic — to a 3D visual target, using the [Round 01 review](../05_visual_system/ROUND_01_REVIEW_AND_SELECTION.md). Nothing here is canon.

The path to the benchmark is now: **Round 1.5 (refinement) → owner confirms the four baselines → Round 2 (3D model sheets) → image-to-video smoke test → Round 3 (benchmark-grade 3D package) → owner authorizes the weighted benchmark.**

## 1. What changes under a 3D target

| Area | v0.3 assumption | v0.4 (3D-first) change |
| --- | --- | --- |
| Look | L-1 clean 2D vs. L-2 soft 3D toy, open | **L-2 soft 3D toy is the working look**; L-1 outputs remain controls/acting references only |
| Materials | implied by look block | A **material spec sheet** becomes a required deliverable (BRP-00): Mulu matte felt/marshmallow, no shine; Tekla shell softly glazed clay, apron woven canvas, skin matte; world matte clay-and-felt, handmade pegged wood |
| Turnarounds | drawings | same-material 3D renders on a plain light-cream background, neutral studio light, all six views per character |
| Thumbnail board | silhouettes from drawings | silhouettes **rendered from the 3D masters** at 128/64/48 px (G-14) |
| Effects (rain, wind) | drawn style frames | style frames plus a **3D execution note** per effect: teardrop geometry, swirl-line treatment (drawn overlay vs. geometry), shell beading |
| Video compatibility | out of scope | new §5 image-to-video readiness requirements and a pre-benchmark smoke test |

## 2. Round 1.5 — refinement pass (bounded, next action)

One small batch per category, same tool family as Round 01, structure-conditioned on the [construction sketches](../05_visual_system/sketches/mulu_silhouette_families.svg) (PNG exports at moderate strength), full provenance rows (R-X1). Each item is accepted only when its refinement list from the [review §5](../05_visual_system/ROUND_01_REVIEW_AND_SELECTION.md) checks clean.

| ID | Deliverable | Acceptance |
| --- | --- | --- |
| R1.5-01 | Mulu 3D master, front neutral | R-M1…R-M5 clean: floating flat base, two nubs, dark oval eyes, underside band, no sweat-drop, Top Puff on his right |
| R1.5-02 | Mulu 3D, happy + sad + worried variants | same body as R1.5-01; feeling reads at 128 px |
| R1.5-03 | Tekla 3D master, 3/4 deadpan, arms folded | R-T1…R-T5 clean: half-lidded eyes, three high-contrast bands, ruler in pocket, tapered snout |
| R1.5-04 | Tekla 3D Curl ball + the Peek | matches the Round 01 ball quality; ear tips at the seam |
| R1.5-05 | Pair 3D at talk height + float height | R-P1 clean; chemistry of the 2D pair preserved |
| R1.5-06 | Cloud Hat 3D: side, slight 3/4, slightly above | R-P2; nameable at 48 px in the thumbnail board (answers `RSK-0006` item 1) |
| R1.5-07 | Rain off the shell 3D | R-P3; teardrops bead and roll; she is dry (D13) |
| R1.5-08 | Hilltop 3D master wide (HT-01 framing) | R-H1…R-H4 clean: set-plan geography, umbrella bed, two-square board, no clutter |
| R1.5-09 | Thumbnail board (G-14) from the above | both leads nameable as silhouettes at 48 px |

**Owner gate after Round 1.5:** confirm the four baselines (or send one back). This is the formal pick moment from the generation package, one pass later than planned.

## 3. Round 2 — 3D model sheets (after owner confirmation)

Same sheet list as [v0.3 Round 2](../05_visual_system/GENERATION_PACKAGE_V0.3.md) (G-02–G-05, G-07, G-08, G-12, G-13), executed as same-material 3D renders, plus:

- **BRP-00 material spec sheet** (new): close-up material references per lead and for the world, with the exact matte/glaze/canvas read of the accepted masters.
- **Set dress sheet**: each named Hilltop element alone on a plain background with its fixed states (states per the [set plan](../05_visual_system/HILLTOP_SET_V0.3.md)).
- D-codes are logged per sheet; the D01–D20 checklist applies unchanged ([checklist](../05_visual_system/VISUAL_DEVELOPMENT_V0.3.md)).

## 4. Round 3 — benchmark-grade package (BRP-01…BRP-14, 3D-adjusted)

The v0.3 contents table stands, with these adjustments:

- **BRP-01 / BRP-06 turnarounds:** 3D renders, six views each, construction overlays in W/TH units; the Top Puff side and the three bands verified per view.
- **BRP-04 rain style sheet:** add teardrop geometry + shell-beading style frames (drips bead and roll off the bands).
- **BRP-05 wind style sheet:** decide and record the swirl treatment for 3D (drawn overlay line vs. geometry); the three-thing rule unchanged.
- **BRP-08 pair sheet:** must include the Cloud Hat and rain-off-shell from R1.5-06/07, now consistent with the masters.
- **BRP-09 Hilltop plates:** HT-01–HT-06 as 3D layouts in the three lighting states, from locked camera positions; one autumn re-dress of HT-02.
- **BRP-12 temp sound list:** unchanged (scratch only; no final music, casting or voice cloning).
- **BRP-14 animatic panels:** unchanged; B7 and B10 boarded from the beat sheets.

## 5. Image-to-video readiness and the smoke test

The future benchmark assumes video generation from stills. Before any weighted run, prove the minimum motion case with a **smoke test** (not the benchmark; no renderer decision):

| ID | Clip | Source still | Pass when |
| --- | --- | --- | --- |
| V-01 | Mulu idle bob, 2 s loop | R1.5-01 | continuous gentle bob; zero D01–D06 across frames; returns to model |
| V-02 | Mulu sad drizzle, 2 s | R1.5-02 | drops fall straight from the flat base as teardrops; no sweat-drop; no storm |
| V-03 | Tekla steps + dead stop, 2 s | R1.5-03 | quick small steps, dead stop, no overshoot; three bands stable |
| V-04 | The Curl with click, 1.5 s | R1.5-03/04 | egg → ball in 6–8 frames; shell never deforms; ear tips land at the seam |
| V-05 | Hilltop ambience, 3 s (grass, chimes, stream) | R1.5-08 | set geography holds; ≤ 3 wind-reacting objects; no camera drift |

Readiness requirements on every reference still from Round 1.5 onward: plain light-cream background, soft neutral studio light, full character in frame, no annotations (R-X2), consistent framing across variants, and a provenance row (R-X1) — these are the inputs video tools will condition on.

## 6. Unchanged gates

- The weighted benchmark (B1–B10, weights and pass criteria per [v0.3](BENCHMARK_REFERENCE_PACKAGE_V0.3.md) and the [benchmark brief](PRODUCTION_BENCHMARK_BRIEF_V0.2.md)) runs **only** after: Round 1.5 accepted, owner confirms baselines, Rounds 2–3 complete, and the owner authorizes the run with approaches and a spend limit.
- The design-change trigger stands: if B1–B4 fail in every approach, revisit Mulu's design via the [rescue ladder](../05_visual_system/VISUAL_DEVELOPMENT_V0.3.md) before any visual lock.
- Final Canon v1.0, renderer selection, finished episodes and publication remain blocked (`DEC-0017`); no spend without explicit owner approval.
