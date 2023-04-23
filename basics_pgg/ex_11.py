"""
Write a game of treasure hunting on a two-dimensional board 10 x 10.
The user can enter commands to change the position of the character.
After each move, the user should be notified if he is heading in the right direction.
Going beyond the board means the end of the game.
After finding the treasure, write down the number of moves used by the user to reach the goal.

Additionally:
- after taking more steps than twice the minimum number of steps, put the treasure in a new place
- with 1/5 probability, don’t give the player a clue after completing the step


STAGE 1 - moving around the board
1. Define variables with user and treasure position on a board (start with hard coding the position)
2. Create infinite while loop, where:
- we show the users position
- asking the user about move direction (w, s, a, d)
- change the direction or inform the user that the direction is incorrect

STAGE 2 - Check users position
1. If the user moved outside of the board we are ending the game
2. If users position (x, y) are the same as treasures position (x, y) inform the user that he won and end the game

STAGE 3 - number of tries/steps
1. Define proper variable before the loop
2. After each move we are incrementing this value in this variable
3. If players position and treasure position is the same, then he won the game and we show how many moves he did.

STAGE 4 - hot&cold
https://www.calculatorsoup.com/calculators/geometry-plane/distance-two-points.php
1. Calculate the distance BEFORE players move.
2. Calculate the distance AFTER players move.
3. Based on those two values we show to the user information if he's getting closer or further from the treasure.

STAGE 5 - do not show hint with 1/5 probability
1. use randint(1,5) - if the number we get is different than 5 then we do show the hint.

STAGE 6 - moving the treasure after making to many moves
1. Before the loop count the minimal distance between the users and treasure position. We can use abs() function.
2. After the move we can check if the number of moves is bigger than 2x minimum number of moves.
3. if so:
- draw new position of the treasure (x, y)
- count minimum number of moves once again (for the new treasure position)
- reset the number of moves variable (assign 0)

STAGE 7 - draw players and treasure position at the beginning of the game
1. use randint() function.

Notes:
- distance between 2 points https://www.calculatorsoup.com/calculators/geometry-plane/distance-two-points.php
"""