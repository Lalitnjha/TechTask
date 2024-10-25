from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # Define locators for elements on the login page
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container")

    def __init__(self, driver):
        """
        Constructor to initialize the driver instance and assign it to the class.

        :param driver: WebDriver instance used to interact with the browser.
        """
        self.driver = driver

    def login(self, username, password):
        """
        Method to perform the login action.

        :param username: Username for the login.
        :param password: Password for the login.
        :raises TimeoutException: Raised if elements are not found within the specified time.
        """
        try:
            # Wait for the username field to be visible on the page.
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.USERNAME_FIELD)
            )

            # Find the username, password fields, and login button on the page.
            username_field = self.driver.find_element(*self.USERNAME_FIELD)
            password_field = self.driver.find_element(*self.PASSWORD_FIELD)
            login_button = self.driver.find_element(*self.LOGIN_BUTTON)

            # Clear any existing text and enter the username and password.
            username_field.clear()
            username_field.send_keys(username)
            password_field.clear()
            password_field.send_keys(password)

            # Click the login button to submit the form.
            login_button.click()
        except TimeoutException:
            # Capture a screenshot if the login fields are not loaded within the given time.
            self.driver.save_screenshot("timeout_error.png")
            raise TimeoutException("Login fields did not load within the given time.")

    def get_error_message(self):
        """
        Method to retrieve the error message displayed on failed login.

        :return: Text of the error message displayed on the page.
        :raises TimeoutException: Raised if the error message is not found within the specified time.
        """
        # Wait for the error message to be visible on the page.
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )

        # Find the error message element and return its text.
        error_element = self.driver.find_element(*self.ERROR_MESSAGE)
        return error_element.text
