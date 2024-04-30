from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


def test_assgiment_third():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")

    driver.switch_to.frame(0)

    driver.find_element(By.ID, "email").send_keys("abc@gmail.com")
    driver.find_element(By.ID, "password").send_keys("abc23")
    driver.find_element(By.ID, "password2").send_keys("abc23")
    driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    username = driver.find_element(By.XPATH, "//*[text()='Username must be at least 3 characters']")

    assert username.text == "Username must be at least 3 characters"
