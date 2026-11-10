"""SPARK UI/UX kit — primitives, icons, charts and layout shells.

Everything is emitted as a neutral element list so the same design can be
rendered to SVG (for drag-and-drop into Figma) and to a Figma plugin spec
(for fully editable frames).
"""

from __future__ import annotations

import math

# --------------------------------------------------------------------------- screens
def arc_path(cx, cy, r, a0, a1):
    """Circular arc as cubic Beziers (Figma only supports M/L/C/Q/Z).

    Angles are degrees, clockwise, 0 = 3 o'clock.
    """
    sweep = a1 - a0
    steps = max(1, int(math.ceil(abs(sweep) / 90.0)))
    step = sweep / steps
    k = 4.0 / 3.0 * math.tan(math.radians(step) / 4.0)
    start = math.radians(a0)
    d = f"M {cx + r * math.cos(start):.2f} {cy + r * math.sin(start):.2f}"
    for i in range(steps):
        a = math.radians(a0 + step * i)
        b = math.radians(a0 + step * (i + 1))
        p0 = (cx + r * math.cos(a), cy + r * math.sin(a))
        p3 = (cx + r * math.cos(b), cy + r * math.sin(b))
        p1 = (p0[0] - k * r * math.sin(a), p0[1] + k * r * math.cos(a))
        p2 = (p3[0] + k * r * math.sin(b), p3[1] - k * r * math.cos(b))
        d += (f" C {p1[0]:.2f} {p1[1]:.2f} {p2[0]:.2f} {p2[1]:.2f}"
              f" {p3[0]:.2f} {p3[1]:.2f}")
    return d


def screen(role, sid, title, desc, w, h, bg, elements):
    return {"role": role, "id": sid, "title": title, "description": desc,
            "w": w, "h": h, "bg": bg, "elements": elements}


# --------------------------------------------------------------------------- palette
INK = "#241A1F"
INK_SOFT = "#4A3B42"
MUTED = "#6B7280"
MUTED_2 = "#9AA3AF"
LINE = "#E7EBF2"
WHITE = "#FFFFFF"

CREAM = "#FFDB99"
CREAM_SOFT = "#FFF3E2"
CREAM_BG = "#FFF8EE"
ORANGE = "#FF8310"
ORANGE_DARK = "#D96A00"

MAROON = "#54040F"
MAROON_SOFT = "#FBE9EA"
PARENT_BG = "#FDF7F2"

RED = "#D8301E"
RED_SOFT = "#FDECEA"

BLUE = "#286CB5"
BLUE_DARK = "#1A478B"
SKY = "#D8E9FC"
SKY_SOFT = "#F1F6FE"
DOCTOR_BG = "#F5F8FD"

TEAL = "#2DC197"
TEAL_SOFT = "#E6F8F2"
GREEN = "#7BA400"
GREEN_SOFT = "#F1F6DC"
PURPLE = "#8A38F5"
PURPLE_SOFT = "#F3EBFF"
AMBER = "#FEB612"
AMBER_SOFT = "#FFF7DF"

DARK = "#0B1220"
DARK_PANEL = "#121C2E"
DARK_PANEL_2 = "#17243A"
DARK_LINE = "#243349"
DARK_TEXT = "#E8F1FF"
DARK_MUTED = "#8FA3BF"
CYAN = "#22D3EE"

INDIGO = "#030075"
INDIGO_2 = "#1A478B"
ADMIN_BG = "#F5F7FF"

FONT_HEAD = "Nunito"
FONT_BODY = "Inter"


# --------------------------------------------------------------------------- elements
def R(name, x, y, w, h, fill, rx=0, stroke=None, sw=1, opacity=None, group=None):
    e = {"type": "rect", "name": name, "x": x, "y": y, "w": w, "h": h,
         "fill": fill, "rx": rx}
    if stroke:
        e["stroke"] = stroke
        e["sw"] = sw
    if opacity is not None:
        e["opacity"] = opacity
    if group:
        e["group"] = group
    return e


def C(name, cx, cy, r, fill, stroke=None, sw=1, opacity=None, group=None):
    e = {"type": "circle", "name": name, "cx": cx, "cy": cy, "r": r, "fill": fill}
    if stroke:
        e["stroke"] = stroke
        e["sw"] = sw
    if opacity is not None:
        e["opacity"] = opacity
    if group:
        e["group"] = group
    return e


def P(name, x, y, d, fill="none", stroke=None, sw=2, opacity=None,
      cap="round", join="round", group=None):
    e = {"type": "path", "name": name, "x": x, "y": y, "d": d, "fill": fill,
         "cap": cap, "join": join}
    if stroke:
        e["stroke"] = stroke
        e["sw"] = sw
    if opacity is not None:
        e["opacity"] = opacity
    if group:
        e["group"] = group
    return e


def POLY(name, points, fill, stroke=None, sw=1, opacity=None, group=None):
    e = {"type": "poly", "name": name,
         "points": [[round(px, 2), round(py, 2)] for px, py in points],
         "fill": fill}
    if stroke:
        e["stroke"] = stroke
        e["sw"] = sw
    if opacity is not None:
        e["opacity"] = opacity
    if group:
        e["group"] = group
    return e


