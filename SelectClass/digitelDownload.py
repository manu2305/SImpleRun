from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep
from selenium.webdriver.support.select import Select
expected_url="https://demowebshop.tricentis.com/"
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/digital-downloads")
sleep(2)
sort_by=driver.find_element(By.ID,"products-orderby")
sel=Select(sort_by)
sections=sel.options
i=0
for section in sections:
    sort_by = driver.find_element(By.ID, "products-orderby")
    sel = Select(sort_by)
    sel.select_by_index(i)
    sleep(1)
    i+=1