from selenium import webdriver
import time
import pytest

@pytest.mark.smoke
def test_open_vwologin():
        driver = webdriver.Chrome()
        driver.get("https://bing.com/chat")
        time.sleep(25) #you are telling to python interpretor wait for 25 seconds, not the webdriver
        driver.get("https://google.com")
        print(driver.title)