def T(name, x, y, w, text, size=14, weight=400, color=INK, align="left",
      font=FONT_BODY, lh=None, opacity=None, ls=None, group=None):
    e = {"type": "text", "name": name, "x": x, "y": y, "w": w,
         "text": text, "size": size, "weight": weight, "color": color,
         "align": align, "font": font}
    if lh is not None:
        e["lh"] = lh
    if opacity is not None:
        e["opacity"] = opacity
    if ls is not None:
        e["ls"] = ls
    if group:
        e["group"] = group
    return e


def G(name, *elements):
    """Attach every element to one named group (used for Figma layers)."""
    out = []
    for e in elements:
        if isinstance(e, list):
            for item in e:
                item = dict(item)
                item.setdefault("group", name)
                out.append(item)
        else:
            e = dict(e)
            e.setdefault("group", name)
            out.append(e)
    return out


# --------------------------------------------------------------------------- icons
def _star_points(cx, cy, r):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    return pts


def _shift(elements, dx, dy):
    out = []
    for e in elements:
        e = dict(e)
        if e["type"] in ("rect", "path"):
            e["x"] = e["x"] + dx
            e["y"] = e["y"] + dy
        elif e["type"] == "circle":
            e["cx"] = e["cx"] + dx
            e["cy"] = e["cy"] + dy
        elif e["type"] == "poly":
            e["points"] = [[px + dx, py + dy] for px, py in e["points"]]
        out.append(e)
    return out


def icon(name, x, y, s, color, sw=None, group=None):
    """A small line icon drawn in a 1x1 box scaled by *s*."""
    return _shift(_icon_local(name, 0, 0, s, color, sw, group), x, y)


