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

# Click on menubar  and Close like X
driver.find_element(By.XPATH, "//button[normalize-space()='Open Menu']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Close Menu']").click()
time.sleep(2)

# Click on menubar  and All Items
driver.find_element(By.XPATH, "//button[normalize-space()='Open Menu']").click()
time.sleep(2)
driver.find_element(By.ID, "inventory_sidebar_link").click()
time.sleep(2)

# Click on menubar  and About
driver.find_element(By.XPATH, "//button[normalize-space()='Open Menu']").click()
time.sleep(2)
driver.find_element(By.ID, "about_sidebar_link").click()
driver.back()
time.sleep(2)

# Logout
driver.find_element(By.XPATH, "//button[normalize-space()='Open Menu']").click()
time.sleep(2)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(2)

driver.quit()

