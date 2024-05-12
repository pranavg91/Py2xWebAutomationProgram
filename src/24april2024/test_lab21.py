from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_vwo():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    email = driver.find_element(By.CSS_SELECTOR, "#login-username")
    password = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    submit = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")

    email.send_keys("abc@gmail.com")
    password.send_keys("abc@gmail")
    submit.click()
    # explict wait
    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))
    )

    error_msg = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg.text)

    assert error_msg.text == "Your email, password, IP address or location did not match"
