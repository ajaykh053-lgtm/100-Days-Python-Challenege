import requests

parameters = {"amount": 10, "type": "boolean","category": 31,"difficulty" : "easy"}
respones = requests.get(url="https://opentdb.com/api.php?amount=10&category=31&difficulty=easy&type=boolean", params=parameters)
respones.raise_for_status()
question_data = respones.json()["results"]
