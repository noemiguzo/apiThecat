from __future__ import annotations

import json
import logging

from config.config import abs_path
from config.config import URL_CATAPI
from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)
ENTITY = "votes"


class Vote:
    def __init__(self, rest_client=None, sub_id=None, value=1):
        self.url_cat_api_votes = f"{URL_CATAPI}/{ENTITY}"
        self.rest_client = rest_client
        self.sub_id = sub_id
        self.value = value
        if rest_client is None:
            self.rest_client = RestClient()
        self.validate = ValidateResponse()

    def create_vote(self, file=False, image_id=None, number_tasks=0):
        LOGGER.debug("[vote class] Vote with  %s", image_id)
        response_list = []
        body_vote = {
            "image_id": image_id,
            "sub_id": self.sub_id or "fixture-1",
            "value": self.value or 1,
        }
        header_post = {
            "Content-Type": "application/json",
        }
        if self.rest_client is None:
            self.rest_client = RestClient()
        self.rest_client.session.headers.update(header_post)
        if file:
            vote_json = f"{abs_path}/apiThecat/input_data/votes/votes.json"
            data_vote = self.validate.read_input_data_json(vote_json)
            number_votes = 5

            for index in range(0, number_votes):
                body_vote = data_vote[index]
                body_vote["image_id"] = image_id
                LOGGER.debug("[vote class] -----by - file-------  body_vote %s", body_vote)
                response = self.rest_client.request(
                    "post",
                    self.url_cat_api_votes,
                    data=json.dumps(body_vote),
                )
                response_list.append(response)
        else:
            LOGGER.debug("[vote class] -------  body_vote %s", body_vote)
            response = self.rest_client.request(
                "post",
                self.url_cat_api_votes,
                data=json.dumps(body_vote),
            )
        response_list.append(response)
        return response_list

    def delete_vote(self, vote_id):
        LOGGER.debug("[vote class] deleting Vote id %s", vote_id)
        url_delete_vote = f"{self.url_cat_api_votes}/{vote_id}"
        response = self.rest_client.request("delete", url_delete_vote)

        if response["status_code"] == 204:
            LOGGER.info("Vote Id deleted : %s", vote_id)
