import allure
import requests

from helpers.data import Ingredients, Message, Endpoints


class TestGetOrders:

    @allure.title('Проверка получения заказа конкретного пользователя c авторизацией')
    def test_get_order_successfully(self, get_token):
        token = get_token
        payload = {
            'ingredients': [Ingredients.BUN_R2_D3, Ingredients.MAIN_PROTOSTOMIA, Ingredients.SAUSE_SPICY_X]
        }
        headers = {'Authorization': f'{token}'}
        response = requests.get(Endpoints.ORDERS_URL, headers=headers, json=payload)
        assert response.status_code == 200
        assert Message.GET_ORDER in response.text


    @allure.title('Проверка получения заказа конкретного пользователя без авторизации')
    def test_get_order_without_authorization(self):
        response = requests.get(Endpoints.ORDERS_URL)
        assert response.status_code == 401
        assert Message.GET_ORDER_WITHOUT_AUTH in response.text