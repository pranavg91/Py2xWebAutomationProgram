import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_flipkart():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")

    driver.find_element(By.NAME,"q").send_keys("AC")
    time.sleep(10)

    # driver.find_element(By.XPATH,"//button[@type='submit']").click()
    svg_list = driver.find_elements(By.XPATH,"//*[name() ='svg']")
    svg_list[0].click()
