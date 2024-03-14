import pandas as pd

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,data):
        self.data = data

    def convert_to_df(self,data):
        self.df = pd.read_json(data)
        return self.df
    
    def get_flight_data(self,df):
        self.price = 
        self.origin_city =
        self.origin_airport =
        self.destination_airport = 
        self.out_date = 
        self.return_date =
