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

# Click on cart
driver.find_element(By.XPATH, "//*[name()='path' and contains(@fill,'currentCol')]").click()
time.sleep(2)

# Click on continue shopping
driver.find_element(By.CSS_SELECTOR, ".btn_secondary").click()
time.sleep(2)

# Click on checkout
driver.find_element(By.XPATH, "//*[name()='path' and contains(@fill,'currentCol')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='CHECKOUT']").click()

# Check if on the checkout overview page
if driver.current_url == 'https://www.saucedemo.com/v1/checkout-step-one.html':
    print("Checkout overview page reached: Passed")

    # Enter checkout information
    driver.find_element(By.ID, "first-name").send_keys("Md. Nafis")
    time.sleep(1)
    driver.find_element(By.ID, "last-name").send_keys("Ulfat")
    time.sleep(1)
    driver.find_element(By.ID, "postal-code").send_keys("1216")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@value='CONTINUE']").click()
    time.sleep(2)

    # Click on FINISH
    driver.find_element(By.XPATH, "//a[normalize-space()='FINISH']").click()
    time.sleep(2)

    # Check if on the order completion page
    if driver.current_url == 'https://www.saucedemo.com/v1/checkout-complete.html':
        print("Order completed successfully: Failed")
    else:
        print("Order completion failed: Passed")
else:
    print("Checkout overview page not reached: Failed")

driver.quit()
print("Successfully Completed")
