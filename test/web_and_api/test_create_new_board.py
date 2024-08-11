import unittest
from selenium.webdriver.support import expected_conditions as EC


import allure
from selenium.webdriver.support.wait import WebDriverWait

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.api.api_wrapper import APIWrapper
from logic.api.boards_api import APIBoard
from logic.web.board_page import BoardPage
from logic.web.first_page import FirstPage
from logic.web.home_page import HomePage
from logic.web.login_page import LoginPage
from infra.web.utils import Utils
from infra.jira_handler import JiraHandler

@allure.feature("Board Management")
class NewBoardTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self.driver = self.browser.get_driver(self.config['url'])
        FirstPage(self.driver).click_login_button()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])
        self.home_page = HomePage(self.driver)
        self.api_board = APIBoard(APIWrapper())
        self.random_name = Utils.generate_random_lowercase_string(3,5)
        self.jira_handler = JiraHandler()
        self.fail = False  # Initialize fail flag

    def tearDown(self):
        if self.fail:
            self.jira_handler.create_issue(
                self.secret["jira_project_key"],
                "Board Creation Test Failed",
                "I found a bug in the create new board test",
                "Bug"

            )
            allure.attach(self.driver.get_screenshot_as_png(), name="Failure Screenshot",
                          attachment_type=allure.attachment_type.PNG)

        self.driver.quit()
        self.api_board.delete_board_by_name(self.random_name)

    @allure.story("Create New Board")
    def test_create_board(self):
        """
        This test verifies the creation of a new board via the UI and does teardown via API.
        """
        # Act
        self.home_page.click_create_board_button()
        self.home_page.fill_board_title_input(self.random_name)
        self.home_page.click_create_button()

        # Wait for the board to load
        board_page = BoardPage(self.driver)
        board_loaded = board_page.wait_for_board_to_load(self.random_name)

        # Assert
        try:
            self.assertTrue(board_loaded, "Board did not load successfully")
            self.assertIn(self.random_name, self.driver.current_url, "Board name not found in URL")
        except AssertionError as e:
            self.fail = True
            raise