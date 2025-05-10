from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

expected_url="https://demowebshop.tricentis.com/"
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
community_poll=driver.find_elements(By.XPATH,"//input[@type='radio']")
print(community_poll)
for poll in community_poll:
    poll.click()
    sleep(2)
print(type(community_poll))