import allure
import requests

from helpers.data import Message, Endpoints


class TestCreateUser:

    @allure.title('Проверка создания уникального пользователя')
    def test_create_unique_user_successfully(self, helpers):
        email, name, password = helpers.generate_data()
        payload = {
            'email': email,
            'password': password,
            'name': name,
            }
        response = requests.post(Endpoints.REGISTER_URL, data=payload)
        assert response.status_code == 200
        assert Message.CREATE_USER in response.text

    @allure.title('Проверка невозможности создания двух одинаковых пользователей')
    def test_create_courier_twice(self, helpers):
        email, password, name = helpers.register_new_user_and_return_login_password()
        response = requests.post(Endpoints.REGISTER_URL, data={
            'email': email,
            'password': password,
            'name': name
        })
        assert response.status_code == 403
        assert Message.CREATE_USER_TWICE in response.text

    @allure.title('Проверка создания пользователя без имени')
    def test_create_courier_without_name(self, helpers):
        email, name, password = helpers.generate_data()
        payload = {
            'email': email,
            'password': password,
            }
        response = requests.post(Endpoints.REGISTER_URL, data=payload)
        assert response.status_code == 403
        assert Message.CREATE_COURIER_WITHOUT_PASSWORD in response.text

    @allure.title('Проверка создания пользователя без почты')
    def test_create_courier_without_email(self, helpers):
        email, name, password = helpers.generate_data()
        payload = {
            'password': password,
            'name': name,
            }
        response = requests.post(Endpoints.REGISTER_URL, data=payload)
        assert response.status_code == 403
        assert Message.CREATE_COURIER_WITHOUT_PASSWORD in response.text

    @allure.title('Проверка создания пользователя без пароля')
    def test_create_courier_without_password(self, helpers):
        email, name, password = helpers.generate_data()
        payload = {
            'email': email,
            'name': name,
            }
        response = requests.post(Endpoints.REGISTER_URL, data=payload)
        assert response.status_code == 403
        assert Message.CREATE_COURIER_WITHOUT_PASSWORD in response.text