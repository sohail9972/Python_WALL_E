import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import *;

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.makemytrip.com/")
driver.maximize_window()

driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//span[@class='commonModal__close']").click()

day = "10 June 2025"
mont = "June 2025"

while(True):
    depature_day=driver.find_element(By.XPATH,"//div[contains(@class,'flt_fsw_inputBox dates inactiveWidget')]").text
    print(depature_day)
    if(depature_day==mont):
        day_two=driver.find_elements(By.XPATH,"//div[@class='DayPicker-Day']")
        for i in day_two:
            if i.get_attribute("aria-label")=="Tue Jun 10 2025":
                i.click()
                print("Clicked")
                time.sleep(10)
                break
        break

    else:
        driver.find_element(By.XPATH,"//span[@aria-label='Next Month']").click()
        time.sleep(10)


