import logging
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.web.first_page import FirstPage
from logic.web.login_page import LoginPage


class SuccessfulLoginTest(unittest.TestCase):

    def setUp(self):
        # Initialize the browser and load configuration
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()

        # Start the browser session and navigate to the specified URL
        self.driver = self.browser.get_driver(self.config['url'])

    def tearDown(self):
        # Quit the WebDriver session after test execution
        self.driver.quit()

    def test_login_successful(self):

        # Test case for successful login
        logging.info("Successful Login Test")
        first_page = FirstPage(self.driver)
        first_page.login_button_click()  # click the Login button
        login_page = LoginPage(self.driver)
        login_page.fill_login_email_input(self.config['email'])  # Enter email
        login_page.continue_button_click()  # click the continue button
        login_page.fill_login_password_input(self.config['password'])  # Enter password
        login_page.continue_button_click()  # click the continue button

        # Wait for URL to contain the board title and assert its presence
        WebDriverWait(self.driver, 25).until(EC.url_contains(self.config['username']))
        self.assertTrue(self.config['username'] in self.driver.current_url)

