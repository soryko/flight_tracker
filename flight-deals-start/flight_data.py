import pandas as pd
import os
from datetime import datetime

TODAY = datetime.now().strftime("%d-%m-%Y")

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,data):
        self.data = data
        self.price = data['price']
        self.origin_city = data["route"][0]["cityFrom"]
        self.origin_airport = data["route"][0]["flyFrom"]
        self.destination_city = data["route"][0]["cityTo"]
        self.destination_airport = data["route"][0]["flyTo"]
        self.out_date = data["route"][0]["local_departure"].split("T")[0]
        self.return_date = data["route"][1]["local_departure"].split("T")[0]

    def get_flight_data(self):
        flight_data = [self.price, 
                       self.origin_city, 
                       self.origin_airport,
                       self.destination_city,
                       self.destination_airport,
                       self.out_date,
                       self.return_date]
        
        self.df = pd.DataFrame([flight_data], columns=["price","origin_city", "origin_airport", "destination_city", "destination_airport", "out_date", "return_date"])
        return flight_data

    def get_csv(self):
        filename = f"{TODAY}_flightDeals.csv"
        if os.path.exists(filename):
            df = pd.read_csv(filename)
            df = df.append(self.df, ignore_index=True)

        else:
            df = self.df
        
        df.to_csv(filename, index=False)
        print("csv created/updated")

'''        for row in df:
            self.id = row["id"]
            self.price = row["price"]
            self.origin_city = row["route"][0]["cityFrom"]
            self.origin_airport = row["route"][0]["flyFrom"]
            self.destination_airport = row["route"][0]["cityTo"]
            self.out_date = row["route"][0]["local_departure"].split("T")[0]
            self.return_date = row["route"][1]["local_departure"].split("T")[0]
            rows.append(self.price, self.origin_city, self.origin_airport, self.destination_airport, self.out_date, self.return_date)'''