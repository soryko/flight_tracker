import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = 'https://api.tequila.kiwi.com/v2'
        self.endpoint = ''
        self.params = {}
        self.api_key = ""
        self.headers = { 
            "apikey": self.api_key,
            }
        self.fly_from = "FRA"
        self.fly_to = ""
        self.nights_in_dst_from = 4
        self.currency = 'EUR'
        self.locale = 'en'
        self.max_stopovers = 2
        self.price_from = 0
        self.price_to = 1000
        self.adult_hand_bag = ''
        self.adult_hold_bag = ''
        self.selected_cabins = 'M'
        self.mix_with_cabins = "C"
        self.adults = 2
        self.max_fly_duration = 20
    
    def get(self):
        url = self.url + self.endpoint
        self.response = requests.get(url=url)
        return self.response
    