import turtle as t
import random

turtle_1 = t.Turtle()
t.colormode(255)
#turtle_1.shape("turtle")
# turtle_1.color("red")

# Draw a square
# for _ in range(4):
#     turtle_1.forward(100)
#     turtle_1.right(90)


#Draw a dashed line
# for _ in range(20):
#     turtle_1.forward(10)
#     turtle_1.up()
#     turtle_1.forward(10)
#     turtle_1.down()


#shapes = {"triangle":3,"square":4,"pentagon":5,"hexagon":6,"heptagon":7,"octagon":8,"nonagon":9,"decagon":10}
#degree = 360/shapes["triangle"]
# colors = ["IndianRed1","Green","LightSeaGreen","gold1","orange","HotPink4","VioletRed3","RoyalBlue1","cyan"]
# shape = 3
# while shape < 10:
#     degree = 360/shape
#     turtle_1.color(random.choice(colors))
#     for _ in range(shape):
#         turtle_1.forward(100)
#         turtle_1.right(degree)
#     shape += 1


# Random Walk
# Solution 1
# turtle_1.pensize(10)
# direction = ["right","left","forward","backward"]
# colors = ["IndianRed1","Green","LightSeaGreen","gold1","orange","HotPink4","VioletRed3","RoyalBlue1","cyan"]
#
#
# def move_direction(dir):
#     if dir == 'right':
#         turtle_1.right(90)
#     elif dir == "left":
#         turtle_1.left(90)
#     elif dir == "backward":
#         turtle_1.backward(10)
#     else:
#         turtle_1.forward(10)
#
#
# for _ in range(200):
#     randdirection = random.choice(direction)
#     turtle_1.color(random.choice(colors))
#     turtle_1.forward(10)
#     move_direction(randdirection)


#Solution 2
# turtle_1.pensize(10)
# turtle_1.speed("fast")
# colors = ["IndianRed1","Green","LightSeaGreen","gold1","orange","HotPink4","VioletRed3","RoyalBlue1","cyan"]
# directions = [0,90,180,270]
# for _ in range(200):
#     turtle_1.color(random.choice(colors))
#     turtle_1.forward(30)
#     turtle_1.setheading(random.choice(directions))
#
# myscreen = Screen()
# myscreen.exitonclick()

#generate random color for random walk

#turtle_1.pensize(5)
# turtle_1.speed("fast")
#
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

#
# directions = [0,90,180,270]
# for _ in range(200):
#     turtle_1.color(random_color())
#     turtle_1.forward(30)
#     turtle_1.setheading(random.choice(directions))

#Draw a spirograph
turtle_1.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        turtle_1.color(random_color())
        turtle_1.circle(100)
        turtle_1.setheading(turtle_1.heading() + size_of_gap)

draw_spirograph((5))

myscreen = t.Screen()
myscreen.exitonclick()