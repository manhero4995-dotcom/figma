"""Admin / researcher workspace screens (desktop 1440x1024)."""

from __future__ import annotations

from design_lib import *  # noqa: F401,F403

NAV = [("home", "Overview"), ("users", "Users"), ("user", "Children"),
       ("monitor", "Devices"), ("flask", "Research"), ("shield", "Audit")]


def chrome(active, breadcrumb):
    e = sidebar("PLATFORM", NAV, active, accent=TEAL, bg="#080833",
                dark=True, soft="#122A4A", group="Sidebar",
                user_name="Admin", user_initials="AR", user_label="Platform")
    e += topbar(breadcrumb, accent=TEAL, initials="AR", group="Top bar",
                search_hint="Search users, reports…")
    return e


def overview():
    e = chrome("Overview", "Admin / Overview")
    e += G("Page header",
           T("Title", 288, 96, 600, "System overview", 28, 800, INK),
           T("Sub", 288, 136, 640, "Live platform health, usage and role activity.", 12, 400, MUTED))
    e += G("Health pill",
           R("Pill", 1128, 100, 272, 36, GREEN_SOFT, 18),
           C("Dot", 1146, 118, 4, GREEN),
           T("Text", 1158, 108, 230, "All systems operational", 10, 700, GREEN))

    stats = [("Active users", "1,248", "+6.2% this month", "users", TEAL, TEAL_SOFT),
             ("Children", "412", "+18 this month", "user", INDIGO_2, "#E8EDFF"),
             ("Robots online", "18 / 24", "6 offline", "robot", CYAN, "#E4FAFE"),
             ("Sessions today", "96", "+14 vs yesterday", "play", PURPLE, PURPLE_SOFT)]
    for i, (label, value, delta, ic, accent, soft) in enumerate(stats):
        e += stat_card(288 + i * 280, 172, 260, 118, label, value, delta, ic,
                       accent, soft, group=f"Stat {i + 1}")

    # Usage chart
    e += G("Usage chart",
           R("Card", 288, 314, 760, 330, WHITE, 18, LINE),
           T("Title", 308, 332, 400, "Sessions & assessments", 14, 800, INK),
           T("Sub", 308, 352, 400, "Daily activity over the last 14 days", 9, 400, MUTED))
    e += G("Usage chart",
           R("Tab active", 900, 330, 54, 28, "#F1F4F9", 8),
           T("Week", 900, 338, 54, "Week", 8.5, 700, INK, "center"),
           T("Month", 962, 338, 54, "Month", 8.5, 500, MUTED, "center"),
           C("Legend sessions", 308, 380, 4, TEAL),
           T("Legend sessions label", 318, 374, 90, "Sessions", 8.5, 500, MUTED),
           C("Legend assessments", 398, 380, 4, INDIGO_2),
           T("Legend assessments label", 408, 374, 110, "Assessments", 8.5, 500, MUTED))
    e += line_chart(320, 402, 690, 196, [42, 55, 48, 62, 58, 70, 66, 78, 74, 86, 82, 92, 88, 96],
                    TEAL, fill_color=TEAL, labels=["1", "3", "5", "7", "9", "11", "13"],
                    group="Usage chart")
    e += line_chart(320, 402, 690, 196, [18, 24, 20, 28, 26, 32, 30, 36, 34, 40, 38, 44, 42, 48],
                    INDIGO_2, grid_color="#F2F4F8", dots=False, group="Usage chart")

    # Donut
    e += G("Roles donut",
           R("Card", 1068, 314, 332, 330, WHITE, 18, LINE),
           T("Title", 1088, 332, 260, "Users by role", 14, 800, INK),
           T("Sub", 1088, 352, 260, "1,248 active accounts", 9, 400, MUTED))
    e += donut(1178, 470, 62, 20, [(46, TEAL), (38, INDIGO_2), (10, CYAN), (6, PURPLE)],
               center_bg=WHITE, group="Roles donut")
    e += G("Roles donut",
           T("Total", 1128, 454, 100, "1,248", 18, 800, INK, "center"),
           T("Label", 1128, 480, 100, "accounts", 8, 500, MUTED, "center"))
    legend = [("Parent", "46%", TEAL), ("Child", "38%", INDIGO_2),
              ("Doctor", "10%", CYAN), ("Researcher", "6%", PURPLE)]
    for i, (label, pct, color) in enumerate(legend):
        y = 426 + i * 34
        e += G("Roles donut",
               C("Dot", 1256, y + 5, 4, color),
               T("Label", 1268, y, 90, label, 9, 500, MUTED),
               T("Value", 1340, y, 42, pct, 9, 700, INK, "right"))

    # Activity table
    e += G("Activity table",
           R("Card", 288, 664, 760, 300, WHITE, 18, LINE),
           T("Title", 308, 682, 400, "Recent admin activity", 14, 800, INK),
           T("View", 988, 684, 40, "View", 9, 700, BLUE, "right"),
           R("Header row", 308, 712, 720, 30, "#F6F8FC", 8))
    for label, x, w in [("Actor", 324, 150), ("Action", 480, 220), ("Target", 720, 180), ("Time", 918, 90)]:
        e += G("Activity table", T("Header", x, 720, w, label, 9, 700, MUTED))
    activity = [("Dr. Hana", "Approved report", "Salma Ahmed", "2 min ago", GREEN),
                ("Admin", "Invited user", "yara@clinic.org", "18 min ago", TEAL),
                ("System", "Robot went offline", "R-07 · Lab 2", "32 min ago", AMBER),
                ("Admin", "Changed role", "Omar · Parent", "1 h ago", TEAL),
                ("Dr. Hana", "Exported CSV", "Cohort · Age 6–9", "2 h ago", TEAL)]
    for i, (actor, action, target, time, color) in enumerate(activity):
        y = 752 + i * 42
        e += G("Activity table",
               C("Dot", 324, y + 6, 4, color),
               T("Actor", 338, y, 130, actor, 9, 600, INK),
               T("Action", 480, y, 220, action, 9, 500, MUTED),
               T("Target", 720, y, 180, target, 9, 500, MUTED),
               T("Time", 918, y, 90, time, 8.5, 400, MUTED, "right"))
        if i < 4:
            e += G("Activity table", R("Row line", 308, y + 28, 720, 1, LINE))

    # Alerts
    e += G("Alerts",
           R("Card", 1068, 664, 332, 300, WHITE, 18, LINE),
           T("Title", 1088, 682, 240, "System alerts", 14, 800, INK),
           *badge(1320, 678, "3", RED, RED_SOFT, w=32, group="Alerts"))
    alerts = [("Robot R-07 offline", "Lab 2 · 12 min", RED, RED_SOFT),
              ("2 failed admin logins", "Security · 40 min", AMBER, AMBER_SOFT),
              ("Storage at 68%", "Reports · 1 h", BLUE, SKY_SOFT)]
    for i, (title, meta, fg, bg) in enumerate(alerts):
        y = 718 + i * 58
        e += G("Alerts",
               C("Icon tile", 1104, y + 16, 14, bg),
               C("Dot", 1104, y + 16, 4, fg),
               T("Title", 1128, y + 6, 210, title, 9.5, 700, INK),
               T("Meta", 1128, y + 24, 210, meta, 8.5, 400, MUTED))
    e += button(1088, 896, 292, 34, "Open alert center", "#F6F8FC", INK, 9,
                LINE, size=9, group="Alerts")
    return screen("admin", "01-overview", "Admin overview",
                  "Platform health, usage, role mix and recent admin activity.",
                  1440, 1024, ADMIN_BG, e)


