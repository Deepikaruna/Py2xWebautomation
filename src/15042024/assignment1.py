from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.smoke
def test_open_katalondemo():
        driver = webdriver.Chrome()
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        appoint_element = driver.find_element(By.ID,"btn-make-appointment")
        appoint_element.click()
        time.sleep(10)
        username_element = driver.find_element(By.ID,"txt-username")
        username_element.send_keys("John Doe")
        pass_element = driver.find_element(By.ID,"txt-password")
        pass_element.send_keys("ThisIsNotAPassword")
        login_element = driver.find_element(By.ID,"btn-login")
        login_element.click()
        time.sleep(5)
        error_message = driver.find_element(By.XPATH,"//div//h2")
        assert error_message.text == "Make Appointment"
        time.sleep(20)