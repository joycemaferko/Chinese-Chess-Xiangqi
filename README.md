# Chinese-Chess-Xiangqi
A two-player game of Chinese Chess (Xiangqi) programmed in Python.

Author: Matthew Joyce
Date: 12/23/2020

Description: Implemenation of Chinese Chess (Xiangqi) in Python. The rules 
can be found here (https://en.wikipedia.org/wiki/Xiangqi).
 
This game is played using algebraic notation to represent the squares on 
the board. For example, "a4" represents the piece in column "a" and row "4". 

To play, initiate an instance of the XiangqiGame class. For example: 
game = XiangqiGame().

Next, include the following two lines to print the board and display the 
current state of the game (UNFINISHED, RED_WINS, BLACK_WINS)

print(game.get_game_state())
game.print_board()

Finally, players make a move using the command: game.make_move("<square from>", "<square_to>")
For example, to move the red general one square forward from his starting position, enter:
game.make_move("e1", "e2")

make_move() will return True if the move is valid, otherwise it will return False

Red has the first move.
