from selenium.webdriver.common.by import By

# Внутри создайте новый класс. Каждый класс будет соответствовать каждому классу PageObject:


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
# теперь каждый селектор — это пара: как искать и что искать.
# Исправлять руками сломанные селекторы во всем проекте — долго и муторно, и есть большой риск забыть и оставить старый селектор.
# Когда мы выносим селекторы в отдельную сущность, мы уменьшаем время на поддержку тестов и сильно упрощаем себе жизнь в долгосрочной перспективе.

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

