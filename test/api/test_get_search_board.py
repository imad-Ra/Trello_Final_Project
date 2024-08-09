import unittest
import logging
import allure
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.boards_api import APIBoard
from infra.jira_handler import JiraHandler

@allure.feature("Board Management API")
class TestGetSearchBoard(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.config = ConfigProvider.load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self.api_request = APIBoard(APIWrapper())
        self.jira_handler = JiraHandler()

    @allure.story("Search Board by Name")
    def test_get_board(self):
        logging.info("Search Board Test")

        # Act
        response = self.api_request.get_search_board(self.config["Board"]["name"])

        # Allure - attach response data
        allure.attach(str(response.data), name="Response Data",
                      attachment_type=allure.attachment_type.JSON)

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["boards"][1]["id"], self.config["Board"]["id"])