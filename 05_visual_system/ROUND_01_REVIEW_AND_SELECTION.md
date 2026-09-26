# Round 01 Visual Review and Selection — Mulu & Tekla

**Status: REVIEW FINDINGS AND SELECTION RECOMMENDATIONS. NOT CANON, NOT A STYLE LOCK, NOT FINAL DESIGN.** Reviewed under the owner-communicated **3D-first working direction** (2026-09-26: 3D characters, 3D world, 3D video benchmark, unless the images argue against it). Recorded as `RES-0010` (findings) and `PROP-0009` (recommendations, awaiting owner confirmation). The formal owner picks (one Mulu family, one Tekla direction, one look) remain the owner's decision per the [generation package](GENERATION_PACKAGE_V0.3.md).

Design source: [Visual Development v0.3](VISUAL_DEVELOPMENT_V0.3.md) · [generation package](GENERATION_PACKAGE_V0.3.md) · [Hilltop set plan](HILLTOP_SET_V0.3.md) · machine-readable selections: [ROUND_01_SELECTION_MANIFEST.json](ROUND_01_SELECTION_MANIFEST.json) · next phase: [3D benchmark reference brief](../06_production/BENCHMARK_3D_REFERENCE_PACKAGE_V0.4.md).

## 1. Evidence base

Round 01 images live **outside the canonical repository**, in the owner's local asset workspace:

