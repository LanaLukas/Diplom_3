import allure

from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from test_url import FORGOT_PASSWORD_URL


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем страницу восстановления пароля')
    def open(self):
        self.open_url(FORGOT_PASSWORD_URL)
        return self

    @allure.step('Вводим email')
    def enter_email(self, email):
        self.enter_text(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step('Кликаем «Восстановить»')
    def click_recover_button(self):
        self.click_element(ForgotPasswordPageLocators.RECOVER_BUTTON)