class Endpoints:
    HOST = 'https://stellarburgers.nomoreparties.site'
    REGISTER_URL = f'{HOST}/api/auth/register'
    LOGIN_URL = f'{HOST}/api/auth/login'
    TOKEN_URL = f'{HOST}/api/auth/token'
    USER_URL = f'{HOST}/api/auth/user'
    ORDERS_URL = f'{HOST}/api/orders'


class Message:
    CREATE_USER = 'success":true'
    CREATE_USER_TWICE = 'User already exists'
    CREATE_COURIER_WITHOUT_PASSWORD = 'Email, password and name are required fields"'
    LOGIN_USER = '"success":true'
    INCORECT_LOGIN_DATA = 'email or password are incorrect'
    UPDATE_USER = 'success":true'
    UPDATE_USER_UNSUCCESSFULLY = '"You should be authorised"'
    CREATE_ORDER = 'success":true'
    CREATE_ORDER_WITHOUT_INGREDIENTS = 'Ingredient ids must be provided'
    CREATE_ORDER_INCORRECT_INGTEDIENTS = 'Internal Server Error'
    GET_ORDER = 'success":true'
    GET_ORDER_WITHOUT_AUTH = 'You should be authorised'    

class Ingredients:
    BUN_R2_D3 = '61c0c5a71d1f82001bdaaa6d'
    MAIN_PROTOSTOMIA = '61c0c5a71d1f82001bdaaa6f'
    SAUSE_SPICY_X = '61c0c5a71d1f82001bdaaa72'
    INCORRECT_INGTEDIENTS = '61c0c5a71d1f82001bdaaa72test'    