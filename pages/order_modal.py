import allure

from pages.base_page import BasePage
from locators.order_modal_locators import OrderModalLocators


class OrderModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверяем видимость модального окна')
    def is_modal_visible(self):
        return self.is_element_visible(OrderModalLocators.ORDER_DETAIL_CONTAINER)

    @allure.step('Ожидаем, что номер заказа не равен 9999')
    def wait_for_order_number_not_9999(self, timeout=15):
        def order_number_ready(driver):
            elements = driver.find_elements(*OrderModalLocators.ORDER_NUMBER_IN_MODAL)
            if not elements:
                return False
            text = elements[0].text.strip()
            return text and text != "9999"
        self.wait_until(order_number_ready, timeout)
        return self.get_text(OrderModalLocators.ORDER_NUMBER_IN_MODAL)