def _icon_local(name, x, y, s, color, sw=None, group=None):
    sw = sw or max(1.4, s * 0.09)
    p = lambda n, d, fill="none": P(n, x, y, d, fill=fill,
                                    stroke=None if fill != "none" else color,
                                    sw=sw, group=group)
    if name == "chevron-right":
        return [p("Chevron", f"M {x + .36 * s:.2f} {y + .2 * s:.2f} L {x + .64 * s:.2f} {y + .5 * s:.2f} L {x + .36 * s:.2f} {y + .8 * s:.2f}")]
    if name == "chevron-left":
        return [p("Chevron", f"M {x + .64 * s:.2f} {y + .2 * s:.2f} L {x + .36 * s:.2f} {y + .5 * s:.2f} L {x + .64 * s:.2f} {y + .8 * s:.2f}")]
    if name == "chevron-down":
        return [p("Chevron", f"M {x + .22 * s:.2f} {y + .38 * s:.2f} L {x + .5 * s:.2f} {y + .66 * s:.2f} L {x + .78 * s:.2f} {y + .38 * s:.2f}")]
    if name == "chevron-up":
        return [p("Chevron", f"M {x + .22 * s:.2f} {y + .62 * s:.2f} L {x + .5 * s:.2f} {y + .34 * s:.2f} L {x + .78 * s:.2f} {y + .62 * s:.2f}")]
    if name == "arrow-right":
        return [p("Shaft", f"M {x + .18 * s:.2f} {y + .5 * s:.2f} L {x + .8 * s:.2f} {y + .5 * s:.2f}"),
                p("Head", f"M {x + .58 * s:.2f} {y + .28 * s:.2f} L {x + .8 * s:.2f} {y + .5 * s:.2f} L {x + .58 * s:.2f} {y + .72 * s:.2f}")]
    if name == "plus":
        return [p("Horizontal", f"M {x + .2 * s:.2f} {y + .5 * s:.2f} L {x + .8 * s:.2f} {y + .5 * s:.2f}"),
                p("Vertical", f"M {x + .5 * s:.2f} {y + .2 * s:.2f} L {x + .5 * s:.2f} {y + .8 * s:.2f}")]
    if name == "check":
        return [p("Check", f"M {x + .18 * s:.2f} {y + .53 * s:.2f} L {x + .4 * s:.2f} {y + .75 * s:.2f} L {x + .82 * s:.2f} {y + .27 * s:.2f}")]
    if name == "close":
        return [p("Line", f"M {x + .25 * s:.2f} {y + .25 * s:.2f} L {x + .75 * s:.2f} {y + .75 * s:.2f}"),
                p("Line", f"M {x + .75 * s:.2f} {y + .25 * s:.2f} L {x + .25 * s:.2f} {y + .75 * s:.2f}")]
    if name == "menu":
        return [p("Line", f"M {x + .2 * s:.2f} {y + .32 * s:.2f} L {x + .8 * s:.2f} {y + .32 * s:.2f}"),
                p("Line", f"M {x + .2 * s:.2f} {y + .5 * s:.2f} L {x + .8 * s:.2f} {y + .5 * s:.2f}"),
                p("Line", f"M {x + .2 * s:.2f} {y + .68 * s:.2f} L {x + .8 * s:.2f} {y + .68 * s:.2f}")]
    if name == "search":
        return [C("Lens", x + .44 * s, y + .44 * s, .24 * s, "none", color, sw, group=group),
                p("Handle", f"M {x + .62 * s:.2f} {y + .62 * s:.2f} L {x + .82 * s:.2f} {y + .82 * s:.2f}")]
    if name == "home":
        return [p("House", f"M {x + .16 * s:.2f} {y + .47 * s:.2f} L {x + .5 * s:.2f} {y + .18 * s:.2f} L {x + .84 * s:.2f} {y + .47 * s:.2f} L {x + .84 * s:.2f} {y + .82 * s:.2f} L {x + .6 * s:.2f} {y + .82 * s:.2f} L {x + .6 * s:.2f} {y + .6 * s:.2f} L {x + .4 * s:.2f} {y + .6 * s:.2f} L {x + .4 * s:.2f} {y + .82 * s:.2f} L {x + .16 * s:.2f} {y + .82 * s:.2f} Z")]
    if name == "gamepad":
        return [p("Body", f"M {x + .16 * s:.2f} {y + .36 * s:.2f} Q {x + .1 * s:.2f} {y + .78 * s:.2f} {x + .26 * s:.2f} {y + .78 * s:.2f} L {x + .36 * s:.2f} {y + .64 * s:.2f} L {x + .64 * s:.2f} {y + .64 * s:.2f} L {x + .74 * s:.2f} {y + .78 * s:.2f} Q {x + .9 * s:.2f} {y + .78 * s:.2f} {x + .84 * s:.2f} {y + .36 * s:.2f} L {x + .66 * s:.2f} {y + .26 * s:.2f} L {x + .34 * s:.2f} {y + .26 * s:.2f} Z"),
                p("D-pad", f"M {x + .32 * s:.2f} {y + .45 * s:.2f} L {x + .44 * s:.2f} {y + .45 * s:.2f} M {x + .38 * s:.2f} {y + .39 * s:.2f} L {x + .38 * s:.2f} {y + .51 * s:.2f}"),
                C("Button", x + .66 * s, y + .42 * s, .035 * s, color, group=group),
                C("Button", x + .74 * s, y + .5 * s, .035 * s, color, group=group)]
    if name == "chart":
        return [R("Bar", x + .2 * s, y + .5 * s, .13 * s, .3 * s, color, 2, group=group),
                R("Bar", x + .43 * s, y + .34 * s, .13 * s, .46 * s, color, 2, group=group),
                R("Bar", x + .66 * s, y + .18 * s, .13 * s, .62 * s, color, 2, group=group)]
    if name == "trend":
        return [p("Line", f"M {x + .15 * s:.2f} {y + .7 * s:.2f} L {x + .4 * s:.2f} {y + .45 * s:.2f} L {x + .58 * s:.2f} {y + .6 * s:.2f} L {x + .85 * s:.2f} {y + .28 * s:.2f}"),
                p("Head", f"M {x + .68 * s:.2f} {y + .28 * s:.2f} L {x + .85 * s:.2f} {y + .28 * s:.2f} L {x + .85 * s:.2f} {y + .45 * s:.2f}")]
    if name == "user":
        return [C("Head", x + .5 * s, y + .35 * s, .16 * s, "none", color, sw, group=group),
                p("Shoulders", f"M {x + .2 * s:.2f} {y + .82 * s:.2f} Q {x + .22 * s:.2f} {y + .58 * s:.2f} {x + .5 * s:.2f} {y + .58 * s:.2f} Q {x + .78 * s:.2f} {y + .58 * s:.2f} {x + .8 * s:.2f} {y + .82 * s:.2f}")]
    if name == "users":
        return [C("Head", x + .38 * s, y + .34 * s, .13 * s, "none", color, sw, group=group),
                p("Body", f"M {x + .12 * s:.2f} {y + .8 * s:.2f} Q {x + .14 * s:.2f} {y + .58 * s:.2f} {x + .38 * s:.2f} {y + .58 * s:.2f} Q {x + .62 * s:.2f} {y + .58 * s:.2f} {x + .64 * s:.2f} {y + .8 * s:.2f}"),
                C("Head", x + .68 * s, y + .3 * s, .11 * s, "none", color, sw, group=group),
                p("Body", f"M {x + .62 * s:.2f} {y + .56 * s:.2f} Q {x + .9 * s:.2f} {y + .58 * s:.2f} {x + .9 * s:.2f} {y + .8 * s:.2f}")]
    if name == "settings":
        out = [C("Ring", x + .5 * s, y + .5 * s, .18 * s, "none", color, sw, group=group)]
        for i in range(8):
            ang = math.radians(i * 45)
            r0, r1 = .28 * s, .4 * s
            out.append(p("Tick", f"M {x + .5 * s + r0 * math.cos(ang):.2f} {y + .5 * s + r0 * math.sin(ang):.2f} L {x + .5 * s + r1 * math.cos(ang):.2f} {y + .5 * s + r1 * math.sin(ang):.2f}"))
        return out
    if name == "star":
        return [POLY("Star", _star_points(x + .5 * s, y + .5 * s, .46 * s), color,
                     stroke=None, group=group)]
    if name == "play":
        return [POLY("Play", [(x + .3 * s, y + .2 * s), (x + .82 * s, y + .5 * s),
                              (x + .3 * s, y + .8 * s)], color, group=group)]
    if name == "pause":
        return [R("Bar", x + .28 * s, y + .22 * s, .16 * s, .56 * s, color, 2, group=group),
                R("Bar", x + .56 * s, y + .22 * s, .16 * s, .56 * s, color, 2, group=group)]
    if name == "mic":
        return [R("Body", x + .4 * s, y + .18 * s, .2 * s, .34 * s, "none", .1 * s, color, sw, group=group),
                p("Cradle", f"M {x + .28 * s:.2f} {y + .46 * s:.2f} Q {x + .3 * s:.2f} {y + .72 * s:.2f} {x + .5 * s:.2f} {y + .72 * s:.2f} Q {x + .7 * s:.2f} {y + .72 * s:.2f} {x + .72 * s:.2f} {y + .46 * s:.2f}"),
                p("Stem", f"M {x + .5 * s:.2f} {y + .72 * s:.2f} L {x + .5 * s:.2f} {y + .84 * s:.2f}")]
    if name == "camera":
        return [R("Body", x + .14 * s, y + .28 * s, .72 * s, .48 * s, "none", .08 * s, color, sw, group=group),
                C("Lens", x + .5 * s, y + .52 * s, .13 * s, "none", color, sw, group=group),
                p("Top", f"M {x + .36 * s:.2f} {y + .28 * s:.2f} L {x + .42 * s:.2f} {y + .18 * s:.2f} L {x + .58 * s:.2f} {y + .18 * s:.2f} L {x + .64 * s:.2f} {y + .28 * s:.2f}")]
    if name == "battery":
        return [R("Body", x + .1 * s, y + .3 * s, .72 * s, .4 * s, "none", .05 * s, color, sw, group=group),
                R("Fill", x + .16 * s, y + .36 * s, .42 * s, .28 * s, color, .02 * s, group=group),
                R("Tip", x + .84 * s, y + .42 * s, .06 * s, .16 * s, color, .02 * s, group=group)]
    if name == "wifi":
        return [p("Arc", arc_path(x + .5 * s, y + .62 * s, .34 * s, 205, 335)),
                p("Arc", arc_path(x + .5 * s, y + .62 * s, .22 * s, 215, 325)),
                C("Dot", x + .5 * s, y + .76 * s, .035 * s, color, group=group)]
    if name == "lock":
        return [R("Body", x + .22 * s, y + .46 * s, .56 * s, .38 * s, "none", .07 * s, color, sw, group=group),
                p("Shackle", f"M {x + .34 * s:.2f} {y + .46 * s:.2f} L {x + .34 * s:.2f} {y + .4 * s:.2f} "
                  + arc_path(x + .5 * s, y + .4 * s, .16 * s, 180, 360)
                  + f" L {x + .66 * s:.2f} {y + .46 * s:.2f}")]
    if name == "alert":
        return [p("Triangle", f"M {x + .5 * s:.2f} {y + .14 * s:.2f} L {x + .9 * s:.2f} {y + .84 * s:.2f} L {x + .1 * s:.2f} {y + .84 * s:.2f} Z"),
                p("Line", f"M {x + .5 * s:.2f} {y + .38 * s:.2f} L {x + .5 * s:.2f} {y + .6 * s:.2f}"),
                C("Dot", x + .5 * s, y + .71 * s, .03 * s, color, group=group)]
    if name == "clock":
        return [C("Face", x + .5 * s, y + .5 * s, .36 * s, "none", color, sw, group=group),
                p("Hands", f"M {x + .5 * s:.2f} {y + .26 * s:.2f} L {x + .5 * s:.2f} {y + .52 * s:.2f} L {x + .67 * s:.2f} {y + .62 * s:.2f}")]
    if name == "bell":
        return [p("Body", f"M {x + .28 * s:.2f} {y + .66 * s:.2f} L {x + .28 * s:.2f} {y + .44 * s:.2f} "
                  + arc_path(x + .5 * s, y + .44 * s, .22 * s, 180, 360)
                  + f" L {x + .72 * s:.2f} {y + .66 * s:.2f} Z"),
                p("Base", f"M {x + .2 * s:.2f} {y + .66 * s:.2f} L {x + .8 * s:.2f} {y + .66 * s:.2f}"),
                C("Clapper", x + .5 * s, y + .78 * s, .04 * s, color, group=group)]
    if name == "book":
        return [p("Cover", f"M {x + .16 * s:.2f} {y + .2 * s:.2f} L {x + .84 * s:.2f} {y + .2 * s:.2f} L {x + .84 * s:.2f} {y + .82 * s:.2f} L {x + .5 * s:.2f} {y + .76 * s:.2f} L {x + .16 * s:.2f} {y + .82 * s:.2f} Z"),
                p("Spine", f"M {x + .5 * s:.2f} {y + .2 * s:.2f} L {x + .5 * s:.2f} {y + .76 * s:.2f}")]
    if name == "flask":
        return [p("Flask", f"M {x + .3 * s:.2f} {y + .16 * s:.2f} L {x + .7 * s:.2f} {y + .16 * s:.2f} L {x + .64 * s:.2f} {y + .4 * s:.2f} L {x + .82 * s:.2f} {y + .78 * s:.2f} Q {x + .84 * s:.2f} {y + .86 * s:.2f} {x + .74 * s:.2f} {y + .86 * s:.2f} L {x + .26 * s:.2f} {y + .86 * s:.2f} Q {x + .16 * s:.2f} {y + .86 * s:.2f} {x + .18 * s:.2f} {y + .78 * s:.2f} L {x + .36 * s:.2f} {y + .4 * s:.2f} Z"),
                p("Liquid", f"M {x + .3 * s:.2f} {y + .62 * s:.2f} L {x + .7 * s:.2f} {y + .62 * s:.2f}")]
    if name == "monitor":
        return [R("Screen", x + .14 * s, y + .18 * s, .72 * s, .48 * s, "none", .06 * s, color, sw, group=group),
                p("Stand", f"M {x + .5 * s:.2f} {y + .66 * s:.2f} L {x + .5 * s:.2f} {y + .82 * s:.2f} M {x + .34 * s:.2f} {y + .82 * s:.2f} L {x + .66 * s:.2f} {y + .82 * s:.2f}")]
    if name == "cpu":
        return [R("Chip", x + .26 * s, y + .26 * s, .48 * s, .48 * s, "none", .05 * s, color, sw, group=group),
                R("Core", x + .4 * s, y + .4 * s, .2 * s, .2 * s, "none", .03 * s, color, sw, group=group)]
    if name == "signal":
        return [R("Bar", x + .16 * s, y + .62 * s, .12 * s, .2 * s, color, 1, group=group),
                R("Bar", x + .34 * s, y + .5 * s, .12 * s, .32 * s, color, 1, group=group),
                R("Bar", x + .52 * s, y + .38 * s, .12 * s, .44 * s, color, 1, group=group),
                R("Bar", x + .7 * s, y + .26 * s, .12 * s, .56 * s, color, 1, group=group)]
    if name == "gauge":
        return [p("Arc", arc_path(x + .5 * s, y + .7 * s, .34 * s, 180, 360)),
                p("Needle", f"M {x + .5 * s:.2f} {y + .7 * s:.2f} L {x + .66 * s:.2f} {y + .42 * s:.2f}"),
                C("Hub", x + .5 * s, y + .7 * s, .035 * s, color, group=group)]
    if name == "temperature":
        return [R("Tube", x + .42 * s, y + .14 * s, .16 * s, .48 * s, "none", .08 * s, color, sw, group=group),
                C("Bulb", x + .5 * s, y + .74 * s, .13 * s, "none", color, sw, group=group)]
    if name == "download":
        return [p("Arrow", f"M {x + .5 * s:.2f} {y + .16 * s:.2f} L {x + .5 * s:.2f} {y + .58 * s:.2f}"),
                p("Head", f"M {x + .32 * s:.2f} {y + .42 * s:.2f} L {x + .5 * s:.2f} {y + .6 * s:.2f} L {x + .68 * s:.2f} {y + .42 * s:.2f}"),
                p("Tray", f"M {x + .18 * s:.2f} {y + .7 * s:.2f} L {x + .18 * s:.2f} {y + .84 * s:.2f} L {x + .82 * s:.2f} {y + .84 * s:.2f} L {x + .82 * s:.2f} {y + .7 * s:.2f}")]
    if name == "filter":
        return [p("Line", f"M {x + .18 * s:.2f} {y + .28 * s:.2f} L {x + .82 * s:.2f} {y + .28 * s:.2f}"),
                p("Line", f"M {x + .28 * s:.2f} {y + .48 * s:.2f} L {x + .72 * s:.2f} {y + .48 * s:.2f}"),
                p("Line", f"M {x + .4 * s:.2f} {y + .68 * s:.2f} L {x + .6 * s:.2f} {y + .68 * s:.2f}")]
    if name == "calendar":
        return [R("Body", x + .16 * s, y + .24 * s, .68 * s, .6 * s, "none", .07 * s, color, sw, group=group),
                p("Top", f"M {x + .16 * s:.2f} {y + .42 * s:.2f} L {x + .84 * s:.2f} {y + .42 * s:.2f}"),
                p("Ticks", f"M {x + .34 * s:.2f} {y + .16 * s:.2f} L {x + .34 * s:.2f} {y + .32 * s:.2f} M {x + .66 * s:.2f} {y + .16 * s:.2f} L {x + .66 * s:.2f} {y + .32 * s:.2f}")]
    if name == "logout":
        return [p("Door", f"M {x + .22 * s:.2f} {y + .16 * s:.2f} L {x + .58 * s:.2f} {y + .16 * s:.2f} L {x + .58 * s:.2f} {y + .84 * s:.2f} L {x + .22 * s:.2f} {y + .84 * s:.2f} Z"),
                p("Arrow", f"M {x + .46 * s:.2f} {y + .5 * s:.2f} L {x + .86 * s:.2f} {y + .5 * s:.2f}"),
                p("Head", f"M {x + .7 * s:.2f} {y + .36 * s:.2f} L {x + .86 * s:.2f} {y + .5 * s:.2f} L {x + .7 * s:.2f} {y + .64 * s:.2f}")]
    if name == "edit":
        return [p("Pencil", f"M {x + .2 * s:.2f} {y + .8 * s:.2f} L {x + .24 * s:.2f} {y + .62 * s:.2f} L {x + .66 * s:.2f} {y + .2 * s:.2f} L {x + .8 * s:.2f} {y + .34 * s:.2f} L {x + .38 * s:.2f} {y + .76 * s:.2f} Z"),
                p("Base", f"M {x + .2 * s:.2f} {y + .8 * s:.2f} L {x + .4 * s:.2f} {y + .8 * s:.2f}")]
    if name == "mail":
        return [R("Envelope", x + .14 * s, y + .26 * s, .72 * s, .48 * s, "none", .06 * s, color, sw, group=group),
                p("Flap", f"M {x + .14 * s:.2f} {y + .3 * s:.2f} L {x + .5 * s:.2f} {y + .56 * s:.2f} L {x + .86 * s:.2f} {y + .3 * s:.2f}")]
    if name == "eye":
        return [p("Eye", f"M {x + .12 * s:.2f} {y + .5 * s:.2f} Q {x + .5 * s:.2f} {y + .18 * s:.2f} {x + .88 * s:.2f} {y + .5 * s:.2f} Q {x + .5 * s:.2f} {y + .82 * s:.2f} {x + .12 * s:.2f} {y + .5 * s:.2f} Z"),
                C("Pupil", x + .5 * s, y + .5 * s, .1 * s, color, group=group)]
    if name == "shield":
        return [p("Shield", f"M {x + .5 * s:.2f} {y + .12 * s:.2f} L {x + .82 * s:.2f} {y + .26 * s:.2f} L {x + .78 * s:.2f} {y + .58 * s:.2f} Q {x + .7 * s:.2f} {y + .8 * s:.2f} {x + .5 * s:.2f} {y + .88 * s:.2f} Q {x + .3 * s:.2f} {y + .8 * s:.2f} {x + .22 * s:.2f} {y + .58 * s:.2f} L {x + .18 * s:.2f} {y + .26 * s:.2f} Z")]
    if name == "robot":
        return [R("Head", x + .22 * s, y + .24 * s, .56 * s, .44 * s, "none", .12 * s, color, sw, group=group),
                C("Eye", x + .38 * s, y + .44 * s, .04 * s, color, group=group),
                C("Eye", x + .62 * s, y + .44 * s, .04 * s, color, group=group),
                p("Antenna", f"M {x + .5 * s:.2f} {y + .24 * s:.2f} L {x + .5 * s:.2f} {y + .12 * s:.2f}"),
                C("Tip", x + .5 * s, y + .1 * s, .035 * s, color, group=group)]
    if name == "bolt":
        return [POLY("Bolt", [(x + .56 * s, y + .08 * s), (x + .22 * s, y + .56 * s),
                              (x + .46 * s, y + .56 * s), (x + .36 * s, y + .92 * s),
                              (x + .78 * s, y + .4 * s), (x + .52 * s, y + .4 * s)],
                     color, group=group)]
    # fallback: a dot
    return [C("Dot", x + .5 * s, y + .5 * s, .12 * s, color, group=group)]


