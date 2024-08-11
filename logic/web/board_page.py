import time

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.config_provider import ConfigProvider
from logic.web.base_app_page import BaseAppPage
from selenium.webdriver.common.action_chains import ActionChains


class BoardPage(BaseAppPage):
    config = ConfigProvider.load_from_file()

    # XPath constants for elements on the page
    HEADER_MENU_BUTTON = '//button[@aria-label="Show menu"]'
    CLOSE_BOARD_BUTTON = \
        '//a[@class="board-menu-navigation-item-link board-menu-navigation-item-link-v2 js-close-board"]'
    CONFIRM_CLOSE_BOARD_BUTTON = '//input[@data-testid="close-board-confirm-button"]'
    DELETE_BOARD_BUTTON = '//button[@data-testid="close-board-delete-board-button"]'
    CONFIRM_DELETE_BOARD_BUTTON = '//button[@data-testid="close-board-delete-board-confirm-button"]'
    LISTS = '//h2[@data-testid="list-name"]'
    WORKSPACE_OPTIONS = '//a[@class="boards-page-board-section-header-options-item"]'
    LIST_TEXT_AREA_INPUT = '//textarea[@data-testid="list-name-textarea"]'
    ADD_LIST_BUTTON = '//button[text()="Add list"]'
    ADDED_LIST_HEADER = '//div[@data-testid="list-header"]'

    def __init__(self, driver):
        """
            Initializes an instance of BoardPage with a WebDriver instance.
            Args:
                driver: WebDriver instance used for interacting with the web browser.
        """
        super().__init__(driver)

    def navigate_to_board(self, board_id):
        self._driver.get(f"{self.config['url']}/b/{board_id}")

    def click_header_menu_button(self):
        """ Clicks on the header menu button in the board page. """
        WebDriverWait(self._driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, self.HEADER_MENU_BUTTON)))
        try:
            header_menu_button = self._driver.find_element(By.XPATH, self.HEADER_MENU_BUTTON)
            header_menu_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def click_close_board_button(self):
        """ Clicks on the close board button. """
        WebDriverWait(self._driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, self.CLOSE_BOARD_BUTTON)))
        try:
            close_board_button = self._driver.find_element(By.XPATH, self.CLOSE_BOARD_BUTTON)
            close_board_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def click_confirm_close_board_button(self):
        """ Clicks on the confirm close board button. """
        WebDriverWait(self._driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, self.CONFIRM_CLOSE_BOARD_BUTTON)))
        try:
            confirm_close_board_button = self._driver.find_element(By.XPATH, self.CONFIRM_CLOSE_BOARD_BUTTON)
            confirm_close_board_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def click_delete_board_button(self):
        """ Clicks on the delete board button. """
        WebDriverWait(self._driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, self.DELETE_BOARD_BUTTON)))
        try:
            delete_board_button = self._driver.find_element(By.XPATH, self.DELETE_BOARD_BUTTON)
            delete_board_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def click_confirm_delete_board_button(self):
        """ Clicks on the confirm delete board button. """
        WebDriverWait(self._driver, 25).until(
            EC.visibility_of_element_located((By.XPATH, self.CONFIRM_DELETE_BOARD_BUTTON)))
        try:
            confirm_delete_board_button = self._driver.find_element(By.XPATH, self.CONFIRM_DELETE_BOARD_BUTTON)
            confirm_delete_board_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def delete_board_flow(self):
        """ Executes the flow to delete a board. """
        time.sleep(3)  #For presenatiton only !
        self.click_header_menu_button()
        self.click_close_board_button()
        self.click_confirm_close_board_button()
        self.click_delete_board_button()
        self.click_confirm_delete_board_button()

    def move_list(self):
        """ Moves a list using drag and drop. """
        action = ActionChains(self._driver)
        WebDriverWait(self._driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.LISTS)))
        try:
            lists = self._driver.find_elements(By.XPATH, self.LISTS)
            action.drag_and_drop(lists[0], lists[1]).perform()
            lists = self._driver.find_elements(By.XPATH, self.LISTS)
            return lists
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def workspace_option_select(self, option_number):
        """ Selects a workspace option based on the given option number. """
        WebDriverWait(self._driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.WORKSPACE_OPTIONS)))
        try:
            workspace_options = self._driver.find_elements(By.XPATH, self.WORKSPACE_OPTIONS)
            if option_number == 1:
                workspace_options[0].click()
            elif option_number == 2:
                workspace_options[1].click()
            elif option_number == 3:
                workspace_options[2].click()
            elif option_number == 4:
                workspace_options[3].click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def fill_list_test_area_input(self, text):
        """ Fills the card text area input with the given text. """
        WebDriverWait(self._driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.LIST_TEXT_AREA_INPUT)))
        try:
            card_test_area_input = self._driver.find_element(By.XPATH, self.LIST_TEXT_AREA_INPUT)
            card_test_area_input.send_keys(text)
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def click_add_list_button(self):
        """ Clicks on the add card button. """
        WebDriverWait(self._driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.ADD_LIST_BUTTON)))
        try:
            add_card_button = self._driver.find_element(By.XPATH, self.ADD_LIST_BUTTON)
            add_card_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    # def add_list_flow(self, text):
    #     """ Executes the flow to add a card with the given text. """
    #     self.fill_list_test_area_input(text)
    #     self.click_add_list_button()
    #
    # def get_board_id(self):
    #     # Assuming the board ID is in the URL
    #     current_url = self._driver.current_url
    #     return current_url.split('/')[-1]

    def wait_for_list_and_verify(self, list_name):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.XPATH, self.LISTS)))
        lists = self._driver.find_elements(By.XPATH, self.LISTS)
        list_names = [list_elem.text for list_elem in lists]
        return list_name in list_names


    def wait_for_board_to_load(self, board_name):
        try:
            # First, wait for the URL to contain the board name
            WebDriverWait(self._driver, 40).until(EC.url_contains(board_name))

            # Then, add a sleep to ensure the page is fully loaded
            time.sleep(8)

            # Finally, wait for a key element on the board page
            WebDriverWait(self._driver, 40).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".board-header"))
            )

            return True
        except:
            return False
