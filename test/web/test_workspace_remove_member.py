import logging
import unittest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.web.board_page import BoardPage
from logic.web.first_page import FirstPage
from logic.web.login_page import LoginPage
from logic.web.members_page import MembersPage
from infra.jira_handler import JiraHandler

@allure.feature("Workspace Management")
class RemoveWorkspaceMembersTest(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.jira_handler = JiraHandler()

        self.driver = self.browser.get_driver(self.config['url'])

        FirstPage(self.driver).click_login_button()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])

        BoardPage(self.driver).workspace_option_select(3)
        self.members_page = MembersPage(self.driver)

    def tearDown(self):
        if len(self.members_page.get_members()) != 1:
            self.members_page.workspace_remove_member_flow()
        self.driver.quit()

    @allure.story("Remove Member from Workspace")
    def test_workspace_remove_member(self):
        logging.info("Remove Member From Workspace Test")

        # Act
        self.members_page.workspace_add_member_flow(self.config['member_email'])
        self.members_page.click_remove_member_button()
        self.members_page.confirm_remove_button_click()

        # Assert
        WebDriverWait(self.driver, 15).until(lambda driver: len(self.members_page.get_members()) == 1)

        # Allure - attach a screenshot of the members list after removal
        allure.attach(self.driver.get_screenshot_as_png(), name="members list after removal",
                      attachment_type=allure.attachment_type.PNG)

        self.assertEqual(len(self.members_page.get_members()), 1)