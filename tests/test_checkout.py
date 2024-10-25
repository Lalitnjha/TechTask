import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from pages.login_page import LoginPage
from pages.product_page import ProductListingPage
from utilities.assertions import Assertions
from utilities.test_data import TestData


class TestCheckout:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """
        Fixture to set up the browser environment before each test and tear it down after.
        - Initializes the browser, navigates to the base URL, and sets up page objects.
        - Ensures the browser is closed after each test.
        """
        # Setup
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get(TestData.BASE_URL)

        # Page object instances
        self.login_page = LoginPage(self.driver)
        self.inventory_page = ProductListingPage(self.driver)
        self.cart_page = CartPage(self.driver)

        # Define screenshot base directory
        self.screenshot_base_dir = os.path.join(os.getcwd(), 'screenshots')

        # Initialize Assertions with screenshot base directory
        self.assertions = Assertions(self.driver, self.screenshot_base_dir)

        yield  # tests runs here

        # Teardown
        self.driver.quit()

    def login_and_add_to_cart(self, username, password):
        """
        Reusable method to log in and add a product to the cart.
        - Logs in using the provided credentials and adds the first product to the cart.
        - Verifies the product is successfully added to the cart.
        """
        self.assertions.capture_screenshot("Before Login")
        self.login_page.login(username, password)
        self.assertions.capture_screenshot("Login Successful")

        self.inventory_page.add_product_to_cart()
        self.assertions.capture_screenshot("Product Added")

        self.inventory_page.go_to_cart()
        self.assertions.verify_element(
            self.cart_page.verify_product_in_cart(),
            "Product does not exist in the cart",
            "Verify Product in Cart"
        )

    def test_complete_checkout(self):
        """
        tests case to verify the complete checkout process.
        - Logs in, adds a product to the cart, proceeds to checkout, and verifies order confirmation.
        """
        # Perform login and add product to the cart
        self.login_and_add_to_cart(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)

        # Proceed with the checkout process
        checkout_page = CheckoutPage(self.driver)
        confirmation_page = ConfirmationPage(self.driver)

        self.cart_page.click_checkout_button()
        checkout_page.enter_checkout_information(TestData.FIRST_NAME, TestData.LAST_NAME, TestData.POSTAL_CODE)
        checkout_page.click_continue_button()
        confirmation_page.click_finish_button()

        # Verify the order confirmation message
        self.assertions.assert_text_equal(
            confirmation_page.get_order_confirmation(),
            "THANK YOU FOR YOUR ORDER",
            "Order confirmation message does not match expected."
        )


if __name__ == "__main__":
    pytest.main()
