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
import string
import secrets

fio_ru = ['Барсукова Маргарита Владимировна',
'Шепетько Юлия Николаевна',
'Соболев Владимир Романович',
'Горбунова Анастасия Александровна',
'Ватулин Андрей Евгеньевич',
'Кузнецов Виктор Михайлович',
'Аверина Оксана Сергеевна',
'Канубриков Николай Николаевич',
'Елисеев Алексей Евгеньевич',
'Сабынин Денис Викторович',
'Кульгина Александра Дмитриевна',
'Козлова Элла Дмитриевна',
'Кайданский Владимир Владимирович',
'Баранова Ольга Владимировна',
'Кайцуков Мурат Русланович',
'Лобойко Яков Владиславович',
'Аксенов Артем Дмитриевич',
'Дроздов Алексей Петрович',
'Новоселов Виктор Владимирович',
'Лянгузова Юлия Евгеньевна',
'Рыжов Александр Сергеевич',
'Подгайный Вячеслав Игоревич',
'Куприянова Анна Борисовна',
'Платонов Евгений Сергеевич',
'Рыжков Юрий Александрович',
'Орлова Елизавета Михайловна',
'Семенихина Марина Алексеевна',
'Сычева Анна Федоровна',
'Белокрылова Наталья Витальевна',
'Ковалев Павел Александрович',
'Иванова Полина Андреевна',
'Панова Александра Андреевна',
'Щетников Александр Михайлович',
'Кириенко Леонид Борисович',
'Черепанов Александр Евгеньевич',
'Гриценко Кристина Владимировна',
'Липовецкая Анастасия Юрьевна',
'Колобов Артем Анатольевич',
'Блюмин Алексей Александрович',
'Григорьев Денис Александрович',
'Сердцева Алла Альбертовна',
'Борсук Ольга Геннадьевна',
'Тонгуров Виталий Михайлович',
'Назарова Юлия Ринатовна',
'Занданова Елена Ефимовна',
'Ярижев Адам Аюпович',
'Даваев Санал Алексеевич',
'Устинова Ксения Анатольевна',
'Чемезов Анатолий Сергеевич',
'Кайданский Владимир Владимирович',
'Закизанова Лилия Рашидовна',
'Дубков Владислав Андреевич',
'Соловьев Айсен Владимирович',
'Габараев Олег Знаурович',
'Хусниев Аяз Алмазович',
'Сергеева Мария Николаевна',
'Шестакова Мария Александровна',
'Уколов Роман Александрович',
'Босиков Дмитрий Сергеевич',
'Пушняк Сергей Александрович',
'Аникин Егор Владимирович',
'Соколов Егор Семенович',
'Пушко Никита Васильевич',
'Дегтярева Татьяна Васильевна',
'Денисова Дарья Сергеевна',
'Епуре Юлиан Ильич',
'Дроботов Борис Иванович',
'Перова Анастасия Геннадьевна',
'Михайлова Мария Вадимовна',
'Овчинников Алексей Сергеевич',
'Судакова Елена Васильевна',
'Досхоева Анастасия Исаевна',
'Чирков Степан Владимирович',
'Лаврентьев Василий Константинович',
'Прядко Владимир Сергеевич',
'Ширшиков Вадим Андреевич',
'Щеголева Татьяна Николаевна',
'Болдырев Юрий Евгеньевич',
'Мовсулов Мохдан Мумадиевич',
'Трынов Дмитрий Сергеевич',              
'Пронникова Полина Михайловна',
'Голованова Алена Игоревна']
fio = ['Barsukova Margarita Vladimirovna',
'Shepetko YUliya Nikolaevna',
'Sobolev Vladimir Romanovich',
'Gorbunova Anastasiya Aleksandrovna',
'Vatulin Andrej Evgenevich',
'Kuznecov Viktor Mihajlovich',
'Averina Oksana Sergeevna',
'Kanubrikov Nikolaj Nikolaevich',
'Eliseev Aleksej Evgenevich',
'Sabynin Denis Viktorovich',
'Kulgina Aleksandra Dmitrievna',
'Kozlova Ella Dmitrievna',
'Kajdanskij Vladimir Vladimirovich',
'Baranova Olga Vladimirovna',
'Kajcukov Murat Ruslanovich',
'Lobojko YAkov Vladislavovich',
'Aksenov Artem Dmitrievich',
'Drozdov Aleksej Petrovich',
'Novoselov Viktor Vladimirovich',
'Lyanguzova YUliya Evgenevna',
'Ryzhov Aleksandr Sergeevich',
'Podgajnyj Vyacheslav Igorevich',
'Kupriyanova Anna Borisovna',
'Platonov Evgenij Sergeevich',
'Ryzhkov YUrij Aleksandrovich',
'Orlova Elizaveta Mihajlovna',
'Semenihina Marina Alekseevna',
'Sycheva Anna Fedorovna',
'Belokrylova Natalya Vitalevna',
'Kovalev Pavel Aleksandrovich',
'Ivanova Polina Andreevna',
'Panova Aleksandra Andreevna',
'SHCHetnikov Aleksandr Mihajlovich',
'Kirienko Leonid Borisovich',
'CHerepanov Aleksandr Evgenevich',
'Gricenko Kristina Vladimirovna',
'Lipoveckaya Anastasiya YUrevna',
'Kolobov Artem Anatolevich',
'Blyumin Aleksej Aleksandrovich',
'Grigorev Denis Aleksandrovich',
'Serdceva Alla Albertovna',
'Borsuk Olga Gennadevna',
'Tongurov Vitalij Mihajlovich',
'Nazarova YUliya Rinatovna',
'Zandanova Elena Efimovna',
'YArizhev Adam Ayupovich',
'Davaev Sanal Alekseevich',
'Ustinova Kseniya Anatolevna',
'CHemezov Anatolij Sergeevich',
'Kajdanskij Vladimir Vladimirovich',
'Zakizanova Liliya Rashidovna',
'Dubkov Vladislav Andreevich',
'Solovev Ajsen Vladimirovich',
'Gabaraev Oleg Znaurovich',
'Husniev Ayaz Almazovich',
'Sergeeva Mariya Nikolaevna',
'SHestakova Mariya Aleksandrovna',
'Ukolov Roman Aleksandrovich',
'Bosikov Dmitrij Sergeevich',
'Pushnyak Sergej Aleksandrovich',
'Anikin Egor Vladimirovich',
'Sokolov Egor Semenovich',
'Pushko Nikita Vasilevich',
'Degtyareva Tatyana Vasilevna',
'Denisova Darya Sergeevna',
'Epure YUlian Ilich',
'Drobotov Boris Ivanovich',
'Perova Anastasiya Gennadevna',
'Mihajlova Mariya Vadimovna',
'Ovchinnikov Aleksej Sergeevich',
'Sudakova Elena Vasilevna',
'Doskhoeva Anastasiya Isaevna',
'CHirkov Stepan Vladimirovich',
'Lavrentev Vasilij Konstantinovich',
'Pryadko Vladimir Sergeevich',
'SHirshikov Vadim Andreevich',
'SHCHegoleva Tatyana Nikolaevna',
'Boldyrev YUrij Evgenevich',
'Movsulov Mohdan Mumadievich',
'Trynov Dmitrij Sergeevich',              
'Pronnikova Polina Mihajlovna',
'Golovanova Alena Igorevna'
]
start_time = float(time.monotonic())

chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False
chrome_options.add_argument('--start-maximized')
browser = webdriver.Chrome(options=chrome_options)

# Генератор пароля
def password():
    alphabet = string.ascii_letters + string.digits + '+-/*!&$#?=@<>'
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(12))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    return password

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

num = 0


try:
    for i in fio:
        # Генерация пароля
        psw = password()

        # Генерация логина
        login = i.split(' ')[0] + i.split(' ')[1].lower()[:1]

        # Получаю имена
        firstname = fio_ru[num].split(' ')[1]
        lastname = fio_ru[num].split(' ')[0]
        surname = fio_ru[num].split(' ')[2]

        num += 1

        print(lastname, firstname, surname, login, psw)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = False
        chrome_options.add_argument('--start-maximized')
        browser = webdriver.Chrome(options=chrome_options)
        link = 'https://rso.sprint.1t.ru/'
        browser.get(link)

        # Клик по кнопке "Зарегистрироваться"
        browser.find_element(By.CSS_SELECTOR, '.v-card-text:nth-child(1).text-center>a').click()

    # Регистрация
        def registration():
            # Поле Фамилия
            el_to_be_clicable("[placeholder='Фамилия']")
            scroll_by_css("[placeholder='Фамилия']")

            el_to_be_clicable("[placeholder='Фамилия']")
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Фамилия']").send_keys(lastname)

            # Поле Имя
            el_to_be_clicable("[placeholder='Имя']")
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Имя']").send_keys(firstname)

            # Поле Отчество
            el_to_be_clicable("[placeholder='Отчество(При наличии)']")
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Отчество(При наличии)']").send_keys(surname)

            # Поле ДР
            el_to_be_clicable("[name='date']")
            browser.find_element(By.CSS_SELECTOR, "[name='date']").send_keys('27.10.1988')

            # Поле Логин
            el_to_be_clicable("[placeholder='Придумайте логин']")
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Придумайте логин']").send_keys(login)

            # Поле Пароль
            el_to_be_clicable("[placeholder='Придумайте пароль']")
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Придумайте пароль']").send_keys(psw)

            # Поле Повторите пароль
            el_to_be_clicable("[placeholder='Повторите пароль']")
            browser.find_element(By.CSS_SELECTOR, "[placeholder='Повторите пароль']").send_keys(psw)

            # Чек-бокс Согласие на обработку данных
            el_to_be_in_dom(".regCheck>input")
            browser.find_element(By.CSS_SELECTOR, ".regCheck>input").click()

            # Клик по кнопке Зарегистрироваться
            el_to_be_in_dom(".btn_primary>span")
            browser.find_element(By.CSS_SELECTOR, ".btn_primary>span").click()
        registration()
        browser.quit()


finally:
    time.sleep(3)
    browser.quit()

'''
1. Сделать рандомный выбор региона
4. Посмотреть -- что там еще можно редактировать
5. Написать коротко о себе
6. Заполнить персональные данные
7. Сделать цикл на 20 повторений
8. Поставить секундомер
'''