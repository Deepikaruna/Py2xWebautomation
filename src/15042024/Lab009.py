from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.smoke
def test_open_vwologin():
        driver = webdriver.Chrome()
        driver.get("https://app.vwo.com")
        email_element = driver.find_element(By.NAME,"username")
        email_element.send_keys("admin")
        pass_element = driver.find_element(By.ID,"login-password")
        pass_element.send_keys("admin")
        button_submit = driver.find_element(By.ID,"js-login-btn")
        button_submit.click()
        time.sleep(5)
        error_message = driver.find_element(By.ID,"js-notification-box-msg")
        assert error_message.text == "Your email, password, IP address or location did not match"
        driver.quit()
