import requests
class DataManager:

    def __init__(self):
        self.sheety_url="https://api.sheety.co/f51728668cc6d9f9988bb2e676485cd7/myFlightDeals/prices"
        self.response=requests.get(url=self.sheety_url)
        self.response.raise_for_status()

    def get_data(self):
        self.my_data=self.response.json()
        return self.my_data