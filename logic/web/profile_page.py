from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.web.utils import Utils
from logic.web.base_app_page import BaseAppPage


class ProfilePage(BaseAppPage):
    USERNAME_INPUT = '//input[@id="username"]'
    PROFILE_CHANGE_SAVE_BUTTON = '//button[@type="submit"]'
    ERROR_MESSAGE = '//p[@id="SaveProfileError_Field_username"]'

    def __init__(self, driver):
        """
            Initializes an instance of ProfilePage with a WebDriver instance.
            Args:
                driver: WebDriver instance used for interacting with the web browser.
        """
        super().__init__(driver)

    def fill_random_username_input(self, min_length, max_length, letter_case):
        """
            Clears the username input field and fills it with a randomly generated username.
            Args:
                min_length (int): Minimum length of the username.
                max_length (int): Maximum length of the username.
                letter_case (str): Letter case of the username ("lowercase" or "uppercase").
        """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.USERNAME_INPUT)))
        try:
            username_input = self._driver.find_element(By.XPATH, self.USERNAME_INPUT)
            username_input.clear()
            if letter_case == "lowercase":
                username_input.send_keys(Utils.generate_random_lowercase_string(min_length, max_length))
            elif letter_case == "uppercase":
                username_input.send_keys(Utils.generate_random_string(min_length, max_length))
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def profile_change_save_button_click(self):
        """ Clicks on the save button after changing the username in the profile. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.PROFILE_CHANGE_SAVE_BUTTON)))
        try:
            profile_change_save_button = self._driver.find_element(By.XPATH, self.PROFILE_CHANGE_SAVE_BUTTON)
            profile_change_save_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def change_valid_username_flow(self, min_length, max_length, letter_case):
        """
            Executes the flow to change the username with valid inputs.
            Args:
                min_length (int): Minimum length of the username.
                max_length (int): Maximum length of the username.
                letter_case (str): Letter case of the username ("lowercase" or "uppercase").
        """
        self.fill_random_username_input(min_length, max_length, letter_case)
        self.profile_change_save_button_click()

    def change_invalid_username_flow(self, min_length, max_length, letter_case):
        """
            Executes the flow to change the username with invalid inputs.
            Args:
                min_length (int): Minimum length of the username.
                max_length (int): Maximum length of the username.
                letter_case (str): Letter case of the username ("lowercase" or "uppercase").
        """
        self.fill_random_username_input(min_length, max_length, letter_case)
        self.profile_change_save_button_click()

    def change_back_username(self, username):
        """
            Changes the username back to a specified username.
            Args:
                username (str): The username to change back to.
        """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.USERNAME_INPUT)))
        try:
            username_input = self._driver.find_element(By.XPATH, self.USERNAME_INPUT)
            username_input.clear()
            username_input.send_keys(username)
            profile_change_save_button = self._driver.find_element(By.XPATH, self.PROFILE_CHANGE_SAVE_BUTTON)
            profile_change_save_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

