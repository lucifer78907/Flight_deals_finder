from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
data = DataManager()
sheet_data = data.get_data()
my_flight_data=FlightData()
my_flight_data.set_time()
# check the sheet data for empty iata codes
for elements in sheet_data:
    if elements['iataCode'] == '':
        from flight_search import FlightSearch

        f_search = FlightSearch()
        city_code = f_search.flight_data(elements['city'])
        elements['iataCode'] = city_code
        ele_dict = {
            "price": {
                "iataCode": elements['iataCode']
            }
        }
        ele_id = elements['id']
        data.update_iata_code(ele_dict, ele_id)

for elements in sheet_data:
        my_flight_data.print_data(elements['iataCode'])
        departue_date=my_flight_data.return_departure_date(elements['iataCode'])
        lowest_price=my_flight_data.return_price(elements['iataCode'])
        if elements['lowestPrice']>lowest_price:
            notify_me = NotificationManager()
            notify_me.send_message(lowest_price,"London-LON",elements['city'],elements['iataCode'],departue_date)
