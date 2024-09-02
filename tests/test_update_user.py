import allure
import requests

from helpers.data import Endpoints, Message

class TestUpdateUser:

    @allure.title('Проверка изменения почты авторизованного пользователя')
    def test_update_email_user_with_authorization(self, helpers, get_token):
        email, name, password = helpers.generate_data()
        payload = {
            'email': email
            }
        headers = {'Authorization': f'{get_token}'}
        response = requests.patch(Endpoints.USER_URL, headers=headers, json=payload)
        assert response.status_code == 200
        assert Message.UPDATE_USER in response.text

    @allure.title('Проверка изменения пароля авторизованного пользователя')
    def test_update_password_user_with_authorization(self, helpers, get_token):
        email, name, password = helpers.generate_data()
        payload = {
            'password': password
            }
        headers = {'Authorization': f'{get_token}'}
        response = requests.patch(Endpoints.USER_URL, headers=headers, json=payload)
        assert response.status_code == 200
        assert Message.UPDATE_USER in response.text

    @allure.title('Проверка изменения имени авторизованного пользователя')
    def test_update_name_user_with_authorization(self, helpers, get_token):
        email, name, password = helpers.generate_data()
        payload = {
            'name': name
            }
        headers = {'Authorization': f'{get_token}'}
        response = requests.patch(Endpoints.USER_URL, headers=headers, json=payload)
        assert response.status_code == 200
        assert Message.UPDATE_USER in response.text

    @allure.title('Проверка изменения данных неавторизованного пользователя')
    def test_update_data_user_without_authorization(self, helpers):
        email, name, password = helpers.generate_data()
        payload = {
            'email': email,
            'password': password
            }
        response = requests.patch(Endpoints.USER_URL, json=payload)
        assert response.status_code == 401
        assert Message.UPDATE_USER_UNSUCCESSFULLY in response.text