# Author: Matthew Joyce
# Date: 12/23/2020
# Description: Implemenation of Xiangqi in Python.

import unittest

class XiangqiGame: 
    """Create XQ Game class, which sets the board and controls game state"""

    def __init__(self):
        """Initializes data members for XQ Game class"""

        self._game_state = "UNFINISHED"
        self._player_turn = "red"
        self._black_gen_pos = "e10"
        self._red_gen_pos = "e1"
        self._black_in_check = False
        self._red_in_check = False
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
    
    def get_game_state(self):
        """Returns current value of game state: Either Unfinished, Black Won, or Red Won"""
        return self._game_state

    def set_game_state(self, state):
        """sets game state"""
        self._game_state = state

    def get_player_turn(self):
        """returns the color of player whose turn it is"""
        return self._player_turn

    def set_player_turn(self, color):
        """sets the color of the player whose turn it is"""
        self._player_turn = color

    def set_black_gen_pos(self, pos):
        """updates the position of the black general to pos"""
        self._black_gen_pos = pos

    def get_black_gen_pos(self):
        """returns black general's location in algebraic notation"""
        return self._black_gen_pos

    def set_red_gen_pos(self, pos):
        """updates the position of the red general to pos"""
        self._red_gen_pos = pos

    def get_red_gen_pos(self):
        """returns red general's location in algebraic notation"""
        return self._red_gen_pos

    def set_red_in_check(self, state):
        """sets True if red in check, Otherwise False"""
        self._red_in_check = state

    def set_black_in_check(self, state):
        """sets True if black in check, Otherwise False"""
        self._black_in_check = state

    def update_general_pos(self, str_from, str_to):
        """updates general's position on the board"""
        
        if str_from == self._black_gen_pos:
            self.set_black_gen_pos(str_to)

        if str_from == self._red_gen_pos:
            self.set_red_gen_pos(str_to)

    # def print_board(self):
    #     empty = "     "
    #     dashes = "  ----"
    #     row_num = 1
    #     columns = ['a','b','c','d','e','f','g','h','i']
    #     river = f"\033[0;34m░░░░░░░░░░\u695A\u6CB3░░░░░░░░░░░River░░░░░░░░░░\u6F22\u754C░░░░░░░░░░░░\033[0m"
    #     print(dashes * 9)

    #     for row in self._board:
    #         print("|" + "|".join(f" {repr(GamePiece)} " if GamePiece else empty \
    #             for GamePiece in row) + "|" + " " + str(row_num))
    #         row_num += 1
    #         print(dashes * 9)
    #         if row_num == 6:
    #             print(river)
    #             print(dashes * 9)

    #     for letter in columns:
    #         print("   {}  ".format(letter), end="")

    def print_board(self):
        """Prints game board."""

        columns = "   a     b     c     d     e     f     g     h     i"
        top = "\u250F" + "\u2501" + ''.join("━━━━┯━" for x in range(8)) + ("\u2501" *4) + "\u2513"
        bot = "\u2517" + "\u2501" + ''.join("━━━━┷━" for x in range(8)) + ("\u2501" *4) + "\u251B"
        sep = "\u2520" + "\u2500" + ''.join("────┼─" for x in range(8)) + ("\u2500" * 4) + "\u2528"

        def r(row):
            return "\u2503" + "\u2502".join(f" {repr(GamePiece)} " if GamePiece else "     " for GamePiece in row) + "\u2503"

        top_mid = f"\n{sep}\n".join(r(self._board[i]) + " " + str(i + 1) for i in range(5))
        river = f"{bot}\n\033[0;34m░░░░░░░░░░\u695A\u6CB3░░░░░░░░░░░River░░░░░░░░░░\u6F22\u754C░░░░░░░░░░░░\033[0m\n{top}"
        bot_mid = f"\n{sep}\n".join(r(self._board[i]) + " " + str(i + 1) for i in range(5, 10))

        print(f"{columns}\n{top}\n{top_mid}\n{river}\n{bot_mid}\n{bot}\n{columns}")


    def is_in_check(self, color):
        """Returns True if given color is in check, otherwise returns False"""

        # returns True if black is in check, otherwise returns False
        if color == "black":
            if self._black_in_check is True:
                return True
            return False

        # returns True if red is in check, otherwise returns False
        if color == "red":
            if self._red_in_check is True:
                return True
            return False

    def make_move(self, str_from, str_to):
        """
        Checks move for validity, makes move, checks and updates game state as
        neccessary. Returns true if move is successful, false otherwise
        
        """
        #Parses string input and matches the string values to the list of lists board.
        current_col = ord(str_from[0]) - 97
        current_row = int(str_from[1:]) - 1
        new_col = ord(str_to[0]) - 97
        new_row = int(str_to[1:]) - 1
        moving_piece = self._board[current_row][current_col]
        destination = self._board[new_row][new_col]
        player = self.get_player_turn()

        # Checks to ensure that there is actually a piece on the square to move
        if moving_piece is None:
            return False

        # Checks to ensure that player is actually moving to a different square
        if str_from == str_to:
            return False

        # Checks that the game has not already been won
        if self._game_state != "UNFINISHED":
            return False

        #Checks to ensure players are moving in turn
        if moving_piece.get_color() != player:
            print("It's the other player's turn!")
            return False

        # returns False if the move fails validity checks for the piece in question
        if not moving_piece.is_valid_move(current_col, current_row, new_col, \
            new_row, self._board):
            return False

        # make the move
        self.the_move(str_from, str_to, moving_piece)

        # update the location for the piece
        moving_piece.set_location(str_to)

        # Track General's position for "in-check"
        if type(moving_piece) is General:
            self.update_general_pos(str_from, str_to)

        # Test if the move has placed General in check. If opposing Gen in check,
        # update check status, return true. If player has put their own general in 
        # check, reverse move and return false.
        self.check_for_check()
        if player == "red" and self.is_in_check("red"):
            #reverse move and update General position
            if type(moving_piece) is General:
                self.reverse_move(str_from, str_to, moving_piece, destination)
                moving_piece.set_location(str_from)
                self.update_general_pos(str_to, str_from)
                return False
            else:
                #reverse move
                self.reverse_move(str_from, str_to, moving_piece, destination)
                moving_piece.set_location(str_from)
                return False

        if player == "black" and self.is_in_check("black"):
            #reverse move and update General position
            if type(moving_piece) is General:
                self.reverse_move(str_from, str_to, moving_piece, destination)
                moving_piece.set_location(str_from)
                self.update_general_pos(str_to, str_from)
                return False
            else:
                #reverse move
                self.reverse_move(str_from, str_to, moving_piece, destination)
                moving_piece.set_location(str_from)
                return False

        # check for checkmate
        self.check_for_checkmate(player)

        # Switch Player Turn
        if self.get_player_turn() == "red":
            self.set_player_turn("black")
            return True
        else:
            self.set_player_turn("red")
            return True

    def the_move(self, str_from, str_to, moving_piece):
        """actually conduct the move"""

        #Parses string input and matches string values to the list of lists board.
        current_col = ord(str_from[0]) - 97
        current_row = int(str_from[1:]) - 1
        new_col = ord(str_to[0]) - 97
        new_row = int(str_to[1:]) - 1

        self._board[new_row][new_col] = moving_piece
        self._board[current_row][current_col] = None

    def reverse_move(self, str_from, str_to, moving_piece, destination):
        """reverses a move that put one's own General in check"""

        #Parses string input and matches string values to the list of lists board.
        current_col = ord(str_from[0]) - 97
        current_row = int(str_from[1:]) - 1
        new_col = ord(str_to[0]) - 97
        new_row = int(str_to[1:]) - 1

        self._board[new_row][new_col] = destination
        self._board[current_row][current_col] = moving_piece


    def check_for_check(self):
        """check potential moves for all pieces of a color, add them to a set.
        If opposing General's position is present in the set, General is in check. 
        Set that color to in-check.
        """
        # Default to not in check. This condition will be re-evaluated every move
        self.set_red_in_check(False)
        self.set_black_in_check(False)

        # Iterate over all spaces on the board
        for row in self._board:
            for square in row:
                mover = square

                if mover is not None:
                    str_from = mover.get_location()
                    current_col = ord(str_from[0]) - 97
                    current_row = int(str_from[1:]) - 1

                    # mover is red. Check valid moves against black general's position
                    # If any of red's valid moves can capture the General, black is in check
                    if mover.get_color() == "red":
                        new_col = ord(self.get_black_gen_pos()[0]) - 97
                        new_row = int(self.get_black_gen_pos()[1:]) - 1

                        if mover.is_valid_move(current_col, current_row, new_col, \
                            new_row, self._board):
                            self.set_black_in_check(True)
                            return True

                    # mover is black. Check valid moves against red general's 
                    # position
                    else:
                        new_col = ord(self.get_red_gen_pos()[0]) - 97
                        new_row = int(self.get_red_gen_pos()[1:]) - 1

                        if mover.is_valid_move(current_col, current_row, new_col, \
                            new_row, self._board):
                            self.set_red_in_check(True)
                            return True


    def check_for_checkmate(self, player):
        """Can the color in check get out of it?
        For all pieces on the board for the team in check, run all possible moves.
        After each one, run check for check. Still in check?  Keep going. end of 
        possible moves?  Checkmate.
        """
        possible_moves = []
        
        # Player has put their opponent in check. Iterate thorugh all squares 
        # on the board
        if player == "black" and self.is_in_check("red"):
            for row in self._board:
                for square in row:
                    mover = square

                    # For all pieces of the color in check, test all possible moves.
                    # If move is valid, put it in the list "possible_moves" as a 
                    # tuple "str_from, str_to"
                    if mover is not None and mover.get_color() == "red": 
                        str_from = mover.get_location()
                        current_col = ord(str_from[0]) - 97
                        current_row = int(str_from[1:]) - 1

                        for x in range(10):
                            for y in range(9):
                                new_row = x
                                new_col = y

                                if mover.is_valid_move(current_col, current_row, \
                                    new_col, new_row, self._board):
                                    str_from = str(chr(current_col + 97) + \
                                        str(current_row +1))
                                    str_to = str(chr(new_col + 97) + \
                                        str(new_row + 1))
                                    possible_moves.append((str_from, str_to))

            count = 0
            # Iterate through this list of possible moves, test them to see if 
            # they bring General out of check. 
            for str_from, str_to in possible_moves:
                
                current_col = ord(str_from[0]) - 97
                current_row = int(str_from[1:]) - 1
                new_col = ord(str_to[0]) - 97
                new_row = int(str_to[1:]) - 1
                mover = self._board[current_row][current_col]
                destination = self._board[new_row][new_col]

                # test the move, update piece locations as necessary
                self.the_move(str_from, str_to, mover)
                mover.set_location(str_to)

                if type(mover) is General:
                    self.update_general_pos(str_from, str_to)

                # test whether the move has brought the General out of check
                # then reverse the move and update piece locations
                self.check_for_check()
                if self.is_in_check("red"):
                    if type(mover) is General:
                        self.reverse_move(str_from, str_to, mover, destination)
                        mover.set_location(str_from)
                        self.update_general_pos(str_to, str_from)
                        continue
                    else:
                        #reverse move
                        self.reverse_move(str_from, str_to, mover, destination)
                        mover.set_location(str_from)
                        continue

                # This particular move has brought the General out of check,
                # therefore there is no checkmate.
                if self.is_in_check("red") == False:
                    count += 1
                    #reverse move and update General position
                    if type(mover) is General:
                        self.reverse_move(str_from, str_to, mover, destination)
                        mover.set_location(str_from)
                        self.update_general_pos(str_to, str_from)
                        return False
                    else:
                        #reverse move
                        self.reverse_move(str_from, str_to, mover, destination)
                        mover.set_location(str_from)
                        return False

            if count == 0:
                print("Checkmate!")
                self.set_game_state("BLACK_WINS")

        # Player has put their opponent in check. Iterate thorugh all squares 
        # on the board
        if player == "red" and self.is_in_check("black"):
            for row in self._board:
                for square in row:
                    mover = square

                    # For all pieces of the color in check, test all possible moves.
                    # If move is valid, put it in the list "possible_moves" as a 
                    # tuple "str_from, str_to"
                    if mover is not None and mover.get_color() == "black": 
                        str_from = mover.get_location()
                        current_col = ord(str_from[0]) - 97
                        current_row = int(str_from[1:]) - 1

                        for x in range(10):
                            for y in range(9):
                                new_row = x
                                new_col = y

                                if mover.is_valid_move(current_col, current_row, \
                                    new_col, new_row, self._board):
                                    
                                    str_from = str(chr(current_col + 97) + \
                                        str(current_row +1))
                                    str_to = str(chr(new_col + 97) + \
                                        str(new_row + 1))
                                    possible_moves.append((str_from, str_to))

            count = 0
            # Iterate through this list of possible moves, test them to see if 
            # they bring General out of check. 
            for str_from, str_to in possible_moves:

                current_col = ord(str_from[0]) - 97
                current_row = int(str_from[1:]) - 1
                new_col = ord(str_to[0]) - 97
                new_row = int(str_to[1:]) - 1
                
                mover = self._board[current_row][current_col]
                destination = self._board[new_row][new_col]

                # test the move to see if it will bring color out of check
                self.the_move(str_from, str_to, mover)
                mover.set_location(str_to)

                if type(mover) is General:
                    self.update_general_pos(str_from, str_to)

                # test whether the move has brought the General out of check
                # then reverse the move and update piece locations
                self.check_for_check()
                if self.is_in_check("black"):
                    #reverse move and update General position
                    if type(mover) is General:
                        self.reverse_move(str_from, str_to, mover, destination)
                        mover.set_location(str_from)
                        self.update_general_pos(str_to, str_from)
                        continue
                    else:
                        #reverse move
                        self.reverse_move(str_from, str_to, mover, destination)
                        mover.set_location(str_from)
                        continue

                # This particular move has brought the General out of check,
                # therefore there is no checkmate.
                if self.is_in_check("black") == False:
                    count += 1
                    #reverse move and update General position
                    if type(mover) is General:
                        self.reverse_move(str_from, str_to, mover, destination)
                        mover.set_location(str_from)
                        self.update_general_pos(str_to, str_from)
                        return False
                    else:
                        #reverse move
                        self.reverse_move(str_from, str_to, mover, destination)
                        mover.set_location(str_from)
                        return False

            if count == 0:
                print("Checkmate!")
                self.set_game_state("RED_WINS")

