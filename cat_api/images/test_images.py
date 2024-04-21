"""Class providing image API test """
import logging
import pytest

from entities.image import Image
from utils.logger import get_logger

from config.config import URL_CATAPI, IMAGE_FOLDER
from helpers.rest_client import RestClient
from helpers.validate_response import ValidateResponse

LOGGER = get_logger(__name__, logging.DEBUG)


class TestImages:
    """ test image class"""
    @classmethod
    def setup_class(cls):
        """
        Setup class for images
        """
        cls.rest_client = RestClient()
        cls.URL_CAT_API_IMAGES = f"{URL_CATAPI}/images/"

        image = Image()
        cls.image_id = image.get_first_image_id()
        cls.validate = ValidateResponse()
        cls.image_list = []

    @pytest.mark.acceptance
    def test_upload_image(self):
        """
        Test upload image open png file
        """
        LOGGER.info("Test upload images")
        upload_url = f"{self.URL_CAT_API_IMAGES}upload"
        print('url', upload_url)
        with open(f'{IMAGE_FOLDER}cat1noemi.png', "rb") as image_file:
            test_file = {'file': ('testnamenew', image_file.read(), 'image/png')}
       # test_file = {'file': ('testnamenew', open(f'{IMAGE_FOLDER}cat1noemi.png', "rb"), 'image/png')}
        response = self.rest_client.request("post", upload_url, files=test_file)
        LOGGER.info(response)
        if response["status_code"] == 201:
            self.image_id = response["body"]["id"]
            self.image_list.append(self.image_id)

        self.validate.validate_response(response, "images", "upload_image")

    @pytest.mark.acceptance
    def test_get_all_images(self):
        """
        Test get all images endpoint
        """
        LOGGER.info("Test get all images")

        response = self.rest_client.request("get", self.URL_CAT_API_IMAGES)
        self.validate.validate_response(response, "images", "get_all_images")


    @pytest.mark.acceptance
    def test_get_image(self):
        """
        Test get image endpoint
        """
        LOGGER.info("Test get image")


        url_get_image = f"{self.URL_CAT_API_IMAGES}{self.image_id}"
        response = self.rest_client.request("get", url_get_image)
        self.validate.validate_response(response, "images", "get_image")

    @pytest.mark.acceptance
    def test_delete_image(self, create_image):
        """
        delete image
        :param create_image:
        :return:
        """

        url_delete_image = f"{self.URL_CAT_API_IMAGES}{create_image}"

        LOGGER.info(url_delete_image)
        response = self.rest_client.request("delete", url_delete_image)
        self.validate.validate_response(response, "images", "delete_image")

    @classmethod
    def teardown_class(cls):
        """
        PyTest teardown class
        """
        LOGGER.debug("Teardown Cleanup images data %s", cls.image_list)
        for image_id in cls.image_list:
            url_delete_image = f"{cls.URL_CAT_API_IMAGES}{image_id}"

            response = cls.rest_client.request("delete", url_delete_image)
            if response["status_code"] == 204:
                LOGGER.info("Image Id deleted : %s", image_id)
