import unittest
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.jira_handler import JiraHandler
from logic.web.first_page import FirstPage
from logic.web.login_page import LoginPage


class FailedTestForJira(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self.driver = self.browser.get_driver(self.config["url"])
        self.jira_handler = JiraHandler()

    def tearDown(self):
        self.driver.quit()

    @allure.story("Intentional Failure for Jira Integration")
    def test_intentional_failure(self):
        """
        This test demonstrates Jira integration for failed tests by intentionally asserting that a successful login
        should fail. It logs in with valid credentials, verifies the login, then falsely asserts the login failed.
        The purpose is to confirm that when a test fails, a Jira issue is automatically
        created, enabling automated tracking of test failures.
        """

        # Arrange
        first_page = FirstPage(self.driver)
        login_page = LoginPage(self.driver)

        # Act
        first_page.click_login_button()
        login_page.fill_login_email_input(self.config['email'])
        login_page.click_continue_button()
        login_page.fill_login_password_input(self.config['password'])
        login_page.click_continue_button()

        is_logged_in = WebDriverWait(self.driver, 10).until(
            EC.url_contains(self.config['username'])
        )

        # Assert
        try:
            self.assertFalse(is_logged_in, "User should not be logged in, but they are.")
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_result_screenshot",
                          attachment_type=allure.attachment_type.PNG)

            self.jira_handler.create_issue(
                self.secret["jira_project_key"],
                "Test Failed: Intentional Failure for Jira Integration",
                f"Assertion failed: {str(e)}",
                "Bug"
            )
            raise  # Re-raise the exception to mark the test as failed


if __name__ == '__main__':
    unittest.main()