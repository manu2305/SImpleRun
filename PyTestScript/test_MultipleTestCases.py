import pytest
from selenium import webdriver

def test_dws():
    driver=webdriver.Chrome()
    driver.maximize_window()

    driver.implicitly_wait(15)
    driver.get("https://demowebshop.tricentis.com/")
    print("iam demowebshop")
    driver.close()
def test_rcb():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://royalchallengers.com/")
    print("yi sala cup namde")
    driver.close()
def test_csk():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.chennaisuperkings.com/")
    print("thala for a reason")
    driver.close()
def test_mi():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.mumbaiindians.com/")
    print("hit man of india")
    driver.close()