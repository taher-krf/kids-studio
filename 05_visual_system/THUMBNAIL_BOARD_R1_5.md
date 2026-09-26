# Thumbnail board R1.5 (G-14 / R1.5-09) — 128 / 64 / 48 px readability

**Status: DEVELOPMENT TEST RECORD. LOCAL TEST ARTIFACTS ONLY — NO IMAGE BYTES IN THE REPOSITORY.** Produced 2026-09-26 from the owner-confirmed Round 1.5 development baselines (`DEC-0020`; register: [ROUND_1_5_BASELINE_MANIFEST.json](ROUND_1_5_BASELINE_MANIFEST.json)). Fills the Round 1.5 thumbnail-board item (R1.5-09) of the [3D benchmark reference brief](../06_production/BENCHMARK_3D_REFERENCE_PACKAGE_V0.4.md) and the G-14 thumbnail test of the [generation package](GENERATION_PACKAGE_V0.3.md).

## 1. Artifacts and method

The board images live in the owner's local asset workspace, not in the repository (image-storage practice per `RSK-0006` item 8):

`C:\Users\PC\Documents\GitHub\Kids Studio Assets\Visual Development\Round 01\_tests\`
- `R15_THUMBNAIL_BOARD_SILHOUETTE.png` — black silhouettes at 128 / 64 / 48 px
- `R15_THUMBNAIL_BOARD_COLOUR.png` — colour downscales of the same crops at 128 / 64 / 48 px

Generator: [`scripts/build_thumbnail_board.py`](../scripts/build_thumbnail_board.py) (dev-only local tool; requires Pillow; not part of the stdlib validation/export toolchain, `DEC-0009` unchanged). Re-run to reproduce. The master images were not modified.

**Method:** crop hint per subject → per-row background estimation (median of the edge columns) → border flood-fill segmentation (background = everything reachable from the frame edge within a per-subject colour tolerance) → keep components ≥ 8% of the largest → bounding-box crop → render at 128 / 64 / 48 px (LANCZOS), displayed at a uniform 128 px cell with NEAREST so relative pixelation stays honest.

## 2. Limitations (recorded, not papered over)

1. **Cream-on-cream segmentation is near the noise floor.** Mulu's warm-cream body against the light-cream studio background separates by only ~9–11 RGB units; a plain distance threshold fails (hollow masks) and even flood-fill needs a tolerance of ~8. His top edge is slightly lumpy in the mask.
2. **The Pair silhouette includes Mulu's cast shadow** (the soft ellipse beneath him is darker than the background and survives segmentation). It inflates his ground footprint in that row only.
3. Segmentation is stdlib/Pillow tooling, not a matte tool. For a publication-grade G-14 board, re-render silhouettes from a future 3D scene or have the image tool produce "black silhouette on white" variants; treat this board as the development-level answer.
4. Single-reviewer judgment; no child testing (`RSK-0002`, `RSK-0005` stand).

## 3. Findings (silhouette board)

| Subject | 128 px | 64 px | 48 px | Notes |
| --- | --- | --- | --- | --- |
| Mulu | reads | reads | **reads** | flat base + asymmetric puffs + tall Top Puff survive; the curl merges into the puff at 48 px (expected); Top Puff side visible in silhouette |
| Tekla | reads | reads | **reads, with the known caveat** | instantly a compact eared critter; at 48 px the tall ears dominate and the read neighbours rabbit/aardvark more than armadillo — the `RSK-0006` item 4 / R-T5 watch item is **confirmed visible in the 3D master**, not yet a failure (stepped banded back and snout still separate her from a rabbit in colour) |
| Pair | reads | reads | **reads** | instant two-character contrast (wide/soft/low vs. narrow/crisp/upright); shadow artifact noted above |
| Cloud Hat | reads | reads | **weakest (open)** | reads as *one* merged figure with a wide soft cap; "a hat that is a friend" needs colour or the slight 3/4 treatment. This **confirms, not closes**, `RSK-0006` item 1 (the Cloud Hat is the weakest pair silhouette at 48 px) |

**Colour board:** all four subjects are clearly nameable at all three sizes in colour, including 48 px (cream cloud + tall puff; terracotta + teal apron; two-tone pair; cloud-on-critter stack).

## 4. Verdict against R1.5-09 acceptance

Acceptance text: "both leads nameable as silhouettes at 48 px."

- Mulu at 48 px: **pass**.
- Tekla at 48 px: **pass** (nameable as herself against the cast; armadillo-specific read is weak — logged as a watch item for Round 2 turnarounds).
- **R1.5-09: COMPLETE with documented limitations.** The Cloud Hat 48 px weakness is a standing, already-recorded risk (`RSK-0006` item 1) — this board provides its first render-level evidence and keeps it open. Repeat the board from Round 2 model sheets (and from the curled-ball Cloud Hat variant when produced) before any style lock.

## 5. Follow-ups

- Round 2: re-run this script against the turnaround masters; add the curled-ball Cloud Hat and rain-off-shell subjects.
- If a cleaner matte is wanted, budget one Gemini edit pass ("same character as a flat black silhouette on a plain white background") per master — owner decision, no spend assumed.
- V-01–V-05 smoke-test clips should be spot-checked at 48 px for the same readability (see [video smoke test package](../06_production/VIDEO_SMOKE_TEST_PACKAGE_V0.1.md)).