# --------------------------------------------------------------------------- mascot
def mascot(x, y, s, accent=ORANGE, group="Robot mascot"):
    """Friendly robot, total height *s*."""
    e = []
    e.append(C("Antenna tip", x + .5 * s, y + .04 * s, .045 * s, accent, group=group))
    e.append(P("Antenna", x + .5 * s, y + .085 * s, f"M 0 0 L 0 {.055 * s:.2f}",
                stroke=INK, sw=max(1.5, .025 * s), group=group))
    e.append(R("Head", x + .19 * s, y + .14 * s, .62 * s, .42 * s, WHITE, .16 * s,
               INK, max(1.5, .018 * s), group=group))
    e.append(R("Face", x + .25 * s, y + .2 * s, .5 * s, .3 * s, "#EAF4FF", .11 * s, group=group))
    e.append(C("Eye", x + .39 * s, y + .32 * s, .045 * s, INK, group=group))
    e.append(C("Eye", x + .61 * s, y + .32 * s, .045 * s, INK, group=group))
    e.append(C("Glint", x + .402 * s, y + .308 * s, .012 * s, WHITE, group=group))
    e.append(C("Glint", x + .622 * s, y + .308 * s, .012 * s, WHITE, group=group))
    e.append(P("Smile", x + .43 * s, y + .41 * s,
               f"M 0 0 Q {.07 * s:.2f} {.06 * s:.2f} {.14 * s:.2f} 0",
               stroke=INK, sw=max(1.5, .022 * s), group=group))
    e.append(R("Body", x + .25 * s, y + .58 * s, .5 * s, .28 * s, accent, .1 * s,
               None, group=group))
    e.append(R("Belly", x + .38 * s, y + .64 * s, .24 * s, .16 * s, WHITE, .07 * s,
               opacity=.9, group=group))
    e.append(C("Belly dot", x + .5 * s, y + .72 * s, .035 * s, accent, group=group))
    e.append(R("Arm", x + .16 * s, y + .6 * s, .09 * s, .2 * s, accent, .045 * s, group=group))
    e.append(R("Arm", x + .75 * s, y + .6 * s, .09 * s, .2 * s, accent, .045 * s, group=group))
    e.append(R("Foot", x + .3 * s, y + .86 * s, .16 * s, .08 * s, INK, .04 * s, group=group))
    e.append(R("Foot", x + .54 * s, y + .86 * s, .16 * s, .08 * s, INK, .04 * s, group=group))
    return e


