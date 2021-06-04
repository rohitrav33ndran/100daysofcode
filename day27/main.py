import tkinter

def button_clicked():
    print("I got clicked")
    user_input = input.get()
    my_label.config(text=user_input)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

#Label
my_label = tkinter.Label(text="I am a Label", font=("Arial",24,"bold"))
my_label["text"] = "New text"
# my_label.pack()
# my_label.place(x=0,y=0)
my_label.grid(column=1,row=1)


#Button
button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=2,row=2)
new_button = tkinter.Button(text="Click Me",bg="grey", fg="blue", command=button_clicked)
new_button.grid(column=3,row=1)

#Entry
user_input = tkinter.StringVar(window)
input = tkinter.Entry(width=10, textvariable=user_input)
# input.pack()
input.grid(column=4,row=3)




window.mainloop()
