import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime as DT
from datetime import timedelta
import datetime
import random
import os

start_time = float(time.monotonic())

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False
chrome_options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=chrome_options)


# ожидание появления элемента в dom
def el_to_be_in_dom(CSS_SELECTOR):
    en_af = WebDriverWait(browser, 5, 0.5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR))
        )

# ожидание кликабельности элемента по селектору
def el_to_be_clicable(CSS_SELECTOR):
    en_af = WebDriverWait(browser, 10, 0.5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, CSS_SELECTOR))
        )

# ожидание отсутствия элемента в думе
def not_presence_el_loc(CSS_SELECTOR):
    WebDriverWait(browser, 10, 0.01).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, CSS_SELECTOR))
    )

# прокрутка до элемента по селектору
def scroll_by_css(selector):
    element = browser.find_element(By.CSS_SELECTOR, selector)
    browser.execute_script("arguments[0].scrollIntoView(true);", element)

# генератор случайного значения
now = datetime.datetime.now().isoformat()[20:]

# Генерация даты рождения
def d_of_birth():
    def get_random_date(start, end):
        delta = end - start
        return start + timedelta(random.randint(0, delta.days))

    start_dt = DT.strptime('01.01.1980', '%d.%m.%Y')
    end_dt = DT.strptime('01.01.2008', '%d.%m.%Y')

    rand_date = str(get_random_date(start_dt, end_dt))[:10].split('-')
    d_of_birth = rand_date[2] + '.' + rand_date[1] + '.' + rand_date[0]
    return d_of_birth
birthday = d_of_birth()

# Генерация логина
login = 'Login' + now
print(login)

# Списки случайных имён
m_firstname = {'Александр': 'Aleksandr',
    'Лев': 'Lev',
    'Николай': 'Nikolai',
    'Фёдор': 'Fedor',
    'Иван': 'Ivan',
    'Антон': 'Anton'
    }
m_surname = {'Сергеевич': 'Sergeevich',
             'Николаевич': 'Nikolaevich',
             'Васильевич': 'Vasilievich',
             'Михайлович': 'Mikhailovich',
             'Сергеевич': 'Sergeevich',
             'Павлович': 'Pavlovich',
             '': ''}
m_lastname = {'Пушкин': 'Pushkin',
              'Толстой': 'Tolstoi',
              'Гоголь': 'Gogol',
              'Достоевский': 'Dostoevskii',
              'Тургеньев': 'Turgeniev',
              'Чехов': 'Chekhov'}

w_firstname = {'Анна': 'Anna',
               'Зинаида': 'Zinaida',
               'Надежда': 'Nadezhda',
               'Елена': 'Elena',
               'Ксения': 'Ksenia',
               'Кира': 'Kira'}
w_surname = {'Андреевна': 'Andreevna',
             'Александровна': 'Aleksandrovna',
             'Андреевна': 'Andreevna',
             'Генриховна': 'Genrikhovna',
             'Сергеевна': 'Sergeevna',
             'Андреевна': 'Andreevna',
             '':''}
w_lastname = {'Ахматова': 'Akhmatova',
              'Волконская': 'Volkonskaia',
              'Дурова': 'Durova',
              'Гуро': 'Guro',
              'Карелина': 'Karelina',
              'Князева': 'Kniazeva'}

# Выбор пола м - 0, ж - 1
gender_num = random.randint(0, 1)
gender = 0
if gender_num == 0:
    gender = 'm'
else: gender = 'w'


if gender_num == 0:
    firstname = random.choice(list(m_firstname.keys()))
    surname = random.choice(list(m_surname.keys()))
    lastname = random.choice(list(m_lastname.keys()))

    en_firstname = m_firstname[firstname]
    en_surname = m_surname[surname]
    en_lastname = m_lastname[lastname]
else:
    firstname = random.choice(list(w_firstname.keys()))
    surname = random.choice(list(w_surname.keys()))
    lastname = random.choice(list(w_lastname.keys()))

    en_firstname = w_firstname[firstname]
    en_surname = w_surname[surname]
    en_lastname = w_lastname[lastname]

try:
    link = 'https://rso.sprint.1t.ru/'
    browser.get(link)

    # Клик по кнопке "Зарегистрироваться"
    browser.find_element(By.CSS_SELECTOR, '.v-card-text:nth-child(1).text-center>a').click()

# Регистрация
    def registration():
        # Выбор региона из выпадающего списка
        el_to_be_clicable('.v-field__field>.v-field__input')
        browser.find_element(By.CSS_SELECTOR, '.v-field__field>.v-field__input').click()

        selector = '.form__select-item:nth-child({})>.v-list-item__content>.v-list-item-title'.format(str(random.randint(1, 6)))
        el_to_be_clicable(selector)
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
        el_to_be_clicable('.v-overlay__content>div>.v-card-text')
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

