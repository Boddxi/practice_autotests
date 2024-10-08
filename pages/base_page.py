from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
# Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать:
from selenium.common.exceptions import NoSuchElementException
# Теперь для всех проверок, что элемент действительно присутствует на странице, мы можем использовать этот метод.

from pages.locators import BasePageLocators


# базовая страница (с вспомогательными методами для работы с драйвером), от которой наследуются остальные классы
class BasePage():
    # добавляем конструктор — метод, который вызывается, когда создаем объект. Он объявляется ключевым словом __init__
    # (параметры: экземпляр драйвера и url адрес). Внутри конструктора сохраняем эти данные как аттрибуты класса

    # Чтобы выводить адекватное сообщение об ошибке, мы будем все проверки осуществлять с помощью assert и перехватывать исключения.
    # Для этого напишем вспомогательный метод поиска элемента в нашей базовой странице BasePage, который будет возвращать нам True или False.
    # Можно сделать это по-разному (с настройкой явных или неявных ожиданий). Сейчас воспользуемся неявным ожиданием.
    # В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # добавим команду для неявного ожидания со значением по умолчанию в 10
        self.timeout = timeout  # устанавливаем значение времени ожидания для атрибута объекта
        self.browser.implicitly_wait(timeout)

    # добавим метод open. Он должен открывать нужную страницу в браузере, используя метод get(). open() может обращаться
    # к атрибутам класса: self.browser и self.url
    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()


# Теперь в этом же классе реализуем метод is_element_present, в котором будем перехватывать исключение. В него будем передавать два аргумента:
# как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
# Чтобы перехватывать исключение, нужна конструкция try/except:
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

