from time import sleep
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.support.select import Select

expected_url="https://demowebshop.tricentis.com/"
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.get("file:///C:/Users/QSP1/Downloads/demo%20(1).html")
sleep(2)
# actual_url=driver.current_url
# s=driver.title
# if expected_url==actual_url:
#     print("iam in dws")
#     driver.find_element("id","small-searchterms").send_keys("manikandan")
# else:
#     print("iam not in dws")
single_select=driver.find_element(By.ID,"standard_cars")
sel=Select(single_select)
op=sel.options
print(len(op))
    
