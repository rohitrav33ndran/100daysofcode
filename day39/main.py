#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta



ORIGIN_IATA_CODE = "BER"



data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_sheets("prices")
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 30)
if sheet_data[0]['iataCode'] == "":
    location_data = [(row['code'],row['id']) for row in sheet_data]
    # for item in data_manager.prices_sheet['prices']:
    #     locations = flight_search.get_locations(item['city'])
    data_manager.update_row_sheets(location_data)

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

# prices_sheet = data_manager.get_sheets("prices")
for each_city in sheet_data['prices']:
    # print(each_city)
    search_data = flight_search.search_cheap_flights(ORIGIN_IATA_CODE,each_city['iataCode'],tomorrow,six_month_from_today)
    if search_data is not None:
        if search_data.price < each_city['lowestPrice']:
            message = f"{search_data.from_city} to {search_data.to_city} on date {search_data.from_date} has lowest price GBP {search_data.price}"
            if search_data.via_city > 0:
                message = f"\nThe flight has {search_data.stop_over} stop over via city {search_data.via_city}"
            notification_manager.send_email(message)
    else:
        continue
