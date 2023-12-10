# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:35:19 2023

@author: codyi
"""

import os
import pytest
from Sprint_5_Final import SOSGame, SELECTED_MODE, save_game_state

# Define test cases for the save_game_state function
def test_save_game_state(tmpdir):
    # Create an instance of the SOSGame class
    game = SOSGame()

    # Set some sample game state for testing
    game.board = [['S', ' ', 'O'], ['S', 'O', 'S'], ['O', 'S', ' ']]
    game.current_player = 'Player 1'
    game.choices = {'Player 1': 'S', 'Player 2': 'O'}
    game.score = {'Player 1': 2, 'Player 2': 1}
    game.winner = 'Player 1'

    # Specify the filename for the test
    test_filename = os.path.join(tmpdir, 'test_game_state.txt')

    # Call the save_game_state function to save the game state to the test file
    save_game_state(game, test_filename)

    # Read the content of the saved file
    with open(test_filename, 'r') as file:
        saved_content = file.read()

    # Define the expected content based on the sample game state
    expected_content = f"Selected Game Mode: {SELECTED_MODE}\n"
    expected_content += "S   \nSOS\nOS  \n"
    expected_content += "Current Player: Player 1\n"
    expected_content += "Player 1's Choice: S\n"
    expected_content += "Player 2's Choice: O\n"
    expected_content += "Player 1's Score: 2\n"
    expected_content += "Player 2's Score: 1\n"
    expected_content += "Winner: Player 1\n"

    # Compare the saved content with the expected content
    assert saved_content == expected_content

# Run the tests
if __name__ == "__main__":
    pytest.main()