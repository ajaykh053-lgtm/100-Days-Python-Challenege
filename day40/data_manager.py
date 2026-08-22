import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from pprint import pprint
# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]

class DataManager:

    def __init__(self):
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.Authorization = {"Authorization": "Bearer ierf83743ct4b43i8rc"}
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.Authorization)
        pprint(response.text)
        data = response.json()["prices"]
        self.destination_data = data
        return self.destination_data
    def get_user_data(self):
        respones = requests.get(url=os.environ['SHEETY_USER_ENDPOINT'],headers=self.Authorization)
        pprint(respones.text)
        data = respones.json()['user']
        return data

    # ==================== Updated the price in the spreadsheet ====================

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
            json=new_data,
            headers=self.Authorization,
        )
        # print(response.text)