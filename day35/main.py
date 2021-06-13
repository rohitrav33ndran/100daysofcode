import requests
import os
from twilio.rest import Client

BERLIN_LAT = "52.509079"
BERLIN_LONG = "13.298040"
THALASSERY_LAT = "11.753000"
THALASSERY_LONG = "75.493400"

#

owa_endpoint = os.environ['OPEN_WEATHER_ENDPOINT']
owa_token = os.environ['OPEN_WEATHER_API_TOKEN']
twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone_no = os.environ['TWILIO_PHONE_NO']
clien_phone_no = os.environ['CLIENT_PHONE_NO']


parameters = {
    "lat":THALASSERY_LAT,
    "lon":THALASSERY_LONG,
    "exclude":"current,minutely,daily",
    "appid":owa_token,
}

response = requests.get(url=owa_endpoint, params=parameters)
response.raise_for_status()
data = response.json()["hourly"]
weather_ids = []
for hour in range(12):
    weather_ids.append(data[hour]["weather"][0]["id"])

will_rain = False
for id in weather_ids:
    if id < 700:
        will_rain = True
if will_rain:
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Carry an umbrella",
        from_=twilio_phone_no,
        to=clien_phone_no
    )
    print(message.status)