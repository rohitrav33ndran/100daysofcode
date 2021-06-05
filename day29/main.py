from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    passw = "".join(password_list)
    password.insert(0,passw)
    pyperclip.copy(passw)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_name.get()
    email = email_username.get()
    passwd = password.get()
    if len(website) == 0 or len(passwd) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any empty fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} "
                               f"\nPassword: {passwd} \nIs it ok to save?")

        if is_ok:
            with open("credentials.txt",mode="a") as cred:
                cred.write(f"{website} | {email} | {passwd}\n")
                #below will help to delete the exiting form entries
                website_name.delete(0, END)
                password.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200,highlightthickness=2)
my_pass_logo = PhotoImage(file="logo.gif")
canvas.create_image(100,100, image=my_pass_logo)
canvas.grid(column=2,row=1)

# Label
label_website = Label(text="Website")
label_website.grid(column=1,row=2)
label_email_username = Label(text="Email/Username")
label_email_username.grid(column=1,row=3)
label_password = Label(text="Password")
label_password.grid(column=1,row=4)

# Button
generate_password_button = Button(width=12,text="GeneratePass",relief=RAISED,command=generate_password)
generate_password_button.grid(column=3,row=4)
add_button = Button(width=35,text="Add",relief=RAISED,command=save_password)
add_button.grid(column=2,row=5,columnspan=2)

# Entry
website_name = Entry(width=35)
website_name.grid(column=2,row=2,columnspan=2)
website_name.focus()
email_username = Entry(width=35)
email_username.grid(column=2,row=3,columnspan=2)
email_username.insert(0, 'rohit.raveendran@outlook.com')
password = Entry(width=20)
password.grid(column=2,row=4)




window.mainloop()