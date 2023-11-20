# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:01:46 2023

@author: codyi
"""

import pygame
import sys
import random

global IS_AI_GAME
IS_AI_GAME = False
global AI_PLAYER_NUMBER
AI_PLAYER_NUMBER = 1

# Constants
WIDTH, HEIGHT = 800, 600
BOARD_SIZE = 5
CELL_SIZE = (WIDTH - 300) // BOARD_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SELECTED_MODE = None

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SOS Game")
font = pygame.font.Font(None, 36)

class Radiobox:
    def __init__(self, surface, x, y, idnum, color=(230, 230, 230),
        caption="", outline_color=(0, 0, 0), check_color=(0, 0, 0),
        font_size=22, font_color=(0, 0, 0), 
    text_offset=(28, 1), font='Ariel Black'):
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.caption = caption
        self.oc = outline_color
        self.cc = check_color
        self.fs = font_size
        self.fc = font_color
        self.to = text_offset
        self.ft = font

        #identification for removal and reorginazation
        self.idnum = idnum

        # checkbox object
        self.radiobox_obj = pygame.Rect(self.x, self.y, 12, 12)
        self.radiobox_outline = self.radiobox_obj.copy()

        # variables to test the different states of the radiobox
        self.checked = False

    def _draw_button_text(self):
        self.font = pygame.font.SysFont(self.ft, self.fs)
        self.font_surf = self.font.render(self.caption, True, self.fc)
        w, h = self.font.size(self.caption)
        self.font_pos = (self.x + self.to[0], self.y + 12 / 2 - h / 2 + 
        self.to[1])
        self.surface.blit(self.font_surf, self.font_pos)

    def render_radiobox(self):
        if self.checked:
            pygame.draw.rect(self.surface, self.color, self.radiobox_obj)
            pygame.draw.rect(self.surface, self.oc, self.radiobox_outline, 1)
            pygame.draw.circle(self.surface, self.cc, (self.x + 6, self.y + 6), 4)

        elif not self.checked:
            pygame.draw.rect(self.surface, self.color, self.radiobox_obj)
            pygame.draw.rect(self.surface, self.oc, self.radiobox_outline, 1)
        self._draw_button_text()

    def _update(self, event_object):
        x, y = pygame.mouse.get_pos()
        px, py, w, h = self.radiobox_obj
        if px < x < px + w and py < y < py + w:
            if self.checked:
                self.checked = False
            else:
                self.checked = True

    def update_radiobox(self, event_object):
        if event_object.type == pygame.MOUSEBUTTONDOWN:
            self.click = True
            self._update(event_object)
            
class Button:
    def __init__(self, x, y, w, h, text, color, hover_color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.current_color = self.color
        
    def display(self, surface):
        pygame.draw.rect(surface, self.current_color, (self.x, self.y, self.w, self.h))
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=(self.x + self.w // 2, self.y + self.h // 2))
        surface.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.x < event.pos[0] < self.x + self.w and self.y < event.pos[1] < self.y + self.h:
                return True
        return False

    def update(self, event):
        if self.x < event.pos[0] < self.x + self.w and self.y < event.pos[1] < self.y + self.h:
            self.current_color = self.hover_color
        else:
            self.current_color = self.color

def select_board_size():
    global BOARD_SIZE, CELL_SIZE, SELECTED_MODE, IS_AI_GAME, AI_PLAYER_NUMBER
    increase_button = Button(WIDTH // 2 + 50, HEIGHT // 2, 40, 40, "+", (100, 100, 100), (150, 150, 150))
    decrease_button = Button(WIDTH // 2 - 90, HEIGHT // 2, 40, 40, "-", (100, 100, 100), (150, 150, 150))
    start_button = Button(WIDTH // 2 - 70, HEIGHT // 2 + 50, 140, 50, "Start Game", (0, 128, 0), (0, 255, 0))
    
    # Radioboxes for game modes
    radio_simple = Radiobox(screen, WIDTH // 2 - 120, HEIGHT // 2 - 80, 5, caption='Simple')
    radio_general = Radiobox(screen, WIDTH // 2 + 20, HEIGHT // 2 - 80, 6, caption='General')
    game_modes = [radio_simple, radio_general]
    radio_ai_player1 = Radiobox(screen, WIDTH // 2 - 160, HEIGHT // 2 + 150, 9, caption='AI as Player 1')
    radio_ai_player2 = Radiobox(screen, WIDTH // 2 + 60, HEIGHT // 2 + 150, 10, caption='AI as Player 2')
    ai_player_modes = [radio_ai_player1, radio_ai_player2]
    
    running = True
    while running:
        CELL_SIZE = (WIDTH - 300) // BOARD_SIZE  # This line recalculates CELL_SIZE
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if increase_button.is_clicked(event) and BOARD_SIZE < 9:
                    BOARD_SIZE += 1
                if decrease_button.is_clicked(event) and BOARD_SIZE > 3:
                    BOARD_SIZE -= 1
                if start_button.is_clicked(event):
                    if radio_simple.checked:
                        SELECTED_MODE = 'Simple'
                    elif radio_general.checked:
                        SELECTED_MODE = 'General'
                    running = False
                    
                # Update game modes radioboxes
                for option in game_modes:
                    option.update_radiobox(event)
                    if option.checked is True:
                        for r in game_modes:
                            if r != option:
                                r.checked = False
                            
                # Update AI player selection radioboxes
                for option in ai_player_modes:
                    option.update_radiobox(event)
                    if option.checked:
                        IS_AI_GAME = True
                        AI_PLAYER_NUMBER = 1 if option.caption == 'AI as Player 1' else 2
                        for r in ai_player_modes:
                            if r != option:
                                r.checked = False

            if event.type == pygame.MOUSEMOTION:
                increase_button.update(event)
                decrease_button.update(event)
                start_button.update(event)

        increase_button.display(screen)
        decrease_button.display(screen)
        start_button.display(screen)
        
        # Render game mode radios
        for radio in game_modes:
            radio.render_radiobox()
            
        # Render AI player selection radios
        for radio in ai_player_modes:
            radio.render_radiobox()

        board_text = font.render(f"Board Size: {BOARD_SIZE}x{BOARD_SIZE}", True, BLACK)
        text_rect = board_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        screen.blit(board_text, text_rect)

        pygame.display.update()

class SOSGame:
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = 'Player 1'
        self.choices = {'Player 1': None, 'Player 2': None}
        self.score = { 'Player 1' : 0, 'Player 2': 0}
        self.scored_position = set()
        self.winner = None

    def set_choice(self, player, choice):
        """Set player's choice."""
        self.choices[player] = choice

    def get_choice(self):
        """Get the choice for the current player."""
        return self.choices[self.current_player]

    def switch_player(self):
        self.current_player = 'Player 2' if self.current_player == 'Player 1' else 'Player 1'

    def place_symbol(self, row, col):
        # Add a validation check for row and col
        if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
            return False  # Exit the method if row or col is out of range
        symbol = self.get_choice()
        if self.board[row][col] == ' ' and symbol:
            self.board[row][col] = symbol
            # Print the board after placing the symbol
            self.draw_board()

            sos_made = False
            for i in range(-2, 3):  # adjust to check 2 squares around
                for j in range(-2, 3):
                    if 0 <= row + i < BOARD_SIZE and 0 <= col + j < BOARD_SIZE:
                        sos_found, direction = self.check_for_sos(row + i, col + j)
                        if sos_found and (row + i, col + j, direction) not in self.scored_position:
                            self.scored_position.add((row + i, col + j, direction))
                            print(f"{self.current_player} has made an SOS!")
                            self.score[self.current_player] += 1
                            sos_made = True


                        if SELECTED_MODE == 'Simple':
                            if self.score[self.current_player] > 0:
                                self.winner = self.current_player
                                return True
                            elif self.is_draw():
                                self.winner = 'Draw'
                                return True
                        
                        # Check for end game in General mode
                        if SELECTED_MODE == 'General':
                            if not sos_made: # If the player couldn't make a SOS, then check for winner
                                if self.board_is_full():
                                    if self.score['Player 1'] > self.score['Player 2']:
                                        self.winner = 'Player 1'
                                    elif self.score['Player 1'] < self.score['Player 2']:
                                        self.winner = 'Player 2'
                                    else:
                                        self.winner = 'Draw'

            return True
        return False
   
    def draw_board(self):
        screen.fill(WHITE)
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x = col * CELL_SIZE + 150
                y = row * CELL_SIZE + 50
                pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

                symbol = self.board[row][col]
                if symbol in ('S', 'O'):
                    text = font.render(symbol, True, BLACK)
                    text_rect = text.get_rect()
                    text_rect.center = (x + CELL_SIZE // 2, y + CELL_SIZE // 2)
                    screen.blit(text, text_rect)

                    # Drawing the SOS line
                    for r, c, direction in self.scored_position:
                        line_color = RED if self.current_player == "Player 1" else BLUE

                        # Define starting and ending points for the line
                        start_x, start_y = None, None
                        end_x, end_y = None, None

                        if direction == "horizontal" and row == r and c <= col < c + 3:
                            start_x, start_y = c * CELL_SIZE + 150, y + CELL_SIZE//2
                            end_x, end_y = (c + 3) * CELL_SIZE + 150, y + CELL_SIZE//2
                        elif direction == "vertical" and col == c and r <= row < r + 3:
                            start_x, start_y = x + CELL_SIZE//2, r * CELL_SIZE + 50
                            end_x, end_y = x + CELL_SIZE//2, (r + 3) * CELL_SIZE + 50
                        elif direction == "vertical_centered" and col == c and r - 1 <= row <= r + 1:
                            start_x, start_y = x + CELL_SIZE//2, y - CELL_SIZE
                            end_x, end_y = x + CELL_SIZE//2, y + CELL_SIZE
                        elif direction == "diagonal_down_right" and r <= row < r + 3 and c <= col < c + 3:
                            start_x, start_y = c * CELL_SIZE + 150, r * CELL_SIZE + 50
                            end_x, end_y = (c + 3) * CELL_SIZE + 150, (r + 3) * CELL_SIZE + 50
                        elif direction == "diagonal_down_left" and r <= row < r + 3 and c - 2 <= col <= c:
                            start_x, start_y = (c + 1) * CELL_SIZE + 150, r * CELL_SIZE + 50
                            end_x, end_y = (c - 2) * CELL_SIZE + 150, (r + 3) * CELL_SIZE + 50

                        # If starting and ending points are defined, draw the line
                        if start_x is not None and start_y is not None and end_x is not None and end_y is not None:
                            pygame.draw.line(screen, line_color, (start_x, start_y), (end_x, end_y), 3)


    def draw_game_mode(self):
        if SELECTED_MODE:
            game_mode_text = font.render(f"Game Mode: {SELECTED_MODE}", True, BLACK)
            screen.blit(game_mode_text, (10, 10))  # Adjust the (10, 10) for your desired position.
            
    def check_win(self, row, col, symbol):
        """Check if placing a symbol on a given position wins the game."""
        if SELECTED_MODE == "Simple":
            return self.simple_win_check(row, col, symbol)
        elif SELECTED_MODE == "General":
            return self.general_win_check(row, col, symbol)
        return 0
    
    def display_scores(self):
        player1_score_text = font.render(f"Player 1 Score: {self.score['Player 1']}", True, BLACK)
        screen.blit(player1_score_text, (10, HEIGHT - 40))

        player2_score_text = font.render(f"Player 2 Score: {self.score['Player 2']}", True, BLACK)
        screen.blit(player2_score_text, (WIDTH - 200, HEIGHT - 40))
        
    def check_for_sos(self, row, col):
        # Horizontal check
        if col < BOARD_SIZE - 2 and self.board[row][col] == 'S' and self.board[row][col + 1] == 'O' and self.board[row][col + 2] == 'S':
            return True, "horizontal"

        # Vertical check
        # This will check for any pattern starting with an S and ending with an S
        if row <= BOARD_SIZE - 3:
            if self.board[row][col] == 'S' and self.board[row + 1][col] == 'O' and self.board[row + 2][col] == 'S':
                return True, "vertical"
        # This will check for any pattern centered around an O
        if 0 < row < BOARD_SIZE - 1:
            if self.board[row - 1][col] == 'S' and self.board[row][col] == 'O' and self.board[row + 1][col] == 'S':
                return True, "vertical_centered"

        # Diagonal check (top-left to bottom-right)
        if row < BOARD_SIZE - 2 and col < BOARD_SIZE - 2 and self.board[row][col] == 'S' and self.board[row + 1][col + 1] == 'O' and self.board[row + 2][col + 2] == 'S':
            return True, "diagonal_down_right"

        # Diagonal check (top-right to bottom-left)
        if row < BOARD_SIZE - 2 and col > 1 and self.board[row][col] == 'S' and self.board[row + 1][col - 1] == 'O' and self.board[row + 2][col - 2] == 'S':
            return True, "diagonal_down_left"

        return False, None
    
    def board_is_full(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True
    
    def is_draw(self):
        if SELECTED_MODE == 'Simple':
            return self.board_is_full() and self.winner is None
        elif SELECTED_MODE == 'General':
            return self.board_is_full()
    
    def display_draw_message(self):
        """Display the draw message."""
        message = "It's a Draw!"
        text_surface = font.render(message, True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, 30))
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)  # Wait for 2 seconds before proceeding

    def display_winner_message(self, winner):
        """Display the winner message."""
        if winner == 'Draw':
            message = "It's a Draw!"
        else:
            message = f"{winner} Wins!"
        text_surface = font.render(message, True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, 30))
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)  # Wait for 2 seconds before proceeding


