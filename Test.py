# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:28:19 2023

@author: codyi
"""

import pygame
import button


pygame.init()

# Classes
class Checkbox:
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
        self.checkbox_obj = pygame.Rect(self.x, self.y, 12, 12)
        self.checkbox_outline = self.checkbox_obj.copy()

        # variables to test the different states of the checkbox
        self.checked = False

    def _draw_button_text(self):
        self.font = pygame.font.SysFont(self.ft, self.fs)
        self.font_surf = self.font.render(self.caption, True, self.fc)
        w, h = self.font.size(self.caption)
        self.font_pos = (self.x + self.to[0], self.y + 12 / 2 - h / 2 + 
        self.to[1])
        self.surface.blit(self.font_surf, self.font_pos)

    def render_checkbox(self):
        if self.checked:
            pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
            pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
            pygame.draw.circle(self.surface, (255, 0, 255), (self.x + 6, self.y + 6), 4)

        elif not self.checked:
            pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
            pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
        self._draw_button_text()

    def _update(self, event_object):
        x, y = pygame.mouse.get_pos()
        px, py, w, h = self.checkbox_obj
        if px < x < px + w and py < y < py + w:
            if self.checked:
                self.checked = False
            else:
                self.checked = True

    def update_checkbox(self, event_object):
        if event_object.type == pygame.MOUSEBUTTONDOWN:
            self.click = True
            self._update(event_object)
            
            
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

# Game Window
screen_width = 800
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Test')


# Variables
game_menu = False

# Fonts
font = pygame.font.SysFont("Times New Roman", 40)

# Colors
TEXT_COL = (255, 255, 255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    
radioboxes = []
option = Radiobox(screen, 200, 200, 0, caption = 'Option 1')
option2 = Radiobox(screen, 200, 250, 1, caption = 'Option 2')
option3 = Radiobox(screen, 200, 300, 2, caption = 'Option 3')
radioboxes.append(option)
radioboxes.append(option2)
radioboxes.append(option3)

radioboxes_2 = []
option4 = Radiobox(screen, 400, 250, 0, caption = 'Option 4')
option5 = Radiobox(screen, 400, 300, 1, caption = 'Option 5')
option6 = Radiobox(screen, 400, 350, 2, caption = 'Option 6')
radioboxes_2.append(option4)
radioboxes_2.append(option5)
radioboxes_2.append(option6)

checkboxes = []
box1 = Checkbox(screen, 400, 200, 0, caption = 'Check Here')
checkboxes.append(box1)


run = True
while run:
    
    screen.fill((52,78,91))
    
    # Check if Menu is up
    if game_menu == True:
       pygame.draw.line(screen, (255, 255, 255), (0, 100), (800, 100), 10)
       for option in radioboxes:
           option.render_radiobox()
       for option in radioboxes_2:
           option.render_radiobox()
       for box in checkboxes:
           box.render_checkbox()
    else:
        draw_text("Press Escape to Bring Up Menu", font, TEXT_COL, 150, 150)
    
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_menu = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for option in radioboxes:
                option.update_radiobox(event)
                if option.checked is True:
                    for r in radioboxes:
                        if r != option:
                            r.checked = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for option in radioboxes_2:
                option.update_radiobox(event)
                if option.checked is True:
                    for r2 in radioboxes_2:
                        if r2 != option:
                            r2.checked = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in checkboxes:
                box.update_checkbox(event)
                if box.checked is True:
                    for c in checkboxes:
                        if c != box:
                            c.checked = False
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
            
            
pygame.quit()