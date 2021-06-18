import requests
import os
from datetime import datetime, timedelta
from flight_data import FlightData

TEQUILA_API_URL = "https://tequila-api.kiwi.com"
FLIGHT_LOCATION_SEARCH_URL = f"{TEQUILA_API_URL}/locations/query"
CHEAP_FLIGHT_SEARCH_URL = f"{TEQUILA_API_URL}/v2/search"
FLIGHT_LOCATION_SEARCH_API_KEY = os.environ.get("FLIGHT_LOCATION_SEARCH_API_KEY")
SEARCH_HEADER = {
    "accept": "application/json",
    "apikey": FLIGHT_LOCATION_SEARCH_API_KEY
}
LOCATION_SEARCH_PARAMS = {}
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flight_location_search_url = FLIGHT_LOCATION_SEARCH_URL
        self.flight_location_search_api_key = FLIGHT_LOCATION_SEARCH_API_KEY
        self.cheap_flight_search_url = CHEAP_FLIGHT_SEARCH_URL
        self.locations_search_params = LOCATION_SEARCH_PARAMS
        self.LOCATION_SEARCH_HEADER = SEARCH_HEADER

    def get_locations(self, query, locale="en-US", location_types="airport",limit=10,active_only="true"):
        self.locations_search_params = {
            "term":query,
            "locale": locale,
            "location_types": location_types,
            "limit": limit,
            "active_only": active_only
        }
        response = requests.get(url=self.flight_location_search_url,params=self.locations_search_params, headers=self.LOCATION_SEARCH_HEADER)
        return response.json()['locations'][0]['city']

    def search_cheap_flights(self):
        search_params = {
            "fly_from": "BER",
            "fly_to": "PRG",
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_month_from_today.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=self.cheap_flight_search_url,params=search_params,headers=SEARCH_HEADER)
        # print(response.json())

        try:
            res_data = response.status_code
        except IndexError:
            print(f"No flights found for .")
            return None
        print(res_data)
        return res_data
