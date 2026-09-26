# Production Benchmark Brief v0.2

**Status: BRIEF ONLY. THE BENCHMARK IS NOT AUTHORIZED TO RUN. NO TOOL, RENDERER, SERVICE OR PURCHASE IS SELECTED.** Written under `DEC-0018`, part of `PROP-0007`. It gives concrete content to the weighted benchmark recommended by Stress Test 001 (`PROP-0006` repair 5) and Red-Team Review 001 §15. Running it requires a separate owner authorization and applicable spend approval ([technology benchmark](TECHNOLOGY_BENCHMARK.md)).

## 1. The question the benchmark answers

**What does it cost, in time and money per *accepted* second, to produce this show's recurring scenes and its showcase scenes at consistent quality, and which production approach does that best?**

It also answers a creative question: **do the production-aware design choices in [Show Bible v0.2 §22](../01_show_bible/SHOW_BIBLE_V0.2_DEVELOPMENT.md) actually make the hard shots affordable?** These choices are the soft-solid cloud, discrete drops, drawn wind, the three-thing rule and a waterproof Tekla. If they don't, the design must change before the Visual Bible locks.

## 2. What changed since the red team's worst case

The red team scored the concept as close to the hardest continuity stack available. v0.2 redesigns three of the five stressors on purpose. The benchmark must confirm or refute each:

| Stressor (red team) | v0.2 design response | Benchmark must show |
| --- | --- | --- |
| Vapor-body continuity | Opaque soft-solid Mulu with a fixed silhouette | Identity holds across 20+ shots with no drift |
| Rain–prop contact | Discrete drops from the flat base only; Tekla never wet | Drops start, stop and change rate on cue, from the right place |
| Wet/dry persistence | "The hill dries in one scene"; tracked only when story-relevant | Within-scene wet trails stay consistent |
| Calibrated mild wind | Drawn swirl lines + three-thing rule | Wind reads as mild and legible with ≤3 reacting objects |
| Subtle acting / timing | Tekla's feelings are carried by big behaviors; reaction holds are designed | Comic timing holds to the frame; the "I'm fine" beat lands |

## 3. Test shots (weighted)

Each test is a short shot or mini-sequence drawn from the development pilots ([pilot candidates](../04_episodes/PILOT_CANDIDATES_V0.2.md)). Weights reflect where the show's identity and cost concentrate.

| ID | Test | Source | Weight |
| --- | --- | --- | ---: |
| B1 | **Identity continuity:** both leads across 20 varied shots (angles, distances, lighting states) | any | 15% |
| B2 | **Mulu body acting:** idle bob, happy spin, drift-back, vibrating stillness; squash through a gap and return to model | Pilot 1 (seatbelt) | 10% |
| B3 | **Discrete rain:** Secret Drip start/stop, side-drip, rate change, drizzle, happy rain | Pilot 3 | 15% |
| B4 | **Within-scene wet trail:** a drip trail stays consistent across 4 consecutive shots, then is gone next scene | Pilot 3 | 10% |
| B5 | **Drawn wind + three-thing rule:** joy gust scattering a row of pinecones; sheet lifted; chimes ringing | Pilots 1–3 | 10% |
| B6 | **Tekla behavior acting:** the Straightening, the Tiny Bow, the Curl and uncurl, the Roll | Pilot 2 | 10% |
| B7 | **Comic timing:** the pebble *clonk* → hold → "I'm fine" → straighten beat, to the frame | Pilot 1 | 10% |
| B8 | **Designed contact:** the Cloud Hat; handing over a teacup; Mulu carrying the umbrella beneath himself | Pilots 1, 3 | 10% |
| B9 | **Environment reuse:** the Hilltop's six standard setups across 20 shots; seasonal re-dress of one setup | hub | 5% |
| B10 | **Mini-scene integration:** a 30–45 s sequence, Pilot 1's unveiling (sheet-pull to "Meant to do that") | Pilot 1 | 5% |

**Slate mix to price:** from the tested cost per accepted second, estimate a 10-episode slate at the Show Bible tier mix (about 6 Tier A : 3 Tier B : 1 Tier C), matching the Stress Test 001 burden mix (about 6 MEDIUM : 3 HIGH : 1 EXTREME).

## 4. Approaches to compare (categories, not products)

1. **Generative-led:** video generation from references and first/last frames, with editing.
2. **Hybrid:** deterministic character assets and rigs (2D or 3D) for the leads and effects, with generative help for backgrounds, exploration or in-betweens.
3. **Deterministic:** conventional 2D or 3D animation pipeline as the quality and cost baseline.

Specific products stay candidates under `06_production/TECHNOLOGY_BENCHMARK.md`. No product is endorsed by this brief.

## 5. Metrics (per test, per approach)

- **Cost per accepted second** (the primary decision metric): money plus human hours, including rejected attempts.
- **Yield:** the share of attempts accepted without manual fix.
- **Drift incidents** per 10 shots, using the named failure list in the [Visual Bible brief §10](../05_visual_system/VISUAL_BIBLE_BRIEF_V0.2.md).
- **Editability:** can one shot be revised without regenerating or breaking its neighbors?
- **Timing control:** frame accuracy of holds and reactions.
- **Safety review:** every generated frame batch is checked for unsafe or uncanny content. This is non-optional.
- **Rights and provenance:** inputs, outputs and terms recorded for each approach.

## 6. Pass / warning thresholds (proposed; owner may revise)

- **Pass:** an approach passes a test if it produces the shot at **consistent model** (zero drift incidents in the accepted set) with **frame-controllable timing**, at a cost the owner judges viable for the tier.
- **Design-change trigger:** if B1–B4 fail across *all* approaches, the soft-solid cloud and discrete-rain design choices are not enough. Revisit the Mulu design before the Visual Bible locks, not after.
- **Concept-economics trigger:** if Tier A cost is not viable in any approach, raise the red-team §19B trigger (the Fix-It economics comparison) with the owner.

## 7. Inputs the benchmark needs (from other phases)

- A benchmark reference package from the Visual Bible phase: provisional turnarounds, state sheets, the rain/wind style sheets and the Hilltop set plan. This can be a *benchmark-grade* package, not final design.
- Beat-level descriptions of B7 and B10 from the pilot beat sheets.
- A shot manifest template extension with state fields (capacity, tint, edge, wet patches, Snail position, Keep Shelf), per [Visual Bible brief §10](../05_visual_system/VISUAL_BIBLE_BRIEF_V0.2.md).

## 8. Out of scope

Choosing a winner tool, buying subscriptions, producing publishable footage, voice casting, music composition, publishing.

## 9. Recommended sequencing

Visual Bible exploration → owner picks a direction → benchmark-grade reference package → **benchmark run (needs owner authorization and a spend limit)** → results feed the Visual Bible lock and the pilot production decision. The benchmark should run *before* the Visual Bible locks, so production evidence can still shape the design.