def users():
    e = chrome("Users", "Admin / Users & roles")
    e += G("Page header",
           T("Title", 288, 96, 500, "Users & roles", 26, 800, INK),
           T("Sub", 288, 136, 700, "Invite people, assign roles and control access.", 11.5, 400, MUTED))
    e += button(1252, 96, 128, 40, "Invite user", TEAL, WHITE, 10, size=10)

    e += G("Toolbar",
           R("Search field", 288, 148, 320, 34, WHITE, 17, LINE),
           *icon("search", 302, 157, 16, MUTED_2),
           T("Placeholder", 326, 158, 260, "Search name, email or ID…", 9, 400, MUTED_2))
    for i, (label, w, active) in enumerate([("All roles", 70, True), ("Active", 58, False),
                                            ("Pending", 64, False), ("Suspended", 76, False)]):
        x = 624 + i * 82
        e += G("Toolbar",
               R("Chip", x, 148, w, 34, TEAL if active else WHITE, 17, None if active else LINE),
               T("Label", x, 157, w, label, 9, 700 if active else 500,
                 WHITE if active else MUTED, "center"))
    e += button(1212, 148, 168, 34, "Export CSV", WHITE, INK, 17, LINE,
                icon_name="download", size=9)

    e += G("Users table",
           R("Card", 288, 200, 1112, 620, WHITE, 18, LINE),
           R("Header row", 308, 220, 1072, 36, "#F6F8FC", 8))
    for label, x, w in [("User", 324, 280), ("Role", 620, 110), ("Linked child", 750, 150),
                         ("Status", 920, 90), ("Last active", 1020, 120), ("Actions", 1170, 60)]:
        e += G("Users table", T("Header", x, 232, w, label, 9.5, 700, MUTED))

    rows = [("Salma Ahmed", "salma@spark.app", "Child", ORANGE, CREAM_SOFT, "Omar Hassan", "Active", GREEN, GREEN_SOFT, "2 min ago"),
            ("Omar Hassan", "omar@example.com", "Parent", MAROON, MAROON_SOFT, "Salma Ahmed", "Active", GREEN, GREEN_SOFT, "18 min ago"),
            ("Dr. Hana Saleh", "hana@clinic.org", "Doctor", BLUE, SKY_SOFT, "24 children", "Active", GREEN, GREEN_SOFT, "1 h ago"),
            ("Yara Samir", "yara@clinic.org", "Doctor", BLUE, SKY_SOFT, "—", "Pending", AMBER, AMBER_SOFT, "Invited"),
            ("Admin", "admin@spark.app", "Admin", TEAL, TEAL_SOFT, "Platform", "Active", GREEN, GREEN_SOFT, "5 min ago"),
            ("Rami Adel", "rami@uni.edu", "Researcher", INDIGO_2, "#E8EDFF", "Aggregate", "Active", GREEN, GREEN_SOFT, "Yesterday"),
            ("Nour Hassan", "nour@example.com", "Parent", MAROON, MAROON_SOFT, "Lina Youssef", "Suspended", RED, RED_SOFT, "3 days ago"),
            ("Adam Nabil", "adam@spark.app", "Child", ORANGE, CREAM_SOFT, "Nour Hassan", "Active", GREEN, GREEN_SOFT, "Today")]
    for i, (name, email, role, rfg, rbg, linked, status, sfg, sbg, last) in enumerate(rows):
        y = 270 + i * 64
        e += G("Users table",
               C("Avatar", 334, y + 20, 16, rbg),
               T("Initial", 326, y + 13, 16, name[0], 8, 800, rfg, "center"),
               T("Name", 362, y + 8, 190, name, 10.5, 700, INK),
               T("Email", 362, y + 26, 220, email, 8.5, 400, MUTED),
               *badge(620, y + 10, role, rfg, rbg, w=74, group="Users table"),
               T("Linked", 750, y + 15, 150, linked, 9, 500, MUTED),
               *badge(920, y + 10, status, sfg, sbg, w=82, group="Users table"),
               T("Last", 1020, y + 15, 120, last, 8.5, 400, MUTED),
               *icon("chevron-right", 1200, y + 16, 14, MUTED_2))
        if i < 7:
            e += G("Users table", R("Row line", 308, y + 52, 1072, 1, LINE))
    e += G("Users table",
           T("Pagination", 324, 786, 300, "Showing 1–8 of 1,248 users", 9, 500, MUTED),
           T("Prev", 1060, 786, 50, "‹ Prev", 9, 500, MUTED, "right"),
           T("Next", 1170, 786, 90, "Next ›", 9, 700, TEAL, "right"))

    e += G("Role note",
           *icon("shield", 288, 848, 16, TEAL),
           T("Text", 312, 848, 820,
             "Role scopes access: parents see linked children only; doctors see assigned children; researchers see anonymised aggregates.",
             8.5, 500, MUTED),
           T("Audit link", 1150, 848, 250, "View audit log →", 8.5, 700, TEAL, "right"))
    return screen("admin", "02-users", "Users & roles",
                  "User directory, role badges, account status and scoping note.",
                  1440, 1024, ADMIN_BG, e)


