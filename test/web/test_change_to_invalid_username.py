import logging
import unittest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.web.first_page import FirstPage
from logic.web.home_page import HomePage
from logic.web.login_page import LoginPage
from logic.web.profile_page import ProfilePage
from infra.jira_handler import JiraHandler

@allure.feature("Invalid Username - test")
class ProfileInvalidUsernameChange(unittest.TestCase):
    def setUp(self):
        # Arrange
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.jira_handler = JiraHandler()

        self.driver = self.browser.get_driver(self.config['url'])

        FirstPage(self.driver).click_login_button()
        LoginPage(self.driver).login_flow(self.config['email'], self.config['password'])

        self.home_page = HomePage(self.driver)
        self.profile_page = ProfilePage(self.driver)

    def tearDown(self):
        self.profile_page.change_back_username(self.config['username'])
        self.driver.quit()

    @allure.story("Change to Invalid Username")
    def test_change_to_invalid_username(self):
        logging.info("Invalid Username Change Test")

        # Arrange
        self.home_page.click_header_account_button()
        self.home_page.click_profile_and_visibility_button()

        # Act
        self.profile_page.fill_random_username_input(5, 20, "uppercase")
        self.profile_page.profile_change_save_button_click()

        # Assert
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.profile_page.ERROR_MESSAGE)))

        # Allure - attach a screenshot of the error message
        allure.attach(self.driver.get_screenshot_as_png(), name="invalid username error message",
                      attachment_type=allure.attachment_type.PNG)

        self.assertTrue(self.driver.find_element(By.XPATH, self.profile_page.ERROR_MESSAGE).is_displayed())




