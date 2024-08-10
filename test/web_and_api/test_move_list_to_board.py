import unittest
import logging
import allure
import time
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.web.first_page import FirstPage
from logic.web.login_page import LoginPage
from logic.web.board_page import BoardPage
from logic.api.lists_api import APIList
from infra.api.api_wrapper import APIWrapper
from infra.jira_handler import JiraHandler

@allure.feature("List Management")
class TestMoveList(unittest.TestCase):
    """
    Test case to move a list between existing boards using API and verify the change via UI.
    """

    def setUp(self):
        # Arrange
        self.config = ConfigProvider.load_from_file()
        self.secret = ConfigProvider.load_from_secret()  # Added for Jira
        self.jira_handler = JiraHandler()
        self.api_wrapper = APIWrapper()
        self.api_list = APIList(self.api_wrapper)

        # Load test data from config
        self.list_to_move_id = self.config["List"]["id"]
        self.list_to_move_name = self.config["List"]["name"]
        self.original_board_id = self.config["Board"]["id"]
        self.target_board_id = self.config["Board"]["id2"]

        # Set up WebDriver and login
        self.driver = BrowserWrapper().get_driver(self.config['url'])
        FirstPage(self.driver).click_login_button()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])

        # Wait after login
        time.sleep(5)

    def tearDown(self):
        # Clean up: move list back and close browser
        self.api_list.move_list(self.list_to_move_id, self.original_board_id)
        self.driver.quit()

    @allure.story("Move List to Another Board and Verify via UI")
    def test_move_list(self):
        """
        This test verifies moving a list between boards using API and checks the change via UI.
        It moves a list to a target board and verifies its presence through the user interface.
        The purpose is to ensure the list movement functionality works correctly across API and UI.
        """
        logging.info("Test Start: Move List to Another Board and Verify via UI")

        try:
            # Act (API): Move list using API
            response = self.api_list.move_list(self.list_to_move_id, self.target_board_id)

            # Act (UI): Navigate to target board immediately after API call
            self.driver.get(f"{self.config['url']}/b/{self.target_board_id}")
            board_page = BoardPage(self.driver)

            # Assert (API response)
            self.assertTrue(response.ok)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['idBoard'], self.target_board_id)

            # Assert (UI verification)
            self.assertTrue(board_page.wait_for_list_and_verify(self.list_to_move_name))

            # Attach screenshot to Allure report
            allure.attach(self.driver.get_screenshot_as_png(), name="Board After List Move",
                          attachment_type=allure.attachment_type.PNG)

        except AssertionError as e:
            self.jira_handler.create_issue(
                self.secret["jira_project_key"],
                "List Movement Test Failed",
                str(e),
                "Bug"
            )
            allure.attach(self.driver.get_screenshot_as_png(), name="Failure Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise