"""All SPARK screens, in presentation order."""

from screens_system import SCREENS as SYSTEM
from screens_child import SCREENS as CHILD
from screens_parent import SCREENS as PARENT
from screens_robot import SCREENS as ROBOT
from screens_doctor import SCREENS as DOCTOR
from screens_admin import SCREENS as ADMIN

ROLES = [
    {"id": "system", "title": "Design system", "page": "00 · Design system",
     "folder": "00-design-system", "accent": "#286CB5",
     "blurb": "Tokens, colours, type and components shared by every role."},
    {"id": "child", "title": "Child app", "page": "01 · Child app",
     "folder": "01-child", "accent": "#FF8310",
     "blurb": "Playful 390×844 mobile app: home, IQ question, rewards, progress."},
    {"id": "parent", "title": "Parent app", "page": "02 · Parent app",
     "folder": "02-parent", "accent": "#54040F",
     "blurb": "Calm mobile app: dashboard, child progress, reports, account."},
    {"id": "robot", "title": "Robot control", "page": "03 · Robot control",
     "folder": "03-robot-control", "accent": "#22D3EE",
     "blurb": "Dark 1180×840 tablet console: camera, joystick, telemetry, sessions."},
    {"id": "doctor", "title": "Doctor workspace", "page": "04 · Doctor",
     "folder": "04-doctor", "accent": "#286CB5",
     "blurb": "Desktop 1440×1024: overview, child assessment, report review, exports."},
    {"id": "admin", "title": "Admin & research", "page": "05 · Admin & research",
     "folder": "05-admin-research", "accent": "#2DC197",
     "blurb": "Desktop 1440×1024: platform overview, users, analytics, audit."},
]

SCREENS = SYSTEM + CHILD + PARENT + ROBOT + DOCTOR + ADMIN
