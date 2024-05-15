import time
from _ast import arguments

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import *

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait


def test_alert():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()
    driver.find_element(locate_with(By.ID,"exp-3").
                        to_right_of({By.XPATH:"//span[text()='Years of Experience']"})).click()

    time.sleep(30)