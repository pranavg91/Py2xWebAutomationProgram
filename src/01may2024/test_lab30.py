import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import *


def test_01_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name=driver.find_element(By.NAME,"firstname")
    actions=ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name,"prea").key_up(Keys.SHIFT).context_click().context_click().perform()
    time.sleep(20)