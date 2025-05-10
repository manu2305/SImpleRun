from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
#driver.implicitly_wait(15)
driver.get("https://omayo.blogspot.com/")
sleep(2)
# act=ActionChains(driver)
# act.key_down(Keys.PAGE_DOWN).perform()
# driver.execute_script("window.scrollBy(0,1000);")
driver.execute_script("window.scrollTo(0,1000);")
sleep(2)
driver.execute_script("window.scrollTo(0,-1000);")