`C:\Users\PC\Documents\GitHub\Kids Studio Assets\Visual Development\Round 01\` (`Mulu\`, `Tekla\`, `Pair\`, `Hilltop\`)

This owner action answers the open storage question (`RSK-0006` item 8) in practice: **exploration images are kept in a local asset workspace, not committed to the repository.** This review references them by filename only; no image bytes enter the repo.

| Category | File | Look | Notes |
| --- | --- | --- | --- |
| Mulu | `Mulu/Gemini_Generated_Image_7l13gp7l13gp7l13.jfif` | 2D clean | two variants (tall, small); control-quality only |
| Mulu | `Mulu/Gemini_Generated_Image_nfdbipnfdbipnfdb.jfif` | **3D soft toy** | two variants (calm, worried); **selected look baseline** |
| Tekla | `Tekla/Gemini_Generated_Image_pkrb8apkrb8apkrb.jfif` | 2D clean | standing + curled ball; control-quality only |
| Tekla | `Tekla/Gemini_Generated_Image_zbn8cfzbn8cfzbn8.jfif` | **3D clay** | standing + curled ball ("click" annotation); **selected baseline** |
| Pair | `Pair/Gemini_Generated_Image_sj9iaasj9iaasj9i.jfif` | 2D clean | talk-height two-shot; **selected structural baseline** |
| Hilltop | `Hilltop/Gemini_Generated_Image_fvze2dfvze2dfvze.jfif` | 2D storybook | master-wide style plate; composition reference only |

**Provenance:** filenames indicate a Gemini image generator; no prompts, seeds, settings or batch log were kept — a gap against [generation package §8](GENERATION_PACKAGE_V0.3.md). From the refinement pass onward every batch gets a provenance row (refinement R-X1).

**Coverage gaps against Round 1 of the generation package:** no 3D pair, no 3D Hilltop, no Cloud Hat (G-10), no rain-off-the-shell (G-11), no turnarounds or expression sheets, no thumbnail board (G-14). The 2D outputs stand in as the L-1 controls; no M-A/M-C or T-A/T-B control families were generated — acceptable in hindsight, since M-B and T-C were already the recommended directions and nothing in the outputs argues for the alternates.

## 2. Findings by category

Scored with the [review rubric](GENERATION_PACKAGE_V0.3.md) (0/1/2; 22 max; advance at ≥ 16 with a 2 on "Not generic" and a clean childhood gate). "—" = not assessable from Round 01 material.

### 2.1 Mulu

| Criterion | Mulu-01 (2D, `7l13gp`) | Mulu-02 (3D, `nfdbip`) |
| --- | --- | --- |
| Cloud read | 1 (cloud head on a kid's body) | 2 (reads as a cumulus at a glance; the soft-solid 3D head is cloud-true, not marshmallow) |
| Spec match (M-B) | 0 (arms with fingers, legs, feet; sweat-drop; no flat base, no nubs) | 1 (one tall puff + one shoulder puff present; but arms, legs and feet instead of a floating flat base + two nubs; no cool underside band) |
| Face appeal | 2 | 2 (calm and worried variants both huggable) |
| Emotion legibility | 1 | 2 (worried variant reads instantly: brows, blush, small mouth) |
| Not generic | 0 (anime sweat-drop + stock 2D mascot) | 1 (charming but glossy iris/sclera eyes are stock "AI 3D cute") |
| Pair contrast | (see 2.3) | (see 2.3) |
| Thumbnail 48 px | — (not tested) | — (not tested) |
| Drift (D-codes) | 0 (D06 limbs; D08 sweat-drop water) | 0 (D06 limbs; D08 sweat-drop; underside band missing) |
| Childhood gate | pass | pass |

**Findings.** The 3D candidate is the strongest Mulu: the matte soft-solid material reads as a *cloud*, which tentatively answers `RSK-0006` item 3 (the marshmallow risk) in 3D's favour. Both solo images share the same systematic drift: **the generator gave Mulu a humanoid body** (arms, legs, feet) instead of the floating flat-base body with two nubs, and drew water as an anime sweat-drop instead of base rain. The best spec-faithful Mulu structure is ironically in the 2D pair image (2.3): floating, flat base with a cool underside, asymmetric puffs, no legs.

### 2.2 Tekla

| Criterion | Tekla-01 (2D, `pkrb8a`) | Tekla-02 (3D, `zbn8cf`) |
| --- | --- | --- |
| Armadillo read (not turtle) | 2 (bands, ringed cone tail, snout; no carapace) | 2 (stepped band seams + cone tail; no carapace; ears slightly rabbit-tall at small sizes) |
| Spec match (T-C) | 1 (hard hat, apron, pocket, ruler all present; but fully upright — closer to T-A — and a short bearish snout) | 1 (three bands + hard hat + apron + pocket; ruler missing (D15); eyes wrong; arms not folded) |
| Face appeal | 2 | 2 |
| Emotion legibility | 2 (the flat-mouth deadpan is exactly "I'm fine") | 1 (round sclera eyes read worried-cute, not deadpan; the ball reads perfectly) |
| Not generic | 1 | 1 (standard clay-cute eyes) |
| Pair contrast | (see 2.3) | (see 2.3) |
| Thumbnail 48 px | — | — |
| Drift (D-codes) | 1 (shell reads slightly as a worn cape; upright stance) | 0 (D15 ruler; eye drift; "click"/motion-line annotations — fine on a dev sheet, barred from reference art) |
| Childhood gate | pass | pass |

**Findings.** The 3D clay direction is charming and the **curled ball is fully convincing in 3D** (ear tips peeking from the seam, tidy bands, readable "click" action) — the Curl, her most important transformation, survives the medium. Two fixes matter most: the eyes must go half-lidded with a flat lid line (the deadpan *is* the character), and the shell needs its terracotta deepened against the cream-tan skin — right now shell and skin are near-identical in value, so the three bands under-read (a D11-adjacent risk). The 2D control proves the deadpan works when drawn; it is kept as the acting reference, not the baseline.

### 2.3 The Pair

| Criterion | Pair-01 (2D, `sj9iaa`) |
| --- | --- |
| Instant silhouette contrast | 2 (wide/soft/cream vs. narrow/crisp/terracotta — nameable apart at a glance) |
| Scale | 2 (Mulu ≈ 2× her body width, ≈ her height, floating at talk height; matches [§4.1](VISUAL_DEVELOPMENT_V0.3.md) within tolerance) |
| Chemistry | 2 (they read as friends; his open face vs. her composed stance is the show's shape language) |
| Balance | 2 (neither dominates; equal frame weight) |
| Series-duo believability | 2 (thumbnail/poster-ready composition) |
| Cloud Hat / contact poses | — (not generated — the key open test) |
| Drift | 1 (his sclera eyes again; her happy smile is off-default but legitimate as a beat; slight lash hint on her eye to watch, D14) |
| Childhood gate | pass |

**Findings.** The single pair image is the most decision-useful asset of Round 01: it proves the duo reads instantly, and it contains the best Mulu structure of the round (floating, flat base, cool underside shading, asymmetric puffs). It is 2D only — **no 3D pair exists yet**, and neither does the Cloud Hat test that `RSK-0006` item 1 flags as the weakest silhouette. The pair is therefore selected as a *structural* baseline (staging, scale, chemistry) that must be re-rendered in 3D.

### 2.4 The Hilltop

| Criterion | Hilltop-01 (2D, `fvze2d`) |
| --- | --- |
| World charm | 2 (warm, lived-in, handmade; the two-fingerprints idea reads) |
| Simplicity / reusability | 0 (hammock, telescope, souvenir shelf, backpack, baskets, duplicate chimes, tools on the knoll face — over the set plan's named-element budget) |
| Small playable comedy set | 1 (right spirit; needs decluttering to stay shootable across hundreds of shots) |
| Supports the three pilots | 1 (knoll + door, garden, stream, chimes, board, bench all present; the umbrella bed — needed by P1 and P3 — is wrong) |
| Geography / continuity | 0 (tree on stage RIGHT vs. the plan's stage-left; garden downstage-left vs. the right slope; forecast board has four squares vs. two; umbrella is a patterned parasol over a hammock vs. the red upturned umbrella-bed on a post above the door) |
| 3D suitability | — (2D storybook only; no 3D world image exists) |
| Childhood gate | pass |

**Findings.** A genuinely charming plate that gets the *feeling* right and the *geography* wrong. It is adopted as a **composition and charm reference only**; the baseline world must be rebuilt in 3D directly from [HILLTOP_SET_V0.3](HILLTOP_SET_V0.3.md), with element positions, the umbrella bed and the two-square board corrected, and the clutter cut to named set elements.

## 3. Repeated failure patterns (cross-cutting)

1. **Humanoid-body drift on Mulu** (2 of 3 images): generators keep giving the cloud arms, legs and feet. This is the single biggest spec risk and must be countered with structure conditioning (the sketch SVGs as control images) and explicit negatives (R-M1, R-X1).
2. **Generic-AI face drift** (all images): glossy irises + sclera where the spec requires simple dark ovals (him) and half-lidded dark eyes (her). This is what currently caps every candidate at 1 on "Not generic".
3. **Wrong water grammar**: the anime sweat-drop stands in for rain. Mulu's water only ever falls from his flat base as teardrops (D08).
4. **Geography and asymmetry flips**: tree side flipped on the Hilltop; watch the Top Puff side (D04) and band count (D11) in every 3D batch.
5. **Text/motion annotations** on sheets ("click", motion lines): acceptable on dev sheets, barred from reference art (R-X2).
6. **No provenance log** for Round 01 (R-X1) and **no thumbnail board** (R-X3).
7. **Coverage gaps**: no 3D pair, 3D Hilltop, Cloud Hat, or rain-off-shell.

## 4. Selections (recommended working baselines)

| Category | Selected baseline | Source evidence | Nature of selection |
| --- | --- | --- | --- |
| **Mulu** | **3D soft-solid M-B**, look from `nfdbip`, structure corrected to spec | Mulu-02 (look) + Pair-01 (structure) | Look baseline + structural correction list (R-M1…R-M5) |
| **Tekla** | **3D clay T-C**, from `zbn8cf` | Tekla-02 (+ Tekla-01 as deadpan acting reference) | Baseline with fix list (R-T1…R-T5) |
| **Pair** | **Pair-01 staging/scale/chemistry, re-rendered in 3D** | `sj9iaa` | Structural baseline; 3D re-render + Cloud Hat + rain-off-shell required (R-P1…R-P3) |
| **Hilltop** | **Corrected 3D build per the set plan** | `fvze2d` as charm/composition reference only | Rebuild, not refinement (R-H1…R-H4) |

Nothing here is a canon lock. These are the agent's recommended baselines under the owner's 3D-first working direction, for owner confirmation (`PROP-0009`).

## 5. Required refinements before benchmark generation

**Mulu (R-M):**
- R-M1: remove arms, hands, legs and feet → the floating flat-base body with exactly two nubs (D06).
- R-M2: eyes → dark vertical ovals, one highlight each, no sclera, no pupils; chunky separate brows (spec §2.3).
- R-M3: restore the cool blue-grey underside band; warm-cream body (P-1 "Sunny Clay").
- R-M4: no sweat-drop; water only as teardrops from the flat base; wind as swirl lines (D08–D10).
- R-M5: Top Puff over his own right side in every output; reject mirror flips (D04).

**Tekla (R-T):**
- R-T1: half-lidded eyes with a flat lid line; no sclera; keep the small flat mouth (the deadpan default).
- R-T2: deepen the shell to terracotta `#C9643E` against cream-tan skin `#F1D4AF` so exactly three bands read in colour *and* silhouette (D11).
- R-T3: default pose arms folded.
- R-T4: the yellow folding ruler always in the apron pocket (D15).
- R-T5: lengthen/taper the snout slightly; keep ears but watch the rabbit neighbour at ≤ 64 px.

