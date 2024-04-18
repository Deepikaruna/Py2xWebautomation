import time

from selenium import webdriver

def test_wasabi_login():
    driver = webdriver.Chrome() #post request|create the session
     # Get request to URL param
    # Session is created - unique ID - 16 digit ID
    # 64bafsnfajasfasfsa - Session?
    #webdriver.chrome - fresh copy of browser is created
    #open new tabs,open URL those will be different from normal browser - automation
    #close browser everything is deleted

    time.sleep(20)
    driver.get("https://console.wasabibeta.com")
    print(driver.title)
    #print(driver.page_source)
    print(driver.session_id)
    driver.maximize_window()
    assert driver.title == " Login -  Wasabi"
