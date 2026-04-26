import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from helpers import create_order_with_ingredients
from pages.order_feed_page import OrderFeedPage
from pages.order_modal import OrderModal
from locators.order_feed_page_locators import OrderFeedPageLocators


class TestOrderFeed:
    @allure.title('Клик на заказ открывает детали заказа')
    @allure.description('Проверяем, что клик по заказу в ленте заказов открывает страницу с деталями заказа.')
    def test_click_order_opens_details_modal(self, driver):
        order_feed_page = OrderFeedPage(driver).open()
        order_feed_page.click_first_order()
        order_modal = OrderModal(driver)
        assert order_modal.is_modal_visible()

    @allure.title('Заказы пользователя из «Истории заказов» отображаются в ленте заказов')
    @allure.description('Проверяем, что заказы, созданные пользователем, отображаются в ленте заказов.')
    def test_user_orders_appear_in_order_feed(self, driver):
        order_number = create_order_with_ingredients()
        order_feed_page = OrderFeedPage(driver).open()
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(OrderFeedPageLocators.ORDER_CARD)
        )

        order_feed_page.click_order_by_number(order_number)
        order_modal = OrderModal(driver)
        assert order_modal.is_modal_visible()

    @allure.title('При создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    @allure.description('Проверяем, что после оформления нового заказа counter_total увеличивается.')
    def test_total_orders_counter_increases_after_new_order(self, driver):
        order_feed_page = OrderFeedPage(driver).open()
        counter_before = order_feed_page.get_total_orders_counter()
        create_order_with_ingredients()
        order_feed_page.open()
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER)
        )
        counter_after = order_feed_page.get_total_orders_counter()
        assert counter_after > counter_before

    @allure.title('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    @allure.description('Проверяем, что после оформления нового заказа counter_today увеличивается.')
    def test_today_orders_counter_increases_after_new_order(self, driver):
        order_feed_page = OrderFeedPage(driver).open()
        counter_before = order_feed_page.get_today_orders_counter()
        create_order_with_ingredients()
        order_feed_page.open()
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(OrderFeedPageLocators.TODAY_ORDERS_COUNTER)
        )
        counter_after = order_feed_page.get_today_orders_counter()
        assert counter_after > counter_before

    @allure.title('После оформления заказа его номер появляется в разделе «В работе»')
    @allure.description('Проверяем, что после создания нового заказа его номер появляется в блоке «В работе» на странице ленты заказов.')
    def test_new_order_number_appears_in_progress_section(self, driver):
        order_number = create_order_with_ingredients()
        order_feed_page = OrderFeedPage(driver).open()
        assert order_feed_page.wait_for_order_in_progress(order_number)