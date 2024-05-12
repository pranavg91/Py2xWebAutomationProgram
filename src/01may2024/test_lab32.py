import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.action_chains import ActionBuilder


def test_01_actions():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com")
    driver.maximize_window()
    time.sleep(30)

    driver.find_element(By.XPATH,"//span[@class='commonModal__close']").click()

    from_city = driver.find_element(By.ID,"fromCity")

    actions = ActionChains(driver)
    actions.move_to_element(from_city).send_keys("Abc").perform()

    time.sleep(20)
