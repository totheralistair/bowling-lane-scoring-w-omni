# Conversation Transcript

Session `27d9cf84-87b9-412a-b481-ac21d1c722ae` · last updated 2026-11-12 19:38 UTC

### User · 18:09

omni guide

### Claude · 18:09

> _tool: Bash — Read pairing mode contract_

### Claude · 18:09

> _tool: Bash — Check guardrails and read agent tools doc_

### Claude · 18:09

> _tool: Bash — Read collaboration letter and guide-state memory_

### Claude · 18:09

> _tool: Skill — omni-guide_

### User · 18:09

_[skill loaded: omni-guide]_

### Claude · 18:09

> _tool: Bash — Read how I should work_

### Claude · 18:10

Picking up your bowling project where we stopped.

### Claude · 18:10

> _tool: Read — /Users/alistaircockburn/.claude/projects/-Users-alistaircockburn-Desktop-OMNI-bowling-lane-scoring/27d9cf84-87b9-412a-b481-ac21d1c722ae/tool-results/b4jmrlgcy.txt_

### Claude · 18:10

> _tool: Bash — Check where we stopped_

### Claude · 18:10

> _tool: Bash — Look up where your project stands_

### Claude · 18:10

> _tool: Bash — Look for your notes from last time_

### Claude · 18:10

> _tool: Bash — Read the end of your project notes_

### Claude · 18:10

> _tool: Bash — Read the rest of today's readiness check_

### Claude · 18:10

> _tool: Bash — Save where we stopped_

### Claude · 18:10

> _tool: Bash — Check how saving where we stopped works_

### Claude · 18:10

> _tool: Bash — Save where we stopped_

### Claude · 18:10

Where Bowling Lane Scoring stands.

Settled with you:
- Starting point: Bowlers arrive at a lane that only scores on paper
- Problems: The score settles the rules; Score kept for everyone
- Goal: Bowlers take to the new lanes on their own
- Sign it's working: Roll number and pins down after each roll
- Ways to do it: Clear-now command (deferred feature); Free clearing roll
- Comparison: Free clearing roll beats rules in the pinsetter
- Chosen way: Lane tablet keeps score for the group

Your map: https://app.omni3.ai/intent-map/9734b3f5-3e03-4ca6-8601-d315526caaf0

Today's check found the plan isn't ready for the agents yet: there's no Goal document, and nine questions about the trial are still open (the first is what happens when balls keep rolling after the 10th frame).

We'll write the Goal document: it sets down the outcome you've decided, in a form the agents can build from. We start with those nine questions, one at a time. Shall we start there?

◆ OMNI · Goal document · next: start on the nine open trial questions?

### User · 18:14

i'm working on the use case still.... here's where I am



<pasted_content id="04d7">
3rd Try: 

Precondition: At the beginning of the day and after every group pays, the manager uses the Lanes Manager App (LM app) to reset the ScoreKeeper app (the Tablet) to a blank and empty game, with the instruction to “Enter Players”. When a new group arrives, the Tablet shows this reset state.
1. Bowler enters the group's names in bowling order and starts the game. 
2. The Tablet always indicates whose turn it is and which roll it it. 
3. After each roll, the Pinsetter sends roll number (1st or 2nd) and number of pins currently down. 
    The Tablet updates the score in that bowler's frame according to the rules of bowling. 
    Tablet indicates who the next bowler is and which roll it will be (including the 
     possible 3rd roll in the 10th frame).
