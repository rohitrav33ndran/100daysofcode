import requests
from datetime import datetime
import smtplib
import time
#
# response = requests.get(url="http://api.open-notify.org//iss-now.json")
# print(response.json())
#
# print(response.headers)
#
MY_LATITUDE = 52.509080
MY_LONGITUDE = 13.298040
USERNAME = "useremail"
PASSWORD = "pass"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position


def check_position(iss_latitude,iss_longitude,my_latitude,my_longitude):
    if my_latitude + 0.5 < iss_latitude < my_latitude - 0.5 \
            and my_longitude + 0.1 < iss_longitude < my_longitude - 0.1:
        return True
    else:
        return False


def check_day(sunrise,sunset,timenow):
    if sunrise + 4 < timenow < sunset - 2:
        return True
    else:
        False


def send_mail():
    with smtplib.SMTP(host="smtp.gmail.com",port=587) as conn:
        conn.starttls()
        conn.login(user=USERNAME,password=PASSWORD)
        conn.sendmail(
            from_addr=USERNAME,
            to_addrs="rohit.raveendran@outlook.com",
            msg="Subject: Look Up - ISS \n\n"
                "Iss in visibility and right above you in the sky"
        )


parameters = {
    "lat":MY_LATITUDE,
    "lng":MY_LONGITUDE,
    "formatted":0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now().hour

while True:
    time.sleep(60)
    if check_position(iss_latitude,iss_longitude,MY_LATITUDE,MY_LONGITUDE) and check_day(sunrise,sunset,time_now):
        send_mail()

