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
dropdown=driver.find_element(By.XPATH,"//button[@class='dropbtn']")
driver.execute_script("arguments[0].scr"
                      "ollIntoView(true);",dropdown)