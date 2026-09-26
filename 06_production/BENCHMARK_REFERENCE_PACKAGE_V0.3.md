# Benchmark-Grade Reference Package v0.3 — Specification

**Status: SPECIFIED, NOT PRODUCED. THE BENCHMARK IS NOT AUTHORIZED TO RUN. NO TOOL, RENDERER OR PURCHASE IS SELECTED.** Proposed under `PROP-0008`. This is the exact reference package and shot list that the [weighted production benchmark](PRODUCTION_BENCHMARK_BRIEF_V0.2.md) needs (its §7 "inputs"). Running the benchmark needs a separate owner authorization and spend limit.

> **Round 01 update (2026-09-26, `PROP-0009`):** under the owner-communicated 3D-first working direction, the 3D-adjusted path to this package (Round 1.5 → Round 2 → image-to-video smoke test → Round 3) is specified in [BENCHMARK_3D_REFERENCE_PACKAGE_V0.4.md](BENCHMARK_3D_REFERENCE_PACKAGE_V0.4.md). The shot list, weights and acceptance logic below remain the governing spec.

"Benchmark-grade" means consistent enough to test identity and effects against, not final design. The package is produced in visual Round 3 ([generation package](../05_visual_system/GENERATION_PACKAGE_V0.3.md)), after the owner picks directions in Round 1.

## 1. Package contents

