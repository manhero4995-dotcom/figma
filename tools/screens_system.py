"""Shared design-system board."""

from __future__ import annotations

from design_lib import *  # noqa: F401,F403


def design_system():
    e = []
    e += G("Title",
           T("Title", 56, 48, 900, "SPARK UI/UX", 36, 900, INK),
           T("Sub", 56, 98, 900, "Design system, role accents and shared components for the child, parent, robot, doctor and admin products.",
             12, 400, MUTED),
           *badge(1250, 56, "v1 · Nov 2026", BLUE, SKY_SOFT, w=134, group="Title"))

    # Brand colours
    e.append(T("Section", 56, 138, 500, "Brand colours", 15, 800, INK))
    brand = [("Maroon", MAROON, "#54040F", WHITE), ("Cream", CREAM, "#FFDB99", INK),
             ("Orange", ORANGE, "#FF8310", WHITE), ("Blue", BLUE, "#286CB5", WHITE),
             ("Sky", SKY, "#D8E9FC", INK), ("Teal", TEAL, "#2DC197", WHITE)]
    for i, (name, color, hexv, fg) in enumerate(brand):
        x = 56 + i * 216
        e += G(f"Brand {name}",
               R("Swatch", x, 166, 200, 96, color, 14),
               T("Name", x + 14, 180, 170, name, 11, 700, fg),
               T("Hex", x + 14, 226, 170, hexv, 9, 500, fg, opacity=.85),
               T("Caption", x, 270, 200, "Brand / " + name, 8.5, 500, MUTED))

    # Role accents
    e.append(T("Section", 56, 312, 500, "Role accents", 15, 800, INK))
    roles = [("Child", ORANGE, WHITE), ("Parent", MAROON, WHITE),
             ("Robot control", CYAN, DARK), ("Doctor", BLUE, WHITE),
             ("Admin / Research", TEAL, DARK)]
    for i, (name, color, fg) in enumerate(roles):
        x = 56 + i * 270
        e += G(f"Role {name}",
               R("Swatch", x, 340, 246, 86, color, 14),
               T("Name", x + 14, 354, 210, name, 12, 800, fg),
               T("Hex", x + 14, 382, 210, color.upper(), 9, 500, fg, opacity=.85))

    # Neutrals
    e.append(T("Section", 56, 456, 500, "Neutrals & surfaces", 15, 800, INK))
    neutrals = [("Ink", INK), ("Ink soft", INK_SOFT), ("Muted", MUTED),
                ("Line", LINE), ("Surface", "#F6F8FC"), ("White", WHITE)]
    for i, (name, color) in enumerate(neutrals):
        x = 56 + i * 216
        e += G(f"Neutral {name}",
               R("Swatch", x, 484, 200, 56, color, 10, LINE),
               T("Name", x, 548, 200, name, 8.5, 500, MUTED))

    # Typography
    e.append(T("Section", 56, 596, 500, "Typography", 15, 800, INK))
    e.append(T("Note", 56, 620, 500, "Nunito for headings · Inter for body", 9, 400, MUTED))
    type_rows = [("Display / 40", 40, 900, "Big adventures", 652),
                 ("Heading / 28", 28, 800, "Good morning, Dr. Hana", 706),
                 ("Section / 20", 20, 800, "Today's plan", 749),
                 ("Body / 14", 14, 400, "Stay close to your child's learning journey.", 786),
                 ("Caption / 12", 12, 400, "Last updated 12 Nov 2026 · 10:24", 814),
                 ("Eyebrow / 10", 10, 700, "PARENT SPACE", 840)]
    for label, size, weight, sample, y in type_rows:
        e += G(f"Type {label}",
               T("Label", 56, y + 4, 160, label, 8.5, 700, MUTED, ls=.6),
               T("Sample", 240, y, 760, sample, size, weight, INK, ls=1.4 if size == 10 else None))

    # Components
    e.append(T("Section", 56, 892, 500, "Components", 15, 800, INK))
    e += button(56, 922, 150, 44, "Primary", ORANGE, WHITE, 12, size=11)
    e += button(220, 922, 150, 44, "Secondary", WHITE, INK, 12, LINE, size=11)
    e += button(384, 922, 150, 44, "Danger", RED, WHITE, 12, size=11)
    e += button(548, 922, 150, 44, "Disabled", "#EDF0F5", MUTED_2, 12, size=11)

    e += G("Input sample",
           T("Label", 740, 906, 200, "Label", 8.5, 700, MUTED),
           R("Field", 740, 922, 300, 44, WHITE, 10, LINE),
           T("Placeholder", 756, 936, 260, "Enter a value…", 10, 400, MUTED_2))

    e += G("Badge samples",
           T("Label", 740, 986, 200, "Badges", 8.5, 700, MUTED))
    for i, (label, fg, bg) in enumerate([("Active", GREEN, GREEN_SOFT), ("Draft", AMBER, AMBER_SOFT),
                                          ("Shared", TEAL, TEAL_SOFT), ("Review", RED, RED_SOFT)]):
        e += badge(740 + i * 78, 1002, label, fg, bg, w=70)

    e += G("Card sample",
           R("Card", 1080, 906, 304, 130, WHITE, 16, LINE),
           T("Label", 1098, 922, 200, "Assigned children", 9, 500, MUTED),
           T("Value", 1098, 940, 200, "24", 28, 800, INK),
           C("Icon tile", 1340, 924, 14, SKY_SOFT),
           *icon("users", 1333, 917, 14, BLUE),
           T("Delta", 1098, 994, 140, "+3 this week", 8.5, 700, GREEN))

    e += G("Nav sample",
           R("Nav item", 56, 1002, 220, 44, SKY_SOFT, 12),
           R("Accent", 56, 1014, 3, 20, BLUE, 1.5),
           *icon("home", 74, 1012, 20, BLUE),
           T("Label", 106, 1010, 150, "Overview", 11, 700, INK))
    e += G("Toggle sample",
           T("Label", 300, 1006, 200, "Obstacle stop", 9, 600, INK),
           R("Track", 300, 1028, 40, 22, TEAL, 11),
           C("Knob", 328, 1039, 8, WHITE))
    e += G("Progress sample",
           T("Label", 56, 1074, 200, "Progress", 8.5, 700, MUTED),
           R("Track", 56, 1092, 240, 8, LINE, 4),
           R("Fill", 56, 1092, 168, 8, ORANGE, 4))

    e += G("Footer",
           R("Line", 56, 1148, 1328, 1, LINE),
           T("Text", 56, 1162, 800, "Use these tokens in Figma styles; every screen frame is named and fully editable.",
             9, 500, MUTED),
           T("Link", 1150, 1162, 234, "figma.com · spark-desktop", 9, 700, BLUE, "right"))
    return screen("system", "00-design-system", "Design system",
                  "Brand colours, role accents, typography and shared components.",
                  1440, 1240, "#F7F8FC", e)


SCREENS = [design_system()]
