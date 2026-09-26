# Visual Development v0.3 — Mulu & Tekla

**Status: VISUAL DEVELOPMENT DIRECTION. NOT A STYLE LOCK, NOT FINAL DESIGN, NOT CANON.** Written under the owner's development decisions (`DEC-0019`) and proposed as `PROP-0008`. It turns the [Visual Bible brief v0.2](VISUAL_BIBLE_BRIEF_V0.2.md) into concrete design directions. The sketches are rough construction drawings, generated from parametric shapes by [`scripts/build_dev_sketches.py`](../scripts/build_dev_sketches.py). They are not model sheets or reference art.

> **Round 01 update (2026-09-26, `RES-0010` / `PROP-0009`):** Round 01 exploration images are reviewed in [ROUND_01_REVIEW_AND_SELECTION.md](ROUND_01_REVIEW_AND_SELECTION.md). Under the owner-communicated 3D-first working direction, the "Look / rendering style" row below is now answered in practice by the **soft 3D toy direction (L-2)**, pending the owner's formal confirmation after the Round 1.5 refinement pass. The M-B and T-C recommendations stand; no candidate passed the rubric unmodified.

Companions: [Hilltop set plan](HILLTOP_SET_V0.3.md) · [generation package](GENERATION_PACKAGE_V0.3.md) · [benchmark reference package](../06_production/BENCHMARK_REFERENCE_PACKAGE_V0.3.md) · [pilot beat sheets](../04_episodes/development_pilots/README.md) · [Show Bible v0.2](../01_show_bible/SHOW_BIBLE_V0.2_DEVELOPMENT.md).

## 0. What this package recommends, and what stays open

| Question | Recommendation | Status |
| --- | --- | --- |
| Mulu silhouette family | **M-B "Cumulus"**: a flat low body, one tall Top Puff, one small shoulder puff | Recommended; confirm with Round 1 images |
| Tekla direction | **T-C "Leaning Egg"**: semi-upright, three wrapped bands, head shield as a hard hat | Recommended; confirm with Round 1 images |
| Palette | **"Sunny Clay"**: warm cream cloud, terracotta shell, teal apron | Recommended for exploration; not locked |
| Look / rendering style | Explore **clean 2D** and **soft 3D toy** side by side | Open until Round 1 |
| Soft-solid cloud | Default direction, with a rescue ladder if it fails to charm (§2.8) | Owner-approved default, not locked (`DEC-0019`) |
| Renderer, tools | Not chosen | Blocked until the benchmark |

The sheets:

| Sheet | Shows |
| --- | --- |
| [Mulu silhouette families](sketches/mulu_silhouette_families.svg) | the generic icon we avoid, M-A, M-B, M-C, in colour, silhouette and thumbnail |
| [Mulu acting states](sketches/mulu_acting_states.svg) | Top Puff poses, depletion states, the eight-row weather code |
| [Tekla directions](sketches/tekla_directions.svg) | the turtle read we avoid, T-A, T-B, T-C, the Curl, silhouettes |
| [Tekla tells](sketches/tekla_tells.svg) | designed neutral, the five tells, the Curl, the Peek, two breaks |
| [The pair](sketches/pair_tests.svg) | scale grid, hover heights, the contact set, thumbnails |
| [Hilltop master wide](sketches/hilltop_master_wide.svg) and [set plan](sketches/hilltop_set_plan.svg) | the home set and its camera setups |

## 1. Design principles

1. **Silhouette first.** Each lead must be identifiable as a black shape at 48 px. Colour and faces are a bonus, not the identity.
2. **One signature feature each, big enough to act with.** Mulu has the Top Puff; Tekla has the banded shell with its head-shield "hard hat". Everything else stays simple.
3. **Built from fixed primitives.** Mulu is five shapes (body, Top Puff, shoulder puff, two nubs) plus a curl. Tekla is about a dozen. Fewer parts drift less, rig faster and survive AI-assisted generation.
4. **Soft vs. crisp is the pair's whole shape language.** Mulu is all circles; Tekla is arcs, bands and small triangles (ears, snout, tail). Their names echo it (bouba/kiki).
5. **Change reads as acting, never as error.** Every state that can change is enumerated (§2.5, §3.4). Anything else changing is drift (§7).
6. **Design against the average.** Generic prompts converge on the three-bump cloud and the round cute critter. Every choice here is written down so it can be enforced.
7. **Production constraints should add charm.** The flat base, the countable drops and the waterproof shell are also jokes, icons and toys.

