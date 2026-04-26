import allure

from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from test_url import PROFILE_PAGE_URL


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем «История заказов»')
    def click_order_history(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step('Кликаем «Выход»')
    def click_logout(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step('Проверяем, что находимся на странице профиля')
    def is_profile_page_displayed(self):
        return self.wait_for_url_to_be(PROFILE_PAGE_URL)