class GamePiece:
    """Create GamePiece class, which provides general rules for all pieces"""

    def __init__(self, color, location, piece_id):
        """Initializes data members for GamePiece class"""

        self._color = color
        self._location = location
        self._piece_id = piece_id

    def __repr__(self):
        """returns easily identifiable representation of piece object on board,
        including color.
        """
        
        if self._color == "red":
            return f"\u001b[31m{self._piece_id}\u001b[0m"

        if self._color == "black":
            return f"\u001b[30;1m{self._piece_id}\u001b[0m"

    def get_color(self):
        """returns value of color"""

        return self._color

    def get_location(self):
        """gets location of piece"""

        return self._location

    def set_location(self, new_location):
        """updates location of game piece"""

        self._location = new_location

    def fratricide_check(self, current_col, current_row, new_col, new_row, board):
        """tests move against general rules for all pieces. Returns true if move
        is successful, otherwise false. 
        """
        moving_piece = board[current_row][current_col]
        destination = board[new_row][new_col]

        # Prevents fratricide
        if destination is not None:
            if moving_piece.get_color() == destination.get_color():
                return True
        
class Chariot(GamePiece):
    """Creates Chariot sub-class"""
    
    def is_valid_move(self, current_col, current_row, new_col, new_row, board):
        
        if self.fratricide_check(current_col, current_row, new_col, new_row, board):
            return False

        move_delta_horizontal = abs(current_col - new_col)
        move_delta_vertical = abs(current_row - new_row)
        diagonal_move = abs(new_col - current_col) != 0 and abs(current_row - new_row) != 0

        if diagonal_move:
            return False

        # vertical block
        for x in range(1, move_delta_vertical):

            # if we are moving up vertically, then we check the values of x in 
            # the range of 1 to the end of the movement delta subtracted from the 
            # y coordinate. If any of them are other than None, there is a block,
            # so return False.
            if current_row >= new_row:
                if board[current_row - x][current_col] is not None:
                    #print("vertical block")
                    return False

            # if we are moving down vertically, we make the same check as above, 
            # except that we add the values of x to the y coordinate.
            else:
                if board[current_row + x][current_col] is not None:
                    #print("vertical block")
                    return False

        # horizontal block
        for y in range(1, move_delta_horizontal):

            # if we are moving left, we check the values of y from 1 to the end 
            # of the movement delta subtracted from the x coordinate. If any of 
            # them are other than None, there is a block, return False.
            if current_col > new_col:
                if board[current_row][current_col - y] is not None:
                    return False

            # if we are moving right, we make the same check as above, except that 
            # we add the values of y to the x coordinate.
            else:
                if board[current_row][current_col + y] is not None:
                    return False

        return True



