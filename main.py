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

import colour_codes as cc

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
background_colour = (cc.slate_green)
screen.fill(background_colour)
  
# update the full display using flip
pygame.display.flip()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def draw_field():
  pygame.draw.rect(screen, cc.green, pygame.Rect(70, 70, 300, 150))
  pygame.display.flip()
  
def draw_border():
  pygame.draw.rect(screen, cc.tan, pygame.Rect(45, 45, 350, 200))
  pygame.display.flip()

def draw_pocket(x,y):
  pygame.draw.circle(screen, cc.black, (x,y), 10)
  pygame.display.flip()

def pockets():
  pocket1 = draw_pocket(100,50)
  pocket2 = draw_pocket(150,50)


# function to draw pool table
def draw_pool_table():
  draw_border()
  draw_field()
  pockets()
  
draw_pool_table()




# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# creates exit command for top right corner of screen
# variable to keep game loop running as true
running = True
# game loop
while running:  
# for loop through the event queue  
    for event in pygame.event.get():     
# checks for QUIT event      
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
    pygame.display.update()