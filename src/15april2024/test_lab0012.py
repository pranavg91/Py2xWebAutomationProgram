import time

from selenium import webdriver

def test_login_vso():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bing.com.chat")
    time.sleep(4) #pyhton inter wait for th 25 sec, not the webdriver
    driver.get("https://google.com")
    print(driver.title)
    driver.refresh()
    driver.forward()
    time.sleep(7)
    print("last title " + driver.title)
    assert driver.title == "Google"

