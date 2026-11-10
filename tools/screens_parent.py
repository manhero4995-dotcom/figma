"""Parent app screens (mobile 390x844)."""

from __future__ import annotations

from design_lib import *  # noqa: F401,F403


def home():
    e = []
    e += status_bar()
    e += G("Parent header",
           C("Logo circle", 44, 76, 20, MAROON),
           *icon("bolt", 34, 66, 20, WHITE),
           T("Brand", 72, 64, 100, "SPARK", 18, 900, INK),
           C("Bell button", 350, 76, 20, WHITE),
           *icon("bell", 340, 66, 20, INK),
           C("Bell dot", 364, 62, 4, RED))
    e.append(T("Greeting", 20, 108, 350, "Good evening, Omar", 22, 800, INK))
    e.append(T("Greeting sub", 20, 140, 350, "Here's how Salma's week is going.", 12, 500, MUTED))

    e += G("Child switcher",
           R("Card", 20, 170, 350, 74, WHITE, 18, LINE),
           C("Avatar", 54, 207, 22, CREAM),
           T("Initial", 38, 196, 32, "S", 15, 800, MAROON, "center"),
           T("Name", 88, 188, 150, "Salma", 15, 800, INK),
           T("Meta", 88, 210, 170, "Age 7 · Grade 2", 10.5, 500, MUTED),
           *badge(248, 196, "Linked", GREEN, GREEN_SOFT, w=58, group="Child switcher"),
           *icon("chevron-right", 338, 200, 16, MUTED_2))

    e += G("Weekly card",
           R("Card", 20, 262, 350, 146, MAROON, 24),
           T("Eyebrow", 40, 280, 200, "THIS WEEK", 9.5, 700, CREAM, ls=1.4),
           T("Value one", 40, 302, 100, "4", 24, 900, WHITE),
           T("Label one", 40, 336, 100, "Sessions", 9.5, 500, "#F3C9CE"),
           T("Value two", 156, 302, 100, "82%", 24, 900, WHITE),
           T("Label two", 156, 336, 100, "Avg score", 9.5, 500, "#F3C9CE"),
           T("Value three", 272, 302, 80, "12", 24, 900, WHITE),
           T("Label three", 272, 336, 80, "Stars", 9.5, 500, "#F3C9CE"),
           R("Divider one", 142, 300, 1, 54, "#7A2832"),
           R("Divider two", 258, 300, 1, 54, "#7A2832"),
           *badge(40, 362, "+8% vs last week", CREAM, "#6B1520", group="Weekly card"))

    e += section_title(20, 428, "Latest activity", action="See all", w=350,
                       group="Activity")
    rows = [
        ("bolt", CREAM_SOFT, ORANGE, "IQ Assessment", "12 Nov · 20 min", "82%", GREEN, GREEN_SOFT),
        ("gamepad", SKY_SOFT, BLUE, "Memory Match", "10 Nov · 8 min", "90%", BLUE, SKY_SOFT),
        ("book", TEAL_SOFT, TEAL, "Weekly report", "8 Nov · PDF", "New", ORANGE, CREAM_SOFT),
    ]
    for i, (ic, soft, accent, title, meta, val, vfg, vbg) in enumerate(rows):
        y = 452 + i * 70
        g = f"Activity {i + 1}"
        e += G(g,
               R("Card", 20, y, 350, 62, WHITE, 16, LINE),
               C("Icon tile", 54, y + 31, 18, soft),
               *icon(ic, 44, y + 21, 20, accent),
               T("Title", 84, y + 11, 180, title, 13, 700, INK),
               T("Meta", 84, y + 32, 180, meta, 10.5, 500, MUTED),
               *badge(290, y + 20, val, vfg, vbg, w=48, group=g),
               *icon("chevron-right", 340, y + 23, 14, MUTED_2))

    e += G("Nudge card",
           R("Card", 20, 668, 350, 84, CREAM_SOFT, 18, CREAM),
           C("Icon tile", 46, 710, 16, WHITE),
           *icon("alert", 37, 701, 18, ORANGE),
           T("Title", 74, 682, 210, "No practice for 2 days", 13, 800, INK),
           T("Sub", 74, 704, 210, "A gentle nudge can help.", 10.5, 500, MUTED))
    e += button(248, 694, 104, 32, "Send nudge", MAROON, WHITE, 16, size=10,
                group="Nudge card")
    e += bottom_nav("Home", accent=MAROON)
    return screen("parent", "01-home", "Parent dashboard",
                  "Child switcher, weekly summary, activity and practice nudge.",
                  390, 844, PARENT_BG, e)


