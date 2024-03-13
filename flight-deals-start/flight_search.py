import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = 'https://api.tequila.kiwi.com/v2'
        self.endpoint = '/Search'
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
        self.adult_hand_bag = 1
        self.adult_hold_bag = 2
        self.selected_cabins = 'M'
        self.mix_with_cabins = "C"
        self.adults = 2
        self.max_fly_duration = 20
    
    def querify(self, fly_to , fly_from="FRA", currency='EUR',locale='en', selected_cabins='M', adult_hand_bag = 1, adult_hold_bag = 2, **kwargs):
        self.params = {}
        for key, value in kwargs:
            self.params[key] = value
        return self.params
    
    def get(self):
        url = self.url + self.endpoint
        self.response = requests.get(url=url, self.params)
        return self.response
    