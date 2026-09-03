import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

load_dotenv()
SIMILAR_NAME = "chefsteps"


class InstaFollower:
    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)
        self.user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        # include double -- for command line argument to Chrome.
        self.chrome_option.add_argument(f"--user-data-dir={self.user_data_dir}")
        self.driver = webdriver.Chrome(options=self.chrome_option)
        self.wait = WebDriverWait(self.driver, 3)

    def login(self):
        self.driver.get(url=f"{os.environ['SHAREANAN']}/login")
        Email_input = self.driver.find_element(by=By.NAME, value="username")
        Email_input.send_keys(os.environ["EMAIL"])
        sleep(1)
        pass_input = self.driver.find_element(by=By.NAME, value="password")
        pass_input.send_keys(os.environ["PASSWORD"])
        sleep(1)
        Login_btn = self.driver.find_element(
            by=By.CSS_SELECTOR, value=".naan-btn-primary"
        )
        Login_btn.click()
        self.wait.until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, "naan-popup-card"))
        )
        self.save_credentail = self.driver.find_element(
            by=By.CLASS_NAME, value="naan-popup-dismiss"
        )
        self.driver.execute_script("arguments[0].click();", self.save_credentail)
        sleep(1)
        self.wait.until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, "naan-popup-overlay"))
        )
        self.dismiss_notification = self.driver.find_element(
            by=By.CLASS_NAME, value="naan-popup-dismiss"
        )
        self.driver.execute_script("arguments[0].click();", self.dismiss_notification)

    def find_followers(self):
        self.search = self.driver.find_element(by=By.CLASS_NAME, value="naan-rail-item")
        self.driver.execute_script("arguments[0].click();", self.search)
        sleep(2)
        self.chefsteps = self.driver.find_element(
            by=By.XPATH, value="/html/body/aside/div[4]/a[1]"
        )
        self.driver.execute_script("arguments[0].click();", self.chefsteps)
        self.wait.until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, "naan-center"))
        )
        # self.driver.get(url=f"{os.environ['SHAREANAN']}/u/{SIMILAR_NAME}/followers")
        self.follower = self.driver.find_element(
            by=By.CSS_SELECTOR, value=".naan-followers-link"
        )
        self.driver.execute_script("arguments[0].click();", self.follower)
        sleep(2)

    def follow(self):
        self.follower_list = self.driver.find_element(
            by=By.CSS_SELECTOR, value=".followers-scroll"
        )
        self.driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight", self.follower_list
        )
        sleep(1)
        self.follower_list.send_keys(Keys.PAGE_DOWN)
        self.follower_list.send_keys(Keys.PAGE_DOWN)
        self.follow_btn = self.driver.find_elements(
            by=By.XPATH, value="/html/body/div[2]/div/div[3]/div/button"
        )
        print(len(self.follow_btn))
        for btn in reversed(self.follow_btn):
            self.driver.execute_script(
                "arguments[0].scrollTop+=13000", self.follower_list
            )
            if "is-following" in btn.get_attribute(name="class"):  # type: ignore
                print("Your already following this person")
            else:
                self.driver.execute_script("arguments[0].click();", btn)
                print("followed new person")
                sleep(1)
