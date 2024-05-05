import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_windows_handle():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/windows")

    parent_window = driver.current_window_handle
    print(parent_window)
    print(driver.page_source)

    link = driver.find_element(By.PARTIAL_LINK_TEXT, "Click Here")
    link.click()

    window_handle = driver.window_handles
    print(window_handle)

    for handles in window_handle:
        driver.switch_to.window(handles)
        if "New Window" in driver.page_source:
            print("found")
            break

    driver.switch_to.window(parent_window)
    # assert driver.current_url == "https://the-internet.herokuapp.com/windows"
    time.sleep(10)
