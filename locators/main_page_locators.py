from selenium.webdriver.common.by import By


class MainPageLocators:
    INGREDIENT_CARD_BY_NAME = (
        By.XPATH,
        "//a[contains(@class,'BurgerIngredient_ingredient') and .//p[contains(@class,'ingredient__text') and normalize-space()='{name}']]",
    )
    INGREDIENT_COUNTER = (
        By.XPATH,
        "//a[contains(@class,'BurgerIngredient_ingredient') and .//p[contains(@class,'ingredient__text') and normalize-space()='{name}']]//p[contains(@class,'counter_counter__num')]",
    )
    CONSTRUCTOR_DROP_ZONE = (
        By.XPATH,
        "//section[contains(@class,'BurgerConstructor_basket')]",
    )
    PLACE_ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'button_button') and normalize-space()='Оформить заказ']",
    )
    INGREDIENT_MODAL_TITLE = (
        By.XPATH,
        "//h2[contains(@class,'Modal_modal__title') and normalize-space()='Детали ингредиента']",
    )
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'Modal_modal__close')]",
    )