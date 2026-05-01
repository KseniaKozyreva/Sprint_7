import pytest
import sender_stand_request
import data

class TestCreateCourier:

    # 1. Успешное создание курьера 
    def test_create_courier_success(self):
        result = data.register_new_courier_and_return_login_password()
        
        assert len(result) == 3
        assert result[0] != ""

    # 2. Нельзя создать двух одинаковых курьеров 
    @pytest.mark.xfail(reason="Баг: сообщение об ошибке не совпадает с документацией")
    def test_create_duplicate_courier_error(self):
        new_courier = data.register_new_courier_and_return_login_password()
        payload = {"login": new_courier[0], "password": new_courier[1], "firstName": new_courier[2]}
        
        sender_stand_request.post_create_courier(payload)
        response = sender_stand_request.post_create_courier(payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется"

    # 3. Создание без логина 
    @pytest.mark.xfail(reason="Баг: сервер возвращает 404 вместо 400")
    def test_create_courier_no_login_error(self):
        payload = {"password": "1234", "firstName": "saske"}
        response = sender_stand_request.post_create_courier(payload)
        assert response.status_code == 400 
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    # 4. Создание без пароля 
    @pytest.mark.xfail(reason="Баг: сервер возвращает 404 вместо 400")
    def test_create_courier_no_password_error(self):
        payload = {"login": "ninja", "firstName": "saske"}
        response = sender_stand_request.post_create_courier(payload)
        assert response.status_code == 400 
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    # 5. Создание двух одинаковых курьеров
    @pytest.mark.xfail(reason="Баг: сервер добавляет в сообщение лишнюю фразу '. Попробуйте другой.'")
    def test_create_duplicate_courier_error(self):
        payload = { "login": "ninja_2027", "password": "1234", "firstName": "saske"}
        response = sender_stand_request.post_create_courier(payload)
        
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется"
