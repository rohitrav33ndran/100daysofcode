from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_text.config(text="TIMER",fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    # if is the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_text.config(text="LONG BREAK",fg=RED)
    # if its 2nd, 4th, 6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_text.config(text="SHORT BREAK", fg=PINK)
    # if its the 1st/3rd/5th/7th:
    else:
        count_down(work_sec)
        label_text.config(text="WORK")

    #count_down(5 * 60) #60 seconds

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

# Label
label_text = Label(text="TIMER",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label_text.grid(column=2,row=1)
# Canvas
canvas = Canvas(width=204,height=232, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.gif")
canvas.create_image(104,119, image=tomato_png)
timer_text = canvas.create_text(104,140,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2,row=2)

# Button
start_button = Button(text="Start",relief=RAISED, bg=YELLOW,bd=0, highlightthickness=0,command=start_timer)
start_button.grid(column=1,row=3)
reset_button = Button(text="Reset",relief=RAISED,bg=YELLOW,bd=0, highlightthickness=0,command=reset_timer)
reset_button.grid(column=3,row=3)
# Label
check_mark = Label(bg=YELLOW,fg=GREEN, font=(FONT_NAME, 35, "bold"))
check_mark.grid(column=2,row=4)



window.mainloop()