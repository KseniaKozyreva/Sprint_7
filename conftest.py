import pytest
import sender_stand_request
import data

@pytest.fixture
def courier_data():
    # Регистрация курьера
    login, password, first_name = data.register_new_courier_and_return_login_password()
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    yield payload
    # Удаление курьера
    login_response = sender_stand_request.post_login_courier(payload)
    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")
        if courier_id:
            sender_stand_request.delete_courier(courier_id)


@pytest.fixture
def delete_courier_after_test():
    # для удаления курьера после успешного создания
    courier_to_delete = {}
    yield courier_to_delete
    
    # После теста удаляем данные курьера
    if "login" in courier_to_delete and "password" in courier_to_delete:
        login_response = sender_stand_request.post_login_courier(courier_to_delete)
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            if courier_id:
                sender_stand_request.delete_courier(courier_id)
