
# imports pygame module
# imports os system
# imports math function * to multiply
# imports colour variables

import pygame
import sys
from math import *
import colour_codes as cc


# variable made to track time
clk = pygame.time.Clock()

# defines the dimensions of the screen using variables to create pool table
wid = 660
heig = 360
outer_height = 400
margin = 30
display = pygame.display.set_mode((wid, outer_height))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# initializes balls, radius, and the friction
balls = []
no_balls = 15
radius = 10
friction = 0.005

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# ball class
class Ball:
  
# initialize ball object, place, colour, speed, angle, ball number, and font
  def __init__(self, i, j, speed, color, angle, ball_num):
      self.x = i + radius
      self.y = j + radius
      self.color = color
      self.angle = angle
      self.speed = speed
      self.ball_num = ball_num
      self.font = pygame.font.SysFont("Agency FB", 10)
  
# draws balls on display window
# creates eight ball and cue ball seperately
  def draw(self, i, j):
      pygame.draw.ellipse(display, self.color, (i - radius, j - radius, radius*2, radius*2))
      if self.color == cc.black or self.ball_num == "cue":
          ball_no = self.font.render(str(self.ball_num), True, cc.white)
          display.blit(ball_no, (i - 5, j - 5))
      else:
          ball_no = self.font.render(str(self.ball_num), True, cc.black)
          if self.ball_num > 9:
              display.blit(ball_no, (i - 6, j - 5))
          else:
              display.blit(ball_no, (i - 5, j - 5))
  
# moves the ball around the screen based on angles of each individual ball
# takes into account speed, friction, and angles within the margin border
  def move(self):
      self.speed -= friction
      if self.speed <= 0:
          self.speed = 0
      self.x = self.x + self.speed*cos(radians(self.angle))
      self.y = self.y + self.speed*sin(radians(self.angle))
  
      if not (self.x < wid - radius - margin):
          self.x = wid - radius - margin
          self.angle = 180 - self.angle
      if not(radius + margin < self.x):
          self.x = radius + margin
          self.angle = 180 - self.angle
      if not (self.y < heig - radius - margin):
          self.y = heig - radius - margin
          self.angle = 360 - self.angle
      if not(radius + margin < self.y):
          self.y = radius + margin
          self.angle = 360 - self.angle

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        
# pocket class
class Pockets:
  
# initializes pocket dimensions, spot, and colour
  def __init__(self, x, y, color):
      self.r = margin/2
      self.x = x + self.r + 10
      self.y = y + self.r + 10
      self.color = color

# draws the pockets on the display
  def draw(self):
      pygame.draw.ellipse(display, self.color, (self.x - self.r, self.y - self.r, self.r*2, self.r*2))

  # checks if ball has entered the hole
  # checks if 8 ball went into a hole, if so gameover screen
  def check_put(self):
      global balls
      balls_copy = balls[:]
      for i in range(len(balls)):
          dist = ((self.x - balls[i].x)**2 + (self.y - balls[i].y)**2)**0.5
          if dist < self.r + radius:
              if balls[i] in balls_copy:
                  if balls[i].ball_num == 8:
                      gameOver()
                  else:
                      balls_copy.remove(balls[i])

      balls = balls_copy[:]

# cue stick class
class Cue_stick:

# initializes length, colour, and location
  def __init__(self, x, y, length, color):
      self.x = x
      self.y = y
      self.length = length
      self.color = color
      self.tangent = 0

  # applies force to cue ball
  def apply_force(self, cue_ball, force):
      cue_ball.angle = self.tangent
      cue_ball.speed = force

  # draws cue stick on pygame window
  # gets position from mouse
  # draws white aim line
  def draw(self, cuex, cuey):
      self.x, self.y = pygame.mouse.get_pos()
      self.tangent = (degrees(atan2((cuey - self.y), (cuex - self.x))))
      pygame.draw.line(display, cc.white, (cuex + self.length*cos(radians(self.tangent)), cuey + self.length*sin(radians(self.tangent))), (cuex, cuey), 1)
      pygame.draw.line(display, self.color, (self.x, self.y), (cuex, cuey), 3)


