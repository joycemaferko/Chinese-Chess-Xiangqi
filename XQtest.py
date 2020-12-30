import unittest
from xiangQi import XiangqiGame, GamePiece



class xiangQi_test(unittest.TestCase):
    """
    Tests for Chinese Chess (XiangQi)
    """

    def test_soldier(self):
        """Tests movement of soldier gamepiece"""
        
        game =  XiangqiGame()

        # Valid move down, near side of river
        move = game.make_move('a4','a5')
        self.assertTrue(move)

        # Valid move up, near side of river
        move = game.make_move('c7', 'c6')
        self.assertTrue(move)

        # Valid move right, far side of river
        game.make_move('a4','a5')
        game.make_move('c7', 'c6')
        game.make_move('a5','a6')
        game.make_move('c6', 'c5')
        move = game.make_move('a6', 'b6')
        self.assertTrue(move)

        # Valid move left, far side of river
        game.make_move('a4','a5')
        game.make_move('c7', 'c6')
        game.make_move('a5','a6')
        game.make_move('c6', 'c5')
        game.make_move('a6', 'b6')
        move = game.make_move('c5','b5')
        self.assertTrue(move)

        # Valid capture
        game.make_move('a4','a5')
        game.make_move('c7', 'c6')
        game.make_move('a5','a6')
        game.make_move('c6', 'c5')
        game.make_move('a6', 'b6')
        game.make_move('c5','b5')
        game.make_move('e4','e5')
        game.make_move('b5','c5')
        move = game.make_move('c4','c5')
        piece = game._board[4][2]
        self.assertTrue(move)
        self.assertEqual(repr(piece), "\u001b[31mr S\u001b[0m")

        # Invalid move backwards
        move = game.make_move('e7','e8')
        self.assertFalse(move)

        # Invalid move diagonal
        move = game.make_move('e7','f6')
        self.assertFalse(move)

    def test_adviser(self):
        """Tests movement of adviser gamepiece"""

        game2 = XiangqiGame()

        # Valid move down/right
        move = game2.make_move('d1','e2')
        self.assertTrue(move)  

        # Valid move up/right
        move = game2.make_move('d10','e9')
        self.assertTrue(move)  

        # Valid move up/left
        move = game2.make_move('e2','d1')
        self.assertTrue(move) 

        # Valid move down/left
        move = game2.make_move('e9','d10')
        self.assertTrue(move) 

        # Invalid move down/left 
        move = game2.make_move('f1','d3')
        self.assertFalse(move) 

        # Invalid move down
        move = game2.make_move('f1','f2')
        self.assertFalse(move) 

    def test_genenral(self):
        """Tests movement of general gamepiece"""

        game3 = XiangqiGame()

        # Valid move down
        move = game3.make_move('e1','e2')
        self.assertTrue(move)

        # Valid move up
        move = game3.make_move('e10','e9')
        self.assertTrue(move)

        # Valid move diagonal
        move = game3.make_move('e2','f3')
        self.assertTrue(move)

        # Valid move diagonal
        move = game3.make_move('e9','d8')
        self.assertTrue(move)

        # Invalid move (too many spaces)
        move = game3.make_move('f3','d3')
        self.assertFalse(move)

        # Invalid move (out of palace)
        move = game3.make_move('f3','g3')
        self.assertFalse(move)

    def test_elephant(self):
        """Tests movement of elephant gamepiece"""

        game4 = XiangqiGame()

        # Valid capture
        game4.make_move('a1','a2')
        game4.make_move('a7','a6')
        game4.make_move('i1','i2')
        game4.make_move('i7','i6')
        game4.make_move('a2','d2')
        game4.make_move('g7','g6')
        game4.make_move('i2','f2')
        game4.make_move('a6','a5')
        game4.make_move('e4','e5')
        game4.make_move('a10','a6')
        game4.make_move('h3','i3')
        game4.make_move('a5','a4')
        game4.make_move('i3','i6')
        game4.make_move('a4','a3')
        game4.make_move('i6','i8')
        move = game4.make_move('g10','i8')  
        piece = game4._board[7][8]
        self.assertTrue(move)
        self.assertEqual(repr(piece), "\u001b[30;1mb E\u001b[0m")

        # Valid move down/right
        move = game4.make_move('g1','i3')
        self.assertTrue(move)

        # Valid move up/left
        move = game4.make_move('c10','a8')
        self.assertTrue(move)
        
        # Invalid move (blocked)
        move = game4.make_move('c1','e3')
        self.assertFalse(move)

        # Invalid move (blocked)
        move = game4.make_move('g1','e3')
        self.assertFalse(move)

        # Invalid move (blocked)
        move = game4.make_move('c1','e3')
        self.assertFalse(move)

        # Invalid move (blocked)
        game4.make_move('g4','g5')
        game4.make_move('b8','b9')
        game4.make_move('i4','i5')
        move = game4.make_move('c10','a8')
        self.assertFalse(move)

        # Invalid move (elephant cannot cross river)
        game4.make_move('g6','g5')
        game4.make_move('e1','e2')
        game4.make_move('i8','g6')
        game4.make_move('e2','e3')
        move = game4.make_move('g6','i4')
        self.assertFalse(move)

        # Invalid move (elephant cannot cross river)
        game4.make_move('h8','h7')
        game4.make_move('c1', 'a3')
        game4.make_move('h7','h6')
        game4.make_move('a3','c5')
        game4.make_move('h6','h5')
        move = game4.make_move('c5','a7')
        self.assertFalse(move)

       
    def test_horse(self):
        """Tests movement of horse gamepiece"""

        game5 = XiangqiGame()

        # Valid move down/left
        move = game5.make_move('h1','g3')
        self.assertTrue(move)

        # Valid move up/left
        move = game5.make_move('h10','g8')
        self.assertTrue(move)

        # Valid move down/right
        move = game5.make_move('b1','c3')
        self.assertTrue(move)

        # Valid move up/right
        move = game5.make_move('b10','c8')
        self.assertTrue(move)

        # Invalid move (blocked)
        move = game5.make_move('g3','h5')
        self.assertFalse(move)

        # Invalid move (blocked)
        move = game5.make_move('c3','b5')
        self.assertFalse(move)

        # Invalid move (blocked)
        game5.make_move('c3','b1')
        move = game5.make_move('g8','f6')
        self.assertFalse(move)

        # Invalid move (blocked)
        move = game5.make_move('c8','b6')
        self.assertFalse(move)

        # Valid move (capture)
        game6 = XiangqiGame()
        game6.make_move('i1','i2')
        game6.make_move('h8','f8')
        game6.make_move('i2','i3')
        game6.make_move('f8','f3')
        game6.make_move('i4','i5')
        game6.make_move('f3','g3')
        move = game6.make_move('h1','g3')
        piece = game6._board[2][6]
        self.assertTrue(move)
        self.assertEqual(repr(piece), "\u001b[31mr H\u001b[0m")

    def test_chariot(self):
        """Tests movement of horse gamepiece"""

        game7 = XiangqiGame()

        # Valid move down
        move = game7.make_move('i1','i2')
        self.assertTrue(move)

        # Valid move up
        move = game7.make_move('a10','a9')
        self.assertTrue(move)

        # Valid move left
        move = game7.make_move('i2','f2')
        self.assertTrue(move)

        # Valid move right
        move = game7.make_move('a9','d9')
        self.assertTrue(move)

        # Valid move (capture)
        game7.make_move('f2','f7')
        game7.make_move('d9','d8')
        move = game7.make_move('f7', 'g7')
        piece = game7._board[6][6]
        self.assertTrue(move)
        self.assertEqual(repr(piece), "\u001b[31mr R\u001b[0m")
        
        game8 = XiangqiGame()

        # Invalid move (blocked)
        move = game8.make_move('i1','i5')
        self.assertFalse(move)

        # Invalid move (blocked)
        game8.make_move('i1','i2')
        move = game8.make_move('a10','a6')
        self.assertFalse(move)

        # Invalid move (blocked)
        game8.make_move('a10','a8')
        game8.make_move('i4','i5')
        move = game8.make_move('a8','c8')
        self.assertFalse(move)

    def test_cannon(self):
        """Tests movement of cannon gamepiece"""

        game9 = XiangqiGame()

        # Valid move down
        move = game9.make_move('h3','h5')
        self.assertTrue(move)

        # Valid move up
        move = game9.make_move('b8','b6')
        self.assertTrue(move)

        # Valid move left
        move = game9.make_move('h5','f5')
        self.assertTrue(move)

        # Valid move right
        move = game9.make_move('h8','i8')
        self.assertTrue(move)

        # Valid move (capture)
        move = game9.make_move('b3','b10')
        piece = game9._board[9][1]
        self.assertTrue(move)
        self.assertEqual(repr(piece), "\u001b[31mr C\u001b[0m")

        # Invalid move (diagonal)
        move = game9.make_move('i8','h9')
        self.assertFalse(move)

        # Invalid move (blocked)
        move = game9.make_move('i8','i6')
        self.assertFalse(move)

        # Invalid move (illegal capture)
        move = game9.make_move('i8','i1')
        self.assertFalse(move)

        # Invalid move (blocked)
        game9.make_move('g10','e8')
        game9.make_move('e4','e5')
        move = game9.make_move('i8','d8')
        self.assertFalse(move)

    def test_check(self):
        """Tests whether color is in check"""

        game10 = XiangqiGame()

        # Black is in Check
        game10.make_move('h3','h5')
        game10.make_move('i7','i6')
        game10.make_move('h5','e5')
        status = game10.check_for_check()
        self.assertTrue(status)

        # Black moves out of check
        game10.make_move('e10','f9')
        status = game10.check_for_check()
        self.assertFalse(status)

        # Black back in check
        game10.make_move('e5','f5')
        game10.make_move('f9','e10')
        game10.make_move('f5','e5')
        status = game10.check_for_check()
        self.assertTrue(status)

        # Black moves out of check with a block
        game10.make_move('c10','e8')
        status = game10.check_for_check()
        self.assertFalse(status)



if __name__ == '__main__':    
    unittest.main()





        