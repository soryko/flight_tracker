#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
import flight_search
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def main():
    configure()
    token = os.getenv('sheet_token')
    sheet = DataManager(token=token)
    sheet.get_sheet()
    response = sheet.get_response
    rows = response["prices"]
    country_codes = []
    for row in rows:
        country_codes.append(row["iataCode"])
  
if __name__ == "__main__":
    main()