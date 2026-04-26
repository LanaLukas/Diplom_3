import allure

from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from test_url import LOGIN_PAGE_URL, MAIN_PAGE_URL


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем страницу входа')
    def open(self):
        self.open_url(LOGIN_PAGE_URL)
        return self

    @allure.step('Вводим email')
    def enter_email(self, email):
        self.enter_text(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step('Вводим пароль')
    def enter_password(self, password):
        self.enter_text(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step('Кликаем «Войти»')
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Кликаем «Восстановить пароль»')
    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Выполняем вход')
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        self.wait_for_url_to_be(MAIN_PAGE_URL)
        self.wait_for_loading_overlay_to_disappear()