# Intent Map Session — Bowling Lane Scoring

Synthesis of settled decisions, who supplied them, why, what was rejected, and what remains open.

## Status

- **Mode:** guided creation
- **Current step:** COMPLETE: step 9 closed 2026-11-09. Every entity gated and read back from the CLI.
- **Project:** Bowling Lane Scoring (`9734b3f5-3e03-4ca6-8601-d315526caaf0`)
- **References read:** SKILL.md, references/method.md, references/operations.md
- **Creation path:** incremental (user choice)
- **Entities gated:** Situation `af5973c0-a13a-4b8b-8ae1-ab4393a5db1e`; P1 "Score kept for everyone" `6b32273d-580b-4cca-901c-de923419b41e`; P2 "The score settles the rules" `3ea7e223-9f1a-4126-9956-1596d0a8b4b5`; OKR "Bowlers take to the new lanes on their own" `1df92a72-bc88-4c69-9451-34e8cfb2214b`; Signal "Roll number and pins down after each roll" (revised 2026-11-09) `3f015676-71bb-4cf7-9bd9-3311b5c49265`; External Resource "Pinsetter app" `f09e0144-3895-44ee-8071-444e2ef0a080` (readiness partial); Options "Free clearing roll" `45ef9b12-96e8-40ff-9282-c2eb192cb59f` and "Clear-now command (deferred feature)" `43ae809b-c6d6-4789-804f-fc494098dc95`. Evaluation `5d68900a-bd65-47ab-8095-b8b3245ff037` "Free clearing roll beats rules in the pinsetter" and Solution `e7ad4fa7-b267-4623-8a7e-67c132c71547` "Lane tablet keeps score for the group" (both gated 2026-11-09 at step 8; Solution renamed the same day)
- **Open questions:** (1) settled 2026-11-09: lane tablet; (2) the responsibility split between the two apps is architecture work after step 9, tied to prior failure F1; (3) settled 2026-11-09: Solution draft accepted and created; (4) settled 2026-11-09: riskiest assumption replaced (pinsetter app can send each roll to the tablet). Settled since: the pinsetter knows no frames and stays free of rules; frame scoring lives in the scoring app; the free clearing roll is the choice for now.
- **Unclaimed markers:** (1) resolved 2026-11-09; (2) resolved 2026-11-09: the Solution, including appetite and rabbit holes, was accepted and gated
- **Ordering crossings:** none
- **10th-frame table: corrected 2026-11-03 (user + agent), no longer disputed.** See the corrected table in the step 4 log. The earlier wording "spare (completes the 10)" was too narrow; the user's example strike, 3, 4 (3 pins left) is a clean finish, because the pinsetter treats the 3 and the 4 as its own 1st and 2nd rolls and clears after the 4.
- **Next user contribution:** choose the next move after the strategy: the goal document (return route to omni-guide → goal document → omni-gate), or more strategy work. Also outstanding outside the map: the pinsetter demo (cheapest test) and the omni-guide phase move (blocked).
- **Signal S1: created and gated 2026-11-03** (see step 4 close). Revised 2026-11-09: it now reports roll number (1st/2nd) and pins down so far; the earlier pin count per roll plus the reset event.
- **Context:** routed from omni-guide; return route = goal document → omni-gate. User wants one question per turn.

## Log

### Step 0 — Contract
- User restated the brief instead of `p`; agent took it as the go-ahead.
- **Candidate Solution (user-supplied, parked until step 7):** an existing pinsetter app clears the pins, tracks 1st and 2nd roll, and shows pins knocked down on a dashboard at the bottom of the lane. Add a new bowler app (enter names, see scores) and upgrade the pinsetter app to integrate with it.
- Prior failure F1 (from docs/system-modeling/transcript.md): agents put lane assignment and payment into a login app. Reason to make app responsibilities explicit.
- Project created with user approval: name "Bowling Lane Scoring", description as proposed by agent and accepted by user.

### Step 1 — Situation
- User correction: the moment starts earlier than the agent's question did. Before any ball is rolled, the group has to start their app and enter their names and bowling order. Trigger candidate (user-supplied): group setup before the first roll.
- Tell (premature solution, harmless): "fire up their app" is part of the candidate Solution's flow. Recorded there; the Situation still needs today's reality.
- Today (user-supplied): names, bowling order, and scoring are all on paper. The pinsetter's dashboard shows only the pins knocked down per roll.
- Stakes, first answer (user-supplied): people don't like writing on paper; it feels "old". They want "modern", meaning an electronic app. Candidate emotional job: not feeling the alley is outdated. Agent note: no functional failure of paper has been named; "modern" describes a wished-for outcome rather than a consequence, so the stakes aren't settled yet.
- Open: "their app" — the console at the head of the lane, or bowlers' own phones? Solution detail, parked for step 7.
- User pushback: "stop living in failures - i live in future possibilities." Agent reframed: stakes are recorded as the opportunity gained, not a loss.
- Agent-drafted Situation, **unclaimed** (assembled from the user's words; awaiting the user's acceptance or correction):
  - Who: a group of bowlers at a lane
  - Context: the pinsetter's dashboard shows only pins knocked down per roll; names, bowling order, and scoring are all on paper
  - Trigger: the group arrives and must set up names and bowling order before the first roll
  - Stakes (opportunity): bowlers want a modern, electronic experience instead of paper that feels old
