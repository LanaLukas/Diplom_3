import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.order_modal import OrderModal
from test_data import TEST_BUN_NAME, TEST_FILLING_NAME, TEST_USER_EMAIL, TEST_USER_PASSWORD
from test_url import ORDER_FEED_URL, MAIN_PAGE_URL


class TestConstructor:
    @allure.title('Переход по клику на «Конструктор»')
    @allure.description('Проверяем, что клик по «Конструктор» переводит на главную страницу конструктора.')
    def test_navigate_to_constructor(self, driver):
        order_feed_page = OrderFeedPage(driver).open()
        order_feed_page.click_constructor_link()
        assert order_feed_page.wait_for_url_to_be(MAIN_PAGE_URL)

    @allure.title('Переход по клику на «Лента заказов»')
    @allure.description('Проверяем, что клик по «Лента Заказов» переводит на страницу /feed.')
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver).open()
        main_page.click_order_feed_link()
        assert main_page.wait_for_url_to_be(ORDER_FEED_URL)

    @allure.title('Клик на ингредиент открывает всплывающее окно с деталями')
    @allure.description('Проверяем, что клик по ингредиенту открывает модальное окно с деталями.')
    def test_click_ingredient_opens_details_modal(self, driver):
        main_page = MainPage(driver).open()
        main_page.click_ingredient(TEST_BUN_NAME)
        assert main_page.is_ingredient_modal_visible()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    @allure.description('Проверяем, что модальное окно ингредиента закрывается при клике на крестик.')
    def test_ingredient_modal_closes_on_cross_click(self, driver):
        main_page = MainPage(driver).open()
        main_page.click_ingredient(TEST_BUN_NAME)
        main_page.close_modal()
        assert main_page.is_ingredient_modal_closed()

    @allure.title('Добавление ингредиента увеличивает каунтер')
    @allure.description('Проверяем, что при добавлении ингредиента в заказ увеличивается счётчик данного ингредиента.')
    def test_add_ingredient_increases_counter(self, driver):
        main_page = MainPage(driver).open()
        counter_before = main_page.get_ingredient_counter_safe(TEST_BUN_NAME)
        main_page.add_ingredient_to_burger(TEST_BUN_NAME)
        counter_after = main_page.get_ingredient_counter_safe(TEST_BUN_NAME)
        assert counter_after > counter_before

    @allure.title('Залогиненный пользователь может оформить заказ')
    @allure.description('Проверяем, что залогиненный пользователь может оформить заказ и видит окно подтверждения с реальным номером заказа.')
    def test_logged_in_user_can_place_order(self, driver):
        LoginPage(driver).open().login(TEST_USER_EMAIL, TEST_USER_PASSWORD)
        main_page = MainPage(driver)
        main_page.add_ingredient_to_burger(TEST_BUN_NAME)
        main_page.add_ingredient_to_burger(TEST_FILLING_NAME)
        main_page.click_place_order_button()
        order_modal = OrderModal(driver)
        assert order_modal.is_modal_visible()
        assert order_modal.wait_for_order_number_not_9999() != "9999"