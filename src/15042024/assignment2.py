from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.smoke
def test_open_wasabi_login():
    driver = webdriver.Chrome()
    driver.get("https://console.wasabibeta.com/login")
    email_element = driver.find_element(By.NAME,"AccountName")
    email_element.send_keys("krdeepika.ext+aprs18@wasabi.com")
    time.sleep(5)
    pass_element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[3]/main/form/div/div[2]/div/div/input")
    pass_element.send_keys("passwords123")
    sign_in_element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[3]/main/form/div/div[4]/button/span[1]")
    sign_in_element.click()
    time.sleep(10)
    bkt_element = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div/ul[3]/li/div[2]")
    bkt_element.click()
    time.sleep(5)
    createbkt_element = driver.find_element(By.CSS_SELECTOR,"#createBucketBtn")
    createbkt_element.click()
    time.sleep(5)

