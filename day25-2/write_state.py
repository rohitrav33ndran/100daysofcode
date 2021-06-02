from turtle import Turtle


class WriteState(Turtle):
    def __init__(self):
        super().__init__()
        self.t = Turtle()
        self.t.state = ""
        self.t.x = 0
        self.t.y = 0
        # self.t.color("Black")
        self.t.hideturtle()
        self.t.penup()

    def write(self,xcor,ycor,state):
        self.t.x = xcor
        self.t.y = ycor
        self.t.state = state
