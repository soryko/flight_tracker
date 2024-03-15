#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from dotenv import load_dotenv
import os
from flight_data import FlightData
import json

def configure():
    load_dotenv()

def main():
    #get tokens/keys
    configure()
    token = os.getenv('sheet_token')
    sheet = DataManager(token=token)
    sheet.get_sheet()
    #get for things to check
    response = sheet.get_response
    rows = response["prices"]
    codes_and_price = []
    for row in rows:
        codes_and_price.append({row["iataCode"]: row["lowestPrice"]})
    #get flight search api 
    api_key = os.getenv('api_key')
    print(codes_and_price)
    search = FlightSearch(api_key=api_key)
    for code in codes_and_price:
        ctry_code = "".join(list(code))
        fly_to = ctry_code
        search.querify(fly_to=fly_to)
        #print(search.params)
        response = search.get_flights()
        response.raise_for_status()
        data = response.json()['data'][0]
        flight_ = FlightData(data)
        flight_data = flight_.get_flight_data()
        flight_.get_csv()
        print(flight_data.df.head())
        break
        #print(push_data)
'''        sheet_data = {
            "price": {
                "iataCode": ctry_code
            }
        }
        if flight_data.price < code[ctry_code]:
            update_sheet = DataManager(token=token,data=sheet_data)
            update_sheet.post_sheet()

        FlightData(push_data).get_csv(push_data)
'''

        
if __name__ == "__main__":
    main()