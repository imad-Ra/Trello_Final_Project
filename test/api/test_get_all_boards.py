import unittest
import logging
import allure
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.boards_api import APIBoard
from infra.jira_handler import JiraHandler

@allure.feature("Board Management API")
class TestGetBoard(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.config = ConfigProvider.load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self.api_request = APIBoard(APIWrapper())
        self.jira_handler = JiraHandler()

    @allure.story("Get All Boards")
    def test_get_all_boards(self):
        logging.info("Get All Boards Test")

        # Act
        response = self.api_request.get_all_boards()

        # Allure - attach response data
        allure.attach(str(response.data), name="Response Data",
                      attachment_type=allure.attachment_type.JSON)

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["id"], self.config["Board"]["id"])
        self.assertEqual(response.data[0]["name"], self.config["Board"]["name"])
        self.assertEqual(response.data[1]["name"], self.config["Board"]["name2"])