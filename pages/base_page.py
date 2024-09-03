from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

# базовая страница (с вспомогательными методами для работы с драйвером), от которой наследуются остальные классы
class BasePage():
    # добавляем конструктор — метод, который вызывается, когда создаем объект. Он объявляется ключевым словом __init__
    # (параметры: экземпляр драйвера и url адрес). Внутри конструктора сохраняем эти данные как аттрибуты класса
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # добавим метод open. Он должен открывать нужную страницу в браузере, используя метод get(). open() может обращаться
    # к атрибутам класса: self.browser и self.url
    def open(self):
        self.browser.get(self.url)

