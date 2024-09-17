from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.saucedemo.com/v1/")

# 1st username
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

if driver.current_url == 'https://www.saucedemo.com/v1/inventory.html':
    print("1st user: Passed")
    driver.back()
else:
    print("1st user: Fail")
    driver.refresh()

time.sleep(2)

# 2nd username
driver.find_element(By.ID, "user-name").clear()
driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

if driver.current_url == 'https://www.saucedemo.com/v1/inventory.html':
    print("2nd user: Passed")
    driver.back()
else:
    print("2nd user: Fail")
    driver.refresh()

time.sleep(2)

# 3rd username
driver.find_element(By.ID, "user-name").clear()
driver.find_element(By.ID, "user-name").send_keys("problem_user")
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

if driver.current_url == 'https://www.saucedemo.com/v1/inventory.html':
    print("3rd user: Passed")
    driver.back()
else:
    print("3rd user: Fail")
    driver.refresh()

time.sleep(2)

# 4th username
driver.find_element(By.ID, "user-name").clear()
driver.find_element(By.ID, "user-name").send_keys("performance_glitch_user")
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

if driver.current_url == 'https://www.saucedemo.com/v1/inventory.html':
    print("4th user: Passed")
    driver.back()
else:
    print("4th user: Fail")
    driver.refresh()

driver.close()
print("Successfully processed all login attempts")
