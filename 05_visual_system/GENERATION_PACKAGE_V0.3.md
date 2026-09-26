# Visual Generation Package v0.3

**Status: READY-TO-USE BRIEFING FOR THE NEXT PHASE. NOTHING HAS BEEN GENERATED.** Proposed under `PROP-0008`. It is tool-agnostic: the prompts are written for any image generator *and* for a human illustrator. **Choosing a generation tool, any spend, and storing generated images in the repository are owner decisions** (see §1). No output may be published.

> **Round 01 update (2026-09-26, `RES-0010` / `PROP-0009`):** Round 1 exploration ran (six images, Gemini tool family, stored in the owner's local asset workspace outside the repository) and is reviewed in [ROUND_01_REVIEW_AND_SELECTION.md](ROUND_01_REVIEW_AND_SELECTION.md). The next generation action is the bounded **Round 1.5 refinement pass** defined in the [3D benchmark reference brief](../06_production/BENCHMARK_3D_REFERENCE_PACKAGE_V0.4.md), then the owner's formal picks. The prompts and rubric below remain the working toolkit; the provenance log (§8) is mandatory from Round 1.5 onward.

Design source: [visual development package](VISUAL_DEVELOPMENT_V0.3.md) · [Hilltop set plan](HILLTOP_SET_V0.3.md) · construction sketches in [`sketches/`](sketches/mulu_silhouette_families.svg).

## 1. Gates before generating

| Gate | Rule |
| --- | --- |
| Tool | The owner picks the exploration tool (or an illustrator). Picking an exploration tool is **not** a renderer decision; the benchmark still decides production. |
| Spend | No subscription or purchase without explicit owner approval and a limit. |
| Rights | Use only tools whose terms allow commercial use of outputs; record the terms per batch (§8). |
| Safety | Every batch is reviewed for scary, uncanny or inappropriate content before anyone else sees it. |
| Storage | `AGENTS.md` keeps visual assets out of the foundation phase. Before committing any image, the owner decides where exploration images live (suggested: a curated `05_visual_system/exploration/round_01/` of selected images only, each with its provenance record). |
| Originality | No other studio's characters as inputs, and no "in the style of" named artists, studios or shows. |

## 2. Rounds

1. **Round 1, exploration** (G-01 to G-06, G-09 to G-11, in looks L-1 and L-2). About 8–16 candidates per sheet; keep the best 2–3. **Owner picks:** Mulu family, Tekla direction, look.
2. **Round 2, model-sheet candidates** (G-02 to G-05, G-07, G-08, G-12, G-13) in the chosen look only.
3. **Round 3, the benchmark-grade reference package** ([spec](../06_production/BENCHMARK_REFERENCE_PACKAGE_V0.3.md)): the Round 2 winners cleaned up and made consistent.

**Use the sketches as structure.** If the tool accepts a structure, edge or silhouette image, export the relevant SVG to PNG and use it at moderate strength to enforce proportions (the Top Puff side, band count, scale). If not, attach it as a reference image with the words "match these proportions".

## 3. Style blocks (prepend one)

**L-1 Clean 2D**
> 2D children's animation character design, flat colour with one soft shade tone, clean continuous outlines of even weight in deep slate blue, simple readable shapes, warm gentle palette, plain light cream background, preschool television quality, no texture.

**L-2 Soft 3D toy**
> Stylised 3D children's animation character with simple toy-like shapes and specific materials (see the character block), soft studio light, plain light cream background, preschool television quality, not photorealistic.

## 4. Character blocks

### Mulu, M-B "Cumulus" (recommended)
> A small cloud character built from a few soft shapes. A wide, low, soft body with a **perfectly flat bottom**. Rising from the top over his right side, **one tall round puff** about half the body's width, like a cumulus tower, with **one small hooked curl** on top that hooks forward. On the other shoulder, **one small round puff**. Two small round stub arms at the lower sides, no fingers. Opaque warm-cream body with one clean continuous outline; a soft cool blue-grey band along the flat underside. Face low on the front of the body: two dark vertical oval eyes with one white highlight each, short thick separate eyebrows, a small simple mouth. Matte and solid, like felt or a marshmallow. Friendly, bouncy, about five years old in spirit.
>
> *L-2 materials:* matte felt or marshmallow surface, very fine texture, no shine.

**Never (negative list):** three-bump cloud, cloud emoji shape, symmetric cloud, fog, mist, wisps, translucent or glowing vapour, lightning, storm, tears, ghost, wavy bottom edge, sheep, wool, cotton-ball texture, soft-serve swirl, spiral peak, pupils with irises, eyelashes, teeth, hands with fingers, legs, blue or pink body, rainbow, text, letters, logo, watermark.

**Controls (Round 1 only):**
- *M-A "Pillow":* a wide rounded marshmallow-loaf body with a flat bottom, small round puffs at the two lower corners, one small curl centred on top, the same face.
- *M-C "Scoop":* a tall rounded dome with a flat bottom, two small cheek puffs at the lower sides, a small round top-knot with a forward-hooking curl, the same face.

### Tekla, T-C "Leaning Egg" (recommended)
> A small armadillo-inspired girl character, semi-upright like a leaning egg, standing on her hind feet. Her back and shoulders are covered by a terracotta shell made of **exactly three wide bands** with visible seams; the bands make small steps along her back outline. On her head, a terracotta **head shield like a little hard hat** with a short brim over her eyes. A long tapering snout with a round dark nose tip; two tall funnel-shaped ears upright in a V; small **half-lidded** dark eyes with a flat lid line; a short flat mouth. Calm, dry, deadpan, quietly proud. Cream-tan face, belly, arms and feet. Short arms folded across her chest, three small claws on each paw, big flat hind feet, a tapering cone-shaped tail with two rings. She wears a **teal carpenter's apron with one big front pocket** and a yellow folding ruler poking out of it. Crisp, neat shapes.
>
> *L-2 materials:* the shell softly glazed like fired clay; the apron in woven canvas; skin matte.

**Never:** turtle, tortoise, hexagonal plates or scutes, a separate shell or carapace, head or limbs pulled into a shell, pangolin scales, spikes, hedgehog, rabbit, kangaroo, bow, ribbon, eyelashes, lipstick, jewellery, dress, skirt, pink or blue shell, sneakers, gloves, shirt, sports kit, mean or angry face, realistic fur, text, letters, logo, watermark.

**Controls (Round 1 only):**
- *T-A "Upright Builder":* the same character standing fully upright like a small person, the banded shell worn on her back like a plate.
- *T-B "Low Dome":* the same character as a four-legged armadillo with a banded dome body, a small side pouch instead of an apron.

## 5. Sheet prompts

Append these to a style block + character block(s).

| ID | Sheet | Prompt addition | Round |
| --- | --- | --- | --- |
| G-01 | Mulu family exploration | "single character, front view, neutral happy expression, full body, centred" (run M-B, M-A, M-C separately) | 1 |
| G-02 | Mulu turnaround | "character turnaround: front, three-quarter, side, back, same size, aligned on one baseline; the tall puff is always over his own right side (left side of the image in the front view)" | 1–2 |
| G-03 | Mulu expressions | "expression sheet, same body: neutral, happy, excited, sad, secretive glance, embarrassed, frustrated, scared, calm eyes closed, proud, holding his breath with puffed cheeks, shocked" | 2 |
| G-04 | Mulu weather code | "eight small poses, each with its weather: warm breeze swirl lines; skittery gust lines; sad drizzle of small teardrops falling straight down from his flat bottom; one single drop from one spot; two fat slow drops with a pink blush; one short huff line from the mouth; no weather and tucked small; a thin column of drops onto one seedling". Drops always fall straight down from the flat bottom. | 1–2 |
| G-05 | Mulu Top Puff and capacity | "the tall puff in five poses: upright, perked, leaning forward, drooped to the side like a wilted ear, tucked small into the body; plus plump, normal and thin versions" | 2 |
| G-06 | Tekla exploration | "single character, three-quarter view facing right, arms folded, full body" (run T-C, T-A, T-B separately) | 1 |
| G-07 | Tekla turnaround | "turnaround: front, three-quarter, side, back; exactly three shell bands in every view" | 2 |
| G-08 | Tekla tells | "same character: arms folded deadpan; nudging a teacup straight with one claw; a tiny dignified bow; tapping claws; one small tail swish; curled into a perfect banded ball with two ear tips peeking from the seam; one half-lidded eye peeking from the ball's seam; rolling on flat ground as a tidy ball; a real laugh with head back; a huge fake surprised gasp with both paws up" | 2 |
| G-09 | Pair lineup | "both characters side by side, the cloud floating so their eyes are level; the cloud is twice as wide as her body and about as tall as her including ears" | 1 |
| G-10 | Cloud Hat | "she is curled into a banded ball; the cloud rests on top of her like a soft hat, sinking slightly; her two ear tips peek out of the ball's side seam; three versions: side view, slight three-quarter, slightly from above" | 1 |
| G-11 | Rain off the shell | "the cloud drizzles small teardrops onto her shell; the drops bead and roll off the bands; she stays completely dry and looks at a rolling drop" | 1 |
| G-12 | Hilltop master wide | "children's animation background, a soft rolling green hilltop plateau; upstage centre a grassy knoll with a round wooden plank door; planted on the knoll's roof, an upturned red umbrella on a wooden post like a bowl-shaped flower; a small two-square chalkboard on legs right of the door; handmade wind chimes (spoons, shells, a pebble) on a crooked post left of the door; an old round-canopied tree with one long branch at the left edge; a plank bench and a pegged ladder-back chair facing the valley at the right; a vegetable garden with a red pinwheel on the right slope; a blue stream at the foot; distant village rooftops only; no people; no text" (then HT-02 front/reverse and HT-03 per the [set plan](HILLTOP_SET_V0.3.md)) | 2 |
| G-13 | Prop sheet | "prop sheet: the umbrella bed (on post; carried bowl-up; tipped), the two-square chalkboard with chalk sun, drizzle, gusts, single drop, two fat drops, question mark, the wind chimes (loose parts, wrapped in a big leaf, hung), teapot, two teacups and a long straw, a teal carpenter's apron with a yellow folding ruler, an old pegged ladder-back chair and its identical twin, a long wooden shelf with small souvenirs" | 2 |
| G-14 | Thumbnail board | not generated: compose selected outputs as black silhouettes at 128, 64 and 48 px | 1–2 |

## 6. Reference boards

**Inspiration board (store links and a one-line note, not copies):**

- real cumulus clouds with flat bases and single towers;
- three-banded armadillos: the ball, the band count, ears and snout;
- handmade woodwork, pegged furniture, carpenter's aprons, chalkboards;
- rolling hilltops with a single tree; cottage-garden rows;
- folk-craft wind chimes from spoons and shells;
- simple pictogram signage.

**Rules:** no animated characters on the inspiration board. Keep a separate **"AVOID" board** of the neighbours in [§2.9 and §3.7](VISUAL_DEVELOPMENT_V0.3.md#29-nearest-neighbours-cloud), labelled as avoid-only, and never use it as a generation input. Record source and rights for anything kept ([reference image rules](REFERENCE_IMAGE_RULES.md)).

## 7. Review rubric (score 0 / 1 / 2)

| Criterion | 2 = |
| --- | --- |
| Cloud read (Mulu) | reads as a cloud in colour and in silhouette |
| Spec match (Mulu) | one Top Puff on his right, one shoulder puff, flat base, two nubs, face low |
| Armadillo read (Tekla) | reads as an armadillo, not a turtle, rabbit or aardvark |
| Spec match (Tekla) | three bands, hard-hat shield, ears, snout, cone tail, apron + pocket + ruler |
| Face appeal | a four-year-old would want to hug or copy the face |
| Emotion legibility | the intended feeling reads at 128 px |
| **Not generic** | would *not* be mistaken for a random AI children's character (inverted: 2 = distinctive) |
| Pair contrast | soft/wide vs. crisp/narrow is obvious |
| Thumbnail | both nameable at 48 px as silhouettes |
| Drift | zero D-codes ([checklist](VISUAL_DEVELOPMENT_V0.3.md#7-readability-and-drift-checklist)) |
| Childhood gate | nothing scary, uncanny, mean or inappropriate |

A candidate advances only with ≥ 16/22, a 2 on "Not generic", and 0 on childhood-gate problems.

## 8. Provenance log (one row per batch)

`batch_id` · date · round · sheet (G-xx) · look (L-1/L-2) · tool + version + model · settings · seed(s) · full prompt · negative list · control/reference inputs · human edits · reviewer · rubric scores · D-codes · selected (yes/no) · terms and rights note · safety check result.

Keep the log beside the images; add an `ASSET_REGISTRY.json` entry only for owner-approved references ([consistency rules](CONSISTENCY_RULES.md)).