# --------------------------------------------------------------------------- shells
def status_bar(dark=False, group="Status bar"):
    fg = WHITE if dark else INK
    e = [T("Time", 22, 14, 50, "9:41", 12, 700, fg, group=group)]
    e += G(group, *icon("signal", 300, 15, 15, fg))
    e += G(group, *icon("wifi", 322, 15, 15, fg))
    e += G(group, *icon("battery", 346, 14, 18, fg))
    return e


def bottom_nav(active="Home", accent=ORANGE, bg=WHITE, dark=False, group="Bottom navigation"):
    fg = DARK_TEXT if dark else INK
    muted = DARK_MUTED if dark else MUTED
    soft = "#1D2B42" if dark else CREAM_SOFT
    items = [("home", "Home"), ("gamepad", "Games"), ("chart", "Report"), ("user", "Me")]
    e = [R("Nav bar", 0, 772, 390, 72, bg, group=group),
         R("Nav divider", 0, 772, 390, 1, DARK_LINE if dark else LINE, group=group)]
    for i, (ic, label) in enumerate(items):
        cx = 49 + i * 97
        on = label == active
        if on:
            e.append(R("Active pill", cx - 28, 780, 56, 32, soft, 16, group=group))
        e += G(group, *icon(ic, cx - 11, 786, 22, accent if on else muted))
        e.append(T(label + " label", cx - 30, 816, 60, label, 10,
                   700 if on else 500, accent if on else muted, "center", group=group))
    return e


