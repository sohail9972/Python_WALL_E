import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import *;

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://the-internet.herokuapp.com/windows")

time.sleep(10)
driver.refresh()
driver.find_element(By.LINK_TEXT("Click Here")).click()

print(driver.current_window_handle)

chwnd = driver.window_handles[1]

driver.switch_to.window(chwnd)

print(driver.find_element(By.TAG_NAME("h3")).text)

driver.quit()