def create_radioboxes():
  player1_title = font.render("Player 1", True, BLACK)
  player2_title = font.render("Player 2", True, BLACK)

  player1_radioboxes = []
  radio_s1 = Radiobox(screen, 10 + 50, HEIGHT // 4 + 50, 1, caption='S')
  radio_o1 = Radiobox(screen, 10 + 50, HEIGHT // 4 + 100, 2, caption='O')
  player1_radioboxes.append(radio_s1)
  player1_radioboxes.append(radio_o1)

  player2_radioboxes = []
  radio_s2 = Radiobox(screen, WIDTH - 40 - 55, HEIGHT // 4 + 50, 3, caption='S')
  radio_o2 = Radiobox(screen, WIDTH - 40 - 55, HEIGHT // 4 + 100, 4, caption='O')
  player2_radioboxes.append(radio_s2)
  player2_radioboxes.append(radio_o2)

  return player1_title, player1_radioboxes, player2_title, player2_radioboxes

def display_current_player_turn(current_player):
  turn_text = font.render(f"Current Player: {current_player[-1]}", True, BLACK)
  text_rect = turn_text.get_rect()
  text_rect.center = (WIDTH // 2, HEIGHT - 20)
  screen.blit(turn_text, text_rect)
  
def ai_move(board):
    empty_cells = [(i, j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == ' ']
    if empty_cells:
        row, col = random.choice(empty_cells)
        symbol = random.choice(['S', 'O'])
        return row, col, symbol
    return None, None, None 

def perform_ai_move(game):
    row, col, ai_symbol = ai_move(game.board)
    if row is not None and col is not None:
        ai_player = f'Player {AI_PLAYER_NUMBER}'
        game.set_choice(ai_player, ai_symbol)
        if game.place_symbol(row, col):
            game.switch_player()
            
def prompt_restart():
    restart_button = Button(WIDTH // 2 - 70, HEIGHT // 2 + 50, 140, 50, "Restart Game", (0, 128, 0), (0, 255, 0))
    while True:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.is_clicked(event):
                    return True  # Indicates the player wants to restart the game
            if event.type == pygame.MOUSEMOTION:
                restart_button.update(event)

        restart_button.display(screen)
        pygame.display.update()
  
def main():
    select_board_size()  # <-- Call the function at the start of the game
    game = SOSGame()
    print(f"Selected Game Mode: {SELECTED_MODE}") 
    player1_title, player1_radioboxes, player2_title, player2_radioboxes = create_radioboxes()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Radiobox handling for Player 1
                if not IS_AI_GAME or AI_PLAYER_NUMBER != 1:
                    for option in player1_radioboxes:
                        option.update_radiobox(event)
                        if option.checked:
                            game.set_choice('Player 1', option.caption)
                            # Deactivate other radioboxes
                            for other_option in player1_radioboxes:
                                if other_option != option:
                                    other_option.checked = False

                # Radiobox handling for Player 2
                if not IS_AI_GAME or AI_PLAYER_NUMBER != 2:
                    for option in player2_radioboxes:
                        option.update_radiobox(event)
                        if option.checked:
                            game.set_choice('Player 2', option.caption)
                            # Deactivate other radioboxes
                            for other_option in player2_radioboxes:
                                if other_option != option:
                                    other_option.checked = False

                # Board cell click handling
                x, y = pygame.mouse.get_pos()
                col, row = (x - 150) // CELL_SIZE, (y - 50) // CELL_SIZE
                if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                    if (game.current_player == 'Player 1' and not (IS_AI_GAME and AI_PLAYER_NUMBER == 1)) or \
                       (game.current_player == 'Player 2' and not (IS_AI_GAME and AI_PLAYER_NUMBER == 2)):
                        if game.place_symbol(row, col):
                            game.switch_player()
                            pygame.time.wait(500)
                            
        if not IS_AI_GAME and game.current_player == 'Player 2':
            # Code to handle Player 2's turn
            if game.place_symbol(row, col):
                game.switch_player()
                pygame.time.wait(500)
                    
        if IS_AI_GAME and game.current_player == f'Player {AI_PLAYER_NUMBER}':
            pygame.time.wait(500)  # Add delay for AI move
            perform_ai_move(game)
            
                    
        if game.is_draw() or game.winner:
            if game.winner == 'Draw':
                game.display_draw_message()
            else:
                game.display_winner_message(game.winner)
                
            if prompt_restart():
                # Reset the game state and select a new board size
                select_board_size()
                game = SOSGame()
                player1_title, player1_radioboxes, player2_title, player2_radioboxes = create_radioboxes()
                continue

        game.draw_board()
        game.draw_game_mode()
        game.display_scores()
        # Player 1 Title on Game Board
        player1_title_width = player1_title.get_width()
        player1_x = (WIDTH / 3 - player1_title_width) / 2 - 55
        screen.blit(player1_title, (player1_x, HEIGHT // 4))
        # Player 2 Title on Game Board
        player2_title_width = player2_title.get_width()
        player2_x = 2 * WIDTH / 3 + (WIDTH / 3 - player2_title_width) / 2 + 55
        screen.blit(player2_title, (player2_x, HEIGHT // 4))
        # Render for the Radioboxes
        for radio in player1_radioboxes + player2_radioboxes:
            radio.render_radiobox()
        display_current_player_turn(game.current_player)
        pygame.display.update()

if __name__ == "__main__":
    main()