- User addition: the **owner** sees people complain about having to use paper, and fears they won't come back if the alley doesn't LOOK modern, meaning tablet-based. This adds the owner as a stakeholder, and the stakes become repeat visits.
- "Tablet-based" (user-supplied) is recorded as a candidate Solution constraint for step 7, not as part of the Situation.
- Open: whose Situation is this, the owner's or the bowlers'? It's the actor choice and it belongs to the user.
- **Actor chosen (user): the bowlers.** The owner remains a stakeholder in the stakes.
- User's flow (to the Solution, step 7): bowlers walk to the lane and find the app already running, or start it there. They enter their names in bowling sequence, and that starts the game.
- Revised Situation draft, **unclaimed** (supersedes the earlier draft):
  - Who: a group of bowlers
  - Context: at a lane where the pinsetter's dashboard shows only pins knocked down per roll; names, order, and scoring are on paper, which customers complain feels old
  - Trigger: the group walks up to the lane to start a game and must set names and bowling order before the first roll
  - Stakes (opportunity): a modern, tablet-style experience bowlers want, so they come back; the owner fears losing repeat visits otherwise
- **Situation accepted by user ("good").** The revised draft is now claimed. Tell check: approval rather than an answer, but harmless, because every field was built from the user's own words.
- Situation gate: actor, context, trigger, and stakes are all specific. Passes.
- Creation path: incremental (user). Situation created, gated, and read back from the CLI: `af5973c0-a13a-4b8b-8ae1-ab4393a5db1e`, title "Bowlers arrive at a lane that only scores on paper".

### Step 2 — Problem
- Resumed 2026-10-20 from omni-guide. Active CLI project verified to match. Pending question re-asked: the strike moment in frame 3.
- **Job, user-supplied:** "the bowlers want to have fun talking around the bowling game. The bowling itself is just a container for their personal interactions." Emotional/social job: an enjoyable time together; the game is the backdrop to it.
- Tell (premature solution, harmless): the user also described release scope and app behaviour. Parked for step 7, in the user's words:
  - First release: enter preferred names and bowling sequence; highlight who bowls next; after each frame, update the game state from the pin-counter's total pins down (1st and 2nd roll); the app knows what a strike means and updates whatever a strike allows.
  - Later release: announce the next bowler by voice; celebrate a strike so the group cheers (or moans) for the bowler.
- Open (Signal/Solution): on a strike, does the pin-counter send "10" or "strike"? User doesn't know. This is an integration fact that needs checking.
- Agent-drafted gate statement, **unclaimed**: "Bowlers need to know whose turn it is and how the game stands, without anyone tending it, in order to keep their attention on each other and enjoy the time together, but today they can't because names, order, and scores are kept on paper by hand." The blocker ("someone tends the paper and is pulled out of the conversation") is the agent's inference and has not been observed. Placeholder-blocker check is pending.
- **Blocker, observed (user-supplied), so the placeholder-blocker check passes:** (a) "sometimes they argue over how to write the score (imagine two strikes in a row and they don't recall how to score it)"; (b) "the act of writing means that person is missing the celebrations, doing clerical work that takes them out of the fun."
- Compression check: both blockers involve the same actor, the same job, and the same cause (manual paper scoring), so it stays one Problem. Agent qualification: not all arguing is bad. The draft only removes arguing over scoring *rules*, not banter about the game.
- Revised gate statement, **unclaimed** (supersedes the previous draft): "Bowlers need to see whose turn it is and the correct score, kept up for them, in order to stay in the conversation and celebrations together, but today they can't because one of them must keep score on paper by hand. That clerical work takes them out of the fun, and the scoring rules (such as two strikes in a row) are confusing enough that the group argues over them."
- **User correction:** "they argue about the rules of bowling, which is not fun and not banter. That's one problem we're solving." The agent's banter qualification was beside the point. Rule disputes are a problem in their own right.
- Compression re-check: the two blockers have different done-states (the scorekeeper is back in the fun; the group no longer disputes rules). Agent proposes a split into two Problems, **unclaimed**:
  - P1 (clerical): "Bowlers need the score kept for them in order for everyone, including whoever would keep score, to be in the conversation and celebrations, but today they can't because one of them has to write every frame on paper by hand."
  - P2 (rules): "Bowlers need to trust the score without working out the rules in order to keep the game friendly, but today they can't because scoring rules such as two strikes in a row are confusing enough that the group argues over them."
