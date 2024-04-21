"""Class providing rest client support"""
import json
import logging

import requests

from config.config import HEADERS_TODO
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class RestClient:
    """Class rest client methods."""
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS_TODO)

    def request(self, method_name, url,  **kwargs):
        """
            method to do a request call
        :param method_name:
        :param url:
        :return:

        response["status_code"]
        response["headers"]
        response["body"]
        """
        response_dict = {}
        try:
            response = self.select_method(method_name, self.session)(url=url,  **kwargs)
            LOGGER.debug("[Response] to request text: %s", response.text)
            LOGGER.debug("[Response] Status Code: %s", response.status_code)
            response.raise_for_status()
            if hasattr(response, "headers"):
                LOGGER.debug("[Response] Headers: %s", response.headers)
                response_dict["headers"] = response.headers

        except requests.exceptions.HTTPError as http_error:
            LOGGER.error("HTTP Error: %s", http_error)
            response_dict["headers"] = response.headers
        except requests.exceptions.RequestException as request_error:
            LOGGER.error("HTTP Error: %s", request_error)
        finally:
            if response.text:
                if response.ok:
                    response_dict["body"] = json.loads(response.text)
                else:
                    response_dict["body"] = {"msg": f"{response.text}"}
            else:
                response_dict["body"] = {"msg": "No body Content"}
        response_dict["status_code"] = response.status_code

        return response_dict

    @staticmethod
    def select_method(method_name, session):
        """
        Select REST method with session object
        :param method_name:
        :param session:
        :return:
        """
        methods = {
            "get": session.get,
            "post": session.post,
            "delete": session.delete,
            "put": session.put
        }
        return methods.get(method_name)
