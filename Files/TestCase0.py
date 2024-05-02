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
driver.get("https://demo.nopcommerce.com/")


text_area=driver.find_element(By.ID,"email")
text_area.send_keys("test@gmail.com")
driver.find_element(By.ID,"enterimg").click()


variable = driver.find_element(By.XPATH, "//input[@type='email']")
variable.click()
variable.send_keys("Apple MacBook Pro 13-inch")


var = driver.find_element(By.LINK_TEXT, "Register")
var = driver.find_element(By.PARTIAL_LINK_TEXT, "Register")
var.click()
driver.close()