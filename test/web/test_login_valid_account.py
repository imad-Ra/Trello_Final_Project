import logging
import unittest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.web.first_page import FirstPage
from logic.web.login_page import LoginPage
from infra.jira_handler import JiraHandler

@allure.feature("Login Test - valid account + password")
class SuccessfulLoginTest(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.jira_handler = JiraHandler()

        self.driver = self.browser.get_driver(self.config['url'])

    def tearDown(self):
        self.driver.quit()

    @allure.story("Successful Login")
    def test_login_successful(self):
        logging.info("Successful Login Test")

        # Act
        first_page = FirstPage(self.driver)
        first_page.click_login_button()

        login_page = LoginPage(self.driver)
        login_page.fill_login_email_input(self.config['email'])
        login_page.click_continue_button()
        login_page.fill_login_password_input(self.config['password'])
        login_page.click_continue_button()

        # Assert
        WebDriverWait(self.driver, 25).until(EC.url_contains(self.config['username']))

        # Allure - attach a screenshot of the logged-in page
        allure.attach(self.driver.get_screenshot_as_png(), name="logged in page",
                      attachment_type=allure.attachment_type.PNG)

        self.assertTrue(self.config['username'] in self.driver.current_url)