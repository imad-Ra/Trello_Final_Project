import logging
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.web.board_page import BoardPage
from logic.web.first_page import FirstPage
from logic.web.home_page import HomePage
from logic.web.login_page import LoginPage


class BoardPageTest(unittest.TestCase):

    def setUp(self):
        # Initialize browser and load configuration
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()

        # Start browser session and navigate to the specified URL
        self.driver = self.browser.get_driver(self.config['url'])
        FirstPage(self.driver).login_button_click()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])
        HomePage(self.driver).create_board_flow(self.config['board_title'])
        self.driver.implicitly_wait(15)

        # Initialize BoardPage for testing
        self.board_page = BoardPage(self.driver)

    def tearDown(self):
        # Delete the board
        self.board_page.delete_board_flow()

        # Quit the WebDriver session after tests
        self.driver.quit()


    def test_add_list(self):
        # Test case to add a card to the board and verify its presence
        logging.info("Add Card Test")
        self.board_page.fill_list_test_area_input(self.config['list_text'])
        self.board_page.add_list_button_click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.board_page.ADDED_LIST_HEADER)))
        self.assertTrue(self.driver.find_element(By.XPATH, self.board_page.ADDED_LIST_HEADER).is_displayed())