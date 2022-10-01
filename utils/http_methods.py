import allure
import requests

from utils.logger import Logger

"""HTTP Methods List"""


class HttpMethod:
    headers = {'Content-Type': 'application/json'}
    cookies = ""

    @staticmethod
    def send_get_method(url):
        with allure.step("Get location method"):
            Logger.add_request_to_file(url, method="GET")
            get_result = requests.get(url, headers=HttpMethod.headers, cookies=HttpMethod.cookies)
            Logger.add_response_to_file(get_result)
            return get_result

    @staticmethod
    def send_post_method(url, body):
        with allure.step("Post location method"):
            Logger.add_request_to_file(url, method="POST")
            post_result = requests.post(url, headers=HttpMethod.headers, cookies=HttpMethod.cookies, json=body)
            Logger.add_response_to_file(post_result)
            return post_result

    @staticmethod
    def send_put_method(url, body):
        with allure.step("Put location method"):
            Logger.add_request_to_file(url, method="PUT")
            put_result = requests.put(url, headers=HttpMethod.headers, cookies=HttpMethod.cookies, json=body)
            Logger.add_response_to_file(put_result)
            return put_result

    @staticmethod
    def send_delete_method(url, body):
        with allure.step("Delete location method"):
            Logger.add_request_to_file(url, method="DELETE")
            delete_result = requests.delete(url, headers=HttpMethod.headers, cookies=HttpMethod.cookies, json=body)
            Logger.add_response_to_file(delete_result)
            return delete_result
