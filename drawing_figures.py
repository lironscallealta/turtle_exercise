import turtle as t

from random import randint, choice
from turtle import Turtle


tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]
azar1 = randint(0,4)


def drawing_anything():
    tim.speed(1)
    num = 0
    for i in range(200):


        for i in range(3):
            tim.color(choice(colours))
            tim.pensize(num * 2)
            num += 0.5
            tim.forward(30)
            tim.setheading(choice(directions))
        for x in range(3):
            tim.color(choice(colours))
            tim.pensize(num * 2)
            num -= 0.5
            tim.forward(30)
            tim.setheading(choice(directions))

drawing_anything()
