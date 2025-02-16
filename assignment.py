import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

os.environ['PATH'] += r":/Users/pynester/PycharmProjects/selenium101/driver/SeleniumDrivers"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)


def add_last_item_to_cart_taoofherbs():
    driver.get("https://www.taoofherbs.com/search.asp")
    try:
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "frmSearchQuery")))
        search_box.send_keys("lemon")
        search_box.send_keys(Keys.RETURN)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#productlist")))
        product_links = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#productlist tr td.producttext a")))

        print(f"Number of product links found: {len(product_links)}")

        if not product_links:
            raise Exception("No product links found in search results.")

        last_product_link = product_links[-1]
        last_product_link.click()

        quantity_input = wait.until(EC.presence_of_element_located((By.NAME, "qty_1")))
        wait.until(EC.element_to_be_clickable((By.NAME, "qty_1")))

        actions = ActionChains(driver)
        actions.move_to_element(quantity_input).click().perform()
        quantity_input.clear()
        time.sleep(0.5)
        quantity_input.send_keys("5")

        update_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Update']")))
        update_button.click()

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pass


add_last_item_to_cart_taoofherbs()
print("\nScript execution completed.")