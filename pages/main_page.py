import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from test_url import MAIN_PAGE_URL


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем главную страницу')
    def open(self):
        self.open_url(MAIN_PAGE_URL)
        return self

    @allure.step('Кликаем по ингредиенту с названием {name}')
    def click_ingredient(self, name):
        locator = (
            MainPageLocators.INGREDIENT_CARD_BY_NAME[0],
            MainPageLocators.INGREDIENT_CARD_BY_NAME[1].format(name=name),
        )
        self.click_element(locator)

    @allure.step('Получаем счётчик ингредиента {name} (0 если не виден)')
    def get_ingredient_counter_safe(self, name):
        locator = (
            MainPageLocators.INGREDIENT_COUNTER[0],
            MainPageLocators.INGREDIENT_COUNTER[1].format(name=name),
        )
        if self.is_element_visible(locator):
            return int(self.get_text(locator))
        return 0

    @allure.step('Перетаскиваем ингредиент {name} в конструктор')
    def drag_ingredient_to_constructor(self, name):
        ingredient_locator = (
            MainPageLocators.INGREDIENT_CARD_BY_NAME[0],
            MainPageLocators.INGREDIENT_CARD_BY_NAME[1].format(name=name),
        )
        self.drag_and_drop(ingredient_locator, MainPageLocators.CONSTRUCTOR_DROP_ZONE)

    @allure.step('Добавляем ингредиент {name} в бургер (drag-and-drop)')
    def add_ingredient_to_burger(self, name):
        self.drag_ingredient_to_constructor(name)

    @allure.step('Кликаем «Оформить заказ»')
    def click_place_order_button(self):
        self.click_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Закрываем модальное окно')
    def close_modal(self):
        self.click_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step('Проверяем видимость модального окна ингредиента')
    def is_ingredient_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step('Проверяем, что модальное окно ингредиента закрыто')
    def is_ingredient_modal_closed(self):
        return self.is_element_not_visible(MainPageLocators.INGREDIENT_MODAL_TITLE)