import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import *  # type: ignore
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

load_dotenv()
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
wait = WebDriverWait(driver=driver, timeout=3)
driver.get(os.environ["TINDER"])
sleep(2)
# Step 1 — open the login modal and click Facebark
create_acc_btn = driver.find_element(by=By.CLASS_NAME, value="tindog-cta-create")
create_acc_btn.click()
wait.until(ec.presence_of_element_located((By.CLASS_NAME, "modal-body")))
loginwithafacebook_btn = driver.find_element(by=By.CSS_SELECTOR, value=".btn-facebark")
# print(loginwithafacebook_btn.tag_name)
driver.execute_script("arguments[0].click();", loginwithafacebook_btn)

# Step 2 — Facebark login in popup
base_window = driver.window_handles[0]
facebark_window = driver.window_handles[1]
driver.switch_to.window(facebark_window)
# print(driver.title)
wait.until(ec.presence_of_element_located((By.CLASS_NAME, "login-wrapper")))
email_input = driver.find_element(by=By.ID, value="email")
email_input.clear()
email_input.send_keys(os.environ["EMAIL"])
password_input = driver.find_element(by=By.ID, value="pass")
password_input.clear()
password_input.send_keys(os.environ["PASSWORD"])
login_btn = driver.find_element(by=By.CSS_SELECTOR, value=".login-card button")
login_btn.click()
driver.switch_to.window(base_window)
# print(driver.title)

# Step 3 — dismiss the three popups
sleep(3)
driver.find_element(by=By.CLASS_NAME, value="btn-primary").click()  # Allow_location_btn
sleep(1)
driver.find_element(
    by=By.CLASS_NAME, value="btn-secondary"
).click()  # Allow_notification_btn
sleep(1)
driver.find_element(by=By.CLASS_NAME, value="btn-primary").click()  # Accept_cookies_btn
sleep(1)
# Step 4 — like all 20 dogs
liked_dog=0
for n in range(20):
    sleep(3)
    # Check for match popup first
    try:
        match = driver.find_element(
            By.CSS_SELECTOR, 'a[href="/services/tindog/dismiss-match"]'
        )
        driver.execute_script("arguments[0].click();", match)
        print("Match dismissed, going back for more...")
        sleep(2)
        continue  # skip this iteration's like, start fresh
    except NoSuchElementException:
        pass  # No popup, safe to like
    # Like the current dog
    try:
        sleep(3)
        like_btn = driver.find_element(By.CLASS_NAME, "btn-like")
        like_btn.click()
        liked_dog += 1
        print(f"Liked dog #{liked_dog}")
    except (NoSuchElementException, ElementClickInterceptedException):
        print("Like button not found or intercepted waiting 5 seconds")
        sleep(5)
    # print(n)
# driver.quit()
