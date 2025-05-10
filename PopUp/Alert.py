from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep
from selenium.webdriver.support.select import Select
expected_url="https://demowebshop.tricentis.com/"
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
driver.find_element(By.CSS_SELECTOR,".button-1.search-box-button").click()
sleep(2)
driver.find_element(By.CLASS_NAME,"ico-register").click()
# alt=driver.switch_to.alert
# sleep(2)
# print(alt.text)
# alt.accept()