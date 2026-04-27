from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    PASSWORD_INPUT = (
        By.XPATH,
        "//div[contains(@class,'input_type_password')]//input[contains(@class,'input__textfield')]",
    )
    SHOW_HIDE_PASSWORD_BUTTON = (
        By.CSS_SELECTOR,
        "div[class*='input__icon-action']",
    )
    ACTIVE_PASSWORD_INPUT = (
        By.CSS_SELECTOR,
        "div[class*='input_status_active']",
    )