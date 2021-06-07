from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Pandas to read csv files
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="white")
    canvas.itemconfig(card_word, text=current_card["French"], fill="white")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# Create User Interface
window = Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Create Canvas
canvas = Canvas(width=800,height=626,bg=BACKGROUND_COLOR ,highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.gif")
card_back_img = PhotoImage(file="images/card_back.gif")
card_background = canvas.create_image(405,265, image=card_back_img)
card_title = canvas.create_text(400,140,text="French", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,240,text="Trouve", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=1,row=1,columnspan=2)

# Create Button
cross_image = PhotoImage(file="images/right.gif")
unknown_button = Button(image=cross_image, bg=BACKGROUND_COLOR, bd=0, highlightthickness=0, command=next_card)
unknown_button.grid(column=2,row=2)
check_image = PhotoImage(file="images/wrong.gif")
known_button = Button(image=check_image,bg=BACKGROUND_COLOR,bd=0,highlightthickness=0, command=next_card)
known_button.grid(column=1,row=2)

next_card()

window.mainloop()