---

## 2. Mulu

### 2.1 Three silhouette families ([sheet](sketches/mulu_silhouette_families.svg))

| | M-A "Pillow" | **M-B "Cumulus" (recommended)** | M-C "Scoop" |
| --- | --- | --- | --- |
| Construction | wide rounded loaf, corner puffs, centred curl | flat low body + one tall Top Puff over his right side + one small shoulder puff | tall dome, cheek puffs, top-knot |
| Reads as | marshmallow, pillow, bread | a real cumulus tower; a boy with a big tuft of hair | dumpling, bell, ghost |
| Cloud read | weakest | strong in colour *and* silhouette | medium |
| Distinctive vs. the icon | yes | yes, strongly (asymmetric) | yes |
| Acting | whole-body squash only | the Top Puff is an acting antenna (§2.4) | face only |
| Pair with Tekla | good width contrast | best: wide + one rising puff vs. narrow + pointed | two domes (weak) |
| Main risks | Pusheen-style loaf neighbour; no facing direction | mirror-flip drift (D04); must not read as a lump without colour | ghost/snowman read; top-knot drifts toward the poop-emoji shape |

**Why M-B.** It is the only family that is cloud-true, unmistakably *ours*, and carries emotion in silhouette. At 64 px you can still see whether he's happy (Top Puff perked), sad (drooped) or scared (tucked). The sketch iteration showed that a small shoulder puff opposite the Top Puff is what makes the black silhouette read as a cloud rather than a lump, so it is part of the design.

### 2.2 Construction spec (M-B)

Units: **W** = Mulu's body width.

| Part | Spec | Fixed? |
| --- | --- | --- |
| Body | Soft rounded dome, width W, height 0.42 W, **perfectly flat base**, base corners rounded at 0.1 W | fixed |
| Top Puff | Circle, diameter 0.54 W, centre 0.16 W to his right of centre and 0.56 W above the base; top at ~0.83 W | always one; pose varies (§2.4) |
| Curl | Small hooked curl on top of the Top Puff, hooking toward his front; ~0.13 W tall | fixed shape; never spirals upward |
| Shoulder puff | Circle, diameter 0.3 W, on his left shoulder (centre 0.25 W left of centre, 0.39 W up) | fixed, never animates |
| Nubs | Two round stubs, diameter 0.13 W, at the lower sides (0.13 W up); no fingers | always two |
| Underside | A cool blue-grey band, ~0.06 W deep, with a softly scalloped top edge: his "rain-bottom" | fixed |
| Face | Centred 0.06 W toward his left (the shoulder-puff side), balancing the Top Puff; eyes 0.25 W above the base, 0.21 W apart, 0.085 × 0.12 W dark vertical ovals with one highlight; brows are separate short strokes; mouth at 0.14 W | placement fixed; expression varies |
| Outline | One continuous outer outline, deep slate (not black); no internal lines between body and puffs | fixed |
| Surface | Opaque, matte, clean-edged; like a marshmallow or felt | fixed (see §2.8) |

**Handedness rule:** the Top Puff is always over *Mulu's own right side*: screen-left when he faces camera, screen-right when he faces away. The shoulder puff is always opposite. This makes his facing direction readable in silhouette, and a flipped puff is an instant, catchable error (D04).

### 2.3 Face and expression grammar

- **Full-range face.** Big eyes and chunky brows carry everything; the mouth is simple (smile, grin, open, frown, tight line, wobble, little "o").
- **Blush circles** appear only for happy, excited and embarrassed.
- **Eye language:** open ovals (default), closed arcs (calm, content), happy arcs (proud), squeezed `> <` (embarrassed, holding in), small ovals (scared), glancing to the side (secret).
- **No sclera, no pupils, no eyelashes.** One highlight per eye. This keeps the face consistent at every size.
- Expression-sheet deliverables: the twelve face presets drawn on the [acting sheet](sketches/mulu_acting_states.svg) (neutral, happy, excited, sad, secret, embarrassed, frustrated, scared, calm, proud, holding breath, shock).

