import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
# include double -- for command line argument to Chrome.
chrome_option.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_option)
wait = WebDriverWait(driver,3)

driver.get(url="")
