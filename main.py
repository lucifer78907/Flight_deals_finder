#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
data=DataManager()
sheet_data=data.get_data()
#check the sheet data for empty iata codes
for elements in sheet_data:
    if elements['iataCode']=='':
        from flight_search import FlightSearch
        f_search=FlightSearch()
        city_code=f_search.flight_data(elements['city'])
        elements['iataCode']=city_code

pprint(sheet_data)