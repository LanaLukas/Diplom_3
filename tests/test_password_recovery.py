import allure

from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from test_url import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL
from test_data import TEST_USER_EMAIL


class TestPasswordRecovery:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('Проверяем, что клик по ссылке «Восстановить пароль» на странице входа ведёт на страницу /forgot-password.')
    def test_navigate_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver).open()
        login_page.click_forgot_password_link()
        assert login_page.wait_for_url_to_be(FORGOT_PASSWORD_URL)

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @allure.description('Проверяем, что ввод email и клик по кнопке «Восстановить» переходит на страницу /reset-password.')
    def test_enter_email_and_click_recover(self, driver):
        forgot_password_page = ForgotPasswordPage(driver).open()
        forgot_password_page.enter_email(TEST_USER_EMAIL)
        forgot_password_page.click_recover_button()
        assert forgot_password_page.wait_for_url_to_be(RESET_PASSWORD_URL)

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным')
    @allure.description('Проверяем, что клик по кнопке показа/скрытия пароля на странице сброса подсвечивает поле пароля.')
    def test_show_hide_password_button_makes_field_active(self, driver):
        forgot_password_page = ForgotPasswordPage(driver).open()
        forgot_password_page.enter_email(TEST_USER_EMAIL)
        forgot_password_page.click_recover_button()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.enter_password("123456")
        reset_password_page.click_show_hide_password_button()
        assert reset_password_page.is_password_field_active()