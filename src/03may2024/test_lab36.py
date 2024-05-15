import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import *

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")
    drag = driver.find_element(By.ID,"column-a")
    drop = driver.find_element(By.ID,"column-b")

    actions =ActionChains(driver)
    # actions.drag_and_drop(drag,drop).perform()

    actions.click_and_hold(drag).move_to_element(drop).release(drop).perform()
    time.sleep(20)



    time.sleep(20)