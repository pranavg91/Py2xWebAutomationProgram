from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webtable():
    driver = webdriver.Chrome()
    #     driver.get("https://awesomeqa.com/webtable.html")
    #     driver.implicitly_wait(30)
    #
    #     row_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")
    #     row = (len(row_elements))
    #     print(row)
    #
    #     col_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr/th")
    #     col = len(col_elements)
    #     print(col)
    #
    #     first_part = "//table[contains(@id,'cust')]/tbody/tr["
    #     second_part = "]/td["
    #     third_part = "]"
    #
    #
    #     for i in range(2, row + 1):
    #         for j in range(1, col + 1):
    #             dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
    #             data = driver.find_element(By.XPATH, dynamic_path).text
    #             if "Helen Bennett" in data:
    #                 country_path = f"{dynamic_path}/following-sibling::td"
    #                 country_text = driver.find_element(By.XPATH, country_path).text
    #                 print(f"helen is from {country_text}")
    #

    driver.get("https://awesomeqa.com/webtable1.html")
    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")
    row_element = table.find_elements(By.TAG_NAME, "tr")
    for r in row_element:
        col = r.find_elements(By.TAG_NAME,"td")
        for c in col:
            print(c.text)


# fp//div[@role='table']/div[2]/div[
# 2
# sp]/div/div[
# 2
# tp ]