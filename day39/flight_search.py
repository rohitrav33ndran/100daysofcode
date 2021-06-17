import requests
import os


FLIGHT_LOCATION_SEARCH_URL = "https://tequila-api.kiwi.com/locations/query"
FLIGHT_LOCATION_SEARCH_API_KEY = os.environ.get("FLIGHT_LOCATION_SEARCH_API_KEY")
LOCATION_SEARCH_HEADER = {
    "accept": "application/json",
    "apikey": FLIGHT_LOCATION_SEARCH_API_KEY
}
LOCATION_SEARCH_PARAMS = {}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flight_location_search_url = FLIGHT_LOCATION_SEARCH_URL
        self.flight_location_search_api_key = FLIGHT_LOCATION_SEARCH_API_KEY
        self.locations_search_params = LOCATION_SEARCH_PARAMS
        self.LOCATION_SEARCH_HEADER = LOCATION_SEARCH_HEADER

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