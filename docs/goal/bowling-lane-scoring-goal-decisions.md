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
- **Next contribution only the human can make:** the open items in `docs/goal/use-case-play-a-game-cut3.md`: the rule for rolls after the 10th frame (6a); whether to add an extension for a pinsetter message arriving out of order; who "the manager" is (desk staff or owner/manager).
- **Session closed 2026-11-11** in phase 1. Charging is settled (see Decisions, 2026-11-11). Resume with `/goal-writing` (or `/omni-guide`), read this record and the third cut, and ask the open items one at a time.
- **Guide bookmark:** at session start it was already in `~/.omni-ee` for this project's run; parked at close as `.omni-ee/guide-state-parked-20261111.json` (shasum checked).
- **Outside goal writing:** the OMNI bug report is drafted at `docs/omni-feedback/2026-11-09-guide-state-cannot-move-to-project.md`; the user will send it to the OMNI team.
- **Still to cover in phase 1:** the third cut's open items; the manager's use cases (game count and Reset; Reset by login); the LM app to tablet exchange; the group size; the agent's in/out list (unclaimed), including whether the LM app connection is in the trial or the desk asks the group; the "feels invisible" principle (unclaimed); limits such as speed, reliability and security; the proof environment (where the trial's proof runs; the pinsetter demo); risks (add the LM app connection beside the pinsetter); trade-off priorities; success criteria (measure-then-target). Readiness gaps against `general-objective` were listed in the session of 2026-11-11.

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

- **Scoring arithmetic stays out of the use case (human, 2026-11-10):** "leave the scoring rules out of the use cases and just say 'scored according to the rules of bowling'". Raised by the human's check (strike, strike, strike, 7 spare, 2 3 = 94): the draft wrongly said a frame is scored straight after its 2nd ball. The agent tried a forward-looking rules table, then a backward-looking one (the human: a program can only see the current and previous balls); the human then chose to leave the rules out. The X X X 7/ 2 3 = 94 example remains a useful test case.

### 2026-11-11

- **Transition cases (human's analysis, 2026-11-11):** what a new group can face depends only on how the previous group left (reset, full games, part game) and what the new group presses; "found state doesn't matter". Six cases; the agent's separate "New Game then left" case is a part game (human). The agent had missed "part game, then New Game".
- **Arrival table (human, 2026-11-11):** an extension table lists all and only the transition steps, with the "End game…?" checks shown in it for readability. Start Over or New Game pressed during a group's own game belongs in an "at any time" extension. Rejected: the agent's grouping by outcome (good/broken billing) and moving the checks out of the table.
- **New Game can be pressed mid-game (implied by the human's table, 2026-11-11).**
- **Billing through the Lanes Manager app (human, 2026-11-11):** the LM app does not assign a lane to a new group until the previous group pays. At payment the LM app asks the tablet how many games were started since the last Reset, then sends Reset; the tablet shows a blank sheet, "Enter Players". The LM app also resets at the start of the day. A connection between the LM app and the tablets already exists (human). So a new group always finds a blank sheet, and the arrival table's broken-billing rows go away. Reverses the 2026-11-09 rejection of a desk reset: that one was tied to lane assignment; this one is tied to payment, and lane assignment stays in the LM app. Fallback, "a starting point": the desk asks the group how many games (human).
- **A game starts at its first roll (human, 2026-11-11):** every started game is reported, finished or not; "if the manager wants to discount a partial game, it's their option, not part of the reporting". Agent note, unclaimed: Start Over pressed at the lane should not zero the count; only the LM app's Reset does.
- **Manager login on the tablet (human, 2026-11-11):** "mark a separate login for the manager, who will get their own use case(s)". First use: Reset when the LM app's Reset does not arrive. Exception to the "no login" no-go. Agent-proposed wording, not yet confirmed: manager actions only; bowlers never log in; lane assignment and payment stay in the LM app (F1).
- **"All done" is defined by paying (human, 2026-11-11):** "they just walk away when they feel done." No "All done" question on the tablet.
- **Pinsetter message (human's third cut, 2026-11-11):** roll number (1st or 2nd) and pins currently down, i.e. the total so far on that rack. The pinsetter knows nothing of the 10th frame, so the stuck 10th-frame case stays: "3rd roll in 10th frame leaves the Pinsetter waiting for its 2nd roll (e.g. XX3 or 5/2; X34 is not a problem)" (human's wording, agent's tweak). Closes the second cut's open issue 5.
- **Use cases cover only what the app can detect (human, 2026-11-11):** "the software only has to deal with conditions the app can detect". So a roll out of turn is dropped, and F2 ("bowlers can never change a pin count") is not stated in the use case; it goes into the goal document's constraints as a Must. A lost pinsetter message is undetectable, but a message arriving out of order is detectable (agent; open).

## Lessons from earlier projects

| Id | What happened | Status | Carry forward |
|---|---|---|---|
| F1 | Agents put lane assignment and payment into a login app (docs/system-modeling/transcript.md) | Guarded by the no-go "no login, lane assignment or payment" | State each app's job and what it must not do |
| F2 | In the earlier attempt, bowlers could override the pinsetter's numbers in the scoring app (user, 2026-11-09) | Caught in the intent map on 2026-11-03: the agent's "bowler corrects on the tablet" fallback was withdrawn; the pinsetter's count is the source of truth; only the main desk corrects a roll (deferred) | **Must** (agent-proposed, human accepted 2026-11-09): "Bowlers can never change a pin count on the tablet." Reopen deliberately if bowler self-correction is ever wanted. |

## Open questions and unclaimed markers

- Unclaimed: `docs/goal/use-case-play-a-game.md`, a use case with extensions drafted by the agent at the user's request (2026-11-09) to work through charging and the end of a game. Its ✋ items are agent guesses; its OPEN items are the user's.
- Under discussion, not approved: `docs/goal/use-case-play-a-game-cut2.md`, the user's second cut (2026-11-10). Neither cut is approved; the first is kept for comparison.
- Under discussion, not approved: `docs/goal/use-case-play-a-game-cut3.md`, the user's third cut (2026-11-11), with its open items. The user's working copy is `bowling use case.docx`.

- Charging: settled 2026-11-11 (LM app asks the count, then resets).

- Unclaimed: the agent's proposed Must/Should/Could/Won't scope list for the trial (proposed 2026-11-09).

- Unclaimed: "feels invisible" as an app-wide principle.
