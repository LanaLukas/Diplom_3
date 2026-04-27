from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_CARD = (
        By.XPATH,
        "//li[contains(@class,'OrderHistory_listItem')]//a[contains(@class,'OrderHistory_link')]",
    )
    ORDER_CARD_BY_NUMBER = (
        By.XPATH,
        "//li[contains(@class,'OrderHistory_listItem')]//p[contains(@class,'text_type_digits-default') and contains(.,'{number}')]",
    )
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "(//div[contains(@class,'OrderFeed_ordersData')]//p[contains(@class,'OrderFeed_number') and contains(@class,'text_type_digits-large')])[1]",
    )
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "(//div[contains(@class,'OrderFeed_ordersData')]//p[contains(@class,'OrderFeed_number') and contains(@class,'text_type_digits-large')])[2]",
    )
    IN_PROGRESS_ORDERS_LIST = (
        By.XPATH,
        "//ul[contains(@class,'OrderFeed_orderList') and not(contains(@class,'OrderFeed_orderListReady'))]/li",
    )