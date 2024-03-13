#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
import flight_search
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def main():
    sheet = DataManager()
    sheet.get()
    configure()
    bearer = "Bearer " + os.getenv(bearer)
    sheet.bearer = bearer
if __name__ == "__main__":
    main()