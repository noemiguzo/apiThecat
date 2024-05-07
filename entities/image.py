from __future__ import annotations

import logging

from config.config import IMAGE_FOLDER
from config.config import URL_CATAPI
from helpers.rest_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)
ENTITY = "images"


class Image:
    def __init__(self, rest_client=None):
        self.url_cat_api_images = f"{URL_CATAPI}/{ENTITY}"
        self.rest_client = rest_client
        if rest_client is None:
            self.rest_client = RestClient()

    def create_image(self):
        URL_CAT_API_UPLOAD = f"{self.url_cat_api_images}/upload"

        media_file = {
            "file": (
                "namenewcat1",
                open(f"{IMAGE_FOLDER}cat1noemi.png", "rb"),
                "image/png",
            ),
        }

        response = self.rest_client.request(
            "post",
            URL_CAT_API_UPLOAD,
            files=media_file,
        )

        return response

    def delete_image(self, image_id):
        LOGGER.debug("[image class] deleting Image id %s", image_id)
        url_delete_image = f"{self.url_cat_api_images}/{image_id}"
        response = self.rest_client.request("delete", url_delete_image)
        if response["status_code"] == 204:
            LOGGER.info("Image Id deleted : %s", image_id)

    def get_first_image_id(self):
        response = self.rest_client.request("get", self.url_cat_api_images)
        image_id = response["body"][0]["id"]
        LOGGER.debug("[image class] Getting Image id %s", image_id)
        return image_id
