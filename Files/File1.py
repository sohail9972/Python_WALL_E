from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import *;

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Index.html")


text_area=driver.find_element(By.ID,"email")
text_area.send_keys("test@gmail.com")
driver.find_element(By.ID,"enterimg").click()