def child_progress():
    e = []
    e += status_bar()
    e += G("Header",
           C("Back button", 42, 76, 20, WHITE, LINE, 1),
           *icon("chevron-left", 33, 67, 18, INK),
           T("Title", 72, 66, 200, "Salma's progress", 16, 800, INK),
           R("Period pill", 282, 56, 88, 36, WHITE, 18, LINE),
           T("Period", 282, 66, 88, "This month", 10, 600, MUTED, "center"))

    e += G("Score card",
           R("Card", 20, 108, 350, 190, WHITE, 22, LINE),
           T("Label", 40, 126, 200, "Overall score", 11, 600, MUTED),
           T("Value", 40, 144, 100, "82%", 32, 900, INK),
           *badge(128, 158, "+8% this month", GREEN, GREEN_SOFT, group="Score card"))
    e += line_chart(40, 196, 310, 70, [62, 68, 65, 74, 78, 82], MAROON,
                    fill_color="#E8BFC3", labels=["Jun", "Jul", "Aug", "Sep", "Oct", "Nov"],
                    group="Score card")

    e += section_title(20, 316, "Skills", action="This week", w=350, group="Skills")
    skills = [("Logic", 78, MAROON), ("Memory", 64, BLUE), ("Focus", 82, TEAL)]
    for i, (label, value, color) in enumerate(skills):
        x = 20 + i * 122
        e += G(f"Skill {i + 1}",
               R("Card", x, 340, 106, 86, WHITE, 16, LINE),
               T("Label", x + 14, 356, 80, label, 10.5, 600, MUTED),
               T("Value", x + 14, 374, 80, f"{value}%", 20, 800, INK),
               R("Track", x + 14, 406, 78, 6, LINE, 3),
               R("Fill", x + 14, 406, 78 * value / 100, 6, color, 3))

    e += G("Doctor note",
           R("Card", 20, 446, 350, 108, SKY_SOFT, 18),
           C("Avatar", 46, 470, 14, BLUE),
           T("Initials", 38, 463, 16, "DH", 7, 800, WHITE, "center"),
           T("Name", 68, 456, 220, "Dr. Hana · 10 Nov", 10.5, 700, BLUE_DARK),
           T("Note", 40, 484, 310, "Salma shows strong pattern recognition. Keep practising\nmemory games to build focus.", 11.5, 500, INK_SOFT, lh=17))

    e += section_title(20, 574, "Recommended next", w=350, group="Recommendations")
    recs = [("Memory Match", "10 min · Focus", "gamepad", SKY_SOFT, BLUE),
            ("Story: The Lost Star", "5 min · Reading", "book", TEAL_SOFT, TEAL)]
    for i, (title, meta, ic, soft, accent) in enumerate(recs):
        y = 596 + i * 60
        g = f"Recommendation {i + 1}"
        e += G(g,
               R("Card", 20, y, 350, 54, WHITE, 14, LINE),
               C("Icon tile", 46, y + 27, 15, soft),
               *icon(ic, 37, y + 18, 18, accent),
               T("Title", 72, y + 10, 220, title, 12, 700, INK),
               T("Meta", 72, y + 29, 220, meta, 9.5, 500, MUTED),
               *icon("chevron-right", 340, y + 20, 14, MUTED_2))

    e += button(20, 722, 350, 44, "View full report", MAROON, WHITE, 16, size=12)
    e += bottom_nav("Progress", accent=MAROON)
    return screen("parent", "02-child-progress", "Child progress",
                  "Score trend, skills, doctor note and recommendations.",
                  390, 844, PARENT_BG, e)


