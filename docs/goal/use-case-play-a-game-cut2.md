# Bowl a game at a lane

_Second cut, under discussion, not approved (first cut: use-case-play-a-game.md). Main scenario and the first extensions: the user's revision, 2026-11-10. ✋ = agent's guess. OPEN = for the user to supply._

**Main Success Scenario:**

1. Group arrives at the lane; Tablet shows a blank score sheet with "Enter players".
2. Bowler enters the group's names in bowling order and starts the game. Any bowler can change the names and bowling order at any time.
3. Tablet always shows whose turn it is.
4. After each roll in a bowler's frame, Pinsetter sends "roll number in the frame, number of pins knocked down". Tablet updates the score in that bowler's frame according to the rules of bowling (allowing for earlier strikes and spares). Tablet shows who the next bowler is and which roll (including a possible 3rd roll in the 10th frame).
5. Group repeats step 4 until every bowler has finished the 10th frame.
6. After the game, Tablet asks "All done, or new game?"; bowlers choose which.
7. Group leaves the lane.
8. Group pays at the main desk for the games they played. OPEN: how the desk knows how many games that was.

**Extensions:**

1a. Tablet still shows the previous group's game; someone presses Start Over:
  1a1. Previous game was finished: Tablet resets to a blank score sheet; use case continues at step 2.
  1a2. Previous group left mid-game: Tablet asks "End game and start over?"
    1a2a. Yes: Tablet resets to a blank score sheet; use case continues at step 2.
    1a2b. No: the new group takes over the old group's game. OPEN: how billing works.

1b. Tablet still shows the previous group's game; someone presses New Game with the same players:
  1b1. OPEN: how billing works.

3a. Bowlers change the bowling order so someone who hasn't bowled is above someone who has:
  3a1. Tablet shows the person who hasn't bowled as the next bowler.

**From the earlier draft, not yet placed in the revision** _(renumbered to the new steps; keep or drop?)_

4a. Pinsetter's message never arrives:
  4a1. Group goes to the main desk; play on the lane waits.
  4a2. OPEN: in the trial, what does the desk do to get the lane going again?

4b. Pinsetter reports the wrong count:
  4b1. Bowler goes to the main desk before the next ball is thrown.
  4b2. Desk staff fix the count in the pinsetter app's override.
  4b3. Trial iteration: Tablet is not told; the wrong count stands; use case continues.
  4b4. Later iteration: Pinsetter sends "change roll score" for the roll it just sent; Tablet re-scores; use case continues.

4b1a. The next ball has already been thrown:
  4b1a1. The count stands; use case continues.

4c. ✋ A different bowler rolls out of turn:
  4c1. Tablet credits the roll to whoever it shows as up (Pinsetter knows no players).
  4c2. OPEN: does that matter in the trial?

4d. The 10th frame ends with pins still standing (strike-strike-non-strike, or spare then a non-strike bonus ball):
  4d1. Tablet asks the bowler for one free extra ball to clear the lane.
  4d2. Bowler throws it; Pinsetter clears after its 2nd roll; Tablet ignores that ball's pins.

4d2a. Bowler will not throw the clearing ball:
  4d2a1. The lane stays mid-frame; time passes (neither app has a sense of time); the desk can step in.

\*a. At any time, a bowler tries to change a pin count on the Tablet:
  \*a1. Tablet offers no way to do it.

**Open issues:**

1. Charging (step 8, 1a2b, 1b1): how the desk knows how many games a group played.
2. The smallest and largest group.
3. 4a2: getting a lane going again in the trial when a message never arrives.
4. 4c2: a bowler rolling out of turn.
5. Step 4 changes the Pinsetter's message. The earlier draft had "2nd roll, total" (pins down so far in the frame). The revision reads as pins knocked down by that roll alone, and it numbers a 3rd roll in the 10th frame. If that is meant, the Pinsetter must know about the 10th frame, and 4d may no longer be needed.
