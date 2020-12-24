# Author: Matthew Joyce
# Date: 12/23/2020
# Description: Implemenation of Xiangqi in Python

class XiangqiGame: 
    """Create XQ Game class, which sets the board and controls game state"""

    def __init__(self):
        """Initializes data members for XQ Game class"""

        self._game_state = "UNFINISHED"
        self._player_turn = "red"
        self._board = [
            [Chariot("red", "a1", "r R"), Horse("red", "b1", "r H"), Elephant("red", "c1", "r E"), Adviser("red", "d1", "r A"),
                 General("red", "e1", "r G"), Adviser("red", "f1", "r A"), Elephant("red", "g1", "r E"), Horse("red", "h1", "r H"),
                 Chariot("red", "i1", "r R")],
            [None, None, None, None, None, None, None, None, None],
            [None, Cannon("red", "b3", "r C"), None, None, None, None, None, Cannon("red", "h3", "r C"), None],
            [Soldier("red", "a4", "r S"), None, Soldier("red", "c4", "r S"), None, Soldier("red", "e4","r S"), None,
                 Soldier("red", "g4", "r S"), None, Soldier("red", "i4", "r S")],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [Soldier("black", "a7","b S"), None, Soldier("black", "c7","b S"), None, Soldier("black", "e7","b S"), None,
                 Soldier("black", "g7","b S"), None, Soldier("black", "i7","b S")],
                [None, Cannon("black", "b8", "b C"), None, None, None, None, None, Cannon("black", "h8", "b C"), None],
                [None, None, None, None, None, None, None, None, None],
                [Chariot("black", "a10","b R"), Horse("black", "b10","b H"), Elephant("black", "c10","b E"), Adviser("black", "d10","b A"),
                 General("black", "e10","b G"), Adviser("black", "f10","b A"), Elephant("black", "g10","b E"), Horse("black", "h10","b H"),
                 Chariot("black", "i10","b R")]
        ]

    def get_player_turn(self):
        """returns the color of player whose turn it is"""
        return self._player_turn

    def set_player_turn(self, color):
        """sets the color of the player whose turn it is"""
        self._player_turn = color

    def print_board(self):
        """Prints game board."""

        columns = "   a     b     c     d     e     f     g     h     i"
        top = "┏━" + ''.join("━━━━┯━" for _ in range(8)) + '━━━━┓'
        bot = "┗━" + ''.join("━━━━┷━" for _ in range(8)) + '━━━━┛'
        sep = "┠─" + ''.join("────┼─" for _ in range(8)) + '────┨'

        def r(row):
            return "┃" + "│".join(f" {repr(GamePiece)} " if GamePiece else "     " for GamePiece in row) + "┃"

        top_mid = f"\n{sep}\n".join(r(self._board[i]) + " " + str(i + 1) for i in range(5))
        river = f"{bot}\n\033[0;34m░░░░░░░░░░░░░░░░░░░░░░░░░River░░░░░░░░░░░░░░░░░░░░░░░░░\033[0m\n{top}"
        bot_mid = f"\n{sep}\n".join(r(self._board[i]) + " " + str(i + 1) for i in range(5, 10))

        print(f"{columns}\n{top}\n{top_mid}\n{river}\n{bot_mid}\n{bot}\n{columns}")

    def is_in_check(self, color):
        """Returns True if given color is in check, otherwise returns False"""
        pass

    def make_move(self, str_from, str_to):
        """
        Checks move for validity, makes move, checks and updates game state as neccessary.
        Returns true if move is successful, false otherwise
        """
        #Parses string input and matches the string values to the list of lists board.
        current_col = ord(str_from[0]) - 97
        current_row = int(str_from[1:]) - 1
        new_col = ord(str_to[0]) - 97
        new_row = int(str_to[1:]) - 1
        moving_piece = self._board[current_row][current_col]
        player = self.get_player_turn()

        # adding exception for index error to allow for iterating through potential moves
        # try:
        #     destination = self._board[new_col][new_row]
        # except IndexError:
        #     return False

        # Checks that the game has not already been won
        if self._game_state != "UNFINISHED":
            return False

        #Checks to ensure players are moving in turn
        if moving_piece.get_color() != player:
            return False

        # returns False if the move fails validity checks for the piece in question
        # if not moving_piece.is_valid_move(current_col, current_row, new_col, new_row, self._board):
        #     return False

        self.the_move(str_from, str_to, moving_piece)

        # Switch Player Turn
        if self.get_player_turn() == "red":
            self.set_player_turn("black")
            return True
        else:
            self.set_player_turn("red")
            return True

    def the_move(self, str_from, str_to, moving_piece):
        """actually conduct the move"""

        #Parses string input and matches the string values to the list of lists board.
        current_col = ord(str_from[0]) - 97
        current_row = int(str_from[1:]) - 1
        new_col = ord(str_to[0]) - 97
        new_row = int(str_to[1:]) - 1
        # moving_piece = self._board[current_col][current_row]

        self._board[new_row][new_col] = moving_piece
        self._board[current_row][current_col] = None
        

class GamePiece:
    """Create GamePiece class, which provides general rules for all pieces"""

    def __init__(self, color, location, piece_id):
        """Initializes data members for GamePiece class"""

        self._color = color
        self._location = location
        self._piece_id = piece_id

    def __repr__(self):
        """returns easily identifiable representation of piece object on board"""

        return self._piece_id

    def get_color(self):
        """returns value of color"""

        return self._color

    def get_location(self):
        """gets location of piece"""

        return self._location

    def set_location(self, location):
        """updates location of game piece"""

        self._location = location

    def is_valid_move(self, current_col, curr_row, new_col, new_row, board):
        """tests move against general rules for all pieces. Returns true if move
        is successful, otherwise false. 

        May take this out if I can just implement in my sub-classes
        """
        pass

class Chariot(GamePiece):
    """Creates Chariot sub-class"""
    pass

class Horse(GamePiece):
    """Creates Horse sub-class"""
    pass

class Elephant(GamePiece):
    """Creates Elephant sub-class"""
    pass

class Adviser(GamePiece):
    """Creates Adviser sub-class"""
    pass

class General(GamePiece):
    """Creates General sub-class"""
    pass

class Cannon(GamePiece):
    """Creates Cannon sub-class"""
    pass

class Soldier(GamePiece):
    """Creates Soldier sub-class"""
    pass

game = XiangqiGame()




print(game.make_move("a1", "a2"))



game.print_board()
