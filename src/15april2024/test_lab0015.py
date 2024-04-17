import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_vwologin_negative_TC():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    email_element= driver.find_element(By.NAME,"username")
    email_element.send_keys("abc@gmail.com")

    password_element=driver.find_element(By.ID,"login-password")
    password_element.send_keys("123134")

    signin_element = driver.find_element(By.ID,"js-login-btn")
    signin_element.click()

    time.sleep(20)
    error_msg=driver.find_element(By.ID,"js-notification-box-msg")
    print(error_msg.text)

    assert error_msg.text == "Your email, password, IP address or location did not match"