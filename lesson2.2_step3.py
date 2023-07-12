from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_value = int(browser.find_element(By.ID, "num1").text)
    y_value = int(browser.find_element(By.ID, "num2").text)

    answer = str(x_value+y_value)

    browser.find_element(By.CLASS_NAME, "custom-select").click()
    browser.find_element(By.CSS_SELECTOR, f"[value='{answer}']").click()

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
