"""
Header
Name: Hanna
Date: Jan 20 2022
Class: Gr 11 Computer Tech
Program: Culminating
Purpose: to play pool and show what I learned in this course
(Unfinished)
"""

# imports pygame module
# import colour code file
# import single 15 ball file as s15
# import database file as d

import pygame
import colour_codes as cc
import single15ball as s15
import leaderboard_screen as l
import sys
import database as d

# initializes all imported pygame modules
pygame.init()


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
font3 = pygame.font.Font(None, 24)

# button size
button_rect = pygame.Rect(100, 150, 100, 50)
button_rect2 = pygame.Rect(400, 150, 100, 50)
button_rect3 = pygame.Rect(100, 250, 100, 50)

# text rendering
title = font.render("Pool Ball Menu", True, (cc.black))
credit = font2.render("By: Hanna Leung", True, (cc.black))
b_s15_text = font.render("Practice", True, (cc.white))
b_leaderboard_text = font.render("Podium", True, (cc.white))
b_database_text = font3.render("database", True, (cc.white))

# blit the text onto the screen
display.blit(title, (100, 50))
display.blit(credit, (150, 80))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# draws button Practice and text
pygame.draw.rect(display, (cc.black), button_rect)

button_s15 = display.blit(b_s15_text, (button_rect.x + button_rect.width//2 -b_s15_text.get_rect().width//2, button_rect.y + button_rect.height//2 - b_s15_text.get_rect().height//2))

# draws button Podium and text
pygame.draw.rect(display, (cc.black), button_rect2)

button_leaderboard = display.blit(b_leaderboard_text, (button_rect2.x + button_rect2.width//2 -b_leaderboard_text.get_rect().width//2, button_rect2.y + button_rect.height//2 - b_leaderboard_text.get_rect().height//2))

pygame.display.flip()

# draws button database and text
pygame.draw.rect(display, (cc.black), button_rect3)

button_database = display.blit(b_database_text, (button_rect3.x + button_rect3.width//2 -b_database_text.get_rect().width//2, button_rect3.y + button_rect.height//2 - b_database_text.get_rect().height//2))

pygame.display.flip()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def instructions():
    image = pygame.image.load('instructions.png')
    # Get the rectangle of the image
    rect = image.get_rect()
    
    # Set the center position of the image
    rect.center = (wid/2, heig/2)
    
    # Draw the image on the display
    display.blit(image, rect)
    
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    return

class Menu:
    def main_menu():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_s15.collidepoint(event.pos):
                        instructions()
                        s15.pool_table()
                    elif button_leaderboard.collidepoint(event.pos):
                        instructions()
                        l.leaderboard()
                    elif button_database.collidepoint(event.pos):
                        d.database()
                        pygame.display.flip()
            pygame.display.flip()
            pygame.display.flip()
    main_menu()
