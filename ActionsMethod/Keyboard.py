from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
act=ActionChains(driver)
sleep(2)
# act.key_down(Keys.PAGE_DOWN).perform()
facebook=driver.find_element(By.XPATH,"//a[text()='Facebook']")