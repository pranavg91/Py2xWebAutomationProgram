import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_katalon_make_appointment():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # click to make appointment button.

    # click_to_make_appointment_button = driver.find_element(By.LINK_TEXT,"Make Appointment")
    # click_to_make_appointment_button.click()

    #Tag name
    list_of_tagname = driver.find_elements(By.TAG_NAME,"a")
    click_to_make_appointment_button=list_of_tagname[5]
    click_to_make_appointment_button.click()
    time.sleep(4)



    #partial link text
    click_to_make_appointment_button = driver.find_element(By.PARTIAL_LINK_TEXT,"Appointment")
    click_to_make_appointment_button.click()

    time.sleep(10)


    #
    # #enter data in username field
    # time.sleep(5)
    # username_element = driver.find_element(By.NAME,"username")
    # username_element.send_keys("John Doe")
    #
    # #Enter data in password field
    # time.sleep(5)
    # password_element = driver.find_element(By.ID,"txt-password")
    # password_element.send_keys("ThisIsNotAPassword")
    #
    # #click to sign up button
    # time.sleep(5)
    # signup =driver.find_element(By.ID,"btn-login")
    # signup.click()
    #
    # make_appointment=driver.find_element(By.PARTIAL_LINK_TEXT,"Make Appointment")
    # print(make_appointment.text)
    #
    # assert make_appointment.text == "Make Appointment"
