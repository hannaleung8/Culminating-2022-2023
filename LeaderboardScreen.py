
import pygame
import colour_codes as cc

# defines the dimensions of the screen using variables to create pool table
wid = 660
heig = 360
outerHeight = 400
margin = 30
display = pygame.display.set_mode((wid, outerHeight))

display.fill(cc.background3)
pygame.display.flip()
