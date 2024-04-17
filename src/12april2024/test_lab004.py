from selenium import webdriver
import time


def test_open_vwo_page():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    print(driver.current_url)

    print(driver.title)
    assert driver.title == "Login - VWO"
