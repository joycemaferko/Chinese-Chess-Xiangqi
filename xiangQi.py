# Author: Matthew Joyce
# Date: 12/23/2020
# Description: Implemenation of Xiangqi in Python

class XiangqiGame: 
    """Create XQ Game class, which sets the board and controls game state"""

    def __init__(self):
        """Initializes data members for XQ Game class"""

        self._game_state = "UNFINISHED"
        self._player_turn = "red"
        self._board = []

    def get_player_turn(self):
        """returns the color of player whose turn it is"""
        return self._player_turn

    def set_player_turn(self, color):
        """sets the color of the player whose turn it is"""
        self._player_turn = color

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
    """Creates Chariot sub-class"""
    pass

class Elephant(GamePiece):
    """Creates Chariot sub-class"""
    pass

class Adviser(GamePiece):
    """Creates Chariot sub-class"""
    pass

class General(GamePiece):
    """Creates Chariot sub-class"""
    pass

class Cannon(GamePiece):
    """Creates Chariot sub-class"""
    pass

class Soldier(GamePiece):
    """Creates Chariot sub-class"""
    pass