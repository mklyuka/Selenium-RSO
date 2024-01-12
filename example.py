import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import datetime

browser = webdriver.Chrome()

# генератор случайного значения
now = datetime.datetime.now().isoformat()[20:]

# Генерация логина
login = 'Login' + now

# Списки случайных имён

try:
    link = 'https://rso.sprint.1t.ru/'
    browser.get(link)

    # Клик по кнопке "Зарегистрироваться"
    browser.find_element(By.CSS_SELECTOR, '.v-card-text:nth-child(1).text-center>a').click()

# Регистрация
    def registration():
        # Выбор региона из выпадающего списка
        en_af = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.v-field__field'))
        )
        browser.find_element(By.CSS_SELECTOR, '.v-field__field').click()

        en_af = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.form__select-item:nth-child(2)>.v-list-item__content>.v-list-item-title'))
        )

        browser.find_element(By.CSS_SELECTOR, '.form__select-item:nth-child(2)>.v-list-item__content>.v-list-item-title').click()

        # Поле Фамилия
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Фамилия']").send_keys('Чуковский')

        # Поле Имя
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Имя']").send_keys('Корней')

        # Поле Отчество
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Отчество(При наличии)']").send_keys('Иванович')
        
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
        browser.find_element(By.ID, "checkbox-3").click()

        # Клик по кнопке Зарегистрироваться
        browser.find_element(By.CSS_SELECTOR, ".btn_primary>span").click()
    registration()

# Авторизация
    def log_in():

    # Ожидание загрузки страницы
        en_af = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[placeholder='Логин']"))
        )
    
    # Поле Логин
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Логин']").send_keys(login)
    
    # Поле Пароль
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Пароль']").send_keys('SsjfNnfm1!2')

    # Ожидание кнопки Войти
        en_af = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.btn_primary>span'))
        )

    # Клик по кнопке Войти
        browser.find_element(By.CSS_SELECTOR, ".btn_primary>span").click()
    log_in()



finally:
    time.sleep(5)
    browser.quit()