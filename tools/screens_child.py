"""Child app screens (mobile 390x844)."""

from __future__ import annotations

from design_lib import *  # noqa: F401,F403


def home():
    e = []
    e += status_bar()
    e += G("Child header",
           C("Logo circle", 44, 76, 20, ORANGE),
           *icon("bolt", 34, 66, 20, WHITE),
           T("Brand", 72, 64, 100, "SPARK", 18, 900, INK),
           C("Bell button", 350, 76, 20, WHITE),
           *icon("bell", 340, 66, 20, INK))
    e.append(T("Greeting", 20, 112, 350, "Hi, Salma!", 24, 900, INK))
    e.append(T("Greeting sub", 20, 146, 350, "Ready for today's adventure?", 12.5, 500, MUTED))

    e += G("Hero card",
           R("Card", 20, 180, 350, 188, ORANGE, 24),
           C("Glow one", 336, 212, 46, "#FFA64D"),
           C("Glow two", 306, 344, 70, "#FF9A3D", opacity=.55),
           R("Speech bubble", 36, 198, 196, 58, WHITE, 14),
           T("Speech line one", 50, 208, 170, "Ready for a new mission?", 12, 800, INK),
           T("Speech line two", 50, 228, 170, "Earn 3 stars today.", 10.5, 500, MUTED),
           T("Mission title", 36, 270, 220, "Pattern Hunt", 22, 900, WHITE),
           T("Mission sub", 36, 300, 210, "Find the missing shape", 11.5, 600, "#FFF4E6"))
    e += mascot(252, 214, 96, WHITE, group="Hero card")
    e += button(36, 322, 134, 36, "Start mission", WHITE, ORANGE, 18, size=11.5,
                group="Hero card")

    e += section_title(20, 392, "Today's plan", action="3 activities", w=350,
                       group="Today plan")
    plans = [
        ("bolt", CREAM_SOFT, ORANGE, "IQ Adventure", "10 min · +2 stars", "badge", "+2"),
        ("gamepad", SKY_SOFT, BLUE, "Memory Match", "5 min · +2 stars", "chevron", None),
        ("book", "#F3F4F6", MUTED, "Story & Chat", "Unlocks at 4:00 PM", "lock", None),
    ]
    for i, (ic, soft, accent, title, meta, right, val) in enumerate(plans):
        y = 420 + i * 72
        g = f"Plan card {i + 1}"
        block = [R("Card", 20, y, 350, 62, WHITE, 16, LINE),
                 C("Icon tile", 54, y + 31, 18, soft),
                 *icon(ic, 44, y + 21, 20, accent),
                 T("Title", 84, y + 11, 190, title, 13.5, 700, INK),
                 T("Meta", 84, y + 32, 190, meta, 10.5, 500, MUTED)]
        if right == "badge":
            block += badge(296, y + 19, val, ORANGE, CREAM_SOFT, group=g)
        elif right == "chevron":
            block += icon("chevron-right", 338, y + 22, 16, MUTED_2, group=g)
        else:
            block += icon("lock", 332, y + 21, 18, MUTED_2, group=g)
        e += G(g, *block)

    e += section_title(20, 650, "This week", action="8 stars", w=350,
                       group="Week strip")
    e += G("Week strip",
           R("Card", 20, 674, 350, 82, WHITE, 18, LINE),
           T("Star count", 296, 650, 74, "8 stars", 10.5, 700, ORANGE, "right"))
    days = ["Mo", "Tu", "We", "Th", "Fr"]
    for i, day in enumerate(days):
        cx = 50 + i * 70
        done = i < 3
        current = i == 3
        fill = ORANGE if done else (WHITE if current else "#F3F4F6")
        e += G("Week strip",
               C("Day circle", cx, 700, 15, fill, ORANGE if current else None, 1.6),
               *icon("check", cx - 7, 693, 14, WHITE) if done else [],
               T("Day label", cx - 20, 724, 40, day, 10, 700 if done or current else 500,
                 INK if done or current else MUTED, "center"))
    e += bottom_nav("Home")
    return screen("child", "01-home", "Home", "Today's mission, plan and weekly streak.",
                  390, 844, CREAM_BG, e)


