import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductListingPage
from pages.cart_page import CartPage
from utilities.test_data import TestData
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# Class to handle browser setup and teardown for automated tests
class BrowserSetUp:
    def __init__(self):
        # Constructor initializes driver and page objects as None.
        self.driver = None
        self.login_page = None
        self.inventory_page = None
        self.cart_page = None

    def setup(self):
        """
        Method to set up the WebDriver instance and initialize page objects.
        - Configures Chrome options to start the browser maximized.
        - Sets up ChromeDriver using webdriver_manager for easier driver management.
        - Navigates to the base URL defined in TestData.
        - Initializes page objects for login, product listing, and cart pages.
        """

        # Configuring Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model restrictions
        chrome_options.add_argument(
            "--disable-dev-shm-usage")  # Overcome limited resource issues in container environments
        chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration for better stability

        # Setting up the Chrome WebDriver using webdriver_manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # Navigating to the base URL defined in the test data
        self.driver.get(TestData.BASE_URL)

        # Initializing page objects with the WebDriver instance
        self.login_page = LoginPage(self.driver)  # LoginPage object to handle login functionality
        self.inventory_page = ProductListingPage(self.driver)  # ProductListingPage object to handle product listing
        self.cart_page = CartPage(self.driver)  # CartPage object to handle cart functionality

    def teardown(self):
        """
        Method to tear down the WebDriver instance.
        - Checks if the driver is initialized.
        - Closes all browser windows and safely ends the WebDriver session.
        """
        if self.driver:
            self.driver.quit()  # Close all browser windows and safely end the session


# Pytest fixture to set up and tear down the browser for test classes.
@pytest.fixture(scope="class")
def browser_setup(request):
    """
    Pytest fixture to set up and tear down the browser for the test class.
    - Initializes an instance of BrowserSetUp.
    - Calls the setup method to start the browser and initialize page objects.
    - Assigns the setup instance to the test class, making it accessible as 'browser_setup'.
    - After the test class execution, calls the teardown method to close the browser.
    """

    # Creating an instance of BrowserSetUp
    setup_instance = BrowserSetUp()

    # Setting up the WebDriver and page objects
    setup_instance.setup()

    # Assign the setup instance to the test class itself for access in test methods
    request.node.cls.browser_setup = setup_instance

    # Yield to allow test execution
    yield

    # After all tests are executed, perform teardown
    setup_instance.teardown()
