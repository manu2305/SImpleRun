from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep
from datetime import datetime

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

expected_url="https://demowebshop.tricentis.com/"
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
#driver.implicitly_wait(15)
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
date=datetime.now()
s=str(date).replace(":","-")
driver.save_screenshot("C://ScreenShot//dws"+s+".png")



