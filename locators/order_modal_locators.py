from selenium.webdriver.common.by import By


class OrderModalLocators:
    ORDER_DETAIL_CONTAINER = (
        By.XPATH,
        "//div[contains(@class,'Modal_modal_opened')] | //div[contains(@class,'Modal_pageBox')] | //div[contains(@class,'Modal_orderBox')]",
    )
    ORDER_NUMBER_IN_MODAL = (
        By.XPATH,
        "//h2[contains(@class,'Modal_modal__title')]",
    )