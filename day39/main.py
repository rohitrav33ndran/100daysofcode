#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

iata_code = []

data_manager = DataManager()
flight_search = FlightSearch()
for item in data_manager.prices_sheet['prices']:
    locations = flight_search.get_locations(item['city'])
    data_manager.update_row_sheets(locations['code'],item['id'])

