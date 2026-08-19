import os
import requests
from time import sleep
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
info_list = []
price_list = []
address_list = []
info_list.clear()
price_list.clear()
address_list.clear()
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
}
respones = requests.get(url=f"{os.environ['CLONE_URL']}", headers=header)
# pprint(respones.text)
soup = BeautifulSoup(respones.text, "html.parser")
Adress_Info_list = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
for Info in Adress_Info_list:
    info_list.append(Info.get_text().strip().replace("/n", ""))
# print(info_list)
Adress_price_list = soup.find_all(
    name="span", class_="PropertyCardWrapper__StyledPriceLine"
)
for price in Adress_price_list:
    cost = price.get_text().split("+")[0]
    price = cost.split("/mo")[0]
    price_list.append(price)
# print(price_list)
address_link_list = soup.find_all(name="a", class_="property-card-link")
for address in address_link_list:
    address_list.append(address.get(key="href"))
# print(address_list)
# print(len(address_list))
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
# include double -- for command line argument to Chrome.
chrome_option.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_option)
driver.get(url=os.environ["FORM_LINK"])
for i in range(len(address_list)):
    sleep(3)
    info_input = driver.find_element(
        by=By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
    )
    price_input = driver.find_element(
        by=By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
    )
    address_input = driver.find_element(
        by=By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
    )
    submit_btn = driver.find_element(by=By.CSS_SELECTOR, value=".Y5sE8d")
    info_input.send_keys(f"{info_list[i]}")
    sleep(1)
    price_input.send_keys(f"{price_list[i]}")
    sleep(1)
    address_input.send_keys(f"{address_list[i]}")
    sleep(1)
    driver.execute_script("arguments[0].click();", submit_btn)
    another_submit = driver.find_element(
        by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a"
    )
    driver.execute_script("arguments[0].click();", another_submit)
