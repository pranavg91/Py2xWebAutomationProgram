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
    driver.get("https://www.aqi.in/real-time-most-polluted-city-ranking")

    driver.maximize_window()
    time.sleep(30)

    search = driver.find_element(By.ID,"search_city")
    search.send_keys("India")
    time.sleep(30)

    list_of_state = driver.find_elements(By.XPATH,"//table[@id='example']/tbody/tr/td[2]")
    print("Name" + "|" + "AQI" + "|" + "rank")

    for state in list_of_state:
        if "India" in state.text:
            s1 = driver.find_element(locate_with(By.TAG_NAME,"p").to_right_of(state)).text
            s2 = driver.find_element(locate_with(By.TAG_NAME,"p").to_left_of(state)).text
            s3 = driver.find_element(locate_with(By.TAG_NAME,"p").below(state)).text
            print(state.text + " |" + s1 + "|" + s2)
            print(state.text + " |" + s3 )