# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 21:14:32 2023

@author: codyi
"""

from Sprint_3_Final import SOSGame 

BOARD_SIZE = 5  # For example
SELECTED_MODE = 'General'

def test_player_switching():
    game = SOSGame()
    current_player = game.current_player
    game.switch_player()
    assert game.current_player != current_player

def test_initial_board_empty():
    game = SOSGame()
    for row in game.board:
        for cell in row:
            assert cell == ' '

def test_place_symbol():
    game = SOSGame()
    game.set_choice('Player 1', 'S')
    assert game.place_symbol(0, 0) == True
    assert game.board[0][0] == 'S'

def test_sos_detection_horizontal():
    game = SOSGame()
    game.set_choice('Player 1', 'S')
    game.place_symbol(0, 0)
    game.set_choice('Player 1', 'O')
    game.place_symbol(0, 1)
    game.set_choice('Player 1', 'S')
    game.place_symbol(0, 2)
    assert game.check_for_sos(0, 1) == (True, "horizontal")

def test_sos_detection_vertical():
    game = SOSGame()
    game.set_choice('Player 1', 'S')
    game.place_symbol(0, 0)
    game.set_choice('Player 1', 'O')
    game.place_symbol(1, 0)
    game.set_choice('Player 1', 'S')
    game.place_symbol(2, 0)
    assert game.check_for_sos(1, 0) == (True, "vertical")

def test_board_is_full_false():
    game = SOSGame()
    assert game.board_is_full() == False

def test_board_is_full_true():
    game = SOSGame()
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            game.board[row][col] = 'S'
    assert game.board_is_full() == True

def test_winner_in_general_mode():
    game = SOSGame()
    # Place symbols to form SOS for Player 1
    game.set_choice('Player 1', 'S')
    game.place_symbol(0, 0)
    game.set_choice('Player 1', 'O')
    game.place_symbol(0, 1)
    game.set_choice('Player 1', 'S')
    game.place_symbol(0, 2)
    # Fill the board so it's full
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if game.board[row][col] == ' ':
                game.board[row][col] = 'S'
    assert game.board_is_full() == True
    assert game.winner == 'Player 1'

def test_draw_in_general_mode():
    game = SOSGame()
    # Fill the board so it's full without forming SOS
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            game.board[row][col] = 'S'
    assert game.board_is_full() == True
    assert game.is_draw() == True
    assert game.winner == 'Draw'