import random
import string

import allure
import requests

from .data import Endpoints


class Helpers:

    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string


    def generate_random_email(self, domain='mail.ru', username_prefix='DianaKo1989'):
        random_number = random.randint(0, 9999)
        login = f'{username_prefix}{random_number}'
        email = f'{login}@{domain}'
        return email


    def generate_data(self):
        email = self.generate_random_email()
        name = self.generate_random_string(10)
        password = self.generate_random_string(10)
        return email, name, password

    @allure.step('Регистрируем нового пользователя и получаем информацию для авторизации')
    def register_new_user_and_return_login_password(self):
        login_pass = []

        email = self.generate_random_email()
        password = self.generate_random_string(10)
        name = self.generate_random_string(10)

        payload = {
            'email': email,
            'password': password,
            'name': name,
        }

        response = requests.post(Endpoints.REGISTER_URL, data=payload)

        if response.status_code == 200:
            login_pass.append(email)
            login_pass.append(password)
            login_pass.append(name)

        return login_pass