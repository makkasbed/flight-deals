import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self, url):
        self.url = url

    def retrieve_data(self):
        payload = {}
        headers = {}
        response = requests.request("GET", self.url, headers=headers, data=payload)
        return response.json()

    def update_data(self, id, payload):
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("PUT", self.url+"/"+id, headers=headers, json=payload)
        return response.json()
