import unittest
import logging

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.lists_api import APIList


class TestGetList(unittest.TestCase):

    def setUp(self):
        #Arrange
        self.config = ConfigProvider.load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self.api_request = APIList(APIWrapper())
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def test_get_list(self):
        """
        Tests the API endpoint for retrieving a list id (in board) --> by giving it board id
        """
        logging.info("Starting the 'Get Board' test")


        # Act
        response = self.api_request.get_a_list()

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["id"], self.config["List"]["id"])

        logging.info("Test ended successfully")

