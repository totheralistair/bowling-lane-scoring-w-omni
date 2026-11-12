# OMNI Input Readiness: Bowling Lane Scoring (whole repository)

Checked 2026-11-12 at the agreed level, `general-objective` (the agents start by planning the work).

## Contents

- [Verdict](#verdict)
- [What I read](#what-i-read)
- [Entry-point fit](#entry-point-fit)
- [Readiness matrix](#readiness-matrix)
- [Blockers](#blockers)
- [Notes](#notes)
- [Questions to resolve](#questions-to-resolve)
- [Next action](#next-action)

## Verdict

**Not ready** for `general-objective`.

The strategy is strong and fully settled: who it's for, the two problems, the goal and its measures, the chosen way, and a clear give-way order. The trouble is that no Goal document exists yet. What the agents would need is spread over a decision record (which says it is *not* given to the agents), three use case cuts (none approved), and an unclaimed scope list. Several product decisions on the main path are still open, and nothing says where the trial's proof runs or what the tablet is built on.

## What I read

- `docs/goal/bowling-lane-scoring-goal-decisions.md` (whole)
- `docs/goal/use-case-play-a-game-cut3.md` (whole); cut 1 and cut 2 through `bowling use case v2.docx` and `bowling use case.docx` (whole text)
- `specs/intent-map/bowling-lane-scoring-session.md` (lines 1–140 and the last 60 lines, which cover steps 0–4 and 6–9 and the close)
- `intent-map recap` for the project's current state
- Today's earlier transcript, searched for new decisions (none found)
- Not read: `docs/system-modeling/transcript.md` (its one lesson, F1, is quoted in the decision record), the code scaffold, older transcripts.

## Entry-point fit

- Requested: `general-objective`
- Best fit: `general-objective`
- Reason: the material is about product intent and behaviour, with no design. That's the right level. The gap is completeness, not level.

## Readiness matrix

| Area | Status | Evidence | Gap |
|---|---|---|---|
| Intent | Pass | Intent Map recap; decision record "Idea" | Must be restated in the Goal document itself |
| Scope | Blocker | Decision record "Still to cover": in/out list unclaimed; LM app link in the trial or not | No settled in/out list for the trial |
| Decisions | Blocker | Cut 3 "Open in this cut"; decision record "Next contribution" | Rule for rolls after the 10th frame (6a); out-of-order message; who "the manager" is; manager use cases unwritten |
| Traceability | Pass | Decisions each say who decided and why | — |
| Testability | Note | OKR uses measure-then-target KRs | No statement of what proves the *trial build* works (e.g. the X X X 7/ 2 3 = 94 case) |
| Edge cases | Pass (partly) | Cut 3 extensions, 10th-frame clearing ball, end-of-game and arrival cases | Open items above; 5b is "… procedure involving front desk" |
| Dependencies | Blocker | Pinsetter change untested; LM app ↔ tablet exchange "already exists" but undescribed | Whether agents build the pinsetter change; what the LM app sends and asks |
| Ambiguity | Blocker | Several items marked unclaimed or "agent's wording, not yet confirmed" | Open items don't say which stage needs them or who decides |
| Priority | Blocker | Must/Should/Could/Won't list is unclaimed; F2 is a Must; desk corrections are Won't | No confirmed priority list for the trial |
| Proportionality | Note | Appetite "small"; trial bowlers know it's a trial | Fine once the priority list is confirmed |
| Non-functional constraints | Blocker | None stated | Tablet platform or stack; how reliable it must be; security of the manager login; whether players' names are kept |
| Proof environment | Blocker | Pinsetter demo is the cheapest test; it hasn't run | Real pinsetter or a stand-in? Real LM app or a stand-in? Who supplies them? |
| Documentation | Note | Not stated | What help bowlers and desk staff get; whether a decision log is kept |
| Leanness | Pass | "Scored according to the rules of bowling" kept out of the use case | — |

## Blockers

### 1. There is no Goal document

- **Location:** decision record, Status: "Goal document … (not drafted; drafting is phase 3)"; and "This record is for the human and the cold reviewer only; `omni-ee init --spec` gets only the goal document."
- **Why it blocks OMNI:** the agents get one document. Today they'd have to piece intent together from drafts and unapproved cuts, and would guess which cut wins.
- **Fix:** draft `docs/goal/bowling-lane-scoring-goal.md` from the settled material, with an approved use case.

### 2. Product decisions still open on the main path

- **Location:** cut 3, "Open in this cut"; decision record, "Still to cover in phase 1".
- **Why it blocks OMNI:** epic planning would invent the answers: what happens when balls roll after the game ends (6a); whether an out-of-order pinsetter message is handled; whether "the manager" is desk staff or the owner; what the manager's own use cases are (game count, Reset, Reset by login); whether Start Over at the lane zeroes the game count.
- **Fix:** answer each one, or mark it Won't for the trial and say which later stage decides it.

### 3. Scope and priorities for the trial aren't confirmed

- **Location:** decision record, "Unclaimed: the agent's proposed Must/Should/Could/Won't scope list"; "whether the LM app connection is in the trial or the desk asks the group"; group size open since cut 1 (3b).
- **Why it blocks OMNI:** without a confirmed in/out list, epic planning absorbs nearby features. That's how F1 happened.
- **Fix:** confirm the in/out list and the Must/Should/Could/Won't list, including the LM app link and the largest and smallest group.

### 4. The manager login conflicts with a no-go until its wording is confirmed

- **Location:** decision record, 2026-11-11, "Manager login on the tablet … Exception to the 'no login' no-go. Agent-proposed wording, not yet confirmed."
- **Why it blocks OMNI:** "no login" and "manager login" both stand. That is exactly the F1 shape (login, lane assignment and payment drifting into one app).
- **Fix:** confirm the exception's wording: manager actions only; bowlers never log in; lane assignment and payment stay in the LM app.

### 5. Who builds what across the three apps

- **Location:** Intent Map: "we are creating a small system of 2 apps"; the pinsetter change is the riskiest assumption; the LM app link "already exists" (decision record, 2026-11-11).
- **Why it blocks OMNI:** agents can't tell whether the pinsetter change and the LM app exchange are theirs to build or someone else's to deliver.
- **Fix:** state, for each of the tablet, the pinsetter app and the LM app: who builds or changes it in this run, and what it must never do.

### 6. Where the trial is proven

- **Location:** none; the pinsetter demo is named as the cheapest test but hasn't run.
- **Why it blocks OMNI:** agents can't reach a real pinsetter or LM app. They'd either invent stand-ins or stop mid-run.
- **Fix:** say whether proof runs against the real pinsetter and LM app or stand-ins; who supplies access or recorded messages; and what proof must never touch (for example, the live billing).

### 7. Limits aren't stated

- **Location:** none.
- **Why it blocks OMNI:** the stack, reliability, and the manager login's security are your calls at every level. Left blank, agents pick the strictest or the most convenient.
- **Fix:** name the tablet platform (or say it's open), how reliable a lane must be, how the manager login is protected, and whether names are kept after Reset.

## Notes

- `bowling use case v2.docx` and the earlier `.docx` are untracked, and v2 is open in Word right now. Only committed files reach the agents.
- Say what proof is enough for the trial build: for example, a set of known games scored correctly (X X X 7/ 2 3 = 94), plus the pinsetter demo.
- Carry the give-way order from the Intent Map into the Goal document as trade-off priorities: a correct score above all; try to keep "who bowls next"; polish gives way first.
- "Feels invisible" is still unclaimed as an app-wide principle.

## Questions to resolve

1. After the 10th frame, what happens when balls keep rolling (6a)?
2. Who is "the manager": desk staff or the owner/manager?
3. Is the LM app link in the trial, or does the desk ask the group how many games?
4. Do the agents build the pinsetter change, or does someone else deliver it?
5. Where is the trial proven: the real pinsetter and LM app, or stand-ins?
6. What is the tablet built on, or is that open?
7. Confirm the trial's Must/Should/Could/Won't list.
8. Confirm the manager-login wording.
9. Out-of-order pinsetter message: handle it in the trial, or later?

## Next action

Revise via `goal-writing` (finish phase 1's open items, then draft the Goal document), then re-check.
