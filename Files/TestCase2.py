import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import *;

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.facebook.com/")

driver.implicitly_wait(10)



# tagname#attributeID
driver.find_element(By.CSS_SELECTOR , "input#email").send_keys("abc")
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")


# for the Class with CSS_selector
syntax is tagname.attributeID
driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmail.com")


# with other tag names
# syntax is tagname[attributeID = atributevalue] and tagname is optional in all cases
driver.find_element(By.CSS_SELECTOR, "imput[data-testid=royal_email]").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("abc@gmail.com")
time.sleep(10)


d1=driver.find_element(By.XPATH,"//input[@id='email']")
d1.send_keys("abc@gmail.com")
time.sleep(10)