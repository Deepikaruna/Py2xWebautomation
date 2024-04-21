from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest

@pytest.mark.smoke
def test_appvmo_login():
        driver = webdriver.Chrome()
        driver.get("https://app.vwo.com/")
        make_apppointment_btn = driver.find_element(By.XPATH,"//input[@id='login-username']")
        make_apppointment_btn.send_keys("admin")
        time.sleep(5)

        #By using xpath
       # // a[ @ id = 'btn-make-appointment'] - unique element
       #input
       # type = "email"
       #class = "text-input W(100%)"
       # name = "username"
       # id = "login-username"
       #data-qa="hocewoqusi"

       #xpath
       # //input[@id='login-username']
       # //input[@name='username']
       # //input[@class='text-input W(100%)'] - Not recomended
       # //input[@type ='email'] - Not recomended
       # //input[@data-qa='hocewoqusi']


