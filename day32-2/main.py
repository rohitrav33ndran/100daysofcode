import datetime as dt
import pandas as pd
import random
import smtplib
##################### Extra Hard Starting Project ######################

my_email = "email.com"
my_password = "pass"
now = dt.datetime.now()
day = now.day
month = now.month
current_day = day,month
df = pd.read_csv("birthdays.csv")
email = ""
name = ""
msg_str = ""
letters = ["letter_1.txt","letter_2.txt","letter_3.txt"]

def send_mail(msg,recipient_email):
    with smtplib.SMTP("smtp.gmail.com",port=587) as conn:
        conn.starttls()
        conn.login(user=my_email,password=my_password)
        conn.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg="Subject: Happy Birthday\n\n"
                f"{msg}"
        )


def generate_letter(name,email):
    global msg_str
    msg_str = ""
    random_letter_file = random.choice(letters)
    with open(file=f"letter_templates/{random_letter_file}",mode="r") as file:
        for line in file:
            if "[NAME]" in line:
                msg_str = msg_str + line.replace("[NAME],",name)
                msg_str = msg_str + "\n"
            else:
                msg_str = msg_str + line + "\n"
    send_mail(msg_str,email)



for index,row in df.iterrows():
    if current_day == (row["day"],row["month"]):
        email = row["email"]
        name = row["name"]
        generate_letter(name,email)