import unittest
import logging

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.boards_api import APIBoard


class TestGetAllBoards(unittest.TestCase):

    def setUp(self):
        #Arrange
        self.config = ConfigProvider.load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self.api_request = APIBoard(APIWrapper())
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def test_get_all_boards(self):
        """
        Tests the API endpoint for retrieving all boards
        """
        logging.info("Starting the 'Get All Boards' test")

        # Act
        response = self.api_request.get_all_boards()

        # Log response details
        logging.info(f"Response data: {response.data}")

        # Assert
        self.assertEqual(response.data[2]["id"], self.config["Board"]["id"])
        self.assertEqual(response.data[2]["name"], self.config["Board"]["name"])
        self.assertEqual(response.data[3]["name"], self.config["Board"]["name2"])

        logging.info("Test ended successfully")

if __name__ == '__main__':
    unittest.main()