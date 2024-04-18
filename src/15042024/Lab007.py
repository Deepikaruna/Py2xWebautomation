from selenium import webdriver
import time
import pytest

@pytest.mark.smoke
def test_open_vwologin():
        driver = webdriver.Chrome()
        driver.get("https://console.wasabibeta.com")
        # driver.navigate()
        # navigate commands are not present in python
        driver.back()
        driver.get("https://console.wasabibeta.com")
        print(driver.title)

        driver.forward()
        print(driver.title)

        driver.back()
        print(driver.title)
        driver.refresh()

        time.sleep(5)
        driver.quit()