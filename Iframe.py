from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep
from selenium.webdriver.support.select import Select
expected_url="https://demowebshop.tricentis.com/"
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.dream11.com/")
sleep(2)
text_field=driver.find_element(By.ID,"send-sms-iframe")
driver.switch_to.frame(text_field)
driver.find_element(By.ID,"regEmail").send_keys("7358001010")
