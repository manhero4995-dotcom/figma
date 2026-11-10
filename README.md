# SPARK UI/UX kit — open in Figma & edit

Separate, editable UI/UX for every role in the product:

| Role | Folder | Screens | Canvas |
| --- | --- | --- | --- |
| Design system | `screens/00-design-system/` | 1 | 1440×1240 |
| Child app | `screens/01-child/` | 4 | 390×844 (mobile) |
| Parent app | `screens/02-parent/` | 4 | 390×844 (mobile) |
| Robot control | `screens/03-robot-control/` | 3 | 1180×840 (tablet, dark) |
| Doctor workspace | `screens/04-doctor/` | 4 | 1440×1024 (desktop) |
| Admin & research | `screens/05-admin-research/` | 4 | 1440×1024 (desktop) |

**20 frames total** — 1 design-system board + 19 role screens.

---

## What is in this folder

```
docs/figma/
├─ screens/                  # 20 editable SVG screens, one folder per role
│  ├─ 00-design-system/
│  ├─ 01-child/
│  ├─ 02-parent/
│  ├─ 03-robot-control/
│  ├─ 04-doctor/
│  └─ 05-admin-research/
├─ plugin/                   # "SPARK UI/UX Builder" Figma plugin
│  ├─ manifest.json          # ← import this file in Figma
│  └─ code.js                # self-contained builder (no network access)
├─ spark-uiux-figma-plugin.zip   # same plugin, zipped for sharing
├─ preview.html              # open in a browser to review all screens
├─ DESIGN.md                 # screen inventory, flows, colours, type, rules
├─ spec.json                 # machine-readable layout spec
└─ tools/                    # Python generators (regenerate everything)
```

You do **not** need Node, npm or a build step to use the kit. Both import
paths below work offline.

---

## Method 1 (recommended) — build the file with the plugin

This produces **fully editable Figma frames with named layers and text**, not
flat images. It is the fastest way to get the whole kit organized in one file.

1. Open Figma in the browser or desktop app and create a **new design file**
   (or open an existing draft you own).
2. From the menu bar choose **Plugins → Development → Import plugin from
   manifest…**
3. Select this file:

   ```
   docs/figma/plugin/manifest.json
   ```

4. Run it: **Plugins → Development → SPARK UI/UX Builder**.
5. Wait a few seconds. The plugin creates 6 pages:

   | Page | Contents |
   | --- | --- |
   | `00 · Design system` | Colours, role accents, type scale, components |
   | `01 · Child app` | Home, IQ question, result, progress |
   | `02 · Parent app` | Dashboard, child progress, reports, account |
   | `03 · Robot control` | Control room, telemetry, session & commands |
   | `04 · Doctor` | Overview, child assessment, report review, exports |
   | `05 · Admin & research` | Overview, users & roles, research, audit |

6. Each screen sits on its page as a frame named
   `Role / id · Title`, with grouped layers (header, cards, charts, buttons…).
   Click any layer to edit it.

> If a page name already exists, the plugin appends `· 2`, `· 3`, so it is safe
> to run twice — you never overwrite existing work.

### Fonts

The kit uses **Nunito** (headings) and **Inter** (body). Inter is a Figma
default. If Nunito is missing the plugin falls back to Inter automatically.
To get the intended look, install Nunito once:

- Figma desktop → **Main menu → Help and account → Fonts → Install font**
  (or install Nunito from Google Fonts on your system and restart Figma).

### Sharing the plugin with teammates

Send them `spark-uiux-figma-plugin.zip`, they unzip it and repeat step 2 with
the extracted `manifest.json`. Every person imports it into their own Figma
account — the plugin is not published to the Figma Community.

---

## Method 2 — drag the SVGs into Figma

Use this if you cannot run plugins, or you only need a few screens.

1. Create a new Figma file.
2. Create one page per role and rename them:
   `00 · Design system`, `01 · Child app`, `02 · Parent app`,
   `03 · Robot control`, `04 · Doctor`, `05 · Admin & research`.
3. Open the matching folder on your computer, e.g. `screens/01-child/`.
4. Select all SVG files in that folder and **drag them onto the Figma canvas**
   of the correct page.
5. Figma places each SVG as a frame. Select it and choose
   **right-click → Frame selection** (or `Ctrl/Cmd + Alt + G`) if you want a
   container frame around it.

SVG text imports as editable text in Figma, but complex grouping can flatten.
For maximum editability use Method 1.

> **Do not** use *File → Place image* for SVGs — that rasterizes them. Drag and
> drop from the file manager keeps them as vectors.

---

## How to review without Figma

Open `preview.html` in any browser — it shows all 20 screens grouped by role,
with titles and canvas sizes. It works offline (no server required), or serve
the folder:

