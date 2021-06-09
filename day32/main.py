import smtplib
import datetime as dt
import random
#
my_email = "email.com"
my_password = ""
quotes = []
# # connection = smtplib.SMTP("smtp.gmail.com",port=587)
# # connection.starttls()
# # connection.login(user=my_email,password=my_password)
# # connection.sendmail(from_addr=my_email,to_addrs="rohit.raveendran@outlook.com", msg="Subject:Hello\n\n"
# #                                                                                     "This is the body of the email")
# # connection.close()
#
# with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="rohit.raveendran@outlook.com",
#         msg="Subject:Hello\n\n""This is the body of the email")


# now = dt.datetime.now()
# year = now.year
# print(year)
#
# date_of_birth = dt.datetime(year=1988,month=3,day=23,hour=17)
# print(date_of_birth)

with open(file="quotes.txt",mode="r") as file:
    quotes = file.readlines()

quote_of_the_day = random.choice(quotes)

now = dt.datetime.now()
day = now.weekday()
if day == 2:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="rohit.raveendran@outlook.com",
            msg="Subject:Motivation quote of the day\n\n"
                f"{quote_of_the_day}"
        )


