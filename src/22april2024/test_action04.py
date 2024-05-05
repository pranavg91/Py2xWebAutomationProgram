import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_action04():
    driver = webdriver.Chrome()
    driver.get("https://makemytrip.com")
    driver.maximize_window()
    time.sleep(10)
    driver.find_element(By.XPATH, "//span[@class='commonModal__close']").click()

    time.sleep(10)
    from_city = driver.find_element(By.ID, "fromCity")
    actions = ActionChains(driver)
    actions.move_to_element(from_city).click().send_keys("New delhi").perform()

    time.sleep(10)
