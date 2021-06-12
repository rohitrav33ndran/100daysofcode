from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 130, width=280, text="Question", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=1, row=1, columnspan=2,pady=50)
        right_image = PhotoImage(file="images/true.gif")
        self.right_button = Button(image=right_image,bg=THEME_COLOR,bd=0, highlightthickness=0,command=self.true_pressed)
        self.right_button.grid(column=1, row=2)
        wrong_image = PhotoImage(file="images/false.gif")
        self.wrong_button = Button(image=wrong_image, bg=THEME_COLOR, bd=0, highlightthickness=0,command=self.false_pressed)
        self.wrong_button.grid(column=2, row=2)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0,column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,func=self.get_next_question)







