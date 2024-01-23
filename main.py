import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import datetime
import random
import os

iterations = ''

start_time = float(time.monotonic())

for i in range(1):
    browser = webdriver.Chrome()

    # ожидание появления элемента в dom
    def el_to_be_in_dom(CSS_SELECTOR):
        en_af = WebDriverWait(browser, 10, 0.001).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR))
            )

    # ожидание кликабельности элемента по селектору
    def el_to_be_clicable(CSS_SELECTOR):
        en_af = WebDriverWait(browser, 15, 0.001).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, CSS_SELECTOR))
            )

    # ожидание отсутствия элемента в думе
    def not_presence_el_loc(CSS_SELECTOR):
        WebDriverWait(browser, 10, 0.01).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR))
        )

    # генератор случайного значения
    now = datetime.datetime.now().isoformat()[20:]

    # Генерация логина
    login = 'Login' + now
    print(login)

    # Списки случайных имён
    m_firstname = ['Александр', 'Лев', 'Николай', 'Фёдор', 'Иван', 'Антон']
    m_surname = ['Сергеевич', 'Николаевич', 'Васильевич', 'Михайлович', 'Сергеевич', 'Павлович', '']
    m_lastname = ['Пушкин', 'Толстой', 'Гоголь', 'Достоевский', 'Тургеньев', 'Чехов']

    w_firstname = ['Анна', 'Зинаида', 'Надежда', 'Елена', 'Ксения', 'Кира']
    w_surname = ['Андреевна', 'Александровна', 'Андреевна', 'Генриховна', 'Сергеевна', 'Андреевна', '']
    w_lastname = ['Ахматова', 'Волконская', 'Дурова', 'Гуро', 'Карелина', 'Князева']

    # Выбор пола м - 0, ж - 1
    gender_num = random.randint(0, 1)
    gender = 0
    if gender_num == 0:
        gender = 'm'
    else: gender = 'w'


    if gender_num == 0:
        firstname = random.choice(m_firstname)
        surname = random.choice(m_surname)
        lastname = random.choice(m_lastname)
    else:
        firstname = random.choice(w_firstname)
        surname = random.choice(w_surname)
        lastname = random.choice(w_lastname)

    try:
        link = 'https://rso.sprint.1t.ru/'
        browser.get(link)

        # Клик по кнопке "Зарегистрироваться"
        browser.find_element(By.CSS_SELECTOR, '.v-card-text:nth-child(1).text-center>a').click()

    # Регистрация
        def registration():
            # Выбор региона из выпадающего списка
            el_to_be_clicable('.v-field__field')
            browser.find_element(By.CSS_SELECTOR, '.v-field__field').click()
            not_presence_el_loc("[aria-expanded='false']")

            selector = '.form__select-item:nth-child({})>.v-list-item__content>.v-list-item-title'.format(str(random.randint(1, 6)))
            el_to_be_in_dom('.v-list-item-title')
            browser.find_element(By.CSS_SELECTOR, selector).click()

            # Поле Фамилия
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Фамилия']").send_keys(lastname)

            # Поле Имя
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Имя']").send_keys(firstname)

            # Поле Отчество
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Отчество(При наличии)']").send_keys(surname)
            
            # Поле Телефон
            browser.find_element(By.CSS_SELECTOR, "[placeholder='+7 (999) 999-99-99']").send_keys('+79991234568')

            # Поле Почта
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Электронная почта']").send_keys('example@gmail.com')

            # Поле ДР
            browser.find_element(By.CSS_SELECTOR, "[name='date']").send_keys('12.11.1988')

            # Поле Логин
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Придумайте логин']").send_keys(login)

            # Поле Пароль
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Придумайте пароль']").send_keys('SsjfNnfm1!2')

            # Поле Повторите пароль
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Повторите пароль']").send_keys('SsjfNnfm1!2')

            # Чек-бокс Согласие на обработку данных
            el_to_be_in_dom(".regCheck>input")
            browser.find_element(By.CSS_SELECTOR, ".regCheck>input").click()

            # Клик по кнопке Зарегистрироваться
            el_to_be_in_dom(".btn_primary>span")
            browser.find_element(By.CSS_SELECTOR, ".btn_primary>span").click()
        registration()

    # Авторизация
        def log_in():
        # Ожидание загрузки страницы
            el_to_be_in_dom('.swal2-success-ring')
            not_presence_el_loc('.swal2-success-ring')

        # Поле Логин
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Логин']").send_keys(login)
        
        # Поле Пароль
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Пароль']").send_keys('SsjfNnfm1!2')

        # Клик по кнопке Войти
            el_to_be_in_dom(".login_btn>span")
            browser.find_element(By.CSS_SELECTOR, ".login_btn>span").click()
        log_in()

        time.sleep(3)
    # загрузить аватар
        def upload_av():
            browser.find_element(By.CSS_SELECTOR, '.user-metric__avatar-wrapper>.user-metric__avatar-add').click()
            el_to_be_in_dom('.v-overlay__content>div>.v-card-text')
            browser.find_element(By.CSS_SELECTOR, '.v-overlay__content>div>.v-card-text').click()

            current_path = os.path.abspath(os.path.dirname(__file__)) # получил путь к дирректории
            file_path = os.path.join(current_path, '{}{}.jpg'.format(gender, random.randint(1, 4))) # получил путь к файлу
            browser.find_element(By.CSS_SELECTOR, '.v-field__field>input').send_keys(file_path)

            el_to_be_clicable(".v-card-actions>[type='submit']")
            browser.find_element(By.CSS_SELECTOR, ".v-card-actions>[type='submit']").click()
            not_presence_el_loc(".v-card-actions>[type='submit']")

            # обновить страницу
            browser.get('https://rso.sprint.1t.ru/PersonalData')

        upload_av()

    # загрузить фон
        def upload_back():
            el_to_be_in_dom('.user-metric__top>.v-btn')
            browser.find_element(By.CSS_SELECTOR, '.user-metric__top>.v-btn').click()
            el_to_be_in_dom('.v-overlay__content>div>.v-card-text')
            browser.find_element(By.CSS_SELECTOR, '.v-overlay__content>div>.v-card-text').click()

            current_path = os.path.abspath(os.path.dirname(__file__)) # получил путь к дирректории
            file_path = os.path.join(current_path, 's{}.jpg'.format(random.randint(1, 3))) # получил путь к файлу
            browser.find_element(By.CSS_SELECTOR, '.v-field__field>input').send_keys(file_path)

            el_to_be_clicable(".v-card-actions>[type='submit']")
            browser.find_element(By.CSS_SELECTOR, ".v-card-actions>[type='submit']").click()
            not_presence_el_loc(".v-card-actions>[type='submit']")
            
            # Обновить страницу
            browser.get('https://rso.sprint.1t.ru/PersonalData')    
        
        upload_back()

    # напишите коротко о себе
        def about_me():
            # прокрутка до поля ввода
            ab_me = browser.find_element(By.CSS_SELECTOR, '.textareaUser')
            browser.execute_script("arguments[0].scrollIntoView(true);", ab_me)

            # Ввод текста
            ab_me.click()

            time.sleep(3)

            ab_me.send_keys('Что это? я падаю! у меня ноги подкашиваются» , — подумал он и упал на спину. Он раскрыл глаза, надеясь увидать, чем кончилась борьба французов с артиллеристами, и желая знать, убит или нет рыжий артиллерист, взяты или спасены пушки. Но он ничего не видал. Над ним не было ничего уже, кроме неба, — высокого неба, не ясного, но все-таки неизмеримо высокого, с тихо ползущими по нем серыми облаками.')

            time.sleep(3)

            # Клик по кнопке сохранить
            browser.find_element(By.CSS_SELECTOR, '.btn_primary').click()

            browser.get('https://rso.sprint.1t.ru/PersonalData')
    
    except:
        print('exit')
        browser.quit()
        iterations += '0 '
    else:
        print('else')
        browser.quit()
        iterations += '1 '


end_time = float(time.monotonic())
print('\n' + str((end_time - start_time) / 60))
print(iterations)

'''
1. Сделать рандомный выбор региона
4. Посмотреть -- что там еще можно редактировать
5. Написать коротко о себе
6. Заполнить персональные данные
7. Сделать цикл на 20 повторений
8. Поставить секундомер
'''