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
class AddWorkspaceMembersTest(unittest.TestCase):
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

    @allure.story("Add Member to Workspace")
    def test_workspace_add_member(self):
        logging.info("Add Member To Workspace Test")

        # Act
        self.members_page.invite_members_button_click()
        self.members_page.fill_member_email_input(self.config['member_email'])
        self.members_page.send_invite_button_click()

        # Assert
        WebDriverWait(self.driver, 15).until(lambda driver: len(self.members_page.get_members()) > 1)

        # Allure - attach a screenshot of the members list
        allure.attach(self.driver.get_screenshot_as_png(), name="members list",
                      attachment_type=allure.attachment_type.PNG)

        self.assertIn(self.config['member_username'], self.members_page.get_members()[1].text)