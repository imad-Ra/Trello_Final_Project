import logging
import unittest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.web.board_page import BoardPage
from logic.web.first_page import FirstPage
from logic.web.home_page import HomePage
from logic.web.login_page import LoginPage
from infra.jira_handler import JiraHandler


# Allure feature annotation
@allure.feature("Add list to new board - test")
class AddList(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.jira_handler = JiraHandler()

        self.driver = self.browser.get_driver(self.config['url'])
        FirstPage(self.driver).click_login_button()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])
        HomePage(self.driver).create_board_flow(self.config['board_title'])

        # Arrange
        self.board_page = BoardPage(self.driver)

    def tearDown(self):
        # Act
        self.board_page.delete_board_flow()
        self.driver.quit()

    def test_add_list(self):
        logging.info("Test start")
        self.board_page.fill_list_test_area_input(self.config['list_text'])
        self.board_page.click_add_list_button()

        # Allure - attach a screenshot of the added list
        allure.attach(self.driver.get_screenshot_as_png(), name="List Added",
                      attachment_type=allure.attachment_type.PNG)

        # Assert
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.board_page.ADDED_LIST_HEADER)))
        self.assertTrue(self.driver.find_element(By.XPATH, self.board_page.ADDED_LIST_HEADER).is_displayed())


if __name__ == '__main__':
    unittest.main()
