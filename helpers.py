import allure
import requests

from test_url import API_LOGIN_URL, API_ORDERS_URL, API_INGREDIENTS_URL
from test_data import (
    TEST_USER_EMAIL,
    TEST_USER_PASSWORD,
    EMAIL_FIELD,
    PASSWORD_FIELD,
    AUTHORIZATION_HEADER,
    ACCESS_TOKEN_FIELD,
    INGREDIENTS_FIELD,
    ORDER_FIELD,
    NUMBER_FIELD,
    DATA_FIELD
)


@allure.step('Создаем заказ')
def create_order_with_ingredients():
    logged_in_user = login_user(TEST_USER_EMAIL, TEST_USER_PASSWORD)
    ingredients = get_ingredients()
    ingredient_ids = [ingredients[0]["_id"], ingredients[1]["_id"]]
    headers = {AUTHORIZATION_HEADER: logged_in_user[ACCESS_TOKEN_FIELD]}
    payload = {INGREDIENTS_FIELD: ingredient_ids}
    response = requests.post(API_ORDERS_URL, headers=headers, json=payload)
    return response.json()[ORDER_FIELD][NUMBER_FIELD]

@allure.step('Выполняем вход')
def login_user(email, password):
    payload = {EMAIL_FIELD: email, PASSWORD_FIELD: password}
    response = requests.post(API_LOGIN_URL, data=payload)
    return response.json()

@allure.step('Получаем ингредиенты')
def get_ingredients():
    response = requests.get(API_INGREDIENTS_URL)
    return response.json()[DATA_FIELD]
