"""Robot control console screens (tablet 1180x840, dark UI)."""

from __future__ import annotations

from design_lib import *  # noqa: F401,F403


def robot_topbar():
    e = G("Robot top bar",
          R("Bar", 0, 0, 1180, 64, DARK_PANEL),
          R("Line", 0, 63, 1180, 1, DARK_LINE),
          C("Logo", 32, 32, 16, CYAN),
          *icon("bolt", 24, 24, 16, DARK),
          T("Brand", 56, 18, 220, "SPARK CONTROL", 12.5, 800, DARK_TEXT, ls=1.2),
          T("Workspace", 56, 38, 220, "ROBOT OPERATOR", 8, 700, DARK_MUTED, ls=1.4),
          R("Status pill", 380, 18, 112, 28, "#0F2A27", 14),
          C("Status dot", 396, 32, 4, TEAL),
          T("Status text", 408, 24, 78, "Connected", 9.5, 600, TEAL))
    e += G("Robot top bar",
           R("Latency pill", 504, 18, 74, 28, DARK_PANEL_2, 14),
           T("Latency", 504, 24, 74, "24 ms", 9.5, 600, DARK_MUTED, "center"),
           R("Link pill", 590, 18, 66, 28, DARK_PANEL_2, 14),
           T("Link", 590, 24, 66, "UDP", 9.5, 600, DARK_MUTED, "center"))
    e += G("Robot top bar",
           *icon("battery", 830, 22, 20, TEAL),
           T("Battery", 856, 23, 46, "78%", 10, 700, DARK_TEXT),
           *icon("clock", 922, 22, 18, DARK_MUTED),
           T("Time", 944, 23, 50, "14:32", 10, 600, DARK_MUTED))
    e += button(1014, 14, 146, 36, "EMERGENCY STOP", RED, WHITE, 10, size=9.5,
                group="Robot top bar")
    return e