class Horse(GamePiece):
    """Creates Horse sub-class"""

    def is_valid_move(self, current_col, current_row, new_col, new_row, board):
        
        if self.fratricide_check(current_col, current_row, new_col, new_row, board):
            return False

        # defines all valid options for the horse piece
        horse_move = (abs(new_row - current_row) == 2 and abs(new_col - current_col) == 1) or \
                     (abs(new_row - current_row) == 1 and abs(new_col - current_col) == 2)


        if not horse_move:
            return False

        # possible blocks
        if abs(new_row - current_row) == 2:
            # first square move up
            if current_row > new_row:
                if board[current_row - 1][current_col] is not None:
                    return False
            # first square move down
            if current_row < new_row:
                if board[current_row + 1][current_col] is not None:
                    return False

        if abs(new_row - current_row) == 1:
            # first square move left
            if current_col > new_col:
                if board[current_row][current_col - 1] is not None:
                    return False
            # first square move right
            if current_col < new_col:
                if board[current_row][current_col + 1] is not None:
                    return False

        return True

class Elephant(GamePiece):
    """Creates Elephant sub-class"""
    
    def is_valid_move(self, current_col, current_row, new_col, new_row, board):
        
        if self.fratricide_check(current_col, current_row, new_col, new_row, board):
            return False

        over_river = new_row > 4 and self._color == "red" or new_row < 5 and \
            self._color == "black"
        elephant_diagonal_move = abs(new_row - current_row) == 2 and \
            abs(new_col - current_col) == 2

        # Elephant cannot cross river. If desired square is over river, return False
        if over_river:
            return False

        #Elephant can only move two squares diagonally. Otherwise return False.
        if not elephant_diagonal_move:
            return False

        # "Blocking the elephant's eyes" （塞象眼）. Checks the four diagonal spaces 
        # immediately adjacent to the piece. If the one in the direction of travel is 
        # not empty, the elephant is blocked.  Return False.

        # move down and right
        if current_row < new_row and current_col < new_col:
            if board[current_row + 1][current_col + 1] is not None:
                return False

        # move down and left
        if current_row < new_row and current_col > new_col:
            if board[current_row + 1][current_col - 1] is not None:
                return False

        # move up and right
        if current_row > new_row and current_col < new_col:
            if board[current_row - 1][current_col + 1] is not None:
                return False

        # move up and left
        if current_row > new_row and current_col > new_col:
            if board[current_row - 1][current_col - 1] is not None:
                return False
        
        return True

