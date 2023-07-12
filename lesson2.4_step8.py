from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    # код основной задачи ---------------
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get(link)
    first_button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), "100"))
    first_button.click()

    x = browser.find_element(By.ID, "input_value").text
    result = calc(x)

    form = browser.find_element(By.ID, 'answer')
    form.send_keys(result)

    second_button = browser.find_element(By.ID, 'solve')
    second_button.click()
    # код основной задачи ---------------



    # дополнительный код: парсинг кода ответа, переход и авторизация на Stepic, ---------------
    # выбор нужного урока и шага, ввод и отправка кода ответа
    success_alert = browser.switch_to.alert
    text = success_alert.text
    spis = text.split(' ')

    stepic_link = "https://stepik.org/lesson/184253/step/4?unit=158843"
    browser = webdriver.Chrome()
    browser.get(stepic_link)

    login = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'ember54')))
    login.click()

    NM = browser.find_element(By.ID, 'id_login_email')
    NM.send_keys('Ivanov@ivan.ru')

    PS = browser.find_element(By.ID, 'id_login_password')
    PS.send_keys('123456')

    login_button = browser.find_element(By.CLASS_NAME, 'sign-form__btn')
    login_button.click()

    '''
    Пример другого варианта поиска: есть несколько элементов, содержащих нужную ссылку.
    Проводится поиск по всем, а для скролла выбирается самый первый.

    lesson2_2 = browser.find_elements(By.CSS_SELECTOR, "[href='/lesson/184253/step/1?unit=158843']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", lesson2_2[0])
    '''

    lesson2_2 = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Работа с файлами, списками и js-скриптами")))

    browser.execute_script("return arguments[0].scrollIntoView(true);", lesson2_2)

    lesson2_4 = browser.find_element(By.PARTIAL_LINK_TEXT, "Настройка ожиданий")
    lesson2_4.click()

    step8 = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[href='/lesson/181384/step/8?unit=156009']")))
    step8.click()

    answer_input = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[placeholder='Напишите ваш ответ здесь...']")))
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    answer_input.send_keys(spis[-1])

    final_submit = browser.find_element(By.CLASS_NAME, "submit-submission")
    final_submit.click()

finally:
    time.sleep(5)
    browser.quit()
