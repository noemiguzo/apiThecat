import logging

import pytest

from config.config import URL_CATAPI
from entities.favourite import Favourite

from entities.image import Image
from entities.vote import Vote
from helpers.rest_client import RestClient
from utils.logger import get_logger
import json

LOGGER = get_logger(__name__, logging.DEBUG)


@pytest.fixture()
def create_image():
    image_id = None

    LOGGER.info("Fixture UPLOAD images")
    image = Image()
    response = image.create_image()

    if response["status_code"] == 201:
        image_id = response["body"]["id"]

    return image_id


@pytest.fixture()
def get_image_id_to_vote():
    image = Image()
    return image.get_first_image_id()


@pytest.fixture()
def post_a_vote(get_image_id_to_vote):
    vote_id = None

    vote = Vote()
    response = vote.create_vote(get_image_id_to_vote)
    if response["status_code"] == 201:
        vote_id = response["body"]["id"]

    yield vote_id

    LOGGER.debug("Yield fixture delete vote")
    vote.delete_vote(vote_id)


def delete_vote(vote_id):
    vote = Vote()
    vote.delete_vote(vote_id)


@pytest.fixture()
def log_test_names(request):
    repeated = "=" * 10
    LOGGER.info("%s TEST %s STARTED", repeated, request.node.name)

    def fin():
        LOGGER.info("%s TEST %s COMPLETED", repeated, request.node.name)

    request.addfinalizer(fin)


@pytest.fixture()
def create_a_vote(get_image_id_to_vote):
    vote_id = None
    LOGGER.info("%s CREATE  VOTE",get_image_id_to_vote)
    vote = Vote()
    response = vote.create_vote(get_image_id_to_vote)
    if response["status_code"] == 201:
        vote_id = response["body"]["id"]
    return vote_id


@pytest.fixture()
def create_a_favourite(get_image_id_to_vote):
    favourite_id = None

    favourite = Favourite()
    response = favourite.create_favourite(get_image_id_to_vote)
    if response["status_code"] == 200:
        favourite_id = response["body"]["id"]
    return favourite_id