# заполнение персональных данных
    def user_data():
        scroll_by_css(".contributorBtn:nth-child(2)")
        # переход на страницу персональных данных
        browser.find_element(By.CSS_SELECTOR, ".contributorBtn:nth-child(2)").click()

    user_data()

    # заполнение основной информации
    def main_data():
        scroll_by_css('.v-expansion-panel:nth-child(1) .v-expansion-panel-title__icon')
        browser.find_element(By.CSS_SELECTOR, '.v-expansion-panel:nth-child(1) .v-expansion-panel-title__icon').click()

        time.sleep(3)

        if gender == 'm':
            el_to_be_clicable('.checkbox>[for="m1"]')
            browser.find_element(By.CSS_SELECTOR, '.checkbox>[for="m1"]').click()

        el_to_be_clicable('.form-field:nth-child(2)>.form-input>input')
        browser.find_element(
            By.CSS_SELECTOR, '.form-field:nth-child(2)>.form-input>input'
            ).send_keys(en_lastname)
        
        el_to_be_clicable('.form-field:nth-child(4)>.form-input>input')
        browser.find_element(
            By.CSS_SELECTOR, '.form-field:nth-child(4)>.form-input>input'
            ).send_keys(en_firstname)
        
        el_to_be_clicable('.form-field:nth-child(6)>.form-input>input')
        browser.find_element(
            By.CSS_SELECTOR, '.form-field:nth-child(6)>.form-input>input'
            ).send_keys(en_surname)
        
        el_to_be_clicable('.form-field:nth-child(8)>div>input')
        browser.find_element(
            By.CSS_SELECTOR, '.form-field:nth-child(8)>div>input'
            ).send_keys(birthday)

        browser.find_element(By.CSS_SELECTOR, '.nav-btn__wrapper').click()
    
    main_data()

    # заполнение информации о адресе
    def addres_data():
        scroll_by_css('.none>.form-field:nth-child(4)')

        # регион из выпадающего списка
        el_to_be_clicable('.none>.form-field:nth-child(4) .v-field__input')
        browser.find_element(
            By.CSS_SELECTOR, '.none>.form-field:nth-child(4) .v-field__input'
            ).click()
        
        selector = '.form__select-item:nth-child({})>.v-list-item__content>.v-list-item-title'.format(str(random.randint(1, 6)))
        el_to_be_clicable(selector)
        browser.find_element(By.CSS_SELECTOR, selector).click()

        # Выбор населенного пункта
        region = browser.find_element(By.CSS_SELECTOR, '.v-select__selection>span')
        cityes = {'Амурская область': 'Благовещенск',
                  'Еврейская автономная область': 'Биробиджан',
                  'Забайкальский край': 'Чита',
                  'Камчатский край': 'Петропавловск-Камчатский',
                  'Магаданская область': 'Магадан',
                  'Приморский край': 'Владивосток'}
        city = cityes[region.text]

        el_to_be_clicable('#locality-contact')
        browser.find_element(
            By.CSS_SELECTOR, '#locality-contact'
            ).send_keys(city)
        
        # Адрес
        el_to_be_clicable('#addres-contact')
        browser.find_element(
            By.CSS_SELECTOR, '#addres-contact'
            ).send_keys('ул. Ленина, д. 42, кв. 56')
        
        # Чек-бокс
        el_to_be_clicable('.checkbox>[for="Да"]')
        browser.find_element(By.CSS_SELECTOR, '.checkbox>[for="Да"]').click()

        time.sleep(3)

        scroll_by_css('.none>.form-field:nth-child(4)')
        browser.find_element(By.CSS_SELECTOR, '.nav-btn__wrapper>[label="Далее"]').click()

        return city

    city = addres_data()

    def docs_data():
        scroll_by_css('[for="Да"]')

        # чек-бокс
        el_to_be_clicable('.one>.checkbox:nth-child(2)')
        browser.find_element(By.CSS_SELECTOR, '.one>.checkbox:nth-child(2)').click()

        # номер и серия
        el_to_be_clicable('[id="pass-num "]')
        browser.find_element(
            By.CSS_SELECTOR, '[id="pass-num "]'
            ).send_keys(str(random.randint(1000000000, 9999999999)))
        
        # Дата выдачи
        x = int(birthday.split('.')[2]) + 14
        pass_date = x[:6] + str(x)

        el_to_be_clicable('#pass_date')
        browser.find_element(
            By.CSS_SELECTOR, '#pass_date'
            ).send_keys(pass_date)
        
        # Кем выдан
        el_to_be_clicable('#pass-id')
        browser.find_element(
            By.CSS_SELECTOR, '#pass-id'
            ).send_keys('Центральным отделением ОУФМС города {}'.format(city))
        
    docs_data()







# напишите коротко о себе
    def about_me():
        scroll_by_css('.textareaUser')

        ab_me = browser.find_element(By.CSS_SELECTOR, '.textareaUser').click()

        time.sleep(3)

        ab_me.send_keys('Что это? я падаю! у меня ноги подкашиваются» , — подумал он и упал на спину. Он раскрыл глаза, надеясь увидать, чем кончилась борьба французов с артиллеристами, и желая знать, убит или нет рыжий артиллерист, взяты или спасены пушки. Но он ничего не видал. Над ним не было ничего уже, кроме неба, — высокого неба, не ясного, но все-таки неизмеримо высокого, с тихо ползущими по нем серыми облаками.')

        time.sleep(3)

        # Клик по кнопке сохранить
        browser.find_element(By.CSS_SELECTOR, '.btn_primary').click()

        browser.get('https://rso.sprint.1t.ru/PersonalData')

finally:
    time.sleep(5)
    browser.quit()


end_time = float(time.monotonic())
print('\n' + str((end_time - start_time) / 60))

'''
1. Сделать рандомный выбор региона
4. Посмотреть -- что там еще можно редактировать
5. Написать коротко о себе
6. Заполнить персональные данные
7. Сделать цикл на 20 повторений
8. Поставить секундомер
'''