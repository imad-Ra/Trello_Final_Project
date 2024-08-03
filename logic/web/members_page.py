from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from logic.web.base_app_page import BaseAppPage


class MembersPage(BaseAppPage):
    INVITE_MEMBERS_BUTTON = '//button[@class="w2Ok_QPiPTxPuy bxgKMAm3lq5BpA SdamsUKjxSBwGb SEj5vUdI3VvxDc"]'
    MEMBER_EMAIL_INPUT = '//input[@data-testid="add-members-input"]'
    SEND_INVITE_BUTTON = '//button[@class="DXtVhm7hhVXHuw bxgKMAm3lq5BpA SdamsUKjxSBwGb PnEv2xIWy3eSui SEj5vUdI3VvxDc"]'
    MEMBERS = '//div[@data-testid="workspace-member-item"]'
    REMOVE_MEMBER_BUTTON = '//button[@class="RGbFPavlhzMAS7 bxgKMAm3lq5BpA SEj5vUdI3VvxDc"]'
    CONFIRM_REMOVE_BUTTON = '//p[text()="Remove from Workspace"]'

    def __init__(self, driver):
        """
            Initializes an instance of MembersPage with a WebDriver instance.
            Args:
                driver: WebDriver instance used for interacting with the web browser.
        """
        super().__init__(driver)

    def invite_members_button_click(self):
        """ Clicks on the invite members button. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.INVITE_MEMBERS_BUTTON)))
        try:
            invite_members_button = self._driver.find_element(By.XPATH, self.INVITE_MEMBERS_BUTTON)
            invite_members_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def fill_member_email_input(self, member_email):
        """ Fills the member email input with the given email and presses Enter. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.MEMBER_EMAIL_INPUT)))
        try:
            member_email_input = self._driver.find_element(By.XPATH, self.MEMBER_EMAIL_INPUT)
            member_email_input.send_keys(member_email)
            member_email_input.send_keys(Keys.ENTER)
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def send_invite_button_click(self):
        """ Clicks on the send invite button. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.SEND_INVITE_BUTTON)))
        try:
            send_invite_button = self._driver.find_element(By.XPATH, self.SEND_INVITE_BUTTON)
            send_invite_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def get_members(self):
        """ Returns a list of members currently displayed on the page. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.MEMBERS)))
        try:
            members = self._driver.find_elements(By.XPATH, self.MEMBERS)
            return members
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def remove_member_button_click(self):
        """ Clicks on the remove member button. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.REMOVE_MEMBER_BUTTON)))
        try:
            remove_member_button = self._driver.find_element(By.XPATH, self.REMOVE_MEMBER_BUTTON)
            remove_member_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def confirm_remove_button_click(self):
        """ Clicks on the confirm remove button. """
        WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.CONFIRM_REMOVE_BUTTON)))
        try:
            confirm_remove_button = self._driver.find_element(By.XPATH, self.CONFIRM_REMOVE_BUTTON)
            confirm_remove_button.click()
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def workspace_add_member_flow(self, member_email):
        """
            Executes the flow to add a member to the workspace.
            Args:
                member_email: Email of the member to add.
        """
        self.invite_members_button_click()
        self.fill_member_email_input(member_email)
        self.send_invite_button_click()

    def workspace_remove_member_flow(self):
        """ Executes the flow to remove a member from the workspace. """
        self.remove_member_button_click()
        self.confirm_remove_button_click()
