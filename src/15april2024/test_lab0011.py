import time

from selenium import webdriver

def test_login_vso():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")

    print("session id " + driver.session_id)

    time.sleep(10)
    driver.quit()
    time.sleep(10)


