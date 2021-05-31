from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)
        self.FINISH_LINE_Y = FINISH_LINE_Y

    def up(self):
        current_xcor = self.xcor()
        current_ycor = self.ycor()
        self.goto(current_xcor, current_ycor + 10)


    def refresh(self):
        self.goto(STARTING_POSITION)