- Done-state question (end of game) is still unanswered. Re-ask it once the split is settled.
- **Split accepted (user): "two separate problems - good."** P1 (clerical) and P2 (rules) wording is claimed. Tell check: approval rather than an answer, but harmless, because both statements were built from the user's own words.
- Both gate statements are complete and tool-free. Before creating: the done-state for each is still owed by the user. Asking P1 first.
- **P1 done-state (user-supplied):** after a strike, the former scorekeeper is "cheering and high-fiving with everyone, not writing anything down." This is observable, so it can become a measure at the OKR step.
- Next: P2 done-state.
- **P2 done-state (user-supplied):** "someone glances at the screen, sees the score, and keeps chatting. If they decide to debate scoring rules, they look at the score and 'deduce' what the rules are, instead of just arguing personally." Emotional job surfaced: the score becomes a neutral referee, so a rules question turns into a puzzle rather than one person being wrong.
- Both Problems now have a gate statement, blocker, and done-state. Resistance forces and initial KPI are not yet supplied and are left empty. Next: preview the creation and get approval.
- **User requirement:** "make sure the app knows how to handle the potential 3-rolls at the end - I don't know whether the pin-setter or this app knows those variations." This is the 10th-frame bonus roll(s) after a strike or spare.
  - Problem-level effect: added to P2's blocker examples, because a trusted score must be right in the 10th frame too. P2 statement becomes "...scoring rules like two strikes in a row or the extra rolls in the 10th frame are confusing enough..."
  - Solution-level (step 7): the scoring must cover the 10th frame's up-to-three rolls.
  - Open (Signal step, joins the "10 or strike" question): what the pinsetter knows and reports. Does it know about frames, strikes, spares, and the 10th-frame bonus rolls, or does it only report pins down per roll? This decides whether the rules live in the pinsetter or in this app.
- Save approval for P1/P2 is still pending; preview to be re-shown with the P2 wording change.
- **Created with user approval ("yes, save them"):** P1 "Score kept for everyone" `6b32273d-580b-4cca-901c-de923419b41e` and P2 "The score settles the rules" `3ea7e223-9f1a-4126-9956-1596d0a8b4b5`; OKR "Bowlers take to the new lanes on their own" `1df92a72-bc88-4c69-9451-34e8cfb2214b`. Chain relations Situation→P1 `f829b0c8-…` and Situation→P2 `88534ca6-…` were read back from the CLI.
- **Gating refused:** `transition problem <id> --state gated` returns "422 Unprocessable Entity" with no detail, for both. Both remain **draft**. Likely cause (agent hypothesis, not confirmed): the server requires every Problem field, and resistance forces and initial KPI are empty. The gated Situation has all four of its fields filled. The CLI uses OAuth, so the raw API error body can't be read.
- Next user contribution: resistance forces (what might make a group hesitate to give up paper), then an initial KPI for each Problem.
- **Resistance forces (user-supplied, hedged):** "can't think of one, but if so, will be because they don't trust it yet." Uncertainty signal, so it's modelled as an assumption: the only expected resistance is not trusting the automatic score until it has proved itself. It applies to both Problems, and most of all to P2, whose whole point is a trusted score. Proposed field text for both: "Expected (assumption, not observed): bowlers may not trust the automatic score until it has proved itself; no other resistance identified."
- Next: an initial KPI per Problem, then preview both field updates and retry gating.
- **User correction:** the agent's "fewer paper sheets" KPI is meaningless once paper is gone. Rejected.
- **P1 initial KPI (user-supplied):** the owner watches the players' moods. Players point at the score on the screen and tease or celebrate; their attention is on the roll, the competition between them, or personal conversation. Observational and qualitative; to be sharpened at the OKR step.
- Next: P2 initial KPI.
- **P2 initial KPI (user-supplied):** the owner hears curiosity instead of disputes, such as "look, it's saving the final score for one more roll!" or "I wonder how it's going to score that 3rd roll?" The group reads the screen to learn the rules.
- **Integration note (user-supplied, for Signal/Solution):** "the pin-setter app will need some attention to decide whether the scoring app tells it about the 10th frame rules, or the pin-setter app stays dumb and a bowler just rolls one more (4th) roll to close the frame for the pin-setter." Two candidate designs:
  - (a) The scoring app tells the pinsetter about the 10th-frame rules, so the pinsetter knows when the frame ends.
  - (b) The pinsetter stays rules-unaware, and a bowler throws one extra (4th) roll so the pinsetter closes its frame.
  These are candidate Options for step 5. Together with the "10 or strike" question, they depend on a Signal: what the pinsetter knows and reports.
