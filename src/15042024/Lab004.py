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

        driver.close()
        time.sleep(10)
