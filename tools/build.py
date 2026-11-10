#!/usr/bin/env python3
"""Build the SPARK Figma kit: SVG screens, plugin, preview and design doc.

Run from anywhere:

    python3 docs/figma/tools/build.py
"""

from __future__ import annotations

import html
import json
import math
import re
import shutil
import zipfile
from pathlib import Path

from screens import ROLES, SCREENS

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent                      # docs/figma
SCREEN_DIR = ROOT / "screens"
PLUGIN_DIR = ROOT / "plugin"
SPEC_PATH = ROOT / "spec.json"

ROLE_BY_ID = {r["id"]: r for r in ROLES}

FLOWS = {
    "child": ["Home", "IQ question", "Result", "My progress"],
    "parent": ["Dashboard", "Child progress", "Reports", "Account"],
    "robot": ["Control room", "Telemetry", "Session & commands"],
    "doctor": ["Overview", "Child assessment", "Report review", "Exports"],
    "admin": ["Overview", "Users & roles", "Research", "Audit & exports"],
    "system": ["Design system"],
}


# --------------------------------------------------------------------------- helpers
def num(v):
    if isinstance(v, float):
        if abs(v - round(v)) < 0.005:
            return str(int(round(v)))
        return f"{v:.2f}".rstrip("0").rstrip(".")
    return str(v)


def esc(v):
    return html.escape(str(v), quote=True)


def sanitize(value, used):
    base = re.sub(r"[^A-Za-z0-9_-]+", "-", value).strip("-") or "Layer"
    if base not in used:
        used.add(base)
        return base
    i = 2
    while f"{base}-{i}" in used:
        i += 1
    used.add(f"{base}-{i}")
    return f"{base}-{i}"


def element_svg(el):
    kind = el["type"]
    opacity = f' opacity="{num(el["opacity"])}"' if el.get("opacity") is not None else ""
    if kind == "rect":
        stroke = (f' stroke="{el["stroke"]}" stroke-width="{num(el.get("sw", 1))}"'
                  if el.get("stroke") else "")
        return (f'<rect x="{num(el["x"])}" y="{num(el["y"])}" width="{num(el["w"])}" '
                f'height="{num(el["h"])}" rx="{num(el.get("rx", 0))}" '
                f'fill="{el["fill"]}"{stroke}{opacity}/>')
    if kind == "circle":
        stroke = (f' stroke="{el["stroke"]}" stroke-width="{num(el.get("sw", 1))}"'
                  if el.get("stroke") else "")
        return (f'<circle cx="{num(el["cx"])}" cy="{num(el["cy"])}" r="{num(el["r"])}" '
                f'fill="{el["fill"]}"{stroke}{opacity}/>')
    if kind == "path":
        stroke = (f' stroke="{el["stroke"]}" stroke-width="{num(el.get("sw", 1))}" '
                  f'stroke-linecap="{el.get("cap", "round")}" '
                  f'stroke-linejoin="{el.get("join", "round")}"'
                  if el.get("stroke") else "")
        return (f'<path d="{esc(el["d"])}" transform="translate({num(el["x"])} {num(el["y"])})" '
                f'fill="{el["fill"]}"{stroke}{opacity}/>')
    if kind == "poly":
        pts = " ".join(f"{num(px)},{num(py)}" for px, py in el["points"])
        stroke = (f' stroke="{el["stroke"]}" stroke-width="{num(el.get("sw", 1))}"'
                  if el.get("stroke") else "")
        return f'<polygon points="{pts}" fill="{el["fill"]}"{stroke}{opacity}/>'
    if kind == "text":
        size = el["size"]
        lh = el.get("lh") or size * 1.35
        align = el.get("align", "left")
        w = el.get("w", 0)
        if align == "center":
            tx, anchor = el["x"] + w / 2, "middle"
        elif align == "right":
            tx, anchor = el["x"] + w, "end"
        else:
            tx, anchor = el["x"], "start"
        ls = f' letter-spacing="{num(el["ls"])}"' if el.get("ls") is not None else ""
        lines = str(el["text"]).split("\n")
        spans = []
        for i, line in enumerate(lines):
            y = el["y"] + size * 0.8 + i * lh
            spans.append(f'<tspan x="{num(tx)}" y="{num(y)}">{esc(line)}</tspan>')
        family = el.get("font", "Inter")
        stack = f"{family}, Inter, sans-serif" if family != "Inter" else "Inter, sans-serif"
        return (f'<text font-family="{stack}" font-size="{num(size)}" '
                f'font-weight="{el.get("weight", 400)}" fill="{el["color"]}" '
                f'text-anchor="{anchor}"{ls}{opacity}>{"".join(spans)}</text>')
    raise ValueError(f"Unknown element type {kind!r}")


