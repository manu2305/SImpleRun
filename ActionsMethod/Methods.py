from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.myntra.com/")
act=ActionChains(driver)
men=driver.find_element(By.XPATH,"//a[text()='Men']")
#act.click(men).perform()
#act.move_to_element(men).perform()
