import unittest
import logging
import allure
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.web.utils import Utils
from logic.api.boards_api import APIBoard
from infra.jira_handler import JiraHandler

@allure.feature("Board Management API")
class TestCreateBoard(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.config = ConfigProvider.load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self.api_request = APIBoard(APIWrapper())
        self.jira_handler = JiraHandler()
        self.random_name = Utils.generate_random_lowercase_string(3, 5)

    def tearDown(self):
        self.api_request.delete_board_by_name(self.random_name)

    @allure.story("Create New Board")
    def test_create_board(self):
        logging.info("Create Board Test")

        # Act
        params = {
            "name": self.random_name,
        }
        response = self.api_request.post_create_a_board(params)

        # Allure - attach request and response data
        allure.attach(f"Board Name: {self.random_name}", name="Request Data",
                      attachment_type=allure.attachment_type.JSON)
        allure.attach(str(response.data), name="Response Data",
                      attachment_type=allure.attachment_type.JSON)

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], self.random_name)