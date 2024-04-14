from selenium import webdriver
import time


def test_open_vwo():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    time.sleep(5)
    print(driver.title)
    assert driver.title == "Login - VWO"
