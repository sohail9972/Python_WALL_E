import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import *;

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://www.oracle.com/in/")


time.sleep(10)
var = driver.find_element(By.XPATH , "//button[normalize-space()='Products']").click()


components = driver.find_elements(By.XPATH, "//ul[@id='cloud-infrastructure']//li")
time.sleep(10)
a=len(components)
print(a)
for ele in components:
    print(ele.text)

print(len(driver.find_elements(By.XPATH, "//ul[@id='cloud-infrastructure']//li")))