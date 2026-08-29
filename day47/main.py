import os
import smtplib
import requests
from pprint import pprint
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()
Practice_URL = "https://appbrewery.github.io/instant_pot/"
live_url = ["https://www.amazon.in/Portronics-Wireless-Bluetooth-Connectivity-Rechargeable/dp/B0BG8LZNYL?th=1","https://www.amazon.in/Aluminium-Ergonomic-Adjustable-Tabletop-Compatible/dp/B0F7B1W5MN?th=1"]
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
}
BUY_PRICE = [630,250]
for num in range(0,2):
    respones = requests.get(url=live_url[num], headers=header)
    # pprint(respones.text)
    soup = BeautifulSoup(respones.text, "html.parser")
    # pprint(soup)
    Item_price = soup.find(name="span", class_="a-price-whole") 
    # print(Item_price.getText())
    price_as_float = float(Item_price.getText()) #type:ignore#type:ignore
    # print(price_as_float)
    title = soup.find(name="span",class_="a-size-large product-title-word-break").getText() #type:ignore
    # print(title)
    if price_as_float < BUY_PRICE[num]:
        # message = f"{title} is now\n only for Rupee-{price_without_currency}"
        message = f"{title} is now\n only for ₹ {price_as_float}. "
        connection = smtplib.SMTP(host=os.environ["SMTP_ADDRESS"], port=587)
        connection.starttls()
        result = connection.login(user=os.environ["MY_EMAIL"], password=os.environ["PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["MY_EMAIL"],
            to_addrs="ajaykh053@gmail.com", 
            msg=f"Subject : Amazon Price Alert!\n\n{message}\n{live_url[num]}".encode("utf-8"),
        )
        connection.close()
