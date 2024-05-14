import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import *;

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Index.html")
driver.get("https://www.oracle.com/in/")

var = driver.find_element(By.XPATH , "//button[normalize-space()='Products']")
var.click()

components = driver.find_elements(By.XPATH, "//ul[@id='cloud-infrastructure']//li")
# b=list[components]
time.sleep(10)
a=len(components)
print(a)

print(len(driver.find_elements(By.XPATH, "//ul[@id='cloud-infrastructure']//li")))