def screen_svg(screen):
    used = set()
    out = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{screen["w"]}" '
        f'height="{screen["h"]}" viewBox="0 0 {screen["w"]} {screen["h"]}" fill="none">',
        f'<title>{esc(screen["title"])}</title>',
        f'<desc>{esc(screen["description"])}</desc>',
        f'<rect id="Background" x="0" y="0" width="{screen["w"]}" '
        f'height="{screen["h"]}" fill="{screen["bg"]}"/>',
    ]
    current = None
    for el in screen["elements"]:
        group = el.get("group")
        if group != current:
            if current is not None:
                out.append("</g>")
            current = group
            if group:
                out.append(f'<g id="{sanitize(group, used)}" data-name="{esc(group)}">')
        out.append(element_svg(el))
    if current is not None:
        out.append("</g>")
    out.append("</svg>")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- preview
def preview_html():
    parts = ["""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SPARK UI/UX kit</title>
<style>
  :root { color-scheme: light; }
  * { box-sizing: border-box; }
  body { margin: 0; font-family: Inter, system-ui, sans-serif; background: #F4F6FA; color: #241A1F; }
  header { padding: 40px 48px 24px; background: #fff; border-bottom: 1px solid #E7EBF2; }
  h1 { margin: 0 0 8px; font-size: 30px; letter-spacing: -0.02em; }
  header p { margin: 0; color: #6B7280; max-width: 760px; line-height: 1.6; font-size: 14px; }
  .meta { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 18px; }
  .pill { background: #F1F4F9; border-radius: 999px; padding: 6px 12px; font-size: 12px; color: #4A3B42; }
  main { padding: 32px 48px 80px; }
  section { margin-bottom: 48px; }
  .role-head { display: flex; align-items: baseline; gap: 12px; margin-bottom: 6px; }
  .role-head h2 { margin: 0; font-size: 20px; }
  .role-head span { color: #6B7280; font-size: 13px; }
  .role-blurb { margin: 0 0 18px; color: #6B7280; font-size: 13px; }
  .grid { display: flex; flex-wrap: wrap; gap: 20px; align-items: flex-start; }
  .card { background: #fff; border: 1px solid #E7EBF2; border-radius: 12px; padding: 10px; }
  .card img { display: block; border-radius: 8px; }
  .card.mobile img { width: 260px; }
  .card.tablet img { width: 560px; }
  .card.desktop img { width: 620px; }
  .caption { display: flex; justify-content: space-between; gap: 10px; padding: 9px 4px 2px; font-size: 12px; }
  .caption b { font-weight: 700; }
  .caption span { color: #6B7280; }
  footer { padding: 0 48px 40px; color: #6B7280; font-size: 12px; }
  code { background: #EEF1F6; padding: 2px 5px; border-radius: 4px; }
</style>
</head>
<body>
<header>
  <h1>SPARK UI/UX kit</h1>
  <p>Separate screens per role, ready to import into Figma. Open this page to review the screens,
     or use the plugin in <code>plugin/</code> to build an editable Figma file automatically.</p>
  <div class="meta">
    <span class="pill">6 role folders</span>
    <span class="pill">19 screens + design system</span>
    <span class="pill">Editable SVG &amp; Figma plugin</span>
  </div>
</header>
<main>
"""]

    for role in ROLES:
        screens = [s for s in SCREENS if s["role"] == role["id"]]
        if not screens:
            continue
        parts.append('  <section>')
        parts.append(f'    <div class="role-head"><h2>{esc(role["title"])}</h2>'
                     f'<span>{len(screens)} screen{"s" if len(screens) != 1 else ""}</span></div>')
        parts.append(f'    <p class="role-blurb">{esc(role["blurb"])}</p>')
        parts.append('    <div class="grid">')
        for screen in screens:
            if screen["w"] <= 500:
                cls = "mobile"
            elif screen["w"] <= 1200:
                cls = "tablet"
            else:
                cls = "desktop"
            rel = f'screens/{role["folder"]}/{screen["id"]}.svg'
            parts.append(f'      <div class="card {cls}">'
                         f'<a href="{rel}" target="_blank"><img src="{rel}" alt="{esc(screen["title"])}"></a>'
                         f'<div class="caption"><b>{esc(screen["id"])} · {esc(screen["title"])}</b>'
                         f'<span>{screen["w"]}×{screen["h"]}</span></div></div>')
        parts.append('    </div>')
        parts.append('  </section>')
    parts.append("""</main>
<footer>
  Generated by <code>tools/build.py</code>. Import guide: <code>README.md</code> ·
  Design inventory: <code>DESIGN.md</code>.
</footer>
</body>
</html>
""")
    return "\n".join(parts)


