import unittest
import logging
import allure
from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from logic.api.lists_api import APIList
from infra.jira_handler import JiraHandler

@allure.feature("List Management API")
class TestGetList(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.config = ConfigProvider.load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self.api_request = APIList(APIWrapper())
        self.jira_handler = JiraHandler()

    @allure.story("Get List by Board ID")
    def test_get_list(self):
        logging.info("Get List Test")

        # Act
        response = self.api_request.get_a_list()

        # Allure - attach response data
        allure.attach(str(response.data), name="Response Data",
                      attachment_type=allure.attachment_type.JSON)

        # Assert
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["id"], self.config["List"]["id"])