from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (
        By.XPATH,
        "//label[text()='Email']/following-sibling::input",
    )
    PASSWORD_INPUT = (
        By.XPATH,
        "//div[contains(@class,'input_type_password')]//input[contains(@class,'input__textfield')]",
    )
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'button_button_type_primary') and normalize-space()='Войти']",
    )
    FORGOT_PASSWORD_LINK = (
        By.XPATH,
        "//a[contains(@class,'Auth_link') and normalize-space()='Восстановить пароль']",
    )