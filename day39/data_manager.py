import requests
import os
from datetime import datetime

SHEETY_FLIGHT_DEALS_API_URL = os.environ.get("SHEETY_FLIGHT_DEALS_API_URL")
SHEETY_RAND_TOKEN = os.environ.get("SHEETY_RAND_TOKEN")
SHEETY_HEADER = {
    "Authorization": f"Bearer {SHEETY_RAND_TOKEN}"
}


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_FLIGHT_DEALS_API_URL = SHEETY_FLIGHT_DEALS_API_URL
        self.SHEETY_RAND_TOKEN = SHEETY_RAND_TOKEN
        self.SHEETY_HEADER = SHEETY_HEADER
        self.prices_sheet = self.get_sheets()

    def get_sheets(self):
        response = requests.get(url=self.SHEETY_FLIGHT_DEALS_API_URL, headers=self.SHEETY_HEADER)
        print(response.json())
        return response.json()

    def update_row_sheets(self,code,id):
        prices = {
            "price": {
                "iataCode": code,
            }
        }
        update_url = f"{self.SHEETY_FLIGHT_DEALS_API_URL}/{id}"
        response = requests.put(url=update_url, json=prices, headers=SHEETY_HEADER)
        print(response.text)