from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.saucedemo.com/v1/")


# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()


# click on product
driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
time.sleep(2)

# click on add to cart
driver.find_element(By.XPATH, "//button[normalize-space()='ADD TO CART']").click()
time.sleep(2)

# click on back
driver.find_element(By.CLASS_NAME, "inventory_details_back_button").click()
driver.refresh()
time.sleep(2)

# Click on cart
driver.find_element(By.XPATH, "//*[name()='path' and contains(@fill,'currentCol')]").click()
time.sleep(2)

# click on remove and Back to home
driver.find_element(By.XPATH, "//button[normalize-space()='REMOVE']").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.refresh()
time.sleep(5)


driver.quit()
print("Successfully Completed")