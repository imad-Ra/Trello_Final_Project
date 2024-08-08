import unittest
import logging

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.web.utils import Utils
from logic.api.boards_api import APIBoard


class TestCreateBoard(unittest.TestCase):


    def setUp(self):
        #Arrange
        self.config = ConfigProvider.load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self.api_request = APIBoard(APIWrapper())
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        self.random_name = Utils.generate_random_lowercase_string(3,5)

    def tearDown(self):
        self.api_request.delete_board_by_name(self.random_name)

    def test_create_board(self):
        """
        Tests the API endpoint for creating a board
        """
        logging.info("Starting the 'Create Board' test")

        # Prepare parameters
        params = {
            "name": self.random_name,
        }

        # Act
        response = self.api_request.post_create_a_board(params)


        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], self.random_name)

