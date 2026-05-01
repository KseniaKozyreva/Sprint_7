import configuration
import requests

# Создание курьера
def post_create_courier(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_COURIER_PATH,
                         json=body)

# Логин курьера
def post_login_courier(body):
    return requests.post(configuration.URL_SERVICE + configuration.LOGIN_COURIER_PATH,
                         json=body)

# Создание заказа
def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

# Получение списка заказов
def get_orders_list():
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH)

# Удаление куртера по его id
def delete_courier(courier_id):
    return requests.delete(configuration.URL_SERVICE + configuration.CREATE_COURIER_PATH + f"/{courier_id}")
