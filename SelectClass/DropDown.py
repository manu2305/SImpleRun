from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep

from selenium.webdriver.support.select import Select

expected_url="https://demowebshop.tricentis.com/"
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("file:///C:/Users/QSP1/Downloads/demo%20(1).html")
sleep(2)
single_Select=driver.find_element(By.ID,"standard_cars")
sel=Select(single_Select)
cars=sel.options
print(type(cars))
print(sel.is_multiple)
for car in cars:
    car.click()
sel.select_by_index(2)
sleep(2)
sel.select_by_value("hda")
sleep(2)
sel.select_by_visible_text("Ford")
value=sel.all_selected_options
print(value)