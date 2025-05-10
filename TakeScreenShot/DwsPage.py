from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
#driver.save_screenshot("dwsHomePage.png")
driver.get_screenshot_as_file("homePage.png")
#driver.find_element(By.CLASS_NAME,"ico-register").click()
#driver.save_screenshot("registerPage.png")
sleep(2)

driver.quit()