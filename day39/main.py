#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData


iata_code = []

data_manager = DataManager()
flight_search = FlightSearch()
prices_sheet = data_manager.get_sheets("prices")
# for item in data_manager.prices_sheet['prices']:
#     locations = flight_search.get_locations(item['city'])
#     data_manager.update_row_sheets(locations['code'],item['id'])

# print("Welcome to Rohit's Flight club")
# print("We find the best flight deals and email you")
# first_name = input("What is your first name ?\n")
# last_name = input("What is your last name ?\n")
# email = input("What is your email ?\n")
# verify_email = input("Type your email again.\n")
# if email == verify_email:
#     print("You are in the club !")
#     data_manager.add_row_sheets(first_name,last_name,email)
#
#
# users_sheet = data_manager.get_sheets("users")
# print(users_sheet)

prices_sheet = data_manager.get_sheets("prices")
for each_city in prices_sheet['prices']:
    print(each_city)
    search_data = flight_search.search_cheap_flights("BER",each_city['iataCode'])
    if search_data is not None:
        if search_data.price < each_city['lowestPrice']:
            print(f"{search_data.from_city} to {search_data.to_city} on date {search_data.from_date} has lowest price GBP {search_data.price}")
    else:
        continue