# checks collision function
def collision(ball1, ball2):
    dist = ((ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2)**0.5
    if dist <= radius*2:
        return True
    else:
        return False

# checks if cue ball hits any ball using collision function
def check_cue_collision(cue_ball):
    for i in range(len(balls)):
        if collision(cue_ball, balls[i]):
            if balls[i].x == cue_ball.x:
                angle_incline = 2*90
            else:
                u1 = balls[i].speed
                u2 = cue_ball.speed

                balls[i].speed = ((u1*cos(radians(balls[i].angle)))**2 + (u2*sin(radians(cue_ball.angle)))**2)**0.5
                cue_ball.speed = ((u2*cos(radians(cue_ball.angle)))**2 + (u1*sin(radians(balls[i].angle)))**2)**0.5

                tangent = degrees((atan((balls[i].y - cue_ball.y)/(balls[i].x - cue_ball.x)))) + 90
                angle = tangent + 90

                balls[i].angle = (2*tangent - balls[i].angle)
                cue_ball.angle = (2*tangent - cue_ball.angle)

                balls[i].x += (balls[i].speed)*sin(radians(angle))
                balls[i].y -= (balls[i].speed)*cos(radians(angle))
                cue_ball.x -= (cue_ball.speed)*sin(radians(angle))
                cue_ball.y += (cue_ball.speed)*cos(radians(angle))


# checks collision between balls using collision function
def check_collision():
    for i in range(len(balls)):
        for j in range(len(balls) - 1, i, -1):
            if collision(balls[i], balls[j]):
                if balls[i].x == balls[j].x:
                    angle_incline = 2*90
                else:
                    u1 = balls[i].speed
                    u2 = balls[j].speed

                    balls[i].speed = ((u1*cos(radians(balls[i].angle)))**2 + (u2*sin(radians(balls[j].angle)))**2)**0.5
                    balls[j].speed = ((u2*cos(radians(balls[j].angle)))**2 + (u1*sin(radians(balls[i].angle)))**2)**0.5

                    tangent = degrees((atan((balls[i].y - balls[j].y)/(balls[i].x - balls[j].x)))) + 90
                    angle = tangent + 90

                    balls[i].angle = (2*tangent - balls[i].angle)
                    balls[j].angle = (2*tangent - balls[j].angle)

                    balls[i].x += (balls[i].speed)*sin(radians(angle))
                    balls[i].y -= (balls[i].speed)*cos(radians(angle))
                    balls[j].x -= (balls[j].speed)*sin(radians(angle))
                    balls[j].y += (balls[j].speed)*cos(radians(angle))

# creates border around field
def border():
    pygame.draw.rect(display, cc.grey, (0, 0, wid, 30))
    pygame.draw.rect(display, cc.grey, (0, 0, 30, heig))
    pygame.draw.rect(display, cc.grey, (wid - 30, 0, wid, heig))
    pygame.draw.rect(display, cc.grey, (0, heig - 30, wid, heig))

# creates score on screen
# checks the amount of balls on the screen
def score():
    font = pygame.font.SysFont("Agency FB", 30)

    pygame.draw.rect(display, (51, 51, 51), (0, heig, wid, outer_height))
    for i in range(len(balls)):
        balls[i].draw((i + 1)*2*(radius + 1), heig + radius + 10)

    text = font.render("Remaining Balls: " + str(len(balls)), True, cc.stickColor)
    display.blit(text, (wid/2 + 50, heig + radius/2))

# reset screen to initial postions
def reset():
    global balls, no_balls
    no_balls = 15
    balls = []

    s = 70

  
    a1 = Ball(s, heig/2 - 4*radius, 0, cc.colors[0], 0, 1)
    a2 = Ball(s + 2*radius, heig/2 - 3*radius, 0,  cc.colors[1], 0, 2)
    a3 = Ball(s, heig/2 - 2*radius, 0, cc.colors[2], 0, 3)
    a4 = Ball(s + 4*radius, heig/2 - 2*radius, 0, cc.colors[3], 0, 4)
    a5 = Ball(s + 2*radius, heig/2 - 1*radius, 0, cc.colors[4], 0, 5)
    a6 = Ball(s, heig/2, 0, cc.colors[5], 0, 6)
    a7 = Ball(s + 6*radius, heig/2 - 1*radius, 0, cc.colors[6], 0, 7)
    a8 = Ball(s + 4*radius, heig/2, 0, cc.colors[7], 0, 8)
    a9 = Ball(s + 8*radius, heig/2, 0, cc.colors[8], 0, 9)
    a10 = Ball(s + 6*radius, heig/2 + 1*radius, 0, cc.colors[9], 0, 10)
    a11 = Ball(s + 2*radius, heig/2 + 1*radius, 0, cc.colors[10], 0, 11)
    a12 = Ball(s, heig/2 + 2*radius, 0, cc.colors[11], 0, 12)
    a13 = Ball(s + 4*radius, heig/2 + 2*radius, 0, cc.colors[12], 0, 13)
    a14 = Ball(s + 2*radius, heig/2 + 3*radius, 0, cc.colors[13], 0, 14)
    a15 = Ball(s, heig/2 + 4*radius, 0, cc.colors[14], 0, 15)

    balls.append(a1)
    balls.append(a2)
    balls.append(a3)
    balls.append(a4)
    balls.append(a5)
    balls.append(a6)
    balls.append(a7)
    balls.append(a8)
    balls.append(a9)
    balls.append(a10)
    balls.append(a11)
    balls.append(a12)
    balls.append(a13)
    balls.append(a14)
    balls.append(a15)


# function for game over
# text pops 
def gameOver():
    font = pygame.font.SysFont("Agency FB", 75)
    if len(balls) == 0:
        text = font.render("You Won!", True, (133, 193, 233))
    else:
        text = font.render("You Lost! Black in Hole!", True, (241, 148, 138))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()

                if event.key == pygame.K_r:
                    pool_table()
        display.blit(text, (50, heig/2))

        pygame.display.update()
        clk.tick()

def close():
    pygame.quit()
    sys.exit()

# Main Function
def pool_table():
    loop = True

    reset()

    no_pockets = 6
    pockets = []

    i1 = Pockets(0, 0, cc.black)
    i2 = Pockets(wid/2 - i1.r*2, 0, cc.black)
    i3 = Pockets(wid - i1.r - margin - 5, 0, cc.black)
    i4 = Pockets(0, heig - margin - 5 - i1.r, cc.black)
    i5 = Pockets(wid/2 - i1.r*2, heig - margin - 5 - i1.r, cc.black)
    i6 = Pockets(wid - i1.r - margin - 5, heig - margin - 5 - i1.r, cc.black)

    pockets.append(i1)
    pockets.append(i2)
    pockets.append(i3)
    pockets.append(i4)
    pockets.append(i5)
    pockets.append(i6)

    cue_ball = Ball(wid/2, heig/2, 0, cc.white, 0, "cue")
    cue_stick = Cue_stick(0, 0, 100, cc.stickColor)


    start = 0
    end = 0

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()

                if event.key == pygame.K_r:
                    pool_table()

            if event.type == pygame.MOUSEBUTTONDOWN:
                start = [cue_ball.x, cue_ball.y]
                x, y = pygame.mouse.get_pos()
                end = [x ,y]
                dist = ((start[0] - end[0])**2 + (start[1] - end[1])**2)**0.5
                force = dist/10.0
                if force > 10:
                    force = 10

                cue_stick.apply_force(cue_ball, force)


        display.fill(cc.background)

        cue_ball.draw(cue_ball.x, cue_ball.y)
        cue_ball.move()

        if not (cue_ball.speed > 0):

            cue_stick.draw(cue_ball.x, cue_ball.y)

        for i in range(len(balls)):
            balls[i].draw(balls[i].x, balls[i].y)

        for i in range(len(balls)):
           balls[i].move()

        check_collision()
        check_cue_collision(cue_ball)
        border()

        for i in range(no_pockets):
            pockets[i].draw()

        for i in range(no_pockets):
            pockets[i].check_put()

        if len(balls) == 1 and balls[0].ball_num == 8:
            gameOver()

        score()

        pygame.display.update()
        clk.tick(60)
      