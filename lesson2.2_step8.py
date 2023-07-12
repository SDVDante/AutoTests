from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name_form = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    name_form.send_keys('Ivan')

    name_form = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    name_form.send_keys('Ivanov')

    name_form = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    name_form.send_keys('ivanov@ivan.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(current_dir, 'file_for_2.2-8.txt')

    upload = browser.find_element(By.ID, "file")
    upload.send_keys(file)

    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
