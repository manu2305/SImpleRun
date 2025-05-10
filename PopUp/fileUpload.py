from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep
from selenium.webdriver.support.select import Select
expected_url="https://demowebshop.tricentis.com/"
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.ilovepdf.com/word_to_pdf")
sleep(2)
file=driver.find_element(By.XPATH,"//input[@type='file']")
file.send_keys("D:\Selenium\world.docx")
try:
    a=4/0
except Exception:
    print("exception")