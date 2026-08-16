import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.environ["TWILIO_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
WEATHER_API = os.environ["WEATHER_API"]
API_KEY = os.environ["API_KEY"]
#mine
# "lat": 14.403139,
# "lon": 76.437060,this is where i live here not raining
# 25.0759
# 121.3145this is where currently raining todaay now
#if you did't gt email try to find place where its gonna rain from google add there lat & lon you will get email for sure.
parameter = {
    "lat": 14.403139,
    "lon": 76.437060,
    "cnt": 4,
    "units": "metric",
    "appid": API_KEY,
}
respones = requests.get(url=WEATHER_API, params=parameter)
respones.raise_for_status()
weather_data = respones.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella ☔",
        from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
        to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}',
    )
    print(message.status)