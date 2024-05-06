"""
(c) Copyright Jalasoft 2024

environment.py
    file contains all environment functions/fixtures to be used by features
"""
import logging

from config.config import URL_CATAPI
from entities.image import Image
from entities.vote import Vote
from entities.favourite import  Favourite
from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)





def before_all(context):
    """
    Fixture to initialize variables and objects
    :param context:
    """
    LOGGER.info("==========================  Before All ==========================")
    context.rest_client = RestClient()
    context.url_cat_images = f"{URL_CATAPI}/images"
    context.url_cat_votes = f"{URL_CATAPI}/votes"
    context.url_cat_favourites = f"{URL_CATAPI}/favourites"

    context.resource_list = {
        "images": [],
        "votes": [],
        "favourites": []
    }
    context.validate = ValidateResponse()
    context.image = Image()
    context.vote = Vote()
    context.favourite = Favourite()


def before_scenario(context, scenario):
    """

    :param context:
    :param scenario:
    """
    context.resource_list = {
        "votes": [],
        "favourites": [],
        "images": []
    }
    LOGGER.info("Before Scenario::::")
    LOGGER.info("Test '%s' STARTED", scenario.name)
    LOGGER.info("Tags '%s' ", scenario.tags)
    if "_id" in ''.join(scenario.tags):
        new_image = context.image.create_image()
        context.image_id = new_image["body"]["id"]
        context.resource_list["images"].append(context.image_id)
        LOGGER.warning(context.resource_list)

    if "vote_id" in scenario.tags:

        new_vote = context.vote.create_vote(image_id=context.image_id)[0]
        context.vote_id = new_vote["body"]["id"]
        context.resource_list["votes"].append(context.vote_id)
        LOGGER.warning(context.resource_list)

    if "favourite_id" in scenario.tags:

        new_image = context.favourite.create_favourite(context.image_id)
        context.favourite_id = new_image["body"]["id"]
        context.resource_list["favourites"].append(context.favourite_id)

    LOGGER.info(context.resource_list)

def after_scenario(context, scenario):
    """

    :param context:
    :param scenario:
    """
    LOGGER.warning("After scenario: %s::::", scenario.name)

    for resource in context.resource_list:
        LOGGER.warning("After resource: %s", resource)
        LOGGER.warning("After resource list: %s", context.resource_list[resource])
        for resource_id in context.resource_list[resource]:
            url_delete = f"{URL_CATAPI}/{resource}/{resource_id}"
            LOGGER.warning("Delete entity URL %s ", url_delete)
            LOGGER.warning("%s Id to be deleted : %s", resource, resource_id)
            response = context.rest_client.request("delete", url_delete)
            if response["status_code"] == 204:
                LOGGER.info("%s Id deleted : %s", resource, resource_id)

