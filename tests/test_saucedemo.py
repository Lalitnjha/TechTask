import os
import pytest
from selenium.common import TimeoutException
from utilities.setup import BrowserSetUp
from utilities.assertions import Assertions
from utilities.test_data import TestData


class TestSauceDemo:
    """
    tests suite for the SauceDemo web application, covering both happy path and unhappy path scenarios.
    """

    @pytest.fixture(autouse=True)
    def browser_setup_fixture(self):
        """
        Fixture to set up the browser environment before each test and tear it down afterward.
        - Initializes the browser and navigates to the starting page.
        - Sets up the Assertions utility for verification and screenshot capture.
        """
        self.browser_setup = BrowserSetUp()
        self.browser_setup.setup()

        # Define screenshot base directory
        self.screenshot_base_dir = os.path.join(os.getcwd(), 'screenshots')

        # Initialize Assertions with screenshot base directory
        self.assertions = Assertions(self.browser_setup.driver, self.screenshot_base_dir)
        yield
        self.browser_setup.teardown()

    def login_and_verify(self, username, password, screenshot_prefix):
        """
        Helper method to log in and verify the login process.
        - Captures screenshots before and after login.
        :param username: The username for login.
        :param password: The password for login.
        :param screenshot_prefix: Prefix for screenshot naming.
        """
        self.assertions.capture_screenshot(f"{screenshot_prefix} - Before Login")
        self.browser_setup.login_page.login(username, password)
        self.assertions.capture_screenshot(f"{screenshot_prefix} - Login Successful")

    def test_happy_path(self):
        """
        tests case for a successful user journey (happy path).
        - Logs in with valid credentials, adds a product to the cart, and verifies its presence.
        """
        self.login_and_verify(TestData.VALID_USERNAME, TestData.VALID_PASSWORD, "Happy Path")

        self.browser_setup.inventory_page.add_product_to_cart()
        self.assertions.capture_screenshot("Product Added")

        self.browser_setup.inventory_page.go_to_cart()
        self.assertions.verify_element(
            self.browser_setup.cart_page.verify_product_in_cart(),
            "Product does not exist in the cart",
            "Verify Product in Cart"
        )

    def test_unhappy_path(self):
        """
        tests case for an invalid login attempt (unhappy path).
        - Attempts to log in with invalid credentials and verifies the error message.
        """
        self.assertions.capture_screenshot("Unhappy Path - Before Login Attempt")
        try:
            self.browser_setup.login_page.login(TestData.INVALID_USERNAME, TestData.INVALID_PASSWORD)
            self.assertions.capture_screenshot("Unhappy Path - Login Failed")
        except TimeoutException as e:
            self.assertions.handle_exception(e, "Timeout Error during Login")

        expected_message = "Epic sadface: Username and password do not match any user in this service"
        actual_message = self.browser_setup.login_page.get_error_message()
        self.assertions.verify_element(
            actual_message == expected_message,
            f"Unexpected error message: {actual_message}",
            "Verify Error Message"
        )


if __name__ == "__main__":
    pytest.main()
