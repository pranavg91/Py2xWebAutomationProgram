import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    button = driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
    button.click()

    wait = WebDriverWait(driver=driver,timeout=10)
    wait.until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.send_keys("pranav")
    alert.accept()

    expected_result = driver.find_element(By.ID, "result")
    print(expected_result.text)
    assert "pranav" in expected_result.text


    time.sleep(20)