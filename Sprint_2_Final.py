# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:27:27 2023

@author: codyi
"""

import pygame
import sys

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
    global BOARD_SIZE, CELL_SIZE
    increase_button = Button(WIDTH // 2 + 50, HEIGHT // 2, 40, 40, "+", (100, 100, 100), (150, 150, 150))
    decrease_button = Button(WIDTH // 2 - 90, HEIGHT // 2, 40, 40, "-", (100, 100, 100), (150, 150, 150))
    start_button = Button(WIDTH // 2 - 70, HEIGHT // 2 + 50, 140, 50, "Start Game", (0, 128, 0), (0, 255, 0))
    
    # Radioboxes for game modes
    radio_simple = Radiobox(screen, WIDTH // 2 - 120, HEIGHT // 2 - 80, 5, caption='Simple')
    radio_general = Radiobox(screen, WIDTH // 2 + 20, HEIGHT // 2 - 80, 6, caption='General')
    game_modes = [radio_simple, radio_general]
    
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

        board_text = font.render(f"Board Size: {BOARD_SIZE}x{BOARD_SIZE}", True, BLACK)
        text_rect = board_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        screen.blit(board_text, text_rect)

        pygame.display.update()

# Constants
WIDTH, HEIGHT = 800, 600
BOARD_SIZE = 5
CELL_SIZE = (WIDTH - 300) // BOARD_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SELECTED_MODE = None

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SOS Game")
font = pygame.font.Font(None, 36)

class SOSGame:
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.current_player = 'Player 1'
        self.choices = {'Player 1': None, 'Player 2': None}

    def set_choice(self, player, choice):
        """Set player's choice."""
        self.choices[player] = choice

    def get_choice(self):
        """Get the choice for the current player."""
        return self.choices[self.current_player]

    def switch_player(self):
        self.current_player = 'Player 2' if self.current_player == 'Player 1' else 'Player 1'

    def place_symbol(self, row, col):
        symbol = self.get_choice()  
        if self.board[row][col] == ' ' and symbol:  
            self.board[row][col] = symbol
            self.switch_player()
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
                for option in player1_radioboxes:
                    option.update_radiobox(event)
                    if option.checked:
                        game.set_choice('Player 1', option.caption)
                        # Deactivate other radioboxes
                        for other_option in player1_radioboxes:
                            if other_option != option:
                                other_option.checked = False

                # Radiobox handling for Player 2
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
                    game.place_symbol(row, col)

        game.draw_board()
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