def sidebar(role, items, active, accent=BLUE, bg=WHITE, dark=False,
            soft=None, group="Sidebar", user_name="Dr. Hana",
            user_initials="DH", user_label=None):
    fg = WHITE if dark else INK
    muted = DARK_MUTED if dark else MUTED
    soft = soft or ("#15233A" if dark else SKY_SOFT)
    e = [R("Sidebar background", 0, 0, 248, 1024, bg, group=group)]
    e.append(C("Logo circle", 44, 44, 20, accent, group=group))
    e += G(group, *icon("bolt", 34, 34, 20, WHITE))
    e.append(T("Brand", 74, 25, 100, "SPARK", 18, 900, fg, group=group))
    e.append(T("Workspace", 74, 49, 150, role, 9, 700, muted, ls=1.2, group=group))
    e.append(R("Divider", 20, 92, 208, 1, DARK_LINE if dark else LINE, group=group))
    y = 112
    for ic, label in items:
        on = label == active
        if on:
            e.append(R("Active item", 14, y - 8, 220, 44, soft, 12, group=group))
            e.append(R("Active accent", 14, y + 4, 3, 20, accent, 1.5, group=group))
        e += G(group, *icon(ic, 32, y, 20, accent if on else muted))
        e.append(T(label + " nav", 64, y - 2, 150, label, 13, 700 if on else 500,
                   fg if on else muted, group=group))
        y += 50
    # account card
    e.append(R("Account card", 16, 914, 216, 86, "#0F1B30" if dark else "#F6F8FC", 16, group=group))
    e.append(C("Avatar", 46, 946, 18, accent, group=group))
    e.append(T("Initials", 36, 937, 20, user_initials, 10, 800, WHITE, "center", group=group))
    e.append(T("User name", 74, 932, 140, user_name, 12, 700, fg, group=group))
    e.append(T("User role", 74, 950, 140, user_label or role.title(), 10, 500, muted, group=group))
    e += G(group, *icon("logout", 202, 932, 16, muted))
    return e


