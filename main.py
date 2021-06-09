from data_manager import DataManager

data = DataManager()
sheet_data = data.get_data()
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
