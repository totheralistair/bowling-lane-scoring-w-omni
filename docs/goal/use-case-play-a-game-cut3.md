# Bowl a game at a lane

_Third cut ("3rd Try"), the user's text as pasted on 2026-11-11, under discussion, not approved. The user's working copy is `bowling use case.docx`; earlier cuts: use-case-play-a-game.md (reference) and use-case-play-a-game-cut2.md. Fixes the user agreed to but has not yet typed in are listed after the text._

**Precondition:** At the beginning of the day and after every group pays, the manager uses the Lanes Manager App (LM app) to reset the ScoreKeeper app (the Tablet) to a blank and empty game, with the instruction to "Enter Players". When a new group arrives, the Tablet shows this reset state.

1. Bowler enters the group's names in bowling order and starts the game.
2. The Tablet always indicates whose turn it is and which roll it it.
5. After each roll, the Pinsetter sends roll number (1st or 2nd) and number of pins currently down. The Tablet updates the score in that bowler's frame according to the rules of bowling. Tablet indicates who the next bowler is and which roll it will be (including the possible 3rd roll in the 10th frame).
6. Group repeats step 5 until every bowler has finished the 10th frame.
7. Bowlers choose whether to start a new game, or go and pay for the games they bowled.
8. When the Group pays at the main desk for the games they played, the manager has the LM app reset the Tablet for the next group. (separate use case, showing dialog of # games to charge, followed by the reset)

\*a. Any bowler can change the names and bowling sequence at any time. This may produce the situation that someone who hasn't bowled in this frame is above someone who has. The Tablet calls for the appropriate next person to bowl. (Bold, text, voice, whatever)

5a. 3rd roll in 10th frame: Tablet asks the bowler to bowl one more roll just to clear the pinsetter.

5b. Pinsetter reports incorrect number of pins down: … procedure involving front desk

6a. Bowlers keep rolling balls after the 10th frame: ??? What's the rule?

## Agreed fixes not yet in the text

- 5a trigger (user's wording with the agent's tweak): "3rd roll in 10th frame leaves the Pinsetter waiting for its 2nd roll (e.g. XX3 or 5/2; X34 is not a problem)". Add: Tablet ignores the clearing ball's pins.
- Agent's notes, not yet taken up by the user: step numbering (1, 2, 5, 6); typo "which roll it it"; step 2 and the end of step 5 say the same thing; 5b can cite the trial decision (wrong count stands; later, "change roll score").

## Open in this cut

- 6a: the rule for rolls after the game. Agent's options: (a) Tablet ignores rolls when no game is on, and asks for a clearing ball if a New Game starts with the pinsetter mid-rack; (b) a roll after the game starts a New Game automatically (counted and charged); (c) as (a), plus "Game over: press New Game". Agent leaned to (a) or (c). Undecided.
- A pinsetter message arriving out of order (the visible effect of a lost message): add an extension, or leave for later? Undecided.
- Who "the manager" is: main desk staff, or the owner/manager?
