import requests
class DataManager:

    def __init__(self):
        self.sheety_url="https://api.sheety.co/f51728668cc6d9f9988bb2e676485cd7/myFlightDeals/prices"
        self.response=requests.get(url=self.sheety_url)
        self.response.raise_for_status()

    def get_data(self):
        self.my_data=self.response.json()
        self.my_data=self.my_data['prices']
        return self.my_data

    def update_iata_code(self,element,ele_id):
        update_response=requests.put(url=f"https://api.sheety.co/f51728668cc6d9f9988bb2e676485cd7/myFlightDeals/prices/{ele_id}",json=element)
        print(update_response.status_code)
