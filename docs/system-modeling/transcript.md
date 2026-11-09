# System Modeling — Living Transcript

Synthesis of what settled, moved, was rejected, and remains open, with attribution. Not a turn-by-turn log.

## Status

- **Methodology source:** system-modeling skill, omni v0.9.0 (commit 566b8f52)
- **Run state:** ABANDONED (human decision, step 2)
- **Current step:** 2 — Problem definition
- **Model path:** _not yet drafted (step 9)_
- **Transcript path:** docs/system-modeling/transcript.md
- **Phase references read completely:** SKILL.md, orientation.md, problem-steps.md
- **Settled problem:** _none_
- **Settled beneficiary:** _none_
- **Open questions:** (a) was F1's lane boundary stated in the input or only intended? (input unavailable); (b) are F1 and F2 one structure or two?
- **Tells / red flags fired:** _none_
- **Binding-ordering crossings or waivers:** _none_
- **Next required human contribution:** none — run ended; work continues in goal-writing
- **Context:** side quest from omni-guide run `guide-run-6138fc61…`; return route = audited `omni start`, then goal document (specs/vision.md).

## Log

### Step 0 — Contract
- Human chose `learn`, received orientation, then accepted with `p`. Run moved PENDING → ACTIVE.
- Agent noted up front: step 14 requires an independent reviewer; if unavailable, the run stops at step 14 rather than self-certifying.

### Step 1 — Failure evidence
- **F1 (human-supplied, testimony):** In a previous build of a bowling alley app, agents implemented the "new bowler logging in" part so that it also assigned lanes and took payment — responsibilities that are not its job. Human's framing: "a failure in the agentic decoding of work."
- F1 detail (human-supplied): human believed the instructions clearly said only the main bowling alley app assigns lanes. Found only when running the apps, after the build, and it was a surprise. *Unverified:* whether the input actually stated that boundary. Named falsifier: read the original input.
- Falsifier cannot run: the original input is no longer available (human-supplied). Carried forward as an open question: was the lane-assignment boundary stated in the input, or only intended?
- Open (agent): F1 cost not yet known.
- Agent facilitation correction (human): ask one question at a time.
- **F2 (human-supplied, testimony; humans, not agents):** The business sponsor, integration engineer, and tech lead each said they would enforce hexagonal architecture in the small system slices being integrated and deployed. Under time pressure none of them did, and hexagonal architecture was dropped after a few sprints.
- Agent observation, **unclaimed** and not a problem statement: in both F1 and F2 an architectural boundary that people believed was established did not hold once work was actually done. In F1 the work crossed it; in F2 nobody held it. Whether that's one structure or two is for later steps.
- Open (agent): subject ambiguity — the failure could belong to the bowling app or to how agents decode work. Not resolved here; it's a step-2 choice for the human.
- Step 1 closed by human with F1 and F2 (two independent failures: one from agents, one from humans).

### Step 2 — Problem definition
- Agent offered three candidate subjects (A: bowling app, B: agent instruction decoding, C: boundaries that don't hold). Human rejected all three: "something else."
- **Subject scope chosen (human):** a subset of the bowling alley system, with exactly two apps:
  - **Lane-head app:** used by bowlers at the head of the lane; they enter their names and it shows the scores.
  - **Pinsetter app ("pin-picker"):** picks up pins after each roll; knows about 1st and 2nd rolls; tells the lane-head app the score of each roll.
- Parked by implication (to confirm): login, lane assignment, payment, the main bowling alley app, and F2's architecture enforcement.
- Agent note for step 3: "score of each roll" is a load-bearing noun to define (pins knocked down, or frame score?). Not raised yet.
- Open (agent): a scope is chosen but not yet a *problem* within it. F1's failure (work placed in the wrong app) lies outside this pair.
- Human: no failure in mind for the two-app scope — "i just want the apps." Agent: the method needs a failure to close step 2; offered (1) abandon and go to goal-writing, or (2) keep F1's pattern as the problem.
- **Human reframe (build objective, not a failure):** an existing small pinsetter app already picks up pins, tracks 1st and 2nd roll, and shows pins knocked down on a dashboard at the bottom of the lane. Wanted: (1) a new app for bowlers (enter names, see scores), and (2) upgrade the pinsetter app to integrate with it.
- Agent assessment: this is a brownfield delivery goal, which goal-writing handles, not system modeling. Awaiting the human's decision on ending the run.
- **Run ended ABANDONED by human at step 2** ("yes, let's go to goal writing").
  - Unmet outputs: no settled problem or beneficiary; no problem statement (step 3); no system model; no independent review. Later work must not claim the guarantees of a completed system-modeling run.
  - Carried forward to goal-writing: F1 as the reason to make ownership between the two apps explicit; open question about where frame scoring lives (bowler app vs pinsetter).
