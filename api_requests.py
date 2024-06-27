import requests
import config
import data

def get_current_body(firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color):
    current_body = data.body_create_order.copy()
    current_body["firstName"] = firstName
    current_body["lastName"] = lastName
    current_body["address"] = address
    current_body["metroStation"] = metroStation
    current_body["phone"] = phone
    current_body["rentTime"] = rentTime
    current_body["deliveryDate"] = deliveryDate
    current_body["comment"] = comment
    current_body["color"] = color
    return current_body

def create_order(current_body):
    create_response = requests.post(config.URL_HOST + config.CREATE_ORDER_PATH, headers=data.headers, json=current_body)
    return create_response

def get_order_info(track):
    param = {"t": str(track)}
    get_order_response = requests.get(config.URL_HOST + config.GET_ORDER_PATH, params=param)
    return get_order_response
