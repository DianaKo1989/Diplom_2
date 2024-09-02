import pytest
import requests

from helpers.data import Endpoints
from helpers.helpers import Helpers


@pytest.fixture(scope='function')
def helpers():
    return Helpers()

@pytest.fixture(scope='function')
def get_token(helpers):
    email, pwd, name = helpers.register_new_user_and_return_login_password()
    response = requests.post(Endpoints.LOGIN_URL, data={
        'email': email,
        'password': pwd,
        'name': name
    })
    token = response.json().get('accessToken')

    yield token
    requests.delete(Endpoints.USER_URL, headers={'Authorization': f'{token}'})