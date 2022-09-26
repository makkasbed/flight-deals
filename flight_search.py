import requests


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

    def search(self, code, from_date, to_date):
        url = self.url + "/search?fly_from=" + code + "&date_from=" + from_date + "&date_to=" + to_date

        payload = {}
        headers = {
            'apikey': self.api_key
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()
