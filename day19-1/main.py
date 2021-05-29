from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_count_clockwise():
    tim.left(10)
def move_clockwise():
    tim.right(10)
def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward, "s")
screen.onkey(move_count_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()