# --------------------------------------------------------------------------- design doc
def design_doc():
    lines = [
        "# SPARK UI/UX kit — design inventory",
        "",
        "Separate UI/UX for every product surface. Each screen is a fixed, editable frame;",
        "the SVG files import into Figma and the plugin rebuilds them as named layers.",
        "",
        "## Roles and folders",
        "",
        "| Role | Folder | Screens | Canvas |",
        "| --- | --- | --- | --- |",
    ]
    for role in ROLES:
        screens = [s for s in SCREENS if s["role"] == role["id"]]
        sizes = sorted({f'{s["w"]}×{s["h"]}' for s in screens})
        lines.append(f'| {role["title"]} | `screens/{role["folder"]}/` | '
                     f'{len(screens)} | {", ".join(sizes)} |')

    lines += ["", "## Screen inventory", ""]
    for role in ROLES:
        screens = [s for s in SCREENS if s["role"] == role["id"]]
        if not screens:
            continue
        lines += [f'### {role["title"]}', "", f'{role["blurb"]}', ""]
        lines += ["| # | Screen | Size | Purpose | File |", "| --- | --- | --- | --- | --- |"]
        for i, s in enumerate(screens, 1):
            lines.append(f'| {i} | {s["title"]} | {s["w"]}×{s["h"]} | '
                         f'{s["description"]} | `screens/{role["folder"]}/{s["id"]}.svg` |')
        lines.append("")

    lines += [
        "## Navigation flow",
        "",
    ]
    for role in ROLES:
        if role["id"] in FLOWS:
            lines.append(f'- **{role["title"]}:** ' + " → ".join(FLOWS[role["id"]]))
    lines += [
        "",
        "## Rules the UI must keep",
        "",
        "- **Parent scoping:** a parent only sees children linked to their own account.",
        "- **Doctor scoping:** a doctor only sees assigned children; reports are educational, not clinical diagnoses.",
        "- **Researcher privacy:** only anonymised aggregates; suppress cohorts with fewer than 10 participants.",
        "- **Child safety:** robot control is never exposed in the child app; stop controls stay visible in the operator console.",
        "- **Auth states:** empty, loading, error, offline and permission-denied states must be designed before build.",
        "- **RTL:** Arabic is a first-class language; mirror the layout for `ar` and keep numbers LTR.",
        "",
        "## Colours",
        "",
        "| Token | Hex | Use |",
        "| --- | --- | --- |",
        "| Maroon | `#54040F` | Parent brand, trust |",
        "| Cream | `#FFDB99` | Warm surfaces, highlights |",
        "| Orange | `#FF8310` | Child energy, primary child action |",
        "| Blue | `#286CB5` | Doctor, links, information |",
        "| Sky | `#D8E9FC` | Soft information surfaces |",
        "| Teal | `#2DC197` | Success, admin accent |",
        "| Red | `#D8301E` | Errors, emergency stop |",
        "| Ink | `#241A1F` | Primary text |",
        "| Muted | `#6B7280` | Secondary text |",
        "| Line | `#E7EBF2` | Borders and dividers |",
        "",
        "## Typography",
        "",
        "| Style | Font | Size | Weight |",
        "| --- | --- | --- | --- |",
        "| Display | Nunito | 40 | 900 |",
        "| Heading | Nunito | 28 | 800 |",
        "| Section | Nunito | 20 | 800 |",
        "| Body | Inter | 14 | 400 |",
        "| Caption | Inter | 12 | 400 |",
        "| Eyebrow | Inter | 10 | 700 |",
        "",
        "## What is intentionally still open",
        "",
        "- Photo/illustration placeholders are not final assets; drop the exported PNGs from",
        "  `docs/design/assets/` into the frames.",
        "- Empty, loading, error and offline states are described but not drawn for every screen.",
        "- Tablet breakpoints for the parent/doctor workspaces are not separate frames yet.",
        "- The design system frame is a reference board, not a published Figma library.",
        "",
    ]
    return "\n".join(lines)


