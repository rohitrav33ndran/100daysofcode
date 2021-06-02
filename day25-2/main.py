import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Get the x and y coord.
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
states = pandas.read_csv("50_states.csv")

guessed_state = []
score = 0
while len(guessed_state)< 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    state_d = states[states["state"] == answer_state]
    if answer_state == "Exit":
        break
    if not state_d.empty:
        guessed_state.append(answer_state)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        xcor = state_d["x"]
        ycor = state_d["y"]
        state = state_d.state.item()
        t.goto(int(xcor),int(ycor))
        fstring = f"{state}"
        t.write(fstring)

#states_to_learn.csv
to_learn_list = []


for state in states["state"].tolist():
    if state not in guessed_state:
        to_learn_list.append(state)

df = pandas.DataFrame(to_learn_list)
df.to_csv("state_to_learn.csv")