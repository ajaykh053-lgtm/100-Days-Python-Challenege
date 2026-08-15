import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()

def Booking_details(booked_count,waitlist_count,already_booked_count):
    print("--- BOOKING SUMMARY ---")
    print(f"Classes booked: {booked_count}")
    print(f"Waitlists joined: {waitlist_count}")
    print(f"Already booked/waitlisted: {already_booked_count}")
    print(
        f"Total Tuesday 6pm classes processed: {booked_count+waitlist_count+already_booked_count}"
    )
def what_happend_details(what_happend):
    print("--- DETAILED CLASS LIST ---")
    print(f"{what_happend}")
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

# Filling the from.
Enter_email = driver.find_element(by=By.NAME, value="email")
Enter_email.send_keys(os.environ["ACCOUNT_EMAIL"])
Enter_pass = driver.find_element(by=By.NAME, value="password")
Enter_pass.send_keys(os.environ["ACCOUNT_PASSWORD"])


# Click to Login
Submit_login = driver.find_element(by=By.ID, value="submit-button")
Submit_login.click()


# Wait for schedule page to load
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))


# Find all class cards
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
booked_count = 0
waitlist_count = 0
already_booked_count = 1
what_happend=None
for card in class_cards:
    # Get the day title from the parent day group
    day_group = card.find_element(
        By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]"
    )
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if this is a Tuesday
    if "Tue" in day_title or "Thu" in day_title:
        # Check if this is a 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            # Get the class name
            class_name = card.find_element(
                By.CSS_SELECTOR, "h3[id^='class-name-']"
            ).text
            # Find and click the book button
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            if button.text == "Booked":
                print(f"✓ Already booked: {class_name} on {day_title}")
                already_booked_count += 1
            elif button.text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_name} on {day_title}")
                already_booked_count += 1
            elif button.text == "Book Class":
                button.click()
                print(f"✓ Successfully booked: {class_name} on {day_title}")
                what_happend = f"• [New Booking] {class_name} on {day_title}"
                booked_count += 1
                # Wait a moment for the button state to update
                time.sleep(0.5)
            elif button.text == "Join Waitlist":
                button.click()
                print(f"✓ Joined waitlist for: {class_name} on {day_title}")
                what_happend = f"• [Joined Waitlist] {class_name} on {day_title}"
                waitlist_count += 1
                # Wait a moment for the button state to update
                time.sleep(0.5)
            Booking_details(booked_count,waitlist_count,already_booked_count)
            what_happend_details(what_happend)
