import requests
from twilio.rest import Client

class NotificationManager:

    def __init__(self):
        self.account_sid = "AC682f47acde6b0e9200f2e76c183bae7d"
        self.auth_token = "e730072a6ffdfd2fcd67bbc0c689084a"

    def send_message(self,price,city_from,city_to,city_to_iata,dp_date):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages \
            .create(
            body=f"Low price Alert only ${price} \n from {city_from} to "
                 f"{city_to}-{city_to_iata}\n on {dp_date}",
            from_='+18563475338',
            to='+918171768882'
        )

        print(message.status)