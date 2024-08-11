import time

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.web.base_app_page import BaseAppPage


class HomePage(BaseAppPage):
    BOARD_NAME = "//div[@class='LinesEllipsis  '] "
    NEW_BOARD = "//a[@class='board-tile']"
    CREATE_BOARD_BUTTON = '//div[@class="board-tile mod-add"]'
    BOARD_TITLE_INPUT = '//input[@aria-required="true"]'
    CREATE_BUTTON = '//button[text()="Create"]'
    HEADER_ACCOUNT_BUTTON = '//button[@data-testid="header-member-menu-button"]'
    PROFILE_AND_VISIBILITY_BUTTON = '//a[@data-testid="account-menu-profile"]'


    def __init__(self, driver):
        """
            Initializes an instance of HomePage with a WebDriver instance.
            Args:
                driver: WebDriver instance used for interacting with the web browser.
        """
        super().__init__(driver)

    def click_create_board_button(self):
        """ Clicks on the create board button. """
        WebDriverWait(self._driver, 40).until(
            EC.visibility_of_element_located((By.XPATH, self.CREATE_BOARD_BUTTON)))
        try:
            create_board_button = self._driver.find_element(By.XPATH, self.CREATE_BOARD_BUTTON)
            create_board_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def fill_board_title_input(self, board_title):
        """ Fills the board title input with the given title. """
        WebDriverWait(self._driver, 40).until(
            EC.visibility_of_element_located((By.XPATH, self.BOARD_TITLE_INPUT)))
        try:
            board_title_input = self._driver.find_element(By.XPATH, self.BOARD_TITLE_INPUT)
            board_title_input.send_keys(board_title)
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def click_create_button(self):
        """ Clicks on the create button and waits for board creation. """
        try:
            WebDriverWait(self._driver, 40).until(
                EC.element_to_be_clickable((By.XPATH, self.CREATE_BUTTON)))
            create_button = self._driver.find_element(By.XPATH, self.CREATE_BUTTON)
            create_button.click()

            # Wait for URL to change, indicating board creation
            current_url = self._driver.current_url
            WebDriverWait(self._driver, 40).until(EC.url_changes(current_url))
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking create button: {e}")
            raise  # Re-raise the exception to make the test fail
    def create_board_flow(self, board_title):
        """ Executes the flow to create a board with the given title. """
        self.click_create_board_button()
        self.fill_board_title_input(board_title)
        self.click_create_button()

    def click_header_account_button(self):
        """ Clicks on the header account button. """
        WebDriverWait(self._driver, 40).until(
            EC.visibility_of_element_located((By.XPATH, self.HEADER_ACCOUNT_BUTTON)))
        try:
            header_account_button = self._driver.find_element(By.XPATH, self.HEADER_ACCOUNT_BUTTON)
            header_account_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def click_profile_and_visibility_button(self):
        """ Clicks on the profile and visibility button. """
        WebDriverWait(self._driver, 40).until(
            EC.visibility_of_element_located((By.XPATH, self.PROFILE_AND_VISIBILITY_BUTTON)))
        try:
            profile_and_visibility_button = self._driver.find_element(By.XPATH, self.PROFILE_AND_VISIBILITY_BUTTON)
            profile_and_visibility_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    # def new_board_is_visible(self):
    #     new_board = WebDriverWait(self._driver, 25).until(
    #         EC.presence_of_element_located((By.XPATH, self.NEW_BOARD)))
    #     return new_board.is_displayed()
    #
    # def get_board_name(self):
    #     board_name = WebDriverWait(self._driver, 25).until(
    #         EC.presence_of_element_located((By.XPATH, self.BOARD_NAME)))
    #     return board_name.text
