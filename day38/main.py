import os
import requests
import datetime as dt
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()
GENDER = "male"
WEIGHT_KG = 50
HEIGHT_CM = 172
AGE = 19
basic = HTTPBasicAuth(username=os.environ["USERNAME"], password=os.environ["PASSWORD"])
exercise_text = input("Tell me which exercises you did: ")
header = {
    "Content-Type": "application/json",
    "x-app-id": os.environ["APP_ID"],
    "x-app-key": os.environ["API_KEY"],
}
params = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER,
}
respones = requests.post(
    url=f"{os.environ['EXERCISE_ENDPOINT']}", json=params, headers=header
)
data = respones.json()["exercises"][0]
print(data)
today_date = dt.date.today().strftime("%d/%m/%Y")
print(today_date)
now_time = dt.datetime.now().strftime("%H:%M:%S")
print(now_time)
exercise_name = data["name"].title()
print(exercise_name)
duration = data["duration_min"]
print(duration)
calories = data["nf_calories"]
print(calories)
sheet_inputs = {
    "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": exercise_name,
        "duration": duration,
        "calories": calories,
    }
}
Authorization = {"Authorization": "Bearer cw4i7gvq3i34438o437"}
sheety_respones = requests.post(
    url=os.environ["SHEETY_ENDPOINT"],
    json=sheet_inputs,
    headers=Authorization,
)
print(sheety_respones.text)
