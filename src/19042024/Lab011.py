from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.smoke
def test_vwologin_negative_tc():
        driver = webdriver.Chrome()
        driver.get("https://katalon-demo-cura.herokuapp.com/")

        # By tag name
        list_of_tags = driver.find_elements(By.TAG_NAME,"a")
        make_appintment_btn = list_of_tags[5]
        make_appintment_btn.click()
        time.sleep(5)

        # ID - Unique ID
        #name - Unique Classname
        # Tagname - get1, list of elements via find elements
        #Link/Partial linktext - a anchor tags
        # Css selector - 20%
        #Xpath - 60%