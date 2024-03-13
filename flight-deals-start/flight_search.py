import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = 'https://api.tequila.kiwi.com/v2'
        self.endpoint = ''
        self.params = {}
        self.api_key = 
        self.headers = { 
            "apikey": self.api_key,
            }
    
    def get(self):
        url = self.url + self.endpoint
        self.response = requests.get(url=url)
        return self.response
    