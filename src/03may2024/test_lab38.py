import time
from _ast import arguments

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import *

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_alert():
    driver = webdriver.Chrome()
    driver.get("https://selectorshub.com/xpath-practice-page/")

    div = driver.find_element(By.XPATH, "//div[@class ='jackPart']")

    js_ex = driver.execute_script
    js_ex("arguments[0].scrollIntoView(true)",div)

    time.sleep(30)