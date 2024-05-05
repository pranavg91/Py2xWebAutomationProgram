import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_action03():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    # click = driver.find_element(By.ID, "clickable")
    # actions = ActionChains(driver)
    # actions.double_click(click).perform()
    # time.sleep(100)
    # d_Click = driver.find_element(By.ID, "click-status")
    # assert d_Click.text == "double-clicked"

    #mouse hover
    hover = driver.find_element(By.ID, "hover")
    actions = ActionChains(driver)
    actions.move_to_element(hover).perform()
    time.sleep(20)

    # drag and drop

    drag = driver.find_element(By.ID,"draggable")
    drop = driver.find_element(By.ID,"droppable")
    actions.drag_and_drop(drag,drop).perform()
    time.sleep(30)
