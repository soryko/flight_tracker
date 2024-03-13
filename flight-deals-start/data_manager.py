import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = 'https://api.sheety.co/276edceaa3e67d4611d5bd79ffe6a781/myFlightDeals/prices'
        self.data = ''
    def get(self):
        self.get_response = requests.get(url=self.url)
        return self.get_response
    def post(self):
        self.post_response = requests.get(url=self.url, json=self.data)
        return self.post_response