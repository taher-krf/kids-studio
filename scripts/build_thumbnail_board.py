#!/usr/bin/env python3
"""Build the Round 1.5 silhouette-readability thumbnail board (G-14 / R1.5-09).

DEV-ONLY LOCAL TOOL. Requires Pillow (NOT part of the stdlib validation/export
toolchain pinned by DEC-0009; nothing in CI, validation or export imports this).
Reads the owner-confirmed Round 1.5 masters from the owner's LOCAL asset
workspace and writes test boards back there. No image bytes enter the repo.

Method (documented in 05_visual_system/THUMBNAIL_BOARD_R1_5.md):
per-row background estimation (median of edge columns), border flood-fill
segmentation (background = everything reachable from the frame edge within a
colour tolerance), connected-component filter, bounding-box crop, black
silhouette rendered at 128/64/48 px. Cream-on-cream subjects (Mulu) sit near
the segmentation noise floor, so tolerances are per subject and the output
must be eyeballed.
"""
import sys
from collections import deque
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFilter
except ImportError:
    sys.exit('Pillow required (pip install --user pillow). Dev-only tool; see docstring.')

ASSET_ROOT = Path(r'C:\Users\PC\Documents\GitHub\Kids Studio Assets\Visual Development\Round 01')
OUT_DIR = ASSET_ROOT / '_tests'
SIZES = (128, 64, 48)
WORK_W = 800  # working width for masking

# file, crop hint (original px, excludes shadows), flood-fill tolerance
SUBJECTS = [
    ('Mulu', 'Mulu/R1.5_MULU_3D_MASTER.jfif', (350, 60, 2450, 1295), 8),
    ('Tekla', 'Tekla/R1.5_TEKLA_3D_MASTER.jfif', (820, 110, 1700, 1400), 30),
    ('Pair', 'Pair/R1.5_PAIR_3D_BASELINE.jfif', (380, 240, 2400, 1420), 12),
    ('Cloud Hat', 'Pair/R1.5_CLOUD_HAT_3D.jfif', (860, 60, 1920, 1420), 12),
]


