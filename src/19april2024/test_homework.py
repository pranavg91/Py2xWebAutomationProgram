
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest
from allure_commons.types import AttachmentType

@allure.title("Testing the login page")
@allure.description("need to validate the login page of idrive")
def test_idrive():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()
    time.sleep(20)
    driver.find_element(By.ID, "username").send_keys("augtest_040823@idrive.com")
    time.sleep(20)

    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456")

    time.sleep(20)

    driver.find_element(By.ID, "frm-btn").click()

    time.sleep(20)

    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(20)
