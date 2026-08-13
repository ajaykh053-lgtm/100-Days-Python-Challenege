from selenium import webdriver
from selenium.webdriver.common.by import By
i=0
j=0
# Kepp the browser open after program runs
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)

python = "https://www.python.org/"
# amazon="https://www.amazon.in/Aluminium-Ergonomic-Adjustable-Tabletop-Compatible/dp/B0F7B1W5MN?th=1"
driver.get(url=python)
# finding  element by class name
# item_price = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")
# print(f"The price is {item_price.text}")
# using NAME
# search_bar = driver.find_element(by=By.NAME, value="q")
# # print(search_bar.get_attribute("placeholder"))
# Using ID
# button = driver.find_element(By.ID, value="submit")
# # print(button.size)
# Using CSSSELECTOR
# a_tag = driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
# print(a_tag.text)
# ele = driver.find_element(By.CSS_SELECTOR,value=".download-widget p")
# print(ele.text)
# Using XPATH
# print(driver.find_element(By.XPATH,value="/html/body/div/header/div/div[3]/div/ul[1]/li/a/span"))

event_time = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
events = {}
for n in range(len(event_time)):
    events[n]={
        "time" : event_time[n].text,
        "name" : event_name[n].text,
    }
# # # driver.close()
# driver.quit()
