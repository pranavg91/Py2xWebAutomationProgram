import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import *

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    button = driver.find_element(By.XPATH,"//button[@onclick='addElement()']")

    js_ex = driver.execute_script
    js_ex("arguments[0].click()",button)
    js_ex("arguments[     0].click()",button)
    time.sleep(20)
