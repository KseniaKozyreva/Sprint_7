import configuration
import requests
import allure

# Создание курьера
@allure.step("Отправка запроса на создание курьера")
def post_create_courier(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_COURIER_PATH,
                         json=body)

# Логин курьера
@allure.step("Отправка запроса на логин курьера")
def post_login_courier(body):
    return requests.post(configuration.URL_SERVICE + configuration.LOGIN_COURIER_PATH,
                         json=body)

# Создание заказа
@allure.step("Отправка запроса на создание заказа")
def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

# Получение списка заказов
@allure.step("Отправка запроса на получение списка заказов")
def get_orders_list():
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH)

# Удаление куртера по его id
@allure.step("Отправка запроса на удаление курьера")
def delete_courier(courier_id):
    return requests.delete(configuration.URL_SERVICE + configuration.CREATE_COURIER_PATH + f"/{courier_id}")
