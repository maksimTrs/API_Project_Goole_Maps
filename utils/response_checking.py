import json
import requests
from requests import Response


"""check response data"""

class ResponseChecking:

    @staticmethod
    def check_response_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f"Test passed!!! Status code = {response.status_code}")
        else:
            print(f"Test failed!!! Status code = {response.status_code}")

    @staticmethod
    def check_response_required_fields(response: Response, expected_field_name):
        # token = json.loads(response.text)
        json_response = response.json()
        assert list(json_response) == expected_field_name
        print(f"All method's data were presented: {list(json_response)}")

    @staticmethod
    def check_response_required_field_value(response: Response, field_name, expected_value):
        # token = json.loads(response.text)
        json_response = response.json()
        check_field_value = json_response.get(field_name)
        assert check_field_value == expected_value
        #dict_response = dict(json_response)
        # assert list(dict_response.values()) == expected_value
        # print(f"All method's data were presented: {list(dict_response.values())}")
        print(f"Method's field data was presented: {check_field_value}")
