import pytest
from selenium import webdriver
@pytest.mark.smoke
def test_dws():
    driver=webdriver.Chrome()
    driver.maximize_window()

    driver.implicitly_wait(15)
    driver.get("https://demowebshop.tricentis.com/")
    print("iam demowebshop")
    driver.close()
@pytest.mark.regression
def test_rcb():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://royalchallengers.com/")
    print("yi sala cup namde")
    driver.close()
@pytest.mark.system
def test_csk():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.chennaisuperkings.com/")
    print("thala for a reason")
    driver.close()
@pytest.mark.smoke
def test_mi():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.mumbaiindians.com/")
    print("hit man of india")
    driver.close()