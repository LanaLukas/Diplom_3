from selenium.webdriver.common.by import By


class BasePageLocators:
    HEADER_CONSTRUCTOR_LINK = (
        By.XPATH,
        "//a[contains(@class,'AppHeader_header__link')][.//p[contains(text(),'Конструктор')]]",
    )
    HEADER_ORDER_FEED_LINK = (
        By.XPATH,
        "//a[contains(@class,'AppHeader_header__link')][.//p[contains(text(),'Лента')]]",
    )
    HEADER_PERSONAL_ACCOUNT_LINK = (
        By.XPATH,
        "//a[contains(@class,'AppHeader_header__link')][.//p[contains(text(),'Личный')]]",
    )