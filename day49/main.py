import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()
# ----------------  Step 1 - Setup, Chrome Profile and Basic Navigation ----------------


chrome_option = webdriver.ChromeOptions()

# Keep the browser open if the script finishes or crashes.
# If True, you need to *manually* QUIT Chrome before you re-run the script.

chrome_option.add_experimental_option("detach", True)

# Create a folder for the Chrome Profile Selenium will use every time.

user_data_dir = os.path.join(os.getcwd(), "chrome_profileforday49")

# include double -- for command line argument to Chrome.

chrome_option.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_option)

# Navigate to site.

driver.get(url=os.environ["GYM_URL"])

# Logining into the Page.
Login_join = driver.find_element(by=By.CLASS_NAME, value="Home_heroButton__3eeI3")
Login_join.click()

# Using WebDriverWait operations to wait for some time to load website
wait = WebDriverWait(driver=driver, timeout=2)

# Sample Login details
# Email = driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div[1]/div[1]/p[1]")
# password = driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div[1]/div[1]/p[2]")
# # print(Email_text)
# # print(password.text)
# Email_id = Email.text.split(": ",1)[1]
# Password = password.text.split(": ",1)[1]
# # print(Email_id)
# # print(Password)

#Filling the from.
Enter_email = driver.find_element(by=By.ID, value="email-input")
Enter_email.send_keys(os.environ["ACCOUNT_EMAIL"])
Enter_pass = driver.find_element(by=By.ID, value="password-input")
Enter_pass.send_keys(os.environ["ACCOUNT_PASSWORD"])
#Click to Login
Submit_login = driver.find_element(by=By.ID, value="submit-button")
Submit_login.click()
# Wait for schedule page to load
wait.until(ec.presence_of_element_located((By.ID,"schedule-page")))