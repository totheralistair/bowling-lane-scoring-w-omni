# Bowl a game at a lane

_Fourth cut, Alistair's text as pasted on 2026-11-12, put together from his pastes in that session. His working copy (`bowling use case v2.docx`) is the master; where this file and his copy differ, his copy wins. Extensions settled with him on 2026-11-12; not yet formally approved as the use case for the Goal document._

## Contents

- [Main success scenario](#main-success-scenario)
- [Extensions](#extensions)
- [Extensions out of scope](#extensions-out-of-scope)
- [Notes](#notes)

## Main success scenario

**Precondition:** At the beginning of the day and after every group pays, the manager uses the Lanes Manager App (LM app) to reset the ScoreKeeper app (the Tablet) to a blank and empty game, with the instruction to "Enter Players". When a new group arrives, the Tablet shows this reset state.

1. Bowler enters the group's names in bowling order and starts the game.
2. The Tablet always indicates whose turn it is, which roll it is and how many games are being charged. A game is charged the moment the first roll is made. Charges are for games /started/ not games /finished/.
3. After each roll, the Pinsetter sends roll number (1st or 2nd) and number of pins currently down. The Tablet updates the score in that bowler's frame according to the rules of bowling. Tablet indicates who the next bowler is and which roll it will be (including the possible 3rd roll in the 10th frame).
4. Group repeats step 3 until every bowler has finished the 10th frame.
5. Bowlers choose whether to start a new game, or go and pay for the games they bowled.
6. When the Group pays at the main desk for the games they played, the manager has the LM app reset the Tablet for the next group. (separate use case, showing dialog of # games to charge, followed by the reset)

## Extensions

\*a. Any bowler can change the names and bowling sequence at any time. This may produce the situation that someone who hasn't bowled in this frame is above someone who has. The Tablet calls for the appropriate next person to bowl.

\*b. A new player is added part way through the game: The Tablet enters them with rolls of zero until they are caught up with the rest of the people.

1a. Someone rolls a ball before names have been entered, the pinsetter sends the roll information: The Tablet starts the game, calling the bowler "Player 1". In case more rolls are done before adding other players, the tablet considers this a 1-person game.

3a. A 3rd roll in 10th frame leaves 2nd roll dangling (eg X.X.3, or 5./.2, although X.3.4 is not a problem): Tablet asks the bowler to bowl one more roll just to clear the pinsetter. It ignores the number the pinsetter sends.

3b. Pinsetter reports incorrect number of pins down: Bowler goes to the main desk. Desk staff fix the number in the pinsetter. Pinsetter sends "Correct roll score" to the tablet (roll number, number of pins down). Tablet updates the score and bowling continues.

3c. Case 3b but a bowler has already bowled the next ball before the pinsetter got corrected: The correction is ignored. (Actually, I don't think this can happen, but ok).

4a. Bowlers keep rolling balls after the final bowler's 10th frame (including any last clearing roll), when the game is technically over: Tablet starts a new game automatically with the same names and order.

## Extensions out of scope

- 1b. Too many bowlers for the lane
- 3d. Pinsetter's message never arrives (the tablet can't detect)
- 3e. A bowler rolls out of turn (the tablet can't detect)
- 3f. A pinsetter message arrives out of order
- 6a. The group leaves without paying

## Notes

- Step 4 reads "repeats step 3" here; the pasted text said "step 5", a leftover from the earlier numbering. Check your copy.
- Not an extension, a limit for the Goal document: the Tablet has no way to enter or change a pin count (Alistair: "*b can't happen because the tablet has no input option for that"; this is the F2 Must).
- The manager's own use case (game count dialog and Reset in the LM app) is still to write.
