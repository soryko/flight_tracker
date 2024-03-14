import requests
from datetime import datetime, timedelta

TODAY = datetime.now()
SIXMONTHS = TODAY + timedelta(days=180)

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,api_key):
        self.url = 'https://api.tequila.kiwi.com'
        self.endpoint = self.url + '/v2/search'
        self.key = api_key
        self.headers = { 
            "apikey": self.key,
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

    def querify(
            self, 
            fly_to, 
            date_from=TODAY.strftime('%d/%m/%Y'), 
            date_to=SIXMONTHS.strftime('%d/%m/%Y'), 
            fly_from="FRA", 
            currency='EUR',
            locale='en', 
            **kwargs):
        self.params = {
            "date_from": date_from,
            "date_to": date_to,
            "fly_to": fly_to,
            "fly_from": fly_from,
            "curr": currency,


        }
        for key, value in kwargs:
            self.params[key] = value
        return self.params
    
    def get_flights(self):
        url = self.endpoint
        self.response = requests.get(url=url, params=self.params, headers=self.headers)
        return self.response
    
    '''           
      "locale": locale,
            "max_stopovers" :  self.max_stopovers,
            "price_from": self.price_from,
            "price_to": self.price_to,
            "adult_hand_bag": self.adult_hand_bag,
            "adult_hold_bag": self.adult_hold_bag,
            "selected_cabins": self.selected_cabins,
            "mix_with_cabins": self.mix_with_cabins,
            "adults": self.adults,
            "flight_duration": self.max_fly_duration,
            '''