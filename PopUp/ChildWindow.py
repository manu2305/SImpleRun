from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/news/rss/1"
expected_url1="https://www.facebook.com/nopCommerce"
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
parent=driver.current_window_handle
sleep(2)
links=driver.find_elements(By.XPATH,"//div[@class='column follow-us']/ul/li/a")
for link in links:
    link.click()
    actual_url=driver.current_url
    if expected_url==actual_url:
        driver.back()
    sleep(1.5)
sleep(2)
childs=driver.window_handles
for child in childs:

    
    driver.switch_to.window(child)
    actual_url1=driver.current_url
    if expected_url1==actual_url1:
        sleep(2)
        driver.find_element(By.XPATH,"//span[text()='Create new account']").click()
    sleep(2)