def iq_question():
    e = []
    e += status_bar()
    e += G("Quiz header",
           C("Back button", 42, 76, 20, WHITE, LINE, 1),
           *icon("chevron-left", 33, 67, 18, INK),
           T("Title", 72, 66, 200, "IQ Adventure", 16, 800, INK),
           R("Timer pill", 296, 56, 74, 40, WHITE, 20, LINE),
           *icon("clock", 306, 66, 18, ORANGE),
           T("Timer", 328, 66, 40, "00:42", 11, 700, INK))
    e.append(T("Progress label", 20, 112, 250, "Question 3 of 8", 11, 600, MUTED))
    e.append(T("Progress value", 290, 112, 80, "38%", 11, 700, ORANGE, "right"))
    e.append(R("Progress track", 20, 132, 350, 8, "#FFE3BC", 4))
    e.append(R("Progress fill", 20, 132, 133, 8, ORANGE, 4))

    e += G("Question card",
           R("Card", 20, 160, 350, 260, WHITE, 24, LINE),
           T("Eyebrow", 40, 182, 200, "PATTERN", 10, 800, ORANGE, ls=1.4),
           T("Question", 40, 206, 300, "Which shape comes next?", 20, 800, INK))
    # sequence
    e += G("Sequence",
           C("Circle", 85, 300, 25, SKY),
           R("Square", 140, 275, 50, 50, CREAM, 10),
           POLY("Triangle", [(225, 273), (251, 323), (199, 323)], TEAL_SOFT),
           C("Unknown", 325, 300, 25, "#F3F4F6"),
           T("Question mark", 305, 292, 40, "?", 20, 800, MUTED_2, "center"))
    e.append(T("Answers label", 20, 438, 350, "Choose one answer", 11, 600, MUTED))

    answers = [
        ("A", "circle", SKY, "Circle"),
        ("B", "square", CREAM, "Square"),
        ("C", "triangle", TEAL_SOFT, "Triangle"),
        ("D", "diamond", PURPLE_SOFT, "Diamond"),
    ]
    for i, (letter, shape, soft, label) in enumerate(answers):
        x = 20 + (i % 2) * 185
        y = 462 + (i // 2) * 74
        g = f"Answer {letter}"
        selected = letter == "B"
        block = [R("Card", x, y, 165, 64, "#FFF8EE" if selected else WHITE, 16,
                   ORANGE if selected else LINE, 2 if selected else 1),
                 C("Letter circle", x + 24, y + 32, 14, CREAM_SOFT if selected else "#F3F4F6"),
                 T("Letter", x + 10, y + 25, 28, letter, 11, 800,
                   ORANGE if selected else MUTED, "center"),
                 T("Shape label", x + 48, y + 24, 80, label, 12, 700, INK)]
        if shape == "circle":
            block.append(C("Shape", x + 140, y + 32, 13, BLUE))
        elif shape == "square":
            block.append(R("Shape", x + 127, y + 19, 26, 26, ORANGE, 4))
        elif shape == "triangle":
            block.append(POLY("Shape", [(x + 140, y + 18), (x + 154, y + 46), (x + 126, y + 46)], TEAL))
        else:
            block.append(POLY("Shape", [(x + 140, y + 18), (x + 154, y + 32), (x + 140, y + 46), (x + 126, y + 32)], PURPLE))
        if selected:
            block.append(C("Check", x + 146, y + 12, 8, ORANGE))
            block += icon("check", x + 142, y + 8, 8, WHITE)
        e += G(g, *block)

    e += G("Hint card",
           R("Card", 20, 620, 350, 70, CREAM_SOFT, 18),
           *mascot(32, 630, 48, ORANGE, "Hint card"),
           T("Hint title", 92, 632, 260, "Look for the repeating pattern.", 12, 700, INK),
           T("Hint text", 92, 654, 260, "Circle → square → triangle → ?", 10.5, 500, MUTED))
    e += button(20, 706, 350, 52, "Next question", ORANGE, WHITE, 18, size=14)
    e.append(T("Hint", 20, 770, 350, "No timer pressure — take your time.", 10, 500, MUTED, "center"))
    return screen("child", "02-iq-question", "IQ question",
                  "Focused assessment question with progress and answer states.",
                  390, 844, CREAM_BG, e)


def result():
    e = []
    e += status_bar()
    confetti = [(48, 70, ORANGE), (96, 52, TEAL), (150, 66, SKY), (230, 48, PURPLE),
                (300, 62, ORANGE), (344, 92, AMBER), (70, 110, PURPLE), (330, 130, TEAL)]
    for i, (x, y, color) in enumerate(confetti):
        e += G("Confetti", C(f"Confetti {i}", x, y, 3.5, color, opacity=.8))
    e.append(T("Title", 20, 52, 350, "Amazing work, Salma!", 24, 900, INK, "center"))
    e.append(T("Subtitle", 20, 88, 350, "You finished Pattern Hunt.", 12, 500, MUTED, "center"))

    e += G("Score card",
           R("Card", 20, 120, 350, 236, WHITE, 24, LINE),
           C("Ring track", 195, 214, 64, "none", LINE, 12),
           P("Ring progress", 0, 0, arc_path(195, 214, 64, -90, 180), stroke=ORANGE, sw=12),
           T("Score", 145, 188, 100, "850", 34, 900, INK, "center"),
           T("Points", 145, 230, 100, "points", 11, 500, MUTED, "center"),
           *icon("star", 157, 258, 20, AMBER),
           *icon("star", 185, 254, 24, AMBER),
           *icon("star", 217, 258, 20, AMBER),
           *badge(150, 292, "Personal best", GREEN, GREEN_SOFT, group="Score card"))

    stats = [("80%", "Accuracy"), ("2:10", "Time"), ("4", "Day streak")]
    for i, (val, label) in enumerate(stats):
        x = 20 + i * 122
        e += G(f"Stat {i + 1}",
               R("Card", x, 376, 106, 80, WHITE, 16, LINE),
               T("Value", x, 392, 106, val, 18, 800, INK, "center"),
               T("Label", x, 420, 106, label, 10, 500, MUTED, "center"))

    e += G("Badge card",
           R("Card", 20, 476, 350, 94, CREAM_SOFT, 18),
           C("Badge circle", 52, 523, 26, AMBER),
           *icon("star", 40, 511, 24, WHITE),
           T("Badge title", 90, 492, 240, "Pattern Master", 15, 800, INK),
           T("Badge sub", 90, 514, 240, "2 more sessions to unlock", 10.5, 500, MUTED),
           R("Badge track", 90, 540, 190, 6, WHITE, 3),
           R("Badge fill", 90, 540, 114, 6, ORANGE, 3),
           T("Badge value", 288, 533, 44, "60%", 10, 700, ORANGE, "right"))

    e += button(20, 590, 350, 52, "Play again", ORANGE, WHITE, 18, size=14)
    e += button(20, 654, 350, 48, "Back home", WHITE, INK, 18, LINE, size=13)
    e += mascot(286, 718, 76, ORANGE, "Result mascot")
    e += G("Praise bubble",
           R("Bubble", 20, 730, 240, 58, WHITE, 16, LINE),
           T("Praise", 36, 742, 210, "You're on fire! Keep going.", 11.5, 700, INK))
    return screen("child", "03-result", "Game result",
                  "Celebration, score ring, rewards and next actions.",
                  390, 844, CREAM_BG, e)


def progress():
    e = []
    e += status_bar()
    e.append(T("Title", 20, 56, 260, "My progress", 24, 900, INK))
    e += G("Period switch",
           R("Track", 20, 100, 350, 42, WHITE, 21, LINE),
           R("Active", 24, 104, 170, 34, ORANGE, 17),
           T("This week", 24, 112, 170, "This week", 11, 700, WHITE, "center"),
           T("This month", 194, 112, 172, "This month", 11, 600, MUTED, "center"))

    e += G("Summary card",
           R("Card", 20, 158, 350, 112, WHITE, 20, LINE),
           T("Label", 40, 176, 200, "This week", 11, 600, MUTED),
           T("Value", 40, 194, 250, "8 of 10 stars", 22, 800, INK),
           *icon("star", 312, 178, 22, AMBER),
           R("Track", 40, 232, 250, 8, LINE, 4),
           R("Fill", 40, 232, 200, 8, ORANGE, 4),
           T("Percent", 300, 226, 50, "80%", 11, 700, ORANGE, "right"))

    e += section_title(20, 294, "Skills", action="This week", w=350, group="Skills")
    e += G("Skills",
           R("Card", 20, 320, 350, 196, WHITE, 20, LINE))
    skills = [("Logic", 78, ORANGE), ("Memory", 64, BLUE),
              ("Focus", 82, TEAL), ("Creativity", 70, PURPLE)]
    for i, (label, value, color) in enumerate(skills):
        y = 340 + i * 42
        e += G("Skills",
               T("Name", 40, y, 120, label, 12, 700, INK),
               T("Value", 290, y, 60, f"{value}%", 11, 700, color, "right"),
               R("Track", 40, y + 20, 310, 8, LINE, 4),
               R("Fill", 40, y + 20, 310 * value / 100, 8, color, 4))

    e += section_title(20, 540, "Achievements", action="See all", w=350,
                       group="Achievements")
    badges = [("First quiz", "2 Nov", CREAM_SOFT, ORANGE),
              ("3-day streak", "8 Nov", TEAL_SOFT, TEAL),
              ("Top 10", "10 Nov", PURPLE_SOFT, PURPLE)]
    for i, (name, date, soft, color) in enumerate(badges):
        x = 20 + i * 122
        e += G(f"Achievement {i + 1}",
               R("Card", x, 564, 106, 92, WHITE, 16, LINE),
               C("Icon circle", x + 53, 590, 22, soft),
               *icon("star", x + 43, 580, 20, color),
               T("Name", x + 6, 618, 94, name, 10.5, 700, INK, "center"),
               T("Date", x + 6, 636, 94, date, 9, 500, MUTED, "center"))

    e += G("Next step",
           R("Card", 20, 676, 350, 80, CREAM_SOFT, 18),
           T("Eyebrow", 38, 690, 200, "NEXT STEP", 9, 800, ORANGE, ls=1.2),
           T("Text", 38, 708, 260, "Try Memory Match to boost focus", 13, 800, INK),
           T("Sub", 38, 730, 260, "5 minutes · +2 stars", 10, 500, MUTED),
           C("Arrow circle", 336, 716, 18, ORANGE),
           *icon("arrow-right", 327, 707, 18, WHITE))
    e += bottom_nav("Report")
    return screen("child", "04-progress", "My progress",
                  "Skill bars, weekly streak and achievements.",
                  390, 844, CREAM_BG, e)


SCREENS = [home(), iq_question(), result(), progress()]
