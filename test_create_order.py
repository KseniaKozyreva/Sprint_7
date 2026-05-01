import pytest
import sender_stand_request
import data

class TestCreateOrder:

    @pytest.mark.parametrize("color", [
        ["BLACK"], 
        ["GREY"], 
        ["BLACK", "GREY"], 
        ([])
    ])
    def test_create_order_with_different_colors(self, color):
        payload = data.order_body.copy()
        payload["color"] = color
        
        response = sender_stand_request.post_create_order(payload)
        
        assert response.status_code == 201
        assert "track" in response.json()