### 2.4 The Top Puff (body acting, not a power)

| Pose | Looks like | Means |
| --- | --- | --- |
| Up | upright | neutral |
| Perk | a little taller, tilted forward | happy, proud |
| Lean | tilted strongly toward what he's looking at | wants it, curious, loves it |
| Droop | flopped over his side like a wilted ear | sad, disappointed |
| Tucked | shrunk down into the body | scared, shy |

The Top Puff never detaches, splits, multiplies, changes size outside these poses, or changes side. The shoulder puff never moves. Under Show Bible rule 2 ("inside is acting; outside is weather"), the poses are acting.

### 2.5 Body states (all enumerated)

| State family | Allowed values | Notes |
| --- | --- | --- |
| Tint | normal cream · pink (embarrassed) · grey-blue (sad) | whole body; never other colours |
| Edge | smooth · ruffled | ruffled = excited or frustrated; a scalloped outline, same silhouette |
| Capacity (optional) | plump · normal · wisp | **only when the story uses it** (P1 tea, a rained-out gag). Not a meter and not tracked every shot (`DEC-0019`). Plump: ~6% wider, ~16% taller, sits lower. Wisp: ~16% narrower, ~32% flatter, Top Puff drooped, floats higher. |
| Squash / stretch | ±15% for acting; up to ±40% for designed squeezes (P1's strap and chair) | always returns exactly to model within the same shot |
| Held breath | ~13% wider, ~20% taller, cheeks puffed, eyes squeezed | the "hiding a feeling" state (P3-06) |

### 2.6 Weather style ([acting sheet](sketches/mulu_acting_states.svg))

**Rain** (from the flat base only, straight down):

| Type | Look | Count / rhythm |
| --- | --- | --- |
| The Secret Drip | one chubby teardrop from one fixed spot; a small ripple ring where it lands | 1 drop per ~1.5 s (slow), ~0.8 s (worried) |
| Side-drip | the same drop, leaving from his side at mid-height | only while he holds a feeling in |
| Drizzle | 5–10 small drops in loose columns under the base | continuous, gentle |
| Happy rain | drizzle-sized, bouncier, with a tiny bounce where drops land | short bursts |
| Plips | 2–3 fat, slow drops | one-off |
| Aimed rain | a single-file column of small drops onto one target | calm and caring only |

Drops are teardrops (readable as water by every 3-year-old), light blue with a white highlight and a thin slate outline. There is never mist, streaks, spray, puddle-filling volume, a storm or lightning. Tears from his eyes are **not** used: all his water comes from his base.

**Wind** (drawn):

- The signature is a **swirl line**: a soft white line with a slate edge that ends in a small curl.
- Breeze: 1–2 gentle swirls. Gust: 3–4 shorter, skittery swirls. Huff: one short straight line from the mouth ending in a small puff. Giggle-puff: a tiny puff ball.
- **Deliberate wind** (he chooses to blow) comes from his mouth. **Feeling wind** (joy, excitement) peels off his body edges or spins around him. This distinction is visible and consistent.
- **Three-thing rule:** at most three light objects react to wind in a standard shot.

**At thumbnail size** the drip must read as one drop, the drizzle as "rain" and a gust as "wind lines". This is checked on the thumbnail board in the generation package.

### 2.7 Boyish without stereotype

He reads as a boy through his name, voice, pronoun and energy: bouncy, a tousled Top Puff with a cowlick curl, chunky brows, an open grin. The design avoids blue-for-boys colour coding, caps, sports gear and "tough" posing. He is soft and emotional *and* a boy, and nothing needs explaining.

### 2.8 The soft-solid bet, and the rescue ladder

The owner approved soft-solid as the production-aware default, not locked (`DEC-0019`). The sketches suggest it can read as charming. If Round 1 images show it reads as a marshmallow, a pillow or plastic rather than a cloud, climb this ladder one rung at a time and stop at the first that works:

1. Strengthen the cool underside band and add a faint warm top light (the real cumulus look).
2. Add a fixed, subtle scallop micro-texture to the outline (same silhouette).
3. Add one or two fixed interior puff lines (e.g. where the Top Puff meets the body).
4. Add a soft rim glow on the sky side.
5. **Last resort:** a softly feathered edge. This costs consistency, so it must pass benchmark B1 before adoption.

Translucency and vapour never come back: they're the continuity problem the design removed.

### 2.9 Nearest neighbours (cloud)

| Neighbour | Risk | Our divergence |
| --- | --- | --- |
| The generic cloud icon or emoji (three bumps) | where AI clouds converge | one tall off-centre Top Puff, one small shoulder puff, asymmetric |
| Middlemost Post's Parker J. Cloud; Pixar's *Partly Cloudy* clouds | cloud leads | small, opaque, asymmetric, two-tone base, mild weather only; no storm cloud and no friend who armours up |
| Cloudbabies | sky-caretaker preschool | ours is a character cloud on a hill, not babies on clouds |
| Pusheen / Molang-style loaves | the loaf silhouette | why M-A is not recommended |
| Ghost characters (Casper, Mario's Boo) | white dome + face | why M-C is not recommended; always a flat base |
| The poop emoji | a dome with a spiral peak | the curl hooks forward and never spirals upward |

---

## 3. Tekla

### 3.1 Three directions ([sheet](sketches/tekla_directions.svg))

| | T-A "Upright Builder" | T-B "Low Dome" | **T-C "Leaning Egg" (recommended)** |
| --- | --- | --- | --- |
| Construction | biped; banded plate worn on the back | naturalistic quadruped dome | semi-upright egg; three bands wrap her back from head shield to tail; walks on her hind feet |
| Armadillo read | medium | strongest | strong |
| Turtle risk | high (reads as a backpack or carapace) | medium (a low dome) | low (no separate shell; ears, snout, tail, stepped back) |
| Tools and folded arms | yes | no | yes |
| Deadpan face | yes | weak (profile, low in frame) | yes (3/4 face at head height) |
| The Curl | big transformation | natural | small, clean: egg → ball |
| Neighbours | Fuleco, Mighty (upright anthropomorphic armadillos) | real armadillo, pill bug | aardvark-type silhouettes (e.g. Arthur) at small sizes, answered by the stepped back and tail |

**Why T-C.** It's the only direction that keeps both halves of her: a real armadillo (bands, snout, ears, tail, the ball) and a small builder with free hands and a face at eye height that can play "I'm fine". Her head shield doubles as a hard hat.

### 3.2 Construction spec (T-C)

Units: **TH** = her standing height, ground to ear tips.

| Part | Spec |
| --- | --- |
| Body | Egg, 0.65 TH tall × 0.48 TH wide, tilted ~14° forward |
| Shell | Covers her back and shoulders. **Exactly three bands.** Two band lips make the back outline visibly step, so the shell reads in silhouette. Terracotta, with darker seams and a light edge under each seam. |
| Belly | Soft cream-tan front of the egg (where the apron sits) |
| Head | 0.29 TH wide, forward of the body axis; soft cream-tan |
| Snout | Long and tapering, ~0.29 TH forward of the head centre; a round dark nose tip |
| Head shield | A terracotta cap with a short brim over the eyes: her built-in **hard hat** |
| Ears | Funnel-shaped, upright in a V, ~0.3 TH above the head centre; pink inner ear |
| Eyes | Small, dark, **half-lidded** with a flat lid line; one highlight |
| Mouth | A short flat line under the snout |
| Arms | Short, with three-clawed paws; default pose is arms folded |
| Legs and feet | Short legs; big flat hind feet (~0.18 TH long) for quick steps and dead stops |
| Tail | Tapering cone, ~0.3 TH, two ring marks, terracotta |
| Apron | Teal carpenter's apron with **one big pocket**; a yellow folding ruler always pokes out of it |
| Ball (the Curl) | Diameter ~0.56 TH; three bands visible; head shield and tail cap meet at a front seam; **two ear tips peek out of the seam** |

### 3.3 The Curl, the Peek and the Roll

- **The Curl:** she tucks forward and the egg closes into a ball in 6–8 frames, ending on a small **click**, the sound of a closed book. The apron disappears inside the ball.
- **The Peek:** one half-lidded eye appears in the seam. Use rarely.
- **The Roll:** a tidy roll on flat ground with the bands visibly rotating, then a dead stop and uncurl. No spin blur, speed lines or spikes, so it can never read as a spin-dash. Never downhill on screen (imitable danger).

### 3.4 Designed neutral, tells and breaks ([sheet](sketches/tekla_tells.svg))

- **Neutral ("I'm fine."):** half-lidded eyes, flat small mouth, upright, arms folded, ears at attention. It is a deliberate, charming mask, not a blank face.
- **Tells** (her feelings live in behaviour): **the Straightening** (small, precise nudges to tidy things), **the Build**, **tap-tap** (mostly a sound), **the Curl**, **the Swish** (one small tail swish when truly happy; rare).
- **Year-one teaching order:** the Straightening, the Curl and "I'm fine" first. Layer in the Bow, tap-tap and the Swish. This answers the code-overload risk (`RSK-0005`).
- **Breaks are events:** the real laugh (head back, eyes closed, mouth open) and the terrible fake GASP (both paws up, round eyes). At most one break per episode.
- Her face moves less than Mulu's by design, but never too little to read. Head angle and eyelid angle carry the small shifts.

### 3.5 Builder identity without clutter

The apron with one pocket and one tool (the folding ruler) is the whole costume. Other tools live in the workshop and appear only when used. Her fingerprints are on the world instead: pegs, planks, string, picture-tags (see the [set plan](HILLTOP_SET_V0.3.md)).

### 3.6 A girl, without stereotyped accessories

She reads as a girl through her name, voice, pronoun and how others refer to her. There are no bows, eyelashes, lipstick, jewellery, skirts or pink coding. If testing shows a visual cue is wanted, use proportion (slightly rounder cheeks, a finer snout), never an accessory. Her competence, dry wit and pride are simply hers.

### 3.7 Nearest neighbours (armadillo, turtle, rolling)

Targeted search, not clearance (see `RES-0009`):

| Neighbour | What it is | Our divergence |
| --- | --- | --- |
| Mighty the Armadillo (Sega) | upright armadillo with a red shell, gloves and sneakers; spin moves | terracotta bands, no clothes except the apron, no spin-dash |
| Fuleco (FIFA 2014 mascot) | upright three-banded armadillo, amber fur, blue shell with a hex pattern, clothes | no hex pattern, no blue shell, not a sports mascot |
| *Pluto and the Armadillo* (Disney, 1943) | an armadillo mistaken for a ball | "mistaken for a ball" is never a signature gag |
| Turtle leads (e.g. Wonder Pets' Tuck, Franklin) | a rigid dome she hides inside | she has no carapace and never retracts; she rolls up |
| Aardvark-type silhouettes (e.g. Arthur) | upright, snout, ears | the stepped banded back, hard hat and cone tail |

Sources: [Fuleco](https://en.wikipedia.org/wiki/Fuleco) · [Mighty the Armadillo](https://sonic.fandom.com/wiki/Mighty_the_Armadillo) · [Pluto and the Armadillo](https://www.imdb.com/title/tt0036269/) · [Wild Kratts, "Shapes of the Armadillo"](https://www.wildkratts.com/where-to-watch-wild-kratts-shapes-of-the-armadillo/) · [Armadillo (Marvel)](https://en.wikipedia.org/wiki/Armadillo_(character)). Turtle and aardvark neighbours are from general knowledge. Desk-level only; not clearance.

---

## 4. The pair ([sheet](sketches/pair_tests.svg))

### 4.1 Scale and heights

| Measure | Value |
| --- | --- |
| Mulu body width | 0.9 TH (about twice her body width) |
| Mulu total height | ~0.85 TH: as tall as her, twice as wide |
| Talk height | Mulu's base at 0.45 TH; their eye lines meet |
| Float height | base at ~1.1 TH, clear of her ears (travel, shade) |
| Lookout height | the Lookout branch, ~4 TH: his ceiling |
| Her ball | ~0.56 TH diameter |

### 4.2 Contrast

- **Shape:** soft/wide/rising vs. crisp/narrow/pointed.
- **Value:** Mulu is the lightest thing in most frames; Tekla is a mid-dark warm.
- **Temperature:** Mulu cream with a cool underside; Tekla terracotta and teal.
- **Placement:** Mulu floats; Tekla is grounded. They are never at the same height unless at talk height.

### 4.3 Designed contact set

Only these in standard shots: **the Cloud Hat** (Mulu settles on her ball, sinking ~0.1 TH, her ear tips visible), **the teacup handover** (nub to paw), **rain rolling off her shell**, and **shade** (float height above her). Everything else (her leaning into him, carrying, hugging) is showcase-only. P1-15's lean is flagged for the benchmark.

### 4.4 Staging rules

- **Sky contrast:** stage Mulu against the hill, the tree, the knoll or a saturated sky, never pale sky near the horizon (see the [master wide](sketches/hilltop_master_wide.svg), where he's composed against the knoll).
- **Eye lines:** use talk height for any exchange of looks.
- **One focal action per shot.** If both act, stage them one after the other.

### 4.5 Thumbnail findings (honest)

- Side by side, the pair reads instantly at 96, 64 and 48 px: two unmistakably different shapes.
- **The Cloud Hat is the weakest pair silhouette at 48 px** (a lump on a ball). As a logo it needs a slight 3/4 angle so the bands show, Mulu sitting a little higher, or colour. Test it separately in Round 1.
- Mulu's mood survives in silhouette through the Top Puff. Tekla's survives through posture (the Bow and the Curl read; subtle tells do not, which is expected).

---

## 5. Movement and acting rules

Mulu **drifts**; Tekla **ticks**. Timings are at 24 fps and are starting points for the animatic.

| | Mulu | Tekla |
| --- | --- | --- |
| Idle | continuous bob, 1.5–2 s cycle, ~2% of body height; never fully still | fully still, upright, arms folded |
| Travel | ease in over 6–8 frames, drift, overshoot 4–6, settle | quick small steps (~6 frames each), **dead stop, no overshoot** |
| Turn | whole-body rotation, 6–10 frames; the Top Puff lags 2 frames | head first (4 frames), then body (6) |
| Joy | the happy spin, 12–16 frames per turn | the Swish, 8 frames, rare |
| Embarrassment | drifts backward, pink tint, plips | the Tiny Bow: 10–12 frames down, 6 hold, 8 up |
| Overwhelm | goes still and tucked (scared) or hovers too close (worried) | the Curl: 6–8 frames + click; uncurl 8–10 |
| Trying to be still | a 2-frame jitter at ~1% amplitude | n/a |
| True stillness | P2-14 only: no bob at all. Rare, and it means love. | her default |

**Comedy timing for 4–6-year-olds:** add ~6–12 frames to every reaction hold compared with adult comedy. The "I'm fine" beat: impact → hold 18–24 frames → line → 6 frames → the Straightening.

---

## 6. Colour and look directions

### 6.1 Palette options

| | P-1 "Sunny Clay" (recommended to explore first) | P-2 "Storybook Pastel" | P-3 "Bold Graphic" |
| --- | --- | --- | --- |
| Mulu | warm cream `#FFF7E8`, cool underside `#D2DEEF`, slate outline `#34405E` | white, pale blue shade | pure white, thick navy outline |
| Tekla | terracotta `#C9643E` bands, cream-tan skin `#F1D4AF`, teal apron `#2E7F86`, yellow ruler `#F2C230` | dusty peach shell, sage apron | mustard-ochre shell, cobalt apron |
| World | sky `#9BD3F3`, hill `#8DC462`, red umbrella `#E8584A` | pale sky, soft sage | cobalt sky, saturated green |
| Strength | warm, distinct, good phone contrast | gentle, "bedtime" | toys, print and thumbnails |
| Risk | the terracotta must not go brown in shade | **pale-on-pale: Mulu disappears** | generic flat-vector look; harsh |

### 6.2 Look options (rendering style, not renderer)

| | L-1 Clean 2D | L-2 Soft 3D toy | L-3 Textured storybook 2D |
| --- | --- | --- | --- |
| Description | flat colour, clean outline, one-tone soft shading (as in the sketches) | Mulu matte like felt or marshmallow; Tekla like glazed clay; a fabric apron | gouache or crayon texture |
| Consistency | highest | high with rigs; medium with generation | lowest (texture boil) |
| Toys and books | easy | strongest toy read | books |
| Risk | can look plain | "generic AI 3D cute" unless materials are specific | cost and flicker |

**Recommendation:** generate Round 1 in **L-1 and L-2**, compare side by side, and drop L-3 unless both look generic. The look decision comes from images, not this document.

---

## 7. Readability and drift checklist

Use on every generated or drawn batch. **D-codes are logged per shot in the benchmark.**

| Code | Failure |
| --- | --- |
| D01 | Mulu proportion drift (body height, Top Puff size, shoulder puff size) |
| D02 | Puff count wrong (≠ 1 Top Puff, ≠ 1 shoulder puff; extra bumps) |
| D03 | Top Puff detached, floating, or merged away (outside the tucked pose) |
| D04 | Top Puff on the wrong side (mirror flip) |
| D05 | Face placement drift (eyes too high or low, off the face field) |
| D06 | Nubs missing, extra, or grown into hands |
| D07 | Translucency, mist, wisps, fog or feathered vapour edges |
| D08 | Rain from the wrong place (sides, top, eyes as tears), except the designed side-drip |
| D09 | Rain-style drift (streaks, spray, non-teardrop drops, storm density) |
| D10 | Wind drift (volumetric air, dust clouds, tornadoes; > 3 reacting objects in a standard shot) |
| D11 | Tekla band count ≠ 3; hex scutes; a separate carapace (turtle drift) |
| D12 | Tekla retracting her head or limbs into a shell |
| D13 | Tekla wet |
| D14 | Stereotyped-accessory drift (bows, lashes, pink coding, jewellery) |
| D15 | Apron, pocket or ruler missing or changed |
| D16 | Pair scale drift (Mulu width vs. TH) |
| D17 | Tint or edge state that doesn't match the beat's feeling |
| D18 | Prop state or position mismatch against the shot manifest |
| D19 | Text in the world (letters, words); pictograms only |
| D20 | Unplanned characters, especially grown-ups (offscreen by decision) |

**Thumbnail rule:** test every state and the pair at **128, 64 and 48 px**. If a four-year-old needs colour to name them, the silhouette fails.

## 8. What the visual-generation round must produce and decide

See the [generation package](GENERATION_PACKAGE_V0.3.md) for prompts, the reference board and the review rubric.

1. **Round 1, exploration:** M-B (plus M-A and M-C as controls), T-C (plus T-A and T-B), the pair lineup and the Cloud Hat, in L-1 and L-2, in P-1. **Owner picks:** one Mulu, one Tekla, one look.
2. **Round 2, model-sheet candidates:** turnarounds, the expression and state sheets, the weather-code sheet, the tells sheet, and a Hilltop master-wide paintover.
3. **Round 3:** the [benchmark-grade reference package](../06_production/BENCHMARK_REFERENCE_PACKAGE_V0.3.md).

## 9. Self-review

| Question | Answer |
| --- | --- |
| Would a four-year-old recognise the two leads instantly? | In silhouette, yes: a lopsided cloud and a long-eared, snouted, banded critter. The Cloud Hat needs work at 48 px (§4.5). |
| Do they look different from generic AI children's characters? | On paper, yes: the asymmetric Top Puff, the shoulder puff and the underside band; the hard-hat shield, stepped bands and apron. **The real test is Round 1**, where the rubric scores "generic-AI look" explicitly. |
| Is the pair appealing before any story is explained? | The sketches suggest so: soft and crisp, big and small, happy face and deadpan face. The owner should judge Round 1 images, not these sketches. |
| Did production constraints help or sterilise? | They helped: the flat base is his rain source *and* his silhouette; the waterproof shell is the thesis image *and* a continuity saving; enumerated states give Mulu readable acting. |
