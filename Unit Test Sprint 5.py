# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:34:52 2023

@author: codyi
"""

import unittest
from unittest.mock import mock_open, patch

# Import the function to be tested
from Sprint_5_Final import save_game_state

class TestSaveGameState(unittest.TestCase):

    def test_save_game_state(self):
        # Mock the built-in `open` function to capture file writes
        mock_file_content = []
        def mock_write(file, content):
            mock_file_content.append(content)

        with patch('builtins.open', mock_open(), create=True) as mock_file:
            mock_file.return_value.write = mock_write

            # Call the function with sample data
            game_state = {
                'Selected Game Mode': 'Simple',
                'Board State': [
                    [' ', ' ', ' '],
                    [' ', ' ', ' '],
                    [' ', ' ', ' ']
                ],
                'Current Player': 'Player 1',
                'Player 1 Choice': 'S',
                'Player 2 Choice': 'O',
                'Player 1 Score': 0,
                'Player 2 Score': 0,
                'Winner': None
            }
            save_game_state(game_state, 'test_game_state.txt')

            # Verify that the function opened the file and wrote the expected content
            expected_content = [
                'Selected Game Mode: Simple\n',
                'Board State: \n',
                '  |  |  \n',
                '---------\n',
                '  |  |  \n',
                '---------\n',
                '  |  |  \n',
                'Current Player: Player 1\n',
                'Player 1 Choice: S\n',
                'Player 2 Choice: O\n',
                'Player 1 Score: 0\n',
                'Player 2 Score: 0\n',
                'Winner: None\n'
            ]
            self.assertEqual(mock_file_content, expected_content)

if __name__ == '__main__':
    unittest.main()