**Pair (R-P):**
- R-P1: 3D pair at talk height and float height; Mulu ≈ 0.9 TH wide and ≈ 0.85 TH tall (D16).
- R-P2: the Cloud Hat in 3D — side, slight 3/4, slightly above (G-10); her ear tips out of the seam; test at 48 px (answers `RSK-0006` item 1).
- R-P3: rain rolling off the shell in 3D (G-11); she stays completely dry (D13).

**Hilltop (R-H):**
- R-H1: fix geography to the set plan — knoll + round door upstage centre, Lookout Tree stage-left with Mulu's branch, bench + old chair downstage right, garden on the right slope, stream at the foot; hold the 180° line.
- R-H2: replace parasol + hammock with the red upturned umbrella-bed on a post above the door (ribs + hooked handle readable).
- R-H3: two-square Forecast Board, pictograms only (D19).
- R-H4: cut clutter to named set elements; keep the handmade pegged style; design once with fixed states.

**Cross-cutting (R-X):**
- R-X1: a provenance row per batch (tool + version + model, settings, seeds, full prompt, negatives, control inputs) per [§8](GENERATION_PACKAGE_V0.3.md).
- R-X2: no text, letters or motion-line annotations inside reference art.
- R-X3: compose the 128/64/48 px black-silhouette thumbnail board (G-14) from refinement outputs before Round 2.

