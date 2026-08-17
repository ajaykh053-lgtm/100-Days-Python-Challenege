# import os
# from time import sleep
# from dotenv import load_dotenv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait

# load_dotenv()


# class InternetSpeedTwitterBot:
#     def __init__(self):
#         self.chrome_option = webdriver.ChromeOptions()
#         self.chrome_profile = os.environ["CHROME_PROFILE"]
#         if self.chrome_profile:
#             self.chrome_option.add_experimental_option("detach", True)
#             self.chrome_option.add_argument(f"--user-data-dir={self.chrome_profile}")
#             self.chrome_option.add_argument("--profile-directory=Default")
#         else:
#             raise ValueError(
#                 "CHROME_PROFILE not set in .env — add your Chrome profile path."
#             )

#         # Remove the "Chrome is controlled by automation" bar
#         self.chrome_option.add_experimental_option(
#             "excludeSwitches", ["enable-automation"]
#         )
#         self.chrome_option.add_experimental_option("useAutomationExtension", True)
#         # self.chrome_option.add_argument("--disable-blink-features=AutomationControlled")
#         # self.chrome_option.add_argument("--disable-notifications")
#         # self.chrome_option.add_argument("--no-first-run")
#         self.driver = webdriver.Chrome(options=self.chrome_option)
#         self.get_internet_speed()
#         # self.driver.execute_script(
#         #     "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
#         # )
#         self.wait = WebDriverWait(self.driver, 70)
#         self.down = 0
#         self.up = 0

#     def get_internet_speed(self):
#         self.driver.get(url=os.environ["SPEED_TESTER"])
#         sleep(1)
#         self.driver.find_element(by=By.CSS_SELECTOR, value=".css-ketujc").click()
#         self.wait.until(
#             ec.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-pztkm1"))
#         )
#         self.down = self.driver.find_element(
#             by=By.XPATH,
#             value="/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3",
#         )
#         self.up = self.driver.find_element(
#             by=By.XPATH,
#             value="/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3",
#         )
#         # print(f"Down : {self.down.text}")
#         # print(f" Up : {self.up.text}")
#         return self.down, self.up

#     def tweet_at_provider(self, Message):
#         self.driver.get(url=os.environ["Y"])
#         self.login_btn = self.driver.find_element(
#             by=By.CLASS_NAME, value="y-login-link"
#         )
#         self.driver.execute_script("arguments[0].click();", self.login_btn)
#         self.wait.until(
#             ec.presence_of_all_elements_located((By.CLASS_NAME, "y-login-wrap"))
#         )
#         self.email_input = self.driver.find_element(by=By.ID, value="email")
#         self.email_input.clear()
#         self.email_input.send_keys(os.environ["EMAIL"])
#         self.password_input = self.driver.find_element(by=By.ID, value="password")
#         self.password_input.clear()
#         self.password_input.send_keys(os.environ["PASSWORD"])
#         self.login = self.driver.find_element(
#             by=By.CSS_SELECTOR, value=".y-btn-primary"
#         )
#         self.login.click()
#         self.wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, "x-app")))
#         self.post_btn = self.driver.find_element(
#             by=By.CSS_SELECTOR, value=".x-post-cta"
#         )
#         self.post_btn.click()
#         self.wait.until(
#             ec.presence_of_all_elements_located((By.CLASS_NAME, "y-modal-card"))
#         )
#         self.Write_section = self.driver.find_element(
#             by=By.CSS_SELECTOR, value=".y-modal-compose-row .x-compose"
#         )
#         self.Write_section.send_keys(f"{Message}")
#         self.post_btn = self.driver.find_element(
#             by=By.CSS_SELECTOR, value=".post-button"
#         )
#         self.post_btn.click()
import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)

        # ✅ FIX: Use your REAL Chrome profile from .env
        # Chrome must be fully closed before running this script
        chrome_profile = os.environ.get("CHROME_PROFILE")
        if chrome_profile:
            self.chrome_option.add_argument(f"--user-data-dir={chrome_profile}")
            self.chrome_option.add_argument("--profile-directory=Default")
        else:
            raise ValueError("CHROME_PROFILE not set in .env — add your Chrome profile path.")

        # Remove the "Chrome is controlled by automation" bar
        self.chrome_option.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_option.add_experimental_option("useAutomationExtension", False)
        self.chrome_option.add_argument("--disable-blink-features=AutomationControlled")
        self.chrome_option.add_argument("--disable-notifications")
        self.chrome_option.add_argument("--no-first-run")

        self.driver = webdriver.Chrome(options=self.chrome_option)

        # Patch the webdriver flag so sites can't detect Selenium
        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )

        self.wait = WebDriverWait(self.driver, 70)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(os.environ["SPEED_TESTER"])

        # Wait for the Go button and click it
        start_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".css-ketujc"))
        )
        start_btn.click()

        # Wait for results to appear
        self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".css-pztkm1"))
        )
        sleep(3)  # Let the final reading settle

        self.down = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3"
        )
        self.up = self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3"
        )
        return self.down, self.up

    def tweet_at_provider(self, message):
        # Navigate to X — your Chrome profile means you're ALREADY logged in
        self.driver.get("https://x.com/home")

        # Confirm the home feed loaded (proves we're logged in)
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='primaryColumn']"))
        )
        sleep(1)

        # Click the Post / Compose button in the sidebar
        post_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[data-testid='SideNav_NewTweet_Button']")
            )
        )
        post_btn.click()

        # Wait for the compose box and type the message
        text_area = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[data-testid='tweetTextarea_0']")
            )
        )
        text_area.send_keys(message)
        sleep(1)  # Small pause so X registers the text

        # Click the Post button inside the compose modal
        send_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "[data-testid='tweetButtonInline']")
            )
        )
        send_btn.click()
        print("✅ Tweet posted successfully!")

    def quit(self):
        self.driver.quit()