4. Group repeats step 5 until every bowler has finished the 10th frame.
5. Bowlers choose whether to start a new game, or go and pay for the games they bowled.
6. When the Group pays at the main desk for the games they played, the manager has the LM app reset the Tablet for the next group.
    (separate use case, showing dialog of # games to charge, followed by the reset)

*a. Any bowler can change the names and bowling sequence at any time. This may produce the situation that someone who hasn’t bowled in this frame is above someone who has. 
    The Tablet calls for the appropriate next person to bowl. (Bold, text, voice, whatever)
3a. A 3rd roll in 10th frame leaves 2nd roll dangling (eg XX3, or 5/2, although X34 is not a problem): 
    Tablet asks the bowler to bowl one more roll just to clear the pinsetter.
3b. Pinsetter reports incorrect number of pins down:
    … procedure involving front desk
4a. Bowlers keep rolling balls after the 10th frame:
    ??? What’s the rule?

Paste/update from the original use case the case of the 10th frame and any other conditions we need to handle
</pasted_content id="04d7">

### Claude · 18:14

> _tool: Bash — Read your use case drafts_

### Claude · 18:15

> _tool: Write — /Users/alistaircockburn/Desktop/OMNI/bowling-lane-scoring/docs/goal/use-case-play-a-game-cut4.md_

### Claude · 18:15

> _tool: Bash — Note today's use case work in your project notes_

### Claude · 18:15

I've merged your 3rd Try with the extensions from your first cut. Here it is: /Users/alistaircockburn/Desktop/OMNI/bowling-lane-scoring/docs/goal/use-case-play-a-game-cut4.md

Your own text is unchanged. Each line I added is marked as either from cut 1 or my guess. I left out Start Over, Next Game and the old group's scores (my guess), because the manager's reset now does that job.

Here is the 10th-frame piece:

> **3a.** A 3rd roll in 10th frame leaves 2nd roll dangling (eg XX3, or 5/2, although X34 is not a problem): Tablet asks the bowler to bowl one more roll just to clear the pinsetter. Tablet ignores that ball's pins. *(agreed yesterday, not yet in your text)*
> **3a1.** Bowler won't throw the clearing ball: the lane stays mid-frame; time passes (neither app has a sense of time); the desk can step in. *(from cut 1)*

Is the 10th-frame piece right as it stands?

◆ OMNI · your use case · 10th frame · next: is the 10th-frame piece right?

### User · 18:20

sorry that's not the way i want to work - please just print here the extenions for extension 4a

### Claude · 18:20

Here are the possible ways to handle 4a, written as extensions. All the wording is mine.

**Option (a): the Tablet ignores them**
4a. Bowlers keep rolling balls after the 10th frame:
  4a1. Tablet ignores rolls when no game is on.
  4a2. If a new game starts while the pinsetter is mid-rack, Tablet asks the first bowler for one ball to clear the pinsetter, and ignores that ball's pins.

**Option (b): a roll starts a new game**
4a. Bowlers keep rolling balls after the 10th frame:
  4a1. Tablet starts a new game automatically with the same names and order. That game is counted and charged.

**Option (c): as (a), plus a message**
4a. Bowlers keep rolling balls after the 10th frame:
  4a1. Tablet ignores the rolls and shows "Game over: press New Game".
  4a2. As (a) 4a2.

Yesterday I leaned towards (a) or (c).

◆ OMNI · your use case · 4a · next: your pick for 4a

### User · 18:23

i chose option b and wrote it in my copy of the use case
what's the next extension my version doesn't yet handle

### Claude · 18:23

> _tool: Bash — Note your 4a choice in your project notes_

### Claude · 18:23

The next one is what happens when the bowler won't throw the clearing ball. Your first cut had it:

3a1. Bowler won't throw the clearing ball:
  3a1a. The lane stays mid-frame. Time passes, since neither app has a sense of time. The desk can step in.

◆ OMNI · your use case · 3a1 · next: 3a1 in your copy, then the next extension

### User · 18:25

I wrote this: 



<pasted_content id="04d7">
3a. A 3rd roll in 10th frame leaves 2nd roll dangling (eg XX3, or 5/2, although X34 is not a problem): 
    Tablet asks the bowler to bowl one more roll just to clear the pinsetter.
    it ignores the number the pinsetter sends.
</pasted_content id="04d7">

### Claude · 18:25

Got it. 3a now says the Tablet ignores the clearing ball's count.

One thing to watch: under your 4a, a roll after the 10th frame starts a new game. If the last bowler's 10th frame ends dangling, their clearing ball is the last roll of the game. Your 3a already covers it, because the Tablet asked for that ball, but 4a's wording should make clear that a clearing ball doesn't count as a roll after the game.

Your 3b still says "… procedure involving front desk". Your first cut had this procedure:

3b. Pinsetter reports incorrect number of pins down:
  3b1. Bowler goes to the main desk before the next ball is thrown.
  3b2. Desk staff fix the count in the pinsetter app's override.
  3b3. Trial: the Tablet is not told; the wrong count stands.
  3b4. Later: the Pinsetter sends "change roll score" for that roll; the Tablet re-scores.
3b1a. The next ball has already been thrown: the count stands.

◆ OMNI · your use case · 3b · next: 3b in your copy, then the next extension

### User · 18:27

3a. A 3rd roll in 10th frame leaves 2nd roll dangling (eg XX3, or 5/2, although X34 is not a problem): 
    Tablet asks the bowler to bowl one more roll just to clear the pinsetter.
    it ignores the number the pinsetter sends.

4a. Bowlers keep rolling balls after the final bowler’s 10th frame (game technically over):
    Tablet starts a new game automatically with the same names and order. 
    The completed game is counted and charged.


i think this covers it, no?

### Claude · 18:27

Almost. One gap is left. The last bowler's clearing ball from 3a comes after their 10th frame has ended. As 4a is worded, the Tablet would treat that ball as a roll after the game and start a new game.

A possible fix (my wording):

4a. Bowlers keep rolling balls after the final bowler's 10th frame **and any clearing roll from 3a** (game technically over): …

Does that wording fix it for you?

◆ OMNI · your use case · 4a · next: does the clearing-roll wording fix 4a?

### User · 18:29

4a. Bowlers keep rolling balls after the final bowler’s 10th frame (including any last clearing roll), when the game is technically over:4a. 

i think that does it?

### Claude · 18:29

Yes, that does it. The clearing roll is now part of the 10th frame, so only rolls after it start a new game. Your paste has an extra "4a." at the end, in case that's in your copy too.

◆ OMNI · your use case · 4a settled · next: 3b, the wrong pin count, when you want it

### User · 18:30

yes, what's the extension for that?

### Claude · 18:30

> _tool: Bash — Note the settled 4a wording in your project notes_

### Claude · 18:30

This is the extension from your first cut, in today's numbering:

3b. Pinsetter reports incorrect number of pins down:
  3b1. Bowler goes to the main desk before the next ball is thrown.
  3b2. Desk staff fix the count in the pinsetter app's override.
  3b3. Trial: the Tablet is not told; the wrong count stands.
  3b4. Later: the Pinsetter sends "change roll score" for that roll; the Tablet re-scores.

3b1a. The next ball has already been thrown before anyone reaches the desk:
  3b1a1. The count stands.

◆ OMNI · your use case · 3b · next: 3b in your copy, then the next extension

### User · 18:31

good eye

### Claude · 18:31

Thanks.

◆ OMNI · your use case · 3b · next: the next extension, when you want it

### User · 18:37

i wrote this: 



<pasted_content id="04d7">
3b. Pinsetter reports incorrect number of pins down:
    Bowler goes to the main desk.
    Desk staff fix the number in the pinsetter.
    Pinsetter sends “Correct roll score” to the table (roll number, number of pins down).
    Tablet updates the score and bowling continues.
3c. The bowler has already bowled the next ball before the pinsetter got corrected:
    The correction is ignored. (Actually, I don’t think this can happen, but ok).     
</pasted_content id="04d7">

### Claude · 18:37

Noted. One thing changes from before. In your first cut, the trial left the wrong count standing and only a later version had the Tablet re-score. Your new 3b puts "Correct roll score" straight into the use case. That brings back main-desk corrections, which you'd set aside on the map for later.

Small ones: "table" should be "tablet", and 3c reads as a branch of 3b (3b1).

Is "Correct roll score" now part of the trial?

◆ OMNI · your use case · 3b · next: is "Correct roll score" in the trial?

### User · 18:38

yes

### Claude · 18:38

> _tool: Bash — Note the pin-count correction is now in the trial_

### Claude · 18:38

Noted: desk corrections are now in the trial. The Intent Map still lists them under later, so I'll bring that up when we're back on the map.

Add it to the Decision Map too?

◆ OMNI · your use case · 3b settled · next: add the correction decision to the Decision Map?

### User · 18:39

i revised that extension this way: "3c. Case 3b but a bowler has already bowled the next ball before the pinsetter got corrected:"

### Claude · 18:39

Got it. 3c now says it's a branch of 3b.

◆ OMNI · your use case · 3c · next: the next extension, or the Decision Map entry

### User · 18:39

any other extensions or cases to consider on this use case?

### Claude · 18:39

Yes, six more cases to consider:

1. **Pinsetter's message never arrives** (from cut 1): the group goes to the main desk and play waits. Still open: what the desk does to get the lane going again.
2. **A bowler rolls out of turn** (from cut 1): the Tablet credits the roll to whoever it shows as up, since the Pinsetter knows no players. Still open: does that matter in the trial?
3. **A bowler tries to change a pin count on the Tablet** (from cut 1): the Tablet offers no way to do it. This matters more now that the desk can send corrections.
4. **Too few or too many bowlers** (from cut 1, never settled): the smallest and largest group.
5. **A pinsetter message arrives out of order** (open from yesterday): handle it in the trial, or later?
6. **The group leaves without paying** (my guess): no reset happens, so the next group finds the old game on the Tablet.

◆ OMNI · your use case · more cases · next: which of these six to write first

### User · 18:40

i'll note those... what are the extension numbers for them?

### Claude · 18:40

Using your current numbering (*a, 3a, 3b, 3c, 4a):

- ***b.** A bowler tries to change a pin count on the Tablet
- **1a.** Too few or too many bowlers
- **3d.** Pinsetter's message never arrives
- **3e.** A bowler rolls out of turn
- **3f.** A pinsetter message arrives out of order
- **6a.** The group leaves without paying

◆ OMNI · your use case · numbering · next: which case to write first

### User · 18:41

*b can't happen because the tablet has no imput option for that

### Claude · 18:41

Agreed, so *b comes off the list. "The Tablet has no way to enter a pin count" is still a rule worth keeping. I'll carry it to the Goal document as a limit on the Tablet, not as an extension.

◆ OMNI · your use case · more cases · next: which of the five cases to write first

### User · 18:45

i wrote



<pasted_content id="04d7">
1a. Too many bowlers for the lane:     Out of scope.

  3d. Pinsetter's message never arrives: Out of scope (the tablet can’t detect)
</pasted_content id="04d7">

### Claude · 18:45

> _tool: Bash — Note your 1a and 3d in your project notes_

### Claude · 18:45

Noted. Both fit your rule that neither app has a sense of time. 3e, 3f and 6a are still to write.

1a covers too many bowlers. The other end is a game started with no names entered. Should the Tablet let that start?

◆ OMNI · your use case · 1a · next: can a game start with no names?

### User · 18:45

sorry, paste error:

### Claude · 18:45

The paste didn't come through: only "sorry, paste error:" arrived. Could you paste it again?

◆ OMNI · your use case · 1a · next: your corrected paste

### User · 18:45

<pasted_content id="04d7">
Extensions out of scope: 
1a. Too many bowlers for the lane
3d. Pinsetter's message never arrives (the tablet can’t detect)
3e. A bowler rolls out of turn (the tablet can’t detect)
3f. A pinsetter message arrives out of order
6a. The group leaves without paying
</pasted_content id="04d7">

### Claude · 18:45

> _tool: Bash — Note the out-of-scope cases in your project notes_

### Claude · 18:45

Noted. All five are out of scope, which also answers yesterday's question about out-of-order messages.

One case at the small end is still open. Can a game start with no names entered?

◆ OMNI · your use case · 1a · next: can a game start with no names?

### User · 18:45

ooooooo good call, let me think

### Claude · 18:45

Take your time.

◆ OMNI · your use case · step 1 · next: can a game start with no names?

### User · 18:54

oooo lookee: 



<pasted_content id="04d7">
1a. Someone rolls a ball before names have been entered, the pinsetter sends the roll information:
    The Tablet starts the game, calling the bowler “Player 1”
    In case more rolls are done before adding other players, the tablet considers this a 1-person game.
1b. A new player is added part way through the game:
    The Tablet enters them with rolls of zero until they are caught up with the rest of the people.
</pasted_content id="04d7">

### Claude · 18:54

That handles it, and it matches your 4a: a roll always counts for something, whether a game is on or not.

Two numbering notes:
- 1a clashes with "1a. Too many bowlers" in your out-of-scope list. One of them needs a new number.
- 1b can happen at any frame, so it reads more naturally as ***b**, next to *a (changing names and order).

◆ OMNI · your use case · step 1 · next: your next case, or on to the Goal document

### User · 18:58

how's this



<pasted_content id="04d7">
*a. Any bowler can change the names and bowling sequence at any time. 
    This may produce the situation that someone who hasn’t bowled in this frame is above 
    someone who has. The Tablet calls for the appropriate next person to bowl. 
*b. A new player is added part way through the game:
    The Tablet enters them with rolls of zero until they are caught up with the rest of the people.

1a. Someone rolls a ball before names have been entered, the pinsetter sends the roll information:
    The Tablet starts the game, calling the bowler “Player 1”
    In case more rolls are done before adding other players, the tablet considers this a 1-person game.
3a. A 3rd roll in 10th frame leaves 2nd roll dangling (eg X.X.3, or 5./.2, although X.3.4 is not a problem): 
    Tablet asks the bowler to bowl one more roll just to clear the pinsetter.
    it ignores the number the pinsetter sends.
3b. Pinsetter reports incorrect number of pins down:
    Bowler goes to the main desk.
    Desk staff fix the number in the pinsetter.
    Pinsetter sends “Correct roll score” to the tablet (roll number, number of pins down).
    Tablet updates the score and bowling continues.
3c. Case 3b but a bowler has already bowled the next ball before the pinsetter got corrected:
    The correction is ignored. (Actually, I don’t think this can happen, but ok).     
4a. Bowlers keep rolling balls after the final bowler’s 10th frame (including any last clearing roll), when the game is technically over:
    Tablet starts a new game automatically with the same names and order. 
    The completed game is counted and charged.

Extensions out of scope: 
1b. Too many bowlers for the lane
3d. Pinsetter's message never arrives (the tablet can’t detect)
3e. A bowler rolls out of turn (the tablet can’t detect)
3f. A pinsetter message arrives out of order
6a. The group leaves without paying
</pasted_content id="04d7">

### Claude · 18:58

It reads well. Every case says who does what, and the out-of-scope list keeps the edges visible. I found no conflicts between cases. 1a, *b and 4a now follow one pattern: a roll always counts.

One leftover from your earlier paste: step 4 of the main scenario said "repeats step 5". If your copy still says that, it should be step 3.

That closes the extensions. Next is the Goal document, where three questions are still open: who "the manager" is, whether the LM app link is in the trial, and where the trial is proven. This is also a good point to re-sync today's transcript.

◆ OMNI · your use case · extensions done · next: on to the Goal document?

### User · 19:05

ahhhhh i don't see where the tablet keeps count of the games played

### Claude · 19:05

You're right. Step 6 has the LM app show the number of games to charge, and 4a says "counted and charged", but no step does the counting. A possible fix (my wording):

4. Group repeats step 3 until every bowler has finished the 10th frame. **The Tablet adds one to the group's game count.**

The precondition's reset would then also set the count back to zero.

Does a game count when it's finished, or as soon as it starts?

◆ OMNI · your use case · game count · next: does a game count when finished or when started?

### User · 19:05

when it starts, we agreed on that already

### Claude · 19:05

> _tool: Bash — Find what we agreed about counting games_

### Claude · 19:05

Yes, you settled it yesterday: a game starts at its first roll, and every started game is reported, finished or not. I should have checked before asking.

So the count goes at the first roll, not the end. A possible fix (my wording):

3. After each roll, the Pinsetter sends … **When the roll is the first of a game, the Tablet adds one to the group's game count.**

That also covers 1a and 4a, since both start a game with a roll. 4a's "The completed game is counted and charged" then becomes "The new game is counted."

Does that wording work for you?

◆ OMNI · your use case · game count · next: does the first-roll count wording work?

### User · 19:07

2. The Tablet always indicates whose turn it is, which roll it is and how many games are being charged.
     A game is charged the moment the first roll is made. Charges are for games /started/ not games /finished/.

### Claude · 19:07

> _tool: Bash — Note your new step 2 in your project notes_

### Claude · 19:07

That works, and putting the count on the Tablet lets the group see what they'll be charged.

4a now disagrees with it. "The completed game is counted and charged" should become something like "The new game is charged from that roll." The completed game was already charged when it started.

◆ OMNI · your use case · step 2 settled · next: 4a's last line, then the Goal document

### User · 19:09

i delted that offending sentence: 



<pasted_content id="04d7">
4a. Bowlers keep rolling balls after the final bowler’s 10th frame (including any last clearing roll), when the game is technically over:
    Tablet starts a new game automatically with the same names and order.
</pasted_content id="04d7">

### Claude · 19:09

Good. Step 2 already charges the new game at its first roll, so 4a doesn't need to say it. Your extensions look complete to me.

This is a natural stop, so it's a good time to re-sync today's transcript.

Shall we go on to the Goal document?

◆ OMNI · your use case · done · next: on to the Goal document?

### User · 19:09

yes please, append 'b' to the date, tidy up all files, before starting a new task

### Claude · 19:09

> _tool: Bash — List project files and find this session's log_

### Claude · 19:09

> _tool: Bash — Save today's second transcript and read your decision record_

### Claude · 19:10

> _tool: Write — /Users/alistaircockburn/Desktop/OMNI/bowling-lane-scoring/docs/goal/use-case-play-a-game-cut4.md_

### Claude · 19:10

Now the decision record.

### Claude · 19:10

> _tool: Bash — Add today's decisions to your decision record_

### Claude · 19:10

> _tool: Bash — Re-save today's second transcript_

### Claude · 19:10

> _tool: Skill — goal-writing_

### User · 19:10

_[skill loaded: goal-writing]_

### Claude · 19:10

> _tool: Bash — Note where the Goal document picks up_

### Claude · 19:10

I've tidied up. The fourth cut now holds your final text, today's decisions are in the decision record, and today's second transcript is saved as `bowling-transcript-20261112b.md`. Nothing is committed.

On to the Goal document. Seven decisions are still open before I can draft it. Here they are; we'll take them one at a time:
- who "the manager" is
- whether the LM app link is in the trial
- who builds the pinsetter change
- where the trial is proven
- what the tablet runs on
- the trial's must / should / could / won't list
- the wording for the manager's login

First one: a group pays on a busy Saturday night, and someone at the main desk resets their tablet in the LM app. Is that whoever is working the desk, or only the owner or manager?

◆ OMNI · Goal document · step 1 of 4: open decisions · next: who resets the tablet at payment?

### User · 19:11

one at a time: 


<pasted_content id="04d7">
1- who "the manager" is
2- whether the LM app link is in the trial
3- who builds the pinsetter change
4- where the trial is proven
5- what the tablet runs on
6- the trial's must / should / could / won't list
7- the wording for the manager's login
</pasted_content id="04d7">



1 - a person, we shouldn't care.

### Claude · 19:11

> _tool: Bash — Record that the manager is just a role_

### Claude · 19:11

Got it: the manager is just a role. The software doesn't care who it is.

2. At payment in the trial, the LM app could ask the tablet how many games were started and then reset it. Or the desk could ask the group and reset the tablet some other way. Which one does the trial use?

◆ OMNI · Goal document · step 1 of 4: open decisions · next: is the LM app link in the trial?

### User · 19:12

2 - we'll use hexagonal architecture and a test-first sequence, the app can't know what it is connected to, so it will be no problem to have the test setup play the role of the LM App

### Claude · 19:13

> _tool: Bash — Record the LM app link and your build rules_

### Claude · 19:13

Got it: the LM app link is in the trial, and during proof the test setup plays the LM app. I've also recorded hexagonal architecture and test-first as your rules for the agents.

3. The pinsetter app has to change to send "1st roll, 3", "2nd roll, 6" and "Correct roll score". Do the agents build that change in this run, or does whoever looks after the pinsetter app deliver it?

◆ OMNI · Goal document · step 1 of 4: open decisions · next: who builds the pinsetter change?

### User · 19:14

pinsetter software is out of scope of this project. Assume it gets done in time. we'll work from the test harnesses to start with

### Claude · 19:14

> _tool: Bash — Record that the pinsetter change is out of scope_

### Claude · 19:14

Got it: the agents build only the tablet. The pinsetter change comes from someone else, and you're assuming it arrives in time.

4. That mostly settles where the trial is proven. My guess at the rule: in this run, all proof runs against test harnesses standing in for the pinsetter and the LM app, and nothing touches a real lane or the live LM app. Connecting to the real ones is a later step.

Is that the rule?

◆ OMNI · Goal document · step 1 of 4: open decisions · next: harnesses only in this run?

### User · 19:14

yes

### Claude · 19:14

> _tool: Bash — Record where the trial is proven_

### Claude · 19:14

Settled: in this run, everything is proven against test harnesses.

5. What does the tablet run on? For example, the alley already owns a particular tablet (iPad, Android), or it must run in a web browser, or it's open and the agents choose.

◆ OMNI · Goal document · step 1 of 4: open decisions · next: what does the tablet run on?

### User · 19:16

good Q... not that I really care, but let's say a web app, which will be easier for us to build and test-run. I guess the LM app generates a QR code or URL for the bowlers to pull up on their mobile devices to use - does that work?

### Claude · 19:16

A web app works. Phones through a QR code would undo a choice you made on the map on 9 Nov: lane tablet, not phones. Phones bring in what you set aside then:
- each phone has to join the right lane, and only that lane
- several phones in one group all have to show the same game
- the LM app would have to make the QR code, which is a change to the LM app
- some bowlers won't have a phone with them

A web app running in the browser of a lane tablet avoids all of that, and the same app could reach phones later.

My recommendation (my guess): a web app on a lane tablet for this trial, with phones by QR code as a later step. Is that the choice?

◆ OMNI · Goal document · step 1 of 4: open decisions · next: web app on a lane tablet, phones later?

### User · 19:17

ok, as you choose

### Claude · 19:17

> _tool: Bash — Record the platform and find the earlier scope list_

### Claude · 19:17

Settled: a web app on a lane tablet. Phones come later.

6. Here's my draft of the trial's **Musts** (all my guess, taken from your use case and earlier decisions):
- A correct score after every roll, including strikes, spares, the 10th frame and the clearing ball
- Names and bowling order: entered, changed at any time, players added mid-game, "Player 1" when nobody has entered names
- Shows whose turn it is, which roll, and how many games are charged; a game counts from its first roll
- Answers the LM app with the game count, and resets when told to
- Takes "Correct roll score" from the pinsetter and re-scores; bowlers can never change a pin count

Should, Could and Won't come next. Which of these Musts is wrong or missing?

◆ OMNI · Goal document · step 1 of 4: open decisions · next: which Must is wrong or missing?

### User · 19:18

i don't use Moscow; i'll make an "in/out" list, what is in scope for any particular increment or release, and what is out. If you make that from what you know now, what's in and what's out?

### Claude · 19:18

> _tool: Bash — Note you work with an in/out list_

### Claude · 19:18

Got it, an in/out list. Here it is for this trial, built from what's settled. Each line is my reading of your decisions.

| Topic | Trial |
|---|---|
| Scoring every roll by the rules, incl. 10th frame and clearing ball | In |
| Names and order: enter, change any time, add mid-game, "Player 1" | In |
| Whose turn, which roll, games charged (from first roll) | In |
| New game: by choice, or by rolling after the 10th frame | In |
| LM app asks the game count and resets the tablet | In |
| "Correct roll score" from the desk via the pinsetter | In |
| Bowlers changing a pin count | Out, never |
| Pinsetter software changes | Out (others deliver) |
| Real pinsetter and live LM app connection | Out (test harnesses) |
| Phones by QR code | Out (later) |
| Voice call-out of the next bowler; strike celebration | Out (later) |
| Manager login on the tablet | ? |
| Lost or out-of-order messages, out-of-turn rolls, too many bowlers, leaving without paying | Out |
| Login for bowlers, lane assignment, payment | Out, never in this app |

The manager login is the one I can't place. It was there so the manager could reset the tablet when the LM app's reset doesn't arrive. Is it in or out for the trial?

◆ OMNI · Goal document · step 1 of 4: in/out list · next: manager login in or out?

### User · 19:21

Manager log in is in for the first release, but not for the first trial run

### Claude · 19:21

> _tool: Bash — Record the manager login decision_

### Claude · 19:21

Got it: manager login is out of the trial and in for the first release. That parks question 7 until then.

The rest of the table is still my reading. Which other line is wrong?

◆ OMNI · Goal document · step 1 of 4: in/out list · next: which other in/out line is wrong?

### User · 19:21

is all good. what's next?

### Claude · 19:21

> _tool: Bash — Record the accepted in/out list_

### Claude · 19:21

✓ In/out list settled for the trial.

Three things are left before I can draft:
- **What gives way first** when two goals pull against each other
- **Limits**, for example whether names stay on the tablet after the reset
- **What proves the trial build works**, for example known games that must score correctly

The first one you already gave on the map (9 Nov). Above all, a correct score after every frame. Try to keep showing who bowls next. Polish gives way first (name entry, how the score looks).

Does that order still hold for the trial?

◆ OMNI · Goal document · step 1 of 4: open decisions · next: does the give-way order still hold?

### User · 19:21

yes

### Claude · 19:22

> _tool: Bash — Record that the give-way order holds_

### Claude · 19:22

✓ Give-way order holds for the trial.

Limits. A group pays and the manager resets the tablet. Are their names and scores gone for good, or does anything keep them, such as a record of past games?

◆ OMNI · Goal document · step 1 of 4: limits · next: are names and scores kept after the reset?

### User · 19:22

gone for good, no record

### Claude · 19:22

> _tool: Bash — Record that nothing is kept after the reset_

### Claude · 19:22

Got it: nothing is kept after the reset.

Next limit. In frame 6, someone knocks the tablet's power cord loose, or the browser page reloads. When it comes back, must the game and the game count still be there?

◆ OMNI · Goal document · step 1 of 4: limits · next: must a game survive a reload mid-game?

### User · 19:25

no, the game is stored locally only, no record kept

### Claude · 19:25

Two readings, and they lead to different apps. "Stored locally" usually means the tablet keeps the game in its own storage, so a reload brings it back. "No" sounds like the game is lost.

There's a consequence if it's lost. The game count goes too, so when the group pays, the LM app has nothing to ask for.

After a reload mid-game, does the tablet show the game again, or a blank "Enter Players"?

◆ OMNI · Goal document · step 1 of 4: limits · next: after a reload, game back or blank?

### User · 19:27

hmmm nice catch - what do you recommend?

### Claude · 19:27

My recommendation (my guess): **the game comes back.** The tablet keeps the current game in its own storage until the LM app resets it, and nothing ever leaves the tablet.

- **For:** the score and the game count survive a reload. The score is your top priority, and the count is what the group pays for. It still keeps "gone for good" at the reset.
- **Against:** a little more to build and test. A roll thrown while the page is reloading is lost, which is the same as a lost message, already out of scope.

Take that?

◆ OMNI · Goal document · step 1 of 4: limits · next: game comes back after a reload?

### User · 19:27

ok then, yes

### Claude · 19:27

> _tool: Bash — Record that the game survives a reload_

### Claude · 19:27

Settled: the game survives a reload, and only the reset erases it.

Last: what proves the trial build works. My guess at the proof is a set of known games, played through the pinsetter harness, where the tablet must show these exact scores:
- your X X X 7/ 2 3 game = 94
- a perfect game = 300; all gutter balls = 0
- both stuck 10th-frame endings (X X 3 and 5 / 2), each with its clearing ball ignored
- a "Correct roll score" mid-game that changes the total
- the LM app harness reading the right game count, then resetting

Which of these is wrong or missing?

◆ OMNI · Goal document · step 1 of 4: proof · next: which proof game is wrong or missing?

### User · 19:28

the test cases will drive all the relevant tests

### Claude · 19:28

So the proof is the use case itself (my reading): every step and extension gets a test, written before the code and run against the harnesses. My list would then just be examples, with your 94 game kept as one.

Is that what you mean?

◆ OMNI · Goal document · step 1 of 4: proof · next: use case drives the proof, list as examples?

### User · 19:28

what is my 94 game?

### Claude · 19:28

It's a check you did on 10 Nov, when you caught my draft scoring a frame too early. You bowl strike, strike, strike, then 7 and a spare, then 2 and 3, and the running total comes to 94:

- frame 1: X → 10+10+10 = 30
- frame 2: X → 10+10+7 = 57
- frame 3: X → 10+7+3 = 77
- frame 4: 7 / → 10+2 = 89
- frame 5: 2 3 → 94

It's a good test because frame 1 can't be scored until two more balls have been thrown.

◆ OMNI · Goal document · step 1 of 4: proof · next: use case drives the proof, list as examples?

### User · 19:29

no - we'll make new tests cases from the use case and any other information that becomes relevant - that set oftest cases defines acceptance

### Claude · 19:29

> _tool: Bash — Record how acceptance is defined_

### Claude · 19:29

> _tool: Bash — Save where we stopped_

### Claude · 19:29

> _tool: Bash — Save where we stopped_

### Claude · 19:29

> _tool: Bash — Save where we stopped_

### Claude · 19:29

✓ Open decisions settled. Next comes testing them, starting with the one most likely to surprise someone.

A group finishes their game and starts putting their shoes on. A child throws one more ball down the lane. Under 4a that starts a new game, and under step 2 it's charged at that roll. So the group is billed for a game nobody played, unless the manager notices and knocks it off at the desk.

Is a stray ball costing a game acceptable for the trial?

◆ OMNI · Goal document · step 2 of 4: testing decisions · next: is a stray ball costing a game acceptable?

### User · 19:29

when, in the omni sequence, do we construct and review the test cases?

### Claude · 19:29

> _tool: Bash — Look up where tests are made in OMNI's sequence_

### Claude · 19:30

> _tool: Bash — Read where OMNI writes and reviews tests_

### Claude · 19:30

In OMNI, the agents build the test cases after the Goal document, not before:

1. **Goal document**: yours, now.
2. **Epics**: the agents split the work into chunks.
3. **Stories with acceptance criteria**: each story states what must be observably true. These are the test cases in plain words.
4. **Review of the stories**: an agent checks they are complete, consistent and testable.
5. **Code, test first**: coders turn each criterion into a test before writing the code.

There are human checkpoints along the way where a summary comes to you. I haven't checked whether one sits right after the stories (step 3).

That matters for your rule that the test cases define acceptance. As it stands, the agents would write the test cases from your Goal document, and you'd see them only if a checkpoint shows them to you.

◆ OMNI · Goal document · step 2 of 4: testing decisions · next: is a stray ball costing a game acceptable?

### User · 19:34

every roll counts. Period. The case you propose is up to the manager to decide, out of scope for our project

### Claude · 19:34

> _tool: Bash — Record that every roll counts_

### Claude · 19:34

Settled: every roll counts, and discounts are the manager's business.

Next test, on *a. Ann throws her 1st ball and leaves 4 pins standing. Before her 2nd ball, someone moves Bob above her in the order. The pinsetter is waiting for a 2nd roll on Ann's pins.

Who does the tablet call for next: Ann to finish her frame, or Bob?

◆ OMNI · Goal document · step 2 of 4: testing decisions · next: mid-frame reorder: Ann finishes, or Bob?

### User · 19:38

pleas save the state, transcript and all, my laptop is outof battery
