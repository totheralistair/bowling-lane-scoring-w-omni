# Decision Record: Bowling Lane Scoring goal document

A summary of how each decision behind the goal document was made: who decided, why, and what was rejected. It is not a transcript. This record is for the human and the cold reviewer only; `omni-ee init --spec` gets only the goal document.

## Contents

- [Status](#status)
- [Idea (hypothesis)](#idea-hypothesis)
- [Decisions](#decisions)
- [Open questions and unclaimed markers](#open-questions-and-unclaimed-markers)

## Status

- **Goal document:** `docs/goal/bowling-lane-scoring-goal.md` (not drafted; drafting is phase 3)
- **Phase:** 0, Idea
- **Depth:** standard (agent-proposed, human accepted "yes", 2026-11-09)
- **Entry point (altitude):** not yet chosen
- **Next contribution only the human can make:** choose the entry point (which OMNI starting point the document targets)

## Idea (hypothesis)

Taken from the completed Intent Map project "Bowling Lane Scoring" (`9734b3f5-3e03-4ca6-8601-d315526caaf0`), where every entity was gated on 2026-11-09. The reasoning behind it is in `specs/intent-map/bowling-lane-scoring-session.md`.

- **Situation:** a group of bowlers walks up to a lane that scores only on paper. Customers complain that paper feels old, and the owner fears losing repeat visits.
- **Problems:** "Score kept for everyone" and "The score settles the rules".
- **Objective:** "Bowlers take to the new lanes on their own".
- **Solution (the user's plan):** a scoring app on a tablet at the head of each lane that keeps the score for the whole group.
  - The group enters names in bowling order, which starts the game.
  - After every roll, the pinsetter sends which of its two rolls it was and the pins down so far in that pair ("1st roll, 3" then "2nd roll, 6").
  - The app scores every frame and shows who bowls next.
  - If a count is missing or wrong, the players go to the main desk and play waits.
  - **Detail, 10th frame only:** in the two stuck endings (strike-strike-non-strike, and spare then a non-strike bonus ball), the app asks for one free extra ball to clear the lane and ignores its pins. (Corrected 2026-11-09 at the user's prompting: this detail had been placed in the Solution's headline.)
- **No-gos:** no rules in the pinsetter; no timers in either app; no login, lane assignment or payment.
- **Appetite:** small. Above all, a correct score after every frame. Try to keep showing who bowls next. Polish gives way first.
- **Riskiest assumption:** the pinsetter app can be changed cheaply to send this message, and it knows the pins left standing at its 2nd check. Test: a demo of "1st roll, 3 / 2nd roll, 6" arriving on another device.
- **Prior failure F1** (docs/system-modeling/transcript.md): agents put lane assignment and payment into a login app. This is a reason to keep each app's responsibilities explicit.

## Decisions

- **Depth: standard (agent-proposed, human accepted, 2026-11-09).** Why: several OMNI agents consume the document, and it fixes the pinsetter-to-tablet message. Rejected: light (too few challenges for a contract with another system) and full (the formal ownership agreement adds ceremony; the user has accepted the split many times).

- **Solution headline (human, 2026-11-09):** the plan is "Lane tablet keeps score for the group". The free clearing roll is a 10th-frame detail. Who: the human spotted the problem; the agent proposed the title; the human said "rename it". The intent-map Solution was renamed and read back.

## Open questions and unclaimed markers

- Queued for later turns (the user's standing questions): what previous projects teach us to carry forward and to fix; how we will hear from the people using it.