def topbar(breadcrumb, accent=BLUE, search=True, initials="DH", group="Top bar",
           search_hint="Search children, reports…"):
    e = [R("Top bar", 248, 0, 1192, 72, WHITE, group=group),
         R("Top bar line", 248, 71, 1192, 1, LINE, group=group),
         T("Breadcrumb", 288, 27, 500, breadcrumb, 12, 500, MUTED, group=group)]
    if search:
        e.append(R("Search field", 964, 16, 290, 40, "#F4F7FB", 12, group=group))
        e += G(group, *icon("search", 980, 27, 18, MUTED_2))
        e.append(T("Search placeholder", 1008, 28, 200, search_hint, 12, 400, MUTED_2, group=group))
    e.append(R("Bell button", 1272, 16, 40, 40, "#F4F7FB", 20, group=group))
    e += G(group, *icon("bell", 1283, 27, 18, INK))
    e.append(C("Avatar", 1330, 36, 20, accent, group=group))
    e.append(T("Initials", 1318, 28, 24, initials, 11, 800, WHITE, "center", group=group))
    return e


# --------------------------------------------------------------------------- atoms
def badge(x, y, text, fg, bg, size=10, h=24, w=None, group=None):
    w = w or (len(text) * size * 0.62 + 20)
    return G(group or "Badge",
             R("Pill", x, y, w, h, bg, h / 2, group=group),
             T("Label", x, y + h / 2 - size * 0.62, w, text, size, 700, fg,
               "center", group=group))


def button(x, y, w, h, label, fill, fg, rx=14, stroke=None, icon_name=None,
           size=13, group=None):
    g = group or "Button"
    e = [R("Background", x, y, w, h, fill, rx, stroke, 1.2, group=g)]
    if icon_name:
        e += G(g, *icon(icon_name, x + 18, y + (h - 18) / 2, 18, fg))
        e.append(T("Label", x + 42, y + (h - size * 1.25) / 2, w - 54, label,
                   size, 700, fg, "center", group=g))
    else:
        e.append(T("Label", x, y + (h - size * 1.25) / 2, w, label, size, 700,
                   fg, "center", group=g))
    return e


