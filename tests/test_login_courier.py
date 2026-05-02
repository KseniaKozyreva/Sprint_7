import pytest
import sender_stand_request
import data
import allure

class TestLoginCourier:

   
    # 1. Курьер может авторизоваться 
    @allure.title("Успешная авторизация курьера")
    def test_login_success(self, courier_data):
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        response = sender_stand_request.post_login_courier(payload)
        assert response.status_code == 200
        assert "id" in response.json() 

    # 2. Неправильный пароль
    @allure.title("Неправильный пароль")
    def test_login_wrong_password_error(self):
        new_courier = data.register_new_courier_and_return_login_password()
        payload = {
            "login": new_courier[0],
            "password": "wrong_password" 
        }
        response = sender_stand_request.post_login_courier(payload)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    # 3. Неправильный логин
    @allure.title("Неправильный логин")
    def test_login_wrong_login_error(self):
        new_courier = data.register_new_courier_and_return_login_password()
        
        payload = {
            "login": new_courier[0] + "abcde", 
            "password": new_courier [1]      
        }
        
        response = sender_stand_request.post_login_courier(payload)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"



    # 4. Отсутствие поля 
    @allure.title("Отсутствие поля")
    def test_login_without_login_field_error(self):
        payload = {"password": "1234"} 
        response = sender_stand_request.post_login_courier(payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    # 5. БАГ: если нет пароля, система зависает
    @allure.title("БАГ: если нет пароля, система зависает")
    @pytest.mark.xfail(reason="Баг: система зависает при отсутствии пароля")
    def test_login_without_password_field_error(self):
        payload = {"login": "some_login"} 
        response = sender_stand_request.post_login_courier(payload)
        assert response.status_code == 400

    # 6. авторизоваться под несуществующим пользователем 
    @allure.title("авторизоваться под несуществующим пользователем")
    def test_login_non_existent_user_error(self):
        payload = {
            "login": "non_existent_user",
            "password": "ani_password"
        }
        response = sender_stand_request.post_login_courier(payload)
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
