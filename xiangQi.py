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
            [Chariot("Red", "a1", "r R"), Horse("Red", "b1", "r H"), Elephant("Red", "c1", "r E"), Adviser("Red", "d1", "r A"),
                 General("Red", "e1", "r G"), Adviser("Red", "f1", "r A"), Elephant("Red", "g1", "r E"), Horse("Red", "h1", "r H"),
                 Chariot("Red", "i1", "r R")],
            [None, None, None, None, None, None, None, None, None],
            [None, Cannon("Red", "b3", "r C"), None, None, None, None, None, Cannon("Red", "h3", "r C"), None],
            [Soldier("Red", "a4", "r S"), None, Soldier("Red", "c4", "r S"), None, Soldier("Red", "e4","r S"), None,
                 Soldier("Red", "g4", "r S"), None, Soldier("Red", "i4", "r S")],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [Soldier("Black", "a7","b S"), None, Soldier("Black", "c7","b S"), None, Soldier("Black", "e7","b S"), None,
                 Soldier("Black", "g7","b S"), None, Soldier("Black", "i7","b S")],
                [None, Cannon("Black", "b8", "b C"), None, None, None, None, None, Cannon("Black", "h8", "b C"), None],
                [None, None, None, None, None, None, None, None, None],
                [Chariot("Black", "a10","b R"), Horse("Black", "b10","b H"), Elephant("Black", "c10","b E"), Adviser("Black", "d10","b A"),
                 General("Black", "e10","b G"), Adviser("Black", "f10","b A"), Elephant("Black", "g10","b E"), Horse("Black", "h10","b H"),
                 Chariot("Black", "i10","b R")]
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

    def make_move(self, sq_from, sq_to):
        """
        Checks move for validity, makes move, checks and updates game state as neccessary.
        Returns true if move is successful, false otherwise
        """
        pass

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

game.print_board()

