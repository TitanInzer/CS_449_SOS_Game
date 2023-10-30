# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 21:31:49 2023

@author: codyi
"""

from Sprint_2_Final import SOSGame

def test_board_size():
    game = SOSGame()
    game.BOARD_SIZE = 5
    assert len(game.board) == 5
    assert len(game.board[0]) == 5

def test_game_mode():
    game = SOSGame()
    game.game_mode = "simple"
    assert game.game_mode == "simple"

def test_initialize_board():
    game = SOSGame()
    game.BOARD_SIZE = 5
    game.initialize_board()  # Assuming you have a method to initialize the board in your SOSGame class
    for row in game.board:
        for cell in row:
            assert cell == ' '

def test_s_move():
    game = SOSGame()
    game.current_player = 'Player 1'
    game.player1_symbols = {'Player 1': 'S'}
    
    result = game.place_symbol(0, 0)
    assert result == True
    assert game.board[0][0] == 'S'

def test_o_move():
    game = SOSGame()
    game.current_player = 'Player 1'
    game.player1_symbols['Player 1'] = 'O'
    
    result = game.place_symbol(0, 1)
    assert result == True
    assert game.board[0][1] == 'O'
    
def test_invalid_move():
    game = SOSGame()
    game.current_player = 'Player 1'
    game.player1_symbols = {'Player 1': 'S'}
    
    # Placing an 'S' on 0,0 position
    game.place_symbol(0, 0)
    
    # Now trying to place an 'O' on the same spot
    game.player1_symbols['Player 1'] = 'O'
    result = game.place_symbol(0, 0)
    assert result == False