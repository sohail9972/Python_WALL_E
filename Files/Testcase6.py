import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import *;

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.facebook.com/")

time.sleep(10)
name_field=driver.find_element(By.ID,"email")
# name_field.get_attribute(By.ID("email"))
name_field.send_keys("abc@gmail.com")
pass_field=driver.find_element(By.ID,"pass")
pass_field.send_keys("123456789")
button=driver.find_element(By.XPATH,"//div//button[@name='login']")
button.click()
