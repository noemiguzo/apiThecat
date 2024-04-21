"""Class providing vote API test """
import json
import logging
import pytest

from entities.image import Image
from utils.logger import get_logger


from config.config import URL_CATAPI
from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse
LOGGER = get_logger(__name__, logging.DEBUG)



class TestVotes:
    """ test vote class"""
    @classmethod
    def setup_class(cls):
        """
        Setup class search for images to run vote suite
        """
        cls.header_post = {
            "Content-Type": "application/json"
        }

        cls.rest_client = RestClient()
        image = Image()
        cls.image_id = image.get_first_image_id()
        LOGGER.debug("image ID: %s", cls.image_id)

        cls.vote_list = []
        cls.URL_CAT_API_VOTES = f"{URL_CATAPI}/votes"
        cls.validate = ValidateResponse()
        cls.rest_post_client = RestClient()
        cls.rest_post_client.session.headers.update(cls.header_post)

    def test_post_a_vote(self, _log_test_names):
        """
        Test create vote
        """
        LOGGER.info("Test Create an 'Up' Vote")
        body_vote = {
            "image_id": self.image_id,
            "value": 1
        }


        response = self.rest_post_client.request("post", self.URL_CAT_API_VOTES, data=json.dumps(body_vote))
        if response["status_code"] == 201:
            self.vote_list.append(response["body"]["id"])
        self.validate.validate_response(response, "votes", "post_a_vote")



    def test_post_a_down_vote(self, _log_test_names):
        """
        Test create DOWN vote
        """
        LOGGER.info("Test  Create an 'Down' Vote")
        body_vote = {
            "image_id": self.image_id,
            "value": -1
        }


        response = self.rest_post_client.request("post", self.URL_CAT_API_VOTES, data=json.dumps(body_vote))
        if response["status_code"] == 201:
            self.vote_list.append(response["body"]["id"])

        assert response["status_code"] == 201

    def test_get_all_vote(self, post_a_vote, _log_test_names):
        """
        Test get all votes endpoint
        """
        LOGGER.info("Test get all votes %s",post_a_vote)
        response = self.rest_client.request("get", self.URL_CAT_API_VOTES)

        self.validate.validate_response(response, "votes", "get_all_votes")

    def test_get_vote(self, create_a_vote, _log_test_names):
        """
        Test get vote
        """

        url_get_vote = f"{self.URL_CAT_API_VOTES}/{create_a_vote}"
        LOGGER.info("Test get 83 vote %s", url_get_vote)
        response = self.rest_client.request("get", url_get_vote)
        self.vote_list.append(create_a_vote)
        assert response["status_code"] == 200

    def test_delete_vote(self, create_a_vote, _log_test_names):
        """
            delete vote
        :param create_a_vote:
        :param log_test_names:
        :return:
        """

        url_delete_vote = f"{self.URL_CAT_API_VOTES}/{create_a_vote}"

        LOGGER.info(url_delete_vote)
        response = self.rest_client.request("delete", url_delete_vote)

        self.validate.validate_response(response, "votes", "delete_vote")

    @pytest.mark.functional
    def test_image_id_is_required_to_create_vote(self):
        """
        Test create vote functional test
        """
        LOGGER.info("Test  Create an 'Down' Vote")
        body_vote = {
            "value": -1
        }


        response = self.rest_post_client.request("post", self.URL_CAT_API_VOTES, data=json.dumps(body_vote))
        self.validate.validate_response(response, "votes", "image_id_is_required")

    @pytest.mark.functional
    def test_value_is_required_create_vote(self):
        """
        Test create vote functional test
        """
        LOGGER.info("Test  Create an 'Down' Vote")
        body_vote = {
            "image_id": "F8lwUshaY",
        }


        response = self.rest_post_client.request("post", self.URL_CAT_API_VOTES, data=json.dumps(body_vote))
        self.validate.validate_response(response, "votes", "value_is_required")

    @classmethod
    def teardown_class(cls):
        """
        PyTest teardown class
        """
        LOGGER.debug("Teardown - Cleanup votes")

        for vote_id in cls.vote_list:
            url_delete_vote = f"{cls.URL_CAT_API_VOTES}/{vote_id}"
            LOGGER.debug(url_delete_vote)
            cls.rest_client.request("delete", url_delete_vote)
