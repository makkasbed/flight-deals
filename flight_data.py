class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, from_city, price,code, to_city, to_code):
        self.from_city = from_city
        self.price = price
        self.code = code
        self.to_city = to_city
        self.to_code = to_code
