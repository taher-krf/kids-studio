#!/usr/bin/env python3
"""Build the Mulu & Tekla development sketch sheets (SVG).

DEVELOPMENT EXPLORATION ONLY (PROP-0008). These sheets are rough construction
sketches for owner review and for briefing the visual-generation phase. They are
not approved designs, not model sheets and not reference art.

Every sheet draws the same parametric Mulu and Tekla. That is deliberate: if a
lead can be drawn from a handful of fixed primitives plus a few state
parameters, the design is rig-friendly and easy to keep on model. Standard
library only (DEC-0009). Output is deterministic.

Usage: python scripts/build_dev_sketches.py [--out DIR]
"""
import argparse
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '05_visual_system' / 'sketches'

# "Sunny Clay" exploration palette (VISUAL_DEVELOPMENT_V0.3.md section 6). Not locked.
C = {
    'bg': '#FBF8F2', 'text': '#2A2F3F', 'muted': '#6E7489', 'rule': '#E3DDD2',
    'pick': '#FFF1C7', 'pick_edge': '#E2B84A', 'avoid': '#D0463B',
    'line': '#34405E', 'sil': '#1D2230',
    'mulu': '#FFF7E8', 'mulu_pink': '#FFDCD6', 'mulu_grey': '#DDE2EB', 'mulu_band': '#D2DEEF',
    'blush': '#F4A69E', 'eye': '#232838', 'mouth': '#8C3B3B',
    'shell': '#C9643E', 'shell_d': '#8F4329', 'shell_l': '#E3906A',
    'skin': '#F1D4AF', 'skin_d': '#D9AD80', 'ear_in': '#E7A48C', 'nose': '#3A2B28',
    'apron': '#2E7F86', 'apron_d': '#22656B', 'ruler': '#F2C230',
    'drop': '#6FB2EE', 'drop_hi': '#FFFFFF', 'wind': '#FFFFFF',
    'sky': '#9BD3F3', 'sky_hi': '#D9F0FB', 'hill': '#8DC462', 'hill_d': '#6FA84A',
    'earth': '#A5764C', 'wood': '#B98653', 'wood_d': '#8A5F36', 'stream': '#5DB7D8',
    'far': '#A9BFD6', 'leaf': '#5E9E47', 'umb': '#E8584A', 'umb_d': '#B83E33',
}
FONT = "Nunito, 'Trebuchet MS', Verdana, sans-serif"


def n(v: float) -> str:
    """Compact, deterministic number formatting."""
    if abs(v) < 0.005:
        return '0'
    return f'{v:.2f}'.rstrip('0').rstrip('.')


def esc(text: str) -> str:
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


class Sheet:
    def __init__(self, width: int, height: int, title: str, subtitle: str):
        self.w, self.h = width, height
        self.defs: list[str] = []
        self.body: list[str] = []
        self._ids = 0
        self.add(f'<rect width="{width}" height="{height}" fill="{C["bg"]}"/>')
        self.text(32, 44, title, 26, weight='800')
        self.text(32, 70, subtitle, 14, fill=C['muted'])

    def uid(self, prefix: str) -> str:
        self._ids += 1
        return f'{prefix}{self._ids}'

    def add(self, element: str) -> None:
        self.body.append(element)

    def text(self, x, y, s, size=14, anchor='start', weight='400', fill=None, italic=False):
        style = ' font-style="italic"' if italic else ''
        self.add(f'<text x="{n(x)}" y="{n(y)}" font-family="{FONT}" font-size="{n(size)}" '
                 f'font-weight="{weight}" text-anchor="{anchor}" fill="{fill or C["text"]}"{style}>{esc(s)}</text>')

    def lines(self, x, y, rows, size=13, gap=17, anchor='start', fill=None, weight='400'):
        for i, row in enumerate(rows):
            self.text(x, y + i * gap, row, size, anchor, weight, fill)

    def panel(self, x, y, w, h, pick=False, label=None):
        fill, edge = (C['pick'], C['pick_edge']) if pick else ('#FFFFFF', C['rule'])
        self.add(f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" rx="14" fill="{fill}" '
                 f'stroke="{edge}" stroke-width="{2 if pick else 1.5}"/>')
        if label:
            self.text(x + 16, y + 28, label, 17, weight='800')

    def cross(self, x, y, w, h):
        self.add(f'<path d="M{n(x)} {n(y)} L{n(x + w)} {n(y + h)} M{n(x + w)} {n(y)} L{n(x)} {n(y + h)}" '
                 f'stroke="{C["avoid"]}" stroke-width="5" stroke-linecap="round" opacity="0.8"/>')

    def svg(self) -> str:
        defs = f'<defs>{"".join(self.defs)}</defs>' if self.defs else ''
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
                f'viewBox="0 0 {self.w} {self.h}">\n{defs}\n' + '\n'.join(self.body) + '\n</svg>\n')


# ---------------------------------------------------------------------------
# Mulu (soft-solid cloud). Local units: body width W = 200, origin = centre of
# the flat base, y negative upward.
# ---------------------------------------------------------------------------
MW = 200.0
MH = 84.0  # body height (family B, without the puffs)
CAPACITY = {'plump': (1.06, 1.16), 'normal': (1.0, 1.0), 'wisp': (0.84, 0.68), 'held': (1.13, 1.2)}
# Top Puff poses for family B: (rotation degrees, scale, drop into body)
TOP_POSE = {'up': (0, 1.0, 0), 'perk': (8, 1.1, 0), 'lean': (30, 1.0, 0),
            'droop': (-64, 0.92, 6), 'tucked': (0, 0.5, 20)}


def _mulu_parts(fam: str, top: str):
    """Return silhouette primitives: (kind, geometry, transform)."""
    parts = []
    if fam == 'B':  # "Cumulus": flat low body + one tall Top Puff (with curl) + one small shoulder puff
        x0, x1, r = -100.0, 100.0, 20.0
        body = (f'M{n(x0 + r)} 0 L{n(x1 - r)} 0 Q{n(x1)} 0 {n(x1)} {n(-r)} '
                f'C{n(x1)} {n(-r - 0.55 * MH)} 64 {n(-MH)} 2 {n(-MH)} '
                f'C-64 {n(-MH)} {n(x0)} {n(-r - 0.55 * MH)} {n(x0)} {n(-r)} Q{n(x0)} 0 {n(x0 + r)} 0 Z')
        parts.append(('path', body, ''))
        parts.append(('circle', (50.0, -78.0, 30.0), ''))  # shoulder puff: fixed, never animates
        px, py = -32.0, -0.72 * MH
        ang, k, drop = TOP_POSE[top]
        tr = (f'rotate({n(ang)} {n(px)} {n(py)}) translate({n(px)} {n(py + drop)}) '
              f'scale({n(k)}) translate({n(-px)} {n(-py)})')
        tx, ty, rt = -32.0, -112.0, 54.0
        parts.append(('circle', (tx, ty, rt), tr))
        top_y = ty - rt
        curl = (f'M{n(tx + 2)} {n(top_y + 3)} C{n(tx - 4)} {n(top_y - 16)} {n(tx + 20)} {n(top_y - 26)} '
                f'{n(tx + 22)} {n(top_y - 12)} C{n(tx + 23)} {n(top_y - 3)} {n(tx + 12)} {n(top_y - 4)} '
                f'{n(tx + 13)} {n(top_y - 11)}')
        parts.append(('curl', curl, tr))
        parts.append(('nub', (-96.0, -26.0, 13.0), ''))
        parts.append(('nub', (96.0, -26.0, 13.0), ''))
    elif fam == 'A':  # "Pillow": horizontal marshmallow loaf, corner puffs, centred curl
        h, r = 118.0, 34.0
        body = (f'M{n(-100 + 12)} 0 L{n(100 - 12)} 0 Q100 0 100 -14 L100 {n(-h + r)} '
                f'Q100 {n(-h)} {n(100 - r)} {n(-h - 4)} Q0 {n(-h - 14)} {n(-100 + r)} {n(-h - 4)} '
                f'Q-100 {n(-h)} -100 {n(-h + r)} L-100 -14 Q-100 0 {n(-100 + 12)} 0 Z')
        parts.append(('path', body, ''))
        parts.append(('circle', (-88.0, -22.0, 24.0), ''))
        parts.append(('circle', (88.0, -22.0, 24.0), ''))
        ty = -h - 12
        curl = (f'M0 {n(ty + 6)} C-6 {n(ty - 14)} 18 {n(ty - 24)} 20 {n(ty - 10)} '
                f'C21 {n(ty - 1)} 10 {n(ty - 2)} 11 {n(ty - 9)}')
        parts.append(('curl', curl, ''))
        parts.append(('nub', (-104.0, -48.0, 13.0), ''))
        parts.append(('nub', (104.0, -48.0, 13.0), ''))
    elif fam == 'C':  # "Scoop": tall dome, cheek puffs, topknot
        w2, h = 76.0, 176.0
        body = (f'M{n(-w2 + 14)} 0 L{n(w2 - 14)} 0 Q{n(w2)} 0 {n(w2)} -16 '
                f'C{n(w2)} {n(-h * 0.7)} 44 {n(-h)} 0 {n(-h)} C-44 {n(-h)} {n(-w2)} {n(-h * 0.7)} {n(-w2)} -16 '
                f'Q{n(-w2)} 0 {n(-w2 + 14)} 0 Z')
        parts.append(('path', body, ''))
        parts.append(('circle', (-70.0, -28.0, 28.0), ''))
        parts.append(('circle', (70.0, -28.0, 28.0), ''))
        parts.append(('circle', (0.0, -h - 8, 20.0), ''))
        ty = -h - 28
        curl = (f'M0 {n(ty + 6)} C-5 {n(ty - 12)} 16 {n(ty - 20)} 18 {n(ty - 8)} '
                f'C19 {n(ty)} 9 {n(ty - 1)} 10 {n(ty - 7)}')
        parts.append(('curl', curl, ''))
        parts.append(('nub', (-92.0, -40.0, 12.0), ''))
        parts.append(('nub', (92.0, -40.0, 12.0), ''))
    elif fam == 'icon':  # the generic three-bump cloud we avoid
        parts.append(('path', 'M-95 0 L95 0 Q108 0 108 -22 L108 -30 Q108 -52 86 -52 L-86 -52 Q-108 -52 -108 -30 '
                      'L-108 -22 Q-108 0 -95 0 Z', ''))
        parts.append(('circle', (-52.0, -60.0, 40.0), ''))
        parts.append(('circle', (8.0, -84.0, 58.0), ''))
        parts.append(('circle', (64.0, -58.0, 38.0), ''))
    return parts


