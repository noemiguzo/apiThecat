"""Module providing fixture methods."""
import logging
import pytest

from entities.favourite import Favourite
from entities.image import Image
from entities.vote import Vote

from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


@pytest.fixture(name="create_image")
def create_image_fixture():
    """
    create a image
    :return:
    """
    image_id = None

    LOGGER.info("Fixture UPLOAD images")
    image = Image()
    response = image.create_image()

    if response["status_code"] == 201:
        image_id = response["body"]["id"]

    return image_id


@pytest.fixture(name="get_image_id_to_vote")
def get_image_id_to_vote_fixture():
    """
    Get a image id
    :return:
    """
    image = Image()
    return image.get_first_image_id()


@pytest.fixture(name="post_a_vote")
def post_a_vote_fixture(get_image_id_to_vote):
    """
    Create a vote
    :param get_image_id_to_vote:
    :return:
    """
    vote_id = None

    vote = Vote()
    response = vote.create_vote(get_image_id_to_vote)
    if response["status_code"] == 201:
        vote_id = response["body"]["id"]

    yield vote_id

    LOGGER.debug("Yield fixture delete vote")
    vote.delete_vote(vote_id)


def delete_vote(vote_id):
    """
    delete vote by id
    :param vote_id:
    :return:
    """
    vote = Vote()
    vote.delete_vote(vote_id)


@pytest.fixture(name="_log_test_names")
def log_test_names(request):
    """
    print name function
    :param request:
    :return:
    """
    repeated = "=" * 10
    LOGGER.info("%s TEST %s STARTED", repeated, request.node.name)

    def fin():
        LOGGER.info("%s TEST %s COMPLETED", repeated, request.node.name)

    request.addfinalizer(fin)


@pytest.fixture(name="create_a_vote")
def create_a_vote_fixture(get_image_id_to_vote):
    """
    create a vote
    :param get_image_id_to_vote:
    :return:
    """
    vote_id = None
    LOGGER.info("%s CREATE  VOTE", get_image_id_to_vote)
    vote = Vote()
    response = vote.create_vote(get_image_id_to_vote)
    if response["status_code"] == 201:
        vote_id = response["body"]["id"]
    return vote_id


@pytest.fixture(name="create_a_favourite")
def create_a_favourite_fixture(get_image_id_to_vote):
    """
    create a favourite
    :param get_image_id_to_vote:
    :return:
    """
    favourite_id = None

    favourite = Favourite()
    response = favourite.create_favourite(get_image_id_to_vote)
    if response["status_code"] == 200:
        favourite_id = response["body"]["id"]
    return favourite_id
