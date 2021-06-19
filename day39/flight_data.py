class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,price,from_city,from_airport,to_city,to_airport,departure_date,return_date,via_city="",stop_over=0):
        self.price = price
        self.from_city = from_city
        self.from_airport = from_airport
        self.to_city = to_city
        self.to_airport = to_airport
        self.departure_date = departure_date
        self.return_date = return_date
        self.via_city = via_city
        self.stop_over = stop_over
