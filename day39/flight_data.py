class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,price,from_city,to_city,from_date,to_date):
        self.price = price
        self.from_city = from_city
        self.to_city = to_city
        self.from_date = from_date
        self.to_date = to_date
