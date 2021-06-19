import smtplib
import os
from data_manager import DataManager

my_email = os.environ.get('MY_TEST_EMAIL')
my_password = os.environ.get('MY_EMAIL_PASS')
data_manager = DataManager()
sheet_data = data_manager.get_sheets("users")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_mail(self,msg):
        for user in sheet_data['users']:
            recipient_email = user['email']
            with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
                conn.starttls()
                conn.login(user=my_email, password=my_password)
                conn.sendmail(
                    from_addr=my_email,
                    to_addrs=recipient_email,
                    msg="Subject: Flight Club - Cheap Flights\n\n"
                        f"{msg}"
                )