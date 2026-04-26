from selenium.webdriver.common.by import By


class ProfilePageLocators:
    ORDER_HISTORY_LINK = (
        By.XPATH,
        "//a[contains(@class,'Account_link') and normalize-space()='История заказов']",
    )
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'Account_button') and normalize-space()='Выход']",
    )