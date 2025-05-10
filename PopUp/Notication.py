from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep
from selenium.webdriver.support.select import Select
expected_url="https://demowebshop.tricentis.com/"
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
# options.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=options)
driver.maximize_window()
# driver.get("https://admin:admin@basic-auth-git-main-shashis-projects-4fa03ca5.vercel.app/")
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
driver.find_element(By.CSS_SELECTOR,".button-1.search-box-button").click()
alt=driver.switch_to.alert
sleep(2)
alt.accept()
driver.switch_to.frame()
