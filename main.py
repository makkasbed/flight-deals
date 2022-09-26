# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import os

data_manager = DataManager(os.getenv("SHEET_URL"))
flight_search = FlightSearch(os.getenv("FLIGHT_URL"), os.getenv("F_API_KEY"))

data = data_manager.retrieve_data()
for item in data['prices']:
    city = item['city']
    id = str(item['id'])
    data = flight_search.retrieve_iata_code(name=city)
    code = data["locations"][0]['code']
    payload = {
        "price": {
            "iataCode": code
        }
    }
    results = data_manager.update_data(id, payload)
    print(id, city, code, results)
