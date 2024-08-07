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
    def test_login_invalid_account(self):
        # Test case for unsuccessful login
        logging.info("Unsuccessful Login Test")
        first_page = FirstPage(self.driver)
        first_page.login_button_click()
        login_page = LoginPage(self.driver)
        login_page.fill_login_email_input(self.config['email'])
        login_page.continue_button_click()
        login_page.fill_login_password_input(self.config['wrong_password'])
        login_page.continue_button_click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, login_page.LOGIN_ERROR)))
        self.assertTrue(self.driver.find_element(By.XPATH, login_page.LOGIN_ERROR).is_displayed())
