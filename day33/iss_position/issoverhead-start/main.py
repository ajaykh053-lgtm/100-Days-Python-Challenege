import os
import time
import smtplib
import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
MY_LAT = 15.156661  # Your latitude
MY_LONG = 76.930862  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
# print(iss_latitude)
iss_longitude = float(data["iss_position"]["longitude"])
# print(iss_longitude)
# MY_LAT = iss_latitude
# MY_LONG = iss_longitude
# Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5 :
        return True
    else:
        return False

def is_night():
    print(is_iss_overhead())
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    # print(response.status_code)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    # print(sunrise)
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # print(sunset)
    time_now = datetime.now().hour
    # print(time_now)
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
    # is_iss_overhead()
    # is_night()
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=os.environ['my_email'], password=os.environ['password'])
        connection.sendmail(
                from_addr=os.environ['my_email'],
                to_addrs="ajaykh053@gmail.com",
                msg="Subject : The ISS is close to your current position\n\n Hey dude the the satelite is about go thorugh your way soon.\n\nDon't miss the oportunity seen  that this may take while to another several days."
            )
