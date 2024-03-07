import configuration
import requests
import data
# Ольга Морозова, 14-я когорта — Финальный проект. Инженер по тестированию плюс

# функция создания заказа
def make_order_track():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDERS,
                         json=data.order_body)
    return str(response.json()["track"])

# функция получения заказа по номеру заказа
def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS + track_number)

# функция проверки заказа
def check_order(track_number, status):
    response_new_order = get_order(track_number)
    assert response_new_order.status_code == status

# тесты на проверку статуса
def test_positive_status_code():
    check_order(make_order_track(), 200)

def test_negative_status_code():
    check_order(str(10), 404)