import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.api.api_wrapper import APIWrapper
from logic.api.boards_api import APIBoard
from logic.web.first_page import FirstPage
from logic.web.home_page import HomePage
from logic.web.login_page import LoginPage


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.driver = self.browser.get_driver(self.config['url'])
        FirstPage(self.driver).login_button_click()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])
        self.home_page = HomePage(self.driver)

        # Create APIWrapper instance and pass it to APIBoard
        self.api_wrapper = APIWrapper()
        self.api_board = APIBoard(self.api_wrapper)

    def tearDown(self):
        self.api_board.delete_a_board()
        self.driver.quit()

    def test_create_board(self):
        # Create board via UI
        self.home_page.create_board_button_click()
        self.home_page.fill_board_title_input(self.config['board_title'])
        self.home_page.create_button_click()

        # Verify board creation via UI
        WebDriverWait(self.driver, 30).until(EC.url_contains(self.config['board_title']))
        self.assertTrue(self.config['board_title'] in self.driver.current_url)

        # Verify board via API
        response = self.api_board.get_a_board()
        self.assertTrue(response.ok, f"API request failed. Status: {response.status_code}")
        self.assertEqual(response.data['name'], self.config['board_title'])


if __name__ == '__main__':
    unittest.main()