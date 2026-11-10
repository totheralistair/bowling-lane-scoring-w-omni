# Decision Record: Bowling Lane Scoring goal document

A summary of how each decision behind the goal document was made: who decided, why, and what was rejected. It is not a transcript. This record is for the human and the cold reviewer only; `omni-ee init --spec` gets only the goal document.

## Contents

- [Status](#status)
- [Idea (hypothesis)](#idea-hypothesis)
- [Decisions](#decisions)
- [Open questions and unclaimed markers](#open-questions-and-unclaimed-markers)

## Status

- **Goal document:** `docs/goal/bowling-lane-scoring-goal.md` (not drafted; drafting is phase 3)
- **Phase:** 1, Ground and surface (phase 0 closed 2026-11-09)
- **Depth:** standard (agent-proposed, human accepted "yes", 2026-11-09)
- **Entry point (altitude):** `general-objective`, i.e. epic planning (agent-proposed, human accepted "yes", 2026-11-09)
- **Next contribution only the human can make:** how charging works today: how the desk knows how many games a group played (use case open issue 1). The user called it a real open problem. The question asked at session close offered: the group says, the desk counts paper sheets, the desk reads the pinsetter, or the alley charges by time (which would remove the Next Game charging risk).
- **Session closed 2026-11-09** in phase 1. Resume with `/goal-writing` (or `/omni-guide`), read this record and `docs/goal/use-case-play-a-game.md`, and re-ask the charging question.
- **Still to cover in phase 1 after charging:** the rest of the use case's open issues (group size, a missing message in the trial, a roll out of turn); the agent's in/out list (unclaimed); the "feels invisible" principle (unclaimed); limits such as speed, reliability and security; the proof environment (where the trial's proof runs; the pinsetter demo); trade-off priorities; success criteria.

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

- **Entry point: `general-objective` (agent-proposed, human accepted, 2026-11-09).** Why: the intent map already settles the what and why, and bowling scoring rules are standard. Fixed limits (the pinsetter message, no rules in the pinsetter, no timers, no login or payment) go in as constraints. Rejected: `functional-spec` (would need every behaviour spelled out) and `technical-spec` (would need the design itself). Cost accepted: agents split the work into epics, which is where prior failure F1 happened, so each app's job must be stated plainly.

- **Depth: standard (agent-proposed, human accepted, 2026-11-09).** Why: several OMNI agents consume the document, and it fixes the pinsetter-to-tablet message. Rejected: light (too few challenges for a contract with another system) and full (the formal ownership agreement adds ceremony; the user has accepted the split many times).

- **Solution headline (human, 2026-11-09):** the plan is "Lane tablet keeps score for the group". The free clearing roll is a 10th-frame detail. Who: the human spotted the problem; the agent proposed the title; the human said "rename it". The intent-map Solution was renamed and read back.

- **F2 rule is a Must (agent-proposed, human accepted 2026-11-09):** "Bowlers can never change a pin count on the tablet." Why: the earlier attempt let bowlers override the pinsetter, and the intent map only implied the fix. Rejected: leaving it implied.

- **Hearing from users (human, 2026-11-09):** "the app should feel invisible, it's just like smart paper - you don't tell the paper you like it - only if you don't." So the app asks for no feedback (no ratings, no surveys, no prompts). A complaint field in the scoring app is a **Could** ("low priority"; "they'll never compliment a scoring app"). Otherwise "it's up to the humans to see how things are going": owner and staff observe, which matches the OMNI KRs (desk help requests, setup time, the manager's walk-around marks).
- Agent note, **unclaimed**: "feels invisible" reads as a product principle for the whole app (it serves P1 and P2 done-states), not only a feedback rule. To be confirmed when behaviour is discussed.

- **Problem statements confirmed (human, "alll good", 2026-11-09):** P1 "Score kept for everyone" and P2 "The score settles the rules", as gated in the intent map, go into the goal document unchanged.

- **Desk corrections reach the score through the pinsetter (human chose A, 2026-11-09).** The main desk uses the pinsetter app's existing manual override, and the pinsetter sends a "change roll score" message to the tablet, which re-scores. The human noted the pinsetter-to-tablet interface must now handle that message. Why: one source of truth (the pinsetter), the desk keeps its existing tool, and F2 holds. Rejected: B, a staff override on the tablet (two places can change a count, F2 risk, and a staff code is a kind of login, which is a no-go); C, no fix in the first release (breaks "above all, a correct score" and undermines P2). Consequence: the riskiest assumption and its demo now cover the correction message too.
- Raised by the user's question (2026-11-09): with desk corrections deferred, the first release's "go to the desk, play waits" had no ending.

- **A correction can fix only the most recent roll, before the next ball is thrown (human, 2026-11-09):** "only legal way to handle it - if the next bowler bowls, it's too late." So the "change roll score" message always means "the roll I just sent was really n", and the pinsetter needs no roll numbering.
- **Desk corrections are not in the first release (human, 2026-11-09):** "we implement this in not-the-first-release, sometime later i don't know when." Priority for this run: **Won't** build the correction; the design must not rule it out (second message, re-score the latest roll). No date set.

- **Reframe (human, 2026-11-09):** "the first iteration won't be a 'release' it is just an iteration to see how things go." Earlier wording about a "first release" (intent map, this record) now means the first iteration, a trial. 

- **Trial bowlers know it is a trial (human, 2026-11-09):** "people who know it's a trial, so don't worry." So in the trial iteration a wrong count stands on the tablet (option 1). The correction message stays for a later iteration, and "above all, a correct score" holds whenever the pinsetter's count is right. Rejected for the trial: moving corrections forward (option 2) and lowering the top priority (option 3).

- **Bowlers start each new group themselves (agent-proposed, human accepted "yes good eye", 2026-11-09).** At the end of a game the final scores stay on screen. The tablet offers "Play again, same players" (keeps names and order) and "New group" (clears everything, goes to name entry). Mid-game, "New group" asks "End this game?" first. Why: no timers, no lane assignment (F1), no staff work; it is like turning to a fresh sheet of paper. Rejected: staff resetting each tablet (staff time for every group), a desk reset tied to lane assignment (F1 no-go), an automatic wipe (needs a timer, which is a no-go). Accepted cost: a careless tap can still end another group's game; the confirm step reduces it.

- **Cast of users confirmed (agent-proposed, human accepted "all good", 2026-11-09):** trial bowlers (who know it's a trial); main desk staff; owner/manager (does not use the tablet, owns the objective); whoever looks after the pinsetter app.

- **End of game, in the human's words (2026-11-09):** "after the last bowler does the 10th frame, the scoring app just sits there, does nothing. Then either the current group goes Next Game, or Start Over (for the next group, if they don't want their names and scores to stay up); or if they just leave, then next group hits 'Next Game' or Start Over." The buttons are named **Next Game** (keeps names and order) and **Start Over** (clears names and scores). These replace the agent's "Play again, same players" and "New group". The "End this game?" check for mid-game use stands from the earlier accepted proposal.

- **Charging consequence (human, 2026-11-09):** the agent called it harmless that a new group pressing Next Game starts with the previous group's names. The human corrected this: "it's not harmless, because the previous group gets charged." Games played under a group's names are charged to that group. Open: how games reach the charge, given payment is a no-go in the app.

## Lessons from earlier projects

| Id | What happened | Status | Carry forward |
|---|---|---|---|
| F1 | Agents put lane assignment and payment into a login app (docs/system-modeling/transcript.md) | Guarded by the no-go "no login, lane assignment or payment" | State each app's job and what it must not do |
| F2 | In the earlier attempt, bowlers could override the pinsetter's numbers in the scoring app (user, 2026-11-09) | Caught in the intent map on 2026-11-03: the agent's "bowler corrects on the tablet" fallback was withdrawn; the pinsetter's count is the source of truth; only the main desk corrects a roll (deferred) | **Must** (agent-proposed, human accepted 2026-11-09): "Bowlers can never change a pin count on the tablet." Reopen deliberately if bowler self-correction is ever wanted. |

## Open questions and unclaimed markers

- Unclaimed: `docs/goal/use-case-play-a-game.md`, a use case with extensions drafted by the agent at the user's request (2026-11-09) to work through charging and the end of a game. Its ✋ items are agent guesses; its OPEN items are the user's.

- How charging works: how the desk knows how many games a group played, and what the app must (or must not) do so a new group's game is never charged to the previous group.

- Unclaimed: the agent's proposed Must/Should/Could/Won't scope list for the trial (proposed 2026-11-09).

- Unclaimed: "feels invisible" as an app-wide principle.
