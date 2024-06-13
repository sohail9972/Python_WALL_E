import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import *;

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demo.automationtesting.in/Datepicker.html")

# https://demo.automationtesting.in/Datepicker.html



year = "2026"
month = "June"
day=10


driver.find_element(By.XPATH,"//input[@id='datepicker1']").click()
time.sleep(10)

while(True):
    cal_year=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    cal_month=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text


    if((cal_month.lower()==month) and (cal_year.lower()==year)):
        break
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()


all_dates=driver.find_elements(By.XPATH,"//table//tbody//tr//td")
for ele in all_dates:
    dt= ele.text
    if(dt.lower(day)):
        ele.click()
        break