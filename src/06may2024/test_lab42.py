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
        driver.find_element(By.NAME,"qq").send_keys("the testing acaademy")
    except NoSuchElementException as e:
        print(f"No such element exception as: {e}")

    time.sleep(9)