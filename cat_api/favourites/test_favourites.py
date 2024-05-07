"""Class providing favourites test """
from __future__ import annotations

import json
import logging

import pytest

from config.config import URL_CATAPI
from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestFavourites:
    """test favourites class"""

    @classmethod
    def setup_class(cls):
        """
        Setup class for favourite
        """
        cls.header_post = {
            "Content-Type": "application/json",
        }
        cls.rest_client = RestClient()
        cls.URL_CAT_API_IMAGES = f"{URL_CATAPI}/images/search?"
        response = cls.rest_client.request("get", cls.URL_CAT_API_IMAGES)
        cls.image_id = response["body"][0]["id"]
        LOGGER.debug("image ID: %s", cls.image_id)
        cls.favourite_list = []
        cls.URL_CAT_API_FAVOURITES = f"{URL_CATAPI}/favourites"
        cls.validate = ValidateResponse()

    @pytest.mark.acceptance
    def test_post_favourite(self, _log_test_names):
        """
        Test post favourite
        """
        LOGGER.info("Test post favourite")

        body_favourite = {
            "image_id": self.image_id,
        }
        rest_post_client = RestClient()
        rest_post_client.session.headers.update(self.header_post)
        response = rest_post_client.request(
            "post",
            self.URL_CAT_API_FAVOURITES,
            data=json.dumps(body_favourite),
        )

        if response["status_code"] == 200:
            self.favourite_list.append(response["body"]["id"])
        self.validate.validate_response(response, "favourites", "create_favourite")

    @pytest.mark.acceptance
    def test_delete_favourite(self, create_a_favourite, _log_test_names):
        """
            delete favourite
        :param create_a_favourite:
        :param log_test_names:
        :return:
        """

        url_delete_favourite = f"{self.URL_CAT_API_FAVOURITES}/{create_a_favourite}"
        response = self.rest_client.request("delete", url_delete_favourite)
        self.validate.validate_response(response, "favourites", "delete_favourite")

    @pytest.mark.acceptance
    def test_get_all_favourites(self):
        """
        Test get all favourites endpoint
        """
        response = self.rest_client.request("get", self.URL_CAT_API_FAVOURITES)
        self.validate.validate_response(response, "favourites", "get_all_favourites")

    @pytest.mark.acceptance
    def test_get_favourite(self, create_a_favourite, _log_test_names):
        """
        Test get favourite endpoint
        """
        LOGGER.info("Test get favourite")
        url_get_favourite = f"{self.URL_CAT_API_FAVOURITES}/{create_a_favourite}"
        response = self.rest_client.request("get", url_get_favourite)
        self.favourite_list.append(create_a_favourite)
        assert response["status_code"] == 200

    @pytest.mark.functional
    def test_image_id_is_required_create_favourite(self):
        """
        Test create favourite functional test
        """
        LOGGER.info("Test  Create an 'Down' Vote")
        body_favourite = {}

        rest_post_client = RestClient()
        rest_post_client.session.headers.update(self.header_post)
        response = rest_post_client.request(
            "post",
            self.URL_CAT_API_FAVOURITES,
            data=json.dumps(body_favourite),
        )
        self.validate.validate_response(response, "favourites", "image_id_is_required")

    @classmethod
    def teardown_class(cls):
        """
        PyTest teardown class
        """
        LOGGER.debug("=============Teardown class=============================")
        for favourite_id in cls.favourite_list:
            url_delete_favourite = f"{cls.URL_CAT_API_FAVOURITES}/{favourite_id}"
            LOGGER.debug("Delete favourite  %s", url_delete_favourite)
            response = cls.rest_client.request("delete", url_delete_favourite)
            if response["status_code"] == 200:
                LOGGER.info("favourite Id deleted : %s", favourite_id)
