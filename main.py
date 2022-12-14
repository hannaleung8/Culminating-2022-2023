"""
Header
Name: Hanna
Date: Jan 20 2022
Class: Gr 11 Computer Tech
Program: Culminating
Purpose: 
"""
# imports turtle module
import turtle

# defines turtle pen
# hides turtle
pen = turtle.Turtle()
pen.hideturtle()

# creates screen
# title, size, and background
screen = turtle.Screen()
screen.title('Hannas Desktop')
screen.setup(1000,800)
screen.bgpic('desktop.gif')

  
# animelist application
def create_animelistapp(pen, x, y):
  pen.penup()
  pen.begin_fill()
  screen.addshape('animelistapp.gif')
  pen.shape('animelistapp.gif')
  pen.goto(x, y)
  pen.stamp()
  pen.end_fill()
  return x and y

create_animelistapp(pen,-400,300)

insdf= input()
insdf = "poop"
  screen2 = turtle.Screen()
  screen2.title('H')
  screen.setup(1000,800)
  screen.bgpic('animelistapp.gif')

"""
def animelistapp_click(x, y):
  if button_x <= x <= button_x + buttonLength and button_y <= y <= button_y + buttonWidth:
    screen = turtle.Screen()
    screen.title('H')
    screen.setup(1000,800)
    screen.bgpic('animelistapp.gif')

screen.onclick(animelistapp_click(-400,300))
"""