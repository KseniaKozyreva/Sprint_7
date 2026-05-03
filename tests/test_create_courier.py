import random
import string
import pytest
import allure
import sender_stand_request
import data

class TestCreateCourier:
    # Успешное создание курьера
    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, delete_courier_after_test):
        login = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        payload = {
            "login": login,
            "password": "password123",
            "firstName": "saske"
        }
        
        #  Удаление данных курьера после теста
        delete_courier_after_test["login"] = payload["login"]
        delete_courier_after_test["password"] = payload["password"]

        response = sender_stand_request.post_create_courier(payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    # 2. Нельзя создать двух одинаковых курьеров
    @allure.title("Ошибка при создании дубликата курьера")
    @pytest.mark.xfail(reason="Баг: сообщение об ошибке не совпадает с документацией")
    def test_create_duplicate_courier_error(self, courier_data):
        response = sender_stand_request.post_create_courier(courier_data)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется"

    # 3. Создание без логина
    @allure.title("Отсутствие логина")
    @pytest.mark.xfail(reason="Баг: сервер возвращает 404 вместо 400")
    def test_create_courier_no_login_error(self):
        payload = {"password": "1234", "firstName": "saske"}
        response = sender_stand_request.post_create_courier(payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    # 4. Создание без пароля
    @allure.title("Отсутствие пароля")
    @pytest.mark.xfail(reason="Баг: сервер возвращает 404 вместо 400")
    def test_create_courier_no_password_error(self):
        payload = {"login": "ninja", "firstName": "saske"}
        response = sender_stand_request.post_create_courier(payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    # 5. Создание двух одинаковых курьеров
    @allure.title("Создание двух одинаковых курьеров")
    @pytest.mark.xfail(reason="Баг: сервер добавляет в сообщение лишнюю фразу '. Попробуйте другой.'")
    def test_create_duplicate_courier_extra(self):
        payload = {
            "login": "ninja_2027", 
            "password": "1234", 
            "firstName": "saske"
        }
        response = sender_stand_request.post_create_courier(payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется"
