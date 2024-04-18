from selenium import webdriver
import time
import pytest

@pytest.mark.smoke
def test_wasabi_login():
        driver = webdriver.Chrome()
        driver.get("https://console.wasabibeta.com")
        print(driver.title)
        print(driver.session_id)
        driver.maximize_window()
        time.sleep(10)
        driver.quit()
        # it will close all the windows or tabs
        #session-id == null(invalid)
        #it will close all the other tabs
        time.sleep(10)