class Adviser(GamePiece):
    """Creates Adviser sub-class"""
    
    def is_valid_move(self, current_col, current_row, new_col, new_row, board):
        
        if self.fratricide_check(current_col, current_row, new_col, new_row, board):
            return False

        diagonal_move = abs(new_col - current_col) != 0 and abs(current_row - new_row) != 0

        # Red Palace. For red Advisor, if desired square is not within palace 
        # boundaries, return False
        if self._color == "red":
            if new_row > 2 or new_col < 3 or new_col > 5:
                return False

        # Black Palace. For black Advisor, if desired square is not within palace 
        # boundaries, return False
        if self._color == "black":
            if new_row < 7 or new_col < 3 or new_col > 5:
                return False

        # Advisor must move diagonally. If not, return False.
        if not diagonal_move:
            return False

        # if move is greater than one space diagonally, return False
        if abs(new_row - current_row) > 1 or abs(new_col - current_col) > 1:
            return False

        return True

class General(GamePiece):
    """Creates General sub-class"""
    
    def is_valid_move(self, current_col, current_row, new_col, new_row, board):
        
        if self.fratricide_check(current_col, current_row, new_col, new_row, board):
            return False

        # Red Palace. For red General, if desired square is not within palace 
        # boundaries, return False
        if self._color == "red":
            if new_row > 2 or new_col < 3 or new_col > 5:
                return False

        # Black Palace. For black General, if desired square is not within palace 
        # boundaries, return False
        if self._color == "black":
            if new_row < 7 or new_col < 3 or new_col > 5:
                return False

        # If move is more than one space orthogonally, return False
        if abs(new_row - current_row) > 1 or abs(new_col - current_col) > 1:
            return False

        return True