def research():
    e = chrome("Research", "Research / Analytics")
    e += G("Page header",
           T("Title", 288, 96, 500, "Research analytics", 26, 800, INK),
           T("Sub", 288, 136, 760,
             "Anonymised, aggregate learning data. No direct identifiers are shown.", 11.5, 400, MUTED),
           *badge(1000, 98, "Anonymised aggregates", TEAL, TEAL_SOFT, w=170, group="Page header"))
    e += G("Cohort selector",
           R("Field", 1000, 138, 200, 36, WHITE, 10, LINE),
           T("Cohort", 1014, 148, 170, "All children · 412", 9, 600, INK),
           *icon("chevron-down", 1176, 149, 14, MUTED))
    e += button(1212, 138, 168, 36, "Export CSV", WHITE, INK, 10, LINE,
                icon_name="download", size=9)

    stats = [("Participants", "412", "All cohorts", "users", INDIGO_2, "#E8EDFF"),
             ("Assessments", "1,840", "Completed", "book", TEAL, TEAL_SOFT),
             ("Average IQ", "104", "SD 12.4", "chart", BLUE, SKY_SOFT),
             ("Completion", "87%", "+4% vs last term", "check", GREEN, GREEN_SOFT)]
    for i, (label, value, sub, ic, accent, soft) in enumerate(stats):
        x = 288 + i * 280
        e += G(f"KPI {i + 1}",
               R("Card", x, 188, 260, 96, WHITE, 16, LINE),
               T("Label", x + 18, 202, 190, label, 9.5, 500, MUTED),
               T("Value", x + 18, 220, 190, value, 24, 800, INK),
               T("Sub", x + 18, 258, 190, sub, 8.5, 500, accent),
               C("Icon tile", x + 228, 206, 14, soft),
               *icon(ic, x + 221, 199, 14, accent))

    # Distribution
    e += G("Distribution",
           R("Card", 288, 304, 760, 330, WHITE, 18, LINE),
           T("Title", 308, 322, 400, "Score distribution", 14, 800, INK),
           T("Sub", 308, 342, 400, "SPARK IQ · 1,840 assessments", 9, 400, MUTED))
    dist = [8, 22, 48, 86, 120, 96, 54, 24, 10]
    e += bar_chart(336, 388, 660, 170, dist, BLUE,
                   labels=["60", "70", "80", "90", "100", "110", "120", "130", "140"],
                   maxv=130, group="Distribution")
    mean_x = 336 + (104 - 60) / (140 - 60) * 660
    e += G("Distribution",
           R("Mean line", mean_x, 388, 1, 170, ORANGE, 0, opacity=.8),
           T("Mean label", mean_x - 40, 368, 80, "mean 104", 8.5, 700, ORANGE, "center"),
           C("Mean dot", mean_x, 388, 3, ORANGE))

    # Age comparison
    e += G("Age comparison",
           R("Card", 1068, 304, 332, 330, WHITE, 18, LINE),
           T("Title", 1088, 322, 260, "Age group comparison", 14, 800, INK),
           T("Sub", 1088, 342, 260, "Average score by band", 9, 400, MUTED),
           C("Legend one", 1088, 370, 4, INDIGO_2),
           T("Legend one label", 1098, 364, 70, "Average", 8, 500, MUTED),
           C("Legend two", 1176, 370, 4, CYAN),
           T("Legend two label", 1186, 364, 80, "Completion", 8, 500, MUTED))
    groups = [("6–7", 92, 78), ("8–9", 104, 88), ("10–11", 112, 96)]
    for i, (label, avg, comp) in enumerate(groups):
        gx = 1104 + i * 86
        e += G("Age comparison",
               R("Avg bar", gx, 560 - avg, 24, avg, INDIGO_2, 4),
               R("Comp bar", gx + 30, 560 - comp, 24, comp, CYAN, 4),
               T("Label", gx - 4, 572, 64, label, 8.5, 600, MUTED, "center"),
               T("Avg value", gx - 6, 560 - avg - 14, 36, str(avg), 7.5, 700, INDIGO_2, "center"))
    e += G("Age comparison", R("Baseline", 1088, 560, 292, 1, LINE))

    # Filters
    e += G("Cohort filters",
           R("Card", 288, 654, 300, 310, WHITE, 18, LINE),
           T("Title", 308, 672, 240, "Cohort filters", 13, 800, INK),
           T("Hint", 308, 692, 240, "Applies to all charts", 8.5, 400, MUTED))
    filters = [("Age group", ["6–7", "8–9", "10–11"]), ("Gender", ["All", "Girls", "Boys"]),
               ("Period", ["This term", "Last term"])]
    y = 716
    for label, options in filters:
        e += G("Cohort filters", T("Label", 308, y, 200, label, 8.5, 700, MUTED, ls=.8))
        for j, opt in enumerate(options):
            x = 308 + j * 88
            active = j == 0
            e += G("Cohort filters",
                   R("Chip", x, y + 18, 80, 26, TEAL if active else "#F6F8FC", 13,
                     None if active else LINE),
                   T("Chip label", x, y + 25, 80, opt, 8, 700 if active else 500,
                     WHITE if active else MUTED, "center"))
        y += 66
    e += button(308, 900, 260, 36, "Apply filters", TEAL, WHITE, 10, size=9.5,
                group="Cohort filters")

    # Cohort table
    e += G("Cohort table",
           R("Card", 608, 654, 792, 310, WHITE, 18, LINE),
           T("Title", 628, 672, 300, "Cohort summary", 13, 800, INK),
           T("View", 1330, 674, 50, "View all", 8.5, 700, BLUE, "right"),
           R("Header row", 628, 700, 752, 30, "#F6F8FC", 8))
    for label, x, w in [("Age band", 644, 160), ("n", 820, 60), ("Avg score", 900, 100),
                         ("Completion", 1030, 110), ("Trend", 1180, 90)]:
        e += G("Cohort table", T("Header", x, 708, w, label, 8.5, 700, MUTED))
    cohorts = [("6–7", "148", "92", "78%", "+6%"), ("8–9", "164", "104", "88%", "+4%"),
               ("10–11", "100", "112", "91%", "+3%")]
    for i, (band, n, avg, comp, trend) in enumerate(cohorts):
        y = 744 + i * 48
        e += G("Cohort table",
               T("Band", 644, y, 120, band, 9, 600, INK),
               T("N", 820, y, 60, n, 9, 500, MUTED),
               T("Avg", 900, y, 100, avg, 10, 800, INK),
               T("Comp", 1030, y, 110, comp, 9, 600, TEAL),
               T("Trend", 1180, y, 90, trend, 9, 700, GREEN),
               R("Row line", 628, y + 30, 752, 1, LINE) if i < 2 else [])
    e += G("Cohort table",
           T("Note", 628, 908, 752,
             "Aggregates with n < 10 are suppressed to protect privacy.", 8, 400, MUTED))
    return screen("admin", "03-research", "Research analytics",
                  "KPIs, score distribution, age cohorts and aggregate privacy.",
                  1440, 1024, ADMIN_BG, e)