- Next: preview the field updates (resistance forces and initial KPI on both Problems), then retry gating.
- **Framing (user):** "we are creating a small system of 2 apps, not just the one app." There is architecture work ahead to adjust both apps' capabilities so they work well together.
  - In the Intent Map: model the pinsetter app as an External Resource, readiness **partial** (it exists but needs changes), with a resource-dependency from the relevant Signal and Solution. To be proposed at the Signal step.
  - Steps 5–7: Options and the Solution compare two-app designs (where the scoring rules live, how the 10th frame closes, what the pinsetter reports), not one app alone.
  - After step 9: the responsibility split between the two apps is architecture work, outside Intent Map. It ties back to prior failure F1 (responsibilities put in the wrong app) and the open question of where frame scoring lives.
- Field-update approval (resistance forces and KPI on P1/P2) is still pending.
- Fields added with user approval ("yes, add them and retry"). Gating then **succeeded** for both, which confirms the hypothesis: the server requires every Problem field before a Problem can be gated. Read back: P1 and P2 are both `gated` with no empty fields.
- **Step 2 closed.**

### Step 3 — OKR
- User asked for help. Their picture of launch, user-supplied: day 1, people ask how to use the tablet app; some make mistakes and need to alter or revise names or order; there is confusion about how to use it and whether it's reliable. "This is normal and is probably the reference 'problem' state."
- **Measures (user-supplied):**
  - Success: how many people figure out the app without asking the clerk for help.
  - Damage count: how many people go back to the front desk to ask for help with the app. It should shrink over successive weeks (different people come each day).
  - Setup time: time from sitting down to first roll (start, names, order). It shrinks with repeat visits; first visits take longer and include talk about how to use the app.
- Agent observation (Challenger): these measures track **adoption of the new way**, meaning the switching cost the solution itself introduces. They don't directly measure P1/P2's outcomes (the scorekeeper back in the fun; curiosity instead of rule disputes). They work as guardrail key results next to an outcome key result. The "confusion about reliability" matches the trust assumption in resistance forces. "Mistakes need to alter/revise" implies a Solution requirement (step 7): names and order are easy to correct.
- Agent-drafted OKR, **unclaimed** (one OKR shared by P1 and P2):
  - Objective: bowlers take to the new lanes on their own and spend the game on each other, not on the scoresheet.
  - KR1 (user): front-desk help requests about the app fall week over week, to a target the user has not set.
  - KR2 (user): setup time to first roll falls with repeat visits, target not set.
  - KR3 (from the P1/P2 KPIs): the owner's floor observations show the moods described in P1/P2. Not yet countable.
  - Owner and time horizon not set.
