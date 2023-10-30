# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 21:07:17 2023

@author: codyi
"""

import unittest
from Sprint_3_Final import SOSGame

# Constants for our test
BOARD_SIZE = 3  # Example size for board
SELECTED_MODE = 'Simple'  # Example mode for the test

class TestSOSGame(unittest.TestCase):
    
    def setUp(self):
        self.game = SOSGame()

    def test_initial_state(self):
        self.assertEqual(self.game.current_player, 'Player 1')
        self.assertIsNone(self.game.choices['Player 1'])
        self.assertIsNone(self.game.choices['Player 2'])
        self.assertEqual(self.game.score['Player 1'], 0)
        self.assertEqual(self.game.score['Player 2'], 0)

    def test_set_choice(self):
        self.game.set_choice('Player 1', 'S')
        self.assertEqual(self.game.get_choice(), 'S')
        self.game.switch_player()
        self.game.set_choice('Player 2', 'O')
        self.assertEqual(self.game.get_choice(), 'O')

    def test_switch_player(self):
        self.assertEqual(self.game.current_player, 'Player 1')
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'Player 2')

    def test_place_symbol(self):
        self.game.set_choice('Player 1', 'S')
        self.assertTrue(self.game.place_symbol(0, 0))
        self.assertEqual(self.game.board[0][0], 'S')

    def test_check_for_sos(self):
        self.game.board[0][0] = 'S'
        self.game.board[0][1] = 'O'
        self.game.board[0][2] = 'S'
        self.assertTrue(self.game.check_for_sos(0, 0)[0])

    def test_board_is_full(self):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.game.board[i][j] = 'S'
        self.assertTrue(self.game.board_is_full())


if __name__ == '__main__':
    unittest.main()