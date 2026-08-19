import os
import requests
import datetime
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = os.environ["STOCK_ENDPOINT"]
STOCK_API_KEY = os.environ["STOCK_API_KEY"]
NEWS_ENDPOINT = os.environ["NEWS_ENDPOINT"]
NEWS_API_KEY = os.environ["NEWS_API_KEY"]
TWILIO_SID = os.environ["TWILIO_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_VIRTUAL_NUMBER = os.environ["TWILIO_VIRTUAL_NUMBER"]
TWILIO_WHATSAPP_NUMBER = os.environ["TWILIO_WHATSAPP_NUMBER"]
TWILIO_VERIFIED_NUMBER = os.environ["TWILIO_VERIFIED_NUMBER"]
STOCKSPARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
stock_respones = requests.get(url=STOCK_ENDPOINT, params=STOCKSPARAMS)
stock_price = stock_respones.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_price.items()]

yesterday_data = stock_data_list[0]
daybefore_yesterday_data = stock_data_list[1]

yesterday_closing_price = float(yesterday_data["4. close"])
daybefore_yesterday_closing_price = float(daybefore_yesterday_data["4. close"])
diff_stock_price = abs(yesterday_closing_price - daybefore_yesterday_closing_price)

diff_percent_yesterday_closing_price = (
    diff_stock_price / yesterday_closing_price
) * 100
print(diff_percent_yesterday_closing_price)
if diff_percent_yesterday_closing_price > 0.1:
    toady_date = datetime.date.today()
    yesterday_date = toady_date - datetime.timedelta(days=1)
    newsparams = {
        "q": COMPANY_NAME,
        "apikey": NEWS_API_KEY,
        "from": f"{yesterday_date}",
        "to": f"{yesterday_date}",
        "sortBy": "popularity",
        "language": "en",
    }
    newsrespones = requests.get(url=NEWS_ENDPOINT, params=newsparams)
    articles = newsrespones.json()["articles"]
    three_article = articles[:3]
    formtted_articles = [
        f"Title : {articles["title"]} \n Description : {articles["description"]}"
        for articles in three_article
    ]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for articles in formtted_articles:
        message = client.messages.create(
            body=f"{articles}",
            to=f"whatsapp:{TWILIO_VERIFIED_NUMBER}",
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
        )
        print(message.status)
