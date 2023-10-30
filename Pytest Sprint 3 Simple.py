# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 21:07:17 2023

@author: codyi
"""

from Sprint_3_Final import SOSGame 

# Constants
BOARD_SIZE = 3  # Adjust according to the game settings.
SELECTED_MODE = 'Simple'  # Modify as needed.

def test_initialize_game():
    game = SOSGame()
    assert game.current_player == 'Player 1'
    assert game.board == [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    assert game.choices == {'Player 1': None, 'Player 2': None}
    assert game.score == {'Player 1': 0, 'Player 2': 0}
    assert game.winner is None

def test_switch_player():
    game = SOSGame()
    assert game.current_player == 'Player 1'
    game.switch_player()
    assert game.current_player == 'Player 2'

def test_place_symbol():
    game = SOSGame()
    game.set_choice('Player 1', 'S')
    assert game.place_symbol(0, 0) == True
    assert game.board[0][0] == 'S'

def test_check_for_sos():
    game = SOSGame()

    # Horizontal
    game.board[0] = ['S', 'O', 'S']
    assert game.check_for_sos(0, 1) == (True, "horizontal")

    # Vertical
    game.board[0][2] = 'S'
    game.board[1][2] = 'O'
    game.board[2][2] = 'S'
    assert game.check_for_sos(1, 2) == (True, "vertical")

    # Diagonal Down Right
    game.board[0][0] = 'S'
    game.board[1][1] = 'O'
    game.board[2][2] = 'S'
    assert game.check_for_sos(1, 1) == (True, "diagonal_down_right")

    # Diagonal Down Left
    game.board[0][2] = 'S'
    game.board[1][1] = 'O'
    game.board[2][0] = 'S'
    assert game.check_for_sos(1, 1) == (True, "diagonal_down_left")

def test_board_is_full():
    game = SOSGame()
    assert game.board_is_full() == False

    game.board = [['S' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    assert game.board_is_full() == True

def test_simple_mode_winner():
    game = SOSGame()
    game.set_choice('Player 1', 'S')
    game.place_symbol(0, 0)
    game.set_choice('Player 1', 'O')
    game.place_symbol(0, 1)
    game.set_choice('Player 1', 'S')
    game.place_symbol(0, 2)
    assert game.winner == 'Player 1'