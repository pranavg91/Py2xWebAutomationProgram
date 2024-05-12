import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.action_chains import ActionBuilder


def test_01_actions():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    time.sleep(10)
    parent_win = driver.current_window_handle
    print(parent_win)

    link = driver.find_element(By.LINK_TEXT,'Click Here')
    link.click()
    t_win = driver.window_handles
    print(t_win)

    time.sleep(22)
    for win in t_win:
        driver.switch_to.window(win) # swtich to child
        if "New Window" in driver.page_source:
            print("pass")

        driver.switch_to.window(parent_win) # switch to parent
        time.sleep(40)