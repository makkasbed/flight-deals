# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import os
import datetime

start_date = datetime.date.today() + datetime.timedelta(days=1)
end_date = datetime.date.today() + datetime.timedelta(days=180)


data_manager = DataManager(os.getenv("SHEET_URL"))
flight_search = FlightSearch(os.getenv("FLIGHT_URL"), os.getenv("F_API_KEY"))
notification_manager = NotificationManager(os.getenv("SID"),os.getenv("SKEY"),os.getenv("ANUM"))

data = data_manager.retrieve_data()
for item in data['prices']:
    city = item['city']
    id = str(item['id'])
    iata_code = item['iataCode']
    lowest_price = item["lowestPrice"]
    if iata_code == "":
        data = flight_search.retrieve_iata_code(name=city)
        code = data["locations"][0]['code']

        payload = {
            "price": {
                "iataCode": code
            }
        }
        results = data_manager.update_data(id, payload)
        print(id, city, code, results)

        search_results = flight_search.search(code, from_date=start_date, to_date=end_date)
        if search_results.price < lowest_price:
            message = f"Low Price Alert! Only ${search_results.price} to fly from {search_results.from_city}-{search_results.code} to {search_results.to_city}-{search_results.to_code}"
            result = notification_manager.send_sms(message, "+233XXXXXXXX")
            print(result)
    else:
        search_results = flight_search.search(iata_code, start_date, end_date)
        print(id, iata_code, city,search_results.from_city,lowest_price,search_results.price)
        if search_results.price < lowest_price:
            message = f"Low Price Alert! Only ${search_results.price} to fly from {search_results.from_city}-{search_results.code} to {search_results.to_city}-{search_results.to_code}"
            result = notification_manager.send_sms(message, "+233XXXXXXXX")
            print(result)


