# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:39:51 2023

@author: codyi
"""

import pytest
from Sprint_4_Final import SOSGame, ai_move, perform_ai_move

@pytest.fixture
def game():
    return SOSGame()

def test_ai_move(game, mocker):
    # Mocking random.choice to return predetermined values
    mocker.patch('Sprint_4_Final.random.choice', side_effect=[(0, 0), 'S'])
    row, col, symbol = ai_move(game.board)
    assert (row, col, symbol) == (0, 0, 'S')

def test_perform_ai_move(game, mocker):
    # Mocking random.choice to return predetermined values
    mocker.patch('Sprint_4_Final.random.choice', side_effect=[(0, 0), 'S'])
    perform_ai_move(game)
    assert game.board[0][0] == 'S'