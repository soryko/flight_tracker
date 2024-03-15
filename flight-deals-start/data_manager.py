import requests
import json

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, token, data=""):
        self.url = 'https://api.sheety.co/276edceaa3e67d4611d5bd79ffe6a781/myFlightDeals/prices'
        self.bearer = token
        self.data = data
        self.headers = {"Authorization": f"Bearer {self.bearer}"}
    def get_sheet(self):
        self.get_response = requests.get(url=self.url, headers=self.headers).json()
        return self.get_response
    def post_sheet(self):
        self.post_response = requests.put(url=self.url,headers=self.headers, json=self.data)
        return self.post_response