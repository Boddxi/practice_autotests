from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.base_page import BasePage
from pages.locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    # def should_be_login_link(self):
    #     self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

# Теперь модифицируем метод проверки ссылки на логин так, чтобы он выдавал адекватное сообщение об ошибке:

#     def should_be_login_link(self):
#         assert self.is_element_present(By.ID, "registration_link"), "Login link is not presented"
#         # assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

# Обратите внимание здесь на символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"



