import pygame
import databaseTable as h
import sys
import colour_codes as cc

def leaderboard():
  # Initialize Pygame
  pygame.init()
  
  # Connect to the database
  connection = h.get_connection()
  cursor = connection.cursor()
  
  # Retrieve the data from the database
  cursor.execute("SELECT * FROM Leaderboard")
  data = cursor.fetchall()
  
  # Set the screen size and caption
  screen = pygame.display.set_mode((660, 400))
  
  
  # Create a font object for the text
  font = pygame.font.Font(None, 32)
  
  while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
  
      # Clear the screen
      screen.fill((cc.background3))
  
      # Draw the data from the database
      for i, row in enumerate(data):
          username_text = font.render(str(row[0]), True, (0, 0, 0))
          wins_text = font.render(str(row[1]), True, (0, 0, 0))
          losses_text = font.render(str(row[2]), True, (0, 0, 0))
        
          screen.blit(username_text, (50, 50 + i * 50))
          screen.blit(wins_text, (200, 50 + i * 50))
          screen.blit(losses_text, (350, 50 + i * 50))
      pygame.display.flip()