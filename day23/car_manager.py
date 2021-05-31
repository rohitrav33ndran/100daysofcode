from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2,outline=0)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(250,random.randrange(-250,250))
        self.move(1)

    def move(self, speed):
        current_xcor = self.xcor()
        current_ycor = self.ycor()
        self.goto(current_xcor - MOVE_INCREMENT * speed,current_ycor)
