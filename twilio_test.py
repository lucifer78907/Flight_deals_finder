import requests
from twilio.rest import Client
# "lon": 77.6833,
# "lat": 29.4667,
account_sid = "AC682f47acde6b0e9200f2e76c183bae7d"
auth_token = "63da16a3c6254620f732cddbf445bd13"
api_key = "181416a906abc3d9beb7fdcf721e9962"

parameters = {
    "lon": 76.861732,
    "lat": 11.421430,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_data_hourly=weather_data["hourly"]
will_rain=True
for i in range(1,13):
    for elements in weather_data_hourly[i]['weather']:
        if elements['id']<700 :
            will_rain=True


if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Or bhai kya haal h verrreee🥰",
        from_='+18563475338',
        to='+918171768882'
    )

    print(message.status)