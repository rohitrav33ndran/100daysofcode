from turtle import Turtle,Screen
import random

screen = Screen()
color_list = ["red","blue","orange","green","purple","yellow"]
turtle_list = []
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle would win the race. Enter a color? : ")

def random_move(turtleobj):
    turtleobj.forward(random.randrange(5,25))

turtle_pos = 0
for turtle in range(len(color_list)):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.pensize(10)
    new_turtle.color(color_list[turtle])
    turtle_pos += 50
    new_turtle.up()
    new_turtle.goto(x=-200,y=-170 + turtle_pos)
    turtle_list.append(new_turtle)


# screen.listen()

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle won the race!")
                is_game_on = False
            else:
                print(f"You have lost. The {winning_color} turtle won the race!")
                is_game_on = False
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()