import time
from _ast import arguments

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import *

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


def test_alert():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    driver.maximize_window()
    time.sleep(30)
    try:
        text_area=driver.find_element(By.NAME,"q")
        driver.refresh()
        text_area = driver.find_element(By.NAME, "q")
        text_area.send_keys("the testing acaademy")

    except StaleElementReferenceException as e:
        print(f"No such element exception as: {e}")

    time.sleep(9)