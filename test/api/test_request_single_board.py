import unittest
import logging

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.boards_api import APIBoard


class TestGetBoard(unittest.TestCase):

    def setUp(self):
        #Arrange
        self.config = ConfigProvider.load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self.api_request = APIBoard(APIWrapper())
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def test_get_board(self):
        """
        Tests the API endpoint for retrieving a board
        """
        logging.info("Starting the 'Get Board' test")


        # Act
        response = self.api_request.get_a_board()

        # Log response details
        logging.info(f"Response data: {response.data}")

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], self.config["API"]["id"])

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()