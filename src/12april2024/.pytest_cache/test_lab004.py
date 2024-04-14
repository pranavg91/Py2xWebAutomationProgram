from selenium import webdriver
import time

def test_open_vwo():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
    time.sleep(5)