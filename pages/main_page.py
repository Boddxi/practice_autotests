from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

# Переход между страницами можно реализовать двумя разными способами.
# Первый способ: возвращать нужный Page Object.
# Для этого в файле main_page.py нужно сделать импорт страницы с логином
# Затем в методе, который осуществляет переход к странице логина, проинициализировать новый объект Page и вернуть его:
    # def go_to_login_page(self):
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()
    #     return LoginPage(browser=self.browser, url=self.browser.current_url)
# Обратите внимание! При создании объекта мы обязательно передаем ему тот же самый объект драйвера для работы с браузером,
# а в качестве url передаем текущий адрес.
# Теперь в тесте нам не нужно думать про инициализацию страницы: она уже создана. Сохранив возвращаемое значение в переменную,
# мы можем использовать методы новой страницы в тесте
# Второй подход: переход происходит неявно, страницу инициализируем в теле теста:


# Теперь модифицируем метод проверки ссылки на логин так, чтобы он выдавал адекватное сообщение об ошибке:
#     def should_be_login_link(self):
#         assert self.is_element_present(By.ID, "registration_link"), "Login link is not presented"
#         # assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

# Обратите внимание здесь на символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

# Первый вариант:
#     def should_be_login_link(self):
#         self.browser.find_element(By.CSS_SELECTOR, "#login_link")



# разработчики добавили alert, который вызывается при клике на нужную нам ссылку.
# Добавив обработку alert в метод go_to_login_page, мы восстановим работоспособность всех тестов, не меняя самих тестов:
# def go_to_login_page(self):
#    link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
#    link.click()
#    alert = self.browser.switch_to.alert
#    alert.accept()
# Это еще одно преимущество использования паттерна Page Object — мы разделяем сам тест и логику взаимодействия со страницей.
# Тест становится более читабельным, и его легче поддерживать при изменениях в коде приложения.
