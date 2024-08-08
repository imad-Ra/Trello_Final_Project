import unittest
import logging

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.web.utils import Utils
from logic.api.cards_api import APICard


class TestCreateCard(unittest.TestCase):

    def setUp(self):
        #Arrange
        self.config = ConfigProvider.load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self.api_request = APICard(APIWrapper())
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        self.random_name = Utils.generate_random_lowercase_string(3,5)

    def test_create_card(self):
        """
        Tests the API endpoint for creating a card
        """
        logging.info("Starting the 'Create Card' test")

        # Act
        response = self.api_request.post_create_a_card(self.random_name)


        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], self.random_name)



if __name__ == '__main__':
    unittest.main()