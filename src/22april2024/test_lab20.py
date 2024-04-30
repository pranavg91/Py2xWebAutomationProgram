import test
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure

def test_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    # find element using text
    make_btn = driver.find_element(By.XPATH,"//a[text()='Make Appointment']")

    # partial text     
    driver.find_element(By.XPATH,"//a[contains(text(),'Make')]")
