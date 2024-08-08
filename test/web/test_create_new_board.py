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
from infra.web.utils import Utils


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

        self.random_name = Utils.generate_random_lowercase_string(3,5)

    def tearDown(self):
        self.driver.quit()
        self.api_board.delete_board_by_name(self.random_name)

    def test_create_board(self):
        # Create board via UI
        self.home_page.create_board_button_click()
        self.home_page.fill_board_title_input(self.random_name)
        self.home_page.click_create_button()


        # Verify board creation via UI
        WebDriverWait(self.driver, 30).until(EC.url_contains(self.random_name))
        self.assertTrue(self.random_name in self.driver.current_url)