- **KR1 target (user): "about a third on day 1, almost none by week 4."** Tell (approval instead of answer, mild): the user's numbers repeat the agent's example word for word. Accepted as the user's call, flagged so it can be revisited once launch data exists.
- Next: KR2 setup-time target.
- **User: "you are asking about things I can't even guess at, so I'm just going along with the flow here."** Agent overreached by asking for numeric targets before any baseline exists. This also means KR1's "a third / almost none" was going along, not a judgment: it's downgraded to a placeholder.
- Reframe (agent, **unclaimed**): use measure-then-target key results. Day 1 sets the baseline, and progress means the direction holds week over week. That is falsifiable without guessed numbers, and targets get set after week 1 from real data.
- Proposed OKR, **unclaimed**:
  - Objective: Bowlers take to the new lanes on their own and spend the game on each other, not on the score.
  - KR1: front-desk help requests about the app are counted from day 1 and fall every week through week 4.
  - KR2: setup time (sit down → first roll) is sampled on day 1 and is shorter for returning groups than for first-timers.
  - KR3: on each walk-around, the owner notes how many lanes show the P1/P2 moods (pointing at the screen, teasing, curious about the scoring) rather than huddling over it, and that share rises through week 4.
  - Owner: the alley owner. Time horizon: the first 4 weeks after launch (from the user's "by week 4"). Target KPI: front-desk help requests about the app per day.
- **KR3 refined (user-supplied design):** on walk-arounds the manager keeps a two-mark tally per lane group. A **positive mark** goes to people oblivious to the scoring app, just having fun ("which is what we want"). A **negative mark** goes to a group staring at the app and either arguing with each other or confused by the app. Direction: positive marks rise and level off over time; negative marks fall to very small numbers per night.
- Agent reconciliation, **unclaimed**: P2's KPI (a quick glance, curiosity such as "how's it going to score that 3rd roll?") counts as a **positive** mark. Only staring combined with arguing or confusion counts as negative. Without this, P2's success would be counted as failure.
- Revised KR3, **unclaimed**: "On each walk-around the manager marks each lane group + (having fun, the app in the background, glancing or curious) or − (staring at the app while arguing or confused). Per night, + marks rise and level off, and − marks fall toward a handful, through week 4."
- **OKR saved with user approval ("save it").** Created `1df92a72-bc88-4c69-9451-34e8cfb2214b`, linked P1→OKR `82a49601-…` and P2→OKR `af8790a0-…`, gated, and read back with no empty fields. KR3 is stored in the user's two-mark design, with curious glances counting as +.
- **Step 3 closed.**

### Step 4 — Signal
- Agent's first Signal question was too vague. The user asked "what do you want me to answer, exactly?" Agent narrowed it to: real pinsetter, or ours to design?
- **Pinsetter facts (user-supplied):** real, and upgradable. Today it only knows 2 rolls per frame. After the 1st roll it picks up the pins to count how many were knocked over, sweeps the lane, and sets the remainder back down. After the 2nd roll it clears everything and sets a new ten. It does not know the scoring rules or the 10th-frame 3rd roll.
- **User design leaning (premature solution, harmless; parked for steps 5–7):** "we'll want the scoring app to tell the bowler to make a final roll for free to clear the frame." This is design (b) from earlier: a rules-unaware pinsetter, with the scoring app owning the rules and prompting a free clearing roll. Step 5 must still lay out at least one real alternative (for example, upgrading the pinsetter to know the 10th frame) so that choosing (b) is a real choice.
- Open, and decisive for the Signal: what does the pinsetter do after a **strike** in frames 1–9? Does it reset a new ten right away, or wait for a 2nd roll? If it waits, a strike needs a clearing roll in every frame, not just the 10th.
- **Strike behaviour (user-supplied):** "if all 10 are down, it resets to 1st roll, part of its program." So the pinsetter does recognise a strike in the mechanical sense (10 down → new rack). In frames 1–9 no clearing roll is needed.
- Agent analysis, **unclaimed**, of when a clearing roll is needed in the 10th frame, given this behaviour:
  - Open frame (two rolls, fewer than 10 pins): the pinsetter closes normally. No clearing roll.
  - Strike, then strike, then a 3rd roll that isn't a strike: the pinsetter is left mid-frame. A clearing roll is needed.
  - Strike, then a non-strike, then a 3rd roll: the 2nd and 3rd rolls form the pinsetter's own 2-roll frame. No clearing roll.
  - Spare, then a bonus roll that isn't a strike: the pinsetter is left mid-frame. A clearing roll is needed.
  - Any 3rd roll that is a strike: the pinsetter resets. No clearing roll.
  So the free clearing roll applies only to some 10th-frame endings, and only the scoring app can tell which.
- Next: does the pinsetter send any data out today, or only show it on its dashboard?
- **Session paused by user, 2026-10-20.** Resume with `/intent-map resume Bowling Lane Scoring` from `~/Desktop/OMNI/bowling-lane-scoring`. Graph state at pause, read back: Situation, P1, P2, and OKR all gated; no Signal created yet.
- User at pause: "that table contains some errors, we'll need to fix it up when I come back." The 10th-frame table is marked **disputed**. Review it first on resume. Agent note for that review: the "any 3rd roll that's a strike" row is badly worded for the strike, non-strike case, where roll 3 can only make a spare, not a strike. The user may have other errors in mind.
- **Resumed 2026-11-03.** User corrected the 10th-frame table. Corrected table (the pinsetter resets on a strike, counts any other pair of rolls as a frame, and clears after its 2nd roll):

  | 10th-frame rolls | Pinsetter left stuck mid-frame? | Free clearing roll? |
  |---|---|---|
  | Open frame (two rolls, under 10 pins) | No | No |
  | Strike, strike, non-strike | Yes | **Yes** |
  | Strike, strike, strike | No (resets) | No |
  | Strike, then any two non-strike rolls (for example strike, 3, 4, with 3 pins left; or strike, 3, 7 spare) | No (the 2nd and 3rd rolls are its own 2-roll frame) | No |
  | Spare, then a non-strike bonus roll | Yes | **Yes** |
  | Spare, then a strike | No (resets) | No |

  The clearing roll applies only to strike-strike-non-strike and spare-then-non-strike. The user's example strike, 3, 4 was first read as stuck; on checking the pinsetter's rules the user confirmed it finishes cleanly.
- **Scope clarification (user), 2026-11-03:** the scoring app, where bowlers enter names and bowling order, shows all the rolls and scores. The display at the end of the lane (where the pins are) is **out of scope** of this discussion. So Signal S1's source is the pinsetter app's own count, not its dashboard; the dashboard question is dropped. Still open: whether the pinsetter app can send its per-roll count to another program today, or whether that is new work.
- **Pinsetter count and override (user, 2026-11-03):** the agent's "pinsetter miscounts / bowler corrects on the tablet" fallback was the agent's invention (no observed failure) and is withdrawn. The user checked the bowling rules: when a roll is wrong, the **main desk** fixes it and the bowler continues with the corrected score. So the pinsetter app has a **manual override after a roll**, which can change the pins down and the roll's meaning, for example a strike that did not register and is fixed to a strike, or a non-strike reported as a strike with 1 pin still up. Implications, unclaimed by the user: (1) the pinsetter's count is the source of truth; (2) the scoring app may later need to accept a **correction** to an earlier roll and re-score; (3) the pinsetter and scoring app must not disagree on roll number after an override. **Deferral:** the user suspects this can wait until later and asked for the agent's view. Agent's view: defer it from the first Signal, with one cost-free guard (see below). Open until the user decides.

### Step 4 close
- User accepted the Signal draft ("is good"; the draft was built from the user's own words, so the approval-instead-of-answer tell is harmless). Created with user approval ("sure go ahead"): Signal `3f015676-…` (gated), External Resource "Pinsetter app" `f09e0144-…` (readiness `partial`), chain relation OKR→Signal `a64a3f72-…`, resource-dependency Signal→Pinsetter app `e6ce1397-…`. All read back from the CLI.
- Agent error, fixed: a retry loop created a duplicate "Pinsetter app" resource (type `api`); the duplicate `92aa4f13-…` had no relations and was deleted. The kept resource has type `service`.
- **Open (assumption, unclaimed):** fallback if the pin count does not arrive. **Deferred (user agreed):** main-desk corrections; the scoring design must be able to re-score a corrected roll later.
- **Step 4 closed.**
- **Fallback settled (user, 2026-11-03):** if the pin count does not arrive, the players go to the main desk and all play on that lane stops until it is fixed. Signal reliability field updated and read back (still gated). No unclaimed markers remain.
- **Pinsetter knows no frames (user, 2026-11-03):** "pinsetter knows nothing about what frame they are on (e.g. it can't know how many players are playing). Only the scoring app knows." This settles the carried-over question of where frame scoring lives: **in the scoring app**. Consequence for step 5: the pinsetter can only ever count its own 2-roll cycles, so any design where it clears the 10th frame needs the scoring app to tell it.

### Step 5 — Option
- **User preference (2026-11-03):** option A, "the scoring app tells the bowler to roll one more ball to clear the lane". Recorded as the user's leaning only; the winner is chosen at step 6 (Evaluation) against real alternatives.
- Agent-drafted alternatives, **unclaimed**:
  - **A (user):** free clearing roll. Pinsetter unchanged beyond reporting each roll's pins and the reset. The scoring app asks the bowler for one extra ball in the two stuck endings (strike-strike-non-strike; spare then a non-strike bonus roll).
  - **B:** the scoring app sends the pinsetter the 10th-frame rules, so it clears by itself. Needs the pinsetter to receive instructions, as it knows no frames.
  - **C:** the scoring app sends the pinsetter only a "clear the lane now" command after the last roll; no rules sent. Smaller than B, still needs the pinsetter to receive a command.
- Next: user to say whether B and C are real alternatives or to supply others; then preview and create.
- **User ruling (2026-11-03):** **B is rejected** ("the pinsetter stays dumb": no 10th-frame rules in the pinsetter). **C is a real alternative but costs more to implement than A.** A remains the user's choice "for now". Options to create: A and C. B is recorded here as rejected, not put in the graph. Note: C still needs the pinsetter to receive a "clear now" command, which conflicts less with "stays dumb" than B but is still new inbound work.
- Next: preview Options A and C and get approval to create.
- **Step 5 closed.** User: "keep C if you like, just that it's a deferred feature". Created, linked from the Signal by chain relations, gated, and read back: Option "Free clearing roll" `45ef9b12-96e8-40ff-9282-c2eb192cb59f` (user's choice for now) and Option "Clear-now command (deferred feature)" `43ae809b-c6d6-4789-804f-fc494098dc95`. B stays recorded here as rejected and is not in the graph.

### Step 6 — Evaluation
- **Pinsetter fact (user, 2026-11-03):** if the clearing ball hits nothing, the pinsetter still knows and resets, so a zero-pin clearing roll is not a problem. The pinsetter clears after its 2nd roll whatever the pin count. This removes "a clearing roll that knocks nothing down fails" as a risk to Option A.
- Consequence for the scoring design (agent, unclaimed): the scoring app must ignore the pin count of the clearing roll when scoring, since it asked for that ball itself.
- Still owed by the user: what would make Option A fail (dealbreaker) and what must be true for it to work (riskiest assumption).
- **Refusal case (user, 2026-11-03):** if bowlers refuse to throw the clearing ball, "the app can't know, time just passes." The lane stays mid-frame until someone throws or the desk steps in. Candidate **riskiest assumption** (agent, unclaimed): bowlers will throw the clearing ball when asked. Not yet decided whether this is a dealbreaker or an accepted annoyance.
- Draft Evaluation so far (agent, **unclaimed**): winner Option A, because B is out (user: the pinsetter stays dumb) and C costs more for the same result; criteria and dealbreaker still owed by the user.
- **Stuck lane is not a failure (user, 2026-11-03):** "an event outside our system that our system knows nothing about - time just passes and neither the pinsetter nor the scoring app have a concept of time." So refusal is not a dealbreaker for Option A, and no timeout or timer belongs in either app. Dealbreaker so far (user-supplied): any option that puts rules in the pinsetter (rejects B).
- **Criterion 3 withdrawn (2026-11-03):** the agent's "bowlers don't throw a ball that scores nothing" was badly worded (gutter balls are ordinary) and was the agent's concern, not the user's. Ranked criteria now: (1) the pinsetter stays free of rules (user); (2) least new work on the pinsetter. Open: whether the extra ball outside the sport's rules is a cost the user cares about at all.
- **Criterion 3 dropped for good (user, 2026-11-03):** the extra ball outside the rules "doesn't bother me at all". Ranked criteria are final as two: (1) the pinsetter stays free of rules; (2) least new work on the pinsetter. Still owed: the user's confirmation of the riskiest assumption.
- **Momentum (user, 2026-11-03):** the user felt the agent kept asking repeated questions and asked what the agent could do to progress. Agent change of approach: fill gaps with labelled assumptions and ask for one accept/correct pass instead of one question per turn.
- **Step 6 drafted:** Evaluation `5d68900a-bd65-47ab-8095-b8b3245ff037` created as a draft (not gated until step 8), with chain relations from both Options. The riskiest assumption (pinsetter clears after its 2nd roll in the stuck endings, including a zero-pin ball) is agent-proposed and flagged as such in the entity; the user has not confirmed it.

### Step 7 — Solution (draft, **unclaimed**, not yet in the graph)
Presented to the user 2026-11-03; session saved before the user replied.
- **Flow:** (1) group walks to the lane, scoring app is running or they start it (user); (2) they enter names in bowling order, which starts the game (user); (3) after each roll the pinsetter reports pins down and whether it reset; the app scores the frame and shows whose turn is next (user); (4) in the two stuck 10th-frame endings the app tells the bowler to throw one more ball to clear the lane, and ignores that ball's pins when scoring (user chose option A; the ignoring is the agent's design note); (5) if the pin count does not arrive or a roll is wrong, players go to the main desk and play waits (user).
- **First release (user):** names and order, who bowls next, score kept after every frame, strikes and 10th-frame rolls handled.
- **Later release (user):** announce the next bowler by voice; celebrate a strike.
- **Deferred (user):** main-desk corrections (the design must be able to re-score a corrected roll); clear-now command.
- **Appetite (agent, not user):** small: one new scoring app plus a modest pinsetter upgrade to report each roll.
- **No-gos (user):** no rules in the pinsetter; no timers in either app; no login, lane assignment, or payment.
- **Rabbit holes (agent):** re-scoring after a desk correction; the display at the end of the lane (out of scope per the user).
- **Tablet vs phones:** whether "their app" runs on the lane console or on bowlers' phones is still open (carried from step 1); the user said tablet-style earlier.
- **Resumed 2026-11-09** from omni-guide, after repository setup (binding now `bowling-lane-scoring-w-omni`). The guide run stays in `pre_repo`: its move into project scope is blocked, because no supported command advances the phase, and will be retried after an omni-ee update. The Solution draft was re-presented for the user's yes or changes.
- **Appetite settled (agent-proposed, user accepted "yes", 2026-11-09):** small, meaning one new scoring app at the lane plus one pinsetter change (report pins down and reset after every roll). Give-way order: (1) above all, a correct score after every frame, including strikes and the 10th frame; (2) try to keep showing who bowls next; (3) give up first: polish (name entry, how the score looks). Tablet vs phones goes to step 8 as the first challenge.
- **Solution created 2026-11-09 (user "yes" to the preview):** draft `e7ad4fa7-b267-4623-8a7e-67c132c71547`, chained from the Evaluation and read back from the CLI. The rabbit holes were agent-proposed and are now claimed through that yes.
- **Step 8 opened:** first challenge is tablet vs phones.
- **Challenge 1 settled (user, 2026-11-09): lane tablet.** Agent recommended it (serves both bowlers' and owner's stakes; phones would add a join-phone-to-lane rabbit hole). Solution UI notes updated and read back. Closes the open question carried from step 1.
- **Challenge 2 settled (agent-proposed, user accepted "good proposal, yes use it", 2026-11-09):** riskiest assumption is now that the pinsetter app can be changed cheaply to send pins down and the reset to the lane tablet after every roll. Cheapest test: whoever looks after the pinsetter app shows one roll's pin count and a reset arriving on another device before any scoring is built. The old assumption (clears after 2nd roll on a zero-pin ball) was retired because the user stated it as fact in step 6. Evaluation updated and read back.
- **Signal gap found (user, 2026-11-09):** the user asked what the pinsetter sends for a 3 then a 3. Per the gated Signal, both messages would be "3, no reset": identical, so the tablet could not tell the pinsetter cleared after its 2nd roll, and the two apps could drift after an override or in the stuck 10th-frame endings. Gating held; step 4 reopened.
- **Message format settled (user, 2026-11-09):** the pinsetter sends which of its two rolls it was and the total pins down so far in that roll pair, e.g. "1st roll, 3" then "2nd roll, 6". The tablet derives the 2nd ball as 6 − 3.
- **"Resetting" dropped (agent-proposed, user accepted "yes", 2026-11-09):** reset is implied by the pinsetter's own rules (always after a 2nd roll; after a 1st roll of 10). Cost: a pinsetter jam goes unreported, which the desk fallback already covers.
- **Assumption (user said "I suspect"):** the pinsetter knows the pins left standing at its 2nd check. Folded into the cheapest test: the demo must show both "1st roll, 3" and "2nd roll, 6" arriving on another device.
- **Revision applied (user approved the preview, "good", 2026-11-09):** Signal retitled "Roll number and pins down after each roll" with new what-must-know, minimum version, prerequisites and reliability (assumption added). Evaluation winner rationale, riskiest assumption and cheapest test, and Solution flow step 3 and appetite, now say "roll number and pins down so far". All three read back from the CLI: Signal still gated; Evaluation and Solution draft.

### Step 8 close
- **Evaluation and Solution gated (user: "yes please 'gate them'", 2026-11-09)** after the agent explained gating in plain words (the user had asked what it meant). Challenger outcomes: tablet chosen over phones; riskiest assumption replaced; the Signal sync gap (found by the user) fixed; misleading count, refused clearing ball, extra ball outside the rules, and deferred desk corrections were each already handled in the map. Surviving assumptions, each with a test: the pinsetter app can be changed cheaply to send roll number and pins down so far; the pinsetter knows the pins left standing at its 2nd check. Both are covered by one demo.

### Step 9 — Close
- Read back from the CLI on 2026-11-09. Gated: Situation; Problems P1 and P2; OKR; Signal "Roll number and pins down after each roll"; Options "Free clearing roll" and "Clear-now command (deferred feature)"; Evaluation; Solution. External Resource "Pinsetter app" (service, owner alley, readiness partial).
- Relations read back: chain Situation→P1, Situation→P2, P1→OKR, P2→OKR, OKR→Signal, Signal→both Options, both Options→Evaluation, Evaluation→Solution; resource-dependency Signal→Pinsetter app. These match what the user approved.
- No unclaimed content remains open. Learning-loop trigger: when the pinsetter demo runs, update the Evaluation with its result.
- Transcript exported to `bowling-transcript-20261109.md`. The user asked for periodic reminders to re-sync it.

- **Solution renamed (user, 2026-11-09, during goal writing):** from "Lane scoring app with a free clearing roll" to "Lane tablet keeps score for the group". The user pointed out the clearing roll is a 10th-frame detail, not the headline. Only the title changed; the entity is still gated (read back).


## OMNI guide bookmark: park and restore (set up 2026-11-09)
The OMNI guide keeps one bookmark per Mac at `/Users/alistaircockburn/.omni-ee/guide-state.json`. It could not yet be moved into this project. Until it can, the user swaps it between projects by hand:
- **"park the guide"** (end of session): copy it to `.omni-ee/guide-state-parked-YYYYMMDD.json` in this folder, check the copy, then delete the original. Never touch the `.lock` files.
- **"restore the guide"** (start of session): check the common place is empty, then **copy** the newest parked file back to `~/.omni-ee/guide-state.json`. The parked file stays.

Log of parks and restores:
- **2026-11-09, parked** at the end of the session: run `guide-run-6138fc610d01f46f38cdd473c5fadb51` (phase pre_repo) copied to `.omni-ee/guide-state-parked-20261109.json`. The sha256 `c0079999…a4523af7b` matched the original, which was then deleted from `~/.omni-ee`. Lock files untouched.

## How to resume
Run `/intent-map resume Bowling Lane Scoring` from `~/Desktop/OMNI/bowling-lane-scoring`. The project is `9734b3f5-3e03-4ca6-8601-d315526caaf0`. The CLI can be slow: use a 100-second timeout and check with `intent-map relation list <id>` before retrying a write, so nothing gets duplicated.

