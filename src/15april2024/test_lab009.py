import time

from selenium import webdriver

def test_login_vso():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    time.sleep(5)
    print("session id " + driver.session_id)