def audit():
    e = chrome("Audit", "Admin / Audit & exports")
    e += G("Page header",
           T("Title", 288, 96, 500, "Audit & exports", 26, 800, INK),
           T("Sub", 288, 136, 700, "Every admin action is recorded. Exports are tracked too.", 11.5, 400, MUTED))
    e += button(1212, 96, 168, 40, "Export audit log", WHITE, INK, 10, LINE,
                icon_name="download", size=9)

    chips = [("All events", 288, 88, True), ("Auth", 386, 54, False),
             ("Data", 450, 54, False), ("Exports", 514, 64, False)]
    for label, x, w, active in chips:
        e += G("Filters",
               R("Chip", x, 154, w, 32, INDIGO if active else WHITE, 16, None if active else LINE),
               T("Label", x, 162, w, label, 9, 700 if active else 500,
                 WHITE if active else MUTED, "center"))
    e += G("Search",
           R("Field", 880, 154, 320, 32, WHITE, 16, LINE),
           *icon("search", 894, 162, 16, MUTED_2),
           T("Placeholder", 918, 163, 260, "Search actor, action or IP…", 9, 400, MUTED_2))
    e += button(1212, 154, 168, 32, "Last 30 days", WHITE, INK, 16, LINE,
                icon_name="calendar", size=9)

    e += G("Audit table",
           R("Card", 288, 204, 720, 620, WHITE, 18, LINE),
           R("Header row", 308, 224, 680, 34, "#F6F8FC", 8))
    for label, x, w in [("Time", 324, 80), ("Actor", 410, 110), ("Action", 530, 170),
                         ("Entity", 710, 140), ("IP", 850, 70), ("Result", 930, 60)]:
        e += G("Audit table", T("Header", x, 234, w, label, 9, 700, MUTED))
    events = [("11:12", "Dr. Hana", "report.approve", "Report · Salma", "10.0.0.24", "OK", GREEN),
              ("11:04", "Admin", "user.role.update", "User · Omar", "10.0.0.8", "OK", GREEN),
              ("10:58", "Admin", "export.csv", "Cohort · 412 rows", "10.0.0.8", "OK", GREEN),
              ("10:41", "System", "robot.offline", "Device · R-07", "—", "WARN", AMBER),
              ("10:22", "Unknown", "auth.login", "admin@spark.app", "82.14.3.9", "FAIL", RED),
              ("09:58", "Dr. Hana", "report.edit", "Report · Omar", "10.0.0.24", "OK", GREEN),
              ("09:30", "Admin", "user.invite", "yara@clinic.org", "10.0.0.8", "OK", GREEN),
              ("09:02", "Rami", "research.export", "Aggregate · Age 6–9", "10.0.0.51", "OK", GREEN)]
    for i, (time, actor, action, entity, ip, result, color) in enumerate(events):
        y = 270 + i * 56
        e += G("Audit table",
               T("Time", 324, y + 10, 80, time, 8.5, 500, MUTED),
               T("Actor", 410, y + 10, 110, actor, 9, 600, INK),
               T("Action", 530, y + 10, 170, action, 8.5, 500, INK_SOFT),
               T("Entity", 710, y + 10, 140, entity, 8.5, 500, MUTED),
               T("IP", 850, y + 10, 70, ip, 8.5, 500, MUTED),
               *badge(930, y + 2, result, color, GREEN_SOFT if color == GREEN else (RED_SOFT if color == RED else AMBER_SOFT), w=46, group="Audit table"))
        if i < 7:
            e += G("Audit table", R("Row line", 308, y + 42, 680, 1, LINE))
    e += G("Audit table",
           T("Footer", 324, 786, 400, "Immutable log · retained for 90 days", 8, 400, MUTED),
           T("Next", 900, 786, 80, "Next page ›", 8.5, 700, INDIGO_2, "right"))

    # Export center
    e += G("Export center",
           R("Card", 1028, 204, 372, 300, WHITE, 18, LINE),
           T("Title", 1048, 222, 300, "Export center", 14, 800, INK),
           T("Sub", 1048, 242, 300, "Generated files appear here", 9, 400, MUTED))
    exports = [("Participants CSV", "412 rows · anonymised", "ready", TEAL),
               ("Assessment results", "1,840 rows · CSV", "ready", TEAL),
               ("Audit log", "Last 30 days · CSV", "queued", AMBER)]
    for i, (name, meta, state, color) in enumerate(exports):
        y = 270 + i * 62
        e += G("Export center",
               C("Icon tile", 1068, y + 12, 12, TEAL_SOFT if color == TEAL else AMBER_SOFT),
               *icon("download", 1062, y + 5, 12, color),
               T("Name", 1090, y + 2, 200, name, 9.5, 700, INK),
               T("Meta", 1090, y + 20, 200, meta, 8.5, 400, MUTED),
               T("State", 1348, y + 10, 36, state, 7.5, 700, color, "right"))
    e += button(1048, 456, 332, 32, "Request new export", INDIGO, WHITE, 9, size=9,
                group="Export center")

    # Retention
    e += G("Retention",
           R("Card", 1028, 524, 372, 300, WHITE, 18, LINE),
           T("Title", 1048, 542, 300, "Data retention", 14, 800, INK),
           T("Sub", 1048, 562, 300, "Applied automatically", 9, 400, MUTED))
    retention = [("Audit logs", "90 days"), ("Reports", "24 months"),
                 ("Raw events", "30 days"), ("Anonymised data", "Indefinite")]
    for i, (label, value) in enumerate(retention):
        y = 592 + i * 38
        e += G("Retention",
               T("Label", 1048, y, 180, label, 9, 500, MUTED),
               T("Value", 1250, y, 130, value, 9, 600, INK, "right"),
               R("Row line", 1048, y + 26, 332, 1, LINE))
    e += G("Retention",
           T("Anonymise exports", 1048, 754, 200, "Anonymise exports", 9, 600, INK),
           R("Track", 1322, 752, 36, 20, TEAL, 10),
           C("Knob", 1348, 762, 7, WHITE),
           T("Note", 1048, 788, 290, "Direct identifiers are removed before download.", 7.8, 400, MUTED))

    e += G("Privacy note",
           *icon("lock", 288, 852, 16, INDIGO_2),
           T("Text", 312, 852, 900,
             "Exports are logged with actor, timestamp and row count. Only admins can download audit data.",
             8.5, 500, MUTED))
    return screen("admin", "04-audit", "Audit & exports",
                  "Immutable audit table, export queue and retention policy.",
                  1440, 1024, ADMIN_BG, e)


SCREENS = [overview(), users(), research(), audit()]
