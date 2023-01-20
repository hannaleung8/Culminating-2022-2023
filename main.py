"""
Header
Name: Hanna
Date: Jan 20 2022
Class: Gr 11 Computer Tech
Program: Culminating
Purpose: 
"""
# imports pygame module
# import colour code file
# import single 15 ball file as s15
# import database file as d

import pygame
import colour_codes as cc
import single15ball as s15
import database as d
import LeaderboardScreen as l

# initializes all imported pygame modules
pygame.init()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 





# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# creates screen size, header, and colour
wid = 660
heig = 400
display = pygame.display.set_mode((wid, heig))
pygame.display.set_caption("Pool ball")
display.fill(cc.background2)
pygame.display.flip()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# font objects
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 16)

# button size
button_rect = pygame.Rect(100, 150, 100, 50)
button_rect2 = pygame.Rect(400, 150, 100, 50)

# text rendering
title = font.render("Pool Ball Menu", True, (cc.black))
credit = font2.render("By: Hanna Leung", True, (cc.black))
b_s15_text = font.render("Practice", True, (cc.white))
b_database_text = font.render("Podium", True, (cc.white))

# blit the text onto the screen
display.blit(title, (100, 50))
display.blit(credit, (150, 80))




# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# draw the button and button text
pygame.draw.rect(display, (cc.black), button_rect)

button_s15 = display.blit(b_s15_text, (button_rect.x + button_rect.width//2 -b_s15_text.get_rect().width//2, button_rect.y + button_rect.height//2 - b_s15_text.get_rect().height//2))


pygame.draw.rect(display, (cc.black), button_rect2)

button_database = display.blit(b_database_text, (button_rect2.x + button_rect2.width//2 -b_database_text.get_rect().width//2, button_rect2.y + button_rect.height//2 - b_database_text.get_rect().height//2))

pygame.display.flip()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# game loop
# if a button is clicked transers the user to a different screen

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_s15.collidepoint(event.pos):
                s15.poolTable()
                pygame.display.flip()
            elif button_database.collidepoint(event.pos):
                l.leaderboard()
                pygame.display.flip()
            else:
              print("hi")
              
    # Update the display
    pygame.display.flip()

