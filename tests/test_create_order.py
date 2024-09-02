import allure
import requests

from helpers.data import Endpoints, Ingredients, Message


class TestCreateOrder:

    @allure.title('Проверка создания заказа без ингредиентов')
    def test_create_order_without_ingredients(self):
        payload = {
            'ingredients': []
        }
        
        response = requests.post(Endpoints.ORDERS_URL, json=payload)
        assert response.status_code == 400
        assert Message.CREATE_ORDER_WITHOUT_INGREDIENTS in response.text

    @allure.title('Проверка создания заказа с неправильным хешем ингредиента')
    def test_create_order_incorrect_ingredients(self):
        payload = {
            'ingredients': [Ingredients.BUN_R2_D3, Ingredients.MAIN_PROTOSTOMIA, Ingredients.INCORRECT_INGTEDIENTS]
        }
        response = requests.post(Endpoints.ORDERS_URL, json=payload)
        assert response.status_code == 500
        assert Message.CREATE_ORDER_INCORRECT_INGTEDIENTS in response.text

    @allure.title('Проверка успешного создания заказа с авторизацией')
    def test_create_order_with_authorization_successfully(self, get_token):
        payload = {
            'ingredients': [Ingredients.BUN_R2_D3, Ingredients.MAIN_PROTOSTOMIA, Ingredients.SAUSE_SPICY_X]
        }
        headers = {'Authorization': f'{get_token}'}
        response = requests.post(Endpoints.ORDERS_URL, headers=headers, json=payload)
        assert response.status_code == 200
        assert Message.CREATE_ORDER in response.text

    @allure.title('Проверка успешного создания заказа без авторизации')
    def test_create_order_without_authorization(self):
        payload = {
            'ingredients': [Ingredients.BUN_R2_D3, Ingredients.MAIN_PROTOSTOMIA, Ingredients.SAUSE_SPICY_X]
        }
        response = requests.post(Endpoints.ORDERS_URL, json=payload)
        assert response.status_code == 200
        assert Message.CREATE_ORDER in response.text        