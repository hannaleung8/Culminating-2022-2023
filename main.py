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
import random
from math import *

# initilizes all imported pygame modules
pygame.init()

# variable made to track time
clock = pygame.time.Clock()
  
# defines the dimensions of screen using variables
screen_width = 300
screen_length = 500
screen = pygame.display.set_mode((screen_length, screen_width))

# set the caption of the screen
pygame.display.set_caption('8 Ball Pool')

# defines the background colour
# using RGB color coding
# fills the background colour to the screen
background_colour = (234, 212, 252)
screen.fill(background_colour)
  
# update the full display using flip
pygame.display.flip()
  
# variable to keep game loop running as true
running = True
  
# game loop
while running:  
  
# for loop through the event queue  
    for event in pygame.event.get():     
# checks for QUIT event      
        if event.type == pygame.QUIT:
            running = False