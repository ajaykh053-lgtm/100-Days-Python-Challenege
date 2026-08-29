from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
wikipedia = "https://en.wikipedia.org/wiki/Main_Page"
LAB_Report  = "https://appbrewery.github.io/fake-newsletter-signup/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

# #FInding the number of articles in wikipedia
driver.get(url=wikipedia)
num = driver.find_element(by=By.ID,value="mwDw")
print(num.text)

#Clicking on Links and Finding the links With LINK_TEXT
# all_categeries = driver.find_element(By.LINK_TEXT,value="Content portals")
# all_categeries.click()

# Finding search Bar using NAME And Sending somethig to search
# search_bar = driver.find_element(By.NAME,value="search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)
# driver.quit()
sleep(3)
driver.switch_to.new_window()
driver.get(url=LAB_Report)
first_name = driver.find_element(By.NAME,value="fName")
# print(first_name.text)
last_name = driver.find_element(By.NAME,value="lName")
# print(last_name.text)
email = driver.find_element(By.NAME,value="email")
# print(email.text)
Enter = driver.find_element(By.CSS_SELECTOR,value=".btn-block")
first_name.send_keys("AJAY")
last_name.send_keys("KH")
email.send_keys("ajaykh053@gmail.com")
Enter.click()
# print(Enter.text)