def reports():
    e = []
    e += status_bar()
    e += G("Header",
           T("Title", 20, 56, 250, "Reports", 24, 900, INK),
           C("Download button", 350, 76, 20, WHITE, LINE, 1),
           *icon("download", 340, 66, 20, MAROON))
    chips = [("All", 20, 56, True), ("Assessments", 84, 106, False),
             ("Games", 198, 74, False), ("Notes", 280, 70, False)]
    for label, x, w, active in chips:
        e += G("Filters",
               R("Chip", x, 104, w, 32, MAROON if active else WHITE, 16,
                 None if active else LINE),
               T("Label", x, 112, w, label, 10, 700 if active else 500,
                 WHITE if active else MUTED, "center"))

    rows = [
        ("bolt", CREAM_SOFT, ORANGE, "IQ Assessment", "12 Nov · Scored 82%", "Assessment", MAROON, MAROON_SOFT),
        ("gamepad", SKY_SOFT, BLUE, "Memory Match", "10 Nov · Scored 90%", "Game", BLUE, SKY_SOFT),
        ("book", TEAL_SOFT, TEAL, "Weekly summary", "8 Nov · PDF · 420 KB", "Report", TEAL, TEAL_SOFT),
        ("user", PURPLE_SOFT, PURPLE, "Doctor note", "5 Nov · Dr. Hana", "Note", PURPLE, PURPLE_SOFT),
    ]
    for i, (ic, soft, accent, title, meta, badge_text, bfg, bbg) in enumerate(rows):
        y = 152 + i * 100
        g = f"Report {i + 1}"
        e += G(g,
               R("Card", 20, y, 350, 88, WHITE, 18, LINE),
               C("Icon tile", 56, y + 44, 22, soft),
               *icon(ic, 44, y + 32, 24, accent),
               T("Title", 92, y + 18, 180, title, 13.5, 700, INK),
               T("Meta", 92, y + 40, 180, meta, 10.5, 500, MUTED),
               *badge(258, y + 18, badge_text, bfg, bbg, group=g),
               *icon("chevron-right", 340, y + 36, 16, MUTED_2))
        if i == 2:
            e += G(g, C("New dot", 350, 368, 4, ORANGE))

    e += G("Saved reports",
           R("Card", 20, 560, 350, 72, WHITE, 16, LINE),
           C("Icon tile", 52, 596, 18, SKY_SOFT),
           *icon("book", 42, 586, 20, BLUE),
           T("Title", 84, 578, 200, "Saved reports", 12.5, 700, INK),
           T("Meta", 84, 598, 200, "2 files · 1.4 MB", 10, 500, MUTED),
           *icon("chevron-right", 340, 588, 16, MUTED_2))

    e += G("Help card",
           R("Card", 20, 648, 350, 80, CREAM_SOFT, 18),
           C("Icon tile", 50, 688, 16, WHITE),
           *icon("shield", 40, 678, 20, ORANGE),
           T("Title", 80, 662, 250, "Reports are saved automatically", 12, 700, INK),
           T("Sub", 80, 682, 250, "Download a PDF any time, even offline.", 10, 500, MUTED))
    e += bottom_nav("Report", accent=MAROON)
    return screen("parent", "03-reports", "Reports & activity",
                  "Filterable report history and saved files.",
                  390, 844, PARENT_BG, e)


def account():
    e = []
    e += status_bar()
    e += G("Header",
           T("Title", 20, 56, 250, "Account", 24, 900, INK),
           C("Settings button", 350, 76, 20, WHITE, LINE, 1),
           *icon("settings", 340, 66, 20, INK))

    e += G("Profile card",
           R("Card", 20, 104, 350, 108, WHITE, 20, LINE),
           C("Avatar", 60, 158, 28, MAROON),
           T("Initial", 40, 144, 40, "O", 18, 800, WHITE, "center"),
           T("Name", 102, 126, 210, "Omar Hassan", 17, 800, INK),
           T("Email", 102, 150, 210, "omar@example.com", 10.5, 500, MUTED),
           *badge(102, 172, "Verified", GREEN, GREEN_SOFT, w=66, group="Profile card"),
           C("Edit button", 336, 136, 14, "#F4F6FA"),
           *icon("edit", 329, 129, 14, MUTED))

    e += section_title(20, 236, "Family", w=350, group="Family")
    e += G("Linked child",
           R("Card", 20, 260, 350, 70, WHITE, 16, LINE),
           C("Avatar", 54, 295, 20, CREAM),
           T("Initial", 39, 285, 30, "S", 13, 800, MAROON, "center"),
           T("Name", 86, 278, 180, "Salma", 12.5, 700, INK),
           T("Meta", 86, 298, 180, "Linked · Full access", 10, 500, MUTED),
           *icon("chevron-right", 340, 287, 16, MUTED_2))

    e += G("Settings list",
           R("Card", 20, 344, 350, 240, WHITE, 18, LINE))
    rows = [("bell", "Notifications", "On", GREEN, False),
            ("book", "Language", "Arabic", MUTED, False),
            ("shield", "Privacy & data", "", MUTED, True),
            ("lock", "Change password", "", MUTED, True)]
    for i, (ic, label, value, vcolor, chevron) in enumerate(rows):
        y = 344 + i * 60
        e += G("Settings list",
               *icon(ic, 40, y + 20, 20, MAROON),
               T("Label", 74, y + 20, 200, label, 12, 600, INK),
               R("Row line", 74, y + 59, 280, 1, LINE) if i < 3 else [])
        if value:
            e += G("Settings list",
                   T("Value", 250, y + 21, 54, value, 10, 700, vcolor, "right"))
        if chevron:
            e += G("Settings list", *icon("chevron-right", 334, y + 20, 14, MUTED_2))

    e += G("Privacy note",
           R("Card", 20, 604, 350, 68, SKY_SOFT, 16),
           *icon("lock", 38, 622, 20, BLUE),
           T("Text", 70, 616, 280, "You only see children linked to your own account.", 10.5, 600, BLUE_DARK, lh=16),
           T("Sub", 70, 642, 280, "Other families stay private.", 9.5, 400, MUTED))

    e += button(20, 690, 350, 44, "Sign out", WHITE, RED, 16, RED, icon_name="logout", size=12)
    e += bottom_nav("Me", accent=MAROON)
    return screen("parent", "04-account", "Account & privacy",
                  "Profile, linked child, settings and parent-only scoping.",
                  390, 844, PARENT_BG, e)


SCREENS = [home(), child_progress(), reports(), account()]
