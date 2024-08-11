import unittest
import logging
import allure
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.web.first_page import FirstPage
from logic.web.login_page import LoginPage
from logic.web.board_page import BoardPage
from logic.api.lists_api import APIList
from infra.api.api_wrapper import APIWrapper
from infra.jira_handler import JiraHandler
from logic.web.data_manager import DataManager

@allure.feature("List Management")
class TestMoveList(unittest.TestCase):
    """
    Test case to move a list between existing boards using API and verify the change via UI.
    """

    def setUp(self):
        # Arrange
        self.config = ConfigProvider.load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self.jira_handler = JiraHandler()
        self.api_wrapper = APIWrapper()
        self.api_list = APIList(self.api_wrapper)

        # Use TestDataManager to load test data
        self.test_data = DataManager().get_move_list_test_data()

        # Set up WebDriver and login
        self.driver = BrowserWrapper().get_driver(self.config['url'])
        FirstPage(self.driver).click_login_button()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])

        self.fail = False  # Initialize fail flag

    def tearDown(self):
        if self.fail:
            self.jira_handler.create_issue(
                self.secret["jira_project_key"],
                "List Movement Test Failed",
                "I found a bug in the move list test",
                "Bug"

            )
            allure.attach(self.driver.get_screenshot_as_png(), name="Failure Screenshot",
                          attachment_type=allure.attachment_type.PNG)

        # Clean up: move list back and close browser
        self.api_list.move_list(self.test_data["list_to_move_id"], self.test_data["original_board_id"])
        self.driver.quit()

    @allure.story("Move List to Another Board and Verify via UI")
    def test_move_list(self):
        """
        This test verifies moving a list between boards using API and checks the change via UI.
        """
        logging.info("Test Start: Move List to Another Board and Verify via UI")

        try:
            # Act (API): Move list using API
            response = self.api_list.move_list(self.test_data["list_to_move_id"], self.test_data["target_board_id"])

            # Act (UI): Navigate to target board immediately after API call
            board_page = BoardPage(self.driver)
            board_page.navigate_to_board(self.test_data["target_board_id"])

            # Assert (UI verification)
            self.assertTrue(board_page.wait_for_list_and_verify(self.test_data["list_to_move_name"]),
                            "List was not found on the target board after moving")



        except AssertionError as e:
            self.fail = True
            raise

if __name__ == '__main__':
    unittest.main()