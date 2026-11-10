# SPARK UI/UX kit — design inventory

Separate UI/UX for every product surface. Each screen is a fixed, editable frame;
the SVG files import into Figma and the plugin rebuilds them as named layers.

## Roles and folders

| Role | Folder | Screens | Canvas |
| --- | --- | --- | --- |
| Design system | `screens/00-design-system/` | 1 | 1440×1240 |
| Child app | `screens/01-child/` | 4 | 390×844 |
| Parent app | `screens/02-parent/` | 4 | 390×844 |
| Robot control | `screens/03-robot-control/` | 3 | 1180×840 |
| Doctor workspace | `screens/04-doctor/` | 4 | 1440×1024 |
| Admin & research | `screens/05-admin-research/` | 4 | 1440×1024 |

## Screen inventory

### Design system

Tokens, colours, type and components shared by every role.

| # | Screen | Size | Purpose | File |
| --- | --- | --- | --- | --- |
| 1 | Design system | 1440×1240 | Brand colours, role accents, typography and shared components. | `screens/00-design-system/00-design-system.svg` |

### Child app

Playful 390×844 mobile app: home, IQ question, rewards, progress.

| # | Screen | Size | Purpose | File |
| --- | --- | --- | --- | --- |
| 1 | Home | 390×844 | Today's mission, plan and weekly streak. | `screens/01-child/01-home.svg` |
| 2 | IQ question | 390×844 | Focused assessment question with progress and answer states. | `screens/01-child/02-iq-question.svg` |
| 3 | Game result | 390×844 | Celebration, score ring, rewards and next actions. | `screens/01-child/03-result.svg` |
| 4 | My progress | 390×844 | Skill bars, weekly streak and achievements. | `screens/01-child/04-progress.svg` |

### Parent app

Calm mobile app: dashboard, child progress, reports, account.

| # | Screen | Size | Purpose | File |
| --- | --- | --- | --- | --- |
| 1 | Parent dashboard | 390×844 | Child switcher, weekly summary, activity and practice nudge. | `screens/02-parent/01-home.svg` |
| 2 | Child progress | 390×844 | Score trend, skills, doctor note and recommendations. | `screens/02-parent/02-child-progress.svg` |
| 3 | Reports & activity | 390×844 | Filterable report history and saved files. | `screens/02-parent/03-reports.svg` |
| 4 | Account & privacy | 390×844 | Profile, linked child, settings and parent-only scoping. | `screens/02-parent/04-account.svg` |

### Robot control

Dark 1180×840 tablet console: camera, joystick, telemetry, sessions.

| # | Screen | Size | Purpose | File |
| --- | --- | --- | --- | --- |
| 1 | Control room | 1180×840 | Live camera, joystick, speed, arm and emergency stop. | `screens/03-robot-control/01-control-room.svg` |
| 2 | Telemetry | 1180×840 | Sensor cards, motor current chart and event log. | `screens/03-robot-control/02-telemetry.svg` |
| 3 | Session & commands | 1180×840 | Command console, session checklist, activity and safety. | `screens/03-robot-control/03-session.svg` |

### Doctor workspace

Desktop 1440×1024: overview, child assessment, report review, exports.

| # | Screen | Size | Purpose | File |
| --- | --- | --- | --- | --- |
| 1 | Doctor overview | 1440×1024 | Assignments, review queue, schedule and recent reports. | `screens/04-doctor/01-overview.svg` |
| 2 | Child assessment | 1440×1024 | IQ summary, domain radar, recommendations and session history. | `screens/04-doctor/02-child-assessment.svg` |
| 3 | Report review | 1440×1024 | Draft report, sharing controls, version history and approval. | `screens/04-doctor/03-report-review.svg` |
| 4 | Reports & exports | 1440×1024 | Report status table, PDF/CSV exports and privacy note. | `screens/04-doctor/04-exports.svg` |

### Admin & research

Desktop 1440×1024: platform overview, users, analytics, audit.

| # | Screen | Size | Purpose | File |
| --- | --- | --- | --- | --- |
| 1 | Admin overview | 1440×1024 | Platform health, usage, role mix and recent admin activity. | `screens/05-admin-research/01-overview.svg` |
| 2 | Users & roles | 1440×1024 | User directory, role badges, account status and scoping note. | `screens/05-admin-research/02-users.svg` |
| 3 | Research analytics | 1440×1024 | KPIs, score distribution, age cohorts and aggregate privacy. | `screens/05-admin-research/03-research.svg` |
| 4 | Audit & exports | 1440×1024 | Immutable audit table, export queue and retention policy. | `screens/05-admin-research/04-audit.svg` |

## Navigation flow

- **Design system:** Design system
- **Child app:** Home → IQ question → Result → My progress
- **Parent app:** Dashboard → Child progress → Reports → Account
- **Robot control:** Control room → Telemetry → Session & commands
- **Doctor workspace:** Overview → Child assessment → Report review → Exports
- **Admin & research:** Overview → Users & roles → Research → Audit & exports

## Rules the UI must keep

- **Parent scoping:** a parent only sees children linked to their own account.
- **Doctor scoping:** a doctor only sees assigned children; reports are educational, not clinical diagnoses.
- **Researcher privacy:** only anonymised aggregates; suppress cohorts with fewer than 10 participants.
- **Child safety:** robot control is never exposed in the child app; stop controls stay visible in the operator console.
- **Auth states:** empty, loading, error, offline and permission-denied states must be designed before build.
- **RTL:** Arabic is a first-class language; mirror the layout for `ar` and keep numbers LTR.

## Colours

| Token | Hex | Use |
| --- | --- | --- |
| Maroon | `#54040F` | Parent brand, trust |
| Cream | `#FFDB99` | Warm surfaces, highlights |
| Orange | `#FF8310` | Child energy, primary child action |
| Blue | `#286CB5` | Doctor, links, information |
| Sky | `#D8E9FC` | Soft information surfaces |
| Teal | `#2DC197` | Success, admin accent |
| Red | `#D8301E` | Errors, emergency stop |
| Ink | `#241A1F` | Primary text |
| Muted | `#6B7280` | Secondary text |
| Line | `#E7EBF2` | Borders and dividers |

## Typography

| Style | Font | Size | Weight |
| --- | --- | --- | --- |
| Display | Nunito | 40 | 900 |
| Heading | Nunito | 28 | 800 |
| Section | Nunito | 20 | 800 |
| Body | Inter | 14 | 400 |
| Caption | Inter | 12 | 400 |
| Eyebrow | Inter | 10 | 700 |

## What is intentionally still open

- Photo/illustration placeholders are not final assets; drop the exported PNGs from
  `docs/design/assets/` into the frames.
- Empty, loading, error and offline states are described but not drawn for every screen.
- Tablet breakpoints for the parent/doctor workspaces are not separate frames yet.
- The design system frame is a reference board, not a published Figma library.
