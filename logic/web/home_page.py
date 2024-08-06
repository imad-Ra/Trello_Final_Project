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

    def create_board_button_click(self):
        """ Clicks on the create board button. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.CREATE_BOARD_BUTTON)))
        try:
            create_board_button = self._driver.find_element(By.XPATH, self.CREATE_BOARD_BUTTON)
            create_board_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def fill_board_title_input(self, board_title):
        """ Fills the board title input with the given title. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.BOARD_TITLE_INPUT)))
        try:
            board_title_input = self._driver.find_element(By.XPATH, self.BOARD_TITLE_INPUT)
            board_title_input.send_keys(board_title)
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def create_button_click(self):
        """ Clicks on the create button. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.CREATE_BUTTON)))
        try:
            create_button = self._driver.find_element(By.XPATH, self.CREATE_BUTTON)
            create_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def create_board_flow(self, board_title):
        """ Executes the flow to create a board with the given title. """
        self.create_board_button_click()
        self.fill_board_title_input(board_title)
        self.create_button_click()

    def header_account_button_click(self):
        """ Clicks on the header account button. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.HEADER_ACCOUNT_BUTTON)))
        try:
            header_account_button = self._driver.find_element(By.XPATH, self.HEADER_ACCOUNT_BUTTON)
            header_account_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def profile_and_visibility_button_click(self):
        """ Clicks on the profile and visibility button. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.PROFILE_AND_VISIBILITY_BUTTON)))
        try:
            profile_and_visibility_button = self._driver.find_element(By.XPATH, self.PROFILE_AND_VISIBILITY_BUTTON)
            profile_and_visibility_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def new_board_is_visible(self):
        new_board = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.NEW_BOARD)))
        return new_board.is_displayed()

    def get_board_name(self):
        board_name = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.BOARD_NAME)))
        return board_name.text
