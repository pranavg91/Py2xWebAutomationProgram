import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_map():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()
    time.sleep(50)

    svg_list = driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    for state in svg_list:
        print(state.get_attribute("aria-label"))
        if "Punjab" in state.get_attribute("aria-label"):
            state.click()
            time.sleep(20)
            break
