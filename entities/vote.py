import json
import logging

from config.config import URL_CATAPI
from helpers.rest_client import RestClient
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)
ENTITY = 'votes'

class Vote:

    def __init__(self, rest_client=None):
        self.url_cat_api_votes = f"{URL_CATAPI}/{ENTITY}"
        self.rest_client = rest_client
        if rest_client is None:
            self.rest_client = RestClient()

    def create_vote(self, image_id=None):
        LOGGER.debug("[vote class] Vote with  %s", image_id)
        body_vote = {
            "image_id": image_id,
            "sub_id": "fixture-1",
            "value": 1
        }
        header_post = {
            "Content-Type": "application/json"
        }

        self.rest_client.session.headers.update(header_post)
        response = self.rest_client.request("post", self.url_cat_api_votes, data=json.dumps(body_vote))

        return response

    def delete_vote(self, vote_id):
        LOGGER.debug("[vote class] deleting Vote id %s", vote_id)
        url_delete_vote = f"{self.url_cat_api_votes}/{vote_id}"
        response = self.rest_client.request("delete", url_delete_vote)

        if response["status_code"] == 204:
            LOGGER.info("Vote Id deleted : %s", vote_id)
