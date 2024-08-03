import logging
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.web.board_page import BoardPage
from logic.web.first_page import FirstPage
from logic.web.home_page import HomePage
from logic.web.login_page import LoginPage


class HomePageTest(unittest.TestCase):

    def setUp(self):
        # Initialize browser and load configuration
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()

        # Start browser session, navigate to the specified URL, and maximize window
        self.driver = self.browser.get_driver(self.config['url'])

        # Perform login flow to reach the home page
        FirstPage(self.driver).login_button_click()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])

        # Initialize HomePage for testing
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        # Clean up by deleting the created board and quitting the WebDriver session
        BoardPage(self.driver).delete_board_flow()
        self.driver.quit()

    def test_create_board_successful(self):
        # Test case to create a board and verify its creation
        logging.info("Create Board Test")
        self.home_page.create_board_button_click()
        self.home_page.fill_board_title_input(self.config['board_title'])
        self.home_page.create_button_click()

        # Wait for URL to contain the board title and assert its presence
        WebDriverWait(self.driver, 10).until(EC.url_contains(self.config['board_title']))
        self.assertTrue(self.config['board_title'] in self.driver.current_url)
