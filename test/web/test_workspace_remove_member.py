import logging
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.web.board_page import BoardPage
from logic.web.first_page import FirstPage
from logic.web.login_page import LoginPage
from logic.web.members_page import MembersPage


class MembersPageTest(unittest.TestCase):

    def setUp(self):
        # Initialize the browser and load configuration
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()

        # Start the browser session and navigate to the specified URL
        self.driver = self.browser.get_driver(self.config['url'])

        # Perform login
        FirstPage(self.driver).login_button_click()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])

        # navigate to the Members page
        BoardPage(self.driver).workspace_option_select(3)
        self.members_page = MembersPage(self.driver)

    def tearDown(self):
        # If there are more than 1 member, remove the extra member
        if len(self.members_page.get_members()) != 1:
            self.members_page.workspace_remove_member_flow()

        # Quit the WebDriver session after test execution
        self.driver.quit()

    def test_workspace_remove_member(self):
        # Test case for removing a member from the workspace
        logging.info("Remove Member From Workspace Test")
        self.members_page.workspace_add_member_flow(self.config['member_email'])
        self.members_page.remove_member_button_click()
        self.members_page.confirm_remove_button_click()

        # Wait until the number of members is 1 and Assert that there is only 1 member left
        WebDriverWait(self.driver, 15).until(lambda driver: len(self.members_page.get_members()) == 1)
        self.assertEqual(len(self.members_page.get_members()), 1)
