from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep
expected_url="https://demowebshop.tricentis.com/"
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/digital-downloads")
sleep(2)
products=driver.find_elements(By.XPATH,"//input[@value='Add to cart']")
for product in products:
    product.click()
    sleep(1.5)
sleep(2)
driver.find_element(By.CLASS_NAME,"header-logo").click()
sleep(3)
driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[2]").click()
sleep(6)
driver.find_element(By.CLASS_NAME,"ico-cart").click()
sleep(1.5)
li=[]
prices=driver.find_elements(By.XPATH,"//tbody/tr/td[4]/span[2]")
high=0
i=0
index=0
for price in prices:
    li.append(float(price.text))
    if high<li[i]:
        high=li[i]
        index=i+1
    i+=1
print(index)



