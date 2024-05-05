import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_action2():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.find_element(By.ID, "click")
    #actions = ActionChains(driver)
    # actions.click_and_hold(clickable).key_down(Keys.SHIFT).key_down("pranav").perform()
    #
    # actions.click(clickable).perform()
    # #actions.click_and_hold(clickable).perform()
    time.sleep(20)
    #
    # print(driver.current_url)
    # assert driver.current_url == "https://awesomeqa.com/selenium/resultPage.html"
    action_builder = ActionBuilder(driver)
    action_builder.pointer_action.pointer_down(MouseButton.BACK)
    action_builder.pointer_action.pointer_down(MouseButton.BACK)
    action_builder.perform()