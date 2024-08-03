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
        self.driver.implicitly_wait(10)

        # Initialize BoardPage for testing
        self.board_page = BoardPage(self.driver)

    def tearDown(self):
        # Delete the board
        if self.driver.current_url != f"https://trello.com/u/{self.config['username']}/boards":
            self.board_page.delete_board_flow()

        # Quit the WebDriver session after tests
        self.driver.quit()

    def test_delete_board_successful(self):
        # Test case to delete a board and verify redirection to the main boards page
        logging.info("Delete Board Test")
        self.board_page.header_menu_button_click()
        self.board_page.close_board_button_click()
        self.board_page.confirm_close_board_button_click()
        self.board_page.delete_board_button_click()
        self.board_page.confirm_delete_board_button_click()

        # Assert that the URL contains the username after deletion
        WebDriverWait(self.driver, 10).until(EC.url_contains(self.config['username']))
        self.assertTrue(self.config['username'] in self.driver.current_url)
    #
    # def test_move_list(self):
    #     # Test case to move a list within the board and verify its position
    #     logging.info("Move list Test")
    #     lists = self.board_page.move_list()
    #     WebDriverWait(self.driver, 20).until(lambda driver: lists[1].text == "To Do")
    #     self.assertEqual(lists[1].text, "To Do")

    def test_add_card(self):
        # Test case to add a card to the board and verify its presence
        logging.info("Add Card Test")
        self.board_page.fill_card_test_area_input(self.config['card_text'])
        self.board_page.add_card_button_click()
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located((By.XPATH, self.board_page.ADDED_CARD_HEADER)))
        self.assertTrue(self.driver.find_element(By.XPATH, self.board_page.ADDED_CARD_HEADER).is_displayed())
