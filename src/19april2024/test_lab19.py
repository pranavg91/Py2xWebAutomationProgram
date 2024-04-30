from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest

@allure.title("verfiy the loginn")
@allure.description("TC 1")
def test_mini_project():
    driver = webdriver.Chrome()
    time.sleep(6)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment_btn = driver.find_element(By.XPATH,"//a[@class='btn btn-dark btn-lg']")
    make_appointment_btn.click()
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Error"

    time.sleep(10)
    driver.find_element(By.NAME,"username").send_keys("John Doe")

    driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")

    driver.find_element(By.ID,"btn-login").click()
    time.sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    time.sleep(10)