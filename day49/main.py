import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException

load_dotenv()
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
wait = WebDriverWait(driver=driver, timeout=2)
driver.get(url=os.environ["GYM_URL"])


def retry(func, retries=7, description=None):
    for i in range(retries):
        try:
            return func()
        except (TimeoutError, TimeoutException):
            if i == retries - 1:
                raise
            time.sleep(1)
def login():
    login_button = driver.find_element(by=By.CLASS_NAME, value="Home_heroButton__3eeI3")
    login_button.click()

    # Using WebDriverWait operations to wait for some time to load website
    wait.until(ec.presence_of_element_located((By.ID, "login-page")))

    # Filling the from.
    Enter_email = driver.find_element(by=By.NAME, value="email")
    Enter_email.clear()
    Enter_email.send_keys(os.environ["ACCOUNT_EMAIL"])
    Enter_pass = driver.find_element(by=By.NAME, value="password")
    Enter_pass.clear()
    Enter_pass.send_keys(os.environ["ACCOUNT_PASSWORD"])

    # Click to Login
    Submit_login = driver.find_element(by=By.ID, value="submit-button")
    Submit_login.click()
    # Wait for schedule page to load
    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
def book_class(booking_button):
    booking_button.click()
    wait.until(
        lambda d: booking_button.text == "Booked" or booking_button.text == "Waitlisted"
    )

retry(login, description="login")

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
booked_count = 0
waitlist_count = 0
already_booked_count = 0
what_happend = None

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
                retry(lambda: book_class(button), description="Booking")
                print(f"✓ Successfully booked: {class_name} on {day_title}")
                what_happend = f"• [New Booking] {class_name} on {day_title}"
                booked_count += 1
                # Wait a moment for the button state to update
                time.sleep(0.5)
            elif button.text == "Join Waitlist":
                retry(lambda: book_class(button), description="Waitlistign")
                print(f"✓ Joined waitlist for: {class_name} on {day_title}")
                what_happend = f"• [Joined Waitlist] {class_name} on {day_title}"
                waitlist_count += 1
                # Wait a moment for the button state to update
                time.sleep(0.5)

total_booked = already_booked_count + booked_count + waitlist_count
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

def get_my_bookings():
    global verified_count
    My_booking = driver.find_element(by=By.ID, value="my-bookings-link")
    My_booking.click()
    wait = WebDriverWait(driver=driver, timeout=2)
    wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))
    cards = driver.find_elements(
        by=By.CSS_SELECTOR, value="div[id^='booking-card-booking_']"
    )
    if not cards:
        raise TimeoutException("No booking cards found - page may not have loaded")
    return cards

all_cards = retry(get_my_bookings, description="Get my bookings")
verified_count = 0
for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text
        if ("Tue" in when_text or "Thu" in when_text) and "6:00" in when_text:
            class_name = card.find_element(By.TAG_NAME, value="h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        pass
# Simple comparision
print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")
if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")

