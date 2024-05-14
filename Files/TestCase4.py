import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import *;

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://admin-demo.nopcommerce.com/")
time.sleep(10)
inputField = driver.find_element(By.XPATH, "//input[@id='Email']")
inputField.clear()
inputField.send_keys("admin@gmail.com")

print(inputField.text)
print(inputField.get_attribute('value'))
