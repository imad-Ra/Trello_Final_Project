from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from logic.web.base_app_page import BaseAppPage


class FirstPage(BaseAppPage):
    LOGIN_BUTTON = '//a[@class="Buttonsstyles__Button-sc-1jwidxo-0 kTwZBr"]'

    def __init__(self, driver):
        """
            Initializes an instance of FirstPage with a WebDriver instance.
            Args:
                driver: WebDriver instance used for interacting with the web browser.
        """
        super().__init__(driver)
        try:
            self._login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def click_login_button(self):
        """ Clicks on the login button. """
        self._login_button.click()