```bash
cd docs/figma
python3 -m http.server 8765
# then open http://127.0.0.1:8765/preview.html
```

---

## How to edit the designs

### Inside Figma (after Method 1)

- **Text** — double-click any text layer and type. Fonts, sizes and colours are
  already applied; keep the existing text styles so screens stay consistent.
- **Colours** — the design-system page lists every token. Change a swatch and
  copy its hex into the layers you want to update, or create Figma **colour
  styles** from those swatches and apply them.
- **Layout** — everything is plain frames, rectangles, vectors and text. Move,
  resize, duplicate or delete freely. Select a card group and press
  `Ctrl/Cmd + D` to duplicate it.
- **Illustrations** — the mascot, avatars and camera scene are drawn with
  vectors. To use real artwork, drag a PNG from `docs/design/assets/`
  (`robot-mascot.png`, `child-hero.png`, `spark-logo.png`, …) onto the frame
  and delete the placeholder shapes.
- **Components** — turn a card or button into a real component with
  `Ctrl/Cmd + Alt + K`, then reuse it with **Assets → Local components**.
- **Prototype** — select a button, open the **Prototype** tab, and link frames
  to show the flows listed in `DESIGN.md` (e.g. Child: Home → IQ question →
  Result → Progress).

### Changing the source and regenerating

All screens are generated from Python. Edit the layout, then rebuild:

```bash
cd docs/figma
python3 tools/build.py
```

| File | What it controls |
| --- | --- |
| `tools/design_lib.py` | Palette, icons, mascot, sidebar/topbar/nav, charts, buttons, badges |
| `tools/screens_child.py` | 4 child screens |
| `tools/screens_parent.py` | 4 parent screens |
| `tools/screens_robot.py` | 3 robot-console screens |
| `tools/screens_doctor.py` | 4 doctor screens |
| `tools/screens_admin.py` | 4 admin/research screens |
| `tools/screens_system.py` | Design-system board |
| `tools/screens.py` | Role order, page names, folder names |
| `tools/plugin_template.js` | Figma plugin runtime |

The build regenerates the SVGs, `spec.json`, `plugin/code.js`, `preview.html`,
`DESIGN.md` and the zip, then validates every SVG. Re-import the plugin
(`Plugins → Development → SPARK UI/UX Builder`) to pick up changes in Figma.

---

## Design rules baked into the screens

Keep these when you edit — they come from the backend permissions:

- **Parent scoping** — a parent only sees children linked to their own account.
- **Doctor scoping** — a doctor only sees assigned children. Reports are
  educational insights, never a clinical diagnosis (the disclaimer is on the
  report page for a reason).
- **Researcher privacy** — anonymised aggregates only; cohorts with fewer than
  10 participants are suppressed.
- **Child safety** — the child app never exposes robot control, and the
  operator console always keeps an emergency stop visible.
- **Arabic / RTL** — Arabic is a first-class language. Duplicate a frame, flip
  it horizontally, and keep numbers LTR.
- **States** — empty, loading, error, offline and permission-denied screens are
  still to be drawn; list them before development starts.

Full inventory, colours and type scale: [`DESIGN.md`](DESIGN.md).

---

## Quick checklist

- [ ] New Figma file created
- [ ] `plugin/manifest.json` imported and plugin run
- [ ] 6 pages and 20 frames present
- [ ] Nunito installed (optional, for the intended headings)
- [ ] File renamed, e.g. **SPARK UI/UX Kit v1**
- [ ] Share → *Anyone with the link can view* (or invite the team)
- [ ] Real illustrations dropped in from `docs/design/assets/`

---

## بالعربي — خطوات سريعة

1. افتح Figma واعمل **ملف جديد**.
2. من القائمة: **Plugins → Development → Import plugin from manifest…**
3. اختَر الملف `docs/figma/plugin/manifest.json`.
4. شغّل الإضافة: **Plugins → Development → SPARK UI/UX Builder**.
5. ستنشئ الإضافة **6 صفحات و20 شاشة** قابلة للتعديل بالكامل:
   `00 · Design system`، `01 · Child app`، `02 · Parent app`،
   `03 · Robot control`، `04 · Doctor`، `05 · Admin & research`.
6. للتعديل: اضغط مرتين على أي نص لتغييره، واسحب أي إطار أو زر لتغيير مكانه.
   كل الطبقات مسمّاة (Header، Hero card، Bottom navigation…) داخل كل شاشة.
7. لو الإضافة لا تعمل: افتح مجلد الدور مثل `screens/01-child/` واسحب ملفات
   الـ SVG إلى صفحة الدور في Figma.
8. للمعاينة بدون Figma: افتح `preview.html` في المتصفح.
9. بعد أي تعديل في ملفات `tools/` شغّل:
   `cd docs/figma && python3 tools/build.py` ثم أعد تشغيل الإضافة.
