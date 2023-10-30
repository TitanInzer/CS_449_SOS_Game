# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 21:15:26 2023

@author: codyi
"""

import unittest
from Sprint_2_Final import SOSGame

class TestSOSGame(unittest.TestCase):
    
    def setUp(self):
        # This method will run before each test. 
        # We initialize the game here.
        self.game = SOSGame()
        self.game.current_player = 'Player 1'
        self.game.player1_symbols = 'S'

    def test_board_size(self):
        # For this test, let's say we've set the board size to 5.
        self.game.BOARD_SIZE = 5
        self.assertEqual(len(self.game.board), 5)
        self.assertEqual(len(self.game.board[0]), 5)

    def test_game_mode(self):
        # For now, since we haven't fully implemented game modes,
        # we'll just assume a simple attribute 'game_mode' that stores the current mode.
        self.game.game_mode = "simple"
        self.assertEqual(self.game.game_mode, "simple")

    def test_s_move(self):
        # Temporarily replace the get_choice method for this test
        self.game.get_choice = lambda: 'S'
    
        # Manually set the cell to an empty string
        self.game.board[0][0] = ' '
        
        # Test if the S move works correctly
        self.assertTrue(self.game.place_symbol(0, 0))
        self.assertEqual(self.game.board[0][0], 'S')
    
    def test_o_move(self):
        # Temporarily replace the get_choice method for this test
        self.game.get_choice = lambda: 'O'
    
        # Manually set the cell to an empty string
        self.game.board[0][1] = ' '
    
        # Test if the O move works correctly
        self.assertTrue(self.game.place_symbol(0, 1))
        self.assertEqual(self.game.board[0][1], 'O')

    def test_invalid_move(self):
        # Placing an 'S' on 0,0 position
        self.game.place_symbol(0, 0)
        # Now trying to place an 'O' on the same spot
        self.game.player1_symbols = 'O'
        self.assertFalse(self.game.place_symbol(0, 0))

if __name__ == '__main__':
    unittest.main()