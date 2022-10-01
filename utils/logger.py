import datetime
import os

from requests import Response


class Logger():
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def write_logs_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request_to_file(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        add_data_to_file = f'\n--------------------\n'
        add_data_to_file += f'Test: {test_name}\n'
        add_data_to_file += f'Time: {str(datetime.datetime.now())}\n'
        add_data_to_file += f'Request Method: {method}\n'
        add_data_to_file += f'Request URL: {url}\n'
        add_data_to_file += '\n'

        cls.write_logs_to_file(add_data_to_file)

    @classmethod
    def add_response_to_file(cls, result: Response):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        add_data_to_file = f'Response code: {result.status_code}\n'
        add_data_to_file += f'Response text: {result.text}\n'
        add_data_to_file += f'Response headers: {headers_as_dict}\n'
        add_data_to_file += f'Response cookies: {cookies_as_dict}\n'
        add_data_to_file += f'\n--------------------\n'

        cls.write_logs_to_file(add_data_to_file)

