import allure
import requests

from helpers.data import Endpoints, Message

class TestLoginUser:

    @allure.title('Проверка авторизации пользователя')
    def test_login_user_successfully(self, helpers):
        data = helpers.register_new_user_and_return_login_password()
        response = requests.post(Endpoints.LOGIN_URL, data={
            'email': data[0],
            'password': data[1],
        })
        assert response.status_code == 200
        assert Message.LOGIN_USER in response.text

    @allure.title('Проверка авторизации пользователя с неверным логином ')
    def test_login_user_incorrect_login(self, helpers):
        _, email, pwd = helpers.register_new_user_and_return_login_password()
        response = requests.post(Endpoints.LOGIN_URL, data={
            'email': email,
            'password': pwd,
        })
        assert response.status_code == 401
        assert Message.INCORECT_LOGIN_DATA in response.text

    @allure.title('Проверка авторизации пользователя с неверным паролем')
    def test_login_user_incorrect_password(self, helpers):
        _, email, pwd = helpers.register_new_user_and_return_login_password()
        response = requests.post(Endpoints.LOGIN_URL, data={
            'email': email,
            'password': pwd,
        })
        assert response.status_code == 401
        assert Message.INCORECT_LOGIN_DATA in response.text