class Cannon(GamePiece):
    """Creates Cannon sub-class"""
    
    def is_valid_move(self, current_col, current_row, new_col, new_row, board):
        
        if self.fratricide_check(current_col, current_row, new_col, new_row, board):
            return False

        destination = board[new_row][new_col]
        move_delta_vertical = abs(current_row - new_row)
        move_delta_horizontal = abs(current_col - new_col)
        diagonal_move = abs(new_row - current_row) != 0 and abs(current_col - new_col) != 0
        move_lst = []

        # Cannon cannot move diagonally. If desired square is diagonal, return False
        if diagonal_move:
            return False

        # Checking for blocks when destination is empty
        if destination is None:

            for x in range(1, move_delta_vertical):
                # if we are moving up, check to see if there are any pieces between 
                # moving piece and destination
                if current_row >= new_row:
                    if board[current_row - x][current_col] is not None:
                        return False

                # if we are moving down, we make the same check as above, except that 
                # we add the values of x to the y coordinate.
                else:
                    if board[current_row + x][current_col] is not None:
                        return False

            for y in range(1, move_delta_horizontal):

                # if we are moving left, we check the values of y from 1 to the 
                # end of the movement delta subtracted from the x coordinate. If 
                # any of them are other than "---", there is a block, return False.
                if current_col > new_col:
                    if board[current_row][current_col - y] is not None:
                        return False

                # if we are moving right, we make the same check as above, except 
                # that we add the values of y to the x coordinate.
                else:
                    if board[current_row][current_col + y] is not None:
                        return False

        # Captures. If the destination square is not empty, check for color, then 
        # "screen" requirement.
        if destination is not None:
            
            # if we are moving upwards
            if current_row > new_row:
                for x in range(1, move_delta_vertical):
                    # if there are other pieces in the path to the destination, 
                    # append them to list
                    if board[current_row - x][current_col] is not None:
                        move_lst.append(board[current_row - x][current_col])

                # if list length is not one, necessary "screen" rule fails, return False
                if len(move_lst) != 1:
                    return False

            # if we are moving downwards
            if current_row < new_row:
                for x in range(1, move_delta_vertical):
                    # if there are other pieces in the path to the destination, 
                    # append them to list
                    if board[current_row + x][current_col] is not None:
                        move_lst.append(board[current_row + x][current_col])

                # if list length is not one, necessary "screen" rule fails, return False
                if len(move_lst) != 1:
                    return False

            # if we are moving left
            if current_col > new_col:
                for y in range(1, move_delta_horizontal):
                    # if there are other pieces in the path to the destination, 
                    # append them to list
                    if board[current_row][current_col - y] is not None:
                        move_lst.append(board[current_row][current_col - y])

                # if list length is not one, necessary "screen" rule fails, return False
                if len(move_lst) != 1:
                    return False

            # if we are moving right
            if current_col < new_col:
                for y in range(1, move_delta_horizontal):
                    # if there are other pieces in the path to the destination, append them to list
                    if board[current_row][current_col + y] is not None:
                        move_lst.append(board[current_row][current_col + y])

                # if list length is not one, necessary "screen" rule fails, return False
                if len(move_lst) != 1:
                    return False

        return True

