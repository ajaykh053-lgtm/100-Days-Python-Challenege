from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

# Setup chrome browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(url="https://ozh.github.io/cookieclicker/")
sleep(3)
# Handle initial popups (cookies consent does not have to be clicked, but language does)
print("Looking for language selection...")

try:
    # Select language
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()
    sleep(3)  # more loading
except NoSuchElementException:
    print("Language selection not found")
# Wait for everythihgns to settle
sleep(2)


Cookie_button = driver.find_element(By.ID, value="bigCookie")
item_ids = [f"product{i}" for i in range(18)]
wait = 5
timeout = time() + wait
five_min = time() + 60

# print(Cookies_element.tag_name)
# print(Cookie_count)
while True:
    Cookie_button.click()
    if time() > timeout:
        try:
            products = driver.find_elements(
                by=By.CSS_SELECTOR, value="div[id^='product']"
            )
            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):  # type: ignore
                    best_item = product
                    break
            # print(best_item.tag_name)
            # print(best_item.get_attribute('class'))
            if best_item:
                driver.execute_script("arguments[0].click();", best_item)
                print(f"Bought item : {best_item.get_attribute('id')}")
        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")
        timeout = time() + wait
        if time() > five_min:
            try:
                Cookies_element = driver.find_element(By.ID, value="cookies")
                Cookie_text = Cookies_element.text
                Cookie_count = int(Cookie_text.split()[0].replace(",", ""))
                # print(Cookies_element.tag_name)
                # print(Cookie_count)
                print(f"Final cookies count : {Cookie_count}")
                break
            except NoSuchElementException:
                print("Cookies count could not found")
                break

# https://ozh.github.io/cookieclicker/
