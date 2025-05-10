from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep
from selenium.webdriver.support.select import Select
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
sleep(2)
driver.execute_script("window.scrollBy(0,500);")