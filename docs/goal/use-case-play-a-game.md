# Bowl a game at a lane

_Draft, unclaimed. ✋ = agent's guess. OPEN = for the user to supply._

**Main Success Scenario:**

1. Group arrives at the lane; Tablet shows the previous group's final scores.
2. Bowler presses Start Over; Tablet clears the names and scores and shows name entry.
3. Bowler enters the group's names in bowling order and starts the game.
4. Tablet shows whose turn it is.
5. Bowler rolls; Pinsetter sends "1st roll, n"; Tablet records it in that bowler's frame.
6. Bowler rolls again; Pinsetter sends "2nd roll, total"; Tablet works out the second ball, scores the frame, and shows the next bowler.
7. Group repeats steps 4–6 until every bowler has finished the 10th frame.
8. Tablet shows the final scores and waits.
9. Group leaves the lane.
10. Group pays at the main desk for the games they played. OPEN: how the desk knows how many games that was.

**Extensions:**

1a. Tablet shows name entry (the previous group pressed Start Over):
  1a1. Use case continues at step 3.

1b. Tablet shows a game in progress (the previous group left mid-game):
  1b1. Bowler presses Start Over.
  1b2. Tablet asks "End this game?".
  1b3. Bowler confirms; use case continues at step 3.

1b3a. Bowler does not confirm:
  1b3a1. ✋ Tablet keeps the old game on screen.

2a. Bowler presses Next Game instead of Start Over:
  2a1. Tablet starts a new game with the previous group's names and order.
  2a2. OPEN: this game is charged to the previous group. What stops it, or catches it?

3a. ✋ Bowler mistypes a name or gets the order wrong:
  3a1. Bowler corrects the names or order; allowed until the first ball is rolled.

3b. OPEN: the smallest and largest number of bowlers in a game.

5a. Bowler knocks down all 10 pins on the 1st roll (strike):
  5a1. Pinsetter sends "1st roll, 10" and sets a new ten.
  5a2. Tablet scores a strike and shows the next bowler; use case continues at step 4.

5b. Pinsetter's message never arrives:
  5b1. Group goes to the main desk; play on the lane waits.
  5b2. OPEN: in the trial, what does the desk do to get the lane going again?

5c. Pinsetter reports the wrong count:
  5c1. Bowler goes to the main desk before the next ball is thrown.
  5c2. Desk staff fix the count in the pinsetter app's override.
  5c3. Trial iteration: Tablet is not told; the wrong count stands; use case continues.
  5c4. Later iteration: Pinsetter sends "change roll score" for the roll it just sent; Tablet re-scores; use case continues.

5c1a. The next ball has already been thrown:
  5c1a1. The count stands; use case continues.

5d. ✋ A different bowler rolls out of turn:
  5d1. Tablet credits the roll to whoever it shows as up (Pinsetter knows no players).
  5d2. OPEN: does that matter in the trial?

6a. Bowler knocks down the remaining pins on the 2nd roll (spare):
  6a1. Pinsetter sends "2nd roll, 10"; Tablet scores a spare; use case continues at step 4.

6b. Pinsetter's message never arrives: as 5b.

6c. Pinsetter reports the wrong count: as 5c.

7a. Bowler gets a strike or spare in the 10th frame:
  7a1. Tablet gives the bonus ball or balls the rules allow.

7a1a. The 10th frame ends stuck (strike-strike-non-strike, or spare then a non-strike bonus ball):
  7a1a1. Tablet asks the bowler for one free extra ball to clear the lane.
  7a1a2. Bowler throws it; Pinsetter clears after its 2nd roll; Tablet ignores that ball's pins.

7a1a2a. Bowler will not throw the clearing ball:
  7a1a2a1. The lane stays mid-frame; time passes (neither app has a sense of time); the desk can step in.

8a. Group wants another game:
  8a1. Bowler presses Next Game.
  8a2. Tablet keeps the names and order and starts a new game; use case continues at step 4.
  8a3. OPEN: how the extra game reaches the group's charge.

9a. Group wants their names off the screen:
  9a1. Bowler presses Start Over; Tablet shows name entry; use case continues at step 10.

\*a. At any time, a bowler tries to change a pin count on the Tablet:
  \*a1. Tablet offers no way to do it.

**Open issues:**

1. Charging (steps 10, 2a2, 8a3): how the desk knows how many games a group played.
2. 3b: the smallest and largest group.
3. 5b2: getting a lane going again in the trial when a message never arrives.
4. 5d2: a bowler rolling out of turn.
