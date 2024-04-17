
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_login_vso():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    element =driver.find_element(By.ID,"btn-make-appointment")
    element.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(25)

