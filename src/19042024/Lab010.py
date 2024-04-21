from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.smoke
def test_vwologin_negative_tc():
        driver = webdriver.Chrome()
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        #make_appointment_btn = driver.find_element(By.LINK_TEXT,"Make Appointment")
        #make_appointment_btn.click()

        #Partial Linktext
        # works with a tag,called as partial match, Partial linked text
        #contains keyword
        # Find the first unique element
        
        make_appointment_btn = driver.find_element(By.PARTIAL_LINK_TEXT,"Appointment")
        make_appointment_btn.click()
        time.sleep(5)

        #driver.find_element(By.ID,"btn-make-appointment").click()
        #Linktext - It will always do full match or exact match with the text
        #rule1 - It will always return first one, if there is no linktext it will not be able to find the element




        #assert error_message.text == "Your email, password, IP address or location did not match"
        driver.quit()
