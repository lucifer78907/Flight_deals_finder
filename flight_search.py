import requests

API_KEY = "nQl0yIRUBg8IHjngw7eirQxfeiqZSvgY"
flight_data_url = "https://tequila-api.kiwi.com/locations/query"


class FlightSearch:
    def __init__(self):
        self.header = {
            "apikey": API_KEY,
        }

    def flight_data(self, city):
        self.parameters = {
            "term": city
        }
        response = requests.get(url=flight_data_url, params=self.parameters, headers=self.header)
        new_data = response.json()
        return new_data['locations'][0]['code']
