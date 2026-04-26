import allure

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step('Находим видимый элемент')
    def find_visible_element(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    @allure.step('Открываем страницу {url}')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Ожидаем URL {url}')
    def wait_for_url_to_be(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.url_to_be(url))

    @allure.step('Ожидаем URL содержит {text}')
    def wait_for_url_contains(self, text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(ec.url_contains(text))

    @allure.step('Кликаем по элементу')
    def click_element(self, locator):
        element = self.wait.until(ec.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.wait_for_loading_overlay_to_disappear()
            element = self.wait.until(ec.element_to_be_clickable(locator))
            try:
                element.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Вводим текст в поле')
    def enter_text(self, locator, text):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)
        return element

    @allure.step('Проверяем видимость элемента')
    def is_element_visible(self, locator):
        try:
            self.wait.until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step('Проверяем невидимость элемента')
    def is_element_not_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step('Получаем текст элемента')
    def get_text(self, locator):
        return self.find_visible_element(locator).text

    @allure.step('Перетаскиваем элемент {source_locator} на {target_locator}')
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_visible_element(source_locator)
        target = self.find_visible_element(target_locator)
        js_drag = """
        function createEvent(type) {
            var event = document.createEvent('Event');
            event.initEvent(type, true, true);
            event.dataTransfer = { data: {}, setData: function(k,v) { this.data[k]=v; }, getData: function(k) { return this.data[k]; } };
            return event;
        }
        var src = arguments[0];
        var tgt = arguments[1];
        var dragStart = createEvent('dragstart');
        src.dispatchEvent(dragStart);
        var drag = createEvent('drag');
        tgt.dispatchEvent(drag);
        var dragOver = createEvent('dragover');
        tgt.dispatchEvent(dragOver);
        var drop = createEvent('drop');
        drop.dataTransfer = dragStart.dataTransfer;
        tgt.dispatchEvent(drop);
        var dragEnd = createEvent('dragend');
        src.dispatchEvent(dragEnd);
        """
        self.driver.execute_script(js_drag, source, target)

    @allure.step('Кликаем по ссылке «Конструктор»')
    def click_constructor_link(self):
        self.click_element(BasePageLocators.HEADER_CONSTRUCTOR_LINK)

    @allure.step('Кликаем по ссылке «Лента Заказов»')
    def click_order_feed_link(self):
        self.click_element(BasePageLocators.HEADER_ORDER_FEED_LINK)

    @allure.step('Кликаем по ссылке «Личный Кабинет»')
    def click_personal_account_link(self):
        self.click_element(BasePageLocators.HEADER_PERSONAL_ACCOUNT_LINK)

    @allure.step('Ожидаем исчезновения оверлея загрузки')
    def wait_for_loading_overlay_to_disappear(self):
        try:
            WebDriverWait(self.driver, 5).until(
                ec.invisibility_of_element_located(
                    (By.XPATH, "//div[contains(@class,'Modal_modal_overlay')]")
                )
            )
        except TimeoutException:
            pass