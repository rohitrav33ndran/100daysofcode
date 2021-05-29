# import colorgram
#
# colors = colorgram.extract('hirstpainting.png',50)
# colorslist = []

# for color in range(1,len(colors)):
#     r,g,b = colors[color].rgb
#     colorslist.append((r,g,b))

import turtle as t
import random

turtle_1 = t.Turtle()
t.colormode(255)
turtle_1.pensize(10)
color_list = [(228, 228, 225), (224, 222, 223), (199, 175, 117), (124, 36, 24), (170, 106, 56), (187, 159, 51), (5, 56, 83), (222, 222, 225), (199, 215, 203), (106, 67, 86), (87, 141, 57), (19, 122, 175), (110, 160, 174), (75, 39, 47), (8, 67, 47), (62, 153, 139), (135, 41, 43), (183, 97, 79), (179, 201, 186), (208, 199, 131), (150, 174, 162), (175, 166, 169), (97, 141, 153), (28, 79, 60), (209, 185, 178), (21, 77, 96), (195, 189, 191), (178, 197, 202), (141, 120, 125), (48, 65, 81), (187, 191, 197), (105, 130, 153)]
turtle_1.hideturtle()

def random_color():
    return random.choice(color_list)

turtle_1.speed("fastest")
xposition = -200
yposition = -200
for _ in range(10):
    turtle_1.up()
    turtle_1.setposition(xposition,yposition)
    yposition += 50
    turtle_1.down()
    for _ in range(10):
        turtle_1.dot(20,random_color())
        turtle_1.up()
        turtle_1.forward((50))


myscreen = t.Screen()
myscreen.exitonclick()