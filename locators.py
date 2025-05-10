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
driver.find_element(By.TAG_NAME, "input")
sleep(2)

driver.find_element(By.CSS_SELECTOR,"input[value='Search']").click()
sleep(2)
driver.find_element(By.CLASS_NAME,"ico-register").click()
sleep(2)
driver.find_element(By.LINK_TEXT,"Log in").click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,"Shopping").click()
sleep(2)
driver.find_element(By.NAME,"q").send_keys("laptop")
sleep(2)
driver.find_element(By.XPATH,"//input[@value='Search']").click()
