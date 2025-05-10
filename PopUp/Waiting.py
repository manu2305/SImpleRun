from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

expected_url="https://demowebshop.tricentis.com/"
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
#driver.implicitly_wait(15)
driver.get("https://www.shoppersstack.com/")
sleep(2)
wait=WebDriverWait(driver,30)
login=wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[@class='navbar_Loginbutton__O9-64']")))
#driver.find_element(By.XPATH,"//button[@class='navbar_Loginbutton__O9-64']").click()
login.click()