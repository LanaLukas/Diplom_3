import allure
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from test_url import ORDER_FEED_URL


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем ленту заказов')
    def open(self):
        self.open_url(ORDER_FEED_URL)
        return self

    @allure.step('Кликаем по заказу по номеру')
    def click_order_by_number(self, number):
        locator = (
            OrderFeedPageLocators.ORDER_CARD_BY_NUMBER[0],
            OrderFeedPageLocators.ORDER_CARD_BY_NUMBER[1].format(number=number),
        )
        self.click_element(locator)

    @allure.step('Кликаем по первому заказу в ленте')
    def click_first_order(self):
        self.click_element(OrderFeedPageLocators.ORDER_CARD)

    @allure.step('Получаем счётчик «Выполнено за всё время»')
    def get_total_orders_counter(self):
        return int(self.get_text(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER))

    @allure.step('Получаем счётчик «Выполнено за сегодня»')
    def get_today_orders_counter(self):
        return int(self.get_text(OrderFeedPageLocators.TODAY_ORDERS_COUNTER))

    @allure.step('Ожидаем появление номера заказа {order_number} в разделе «В работе»')
    def wait_for_order_in_progress(self, order_number, timeout=20):
        formatted_number = f"0{order_number}"
        plain_number = str(order_number)

        def order_appeared(driver):
            elements = driver.find_elements(*OrderFeedPageLocators.IN_PROGRESS_ORDERS_LIST)
            texts = [el.text for el in elements]
            return formatted_number in texts or plain_number in texts

        return WebDriverWait(self.driver, timeout).until(order_appeared)