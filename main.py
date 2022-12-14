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

# creates screen
# title, size, and background
screen = turtle.Screen()
screen.title('Hannas Desktop')
screen.setup(1000,800)
screen.bgpic('desktop.gif')

# defines turtle pen
# hides turtle
pen = turtle.Turtle()
pen.hideturtle()

# animelist application
pen.penup()
pen.begin_fill()
screen.addshape('animelistapp.gif')
pen.shape('animelistapp.gif')
pen.goto(-400, 300)
pen.stamp()

"""
Button_x = -450
Button_y = 300
ButtonLength = 100
ButtonWidth = 50

mode = 'dark'


def draw_rect_button(pen, message = 'Hangman'):
    pen.penup()
    pen.begin_fill()
    pen.goto(Button_x, Button_y)
    pen.goto(Button_x + ButtonLength, Button_y)
    pen.goto(Button_x + ButtonLength, Button_y + ButtonWidth)
    pen.goto(Button_x, Button_y + ButtonWidth)
    pen.goto(Button_x, Button_y)
    pen.end_fill()
    pen.goto(Button_x + 15, Button_y + 15)
    pen.write(message, font = ('Arial', 15, 'normal'))


draw_rect_button(pen)


def button_click(x, y):
    global mode
    if Button_x <= x <= Button_x + ButtonLength:
        if Button_y <= y <= Button_y + ButtonWidth:
            print('Clicked')
            if mode == 'dark':
                screen.bgcolor('orange')
                mode = 'light'
            else:
                screen.bgcolor('#111111')
                mode = 'dark'

def distance(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
"""