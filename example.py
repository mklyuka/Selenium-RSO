import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import datetime
import random
import os

browser = webdriver.Chrome()

# ожидание кликабельности элемента по селектору
def el_to_be_clickable(CSS_SELECTOR):
    en_af = WebDriverWait(browser, 10, 0.01).until(
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
male = random.randint(0, 1)

if male == 0:
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
        el_to_be_clickable('.v-field__field')
        browser.find_element(By.CSS_SELECTOR, '.v-field__field').click()

        el_to_be_clickable('.form__select-item:nth-child(2)>.v-list-item__content>.v-list-item-title')
        browser.find_element(
            By.CSS_SELECTOR, '.form__select-item:nth-child({})>.v-list-item__content>.v-list-item-title'.format(
                str(random.randint(1, 5))
                )
            ).click()

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
        el_to_be_clickable(".regCheck>input")
        browser.find_element(By.CSS_SELECTOR, ".regCheck>input").click()

        # Клик по кнопке Зарегистрироваться
        el_to_be_clickable(".btn_primary>span")
        browser.find_element(By.CSS_SELECTOR, ".btn_primary>span").click()
    registration()

# Авторизация
    def log_in():
    # Ожидание загрузки страницы
        el_to_be_clickable('.swal2-success-ring')
        not_presence_el_loc('.swal2-success-ring')

    # Поле Логин
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Логин']").send_keys(login)
    
    # Поле Пароль
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Пароль']").send_keys('SsjfNnfm1!2')

    # Клик по кнопке Войти
        el_to_be_clickable(".login_btn>span")
        browser.find_element(By.CSS_SELECTOR, ".login_btn>span").click()
    log_in()

    time.sleep(3)
# Редактирование профиля
    def editing_profile():
        # загрузить аватар
        browser.find_element(By.CSS_SELECTOR, '.user-metric__avatar-wrapper>.user-metric__avatar-add').click()
        el_to_be_clickable('.v-overlay__content>div>.v-card-text')
        browser.find_element(By.CSS_SELECTOR, '.v-overlay__content>div>.v-card-text').click()

        current_path = os.path.abspath(os.path.dirname(__file__)) # получил путь к дирректории
        file_path = os.path.join(current_path, 'avatar1.png') # получил путь к файлу
        browser.find_element(By.CSS_SELECTOR, '.v-field__field>input').send_keys(file_path)

        el_to_be_clickable(".v-card-actions>[type='submit']")
        browser.find_element(By.CSS_SELECTOR, ".v-card-actions>[type='submit']").click()
    
    editing_profile()





finally:
    time.sleep(5)
    browser.quit()

'''
1. Сделать рандомный выбор региона
2. Перезагрузить страницу
3. Загрузить задний фон
4. Посмотреть -- что там еще можно редактировать
'''