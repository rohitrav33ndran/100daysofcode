import requests
import os
from datetime import datetime

NUTRITIONIX_API_URL = os.environ.get("NUTRITIONIX_API_URL")
SHEETY_API_URL = os.environ.get("SHEETY_API_URL")
NUTRI_APP_ID = os.environ.get("NUTRI_APP_ID")
NUTRI_APP_KEY = os.environ.get("NUTRI_APP_KEY")
SHEETY_RAND_TOKEN = os.environ.get("SHEETY_RAND_TOKEN")
GENDER = "male"
WEIGHT_KG = 80.5
HEIGHT_CM = 167.64
AGE = 30


NUTRI_HEADER = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_APP_KEY,
    "Content-Type": "application/json",
}

SHEETY_HEADER = {
    "Authorization": f"Bearer {SHEETY_RAND_TOKEN}"
}


def track_exercise():
    TRACK = input("Tell me which exercise you did: ")
    EXERCISE_DATA = {
        "query": TRACK,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm":HEIGHT_CM,
        "age":AGE
    }
    response = requests.post(url=NUTRITIONIX_API_URL,json=EXERCISE_DATA,headers=NUTRI_HEADER)
    return response.json()['exercises']


def get_sheets():
    response = requests.get(url=SHEETY_API_URL,headers=SHEETY_HEADER)
    return response.json()


def add_row_sheets(date,time,exercise_name, exercise_duration,exercise_calories):
    workouts = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": exercise_calories,
        }
    }
    response = requests.post(url=SHEETY_API_URL,json=workouts, headers=SHEETY_HEADER)
    print(response.text)


today = datetime.today()
current_date = today.strftime("%d/%m/%Y")
current_time = today.strftime("%H:%M:%S")

# sheet_data = get_sheets()

while True:
    exercises = track_exercise()
    print(exercises)
    for exercise in exercises:
        for key in exercise:
            if key == "name":
                exercise_name = exercise[key]
            elif key == "duration_min":
                exercise_duration = exercise[key]
            elif key == "nf_calories":
                exercise_calories = exercise[key]
        add_row_sheets(current_date,current_time,exercise_name,exercise_duration,exercise_calories)