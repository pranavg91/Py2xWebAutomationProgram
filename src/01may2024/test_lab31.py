import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.action_chains import ActionBuilder


def test_01_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    linkclick=driver.find_element(By.ID,"click")
    linkclick.click()
    time.sleep(32)

    #action builder class
    action_builder =ActionBuilder(driver)
    action_builder.pointer_action.pointer_up(MouseButton.BACK)
    action_builder.perform()
    time.sleep(20 )
