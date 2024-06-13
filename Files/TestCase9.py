import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import *;

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bstackdemo.com/")

print(driver.title)


driver.find_element(By.ID,"signin").click()
driver.implicitly_wait(10)

userName= driver.find_element(By.ID,"username")
password= driver.find_element(By.ID,"password")
login_btn = driver.find_element(By.ID,"login-btn")

userName.click()
userName_input= driver.find_element(By.CSS_SELECTOR,"#react-select-2-option-0-0")
userName_input.click()

#Select testingisfun99 as Password
password.click()
password_input =driver.find_element(By.CSS_SELECTOR,"#react-select-3-option-0-0")
password_input.click()

login_btn.click()
driver.implicitly_wait(10)

logout_btn= driver.find_element(By.CSS_SELECTOR,"#logout")
assert logout_btn.is_displayed()
# assert userName.is_displayed()
# assert password.is_displayed()
# assert login_btn.is_displayed()

time.sleep(10)
driver.close()