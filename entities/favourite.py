from __future__ import annotations

import json
import logging

from config.config import URL_CATAPI
from helpers.rest_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)
ENTITY = "favourites"


class Favourite:
    def __init__(self, rest_client=None):
        self.url_cat_api_favourites = f"{URL_CATAPI}/{ENTITY}"
        self.rest_client = rest_client
        if rest_client is None:
            self.rest_client = RestClient()

    def create_favourite(self, image_id=None):
        body_favourite = {
            "image_id": image_id,
        }
        header_post = {
            "Content-Type": "application/json",
        }
        self.rest_client.session.headers.update(header_post)
        response = self.rest_client.request(
            "post",
            self.url_cat_api_favourites,
            data=json.dumps(body_favourite),
        )

        return response

    def delete_favourite(self, favourite_id):
        LOGGER.debug("[favourite class] deleting Favourite id %s", favourite_id)
        url_delete_favourite = f"{self.url_cat_api_favourites}/{favourite_id}"
        response = self.rest_client.request("delete", url_delete_favourite)
        if response["status_code"] == 204:
            LOGGER.info("Favourite Id deleted : %s", favourite_id)