| ID | Deliverable | Must contain | Accept when |
| --- | --- | --- | --- |
| BRP-01 | Mulu turnaround | front, 3/4 left and right, side left and right, back; construction overlay in W units | matches [§2.2](../05_visual_system/VISUAL_DEVELOPMENT_V0.3.md#22-construction-spec-m-b); the Top Puff on his right in every view |
| BRP-02 | Mulu state chart | the 5 Top Puff poses; 3 tints; 2 edges; 3 capacity states; held breath | every state is the same silhouette family; nothing unlisted |
| BRP-03 | Mulu expressions | the 12 face presets | readable at 128 px |
| BRP-04 | Rain style sheet | drop anatomy; the Drip + ripple; side-drip; drizzle; happy rain; plips; aimed rain; drip-rate chart (slow ~1.5 s, worried ~0.8 s); landing on grass, wood, **Tekla's shell (beads and rolls off)**, and the umbrella bowl | drops always teardrops from the flat base (except the side-drip) |
| BRP-05 | Wind style sheet | the swirl terminal; breeze, gust, huff, giggle-puff; response library (leaf, sheet, chimes, pinwheel, pinecone, apron, ears); three-thing-rule examples | mild at a glance; ≤ 3 reacting objects in standard examples |
| BRP-06 | Tekla turnaround | the same six views; construction overlay in TH units | three bands in every view; apron, pocket and ruler constant |
| BRP-07 | Tekla acting sheet | neutral; the Straightening; Tiny Bow; tap-tap; Swish; Curl key poses (4) + click frame; the Peek; Roll cycle; real laugh; fake GASP | the shell never deforms; the ball matches the ball spec |
| BRP-08 | Pair sheet | scale grid; talk, float and Lookout heights; the Cloud Hat; teacup handover; rain off the shell; shade | scale within ±5% of [§4.1](../05_visual_system/VISUAL_DEVELOPMENT_V0.3.md#41-scale-and-heights) |
| BRP-09 | Hilltop plates | HT-01 to HT-06 layouts in morning, day and golden hour; HT-02 reverse; WS-01; one autumn re-dress of HT-02 | set pieces sit in identical positions per setup ([set plan](../05_visual_system/HILLTOP_SET_V0.3.md)) |
| BRP-10 | Prop sheet with states | umbrella bed (on post / carried / filling ¼·½·¾ / tipped); Forecast Board + 6 symbols; chimes (parts / wrapped / hung / ringing); teapot, 2 cups, straw, jug; old chair + new chair (4 states); sheet; strap; pebbles; rope + pulley; present (wrapped / lace / open); hook; "not looking" screen; Keep Shelf | each state named with the ID used in the [prop manifest](../05_visual_system/PROP_MANIFEST.json) |
| BRP-11 | World extras | the Snail (with its dot) in 4 headings; butterfly cycle; fledgling (hop, flap, land-on-head) | the Snail findable in HT-01 at 1080p |
| BRP-12 | Temp sound list | drip plink, clonk, click, tap-tap, chimes chord, swirl whoosh, "I'm fine" sting; **scratch** lines for B7 and B10 read by a team member | for timing only; no final music or casting, no voice cloning |
| BRP-13 | Shot state manifests | one [shot state record](../04_episodes/templates/SHOT_STATE_TEMPLATE.json) per test shot below | every state field filled before generation or animation |
| BRP-14 | Animatic panels | B7 and B10 boarded from the beat sheets, with the timing chart | holds match §3 |

## 2. Test shots

Weights are from the benchmark brief. The beats are in the [pilot beat sheets](../04_episodes/development_pilots/README.md).

| Test | Weight | Shots (source beats) | Pass criteria (in addition to the brief's) |
| --- | ---: | --- | --- |
| **B1 Identity** | 15% | 20 shots: HT-01 ×3, HT-02 front ×3, HT-02 reverse ×2, HT-03 ×3, HT-05 ×2, HT-06 ×2, WS-01 ×2, close-ups ×3 (Mulu happy, Tekla deadpan, the Cloud Hat); mixed lighting | zero D01–D06, D11, D14–D16 in the accepted set |
| **B2 Mulu body** | 10% | idle bob 4 s; happy spin (P1-03); drift-back; vibrating stillness; hover gap (P1-04); strap squeeze and return (P1-06); Top Puff up→droop (P1-13) | returns exactly to model within the shot; the hover gap reads in every angle |
| **B3 Discrete rain** | 15% | Drip start on cue (P3-01); rate change (P3-05); side-drip (P3-06); drip→drizzle (P3-11); stops dead (P3-13); happy rain into the seat (P1-08); drizzle rolling off the shell (P2-13) | start/stop within ±2 frames of cue; zero D08/D09 |
| **B4 Wet trail** | 10% | P3-03 → P3-05: four consecutive shots (the trail forms; Tekla sees it; laser-stepping close-up; the wide again), then the next scene | identical drop positions across all four (the `wet_patches` record); gone after the scene |
| **B5 Drawn wind** | 10% | joy-spin scatter of pinecones, stakes and a leaf (P2-07); sheet lift (P1-02); chimes feedback loop (P3-16) | ≤ 3 reacting objects; swirl style constant; reads as mild |
| **B6 Tekla behaviour** | 10% | tiny Straightening (P2-04); the Snail rotation (P2-06); Tiny Bow (P1-02); Curl + uncurl with click (P2-09); Roll on flat ground (P2-09); Swish (P1-16) | three bands throughout; no shell deformation; the Roll never reads as a spin-dash |
| **B7 Comic timing** | 10% | P1-07 pebble *clonk* sequence (chart below) | every hold within ±1 frame; one beat revisable without regenerating neighbours |
| **B8 Contact** | 10% | the Cloud Hat (P3-15); teacup handover; umbrella carried beneath Mulu with a rising water level (P3-07); straw drinking (P1-08); Tekla's lean (P1-15, flagged) | no interpenetration; props stay attached; Tekla dry |
| **B9 Environment reuse** | 5% | 20 shots across HT-01 to HT-06; autumn re-dress of HT-02 | set pieces don't drift between shots of one setup; re-dress changes only dressing |
| **B10 Mini-scene** | 5% | P1-02 → P1-03 unveiling, 30–45 s | identity, timing and a sound-off read hold across the assembled scene |

## 3. B7 timing chart (24 fps)

| Frame | Event |
| ---: | --- |
| 0 | Butterfly enters frame-left; Mulu concentrating, sinking with pebbles |
| 0–48 | Butterfly flutters toward him (anticipation, 2 s) |
| 48 | Mulu's eyes flick to it (2-frame move) |
| 54 | Gasp; Top Puff perks |
| 58 | Happy gust; Mulu lifts ~0.1 TH over 8 frames |
| 60 | Pebbles leave his nubs |
| 68 / 74 / 80 | *Clonk* ×3 on her shell (6-frame rhythm) |
| 80–104 | **Hold** (24 frames): her deadpan; his "uh-oh" |
| 104–124 | "I'm fine." |
| 124–130 | Pause |
| 130–136 | She turns to the chair |
| 136–150 | Straightens it (4-frame nudge + hold) |

## 4. Scoring and logging

- Use the benchmark brief's metrics (cost per *accepted* second, yield, drift incidents per 10 shots, editability, timing control, safety, rights).
- Log drift by **D-code** ([checklist](../05_visual_system/VISUAL_DEVELOPMENT_V0.3.md#7-readability-and-drift-checklist)) so failures point at a design rule, not a vague "off-model".
- **Design-change trigger** (from the brief): if B1–B4 fail in every approach, revisit Mulu's design (starting with the [rescue ladder](../05_visual_system/VISUAL_DEVELOPMENT_V0.3.md#28-the-soft-solid-bet-and-the-rescue-ladder)) before any visual lock.

## 5. What must happen before the benchmark runs

1. **Owner:** choose the visual exploration tool or illustrator and a spend limit for Rounds 1–3.
2. Rounds 1–2 done; the owner picks the Mulu family, Tekla direction and look.
3. Round 3 produces BRP-01 to BRP-14.
4. **Owner:** authorize the benchmark run, the approaches (categories from the brief §4) and a spend limit.
