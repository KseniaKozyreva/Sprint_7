import sender_stand_request   

class TestGetOrders:
     #  Возвращается список заказов
    def test_get_orders_list_returns_list(self):
        response = sender_stand_request.get_orders_list()
    
        assert response.status_code == 200
    
        assert "orders" in response.json(), "В ответе отсутствует поле 'orders'"
    
        assert isinstance(response.json()["orders"], list), "Поле 'orders' не является списком"