def _face_geometry(fam: str):
    if fam == 'A':
        return 0.0, -62.0, 24.0, -40.0
    if fam == 'C':
        return 0.0, -84.0, 22.0, -58.0
    if fam == 'icon':
        return 8.0, -44.0, 22.0, -24.0
    return 12.0, -50.0, 21.0, -28.0  # fx, eye y, eye half-spacing, mouth y


FACES = {
    'neutral': ('open', 'soft', 'smile', False, 0),
    'happy': ('open', 'up', 'grin', True, 0),
    'excited': ('wide', 'up', 'open', True, 0),
    'sad': ('down', 'sad', 'frown', False, 0),
    'secret': ('open', 'worry', 'tight', False, 1),
    'embarrassed': ('squeeze', 'worry', 'wobble', True, 0),
    'frustrated': ('open', 'angry', 'huff', False, 0),
    'scared': ('tiny', 'worry', 'o', False, 0),
    'calm': ('closed', 'soft', 'smile', False, 0),
    'proud': ('happyarc', 'up', 'grin', True, 0),
    'held': ('squeeze', 'angry', 'puffed', True, 0),
    'shock': ('wide', 'up', 'o', False, 0),
}


def _mulu_face(s: Sheet, fam: str, expr: str):
    fx, ey, dx, my = _face_geometry(fam)
    eyes, brows, mouth, cheeks, look = FACES[expr]
    e, sw = C['eye'], 4.2
    rx, ry = 8.5, 12.0
    if cheeks:
        for sx in (-1, 1):
            s.add(f'<ellipse cx="{n(fx + sx * 36)}" cy="{n(my - 2)}" rx="9" ry="5" fill="{C["blush"]}" opacity="0.75"/>')
    for side in (-1, 1):
        x = fx + side * dx + look * 5
        if eyes in ('open', 'wide', 'down', 'tiny'):
            k = {'open': 1.0, 'wide': 1.2, 'down': 1.0, 'tiny': 0.6}[eyes]
            yy = ey + (3 if eyes == 'down' else 0)
            s.add(f'<ellipse cx="{n(x)}" cy="{n(yy)}" rx="{n(rx * k)}" ry="{n(ry * k)}" fill="{e}"/>')
            hy = yy - ry * k * (0.1 if eyes == 'down' else 0.38)
            s.add(f'<circle cx="{n(x - rx * k * 0.3 + look * 3)}" cy="{n(hy)}" r="{n(2.9 * k)}" fill="#fff"/>')
        elif eyes == 'closed':
            s.add(f'<path d="M{n(x - rx)} {n(ey)} Q{n(x)} {n(ey + 8)} {n(x + rx)} {n(ey)}" stroke="{e}" '
                  f'stroke-width="{sw}" fill="none" stroke-linecap="round"/>')
        elif eyes == 'happyarc':
            s.add(f'<path d="M{n(x - rx)} {n(ey + 3)} Q{n(x)} {n(ey - 10)} {n(x + rx)} {n(ey + 3)}" stroke="{e}" '
                  f'stroke-width="{sw}" fill="none" stroke-linecap="round"/>')
        elif eyes == 'squeeze':
            d = (f'M{n(x - side * rx)} {n(ey - 7)} L{n(x + side * rx * 0.8)} {n(ey)} L{n(x - side * rx)} {n(ey + 7)}')
            s.add(f'<path d="{d}" stroke="{e}" stroke-width="{sw}" fill="none" stroke-linecap="round" '
                  f'stroke-linejoin="round"/>')
        by = ey - 21
        inner = x - side * 9  # side=-1 is the left eye; its inner end is toward the centre
        outer = x + side * 9
        if brows == 'flat':
            d = f'M{n(inner)} {n(by)} L{n(outer)} {n(by)}'
        elif brows == 'up':
            d = f'M{n(inner)} {n(by - 3)} Q{n(x)} {n(by - 9)} {n(outer)} {n(by - 3)}'
        elif brows == 'soft':
            d = f'M{n(inner)} {n(by + 1)} Q{n(x)} {n(by - 3)} {n(outer)} {n(by + 1)}'
        elif brows in ('sad', 'worry'):
            lift = 8 if brows == 'worry' else 6
            d = f'M{n(inner)} {n(by - lift)} L{n(outer)} {n(by + 2)}'
        else:  # angry
            d = f'M{n(inner)} {n(by + 5)} L{n(outer)} {n(by - 4)}'
        s.add(f'<path d="{d}" stroke="{e}" stroke-width="5" fill="none" stroke-linecap="round"/>')
    m = C['mouth']
    if mouth == 'smile':
        s.add(f'<path d="M{n(fx - 9)} {n(my)} Q{n(fx)} {n(my + 7)} {n(fx + 9)} {n(my)}" stroke="{e}" '
              f'stroke-width="{sw}" fill="none" stroke-linecap="round"/>')
    elif mouth == 'grin':
        s.add(f'<path d="M{n(fx - 13)} {n(my - 3)} Q{n(fx)} {n(my - 1)} {n(fx + 13)} {n(my - 3)} '
              f'Q{n(fx + 11)} {n(my + 13)} {n(fx)} {n(my + 13)} Q{n(fx - 11)} {n(my + 13)} {n(fx - 13)} {n(my - 3)} Z" '
              f'fill="{m}" stroke="{e}" stroke-width="3" stroke-linejoin="round"/>')
    elif mouth == 'open':
        s.add(f'<ellipse cx="{n(fx)}" cy="{n(my + 4)}" rx="12" ry="13" fill="{m}" stroke="{e}" stroke-width="3"/>')
    elif mouth == 'frown':
        s.add(f'<path d="M{n(fx - 9)} {n(my + 5)} Q{n(fx)} {n(my - 3)} {n(fx + 9)} {n(my + 5)}" stroke="{e}" '
              f'stroke-width="{sw}" fill="none" stroke-linecap="round"/>')
    elif mouth == 'tight':
        s.add(f'<path d="M{n(fx - 6 + look * 4)} {n(my + 2)} L{n(fx + 6 + look * 4)} {n(my + 1)}" stroke="{e}" '
              f'stroke-width="{sw}" stroke-linecap="round"/>')
    elif mouth == 'wobble':
        s.add(f'<path d="M{n(fx - 11)} {n(my + 2)} q3 -4 5.5 0 t5.5 0 t5.5 0 t5.5 0" stroke="{e}" '
              f'stroke-width="{sw}" fill="none" stroke-linecap="round"/>')
    elif mouth == 'o':
        s.add(f'<ellipse cx="{n(fx)}" cy="{n(my + 3)}" rx="5" ry="6" fill="{m}" stroke="{e}" stroke-width="3"/>')
    elif mouth in ('huff', 'puffed'):
        for sx in (-1, 1):
            s.add(f'<path d="M{n(fx + sx * 14)} {n(my - 9)} Q{n(fx + sx * 30)} {n(my - 3)} {n(fx + sx * 14)} {n(my + 7)}" '
                  f'stroke="{C["line"]}" stroke-width="3" fill="none" stroke-linecap="round"/>')
        s.add(f'<path d="M{n(fx - 5)} {n(my)} L{n(fx + 5)} {n(my)}" stroke="{e}" stroke-width="{sw}" '
              f'stroke-linecap="round"/>')


