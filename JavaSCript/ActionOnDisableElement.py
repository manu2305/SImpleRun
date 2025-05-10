from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.oracle.com/in/java/technologies/downloads/")
sleep(2)
jdk=driver.find_element(By.LINK_TEXT,"jdk-17.0.14_linux-x64_bin.deb")
driver.execute_script("arguments[0].scrollIntoView(false);",jdk)
jdk.click()
disable_button=driver.find_element(By.LINK_TEXT,"Download jdk-17.0.14_linux-x64_bin.deb")
driver.execute_script("arguments[0].click();",disable_button)