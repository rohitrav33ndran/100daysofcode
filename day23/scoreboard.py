from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-260,260)
        self.score = 1
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.goto(-260,260)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def level_up(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)
