import datetime as dt

import requests

API_ENDPOINT_URL="https://tequila-api.kiwi.com/v2/search"
API_KEY="nQl0yIRUBg8IHjngw7eirQxfeiqZSvgY"
header_param={
    "apikey":API_KEY
}
class FlightData:

    def __init__(self):
        self.price=0
        self.departure_airport_code="LON"
        self.departure_city="London"

    def set_time(self):
        self.today=dt.datetime.now()
        self.from_date=self.today.strftime("%d/%m/%Y")
        self.date_range=self.today+dt.timedelta(days=180)
        self.to_date=self.date_range.strftime("%d/%m/%Y")

    def print_data(self,city):
        self.user_param = {
            "fly_from": self.departure_airport_code,
            "fly_to": city,
            "date_from":self.from_date,
            "date_to":self.to_date,
            "curr":"USD"
        }
        response=requests.get(url=API_ENDPOINT_URL,params=self.user_param,headers=header_param)
        data=response.json()
        new_data=data['data'][0]
        print(city,f" ${new_data['price']}")
        temp=new_data['utc_departure'].split('T')
        self.departure_date=temp[0]
        print(self.departure_date)

    def return_price(self,city_iata):
        self.user_param = {
            "fly_from": self.departure_airport_code,
            "fly_to": city_iata,
            "date_from": self.from_date,
            "date_to": self.to_date,
            "curr": "USD"
        }
        response = requests.get(url=API_ENDPOINT_URL, params=self.user_param, headers=header_param)
        data = response.json()
        new_data = data['data'][0]
        return new_data['price']

    def return_departure_date(self,city):
        self.user_param = {
            "fly_from": self.departure_airport_code,
            "fly_to": city,
            "date_from": self.from_date,
            "date_to": self.to_date,
            "curr": "USD"
        }
        response = requests.get(url=API_ENDPOINT_URL, params=self.user_param, headers=header_param)
        data = response.json()
        new_data = data['data'][0]
        print(city, f" ${new_data['price']}")
        temp = new_data['utc_departure'].split('T')
        self.departure_date = temp[0]
        return self.departure_date