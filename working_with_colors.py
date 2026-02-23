import turtle as t

import random as ra

tim = t.Turtle()
t.colormode(255)
directions = [0, 90, 180, 270]


def randomness_colors():
    r = ra.randint(0,255)
    g = ra.randint(0,255)
    b = ra.randint(0,255)
    color = (r,g,b)
    return color

def drawing_anything_with_colors():
    tim.speed(3)
    num = 0
    for i in range(200):

        for i in range(5):
            tim.color(randomness_colors())
            tim.pensize(num * 2)
            num += 1
            tim.forward(30)
            tim.setheading(ra.choice(directions))
        for x in range(5):
            tim.color(randomness_colors())
            tim.pensize(num * 2)
            num -= 1
            tim.forward(30)
            tim.setheading(ra.choice(directions))

drawing_anything_with_colors()
