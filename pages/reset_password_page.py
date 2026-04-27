import allure

from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Вводим пароль')
    def enter_password(self, password):
        self.enter_text(ResetPasswordPageLocators.PASSWORD_INPUT, password)

    @allure.step('Кликаем кнопку показать/скрыть пароль')
    def click_show_hide_password_button(self):
        self.click_element(ResetPasswordPageLocators.SHOW_HIDE_PASSWORD_BUTTON)

    @allure.step('Проверяем, что поле пароля активно (подсвечено)')
    def is_password_field_active(self):
        return self.is_element_visible(ResetPasswordPageLocators.ACTIVE_PASSWORD_INPUT)