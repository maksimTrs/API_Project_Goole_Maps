import json
import allure
import requests
from requests import Response
from utils.api_methods import GoogleMapsApi
from utils.response_checking import ResponseChecking

"""create change delete Google Maps locations"""

@allure.epic("Test create google map new place")
class TestCreateLocation:

    @allure.description("Test create, update, delete locationallu")
    def test_create_location(self):
        print(">>> Method POST <<<")
        post_response: Response = GoogleMapsApi.create_new_google_maps_place()
        place_id = post_response.json().get("place_id")
        ResponseChecking.check_response_status_code(post_response, 200)
        ResponseChecking.check_response_required_fields(post_response, ['status', 'place_id', 'scope', 'reference', 'id'])

        print(">>> Method GET POST <<<")
        get_response: Response = GoogleMapsApi.get_google_maps_place(place_id)
        ResponseChecking.check_response_status_code(get_response, 200)
        ResponseChecking.check_response_required_fields(get_response, ['location', 'accuracy', 'name', 'phone_number',
                                                                       'address', 'types', 'website', 'language'])
        ResponseChecking.check_response_required_field_value(get_response, 'address', "29, side layout, cohen 09")

        print(">>> Method PUT <<<")
        put_response: Response = GoogleMapsApi.update_google_maps_place(place_id)
        ResponseChecking.check_response_status_code(put_response, 200)
        ResponseChecking.check_response_required_fields(put_response, ["msg"])
        ResponseChecking.check_response_required_field_value(put_response, 'msg', "Address successfully updated")

        print(">>> Method GET PUT <<<")
        # get_response: Response = GoogleMapsApi.get_google_maps_place(place_id)
        get_response = GoogleMapsApi.get_google_maps_place(place_id)
        ResponseChecking.check_response_required_field_value(get_response, 'address', "100 Lenina street, RU")


        print(">>> Method DELETE <<<")
        delete_response: Response = GoogleMapsApi.delete_google_maps_place(place_id)
        ResponseChecking.check_response_status_code(delete_response, 200)
        ResponseChecking.check_response_required_field_value(delete_response, 'status', "OK")


        print(">>> Method GET DELETE <<<")
        get_response: Response = GoogleMapsApi.get_google_maps_place(place_id)
        ResponseChecking.check_response_status_code(get_response, 404)


        print(f"\nTest {self.test_create_location.__qualname__} passed!!!\n")