def row_background(im):
    """Per-row background estimate: median of the outer 8 columns each side."""
    w, h = im.size
    px = im.load()
    bg = []
    for y in range(h):
        samples = [px[x, y] for x in list(range(8)) + list(range(w - 8, w))]
        bg.append(tuple(sorted(c[i] for c in samples)[len(samples) // 2] for i in range(3)))
    return bg


def mask_subject(im, thr):
    """Flood-fill from the borders: anything the background cannot reach is subject.

    Robust for cream-on-cream subjects (Mulu), whose interior matches the
    background colour and breaks naive distance thresholds.
    """
    w, h = im.size
    px = im.load()
    bg = row_background(im)
    reachable = bytearray(w * h)
    queue = deque()
    for x in range(w):
        for y in (0, h - 1):
            queue.append(y * w + x)
    for y in range(h):
        for x in (0, w - 1):
            queue.append(y * w + x)
    while queue:
        i = queue.popleft()
        if reachable[i]:
            continue
        x, y = i % w, i // w
        br, bgc, bb = bg[y]
        r, g, b = px[x, y]
        d = ((r - br) ** 2 + (g - bgc) ** 2 + (b - bb) ** 2) ** 0.5
        if d > thr:
            continue
        reachable[i] = 1
        for j in (i - 1, i + 1, i - w, i + w):
            if 0 <= j < w * h:
                jx, jy = j % w, j // w
                if abs(jx - x) + abs(jy - y) == 1 and not reachable[j]:
                    queue.append(j)
    return bytearray(0 if reachable[i] else 1 for i in range(w * h))


def keep_large_components(mask, w, h, min_ratio=0.08):
    seen = bytearray(w * h)
    comps = []
    for start in range(w * h):
        if not mask[start] or seen[start]:
            continue
        comp = []
        queue = deque([start])
        seen[start] = 1
        while queue:
            i = queue.popleft()
            comp.append(i)
            x, y = i % w, i // w
            for j in (i - 1, i + 1, i - w, i + w):
                if 0 <= j < w * h and mask[j] and not seen[j]:
                    jx, jy = j % w, j // w
                    if abs(jx - x) + abs(jy - y) == 1:
                        seen[j] = 1
                        queue.append(j)
        comps.append(comp)
    if not comps:
        return mask, []
    largest = max(len(c) for c in comps)
    kept = [c for c in comps if len(c) >= largest * min_ratio]
    out = bytearray(w * h)
    for comp in kept:
        for i in comp:
            out[i] = 1
    return out, [len(c) for c in kept]


def silhouette(im, thr):
    w, h = im.size
    m = mask_subject(im, thr)
    m, areas = keep_large_components(m, w, h)
    sil = Image.new('L', (w, h), 255)
    sp = sil.load()
    xs, ys = [], []
    for y in range(h):
        row = y * w
        for x in range(w):
            if m[row + x]:
                sp[x, y] = 0
                xs.append(x)
                ys.append(y)
    if not xs:
        return None, None, areas
    sil = sil.filter(ImageFilter.MinFilter(3))  # close pinholes
    bbox = (max(min(xs) - 4, 0), max(min(ys) - 4, 0), min(max(xs) + 5, w), min(max(ys) + 5, h))
    return sil.crop(bbox), bbox, areas


def fit(img, size):
    out = img.copy()
    out.thumbnail((size, size), Image.LANCZOS)
    canvas = Image.new('L', (size, size), 255)
    canvas.paste(out, ((size - out.width) // 2, (size - out.height) // 2))
    return canvas


def build_board(cells, path, colour):
    label_w, header_h, cell = 150, 28, 136
    board = Image.new('RGB', (label_w + 3 * cell, header_h + len(cells) * cell), (245, 240, 232))
    draw = ImageDraw.Draw(board)
    for c, size in enumerate(SIZES):
        draw.text((label_w + c * cell + 50, 8), f'{size}px', fill=(60, 60, 70))
    for r, (name, sized) in enumerate(cells.items()):
        draw.text((10, header_h + r * cell + 58), name, fill=(60, 60, 70))
        for c, size in enumerate(SIZES):
            tile = fit(sized[size], size).resize((128, 128), Image.NEAREST)
            if colour:
                tile = tile.convert('RGB')
            else:
                tile = Image.merge('RGB', (tile, tile, tile))
            board.paste(tile, (label_w + c * cell + 4, header_h + r * cell + 4))
    board.save(path)
    return path


def main():
    OUT_DIR.mkdir(exist_ok=True)
    sil_cells, col_cells = {}, {}
    for name, rel, crop, thr in SUBJECTS:
        src = ASSET_ROOT / rel
        im = Image.open(src).convert('RGB').crop(crop)
        im.thumbnail((WORK_W, WORK_W * 4), Image.LANCZOS)
        sil, bbox, areas = silhouette(im, thr)
        if sil is None:
            print(f'{name}: EMPTY MASK at threshold {thr} — adjust')
            continue
        coverage = sum(areas) / (im.width * im.height)
        print(f'{name}: bbox={bbox} size=({bbox[2]-bbox[0]}x{bbox[3]-bbox[1]}) '
              f'mask_coverage={coverage:.1%} components_kept={len(areas)}')
        sil_cells[name] = {s: sil for s in SIZES}
        col_cells[name] = {s: im.crop(bbox).convert('RGB') for s in SIZES}
    build_board(sil_cells, OUT_DIR / 'R15_THUMBNAIL_BOARD_SILHOUETTE.png', colour=False)
    # colour context board: LANCZOS downscales of the same crops, no masking
    label_w, header_h, cell = 150, 28, 136
    board = Image.new('RGB', (label_w + 3 * cell, header_h + len(col_cells) * cell), (245, 240, 232))
    draw = ImageDraw.Draw(board)
    for c, size in enumerate(SIZES):
        draw.text((label_w + c * cell + 50, 8), f'{size}px', fill=(60, 60, 70))
    for r, (name, sized) in enumerate(col_cells.items()):
        draw.text((10, header_h + r * cell + 58), name, fill=(60, 60, 70))
        for c, size in enumerate(SIZES):
            t = sized[size].copy()
            t.thumbnail((size, size), Image.LANCZOS)
            tile = Image.new('RGB', (size, size), (245, 240, 232))
            tile.paste(t, ((size - t.width) // 2, (size - t.height) // 2))
            board.paste(tile.resize((128, 128), Image.NEAREST), (label_w + c * cell + 4, header_h + r * cell + 4))
    board.save(OUT_DIR / 'R15_THUMBNAIL_BOARD_COLOUR.png')
    print('wrote', OUT_DIR / 'R15_THUMBNAIL_BOARD_SILHOUETTE.png')
    print('wrote', OUT_DIR / 'R15_THUMBNAIL_BOARD_COLOUR.png')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
