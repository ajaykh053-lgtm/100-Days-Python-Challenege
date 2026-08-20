import os
import requests
import datetime as dt
from dotenv import load_dotenv
# from requests.auth import HTTPBasicAuth
from flask import Flask
load_dotenv()
GENDER = "male"
WEIGHT_KG = 50
HEIGHT_CM = 172
AGE = 19
PIXELA_USERNAME = "ajaykh7"
PIXELA_TOKEN = "sjhgdr43iuwfb84538n"
GRAPH_ID = "graph2"
# basic = HTTPBasicAuth(username=os.environ["USERNAME"], password=os.environ["PASSWORD"])
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
# print(data)
today_date = dt.date.today().strftime("%d/%m/%Y")
# print(today_date)
now_time = dt.datetime.now().strftime("%H:%M:%S")
# print(now_time)
exercise_name = data["name"].title()
# print(exercise_name)
duration = data["duration_min"]
# print(duration)
calories = data["nf_calories"]
# print(calories)
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
# print(sheety_respones.text)
#Add Graph
graph_endpoint = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling",  # Nmae of the graph
    "unit": "Hours",  # Measurement for graph
    "type": "float",  # int float ot str
    "color": "shibafu",  # colour you want choose specifially in japanese
}
header = {"X-USER-TOKEN": PIXELA_TOKEN}
respones = requests.post(url=graph_endpoint, json=graph_config, headers=header)
print(respones.text)
#ADD PIxel
today = dt.date.today().strftime("%Y%m%d")
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_data = {
    "date": f"{today}",
    "quantity": f"{duration/60}",
}
respones = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=header)
print(respones.text)
#https://pixe.la/@ajaykh7