def mulu(s: Sheet, cx, yb, width, fam='B', top='up', cap='normal', tint='normal', edge='smooth',
         face='neutral', sil=False, flip=False, band=True):
    """Draw Mulu with his flat base centred at (cx, yb) and body width `width` px."""
    k = width / MW
    sx, sy = CAPACITY[cap]
    s.add(f'<g transform="translate({n(cx)} {n(yb)}) scale({n(k * sx * (-1 if flip else 1))} {n(k * sy)})">')
    parts = _mulu_parts(fam, top)
    line = C['sil'] if sil else C['line']
    fill = C['sil'] if sil else {'normal': C['mulu'], 'pink': C['mulu_pink'], 'grey': C['mulu_grey']}[tint]
    ow = 3.4 / max(k, 0.25) if sil else 3.4  # keep thumbnails' outline visible

    def shape(kind, geo, tr, paint, stroke, width_):
        t = f' transform="{tr}"' if tr else ''
        if kind == 'path':
            return f'<path d="{geo}" fill="{paint}" stroke="{stroke}" stroke-width="{n(width_)}" stroke-linejoin="round"{t}/>'
        if kind in ('circle', 'nub'):
            x, y, r = geo
            return f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r)}" fill="{paint}" stroke="{stroke}" stroke-width="{n(width_)}"{t}/>'
        return (f'<path d="{geo}" fill="none" stroke="{stroke}" stroke-width="{n(width_)}" '
                f'stroke-linecap="round" stroke-linejoin="round"{t}/>')

    ruffle = edge == 'ruffled'
    # Pass 1: outline under everything (merges the silhouette into one soft mass).
    for kind, geo, tr in parts:
        if kind == 'curl':
            s.add(shape(kind, geo, tr, 'none', line, 11 + 2 * ow))
        else:
            s.add(shape(kind, geo, tr, line, line, 2 * ow))
            if ruffle and kind in ('path', 'circle'):
                s.add(shape(kind, geo, tr, 'none', line, 0).replace(
                    'stroke-width="0"', f'stroke-width="{n(12 + 2 * ow)}" stroke-dasharray="0 13" stroke-linecap="round"'))
    # Pass 2: fills.
    for kind, geo, tr in parts:
        if kind == 'curl':
            s.add(shape(kind, geo, tr, 'none', fill, 11))
        elif kind != 'nub':
            s.add(shape(kind, geo, tr, fill, fill, 0.01))
            if ruffle:
                s.add(shape(kind, geo, tr, 'none', fill, 0).replace(
                    'stroke-width="0"', 'stroke-width="12" stroke-dasharray="0 13" stroke-linecap="round"'))
    if not sil:
        body_geo = parts[0][1]
        if band and fam in ('A', 'B', 'C'):
            cid = s.uid('mclip')
            s.defs.append(f'<clipPath id="{cid}"><path d="{body_geo}"/></clipPath>')
            wave = 'M-120 -12 ' + ' '.join('q6 -7 12 0' for _ in range(20)) + ' L120 0 L-120 0 Z'
            s.add(f'<path d="{wave}" fill="{C["mulu_band"]}" clip-path="url(#{cid})"/>')
        _mulu_face(s, fam, face)
    for kind, geo, tr in parts:
        if kind == 'nub':
            s.add(shape(kind, geo, tr, fill, line, 3.0 if not sil else 0.01))
    s.add('</g>')


def drop(s: Sheet, x, y, size=9.0, sil=False, color=None):
    """One stylised teardrop; (x, y) is the drop's round bottom centre."""
    r = size
    fill = C['sil'] if sil else (color or C['drop'])
    s.add(f'<path d="M{n(x)} {n(y - 2.3 * r)} C{n(x + 0.35 * r)} {n(y - 1.5 * r)} {n(x + r)} {n(y - 0.9 * r)} '
          f'{n(x + r)} {n(y - 0.2 * r)} A{n(r)} {n(r)} 0 0 1 {n(x - r)} {n(y - 0.2 * r)} '
          f'C{n(x - r)} {n(y - 0.9 * r)} {n(x - 0.35 * r)} {n(y - 1.5 * r)} {n(x)} {n(y - 2.3 * r)} Z" '
          f'fill="{fill}" stroke="{C["line"] if not sil else C["sil"]}" stroke-width="1.6"/>')
    if not sil:
        s.add(f'<ellipse cx="{n(x - 0.38 * r)}" cy="{n(y - 0.55 * r)}" rx="{n(0.22 * r)}" ry="{n(0.34 * r)}" fill="#fff" opacity="0.9"/>')