class Soldier(GamePiece):
    """Creates Soldier sub-class"""
    
    def is_valid_move(self, current_col, current_row, new_col, new_row, board):
        
        if self.fratricide_check(current_col, current_row, new_col, new_row, board):
            return False

        # sets variable for backwards move based on color
        backwards_move = new_row < current_row and self._color == "red" or new_row \
             > current_row and self._color == "black"

        # sets variable for diagonal move
        diagonal_move = abs(new_col - current_col) != 0 and abs(current_row - new_row) != 0

        # If soliders have crossed river 
        over_river = new_row > 4 and self._color == "red" or new_row < 5 and self._color == "black"

        # backwards and diagonal move always illegal for Soldiers, return False
        if backwards_move or diagonal_move:
            return False

        # if piece has crossed river, it gains ability to move one square horizontally
        if over_river:
            if abs(new_row - current_row) > 1 or abs(new_col - current_col) > 1:
                return False

        # if piece has not crossed river, it can only move one square vertically forward.
        else:
            if abs(new_row - current_row) > 1 or abs(new_col - current_col) != 0:
                return False

        return True

game = XiangqiGame()



# BLACK WINS
# print(game.make_move('h3','f3'))
# print(game.make_move('h8','f8'))
# print(game.make_move('e1','d2'))
# print(game.make_move('f8','e8'))
# print(game.make_move('d2','e2'))
# print(game.make_move('i7','i6'))
# print(game.make_move('f3','e3'))
# print(game.make_move('e8','e4'))
# print(game.make_move('e3','e7'))
# print(game.make_move('a10','a9'))
# print(game.make_move('e7','a7'))
# print(game.make_move('a9','d9'))
# print(game.make_move('e2','e1'))
# print(game.make_move('d9','d1'))
# print(game.make_move('e1','e2'))
# print(game.make_move('i10','i9'))
# print(game.make_move('i4','i5'))
# print(game.make_move('i9','h9'))
# print(game.make_move('i5','i6'))
# print(game.make_move('h9','h1'))
# print(game.make_move('i6','h6'))
# print(game.make_move('h1','i1'))
# print(game.make_move('h6','g6'))
# print(game.make_move('d1','c1'))
# print(game.make_move('g6','g7'))
# print(game.make_move('i1','g1'))
# print(game.make_move('g7','g8'))
# print(game.make_move('g1','f1'))
# print(game.make_move('a4','a5'))
# print(game.make_move('c1','b1'))
# print(game.make_move('a5','a6'))
# print(game.make_move('b1','a1'))
# print(game.make_move('g4','g5'))
# print(game.make_move('a1','a3'))
# print(game.make_move('g5','g6'))
# print(game.make_move('a3','b3'))
# print(game.make_move('g6','g7'))
# print(game.make_move('b3','d3'))
# print(game.make_move('g8','h8'))
# print(game.make_move('d3','d4'))
# print(game.make_move('h8','i8'))
# print(game.make_move('f1','f4'))
# print(game.make_move('i8','i9'))
# print(game.make_move('b8','e8')) #CM?

#RED CM
# game.make_move('a1','a2')
# game.make_move('a7','a6')
# game.make_move('i1','i2')
# game.make_move('i7','i6')
# game.make_move('a2','d2')
# game.make_move('g7','g6')
# game.make_move('i2','f2')
# game.make_move('a6','a5')
# game.make_move('e4','e5')
# game.make_move('a5','a4')
# game.make_move('b3','e3')
# game.make_move('a4','a3')
# game.make_move('e3','e7')
# game.make_move('i6','i5')
# game.make_move('e5','e6')
# game.make_move('i5','i4')
# game.make_move('a2','d2')
# game.make_move('e6','f6')
# game.make_move('i4','i3')
# game.make_move('f6','g6')
# game.make_move('i3','i2')
# game.make_move('h3','e3') #CM?




game9 = XiangqiGame()


game10 = XiangqiGame()
# Black is in Check
game10.make_move('h3','h5')
game10.make_move('i7','i6')
status = game10.make_move('h5','e5')
game10.is_in_check("black")       
print(status) 


print(game10.get_game_state())




game10.print_board()


