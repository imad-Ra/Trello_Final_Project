import logging
import unittest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.web.first_page import FirstPage
from logic.web.home_page import HomePage
from logic.web.login_page import LoginPage
from logic.web.profile_page import ProfilePage
from infra.jira_handler import JiraHandler

# Allure feature annotation
@allure.feature("Valid Username - test")
class ProfileValidUsernameChange(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.jira_handler = JiraHandler()

        self.driver = self.browser.get_driver(self.config['url'])

        FirstPage(self.driver).click_login_button()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])

        self.home_page = HomePage(self.driver)
        self.profile_page = ProfilePage(self.driver)

        self.home_page.click_header_account_button()
        self.home_page.click_profile_and_visibility_button()

    def tearDown(self):
        # Act
        self.profile_page.change_back_username(self.config['username'])
        self.profile_page.profile_change_save_button_click()
        self.driver.quit()

    @allure.story("Change to Valid Username")
    def test_change_to_valid_username(self):
        logging.info("Valid Username Change Test")
        # Act
        self.profile_page.fill_random_username_input(5, 20, "lowercase")
        self.profile_page.profile_change_save_button_click()

        # Assert
        WebDriverWait(self.driver, 15).until(
            lambda driver: self.driver.find_element(By.XPATH, self.profile_page.USERNAME_INPUT).text != self.config['username'])


        self.assertNotEqual(self.driver.find_element(By.XPATH, self.profile_page.USERNAME_INPUT).text, self.config['username'])


        # Allure: Attach a screenshot of the updated username
        allure.attach(self.driver.get_screenshot_as_png(), name="updated username",
                      attachment_type=allure.attachment_type.PNG)


        # # Jira: Create a bug report if the test fails
        # if self.driver.find_element(By.XPATH, self.profile_page.USERNAME_INPUT).text == self.config['username']:
        #     bug_summary = "Valid username change failed"
        #     bug_description = "The 'Change Username' feature is not working as expected."
        #     issue = self.jira_handler.create_issue(bug_summary, bug_description)
        #     self.assertIsNotNone(issue)
        #     self.assertEqual(issue.fields.summary, bug_summary)
        #     self.assertEqual(issue.fields.description, bug_description)
        #     self.assertEqual(issue.fields.issuetype.name, "Bug")

if __name__ == '__main__':
    unittest.main()