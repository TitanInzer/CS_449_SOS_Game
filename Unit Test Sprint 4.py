# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:39:51 2023

@author: codyi
"""

import unittest
from unittest.mock import patch
from Sprint_4_Final import SOSGame, ai_move, perform_ai_move  # Replace 'your_game_file' with the name of your Python file

class TestAI(unittest.TestCase):
    def setUp(self):
        self.game = SOSGame()

    @patch('Sprint_4_Final.random.choice')
    def test_ai_move(self, mock_choice):
        # Mocking random.choice to return predetermined values
        mock_choice.side_effect = [(0, 0), 'S']
        row, col, symbol = ai_move(self.game.board)
        self.assertEqual((row, col, symbol), (0, 0, 'S'))

    @patch('Sprint_4_Final.random.choice')
    def test_perform_ai_move(self, mock_choice):
        # Mocking random.choice to return predetermined values
        mock_choice.side_effect = [(0, 0), 'S']
        perform_ai_move(self.game)
        self.assertEqual(self.game.board[0][0], 'S')

if __name__ == '__main__':
    unittest.main()