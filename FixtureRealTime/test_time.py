# import time
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# @pytest.mark.usefixtures("setup")
#
#
# class TestCase2:
#     def test_timeSheet(self):
#         self.driver.find_element(By.XPATH, "//span[text()='Time']").click()
#         time.sleep(2)
#         self.driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("peter")
#         time.sleep(3)
#         act = ActionChains(self.driver)
#         act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
#         time.sleep(2)
#         self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
#         time.sleep(2)
#         expected_output = self.driver.find_element(By.XPATH, "//p[text()='No Timesheets Found']")
#         assert expected_output.is_displayed(), "time sheet is present"
#         print("i got my expected OutPut")





s={11,33,'fjgk',590}
print(s)