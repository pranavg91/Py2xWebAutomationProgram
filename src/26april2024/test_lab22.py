import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import pytest
import os


# data driven test cases for the login page

def read_credentials_from_excel(file_path):
    credentials = []  # create empty list
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({
            "username": username,
            "password": password
        })
    return credentials


file_path_fromos = os.getcwd() + "/py2xtestdata.xlsx"
print(file_path_fromos)


@pytest.mark.parametrize("user_cred", read_credentials_from_excel(file_path_fromos))
def test_vwo_login(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    vwo_login(username=username, password=password)


def vwo_login(username, password):
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # Login scenario - run on login multiple times with excel file data

    email = driver.find_element(By.CSS_SELECTOR, "#login-username")
    password_value = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    submit = driver.find_element(By.XPATH, "//button[@id='js-login-btn']")

    email.send_keys(username)
    password_value.send_keys(password)

    submit.click()
    # explict wait
    time.sleep(20)

    result = driver.current_url

    if result != "https://app.vwo.com/#/dashboard":
        print("invalid")
    else:
        print("pass")


    driver.quit()