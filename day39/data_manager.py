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


    def get_sheets(self,sheet_name):
        sheets_url = f"{self.SHEETY_FLIGHT_DEALS_API_URL}/{sheet_name}"
        # print(sheets_url)
        response = requests.get(url=sheets_url, headers=self.SHEETY_HEADER)
        return response.json()

    def update_row_sheets(self,location_data):
        code,id = location_data
        prices = {
            "price": {
                "iataCode": code,
            }
        }
        update_url = f"{self.SHEETY_FLIGHT_DEALS_API_URL}/{id}"
        response = requests.put(url=update_url, json=prices, headers=SHEETY_HEADER)
        return response.status_code

    def add_row_sheets(self,first_name,last_name,email):
        users = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }
        sheet_url = f"{SHEETY_FLIGHT_DEALS_API_URL}/users"
        response = requests.post(url=sheet_url,json=users,headers=SHEETY_HEADER)
        return response.status_code