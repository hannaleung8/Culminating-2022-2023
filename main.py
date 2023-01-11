"""
Header
Name: Hanna
Date: Jan 20 2022
Class: Gr 11 Computer Tech
Program: Culminating
Purpose: 
"""
# imports pygame module
# imports os system
# imports randomizer
# imports math function * to multiply

import pygame
import sys
from math import *
import random

import colour_codes as cc
import single15ball as s15

# initializes all imported pygame modules
pygame.init()

wid = 660
heig = 400
display = pygame.display.set_mode((wid, heig))
pygame.display.set_caption("Pool ball")

display.fill(cc.blue)
pygame.display.flip()

# Create a button

button_s15 = pygame.draw.rect(display, cc.black, pygame.Rect(300, 250, 200, 50))
pygame.display.flip()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_s15.collidepoint(event.pos):
                # Change the background color
                s15.poolTable()
                pygame.display.flip()
            else:
              print("hi")


    # Update the display
    pygame.display.flip()

s15.poolTable()