def stat_card(x, y, w, h, label, value, delta=None, icon_name="chart",
              accent=BLUE, soft=SKY_SOFT, group=None):
    g = group or label
    e = [R("Card", x, y, w, h, WHITE, 18, LINE, 1, group=g),
         T("Label", x + 20, y + 20, w - 70, label, 12, 500, MUTED, group=g),
         T("Value", x + 20, y + 42, w - 60, value, 30, 800, INK, group=g)]
    e.append(R("Icon tile", x + w - 58, y + 18, 38, 38, soft, 12, group=g))
    e += G(g, *icon(icon_name, x + w - 48, y + 28, 18, accent))
    if delta:
        e.append(R("Delta pill", x + 20, y + h - 34, len(delta) * 6.3 + 18, 22,
                   soft, 11, group=g))
        e.append(T("Delta", x + 20, y + h - 29, len(delta) * 6.3 + 18, delta,
                   10, 700, accent, "center", group=g))
    return e


def section_title(x, y, title, sub=None, action=None, w=400, group=None):
    g = group or title
    e = [T("Title", x, y, w, title, 16, 800, INK, group=g)]
    if sub:
        e.append(T("Subtitle", x, y + 24, w, sub, 11, 400, MUTED, group=g))
    if action:
        e.append(T("Action", x + w - 60, y + 2, 60, action, 11, 700, BLUE,
                   "right", group=g))
    return e


# --------------------------------------------------------------------------- charts
def line_chart(x, y, w, h, values, color, fill_color=None, grid_color=LINE,
               maxv=None, labels=None, dots=True, group="Chart"):
    e = []
    maxv = maxv or max(values) * 1.15
    for i in range(1, 5):
        gy = y + h * i / 4
        e.append(R("Grid", x, gy, w, 1, grid_color, group=group))
    pts = []
    for i, v in enumerate(values):
        px = x + (w * i / max(1, len(values) - 1))
        py = y + h - (v / maxv) * h
        pts.append((px, py))
    if fill_color:
        d = f"M {x:.2f} {y + h:.2f} " + " ".join(f"L {px:.2f} {py:.2f}" for px, py in pts) + f" L {x + w:.2f} {y + h:.2f} Z"
        e.append(P("Area", 0, 0, d, fill=fill_color, opacity=.35, group=group))
    d = f"M {pts[0][0]:.2f} {pts[0][1]:.2f} " + " ".join(f"L {px:.2f} {py:.2f}" for px, py in pts[1:])
    e.append(P("Line", 0, 0, d, stroke=color, sw=2.5, group=group))
    if dots:
        for px, py in pts:
            e.append(C("Point", px, py, 3.2, WHITE, color, 2, group=group))
    if labels:
        for i, lab in enumerate(labels):
            px = x + (w * i / max(1, len(labels) - 1))
            e.append(T("Axis label", px - 20, y + h + 10, 40, lab, 9, 500,
                       MUTED, "center", group=group))
    return e


def bar_chart(x, y, w, h, values, color, labels=None, maxv=None, gap=.38,
              group="Chart"):
    e = []
    maxv = maxv or max(values) * 1.15
    n = len(values)
    bw = w / (n * (1 + gap))
    step = bw * (1 + gap)
    for i, v in enumerate(values):
        bh = (v / maxv) * h
        bx = x + i * step + gap * bw / 2
        e.append(R("Bar", bx, y + h - bh, bw, bh, color, 3, group=group))
        if labels:
            e.append(T("Axis label", bx - 8, y + h + 8, bw + 16, labels[i], 9,
                       500, MUTED, "center", group=group))
    return e


def donut(cx, cy, r, thickness, segments, center_bg=DARK_PANEL, group="Donut"):
    e = []
    total = sum(v for v, _ in segments) or 1
    start = -90
    for value, color in segments:
        sweep = 360 * value / total
        end = start + sweep
        e.append(P("Segment", 0, 0, arc_path(cx, cy, r, start, end),
                   stroke=color, sw=thickness, cap="butt", group=group))
        start = end
    e.append(C("Hole", cx, cy, r - thickness / 2, center_bg, group=group))
    return e


def radar(cx, cy, r, axes, values, color, group="Radar"):
    e = []
    n = len(axes)
    for frac in (.25, .5, .75, 1.0):
        pts = []
        for i in range(n):
            ang = -math.pi / 2 + 2 * math.pi * i / n
            pts.append((cx + r * frac * math.cos(ang),
                        cy + r * frac * math.sin(ang)))
        e.append(POLY("Grid", pts, "none", LINE, 1, group=group))
    for i in range(n):
        ang = -math.pi / 2 + 2 * math.pi * i / n
        e.append(P("Axis", 0, 0,
                   f"M {cx:.2f} {cy:.2f} L {cx + r * math.cos(ang):.2f} {cy + r * math.sin(ang):.2f}",
                   stroke=LINE, sw=1, group=group))
    pts = []
    for i, v in enumerate(values):
        ang = -math.pi / 2 + 2 * math.pi * i / n
        rr = r * max(0, min(100, v)) / 100
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    e.append(POLY("Data area", pts, color, color, 2, opacity=.18, group=group))
    e.append(POLY("Data line", pts, "none", color, 2.2, group=group))
    for i, lab in enumerate(axes):
        ang = -math.pi / 2 + 2 * math.pi * i / n
        lx = cx + (r + 26) * math.cos(ang)
        ly = cy + (r + 26) * math.sin(ang)
        e.append(T("Axis label", lx - 52, ly - 7, 104, lab, 10, 600, MUTED,
                   "center", group=group))
    return e
