from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    # код основной задачи ---------------
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.get(link)

    first_button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    first_button.click()

    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]

    browser.switch_to.window(second_window)

    x = browser.find_element(By.ID, "input_value").text
    result = calc(x)

    form = browser.find_element(By.ID, 'answer')
    form.send_keys(result)

    second_button = browser.find_element(By.CLASS_NAME, 'btn-primary')
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

    time.sleep(5)

    login = browser.find_element(By.ID, 'ember54')
    login.click()

    NM = browser.find_element(By.ID, 'id_login_email')
    NM.send_keys('Ivanov@ivan.ru')

    PS = browser.find_element(By.ID, 'id_login_password')
    PS.send_keys('123456')

    login_button = browser.find_element(By.CLASS_NAME, 'sign-form__btn')
    login_button.click()

    time.sleep(5)

    '''
    Пример другого варианта поиска: есть несколько элементов, содержащих нужную ссылку.
    Проводится поиск по всем, а для скролла выбирается самый первый.
    
    lesson2_2 = browser.find_elements(By.CSS_SELECTOR, "[href='/lesson/184253/step/1?unit=158843']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", lesson2_2[0])
    '''

    lesson2_2 = browser.find_element(By.PARTIAL_LINK_TEXT, "Работа с файлами, списками и js-скриптами")

    browser.execute_script("return arguments[0].scrollIntoView(true);", lesson2_2)

    lesson2_3 = browser.find_element(By.PARTIAL_LINK_TEXT, "Работа с окнами")

    lesson2_3.click()

    time.sleep(5)

    step6 = browser.find_element(By.CSS_SELECTOR, "[href='/lesson/184253/step/6?unit=158843']")
    step6.click()

    time.sleep(3)

    answer_input = browser.find_element(By.CSS_SELECTOR, "[placeholder='Напишите ваш ответ здесь...']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
    answer_input.send_keys(spis[-1])

    final_submit = browser.find_element(By.CLASS_NAME, "submit-submission")
    final_submit.click()

finally:
    time.sleep(5)
    browser.quit()
