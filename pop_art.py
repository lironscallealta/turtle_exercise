#Pop art by Callealta
import turtle as t
import random
import colorgram

color_list = []
colors = colorgram.extract("pic1.jpg",35)

for i in range(len(colors)):
    my_tuple = []
    for x in range(3):
        rgb = colors[i].rgb[x]
        my_tuple.append(rgb)
    my_tuple = tuple(my_tuple)
    color_list.append(my_tuple)

list_finished = [(251, 226, 233), (46, 92, 144), (170, 13, 26), (34, 44, 62),
                 (141, 80, 44), (228, 154, 7), (161, 57, 88), (211, 162, 101), (37, 144, 46), (68, 34, 47),
                 (235, 219, 63), (225, 223, 4), (48, 45, 93), (22, 51, 47), (50, 40, 36), (88, 195, 171),
                 (117, 162, 171), (247, 90, 16), (18, 96, 49), (233, 237, 244), (211, 56, 76), (155, 23, 19),
                 (187, 143, 156), (60, 167, 91), (46, 149, 196), (226, 177, 167), (163, 209, 182), (227, 171, 180),
                 (17, 75, 108), (116, 123, 146), (184, 188, 208), (73, 79, 43), (162, 199, 214)]

timy = t.Turtle()
screen = t.Screen()
t.colormode(255)

timy.pensize(3)
timy.hideturtle()

length_finished = len(list_finished)

going = 0
timy.speed("fastest")
for x in range(10):
    timy.penup()
    timy.setposition(-250,-200+ (x * 50))


    for i in range(10):


        timy.dot(15,random.choice(color_list) )

        timy.forward(60)
        going +=1
        if going == length_finished:
            going =0


screen.exitonclick()
