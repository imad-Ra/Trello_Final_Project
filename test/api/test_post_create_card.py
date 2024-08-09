import unittest
import logging
import allure
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.web.utils import Utils
from logic.api.cards_api import APICard
from infra.jira_handler import JiraHandler

@allure.feature("Card Management API")
class TestCreateCard(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.config = ConfigProvider.load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self.api_request = APICard(APIWrapper())
        self.jira_handler = JiraHandler()
        self.random_name = Utils.generate_random_lowercase_string(3, 5)

    @allure.story("Create New Card")
    def test_create_card(self):
        logging.info("Create Card Test")

        # Act
        response = self.api_request.post_create_a_card(self.random_name)

        # Allure - attach request and response data
        allure.attach(f"Card Name: {self.random_name}", name="Request Data",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(response.data), name="Response Data",
                      attachment_type=allure.attachment_type.JSON)

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], self.random_name)