# --------------------------------------------------------------------------- validation
def validate():
    errors = []
    known = {"rect", "circle", "path", "poly", "text"}
    ids = set()
    for s in SCREENS:
        key = (s["role"], s["id"])
        if key in ids:
            errors.append(f'duplicate screen id {s["role"]}/{s["id"]}')
        ids.add(key)
        if s["w"] <= 0 or s["h"] <= 0:
            errors.append(f'{s["id"]}: bad frame size')
        for i, el in enumerate(s["elements"]):
            where = f'{s["id"]}[{i}] {el.get("name")}'
            if el.get("type") not in known:
                errors.append(f"{where}: unknown type {el.get('type')}")
                continue
            for key, value in el.items():
                if isinstance(value, float) and not math.isfinite(value):
                    errors.append(f"{where}: non-finite {key}")
            if el["type"] in ("rect", "text") and (el.get("w", 1) < 0 or el.get("h", 1) < 0):
                errors.append(f"{where}: negative size")
            if el["type"] == "text" and not str(el.get("text", "")).strip():
                errors.append(f"{where}: empty text")
            if el["type"] == "poly" and len(el.get("points", [])) < 3:
                errors.append(f"{where}: polygon needs 3 points")
    return errors


# --------------------------------------------------------------------------- build
def main():
    errors = validate()
    if errors:
        raise SystemExit("Validation failed:\n" + "\n".join(errors[:20]))

    SCREEN_DIR.mkdir(parents=True, exist_ok=True)
    for role in ROLES:
        (SCREEN_DIR / role["folder"]).mkdir(parents=True, exist_ok=True)

    index = []
    for screen in SCREENS:
        role = ROLE_BY_ID[screen["role"]]
        path = SCREEN_DIR / role["folder"] / f'{screen["id"]}.svg'
        path.write_text(screen_svg(screen), encoding="utf-8")
        index.append({"role": role["id"], "file": str(path.relative_to(ROOT))})

    # Figma plugin spec + code
    PLUGIN_DIR.mkdir(parents=True, exist_ok=True)
    spec = {"roles": ROLES, "screens": SCREENS}
    SPEC_PATH.write_text(json.dumps(spec, ensure_ascii=False, separators=(",", ":")),
                         encoding="utf-8")
    template = (HERE / "plugin_template.js").read_text(encoding="utf-8")
    code = template.replace("__SPARK_SPEC__", json.dumps(spec, ensure_ascii=False,
                                                        separators=(",", ":")))
    (PLUGIN_DIR / "code.js").write_text(code, encoding="utf-8")
    manifest = {
        "name": "SPARK UI/UX Builder",
        "id": "1428570000000000001",
        "api": "1.0.0",
        "main": "code.js",
        "editorType": ["figma"],
        "documentAccess": "dynamic-page",
        "networkAccess": {
            "allowedDomains": ["none"],
            "reasoning": "Builds local design frames only; no network calls.",
        },
    }
    (PLUGIN_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    # Zip the plugin for sharing (Figma imports the folder, not the zip).
    zip_path = ROOT / "spark-uiux-figma-plugin.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(PLUGIN_DIR / "manifest.json", "manifest.json")
        zf.write(PLUGIN_DIR / "code.js", "code.js")

    (ROOT / "preview.html").write_text(preview_html(), encoding="utf-8")
    (ROOT / "DESIGN.md").write_text(design_doc(), encoding="utf-8")

    # Sanity: every SVG must be well-formed XML.
    import xml.etree.ElementTree as ET
    for screen in SCREENS:
        role = ROLE_BY_ID[screen["role"]]
        path = SCREEN_DIR / role["folder"] / f'{screen["id"]}.svg'
        try:
            ET.parse(path)
        except Exception as exc:            # noqa: BLE001
            raise SystemExit(f"Invalid SVG {path}: {exc}")

    print(f"Screens: {len(SCREENS)}")
    print(f"Roles:   {len(ROLES)}")
    print(f"Plugin:  {PLUGIN_DIR / 'manifest.json'}")
    print(f"Preview: {ROOT / 'preview.html'}")
    print(f"Zip:     {zip_path} ({zip_path.stat().st_size / 1024:.0f} KB)")
    for role in ROLES:
        screens = [s for s in SCREENS if s["role"] == role["id"]]
        print(f'  {role["title"]:<20} {len(screens)} screen(s) -> screens/{role["folder"]}/')


if __name__ == "__main__":
    main()
