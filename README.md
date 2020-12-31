# Chinese-Chess-Xiangqi
A two-player game of Chinese Chess (Xiangqi) programmed in Python

Author: Matthew Joyce

Date: 12/31/2020

Description: Implemenation of Chinese Chess (Xiangqi) in Python. The rules can be found here (https://en.wikipedia.org/wiki/Xiangqi).

This game is played using algebraic notation to represent the squares on the board. For example, "a4" represents the piece in column "a" and row "4".

To play, initiate an instance of the XiangqiGame class. For example: game = XiangqiGame().

Next, include the following two lines to print the board and display the current state of the game (UNFINISHED, RED_WINS, or BLACK_WINS, respectively)

print(game.get_game_state())

game.print_board()

Finally, players move using the command: game.make_move("square from", "square_to")

For example, to move the red general one square forward from his starting position, enter: game.make_move("e1", "e2")

make_move() will return True if the move is valid, otherwise it will return False. If a player enters an invalid move, it remains their turn until they have played a valid move.

The game continues until one side has placed the other side's general in checkmate, where they have no valid moves to escape.

Red has the first move.

![Capture](https://user-images.githubusercontent.com/55785709/103416240-167e2a00-4b86-11eb-8588-cfc390572a2c.PNG)
