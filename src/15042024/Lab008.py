from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.smoke
def test_open_vwologin():
        driver = webdriver.Chrome()
        driver.get("https://katalon-demo-cura.herokuapp.com/")

        #Find the element of anchor tag button(Make appointment)
        #click on it
        # <a
        # id="btn-make-appointment"
        #  href="./profile.php#login"
        #  class="btn btn-dark btn-lg">
        # Make Appointment</a>

        # can fine element by id,classname,name, tagname,linktext and partial link text
        #css selector and xpath (Short way to find the elements in HTML)
        element = driver.find_element(By.ID,"btn-make-appointment")
        element.click()
        assert driver.current_url =="https://katalon-demo-cura.herokuapp.com/profile.php#login"
        driver.quit()