def control_room():
    e = []
    e += robot_topbar()

    # Camera viewport
    e += G("Camera viewport",
           R("Card", 20, 84, 740, 460, "#0D1727", 18, DARK_LINE),
           P("Horizon", 0, 0, "M 20 300 L 760 300", stroke="#1B2A42", sw=1),
           P("Floor left", 0, 0, "M 390 300 L 20 544", stroke="#1B2A42", sw=1),
           P("Floor mid left", 0, 0, "M 390 300 L 180 544", stroke="#1B2A42", sw=1),
           P("Floor center", 0, 0, "M 390 300 L 390 544", stroke="#1B2A42", sw=1),
           P("Floor mid right", 0, 0, "M 390 300 L 600 544", stroke="#1B2A42", sw=1),
           P("Floor right", 0, 0, "M 390 300 L 760 544", stroke="#1B2A42", sw=1),
           P("Ceiling left", 0, 0, "M 390 300 L 120 84", stroke="#16233A", sw=1),
           P("Ceiling right", 0, 0, "M 390 300 L 660 84", stroke="#16233A", sw=1),
           R("Floor band", 20, 430, 740, 114, "#0F1C30", opacity=.55),
           R("Block red", 318, 420, 58, 40, "#C94B3B", 6, opacity=.85),
           R("Block blue", 392, 436, 52, 28, "#3D7DC4", 5, opacity=.85),
           R("Block amber", 286, 442, 30, 20, "#D9A23B", 4, opacity=.85),
           C("Crosshair outer", 390, 314, 22, "none", CYAN, 1.4),
           C("Crosshair dot", 390, 314, 3, CYAN),
           P("Crosshair h", 0, 0, "M 350 314 L 372 314 M 408 314 L 430 314", stroke=CYAN, sw=1.4),
           P("Crosshair v", 0, 0, "M 390 274 L 390 296 M 390 332 L 390 354", stroke=CYAN, sw=1.4),
           R("Live badge", 36, 100, 58, 22, RED, 11),
           C("Live dot", 48, 111, 3, WHITE),
           T("Live text", 56, 105, 32, "LIVE", 8, 800, WHITE, ls=.8),
           T("Camera label", 36, 512, 200, "CAM 01 · FRONT", 9, 700, DARK_MUTED, ls=1.1),
           T("Timestamp", 470, 512, 140, "14:32:08.240", 9, 500, DARK_MUTED, "right"),
           C("Snapshot button", 646, 506, 16, DARK_PANEL_2),
           *icon("camera", 640, 500, 14, DARK_TEXT),
           C("Record button", 682, 506, 16, DARK_PANEL_2),
           *icon("play", 676, 500, 14, RED),
           C("Mic button", 718, 506, 16, DARK_PANEL_2),
           *icon("mic", 712, 500, 14, DARK_TEXT))

    # Manual control
    e += G("Manual control",
           R("Card", 780, 84, 380, 460, DARK_PANEL, 18, DARK_LINE),
           T("Title", 800, 102, 200, "MANUAL CONTROL", 10, 800, CYAN, ls=1.2),
           *badge(1046, 98, "Manual", CYAN, "#0F2A33", group="Manual control"),
           C("Joystick base", 970, 270, 86, "#0D1727", DARK_LINE, 1.5),
           C("Joystick ring", 970, 270, 62, "none", "#1E304A", 1),
           C("Joystick knob", 970, 270, 31, CYAN, "#7FE9F8", 2),
           C("Knob center", 970, 270, 4, DARK),
           *icon("chevron-down", 962, 184, 16, DARK_MUTED),
           *icon("chevron-right", 1074, 262, 16, DARK_MUTED),
           *icon("chevron-left", 850, 262, 16, DARK_MUTED),
           *icon("chevron-down", 962, 346, 16, DARK_MUTED),
           T("Hint", 800, 368, 340, "Drag the stick or use the keyboard.", 9.5, 500, DARK_MUTED),
           T("Speed label", 800, 394, 80, "SPEED", 9, 700, DARK_MUTED, ls=1),
           T("Speed value", 1000, 394, 140, "0.4 m/s", 10, 700, DARK_TEXT, "right"),
           R("Slider track", 800, 414, 340, 6, "#1E304A", 3),
           R("Slider fill", 800, 414, 136, 6, CYAN, 3),
           C("Slider knob", 936, 417, 8, CYAN),
           T("Low", 800, 428, 60, "0.0", 8, 500, DARK_MUTED),
           T("High", 1080, 428, 60, "1.0", 8, 500, DARK_MUTED, "right"))
    e += button(800, 452, 160, 40, "Return home", DARK_PANEL_2, DARK_TEXT, 10,
                DARK_LINE, size=10.5, group="Manual control")
    e += button(980, 452, 160, 40, "Calibrate", DARK_PANEL_2, DARK_TEXT, 10,
                DARK_LINE, size=10.5, group="Manual control")
    e += button(800, 504, 340, 34, "STOP ROBOT", RED, WHITE, 9, size=9.5,
                group="Manual control")

    # Bottom telemetry strip
    e += G("Telemetry strip",
           R("Card", 20, 564, 740, 236, DARK_PANEL, 18, DARK_LINE),
           T("Title", 40, 580, 300, "LIVE TELEMETRY", 9, 800, DARK_MUTED, ls=1.2))
    metrics = [("battery", "BATTERY", "78%", TEAL), ("gauge", "DISTANCE", "1.2 m", CYAN),
               ("cpu", "TILT", "3.2°", AMBER), ("signal", "SIGNAL", "-52 dBm", PURPLE)]
    for i, (ic, label, value, color) in enumerate(metrics):
        x = 40 + i * 175
        e += G(f"Metric {i + 1}",
               R("Tile", x, 600, 160, 74, "#0D1727", 12, DARK_LINE),
               *icon(ic, x + 14, 612, 16, color),
               T("Label", x + 38, 612, 110, label, 8, 700, DARK_MUTED, ls=.8),
               T("Value", x + 14, 636, 130, value, 18, 800, DARK_TEXT),
               T("State", x + 14, 660, 130, "Nominal", 8.5, 500, color))
    e += G("Telemetry strip",
           T("Log title", 40, 690, 200, "EVENT LOG", 8, 700, DARK_MUTED, ls=1.2))
    logs = [("14:32:08", "INFO", "Session started · S-1042", TEAL),
            ("14:32:12", "INFO", "Robot connected over UDP", TEAL),
            ("14:32:26", "WARN", "Obstacle 0.4 m ahead · auto slow", AMBER)]
    for i, (tm, level, msg, color) in enumerate(logs):
        y = 708 + i * 22
        e += G("Telemetry strip",
               T("Time", 40, y, 70, tm, 8.5, 500, DARK_MUTED),
               T("Level", 118, y, 46, level, 8.5, 700, color),
               T("Message", 172, y, 540, msg, 8.5, 500, DARK_TEXT))

    # Arm controls
    e += G("Arm controls",
           R("Card", 780, 564, 380, 236, DARK_PANEL, 18, DARK_LINE),
           T("Title", 800, 580, 240, "ARM & GRIPPER", 9, 800, DARK_MUTED, ls=1.2),
           T("Hint", 800, 596, 240, "Press and hold to move.", 8.5, 500, DARK_MUTED))
    for i, (label, ic) in enumerate([("Raise", "chevron-up"), ("Lower", "chevron-down"),
                                     ("Open", "plus"), ("Close", "close")]):
        x = 800 + (i % 2) * 175
        y = 614 + (i // 2) * 50
        e += button(x, y, 155, 40, label, DARK_PANEL_2, DARK_TEXT, 9, DARK_LINE,
                    icon_name=ic, size=10)
    e += button(800, 730, 340, 40, "Calibrate arm", DARK_PANEL_2, CYAN, 9, CYAN,
                size=10, group="Arm controls")

    e.append(T("Footer", 20, 812, 700,
               "Mode Manual · Speed 0.4 m/s · Link UDP · Firmware v0.1-sim",
               8.5, 500, DARK_MUTED))
    e.append(T("Session", 780, 812, 380, "Session S-1042 · 08:24", 8.5, 500,
               DARK_MUTED, "right"))
    return screen("robot", "01-control-room", "Control room",
                  "Live camera, joystick, speed, arm and emergency stop.",
                  1180, 840, DARK, e)


def telemetry():
    e = []
    e += robot_topbar()
    e += G("Page header",
           T("Title", 20, 84, 300, "Telemetry", 24, 800, DARK_TEXT),
           T("Sub", 20, 118, 420, "Live sensors and robot health.", 11, 500, DARK_MUTED))
    e += button(930, 88, 104, 36, "Calibrate", DARK_PANEL_2, DARK_TEXT, 9,
                DARK_LINE, size=10)
    e += button(1046, 88, 114, 36, "Restart", DARK_PANEL_2, RED, 9, DARK_LINE,
                size=10)

    cards = [("battery", "BATTERY", "78%", "≈ 3 h 20 m remaining", TEAL),
             ("gauge", "DISTANCE", "1.2 m", "Nearest obstacle", CYAN),
             ("cpu", "IMU TILT", "3.2°", "Within safe range", AMBER),
             ("settings", "MOTORS", "4 / 4", "All joints responding", TEAL),
             ("temperature", "CPU TEMP", "41°C", "Normal under load", AMBER),
             ("signal", "SIGNAL", "-52 dBm", "UDP · 24 ms latency", PURPLE)]
    for i, (ic, label, value, sub, color) in enumerate(cards):
        x = 20 + (i % 3) * 380
        y = 148 + (i // 3) * 148
        g = f"Sensor {i + 1}"
        e += G(g,
               R("Card", x, y, 360, 132, DARK_PANEL, 16, DARK_LINE),
               C("Icon tile", x + 34, y + 34, 18, "#0D1727"),
               *icon(ic, x + 24, y + 24, 20, color),
               T("Label", x + 68, y + 24, 240, label, 9, 700, DARK_MUTED, ls=1.1),
               T("Value", x + 20, y + 58, 220, value, 28, 800, DARK_TEXT),
               T("Sub", x + 20, y + 100, 260, sub, 9.5, 500, DARK_MUTED))
        if i == 0:
            e += G(g,
                   C("Ring track", x + 300, y + 62, 24, "none", "#1E304A", 7),
                   P("Ring fill", 0, 0, arc_path(x + 300, y + 62, 24, -90, 190),
                     stroke=TEAL, sw=7))
        elif i == 2:
            e += G(g,
                   R("Tilt track", x + 250, y + 76, 88, 6, "#1E304A", 3),
                   C("Tilt knob", x + 268, y + 79, 6, AMBER))
        elif i == 3:
            for d in range(4):
                e += G(g, C("Motor dot", x + 260 + d * 20, y + 76, 6, TEAL))

    # Chart
    e += G("Current chart",
           R("Card", 20, 452, 760, 320, DARK_PANEL, 18, DARK_LINE),
           T("Title", 40, 470, 300, "Motor current", 13, 700, DARK_TEXT),
           T("Sub", 40, 490, 300, "Amps · last 60 seconds", 9, 500, DARK_MUTED),
           C("Legend one", 570, 480, 4, CYAN),
           T("Legend one label", 580, 474, 80, "Left", 8.5, 500, DARK_MUTED),
           C("Legend two", 634, 480, 4, AMBER),
           T("Legend two label", 644, 474, 80, "Right", 8.5, 500, DARK_MUTED))
    e += line_chart(56, 520, 690, 190, [2.1, 2.4, 2.2, 2.8, 3.1, 2.9, 3.4, 3.2, 3.6, 3.3],
                    CYAN, fill_color=CYAN, grid_color="#1E304A",
                    labels=["0s", "15s", "30s", "45s", "60s"],
                    group="Current chart")
    e += G("Current chart",
           T("Y label", 34, 514, 20, "4.0", 8, 500, DARK_MUTED, "right"),
           T("Y label", 34, 610, 20, "2.0", 8, 500, DARK_MUTED, "right"),
           T("Y label", 34, 706, 20, "0.0", 8, 500, DARK_MUTED, "right"))

    # Event log
    e += G("Event log",
           R("Card", 800, 452, 360, 320, DARK_PANEL, 18, DARK_LINE),
           T("Title", 820, 470, 220, "Event log", 13, 700, DARK_TEXT),
           *badge(1070, 466, "All", CYAN, "#0F2A33", w=52, group="Event log"))
    events = [("14:32:26", "WARN", "Obstacle 0.4 m ahead", AMBER),
              ("14:31:58", "INFO", "Speed limit applied", TEAL),
              ("14:31:40", "INFO", "Arm calibrated", TEAL),
              ("14:30:12", "INFO", "Session resumed", TEAL),
              ("14:28:04", "WARN", "Battery below 80%", AMBER),
              ("14:26:30", "INFO", "Child linked · Salma", TEAL)]
    for i, (tm, level, msg, color) in enumerate(events):
        y = 506 + i * 42
        e += G("Event log",
               T("Time", 820, y, 60, tm, 8.5, 500, DARK_MUTED),
               T("Level", 888, y, 42, level, 8, 700, color),
               T("Message", 940, y, 200, msg, 8.5, 500, DARK_TEXT),
               R("Row line", 820, y + 26, 320, 1, "#1A2940"))
    e.append(T("Footer", 20, 812, 700,
               "Last update 14:32:08 · refresh 250 ms", 8.5, 500, DARK_MUTED))
    return screen("robot", "02-telemetry", "Telemetry",
                  "Sensor cards, motor current chart and event log.",
                  1180, 840, DARK, e)


def session():
    e = []
    e += robot_topbar()
    e += G("Session header",
           T("Title", 20, 84, 320, "Session S-1042", 22, 800, DARK_TEXT),
           T("Sub", 20, 114, 420, "Memory Match with Salma · started 14:24", 10, 500, DARK_MUTED),
           C("Child avatar", 760, 102, 16, CREAM),
           T("Initial", 752, 94, 16, "S", 9, 800, MAROON, "center"),
           T("Child", 784, 92, 120, "Salma · Age 7", 10, 600, DARK_TEXT),
           *badge(900, 88, "Live", TEAL, "#0F2A27", w=54, group="Session header"))
    e += button(1014, 86, 146, 38, "End session", RED, WHITE, 9, size=10,
                group="Session header")

    # Command console
    e += G("Command console",
           R("Card", 20, 148, 740, 412, DARK_PANEL, 18, DARK_LINE),
           T("Title", 40, 166, 300, "COMMAND CONSOLE", 9, 800, CYAN, ls=1.2),
           T("Hint", 40, 184, 400, "Type a command or use a quick action.", 9, 500, DARK_MUTED))
    lines = [("14:31:58", "/say Great job, Salma!", "OK · spoken", TEAL),
             ("14:30:40", "/move forward 20", "OK · 0.2 m", TEAL),
             ("14:29:12", "/lights green", "OK · LED set", TEAL),
             ("14:27:55", "/pause", "OK · paused 20 s", AMBER),
             ("14:24:02", "/start session", "OK · session live", TEAL)]
    for i, (tm, cmd, res, color) in enumerate(lines):
        y = 214 + i * 40
        e += G("Command console",
               T("Time", 40, y, 60, tm, 8.5, 500, DARK_MUTED),
               T("Command", 112, y, 300, cmd, 9.5, 600, DARK_TEXT),
               T("Result", 470, y, 200, res, 8.5, 500, color),
               R("Row line", 40, y + 26, 700, 1, "#1A2940"))
    for i, label in enumerate(["Wave", "Say hello", "Dance", "Pause"]):
        e += button(40 + i * 96, 424, 88, 30, label, DARK_PANEL_2, DARK_TEXT, 15,
                    DARK_LINE, size=9)
    e += G("Command console",
           R("Input", 40, 476, 560, 48, "#0D1727", 12, DARK_LINE),
           T("Placeholder", 56, 490, 400, "Type /say, /move, /lights …", 10, 500, DARK_MUTED),
           *icon("chevron-right", 566, 490, 18, CYAN))
    e += button(616, 476, 124, 48, "Send", CYAN, DARK, 12, size=10.5,
                group="Command console")

    # Session plan
    e += G("Session plan",
           R("Card", 780, 148, 380, 412, DARK_PANEL, 18, DARK_LINE),
           T("Title", 800, 166, 240, "SESSION PLAN", 9, 800, DARK_MUTED, ls=1.2),
           T("Progress", 1020, 166, 120, "2 of 4", 9, 700, CYAN, "right"))
    steps = [("Connect robot", True), ("Choose activity", True),
             ("Calibrate arm", False), ("Start session", False)]
    for i, (label, done) in enumerate(steps):
        y = 200 + i * 44
        e += G("Session plan",
               C("Step circle", 812, y + 10, 10, TEAL if done else "#1E304A"),
               *icon("check", 805, y + 3, 14, DARK) if done else [],
               T("Step label", 834, y + 2, 250, label, 10.5, 600,
                 DARK_TEXT if done else DARK_MUTED),
               R("Step line", 834, y + 25, 280, 1, "#1A2940") if i < 3 else [])
    e += G("Session plan",
           T("Notes label", 800, 380, 200, "SESSION NOTES", 8.5, 700, DARK_MUTED, ls=1),
           R("Notes box", 800, 398, 340, 76, "#0D1727", 10, DARK_LINE),
           T("Notes", 814, 410, 312, "Salma matched 6 pairs. Needs a slower pace on the last two.", 9, 500, DARK_MUTED, lh=14),
           R("Timer box", 800, 490, 340, 44, "#0D1727", 10, DARK_LINE),
           *icon("clock", 814, 504, 16, CYAN),
           T("Timer", 838, 504, 140, "08:24 elapsed", 10, 700, DARK_TEXT),
           T("Timer note", 1000, 505, 126, "No limit", 8.5, 500, DARK_MUTED, "right"))

    # Activity progress
    e += G("Activity card",
           R("Card", 20, 580, 740, 200, DARK_PANEL, 18, DARK_LINE),
           T("Title", 40, 598, 400, "ACTIVITY · MEMORY MATCH", 9, 800, CYAN, ls=1.2),
           T("Pairs", 600, 598, 140, "6 of 8 pairs", 9, 700, DARK_TEXT, "right"),
           R("Track", 40, 622, 700, 8, "#1E304A", 4),
           R("Fill", 40, 622, 525, 8, TEAL, 4))
    metrics = [("COMMANDS", "18"), ("ERRORS", "0"), ("LATENCY", "24 ms"), ("UPTIME", "08:24")]
    for i, (label, value) in enumerate(metrics):
        x = 40 + i * 175
        e += G("Activity card",
               R("Tile", x, 650, 160, 58, "#0D1727", 10, DARK_LINE),
               T("Label", x + 12, 660, 130, label, 7.5, 700, DARK_MUTED, ls=.8),
               T("Value", x + 12, 676, 130, value, 16, 800, DARK_TEXT))
    e += G("Activity card",
           T("Last", 40, 728, 700, "Last command: /say “Great job!” · delivered in 24 ms", 9, 500, DARK_MUTED))

    # Safety
    e += G("Safety card",
           R("Card", 780, 580, 380, 200, DARK_PANEL, 18, DARK_LINE),
           T("Title", 800, 598, 200, "SAFETY", 9, 800, DARK_MUTED, ls=1.2))
    toggles = [("Obstacle stop", True), ("Speed limit 0.4", True), ("Child lock", True)]
    for i, (label, on) in enumerate(toggles):
        y = 622 + i * 32
        e += G("Safety card",
               T("Label", 800, y + 2, 200, label, 9.5, 600, DARK_TEXT),
               R("Track", 1080, y, 36, 20, TEAL if on else "#1E304A", 10),
               C("Knob", 1106 if on else 1090, y + 10, 7, WHITE if on else DARK_MUTED))
    e += button(800, 720, 340, 38, "Stop robot", RED, WHITE, 9, size=10,
                group="Safety card")
    e.append(T("Footer", 20, 812, 700,
               "Session S-1042 · Operator MK · Mode manual", 8.5, 500, DARK_MUTED))
    return screen("robot", "03-session", "Session & commands",
                  "Command console, session checklist, activity and safety.",
                  1180, 840, DARK, e)


SCREENS = [control_room(), telemetry(), session()]