def plink(s: Sheet, x, y, w=22.0):
    s.add(f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="{n(w)}" ry="{n(w * 0.28)}" fill="none" stroke="{C["drop"]}" stroke-width="2.4"/>')
    s.add(f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="{n(w * 0.5)}" ry="{n(w * 0.14)}" fill="none" stroke="{C["drop"]}" stroke-width="2"/>')


def swirl(s: Sheet, x, y, length=90.0, direction=1, lift=0.0, curl=True, width=4.0):
    """Drawn wind: a gentle line ending in a small curl (the signature swirl terminal)."""
    d = direction
    ex, ey = x + d * length, y + lift
    path = f'M{n(x)} {n(y)} C{n(x + d * length * 0.35)} {n(y - 12)} {n(x + d * length * 0.65)} {n(ey + 12)} {n(ex)} {n(ey)}'
    if curl:
        path += (f' C{n(ex + d * 14)} {n(ey - 6)} {n(ex + d * 12)} {n(ey - 22)} {n(ex)} {n(ey - 20)} '
                 f'C{n(ex - d * 8)} {n(ey - 19)} {n(ex - d * 7)} {n(ey - 10)} {n(ex + d * 1)} {n(ey - 10)}')
    s.add(f'<path d="{path}" fill="none" stroke="{C["line"]}" stroke-width="{n(width + 3.2)}" stroke-linecap="round" opacity="0.55"/>')
    s.add(f'<path d="{path}" fill="none" stroke="{C["wind"]}" stroke-width="{n(width)}" stroke-linecap="round"/>')


# ---------------------------------------------------------------------------
# Tekla (armadillo-inspired builder). Local units: standing height to ear tips
# TH = 200, origin = between the feet on the ground, facing screen-right.
# ---------------------------------------------------------------------------

def _ts(fill, sil, width=3.0):
    if sil:
        return f'fill="{C["sil"]}" stroke="{C["sil"]}" stroke-width="{n(width)}" stroke-linejoin="round"'
    return f'fill="{fill}" stroke="{C["line"]}" stroke-width="{n(width)}" stroke-linejoin="round"'


def _limb(s, x1, y1, x2, y2, width, sil):
    col = C['sil'] if sil else C['skin_d']
    s.add(f'<path d="M{n(x1)} {n(y1)} L{n(x2)} {n(y2)}" stroke="{C["sil"] if sil else C["line"]}" '
          f'stroke-width="{n(width + 6)}" stroke-linecap="round"/>')
    s.add(f'<path d="M{n(x1)} {n(y1)} L{n(x2)} {n(y2)}" stroke="{col}" stroke-width="{n(width)}" stroke-linecap="round"/>')


def tekla_head(s: Sheet, hx, hy, face='neutral', sil=False, tilt=0.0):
    s.add(f'<g transform="translate({n(hx)} {n(hy)}) rotate({n(tilt)})">')
    # Ears (behind the head).
    s.add(f'<path d="M-22 -8 Q-42 -34 -32 -58 Q-12 -48 -4 -18 Z" {_ts(C["skin"], sil)}/>')
    s.add(f'<path d="M-4 -20 Q-2 -44 14 -60 Q26 -40 16 -16 Z" {_ts(C["skin"], sil)}/>')
    if not sil:
        s.add(f'<path d="M-20 -16 Q-34 -34 -28 -50 Q-15 -42 -10 -22 Z" fill="{C["ear_in"]}"/>')
        s.add(f'<path d="M2 -24 Q3 -42 13 -52 Q20 -38 12 -22 Z" fill="{C["ear_in"]}"/>')
    # Head, snout, nose.
    s.add(f'<ellipse cx="0" cy="0" rx="28" ry="24" {_ts(C["skin"], sil)}/>')
    s.add(f'<path d="M12 -12 Q40 -8 55 3 Q59 10 52 13 Q34 15 14 12 Z" {_ts(C["skin"], sil)}/>')
    s.add(f'<ellipse cx="55" cy="7" rx="6" ry="5.5" {_ts(C["nose"], sil, 2.5)}/>')
    # Head shield: her built-in hard hat.
    s.add(f'<path d="M-27 -4 Q-26 -30 0 -32 Q24 -33 30 -15 L38 -11 Q20 -15 -27 -4 Z" {_ts(C["shell"], sil)}/>')
    if not sil:
        s.add(f'<path d="M-14 -24 Q2 -30 20 -24" stroke="{C["shell_l"]}" stroke-width="3" fill="none" stroke-linecap="round"/>')
        e = C['eye']
        if face in ('neutral', 'side', 'bow'):
            for ex, rx in ((20, 5.2), (6, 4.4)):
                ex += 3 if face == 'side' else 0
                if face == 'bow':
                    s.add(f'<path d="M{n(ex - rx)} -3 Q{n(ex)} 2 {n(ex + rx)} -3" stroke="{e}" stroke-width="2.8" fill="none" stroke-linecap="round"/>')
                    continue
                s.add(f'<path d="M{n(ex - rx)} -4 Q{n(ex - rx)} 4 {n(ex)} 4 Q{n(ex + rx)} 4 {n(ex + rx)} -4 Z" fill="{e}"/>')
                s.add(f'<path d="M{n(ex - rx - 1.5)} -4.5 L{n(ex + rx + 1.5)} -4.5" stroke="{C["line"]}" stroke-width="2.4" stroke-linecap="round"/>')
                s.add(f'<circle cx="{n(ex + 1.6)}" cy="0" r="1.3" fill="#fff"/>')
            s.add(f'<path d="M34 16 Q39 17 44 15" stroke="{e}" stroke-width="2.6" fill="none" stroke-linecap="round"/>')
        elif face == 'laugh':
            for ex, rx in ((20, 5.5), (6, 4.6)):
                s.add(f'<path d="M{n(ex - rx)} -1 Q{n(ex)} -9 {n(ex + rx)} -1" stroke="{e}" stroke-width="3" fill="none" stroke-linecap="round"/>')
            s.add(f'<path d="M30 14 Q38 13 46 12 Q42 24 34 22 Z" fill="{C["mouth"]}" stroke="{e}" stroke-width="2.4" stroke-linejoin="round"/>')
        elif face == 'gasp':
            for ex, rx in ((20, 6.8), (5, 5.8)):
                s.add(f'<circle cx="{n(ex)}" cy="-3" r="{n(rx)}" fill="#fff" stroke="{e}" stroke-width="2.4"/>')
                s.add(f'<circle cx="{n(ex + 1)}" cy="-3" r="{n(rx * 0.45)}" fill="{e}"/>')
            s.add(f'<ellipse cx="38" cy="20" rx="7" ry="9" fill="{C["mouth"]}" stroke="{e}" stroke-width="2.4"/>')
    s.add('</g>')


def tekla(s: Sheet, x, yg, height, pose='fine', face=None, sil=False, flip=False, tail='down'):
    """Direction C "Leaning Egg" (recommended). pose: fine, arms, bow, straighten, tap, swish, gasp, laugh."""
    u = height / 192.0  # TH: ground to ear tips
    s.add(f'<g transform="translate({n(x)} {n(yg)}) scale({n(u * (-1 if flip else 1))} {n(u)})">')
    bow = 26 if pose == 'bow' else 0
    # Tail.
    if tail == 'swish' or pose == 'swish':
        s.add(f'<path d="M-30 -40 Q-70 -50 -78 -86 Q-60 -60 -30 -24 Z" {_ts(C["shell"], sil)}/>')
        if not sil:
            s.add(f'<path d="M-92 -70 Q-96 -90 -84 -104 M-102 -64 Q-110 -90 -94 -112" stroke="{C["muted"]}" stroke-width="2.6" fill="none" stroke-linecap="round"/>')
    else:
        s.add(f'<path d="M-30 -40 Q-62 -26 -84 -4 Q-58 -10 -30 -22 Z" {_ts(C["shell"], sil)}/>')
        if not sil:
            s.add(f'<path d="M-52 -30 L-47 -18 M-66 -20 L-62 -11" stroke="{C["shell_d"]}" stroke-width="2.4" stroke-linecap="round"/>')
    # Back leg and foot.
    s.add(f'<ellipse cx="-14" cy="-15" rx="12" ry="15" {_ts(C["skin_d"], sil)}/>')
    s.add(f'<ellipse cx="-7" cy="-5" rx="17" ry="6.5" {_ts(C["skin_d"], sil)}/>')
    # Upper body (bows forward around the hips).
    s.add(f'<g transform="rotate({n(bow)} 0 -30)">')
    s.add('<g transform="rotate(14 0 -74)">')
    cid = s.uid('tclip')
    s.defs.append(f'<clipPath id="{cid}"><ellipse cx="0" cy="-74" rx="46" ry="62"/></clipPath>')
    s.add(f'<ellipse cx="0" cy="-74" rx="46" ry="62" {_ts(C["shell"], sil)}/>')
    for y, xl in ((-98, -42.4), (-58, -44.4)):  # band lips: the back outline steps at each band edge
        s.add(f'<path d="M{n(xl + 5)} {y - 18} Q{n(xl - 10)} {y - 6} {n(xl - 7)} {y + 4} Q{n(xl + 2)} {y + 7} {n(xl + 10)} {y + 1}" {_ts(C["shell"], sil)}/>')
    if not sil:
        for y in (-98, -58):
            s.add(f'<path d="M-60 {y} Q-20 {y + 14} 34 {y - 4}" stroke="{C["shell_d"]}" stroke-width="3.2" fill="none" clip-path="url(#{cid})"/>')
            s.add(f'<path d="M-60 {y + 5} Q-20 {y + 19} 34 {y + 1}" stroke="{C["shell_l"]}" stroke-width="2.4" fill="none" clip-path="url(#{cid})"/>')
    s.add(f'<ellipse cx="18" cy="-70" rx="26" ry="48" {_ts(C["skin"], sil)}/>')
    s.add(f'<path d="M3 -100 L37 -97 Q43 -60 38 -27 Q20 -19 2 -24 Q-2 -60 3 -100 Z" {_ts(C["apron"], sil)}/>')
    if not sil:
        s.add(f'<rect x="10" y="-72" width="7" height="16" rx="1.5" fill="{C["ruler"]}" stroke="{C["line"]}" stroke-width="2"/>')
        s.add(f'<path d="M10 -68 L13 -68 M10 -64 L13 -64 M10 -60 L13 -60" stroke="{C["line"]}" stroke-width="1.4"/>')
        s.add(f'<rect x="6" y="-62" width="30" height="20" rx="4" fill="{C["apron_d"]}" stroke="{C["line"]}" stroke-width="2.4"/>')
        s.add(f'<path d="M4 -99 Q16 -116 36 -97" stroke="{C["apron_d"]}" stroke-width="3" fill="none"/>')
    s.add('</g>')
    # Arms.
    if pose in ('fine', 'arms', 'swish'):
        _limb(s, 16, -100, 50, -96, 11, sil)
        _limb(s, 22, -92, 54, -90, 11, sil)
    elif pose == 'straighten':
        _limb(s, 28, -100, 62, -66, 10, sil)
    elif pose == 'tap':
        _limb(s, 30, -100, 44, -64, 10, sil)
        if not sil:
            for i, dx in enumerate((0, 8, 16)):
                s.add(f'<path d="M{n(42 + dx)} -52 L{n(46 + dx)} -44" stroke="{C["muted"]}" stroke-width="2.4" stroke-linecap="round"/>')
    elif pose == 'gasp':
        pass  # drawn after the head: paws up at the cheeks
    elif pose == 'laugh':
        _limb(s, 30, -100, 50, -80, 10, sil)
    else:  # bow: arms at sides
        _limb(s, 28, -100, 36, -68, 10, sil)
    head_face = face or {'bow': 'bow', 'gasp': 'gasp', 'laugh': 'laugh'}.get(pose, 'neutral')
    tilt = -16 if pose == 'laugh' else (-6 if pose == 'gasp' else 0)
    tekla_head(s, 30, -132, head_face, sil, tilt)
    if pose == 'gasp':
        _limb(s, 22, -100, 2, -128, 10, sil)
        _limb(s, 38, -98, 70, -112, 10, sil)
    s.add('</g>')
    # Front leg and foot.
    s.add(f'<ellipse cx="16" cy="-15" rx="12" ry="15" {_ts(C["skin_d"], sil)}/>')
    s.add(f'<ellipse cx="25" cy="-5" rx="18" ry="6.5" {_ts(C["skin_d"], sil)}/>')
    s.add('</g>')


def tekla_ball(s: Sheet, x, yg, height, peek=False, sil=False, flip=False):
    """The Curl: a near-perfect banded ball; two ear tips always peek out. `height` = her standing TH."""
    u = height / 200.0
    s.add(f'<g transform="translate({n(x)} {n(yg)}) scale({n(u * (-1 if flip else 1))} {n(u)})">')
    s.add(f'<path d="M40 -84 L66 -100 L50 -72 Z" {_ts(C["skin"], sil)}/>')
    s.add(f'<path d="M48 -72 L74 -80 L54 -62 Z" {_ts(C["skin"], sil)}/>')
    cid = s.uid('bclip')
    s.defs.append(f'<clipPath id="{cid}"><circle cx="0" cy="-54" r="54"/></clipPath>')
    s.add(f'<circle cx="0" cy="-54" r="54" {_ts(C["shell"], sil)}/>')
    if not sil:
        for y in (-80, -40):
            s.add(f'<path d="M-60 {y} Q-4 {y + 20} 60 {y - 8}" stroke="{C["shell_d"]}" stroke-width="3.2" fill="none" clip-path="url(#{cid})"/>')
            s.add(f'<path d="M-60 {y + 5} Q-4 {y + 25} 60 {y - 3}" stroke="{C["shell_l"]}" stroke-width="2.4" fill="none" clip-path="url(#{cid})"/>')
        s.add(f'<path d="M26 -101 Q54 -90 56 -56 L34 -56 Q36 -80 26 -101 Z" fill="{C["shell"]}" stroke="{C["line"]}" stroke-width="2.6" clip-path="url(#{cid})"/>')
        s.add(f'<path d="M34 -52 L56 -52 Q54 -24 30 -8 Q38 -30 34 -52 Z" fill="{C["shell"]}" stroke="{C["line"]}" stroke-width="2.6" clip-path="url(#{cid})"/>')
        if peek:
            s.add(f'<path d="M36 -55 Q36 -46 44 -46 Q52 -46 52 -55 Z" fill="{C["eye"]}"/>')
            s.add(f'<path d="M34 -55.5 L54 -55.5" stroke="{C["line"]}" stroke-width="2.6" stroke-linecap="round"/>')
    s.add('</g>')


def tekla_upright(s: Sheet, x, yg, height, sil=False):
    """Direction A "Upright Builder" (explored, not recommended)."""
    u = height / 220.0
    s.add(f'<g transform="translate({n(x)} {n(yg)}) scale({n(u)})">')
    s.add(f'<path d="M-24 -46 Q-54 -30 -70 -8 Q-48 -14 -22 -30 Z" {_ts(C["shell"], sil)}/>')
    cid = s.uid('uclip')
    s.defs.append(f'<clipPath id="{cid}"><ellipse cx="-20" cy="-92" rx="32" ry="58"/></clipPath>')
    s.add(f'<ellipse cx="-20" cy="-92" rx="32" ry="58" {_ts(C["shell"], sil)}/>')
    if not sil:
        for y in (-116, -92, -68):
            s.add(f'<path d="M-56 {y} Q-24 {y + 10} 10 {y}" stroke="{C["shell_d"]}" stroke-width="3" fill="none" clip-path="url(#{cid})"/>')
    _limb(s, -4, -44, -6, -10, 14, sil)
    _limb(s, 16, -44, 18, -10, 14, sil)
    s.add(f'<ellipse cx="-2" cy="-5" rx="15" ry="6" {_ts(C["skin_d"], sil)}/>')
    s.add(f'<ellipse cx="22" cy="-5" rx="15" ry="6" {_ts(C["skin_d"], sil)}/>')
    s.add(f'<ellipse cx="6" cy="-90" rx="30" ry="54" {_ts(C["skin"], sil)}/>')
    s.add(f'<path d="M-12 -112 L26 -112 Q32 -80 28 -48 Q8 -40 -14 -46 Q-18 -80 -12 -112 Z" {_ts(C["apron"], sil)}/>')
    _limb(s, 0, -118, 34, -110, 11, sil)
    _limb(s, 4, -110, 38, -104, 11, sil)
    tekla_head(s, 16, -156, 'neutral', sil)
    s.add('</g>')


def tekla_low(s: Sheet, x, yg, height, sil=False):
    """Direction B "Low Dome" quadruped (explored, not recommended). `height` = matched TH."""
    u = height / 200.0
    s.add(f'<g transform="translate({n(x)} {n(yg)}) scale({n(u)})">')
    s.add(f'<path d="M-58 -24 Q-84 -14 -102 -2 Q-80 -6 -56 -12 Z" {_ts(C["shell"], sil)}/>')
    for lx in (-42, -22, 22, 40):
        s.add(f'<ellipse cx="{lx}" cy="-9" rx="9" ry="10" {_ts(C["skin_d"], sil)}/>')
    cid = s.uid('lclip')
    body = 'M-64 -12 C-64 -60 -36 -82 -6 -82 C28 -82 58 -60 58 -12 Z'
    s.defs.append(f'<clipPath id="{cid}"><path d="{body}"/></clipPath>')
    s.add(f'<path d="{body}" {_ts(C["shell"], sil)}/>')
    if not sil:
        for bx in (-22, 14):
            s.add(f'<path d="M{bx} -86 Q{bx + 10} -46 {bx} -8" stroke="{C["shell_d"]}" stroke-width="3.2" fill="none" clip-path="url(#{cid})"/>')
        s.add(f'<rect x="-14" y="-44" width="26" height="22" rx="4" fill="{C["apron"]}" stroke="{C["line"]}" stroke-width="2.4"/>')
        s.add(f'<rect x="-8" y="-52" width="6" height="12" fill="{C["ruler"]}" stroke="{C["line"]}" stroke-width="1.8"/>')
    tekla_head(s, 70, -46, 'neutral', sil)
    s.add('</g>')


def turtle(s: Sheet, x, yg, height, sil=False):
    """The turtle silhouette Tekla must never resemble."""
    u = height / 120.0
    s.add(f'<g transform="translate({n(x)} {n(yg)}) scale({n(u)})">')
    s.add(f'<ellipse cx="62" cy="-34" rx="20" ry="16" {_ts("#9CC47A", sil)}/>')
    for lx in (-40, 36):
        s.add(f'<ellipse cx="{lx}" cy="-8" rx="12" ry="10" {_ts("#9CC47A", sil)}/>')
    s.add(f'<path d="M-66 -14 C-66 -70 -30 -90 0 -90 C30 -90 60 -70 60 -14 Z" {_ts("#6E9E58", sil)}/>')
    if not sil:
        s.add(f'<path d="M-30 -60 L-12 -70 L8 -60 L8 -38 L-12 -28 L-30 -38 Z M8 -60 L28 -68 L44 -54 M8 -38 L30 -30 L46 -38 '
              f'M-30 -60 L-48 -52 M-30 -38 L-52 -30" stroke="{C["line"]}" stroke-width="2.4" fill="none"/>')
    s.add('</g>')


# ---------------------------------------------------------------------------
# Sheets
# ---------------------------------------------------------------------------
BANNER = 'DEVELOPMENT EXPLORATION (PROP-0008) - not approved design, not reference art'


def silhouette_strip(s: Sheet, x, y, draw, sizes=(64, 32), step=1.9):
    """Draw black silhouettes at thumbnail heights; draw(sheet, x, ground_y, px_height)."""
    cx = x
    for h in sizes:
        draw(s, cx, y, h)
        s.text(cx, y + 18, f'{h}px', 11, 'middle', fill=C['muted'])
        cx += h * step + 16


def sheet_mulu_families() -> Sheet:
    s = Sheet(1480, 980, 'Mulu - three silhouette families', BANNER)
    cols = [
        (40, 'AVOID: the generic cloud icon', 'icon', False),
        (400, 'M-A  "Pillow"', 'A', False),
        (760, 'M-B  "Cumulus" (recommended)', 'B', True),
        (1120, 'M-C  "Scoop"', 'C', False),
    ]
    notes = {
        'icon': ['Three bumps on a slab: the emoji / weather-app', 'cloud. Every AI cloud converges here.',
                 'Reads as "a cloud", never as "Mulu".'],
        'A': ['Wide marshmallow loaf, corner puffs, centred curl.', '+ cuddliest, simplest to rig, toy-friendly',
              '- weakest cloud read (pillow / bread / sheep body)', '- symmetric: no facing direction in silhouette',
              '- Pusheen-style loaf neighbour'],
        'B': ['Wide low body + ONE big Top Puff + curl.', '+ reads as a real cumulus tower (flat base, one tower)',
              '+ Top Puff is an acting antenna: perks, leans,', '   droops, tucks - mood reads even in silhouette',
              '+ unique notch at 32px; shows facing direction', '- asymmetric: mirror-flip drift risk (drift check D04)'],
        'C': ['Tall dome, cheek puffs, top-knot.', '+ big face field, very emotive',
              '- ghost / snowman / dumpling reading risk', '- a second dome beside Tekla\'s dome (weak pair)',
              '- top-knot swirl drifts toward the poop-emoji', '   silhouette: curl must never spiral upward'],
    }
    for x, label, fam, pick in cols:
        s.panel(x, 96, 330, 856, pick, label)
        cx = x + 165
        if fam == 'icon':
            mulu(s, cx, 360, 190, fam='icon', face='happy', band=False)
            s.cross(x + 40, 150, 250, 230)
        else:
            mulu(s, cx, 360, 190 if fam != 'C' else 160, fam=fam, face='happy')
            for dx in (-44, 6, 54):
                drop(s, cx + dx, 404 + (10 if dx == 6 else 0), 7)
        s.text(x + 16, 460, 'Black silhouette', 13, weight='700', fill=C['muted'])
        mulu(s, cx, 620, 150 if fam != 'C' else 124, fam=fam, face='neutral', sil=True)
        s.text(x + 16, 668, 'Thumbnail test', 13, weight='700', fill=C['muted'])
        silhouette_strip(s, x + 70, 760, lambda sh, xx, yy, h, fam=fam: mulu(
            sh, xx, yy, h * (1.35 if fam != 'C' else 0.95), fam=fam, sil=True))
        s.lines(x + 16, 812, notes[fam], 12.5, 18)
    return s


def sheet_mulu_states() -> Sheet:
    s = Sheet(1480, 1420, 'Mulu (M-B) - acting states and the weather code', BANNER)
    s.text(40, 112, 'Top Puff poses = body acting, never a power (Show Bible rule 2). The puff never detaches, splits or changes count.', 14, fill=C['muted'])
    poses = [('perk', 'happy', 'Perk - happy'), ('lean', 'excited', 'Lean - wants it'), ('up', 'neutral', 'Up - neutral'),
             ('droop', 'sad', 'Droop - sad'), ('tucked', 'scared', 'Tucked - scared'), ('up', 'held', 'Held breath - hiding')]
    for i, (top, face, label) in enumerate(poses):
        x = 120 + i * 230
        cap = 'held' if face == 'held' else 'normal'
        mulu(s, x, 300, 150, top=top, face=face, cap=cap, tint='grey' if face == 'sad' else 'normal')
        s.text(x, 332, label, 14, 'middle', '700')
        mulu(s, x, 420, 64, top=top, cap=cap, sil=True)
    s.text(40, 452, 'Same poses at 64px: the Top Puff keeps the mood readable in silhouette.', 12.5, fill=C['muted'])

    s.text(40, 520, 'Optional depletion states (story/comedy use only - not a meter, not tracked every shot)', 17, weight='800')
    for i, (cap, face, label) in enumerate([('plump', 'proud', 'Plump - after tea (heavier, sits lower)'),
                                            ('normal', 'neutral', 'Normal'),
                                            ('wisp', 'sad', 'Wisp - rained out / out of puff')]):
        x = 200 + i * 420
        mulu(s, x, 700, 150, cap=cap, face=face, top='droop' if cap == 'wisp' else 'up')
        s.text(x, 730, label, 14, 'middle', '700')

    s.text(40, 770, 'The weather code: what leaves his body (rain from the flat base, drawn wind). Mild only.', 17, weight='800')
    code = [('happy', 'perk', 'normal', 'Happy: warm breeze'), ('excited', 'lean', 'normal', 'Excited: skittery gusts'),
            ('sad', 'droop', 'grey', 'Sad: drizzle'), ('secret', 'up', 'normal', 'Secret: the Drip'),
            ('embarrassed', 'droop', 'pink', 'Embarrassed: plips'), ('frustrated', 'up', 'normal', 'Frustrated: one huff'),
            ('scared', 'tucked', 'normal', 'Scared: NOTHING'), ('calm', 'up', 'normal', 'Calm: aimed rain')]
    for i, (face, top, tint, label) in enumerate(code):
        col, row = i % 4, i // 4
        x, yb = 190 + col * 350, 920 + row * 270
        mulu(s, x, yb, 140, top=top, face=face, tint=tint, edge='ruffled' if face in ('excited', 'frustrated') else 'smooth')
        s.text(x, yb + 104, label, 14, 'middle', '700')
        if face == 'happy':
            swirl(s, x + 78, yb - 70, 60, 1, -8)
            swirl(s, x - 78, yb - 40, 50, -1, 6)
        elif face == 'excited':
            for j, (dx, dy, ln) in enumerate(((80, -80, 50), (86, -30, 40), (-84, -60, 46), (-80, -14, 36))):
                swirl(s, x + dx, yb + dy, ln, 1 if dx > 0 else -1, (-1) ** j * 8, curl=j % 2 == 0, width=3)
        elif face == 'sad':
            for dx in (-50, -26, -2, 22, 46):
                for dy in (22, 60):
                    drop(s, x + dx + (dy % 7), yb + dy + (dx % 13), 6)
        elif face == 'secret':
            drop(s, x + 30, yb + 30, 7)
            drop(s, x + 30, yb + 62, 7)
            plink(s, x + 30, yb + 80, 16)
        elif face == 'embarrassed':
            drop(s, x - 20, yb + 44, 11)
            drop(s, x + 26, yb + 70, 11)
        elif face == 'frustrated':
            swirl(s, x + 80, yb - 26, 44, 1, 2, curl=False, width=6)
            s.add(f'<circle cx="{n(x + 132)}" cy="{n(yb - 24)}" r="9" fill="#fff" stroke="{C["line"]}" stroke-width="2.4"/>')
        elif face == 'calm':
            sx, sy = x + 10, yb + 92
            s.add(f'<path d="M{n(sx - 22)} {n(sy)} Q{n(sx)} {n(sy - 10)} {n(sx + 22)} {n(sy)} Z" fill="{C["earth"]}" stroke="{C["line"]}" stroke-width="2"/>')
            s.add(f'<path d="M{n(sx)} {n(sy - 6)} L{n(sx)} {n(sy - 22)}" stroke="{C["leaf"]}" stroke-width="3.4"/>')
            s.add(f'<path d="M{n(sx)} {n(sy - 20)} q-14 -2 -16 -12 q12 0 16 12 z M{n(sx)} {n(sy - 20)} q14 -2 16 -12 q-12 0 -16 12 z" fill="{C["leaf"]}" stroke="{C["line"]}" stroke-width="1.8"/>')
            for j in range(5):
                drop(s, sx, yb + 14 + j * 11, 3.8)
    s.text(40, 1400, 'Rain always falls straight down from the flat base, as countable teardrops. Wind is always drawn swirls plus at most three reacting objects.', 13, fill=C['muted'])
    return s


def sheet_tekla_directions() -> Sheet:
    s = Sheet(1480, 1000, 'Tekla - three armadillo-inspired directions', BANNER)
    cols = [(40, 'AVOID: the turtle read', 'turtle', False), (400, 'T-A  "Upright Builder"', 'A', False),
            (760, 'T-B  "Low Dome"', 'B', False), (1120, 'T-C  "Leaning Egg" (recommended)', 'C', True)]
    notes = {
        'turtle': ['One rigid dome, plate pattern, head that', 'retracts. Tekla never retracts: she ROLLS UP.',
                   'Banned: hex plates, a separate carapace,', 'pulling limbs into a shell.'],
        'A': ['Biped, banded plate worn on the back.', '+ arms free, very human acting',
              '- shell reads as a backpack / Koopa / Franklin', '- closest to Fuleco and Mighty (upright',
              '   anthropomorphic armadillos)', '- big transformation into the Curl'],
        'B': ['Naturalistic quadruped dome.', '+ most "real armadillo"; best Roll',
              '- tools and folded arms impossible', '- apron becomes a saddlebag; weak deadpan',
              '   (face in profile, low in frame)', '- low dome = turtle / pill-bug risk'],
        'C': ['Semi-upright egg, 3 bands wrap the back', 'from head shield to tail. Walks on hind feet.',
              '+ arms free for tools and folded-arms "Fine"', '+ egg -> ball is a small, clean Curl',
              '+ head shield = a built-in hard hat', '+ tall ears + snout: never a turtle',
              '- needs a crisp 3/4 face for deadpan acting'],
    }
    for x, label, key, pick in cols:
        s.panel(x, 96, 330, 876, pick, label)
        cx = x + 150
        if key == 'turtle':
            turtle(s, cx, 360, 110)
            s.cross(x + 40, 190, 250, 200)
        elif key == 'A':
            tekla_upright(s, cx, 380, 230)
        elif key == 'B':
            tekla_low(s, cx - 10, 380, 200)
        else:
            tekla(s, cx - 10, 380, 230)
        if key != 'turtle':
            s.text(x + 16, 430, 'Curl', 13, weight='700', fill=C['muted'])
            tekla_ball(s, x + 110, 560, 200)
            s.text(x + 190, 520, 'two ear tips', 11.5, fill=C['muted'])
            s.text(x + 190, 536, 'always peek out', 11.5, fill=C['muted'])
        s.text(x + 16, 600, 'Black silhouette + thumbnails', 13, weight='700', fill=C['muted'])
        draw = {'turtle': lambda sh, xx, yy, h: turtle(sh, xx, yy, h * 0.6, sil=True),
                'A': lambda sh, xx, yy, h: tekla_upright(sh, xx, yy, h, sil=True),
                'B': lambda sh, xx, yy, h: tekla_low(sh, xx, yy, h, sil=True),
                'C': lambda sh, xx, yy, h: tekla(sh, xx, yy, h, sil=True)}[key]
        draw(s, x + 80, 780, 140)
        silhouette_strip(s, x + 200, 780, draw, step=1.2)
        s.lines(x + 16, 832, notes[key], 12.5, 18)
    return s


def sheet_tekla_tells() -> Sheet:
    s = Sheet(1480, 900, 'Tekla (T-C) - designed neutral, the tells and the breaks', BANNER)
    s.text(40, 112, 'Her face moves less than his by design. Feelings live in big, readable behaviour. Breaks are events.', 14, fill=C['muted'])
    row = [('fine', '"I\'m fine." (designed neutral)'), ('straighten', 'The Straightening'), ('bow', 'The Tiny Bow'),
           ('tap', 'Tap-tap (sound + claws)'), ('swish', 'The Swish (rare: truly happy)')]
    for i, (pose, label) in enumerate(row):
        x = 150 + i * 290
        tekla(s, x, 390, 220, pose=pose)
        s.text(x + 10, 426, label, 14, 'middle', '700')
        if pose == 'straighten':
            cx, cy = x + 88, 318
            s.add(f'<path d="M{n(cx - 14)} {n(cy)} L{n(cx + 14)} {n(cy)} L{n(cx + 10)} {n(cy + 18)} L{n(cx - 10)} {n(cy + 18)} Z" '
                  f'fill="#fff" stroke="{C["line"]}" stroke-width="2.6" transform="rotate(-6 {n(cx)} {n(cy)})"/>')
            s.add(f'<path d="M{n(cx + 22)} {n(cy - 4)} q8 6 0 14" stroke="{C["muted"]}" stroke-width="2.4" fill="none"/>')
            s.add(f'<rect x="{n(cx - 30)}" y="{n(cy + 18)}" width="60" height="6" rx="2" fill="{C["wood"]}" stroke="{C["line"]}" stroke-width="2"/>')
    s.text(40, 490, 'The Curl (overwhelmed, happy OR sad) and the breaks', 17, weight='800')
    tekla_ball(s, 160, 700, 220)
    s.text(160, 736, 'The Curl + "click"', 14, 'middle', '700')
    tekla_ball(s, 400, 700, 220, peek=True)
    s.text(400, 736, 'The Peek (one eye in the seam)', 14, 'middle', '700')
    tekla(s, 680, 720, 220, pose='laugh')
    s.text(690, 756, 'Break: the real laugh', 14, 'middle', '700')
    tekla(s, 960, 720, 220, pose='gasp')
    s.text(970, 756, 'Break: the terrible fake GASP', 14, 'middle', '700')
    s.lines(1120, 540, ['Rules', '- Neutral = half-lidded eyes, flat small mouth,', '  upright posture, arms folded.',
                        '- No brows, no lashes, no bows, no pink coding.', '- Ears stay upright ("at attention") except', '  in the Curl and in breaks.',
                        '- Shell never deforms; flexibility is in limbs', '  and the Curl.', '- Rain rolls off her shell: never wet.',
                        '- Year-one core tells: Straightening, Curl,', '  "I\'m fine". Bow, tap-tap, Swish are layered in.'], 13, 19)
    return s


def sheet_pair() -> Sheet:
    s = Sheet(1480, 1300, 'The pair - scale, hover heights, contact poses, thumbnail read', BANNER)
    th, g0, x0 = 200, 540, 80
    for i in range(0, 5):
        y = g0 - i * th / 2
        s.add(f'<path d="M{x0} {n(y)} L{x0 + 700} {n(y)}" stroke="{C["rule"]}" stroke-width="1.5" stroke-dasharray="6 6"/>')
        s.text(x0 - 8, y + 4, f'{i * 0.5:g} TH', 11, 'end', fill=C['muted'])
    tekla(s, 190, g0, th)
    mulu(s, 390, g0 - 0.45 * th, 0.9 * th, face='happy', top='perk', flip=True)
    s.text(290, g0 + 26, 'Talk height: base 0.45 TH, eye lines meet', 13, 'middle', '700')
    tekla(s, 620, g0, th)
    mulu(s, 640, g0 - 1.12 * th, 0.9 * th, face='calm')
    s.text(640, g0 + 26, 'Float height: base ~1.1 TH (travel, shade)', 13, 'middle', '700')
    s.lines(840, 150, ['Scale rules (TH = Tekla standing height to ear tips)',
                       '- Mulu body width = 0.9 TH (about 2x her body width)',
                       '- Mulu total height ~0.85 TH: as tall as her, twice as wide',
                       '- Talk height: base 0.45 TH (eye lines meet)',
                       '- Float height: base ~1.1 TH (clear of her ears)',
                       '- Lookout height: the Lookout branch, ~4 TH (his ceiling)',
                       '- Her ball: diameter ~0.55 TH',
                       '', 'Shape contrast',
                       '- Mulu: soft, wide, one rising puff, cream, floats',
                       '- Tekla: crisp, narrow, pointed ears + snout + tail,',
                       '  terracotta, grounded, stepped banded back',
                       '- Never "two blobs": if Mulu drifts rounder,',
                       '  Tekla must stay pointed.'], 14, 22)
    s.text(40, 700, 'Designed contact set (the only two-character contact in standard shots)', 17, weight='800')
    gy = 990
    tekla_ball(s, 170, gy, th)
    mulu(s, 158, gy - 0.44 * th, 0.9 * th, face='calm', top='lean')
    s.text(170, gy + 32, 'Cloud Hat (comfort + logo pose)', 14, 'middle', '700')
    tekla(s, 420, gy, th, pose='straighten')
    mulu(s, 590, gy - 0.5 * th, 0.9 * th, face='happy', flip=True)
    cx, cy = 505, gy - 118
    s.add(f'<path d="M{n(cx - 12)} {n(cy)} L{n(cx + 12)} {n(cy)} L{n(cx + 9)} {n(cy + 15)} L{n(cx - 9)} {n(cy + 15)} Z" fill="#fff" stroke="{C["line"]}" stroke-width="2.4"/>')
    s.text(505, gy + 32, 'Teacup handover (nub to paw)', 14, 'middle', '700')
    tekla(s, 800, gy, th)
    mulu(s, 806, gy - 1.28 * th, 0.9 * th, face='sad', top='droop', tint='grey')
    for dx, dy in ((-24, 22), (4, 44), (28, 26)):
        drop(s, 806 + dx, gy - 1.28 * th + dy, 6)
    for dx, dy in ((-58, -130), (-70, -96), (-78, -40), (70, -120), (84, -86)):
        drop(s, 800 + dx, gy + dy, 5)
    s.add(f'<path d="M748 {gy - 150} q-12 16 -16 40 M856 {gy - 140} q14 14 16 38" stroke="{C["muted"]}" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    s.text(800, gy + 32, 'Rain rolls off her shell (never wet)', 14, 'middle', '700')
    s.lines(1010, 760, ['Why these three', '- Cloud Hat: the comfort pose and the brand',
                        '  silhouette; tests soft-on-hard contact.', '- Teacup: the everyday ritual; tests a',
                        '  prop passing between two rigs.', '- Rain off the shell: the thesis image; tests',
                        '  drops meeting a surface without wetting it.', '',
                        'Anything else (hugs, carrying her,', 'pulling his nubs) is showcase-only.'], 13.5, 21)
    s.text(40, 1090, 'Pair at thumbnail size (black silhouettes)', 17, weight='800')
    x = 60
    for h in (96, 64, 48):
        tekla(s, x + 20, 1240, h, sil=True)
        mulu(s, x + 20 + h * 1.0, 1240 - 0.45 * h, 0.9 * h, sil=True, top='perk', flip=True)
        tekla_ball(s, x + 80 + h * 1.9, 1240, h, sil=True)
        mulu(s, x + 74 + h * 1.9, 1240 - 0.44 * h, 0.9 * h, sil=True, top='lean')
        s.text(x + 60 + h, 1264, f'{h}px', 12, 'middle', fill=C['muted'])
        x += h * 3.4 + 90
    s.text(1010, 1190, 'Test: a four-year-old names both at 48px and', 13.5, fill=C['muted'])
    s.text(1010, 1212, 'finds the Cloud Hat. If either needs colour', 13.5, fill=C['muted'])
    s.text(1010, 1234, 'to be recognised, the silhouette fails.', 13.5, fill=C['muted'])
    return s


def _tree(s, x, yg, scale=1.0):
    s.add(f'<path d="M{n(x - 16 * scale)} {n(yg)} Q{n(x - 8 * scale)} {n(yg - 90 * scale)} {n(x - 20 * scale)} {n(yg - 170 * scale)} '
          f'L{n(x + 12 * scale)} {n(yg - 170 * scale)} Q{n(x + 6 * scale)} {n(yg - 90 * scale)} {n(x + 18 * scale)} {n(yg)} Z" '
          f'fill="{C["wood"]}" stroke="{C["line"]}" stroke-width="3"/>')
    s.add(f'<path d="M{n(x + 4 * scale)} {n(yg - 140 * scale)} Q{n(x + 90 * scale)} {n(yg - 150 * scale)} {n(x + 150 * scale)} {n(yg - 132 * scale)}" '
          f'stroke="{C["line"]}" stroke-width="{n(15 * scale)}" fill="none" stroke-linecap="round"/>')
    s.add(f'<path d="M{n(x + 4 * scale)} {n(yg - 140 * scale)} Q{n(x + 90 * scale)} {n(yg - 150 * scale)} {n(x + 150 * scale)} {n(yg - 132 * scale)}" '
          f'stroke="{C["wood"]}" stroke-width="{n(9 * scale)}" fill="none" stroke-linecap="round"/>')
    for cx, cy, r in ((-40, -220, 62), (30, -236, 70), (-4, -276, 60), (74, -206, 46)):
        s.add(f'<circle cx="{n(x + cx * scale)}" cy="{n(yg + cy * scale)}" r="{n(r * scale)}" fill="{C["leaf"]}" stroke="{C["line"]}" stroke-width="3"/>')


def sheet_hilltop_wide() -> Sheet:
    s = Sheet(1480, 940, 'The Hilltop - master wide (HT-01) composition sketch', BANNER)
    x0, y0, w, h = 40, 96, 1400, 800
    s.defs.append(f'<linearGradient id="skyg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{C["sky"]}"/>'
                  f'<stop offset="1" stop-color="{C["sky_hi"]}"/></linearGradient>')
    s.defs.append(f'<clipPath id="frame"><rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="16"/></clipPath>')
    s.add('<g clip-path="url(#frame)">')
    s.add(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="url(#skyg)"/>')
    # Distant valley and village (rooftops only; grown-ups offscreen).
    s.add(f'<path d="M{x0} 640 Q400 600 800 626 T{x0 + w} 612 L{x0 + w} {y0 + h} L{x0} {y0 + h} Z" fill="#B9D9A6"/>')
    for i, rx in enumerate((1040, 1080, 1122, 1170, 1206)):
        ry = 612 + (i % 2) * 6
        s.add(f'<path d="M{rx} {ry} l14 -14 l14 14 z" fill="{C["far"]}"/><rect x="{rx + 3}" y="{ry}" width="22" height="12" fill="#C7D6E6"/>')
    # The hill.
    s.add(f'<path d="M{x0 - 20} {y0 + h} L{x0 - 20} 700 Q260 560 700 548 Q1080 540 1300 640 Q1400 690 {x0 + w + 20} 760 L{x0 + w + 20} {y0 + h} Z" '
          f'fill="{C["hill"]}" stroke="{C["line"]}" stroke-width="3"/>')
    # Stream at the foot of the hill (bottom left).
    s.add(f'<path d="M{x0 - 20} 870 Q200 836 360 866 T640 {y0 + h + 10}" stroke="{C["stream"]}" stroke-width="26" fill="none"/>')
    # Lookout Tree (stage left edge).
    _tree(s, 190, 640, 1.25)
    # The knoll with Tekla's round door; umbrella bed planted on top.
    s.add(f'<path d="M430 600 Q470 420 620 410 Q770 420 810 600 Z" fill="{C["hill_d"]}" stroke="{C["line"]}" stroke-width="3"/>')
    s.add(f'<circle cx="620" cy="540" r="58" fill="{C["wood"]}" stroke="{C["line"]}" stroke-width="3"/>')
    for dx in (-30, -10, 10, 30):
        s.add(f'<path d="M{620 + dx} 486 L{620 + dx} 594" stroke="{C["wood_d"]}" stroke-width="2.4" clip-path="url(#frame)"/>')
    s.add(f'<circle cx="620" cy="540" r="58" fill="none" stroke="{C["line"]}" stroke-width="3"/>')
    s.add(f'<circle cx="650" cy="546" r="6" fill="{C["ruler"]}" stroke="{C["line"]}" stroke-width="2"/>')
    s.add(f'<path d="M620 414 L620 300" stroke="{C["line"]}" stroke-width="9" stroke-linecap="round"/>'
          f'<path d="M620 414 L620 300" stroke="{C["wood"]}" stroke-width="5" stroke-linecap="round"/>')
    s.add(f'<path d="M540 250 Q620 330 700 250 Z" fill="{C["umb"]}" stroke="{C["line"]}" stroke-width="3"/>')
    for dx in (-40, 0, 40):
        s.add(f'<path d="M620 300 L{620 + dx} 256" stroke="{C["umb_d"]}" stroke-width="2.4"/>')
    s.add(f'<path d="M620 250 L620 236 Q620 226 630 228" stroke="{C["line"]}" stroke-width="4" fill="none" stroke-linecap="round"/>')
    s.text(620, 222, 'umbrella bed (on her roof)', 13, 'middle', '700')
    # Wind chimes (left of the door) on a crooked post.
    s.add(f'<path d="M500 598 L504 470 Q520 452 544 460" stroke="{C["wood_d"]}" stroke-width="7" fill="none" stroke-linecap="round"/>')
    for i, dx in enumerate((518, 528, 538)):
        s.add(f'<path d="M{dx} 462 L{dx} {n(496 + (i % 2) * 10)}" stroke="{C["line"]}" stroke-width="2"/>')
        s.add(f'<ellipse cx="{dx}" cy="{n(500 + (i % 2) * 10)}" rx="4" ry="7" fill="#DCE3EA" stroke="{C["line"]}" stroke-width="2"/>')
    s.text(470, 450, 'chimes', 13, 'middle', '700')
    # Forecast Board (right of the door): two squares; hers always empty.
    s.add(f'<path d="M712 606 L720 520 M792 606 L784 520" stroke="{C["wood_d"]}" stroke-width="6" stroke-linecap="round"/>')
    s.add(f'<rect x="700" y="470" width="100" height="58" rx="6" fill="#3C4A45" stroke="{C["line"]}" stroke-width="3"/>')
    s.add('<rect x="708" y="478" width="40" height="42" rx="3" fill="none" stroke="#E8EFE9" stroke-width="2"/>'
          '<rect x="752" y="478" width="40" height="42" rx="3" fill="none" stroke="#E8EFE9" stroke-width="2"/>')
    s.add('<circle cx="728" cy="499" r="9" fill="none" stroke="#FCE38A" stroke-width="3"/>')
    for a in range(0, 360, 45):
        ax, ay = 728 + 14 * math.cos(math.radians(a)), 499 + 14 * math.sin(math.radians(a))
        bx, by = 728 + 18 * math.cos(math.radians(a)), 499 + 18 * math.sin(math.radians(a))
        s.add(f'<path d="M{n(ax)} {n(ay)} L{n(bx)} {n(by)}" stroke="#FCE38A" stroke-width="2.4" stroke-linecap="round"/>')
    s.text(750, 448, 'Forecast Board', 13, 'middle', '700')
    # Bench and Tekla's old chair (downstage right, facing the view).
    s.add(f'<rect x="1030" y="572" width="170" height="12" rx="4" fill="{C["wood_d"]}" stroke="{C["line"]}" stroke-width="3"/>'
          f'<path d="M1046 584 L1046 600 M1184 584 L1184 600" stroke="{C["line"]}" stroke-width="5"/>')
    s.add(f'<rect x="1030" y="600" width="170" height="14" rx="4" fill="{C["wood"]}" stroke="{C["line"]}" stroke-width="3"/>'
          f'<path d="M1046 614 L1046 648 M1184 614 L1184 648" stroke="{C["line"]}" stroke-width="7" stroke-linecap="round"/>')
    s.add(f'<path d="M1222 648 L1222 604 L1262 604 L1262 648 M1222 604 L1222 560 L1262 560 L1262 604" stroke="{C["wood_d"]}" stroke-width="6" fill="none" stroke-linejoin="round"/>')
    s.text(1115, 564, 'bench', 13, 'middle', '700')
    s.text(1242, 548, 'old chair', 13, 'middle', '700')
    # Garden on the right slope with pinwheel; the Snail.
    for i in range(5):
        for j in range(3):
            gx, gy = 940 + i * 34 + j * 18, 700 + j * 28
            s.add(f'<path d="M{gx} {gy} q-6 -14 0 -20 q6 6 0 20" fill="{C["leaf"]}" stroke="{C["line"]}" stroke-width="1.6"/>')
    s.add(f'<path d="M1140 760 L1140 690" stroke="{C["wood_d"]}" stroke-width="4"/>')
    for a in (0, 90, 180, 270):
        s.add(f'<path d="M1140 690 l{n(18 * math.cos(math.radians(a)))} {n(18 * math.sin(math.radians(a)))} '
              f'l{n(-8 * math.sin(math.radians(a)))} {n(8 * math.cos(math.radians(a)))} z" fill="{C["umb"]}" stroke="{C["line"]}" stroke-width="1.6"/>')
    s.text(1010, 800, 'garden', 13, 'middle', '700')
    s.add(f'<circle cx="890" cy="742" r="7" fill="#E6C07A" stroke="{C["line"]}" stroke-width="2"/><circle cx="890" cy="742" r="2" fill="{C["umb"]}"/>'
          f'<path d="M880 750 L900 750" stroke="{C["line"]}" stroke-width="3" stroke-linecap="round"/>')
    s.text(890, 772, 'the Snail', 12, 'middle', fill=C['muted'])
    # The pair.
    tekla(s, 560, 690, 116)
    mulu(s, 660, 690 - 52, 104, face='happy', top='perk', flip=True)
    s.add('</g>')
    s.add(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="16" fill="none" stroke="{C["line"]}" stroke-width="3"/>')
    s.lines(x0 + 20, y0 + 30, ['HT-01 master wide: burrow knoll upstage centre (door + umbrella bed = the home icon),',
                               'Lookout Tree stage left, bench + valley view stage right, garden on the right slope,',
                               'stream at the foot. Mulu composed against sky or hill, never pale-on-pale.'], 14, 20)
    return s


def sheet_hilltop_plan() -> Sheet:
    s = Sheet(1480, 1000, 'The Hilltop - set plan and standard camera setups (top-down, schematic)', BANNER)
    s.add(f'<ellipse cx="620" cy="540" rx="520" ry="370" fill="{C["hill"]}" stroke="{C["line"]}" stroke-width="3"/>')
    s.add(f'<ellipse cx="620" cy="500" rx="330" ry="220" fill="#A6D27E" stroke="{C["line"]}" stroke-width="2" stroke-dasharray="8 6"/>')
    s.text(620, 610, 'PLATEAU (open play space)', 13, 'middle', '700', C['muted'])
    s.add(f'<path d="M110 700 Q180 860 420 930 T900 950 T1180 900" stroke="{C["stream"]}" stroke-width="30" fill="none"/>')
    s.text(360, 985, 'STREAM at the foot: stepping stones, little bridge, Heron bend (ST-01)', 13, 'middle', '700')
    blobs = [(620, 360, 74, 46, C['hill_d']), (620, 356, 16, 16, C['umb']), (726, 400, 30, 12, '#3C4A45'),
             (520, 396, 11, 11, C['wood_d']), (820, 680, 70, 13, C['wood']), (904, 680, 15, 15, C['wood_d']),
             (270, 470, 52, 52, C['leaf'])]
    for x, y, rx, ry, col in blobs:
        s.add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{col}" stroke="{C["line"]}" stroke-width="2.4"/>')
    for i in range(4):
        s.add(f'<path d="M{930 + i * 24} 520 L{1000 + i * 24} 590" stroke="{C["leaf"]}" stroke-width="7" stroke-linecap="round"/>')
    s.add(f'<path d="M620 406 Q640 520 720 610 T820 668" stroke="{C["earth"]}" stroke-width="5" fill="none" stroke-dasharray="3 8" stroke-linecap="round"/>')
    s.add(f'<path d="M880 690 Q980 790 1060 880" stroke="{C["earth"]}" stroke-width="5" fill="none" stroke-dasharray="3 8" stroke-linecap="round"/>')
    for x, y, label, anchor in ((536, 340, 'KNOLL + round door', 'end'),
                                (536, 358, '(umbrella bed on the roof)', 'end'),
                                (765, 404, 'Forecast Board', 'start'), (506, 424, 'chimes', 'end'),
                                (740, 650, 'BENCH (faces the valley)', 'end'), (924, 674, 'old chair', 'start'),
                                (270, 545, 'LOOKOUT TREE', 'middle'), (1010, 505, 'GARDEN (right slope)', 'middle'),
                                (1070, 900, 'path to the post board', 'start')):
        s.text(x, y, label, 13, anchor, '700')
    s.text(40, 130, 'DOWNSTAGE (bottom of plan) = the valley view and', 13, 'start', '700', C['muted'])
    s.text(40, 148, 'village rooftops, the sunset side.', 13, 'start', '700', C['muted'])
    cams = [('HT-01', 620, 860, -90, 48, 170, 'master wide'), ('HT-02', 820, 780, -90, 22, 90, 'bench two-shot'),
            ('HT-03', 620, 500, -90, 22, 110, 'door medium'), ('HT-04', 726, 470, -90, 14, 60, 'board insert'),
            ('HT-05', 300, 430, 25, 30, 170, 'Lookout down-angle'), ('HT-06', 1110, 640, -140, 24, 110, 'garden edge')]
    for cid, x, y, ang, half, L, name in cams:
        a1, a2 = math.radians(ang - half), math.radians(ang + half)
        s.add(f'<path d="M{x} {y} L{n(x + L * math.cos(a1))} {n(y + L * math.sin(a1))} A{L} {L} 0 0 1 '
              f'{n(x + L * math.cos(a2))} {n(y + L * math.sin(a2))} Z" fill="#FFE9A8" fill-opacity="0.35" stroke="{C["pick_edge"]}" stroke-width="2"/>')
    for cid, x, y, ang, half, L, name in cams:
        s.add(f'<rect x="{x - 12}" y="{y - 9}" width="24" height="18" rx="4" fill="{C["text"]}"/>')
        s.text(x, y + 28, f'{cid} {name}', 12.5, 'middle', '800')
    s.lines(1180, 130, ['Standard setups', 'HT-01 master wide (establish, entrances)', 'HT-02 bench two-shot + reverse',
                        '      (talks, sunset backs-to-camera)', 'HT-03 door medium (Forecast ritual, chimes)',
                        'HT-04 Forecast Board insert', 'HT-05 Lookout down-angle (Mulu POV,', '      the whole hill as a map)',
                        'HT-06 garden edge (garden, Snail)', '', 'Secondary set masters', 'WS-01 workshop interior',
                        'GD-01 garden rows (from HT-06 side)', 'ST-01 stream bend', '', 'Light: morning key from stage right;',
                        'golden hour sets downstage (valley).'], 13, 20)
    return s


SHEETS = {
    'mulu_silhouette_families.svg': sheet_mulu_families,
    'mulu_acting_states.svg': sheet_mulu_states,
    'tekla_directions.svg': sheet_tekla_directions,
    'tekla_tells.svg': sheet_tekla_tells,
    'pair_tests.svg': sheet_pair,
    'hilltop_master_wide.svg': sheet_hilltop_wide,
    'hilltop_set_plan.svg': sheet_hilltop_plan,
}


def build(out: Path = OUT) -> list[Path]:
    out.mkdir(parents=True, exist_ok=True)
    written = []
    for name, fn in SHEETS.items():
        path = out / name
        path.write_text(fn().svg(), encoding='utf-8', newline='\n')
        written.append(path)
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--out', type=Path, default=OUT)
    args = parser.parse_args()
    for path in build(args.out):
        print(path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
