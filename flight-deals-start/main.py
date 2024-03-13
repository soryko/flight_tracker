#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
import flight_search
from dotenv import load_dotenv
import os

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
     
if __name__ == "__main__":
    main()