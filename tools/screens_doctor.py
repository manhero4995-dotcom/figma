"""Doctor workspace screens (desktop 1440x1024)."""

from __future__ import annotations

from design_lib import *  # noqa: F401,F403

NAV = [("home", "Overview"), ("users", "Children"), ("book", "Assessments"),
       ("chart", "Reports"), ("mail", "Messages")]


def chrome(active, breadcrumb):
    e = sidebar("CLINIC", NAV, active, accent=BLUE, group="Sidebar")
    e += topbar(breadcrumb, accent=BLUE, initials="DH", group="Top bar")
    return e


def overview():
    e = chrome("Overview", "Workspace / Overview")
    e += G("Page header",
           T("Title", 288, 96, 760, "Good morning, Dr. Hana", 28, 800, INK),
           T("Sub", 288, 136, 700, "Five children are waiting for a review today.", 13, 400, MUTED))
    e += G("Date pill",
           R("Pill", 1180, 104, 220, 40, WHITE, 20, LINE),
           *icon("calendar", 1196, 114, 18, BLUE),
           T("Date", 1222, 114, 166, "12 – 18 November", 11, 600, INK))

    stats = [("Assigned children", "24", "+3 this week", "users", BLUE, SKY_SOFT),
             ("Assessments", "18", "+12% vs last week", "book", TEAL, TEAL_SOFT),
             ("Reports pending", "5", "Due today", "chart", ORANGE, CREAM_SOFT),
             ("Avg improvement", "+12%", "vs last month", "trend", GREEN, GREEN_SOFT)]
    for i, (label, value, delta, ic, accent, soft) in enumerate(stats):
        e += stat_card(288 + i * 280, 176, 260, 120, label, value, delta, ic,
                       accent, soft, group=f"Stat {i + 1}")

    # Review table
    e += G("Review table",
           R("Card", 288, 320, 800, 420, WHITE, 18, LINE),
           T("Title", 308, 338, 400, "Children needing review", 15, 800, INK),
           T("Sub", 308, 360, 300, "Flagged in the last 7 days", 10, 400, MUTED),
           T("View all", 1000, 340, 70, "View all", 10, 700, BLUE, "right"),
           R("Header row", 308, 384, 760, 34, "#F6F8FC", 8))
    cols = [("Child", 324, 190), ("Last assessment", 534, 140), ("Score", 690, 60),
            ("Trend", 770, 70), ("Status", 866, 100)]
    for label, x, w in cols:
        e += G("Review table", T("Header", x, 393, w, label, 9.5, 700, MUTED))

    rows = [("Salma Ahmed", "Age 7", "IQ · 12 Nov", "112", "+8", "Review", AMBER, AMBER_SOFT, CREAM),
            ("Omar Khaled", "Age 8", "IQ · 11 Nov", "98", "-3", "Review", AMBER, AMBER_SOFT, SKY),
            ("Lina Youssef", "Age 6", "Game · 10 Nov", "105", "+5", "On track", GREEN, GREEN_SOFT, TEAL_SOFT),
            ("Adam Nabil", "Age 9", "IQ · 9 Nov", "87", "+2", "Review", AMBER, AMBER_SOFT, PURPLE_SOFT),
            ("Nour Hassan", "Age 7", "IQ · 8 Nov", "119", "+11", "On track", GREEN, GREEN_SOFT, CREAM_SOFT)]
    for i, (name, age, last, score, trend, status, fg, bg, soft) in enumerate(rows):
        y = 430 + i * 60
        e += G("Review table",
               C("Avatar", 330, y + 20, 15, soft),
               T("Initial", 322, y + 13, 16, name[0], 8, 800, INK, "center"),
               T("Name", 354, y + 10, 170, name, 11, 700, INK),
               T("Age", 354, y + 28, 170, age, 9, 400, MUTED),
               T("Last", 534, y + 17, 140, last, 9.5, 500, MUTED),
               T("Score", 690, y + 14, 60, score, 13, 800, INK),
               T("Trend", 770, y + 15, 70, trend, 10, 700, GREEN if trend.startswith("+") else RED),
               *badge(866, y + 10, status, fg, bg, w=80, group="Review table"),
               *icon("chevron-right", 1050, y + 16, 14, MUTED_2))
        if i < 4:
            e += G("Review table", R("Row line", 308, y + 50, 760, 1, LINE))

    # Schedule
    e += G("Schedule",
           R("Card", 1108, 320, 292, 220, WHITE, 18, LINE),
           T("Title", 1128, 338, 200, "Today", 14, 800, INK),
           T("Count", 1330, 340, 50, "3 items", 9, 600, MUTED, "right"))
    schedule = [("09:30", "Salma Ahmed", "IQ review"), ("11:00", "Omar Khaled", "Feedback call"),
                ("14:30", "Lina Youssef", "Plan next steps")]
    for i, (time, name, kind) in enumerate(schedule):
        y = 372 + i * 52
        e += G("Schedule",
               R("Time chip", 1128, y, 48, 36, SKY_SOFT, 8),
               T("Time", 1128, y + 9, 48, time, 8.5, 700, BLUE, "center"),
               T("Name", 1188, y + 2, 190, name, 10.5, 700, INK),
               T("Kind", 1188, y + 20, 190, kind, 9, 400, MUTED))

    e += G("Recent reports",
           R("Card", 1108, 556, 292, 184, WHITE, 18, LINE),
           T("Title", 1128, 574, 220, "Recent reports", 14, 800, INK),
           T("View", 1330, 576, 50, "View", 9, 700, BLUE, "right"))
    reports = [("Salma Ahmed", "Shared · 12 Nov", TEAL, TEAL_SOFT),
               ("Adam Nabil", "Draft · 11 Nov", AMBER, AMBER_SOFT)]
    for i, (name, meta, fg, bg) in enumerate(reports):
        y = 608 + i * 58
        e += G("Recent reports",
               C("Avatar", 1142, y + 16, 14, bg),
               T("Initial", 1135, y + 10, 14, name[0], 7.5, 800, fg, "center"),
               T("Name", 1166, y + 6, 160, name, 10, 700, INK),
               T("Meta", 1166, y + 24, 160, meta, 8.5, 400, MUTED))

    # Chart
    e += G("Volume chart",
           R("Card", 288, 756, 800, 220, WHITE, 18, LINE),
           T("Title", 308, 774, 300, "Assessment volume", 14, 800, INK),
           T("Sub", 308, 794, 300, "Last 6 weeks · all assessments", 9, 400, MUTED),
           C("Legend dot", 900, 782, 4, BLUE),
           T("Legend", 910, 776, 80, "Assessments", 8.5, 500, MUTED))
    e += line_chart(320, 822, 730, 110, [12, 18, 15, 22, 19, 26], BLUE,
                    fill_color=BLUE, labels=["W1", "W2", "W3", "W4", "W5", "W6"],
                    group="Volume chart")

    # Quick actions
    e += G("Quick actions",
           R("Card", 1108, 756, 292, 220, WHITE, 18, LINE),
           T("Title", 1128, 774, 220, "Quick actions", 14, 800, INK))
    actions = [("plus", "New assessment"), ("edit", "Add note"),
               ("download", "Export report"), ("mail", "Message parent")]
    for i, (ic, label) in enumerate(actions):
        x = 1124 + (i % 2) * 136
        y = 804 + (i // 2) * 52
        e += button(x, y, 124, 42, label, "#F6F8FC", INK, 10, LINE,
                    icon_name=ic, size=8.2, group="Quick actions")
    e.append(T("Footer", 1128, 916, 252,
               "Templates keep reports consistent.", 8.5, 400, MUTED))
    return screen("doctor", "01-overview", "Doctor overview",
                  "Assignments, review queue, schedule and recent reports.",
                  1440, 1024, DOCTOR_BG, e)


def child_detail():
    e = chrome("Children", "Children / Salma Ahmed / Assessment")
    e += G("Child header",
           C("Avatar", 320, 132, 32, CREAM),
           T("Initial", 300, 116, 40, "S", 20, 800, MAROON, "center"),
           T("Name", 368, 100, 500, "Salma Ahmed", 26, 800, INK),
           T("Meta", 368, 140, 500, "Age 7 · Grade 2 · Parent: Omar Hassan", 11, 400, MUTED),
           *badge(368, 164, "Age 7", BLUE, SKY_SOFT, w=56, group="Child header"),
           *badge(432, 164, "Grade 2", TEAL, TEAL_SOFT, w=64, group="Child header"),
           *badge(504, 164, "ID #C-1042", MUTED, "#F3F4F6", w=88, group="Child header"))
    e += button(1150, 108, 100, 40, "Add note", WHITE, INK, 10, LINE, size=10)
    e += button(1262, 108, 110, 40, "Export", BLUE, WHITE, 10, size=10)

    stats = [("IQ score", "112", "Above average", BLUE, SKY_SOFT),
             ("Percentile", "78th", "vs same age", TEAL, TEAL_SOFT),
             ("Completion", "100%", "24 of 24 items", GREEN, GREEN_SOFT),
             ("Last session", "12 Nov", "20 minutes", ORANGE, CREAM_SOFT)]
    for i, (label, value, sub, accent, soft) in enumerate(stats):
        x = 288 + i * 280
        e += G(f"Summary {i + 1}",
               R("Card", x, 200, 260, 100, WHITE, 16, LINE),
               T("Label", x + 18, 214, 200, label, 10, 500, MUTED),
               T("Value", x + 18, 234, 200, value, 24, 800, INK),
               T("Sub", x + 18, 270, 200, sub, 9, 500, accent))

    e += G("Tabs",
           T("Overview", 288, 324, 90, "Overview", 11, 700, BLUE),
           R("Active line", 288, 348, 64, 2, BLUE),
           T("Responses", 390, 324, 90, "Responses", 11, 500, MUTED),
           T("History", 500, 324, 80, "History", 11, 500, MUTED))

    e += G("Domain scores",
           R("Card", 288, 364, 720, 420, WHITE, 18, LINE),
           T("Title", 308, 382, 400, "Domain scores", 14, 800, INK),
           T("Sub", 308, 402, 400, "Percentile rank by cognitive domain", 9, 400, MUTED))
    e += radar(470, 576, 118, ["Logic", "Memory", "Focus", "Language", "Creative"],
               [78, 64, 82, 70, 74], BLUE, group="Domain scores")
    domains = [("Logic", "78", BLUE), ("Memory", "64", TEAL),
               ("Focus", "82", ORANGE), ("Language", "70", PURPLE), ("Creativity", "74", GREEN)]
    for i, (label, value, color) in enumerate(domains):
        y = 470 + i * 38
        e += G("Domain scores",
               C("Dot", 668, y + 7, 4, color),
               T("Label", 682, y, 120, label, 10, 600, INK),
               T("Value", 820, y, 40, value, 10, 800, color, "right"),
               R("Track", 870, y + 6, 100, 5, LINE, 2.5),
               R("Fill", 870, y + 6, int(value) if False else 100 * int(value) / 100, 5, color, 2.5))
    e += G("Domain scores",
           R("Interpretation", 660, 664, 320, 92, SKY_SOFT, 12),
           T("Eyebrow", 676, 678, 200, "INTERPRETATION", 8, 800, BLUE, ls=1),
           T("Text", 676, 694, 288, "Strong logic and focus. Memory is the main area to\nsupport with short, repeated practice.", 9.5, 500, INK_SOFT, lh=14))

    e += G("Recommendations",
           R("Card", 1028, 364, 372, 260, WHITE, 18, LINE),
           T("Title", 1048, 382, 300, "Recommendations", 14, 800, INK),
           T("Sub", 1048, 402, 300, "Share with the parent after review", 9, 400, MUTED))
    recs = [("Memory Match", "10 min · 3× per week", TEAL, TEAL_SOFT),
            ("Pattern Hunt", "5 min · before reading", ORANGE, CREAM_SOFT),
            ("Short focus breaks", "After 12 minutes", BLUE, SKY_SOFT)]
    for i, (title, meta, accent, soft) in enumerate(recs):
        y = 428 + i * 58
        e += G("Recommendations",
               C("Icon tile", 1062, y + 12, 12, soft),
               C("Dot", 1062, y + 12, 4, accent),
               T("Title", 1086, y + 4, 280, title, 10.5, 700, INK),
               T("Meta", 1086, y + 22, 280, meta, 9, 400, MUTED))

    e += G("Assessment details",
           R("Card", 1028, 644, 372, 200, WHITE, 18, LINE),
           T("Title", 1048, 662, 300, "Assessment details", 14, 800, INK))
    details = [("Assessment", "SPARK IQ · Form A"), ("Completed", "12 Nov 2026 · 10:24"),
               ("Reviewer", "Dr. Hana Saleh"), ("Visibility", "Parent · shared")]
    for i, (label, value) in enumerate(details):
        y = 692 + i * 34
        e += G("Assessment details",
               T("Label", 1048, y, 100, label, 9, 500, MUTED),
               T("Value", 1150, y, 230, value, 9.5, 600, INK, "right"))

    e += G("Recent sessions",
           R("Card", 288, 800, 720, 160, WHITE, 18, LINE),
           T("Title", 308, 818, 300, "Recent sessions", 13, 800, INK),
           T("View all", 928, 820, 60, "View all", 9, 700, BLUE, "right"))
    sessions = [("12 Nov", "IQ Assessment", "24 items", "112", TEAL, TEAL_SOFT),
                ("10 Nov", "Memory Match", "8 pairs", "90%", BLUE, SKY_SOFT),
                ("8 Nov", "Pattern Hunt", "6 rounds", "85%", ORANGE, CREAM_SOFT)]
    for i, (date, name, meta, score, fg, bg) in enumerate(sessions):
        y = 846 + i * 36
        e += G("Recent sessions",
               T("Date", 308, y, 60, date, 9, 500, MUTED),
               T("Name", 378, y, 200, name, 10, 700, INK),
               T("Meta", 600, y, 120, meta, 9, 400, MUTED),
               *badge(870, y - 6, score, fg, bg, w=54, group="Recent sessions"),
               *icon("chevron-right", 968, y - 2, 12, MUTED_2))
    return screen("doctor", "02-child-assessment", "Child assessment",
                  "IQ summary, domain radar, recommendations and session history.",
                  1440, 1024, DOCTOR_BG, e)


def report_review():
    e = chrome("Reports", "Reports / IQ Assessment / Salma Ahmed")
    e += G("Page header",
           T("Title", 288, 96, 420, "Report review", 26, 800, INK),
           *badge(470, 102, "Draft", AMBER, AMBER_SOFT, w=58, group="Page header"),
           T("Sub", 288, 134, 700, "Check the wording, then share with the parent.", 11.5, 400, MUTED))
    e += button(1130, 104, 100, 40, "Preview", WHITE, INK, 10, LINE, size=10)
    e += button(1242, 104, 140, 40, "Approve & send", BLUE, WHITE, 10, size=10)

    e += G("Report page",
           R("Card", 288, 160, 760, 760, WHITE, 12, LINE),
           T("Brand", 320, 184, 220, "SPARK", 12, 900, BLUE, ls=1.4),
           T("Doc title", 320, 204, 500, "Assessment report", 20, 800, INK),
           T("Disclaimer", 320, 232, 500, "Educational insights, not a clinical diagnosis.", 9, 400, MUTED),
           R("Divider", 320, 256, 696, 1, LINE),
           T("Meta child", 320, 270, 180, "Child: Salma Ahmed", 9, 500, MUTED),
           T("Meta date", 500, 270, 180, "Date: 12 Nov 2026", 9, 500, MUTED),
           T("Meta reviewer", 680, 270, 200, "Reviewer: Dr. Hana Saleh", 9, 500, MUTED))

    sections = [
        (306, "Summary", ["Salma completed the SPARK IQ assessment with a score of 112,",
                          "placing her above the expected range for her age."]),
        (386, "Strengths", ["• Strong pattern recognition and logical reasoning.",
                            "• Sustained focus across the first 18 items.",
                            "• Confident approach to unfamiliar shapes."]),
        (486, "Areas to support", ["• Working memory when two rules are combined.",
                                   "• Re-checking answers before submitting."]),
        (586, "Recommendations", ["• 10 minutes of Memory Match, three times a week.",
                                  "• Short focus breaks after 12 minutes of work."]),
        (686, "Next review", ["Review progress in four weeks and compare with the",
                              "next form of the assessment."]),
    ]
    for y, title, lines in sections:
        e += G("Report page", T("Section title", 320, y, 300, title, 13, 800, INK))
        for j, line in enumerate(lines):
            e += G("Report page", T("Body", 320, y + 24 + j * 18, 670, line, 10, 400, INK_SOFT))
    e += G("Report page",
           R("Sign line", 320, 852, 240, 1, LINE),
           T("Sign", 320, 860, 240, "Dr. Hana Saleh · Educational specialist", 8.5, 500, MUTED),
           T("Page", 960, 860, 56, "Page 1 / 2", 8.5, 500, MUTED, "right"))

    e += G("Report details",
           R("Card", 1068, 160, 332, 240, WHITE, 16, LINE),
           T("Title", 1088, 178, 260, "Report details", 13, 800, INK))
    details = [("Template", "IQ Assessment v2"), ("Language", "English / Arabic"),
               ("Created", "12 Nov · 10:30"), ("Last edit", "12 Nov · 11:12")]
    for i, (label, value) in enumerate(details):
        y = 212 + i * 40
        e += G("Report details",
               T("Label", 1088, y, 100, label, 9, 500, MUTED),
               T("Value", 1190, y, 190, value, 9, 600, INK, "right"))

    e += G("Sharing",
           R("Card", 1068, 420, 332, 200, WHITE, 16, LINE),
           T("Title", 1088, 438, 260, "Sharing", 13, 800, INK))
    toggles = [("Share with parent", True), ("Anonymise for research", False)]
    for i, (label, on) in enumerate(toggles):
        y = 472 + i * 44
        e += G("Sharing",
               T("Label", 1088, y + 2, 200, label, 9.5, 600, INK),
               R("Track", 1322, y, 36, 20, TEAL if on else "#E5E9F0", 10),
               C("Knob", 1348 if on else 1332, y + 10, 7, WHITE))
    e.append(T("Sharing note", 1088, 566, 292,
               "The parent receives a read-only copy. Research data uses aggregates only.",
               8.2, 400, MUTED, lh=12, group="Sharing"))

    e += G("Versions",
           R("Card", 1068, 640, 332, 160, WHITE, 16, LINE),
           T("Title", 1088, 658, 260, "Version history", 13, 800, INK))
    versions = [("v3", "Draft · 11:12", "Dr. Hana"), ("v2", "Edit · 10:58", "Dr. Hana"),
                ("v1", "Created · 10:30", "System")]
    for i, (ver, meta, who) in enumerate(versions):
        y = 690 + i * 32
        e += G("Versions",
               *badge(1088, y - 2, ver, BLUE, SKY_SOFT, w=34, group="Versions"),
               T("Meta", 1132, y, 160, meta, 9, 500, INK),
               T("Who", 1290, y, 90, who, 8.5, 400, MUTED, "right"))

    e += G("Comment",
           R("Card", 1068, 820, 332, 100, WHITE, 16, LINE),
           T("Title", 1088, 836, 260, "Reviewer note", 11, 700, INK),
           R("Input", 1088, 858, 292, 44, "#F6F8FC", 8),
           T("Placeholder", 1098, 870, 260, "Add a note for the team…", 8.5, 400, MUTED))
    return screen("doctor", "03-report-review", "Report review",
                  "Draft report, sharing controls, version history and approval.",
                  1440, 1024, DOCTOR_BG, e)


def export_center():
    e = chrome("Reports", "Reports / Export center")
    e += G("Page header",
           T("Title", 288, 96, 500, "Reports & exports", 26, 800, INK),
           T("Sub", 288, 136, 700, "Review status, share reports and export anonymised data.", 11.5, 400, MUTED))
    chips = [("All", 288, 50, True), ("Draft", 348, 60, False),
             ("Shared", 418, 70, False), ("Reviewed", 498, 78, False)]
    for label, x, w, active in chips:
        e += G("Filters",
               R("Chip", x, 158, w, 32, BLUE if active else WHITE, 16, None if active else LINE),
               T("Label", x, 166, w, label, 9.5, 700 if active else 500,
                 WHITE if active else MUTED, "center"))
    e += G("Search",
           R("Field", 900, 158, 300, 32, WHITE, 16, LINE),
           *icon("search", 914, 166, 16, MUTED_2),
           T("Placeholder", 938, 167, 240, "Search child or report…", 9, 400, MUTED_2))
    e += button(1212, 158, 170, 32, "New report", BLUE, WHITE, 16, size=9.5)

    e += G("Reports table",
           R("Card", 288, 208, 1112, 480, WHITE, 18, LINE),
           R("Header row", 308, 228, 1072, 36, "#F6F8FC", 8))
    cols = [("Child", 324, 220), ("Type", 560, 150), ("Date", 720, 110),
            ("Reviewer", 850, 150), ("Status", 1030, 100), ("Actions", 1180, 60)]
    for label, x, w in cols:
        e += G("Reports table", T("Header", x, 240, w, label, 9.5, 700, MUTED))

    rows = [("Salma Ahmed", "IQ Assessment", "12 Nov 2026", "Dr. Hana", "Draft", AMBER, AMBER_SOFT),
            ("Omar Khaled", "IQ Assessment", "11 Nov 2026", "Dr. Hana", "Shared", TEAL, TEAL_SOFT),
            ("Lina Youssef", "Game report", "10 Nov 2026", "Dr. Hana", "Reviewed", GREEN, GREEN_SOFT),
            ("Adam Nabil", "IQ Assessment", "9 Nov 2026", "Dr. Hana", "Shared", TEAL, TEAL_SOFT),
            ("Nour Hassan", "Weekly summary", "8 Nov 2026", "System", "Reviewed", GREEN, GREEN_SOFT),
            ("Yara Samir", "IQ Assessment", "7 Nov 2026", "Dr. Hana", "Draft", AMBER, AMBER_SOFT)]
    for i, (name, typ, date, reviewer, status, fg, bg) in enumerate(rows):
        y = 278 + i * 58
        e += G("Reports table",
               C("Avatar", 334, y + 18, 14, SKY_SOFT),
               T("Initial", 327, y + 12, 14, name[0], 7.5, 800, BLUE, "center"),
               T("Name", 360, y + 8, 190, name, 10.5, 700, INK),
               T("Type", 560, y + 10, 150, typ, 9.5, 500, MUTED),
               T("Date", 720, y + 10, 110, date, 9, 500, MUTED),
               T("Reviewer", 850, y + 10, 150, reviewer, 9, 500, MUTED),
               *badge(1030, y + 3, status, fg, bg, w=76, group="Reports table"),
               *icon("chevron-right", 1210, y + 10, 14, MUTED_2))
        if i < 5:
            e += G("Reports table", R("Row line", 308, y + 46, 1072, 1, LINE))
    e += G("Reports table",
           T("Pagination", 324, 650, 300, "Showing 1–6 of 24 reports", 9, 500, MUTED),
           T("Prev", 1080, 650, 50, "‹ Prev", 9, 500, MUTED, "right"),
           T("Next", 1180, 650, 80, "Next ›", 9, 700, BLUE, "right"))

    exports = [("book", "PDF report", "A ready-to-share report with scores and recommendations.", BLUE, SKY_SOFT),
               ("download", "CSV data", "One row per participant, anonymised identifiers.", TEAL, TEAL_SOFT),
               ("filter", "Bulk export", "Filter by date, assessment or cohort, then download.", ORANGE, CREAM_SOFT)]
    for i, (ic, title, desc, accent, soft) in enumerate(exports):
        x = 288 + i * 380
        e += G(f"Export {i + 1}",
               R("Card", x, 708, 360, 180, WHITE, 18, LINE),
               C("Icon tile", x + 36, 746, 18, soft),
               *icon(ic, x + 26, 736, 20, accent),
               T("Title", x + 20, 780, 300, title, 13, 800, INK),
               T("Desc", x + 20, 802, 320, desc, 9, 400, MUTED, lh=13))
        e += button(x + 20, 848, 110, 30, "Export", WHITE, accent, 15, accent, size=9,
                    group=f"Export {i + 1}")

    e += G("Privacy note",
           *icon("shield", 288, 910, 16, BLUE),
           T("Text", 312, 910, 980,
             "Exports exclude direct identifiers by default. Research exports are aggregates only and cannot be re-identified.",
             8.5, 500, MUTED))
    return screen("doctor", "04-exports", "Reports & exports",
                  "Report status table, PDF/CSV exports and privacy note.",
                  1440, 1024, DOCTOR_BG, e)


SCREENS = [overview(), child_detail(), report_review(), export_center()]
