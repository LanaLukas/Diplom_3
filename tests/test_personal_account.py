import allure

from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
from test_url import ORDER_HISTORY_PAGE_URL, LOGIN_PAGE_URL
from test_data import TEST_USER_EMAIL, TEST_USER_PASSWORD


class TestPersonalAccount:
    @allure.title('Переход по клику на «Личный кабинет»')
    @allure.description('Проверяем, что клик по «Личный Кабинет» для залогиненного пользователя ведёт на страницу профиля.')
    def test_navigate_to_personal_account(self, driver):
        LoginPage(driver).open().login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        main_page = MainPage(driver)
        main_page.click_personal_account_link()
        profile_page = ProfilePage(driver)
        assert profile_page.is_profile_page_displayed()

    @allure.title('Переход в раздел «История заказов»')
    @allure.description('Проверяем, что клик по «История заказов» в личном кабинете открывает раздел с историей.')
    def test_navigate_to_order_history(self, driver):
        LoginPage(driver).open().login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        main_page = MainPage(driver)
        main_page.click_personal_account_link()
        profile_page = ProfilePage(driver)
        profile_page.click_order_history()
        assert profile_page.wait_for_url_contains(ORDER_HISTORY_PAGE_URL)

    @allure.title('Выход из аккаунта')
    @allure.description('Проверяем, что клик по кнопке «Выход» в личном кабинете разлогинивает пользователя и переводит на страницу входа.')
    def test_logout(self, driver):
        LoginPage(driver).open().login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        main_page = MainPage(driver)
        main_page.click_personal_account_link()
        profile_page = ProfilePage(driver)
        profile_page.click_logout()
        assert profile_page.wait_for_url_to_be(LOGIN_PAGE_URL)