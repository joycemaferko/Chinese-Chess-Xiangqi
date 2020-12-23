# Author: Matthew Joyce
# Date: 12/23/2020
# Description: Implemenation of Xiangqi in Python

class XiangqiGame: 
    """Create XQ Game class, which sets the board and controls game state"""

    def __init__(self):
        """Initializes data members for XQ Game class"""

        self._game_state = "UNFINISHED"
        self._player_turn = "red"

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

    