## 6. Recommendation: **B — proceed with 3D, after one small refinement pass**

- **Not A:** no Round 01 candidate passes the rubric unmodified (both 3D candidates score 1 on "Not generic" and carry D-code drift), and 3D coverage of the pair, the world and the two key contact shots does not exist yet.
- **Not C:** a split 2D/3D comparison already happened informally inside Round 01 — the 3D outputs are the strongest candidates in every category they appear in, and the owner's working direction is 3D-first. Re-running a formal 2D/3D bake-off would spend budget to re-answer a decided question.
- **Not D:** nothing in the images argues against the current direction. The premise, the shapes and the soft-solid bet all survived first contact with generation; the failures are drift patterns, not concept failures.
- **Therefore B:** run one bounded refinement pass (Round 1.5) against the R-lists above — same tool family, structure-conditioned on the sketch SVGs — then let the owner confirm the four baselines, then proceed to Round 2 model sheets, the image-to-video smoke test and the Round 3 benchmark package per the [3D benchmark reference brief](../06_production/BENCHMARK_3D_REFERENCE_PACKAGE_V0.4.md).

## 7. Self-review of this review

| Question | Answer |
| --- | --- |
| Could any selection be made from stronger evidence? | No — the 3D coverage gaps are stated, not papered over; the pair and Hilltop selections are explicitly structural/compositional pending 3D re-renders. |
| Is anything here a canon claim? | No. All selections are `PROP-0009` recommendations awaiting owner confirmation; Final Canon v1.0 remains blocked (`DEC-0017`). |
| Were weak candidates preserved, not deleted? | Yes — all six images remain in the owner's local workspace untouched; rejection rationale is recorded above. |
| Does anything argue against 3D? | No image does. The 2D Tekla control is the better *deadpan acting* reference, which is an argument to keep it as reference, not to switch mediums. |
