from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonUtility:
    def __init__(self, driver):
        """
        Constructor to initialize the WebDriver instance.

        Args:
            driver: WebDriver instance used for interacting with the web elements.
        """
        self.driver = driver

    def find_element(self, locator, time=10):
        """
        Waits for the presence of a web element and returns it.

        Args:
            locator: Tuple containing the locator strategy and the locator value.
            time: Maximum wait time (in seconds) before throwing a TimeoutException (default is 10 seconds).

        Returns:
            WebElement: The web element if found within the specified time.

        Raises:
            TimeoutException: If the element is not found within the specified time.
        """
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator, time=10):
        """
        Waits for the presence of a web element and clicks on it.

        Args:
            locator: Tuple containing the locator strategy and the locator value.
            time: Maximum wait time (in seconds) before throwing a TimeoutException (default is 10 seconds).

        Returns:
            None

        Raises:
            TimeoutException: If the element is not found or not clickable within the specified time.
        """
        element = self.find_element(locator, time)
        element.click()

    def enter_text(self, locator, text, time=10):
        """
        Waits for the presence of a web element, clears any pre-existing text, and enters the provided text.

        Args:
            locator: Tuple containing the locator strategy and the locator value.
            text: The text to be entered into the web element.
            time: Maximum wait time (in seconds) before throwing a TimeoutException (default is 10 seconds).

        Returns:
            None

        Raises:
            TimeoutException: If the element is not found or not interactable within the specified time.
        """
        element = self.find_element(locator, time)
        element.clear()
        element.send_keys(text)
