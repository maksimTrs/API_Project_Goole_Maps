from utils.http_methods import HttpMethod
from typing import Final

"""Testing https://rahulshettyacademy.com/maps/api/place/add/json?key=qaclick123"""

BASE_URL: Final = "https://rahulshettyacademy.com"
KEY: Final = "key=qaclick123"
KEY_SEPARATOR: Final = "?"
PLACE_ID_SEPARATOR: Final = "&"
PLACE_ID: Final = "place_id="
POST_PATH: Final = "/maps/api/place/add/json"
GET_PATH: Final = "/maps/api/place/get/json"
PUT_PATH: Final = "/maps/api/place/update/json"
DELETE_PATH: Final = "/maps/api/place/delete/json"


class GoogleMapsApi():

    @staticmethod
    def create_new_google_maps_place():
        json_post_body = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_request_url = BASE_URL + POST_PATH + KEY_SEPARATOR + KEY
        print(post_request_url)

        post_response = HttpMethod.send_post_method(post_request_url, json_post_body)
        print(post_response.json())

        return post_response

    @staticmethod
    def get_google_maps_place(place_id):
        get_request_url = BASE_URL + GET_PATH + KEY_SEPARATOR + KEY + PLACE_ID_SEPARATOR + PLACE_ID + place_id
        print(get_request_url)

        get_response = HttpMethod.send_get_method(get_request_url)
        print(get_response.json())

        return get_response

    @staticmethod
    def update_google_maps_place(place_id):
        json_post_body = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        put_request_url = BASE_URL + PUT_PATH + KEY_SEPARATOR + KEY
        print(put_request_url)

        put_response = HttpMethod.send_put_method(put_request_url, json_post_body)
        print(put_response.json())

        return put_response

    @staticmethod
    def delete_google_maps_place(place_id):
        json_post_body = {
            "place_id": place_id
        }

        delete_request_url = BASE_URL + DELETE_PATH + KEY_SEPARATOR + KEY
        print(delete_request_url)

        delete_response = HttpMethod.send_delete_method(delete_request_url, json_post_body)
        print(delete_response.json())

        return delete_response


