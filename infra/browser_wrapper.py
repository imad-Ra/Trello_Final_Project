from selenium import webdriver
from infra.config_provider import ConfigProvider


class BrowserWrapper:

    def __init__(self):
        """
            Initializes an instance of BrowserWrapper, sets the driver to None,
            loads configuration from file, and prints "Test Start".
        """
        self._driver = None
        self.config = ConfigProvider.load_from_file()
        print("Test Start")

    def get_driver(self, url):
        """
            Initializes the WebDriver based on the browser type specified in the configuration
            and navigates to the given URL.
            Args:
                url (str): The URL to navigate to.
            Returns:
                WebDriver: The initialized WebDriver instance.
        """
        if self.config["browser"] == "Chrome":
            self._driver = webdriver.Chrome()
        elif self.config["browser"] == "FireFox":
            self._driver = webdriver.Firefox()
        elif self.config["browser"] == "Edge":
            self._driver = webdriver.Edge()
        else:
            print("browser not found")

        self._driver.get(url)
        return self._driver
