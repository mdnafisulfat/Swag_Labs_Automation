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

# click on dropdown menu

driver.find_element(By.XPATH, "//select[@class='product_sort_container']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//option[@value='za']").click()
time.sleep(4)


driver.find_element(By.XPATH, "//select[@class='product_sort_container']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//option[@value='lohi']").click()
time.sleep(4)


driver.find_element(By.XPATH, "//select[@class='product_sort_container']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//option[@value='hilo']").click()
time.sleep(4)

driver.find_element(By.XPATH, "//select[@class='product_sort_container']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//option[@value='az']").click()
time.sleep(4)


driver.quit()