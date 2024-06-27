# Бондарев Роман, 17-я когорта — Финальный проект. Инженер по тестированию плюс
import api_requests

def test_get_order_info():
    current_body = api_requests.get_current_body("Бондарев", "Роман", "Ленина 249", 5, "89050810359", 1, "2024-06-26", "тест", ["BLACK"])
    create_order_response = api_requests.create_order(current_body)
    track = create_order_response.json()["track"]
    get_order_response = api_requests.get_order_info(track)
    assert get_order_response.status_code == 200
    assert get_order_response.json()["order"]["track"] == track
