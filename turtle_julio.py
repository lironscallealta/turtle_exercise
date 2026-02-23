from turtle import Turtle, Screen
from random import randint

options = { "triangle" : 3,
            "square" : 4,
            "pentagon" : 5,
            "hexagon" : 6,
            "heptagon" : 7,
            "octagon" : 8,
            "nonagon" : 9,
            "decagon" : 10,
            "hendecagon" : 11,
            "dodecagon" : 12,
            }

julio = Turtle()
tt_turtle_obj = Turtle()

def walking_square():

    for i in range(4):
        final = 0
        for x in range(15):
            tt_turtle_obj.forward(5)
            tt_turtle_obj.penup()
            tt_turtle_obj.forward(5)
            tt_turtle_obj.pendown()
            final +=1
            if final == 15:
                tt_turtle_obj.right(90)
#walking_square()

def drawing(figure_sides: int):
    for i in range(3,figure_sides+1):
        color_list = [
            "black", "gray",
            "red", "orange", "yellow", "gold",
            "green", "lime", "olive",
            "blue", "navy", "cyan",
            "purple", "violet", "magenta",
            "pink", "brown", "maroon",
            "turquoise", "skyblue", "teal"
        ]
        choosing = color_list[(randint(0, len(color_list)))]

        for x in range(i):
            angle = 360 / i
            julio.forward(100)
            julio.color(choosing)
            julio.right(angle)


def dictionary_figures():
    for key in options:
        value = options[key]
        print(f"{key} = {value}")


def saving_figure():
    tries = 0
    number = 0
    while True:

        #complaing
        draw = input("Write the figure you want:\n").lower()

        if 3 <= tries < 6:
            phrases = ["It seems you are not pretty good at this...",
                    "Come on",
                    "What is going on..."]

            print(phrases[number])
            number +=1
            tries +=1
            continue

        elif tries == 6:
            print("I give up you are too stupid for this")
            break

        if draw in options:
            print(f"{draw} has {options[draw]} sides")
            figure = draw
            return figure

        elif draw.isdigit():
            print("It can not be a number")
            tries +=1
            dictionary_figures()
        else:
            print("You must write a correct figure\n")
            tries += 1
            dictionary_figures()

dictionary_figures()

figures = saving_figure()
sides = options[figures]
drawing(sides)





screen = Screen()
screen.exitonclick()
