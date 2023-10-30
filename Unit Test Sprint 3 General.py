# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 21:14:35 2023

@author: codyi
"""

import unittest
from Sprint_3_Final import SOSGame

BOARD_SIZE = 3
SELECTED_MODE = "General"
WHITE, BLACK, RED, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 0, 255)
CELL_SIZE = 100
WIDTH, HEIGHT = 800, 600

class TestSOSGameGeneralMode(unittest.TestCase):

    def setUp(self):
        """Called before each test."""
        self.game = SOSGame()

    def test_initialization(self):
        self.assertEqual(self.game.current_player, 'Player 1')
        self.assertEqual(self.game.choices['Player 1'], None)
        self.assertEqual(self.game.choices['Player 2'], None)
        self.assertEqual(self.game.score['Player 1'], 0)
        self.assertEqual(self.game.score['Player 2'], 0)
        self.assertEqual(len(self.game.board), BOARD_SIZE)
        for row in self.game.board:
            for cell in row:
                self.assertEqual(cell, ' ')

    def test_set_and_get_choice(self):
        self.game.set_choice('Player 1', 'S')
        self.assertEqual(self.game.get_choice(), 'S')

    def test_switch_player(self):
        self.assertEqual(self.game.current_player, 'Player 1')
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'Player 2')
        self.game.switch_player()
        self.assertEqual(self.game.current_player, 'Player 1')

    def test_place_symbol_and_check_sos(self):
        self.game.set_choice('Player 1', 'S')
        self.game.place_symbol(0, 0)  # Placing S
        self.game.switch_player()
        self.game.set_choice('Player 2', 'O')
        self.game.place_symbol(0, 1)  # Placing O
        self.game.switch_player()
        self.game.set_choice('Player 1', 'S')
        self.game.place_symbol(0, 2)  # Placing S, completing SOS
        self.assertEqual(self.game.score['Player 1'], 1)

    def test_full_board(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if (row + col) % 2 == 0:
                    self.game.set_choice(self.game.current_player, 'S')
                else:
                    self.game.set_choice(self.game.current_player, 'O')
                self.game.place_symbol(row, col)
        self.assertTrue(self.game.board_is_full())

if __name__ == "__main__":
    unittest.main()