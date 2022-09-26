import requests
from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    def retrieve_iata_code(self, name):
        url = self.url + "/locations/query?term=" + name

        payload = {}
        files = {}
        headers = {
            'apikey': self.api_key
        }
        response = requests.request("GET", url, headers=headers, data=payload, files=files)
        return response.json()

    def search(self, code, from_date, to_date, origin="LON"):
        url = self.url + "/search?fly_from=" + origin + "&fly_to=" + code + "&date_from=" + str(
            from_date) + "&date_to=" + str(to_date)

        payload = {}
        headers = {
            'apikey': self.api_key
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        try:
            data = response.json()["data"][0]
        except IndexError:
            return None

        flight_data = FlightData(
           price=data["price"],
           code=data["flyFrom"],
           from_city=data["route"][0]["cityFrom"],
           to_city=data["route"][0]["cityTo"],
           to_code=data["flyTo"]
        )
        return flight_data

