import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()


class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_profile = os.environ["CHROME_PROFILE"]
        if self.chrome_profile:
            self.chrome_option.add_experimental_option("detach", True)
            self.chrome_option.add_argument(f"--user-data-dir={self.chrome_profile}")
            self.chrome_option.add_argument("--profile-directory=Default")
        else:
            raise ValueError(
                "CHROME_PROFILE not set in .env — add your Chrome profile path."
            )

        # Remove the "Chrome is controlled by automation" bar
        self.chrome_option.add_experimental_option(
            "excludeSwitches", ["enable-automation"]
        )
        self.chrome_option.add_experimental_option("useAutomationExtension", True)
        self.chrome_option.add_argument("--disable-blink-features=AutomationControlled")
        self.chrome_option.add_argument("--disable-notifications")
        self.chrome_option.add_argument("--no-first-run")
        self.driver = webdriver.Chrome(options=self.chrome_option)
        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        self.wait = WebDriverWait(self.driver, 70)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url=os.environ["SPEED_TESTER"])
        sleep(1)
        self.driver.find_element(by=By.CSS_SELECTOR, value=".css-ketujc").click()
        self.wait.until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-pztkm1"))
        )
        self.down = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3",
        )
        self.up = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3",
        )
        # print(f"Down : {self.down.text}")
        # print(f" Up : {self.up.text}")
        return self.down.text, self.up.text

    def tweet_at_provider(self, Message):
        self.driver.get(url=os.environ["Y"])
        self.login_btn = self.driver.find_element(
            by=By.CLASS_NAME, value="y-login-link"
        )
        self.driver.execute_script("arguments[0].click();", self.login_btn)
        self.wait.until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, "y-login-wrap"))
        )
        self.email_input = self.driver.find_element(by=By.ID, value="email")
        self.email_input.clear()
        self.email_input.send_keys(os.environ["EMAIL"])
        self.password_input = self.driver.find_element(by=By.ID, value="password")
        self.password_input.clear()
        self.password_input.send_keys(os.environ["PASSWORD"])
        self.login = self.driver.find_element(
            by=By.CSS_SELECTOR, value=".y-btn-primary"
        )
        self.login.click()
        self.wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, "x-app")))
        self.post_btn = self.driver.find_element(
            by=By.CSS_SELECTOR, value=".x-post-cta"
        )
        self.post_btn.click()
        self.wait.until(
            ec.presence_of_all_elements_located((By.CLASS_NAME, "y-modal-card"))
        )
        self.Write_section = self.driver.find_element(
            by=By.CSS_SELECTOR, value=".y-modal-compose-row .x-compose"
        )
        self.Write_section.send_keys(f"{Message}")
        self.post_btn = self.driver.find_element(
            by=By.CSS_SELECTOR, value=".post-button"
        )
        self.post_btn.click()
