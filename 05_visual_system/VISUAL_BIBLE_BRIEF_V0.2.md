# Visual Bible Brief v0.2 — What the Visual Bible Must Solve

**Status: DESIGN BRIEF FOR A FUTURE PHASE. NO ARTWORK, NO APPROVED DESIGN.** Written under `DEC-0018`, part of `PROP-0007`. This brief defines the *problems* the later Visual Bible must solve. It doesn't solve them. Final character design, model sheets, palette and style lock all require owner approval. Character details come from the [Show Bible v0.2 draft](../01_show_bible/SHOW_BIBLE_V0.2_DEVELOPMENT.md). The requirements build on [Red-Team Review 001 §14](../03_research/RED_TEAM/INDEPENDENT_RED_TEAM_001.md).

**Update:** the concrete design directions answering this brief are in [Visual Development v0.3](VISUAL_DEVELOPMENT_V0.3.md) (`PROP-0008`). The brief below is kept as written.

## 0. The one-sentence goal

**A child should be able to recognize Mulu and Tekla as black silhouettes at thumbnail size, read Mulu's feeling from his weather and Tekla's feeling from her behavior, and never mistake either of them for somebody else's cloud or armadillo.**

## 1. Silhouette contrast

- **Mulu:** a wide, soft **dome top with a flat base**, like a loaf or a marshmallow. Real cumulus clouds have flat bases, and his flat base is also where rain comes from. One signature top tuft or curl anchors identity. Deliverable: prove he doesn't read as the generic three-bump cloud icon.
- **Tekla:** a compact, low **banded dome on quick legs**. It needs a clear head/snout, ears and a tail so she reads as a *creature* rather than a shell.
- **The curled state:** Tekla curled must be a near-perfect ball with visible bands. It's a second silhouette that is still unmistakably her.
- **Pair test:** the pair side by side, the Cloud Hat (Mulu resting on curled Tekla), and Mulu hovering above Tekla must each read as a single iconic shape.
- **Divergence deliverable:** a one-page comparison against nearest neighbors (Cloudbabies, Middlemost Post's Parker J. Cloud, Partly Cloudy's clouds, common armadillo and turtle characters, Wonder Pets' Tuck), with written design rationale. Designs must come from written decisions, not "cute cloud" prompts.

## 2. Scale relationship

- **Mulu:** about 1.5–2× Tekla's body width. He hovers at "friend height," with his eyes level with hers when he dips low.
- **Tekla:** small enough that the bench, the chair and tools read as big projects for her.
- **Maximum heights:** Mulu's ceiling is the Lookout branch (world rule). Define his three standard hover heights: *talk height*, *float height* and *Lookout height*.
- **The world:** everyday objects (teapot, umbrella, kite) are scaled so both characters can plausibly interact with them.

## 3. Shape language

The bouba/kiki contrast is the design premise, and the names echo it.

- **Mulu: circles and soft ovals.** No corners, generous curves, puffs.
- **Tekla: segmented arcs, a dome and small triangles** (ears, snout, tail tip). Crisp, neat and engineered.
- **World:** a soft rolling hill with Tekla-built crisp objects on it, so her fingerprints are visible everywhere (the bench, the Forecast Board, the umbrella post).
- **Props:** hers are geometric and handmade (pegs, planks, string); his are round, found objects (a teacup, shells, spoons).

## 4. Movement personality

Document these as rules, with a reference animation for each.

| | Mulu ("drifts") | Tekla ("ticks") |
| --- | --- | --- |
| Idle | continuous gentle bob, never fully still | fully still, upright, arms folded |
| Travel | drift with ease-in, overshoot and settle | quick small steps, dead stop; the **Roll** for speed or escape |
| Turning | whole-body rotation (no neck) | head first, then body, precise |
| Joy | the happy spin; rising | the tail **Swish** (rare, small) |
| Embarrassment | drifts backward, pink tint | the **Tiny Bow** |
| Overwhelm | goes still (fear) or rises too close (worry) | the **Curl** into a ball |
| Trying to be still | visible vibration | n/a (stillness is her default) |

**Squash and stretch:** Mulu may squash, stretch and squeeze (for example, through a seatbelt) but **always returns exactly to model within the shot**. Tekla's shell never deforms; her flexibility is in her limbs and the Curl.

## 5. Facial and expression grammar

- **Mulu: full-range face.** Large eyes, expressive brows and a mouth that carries every feeling at readable size. Body acting amplifies it (tint, puffiness, droop, edge ruffle). This counts as acting, not power (Show Bible Rule 2).
- **Tekla: a designed neutral.** Her default "I'm fine" face is a deliberate, charming mask. **Her feelings live mostly outside her face**: straightening, building, tap-tap, the Curl, the Swish. Her face moves *less* than his by design, and the few times it breaks (the real laugh, the terrible fake "GASP!") are events.
- **Expression sheet deliverables:** Mulu's eight weather-code states (Show Bible §12.2), each paired with its face and body state; Tekla's neutral plus her five tells; and three "break" expressions for her.
- **Acting-range requirement:** state what must be readable at phone size before any rig or model decision, so the rig is built for the acting and not the other way round.

## 6. Cloud-body rules (the hardest continuity problem)

The Visual Bible must lock what **never** changes, so that change reads as expression and never as error:

1. **Opaque "soft-solid" body** with a clean outline. No translucency changes and no volumetric vapor.
2. **Fixed silhouette:** dome top, flat base, one top tuft, fixed lobe count.
3. **Fixed face placement** and fixed arm-nub placement (two small nubs, always present).
4. **Three puffiness states only:** full, normal and wisp-thin (the capacity cost, Rule 5).
5. **Three tints only:** normal, pink (embarrassed) and grey (sad).
6. **Two edge states only:** smooth (calm) and ruffled (upset or excited).
7. **Rain leaves only from the flat base:** discrete, countable, stylized drops that fall straight down.
8. **Wind is shown as stylized swirl lines plus object response.** The swirl style is a signature design element.
9. **No shape-shifting,** no growth, no splitting, no fog.

Deliverables: a turnaround; a state chart covering capacity × tint × edge; a rain/drip style sheet (drip, side-drip, drizzle, happy rain, embarrassed "plips"); a wind swirl sheet (breeze, gust, huff, giggle-puff); and "error vs. expression" examples.

## 7. Readability at thumbnail size

- Test every character state, and the pair, at **64 px and 128 px** high.
- **Sky-contrast rule:** Mulu must never disappear against the sky. Define a guaranteed value and color separation, for example a warm cream body with a cool shadow base and outline over saturated or warm skies, never a pale-on-pale sky. Staging should place him against hill, tree or deep sky whenever possible.
- **Tekla against the ground:** a warm shell against green and earth, with its own separation rule.
- **Weather code at small size:** the drip, the drizzle and a gust must each be distinguishable in a thumbnail.

## 8. Simple reusable environment

- **Hilltop hub** designed as a set: Tekla's burrow door, the Forecast Board, the wind chimes, the umbrella bed on its post, the bench and the valley view. Define **six standard camera setups** (wide establishing, bench two-shot, door medium, Forecast Board insert, Lookout down-angle, garden edge) that cover most scenes.
- **Secondary sets:** Garden, Workshop interior (with the Keep Shelf), Stream bend and stepping stones, Lookout Tree.
- **Seasons as variants:** color scripts and swappable seasonal dressing (blossom, summer, autumn leaves, bare branches) rather than new sets.
- **Standard lighting states:** morning, day, golden hour. Night is a showcase variant.
- **Text-free world:** all signage, labels and letters as pictograms. The Visual Bible defines the pictogram set, including the Forecast Board symbols.

## 9. Recognizable props (design once, reuse forever)

| Prop | Owner | Notes |
| --- | --- | --- |
| Umbrella bed (upturned umbrella on a post) | Mulu | Icon. Open/closed and full/empty states. |
| Forecast Board (two squares, chalk symbols) | shared | Symbol set: sun, drizzle, gusts, single drop, pink "plips", question mark; the empty second square. |
| Wind chimes (spoons, shells, pebble) | shared | Must read as handmade; sound design partner. |
| Tool apron with one big pocket | Tekla | Fixed pocket contents silhouette. |
| Teacups, teapot, long straw | shared | The refill ritual. |
| Pinwheel on a garden stake | Garden | Background wind tell. |
| Picture-tags (Tekla's labels) | Tekla | Pictogram style, no words. |
| The Snail (with the dot Tekla painted on its shell) | world | Must be findable in wides at small size. |
| Paper boats | world | Delivery system from Somebody Downstream. |
| The Keep Shelf | Tekla | Grows by one item per episode; continuity-tracked. |

## 10. Production consistency requirements

- **Versioned reference package:** turnarounds, expression and state sheets, prop sheets, set plans, color scripts and a pictogram set. Record each in `ASSET_REGISTRY.json` with its approval status only after owner approval ([consistency rules](CONSISTENCY_RULES.md), [reference image rules](REFERENCE_IMAGE_RULES.md)).
- **State metadata as first-class data:** Mulu's capacity, tint and edge state; wet patches and their scene lifetime; the Snail's position; the Keep Shelf contents. Record these per shot in the episode manifest, not left to memory.
- **Drift checks:** a named checklist of known failure modes, whatever the method: silhouette drift, face-position drift, lobe-count drift, tint mismatch, drops falling from the wrong place, Tekla appearing wet, prop disappearance, scale drift between the pair.
- **Anti-convergence review:** every design iteration is compared against the neighbor board (§1) before approval.

## 11. What the Visual Bible phase should deliver (proposed scope)

1. Three divergent silhouette explorations for each character, plus the pair, with neighbor divergence notes.
2. One owner-selected direction developed into turnarounds and the full state and expression sheets.
3. The Hilltop hub set plan with six camera setups, and one color script.
4. The prop sheet (§9) and the pictogram set.
5. A thumbnail readability test board (§7).
6. A short **visual feasibility handoff** to the production benchmark: the exact reference package the benchmark will test against.

**Not in scope:** final artwork for publication, merchandise design, renderer or tool selection.
