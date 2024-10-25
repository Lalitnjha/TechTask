import allure
import string
import os
import datetime


class Assertions:
    def __init__(self, driver, screenshot_base_dir):
        """
        Initialize the Assertions class with a WebDriver instance.

        :param driver: WebDriver instance for interacting with the browser or mobile app.
        :param screenshot_base_dir: Base directory to save screenshots.
        """
        self.driver = driver
        self.screenshot_base_dir = screenshot_base_dir

    def verify_element(self, condition, message, step_name="Verification"):
        """
        Verify a specified condition and capture a screenshot if the condition fails.

        :param condition: Boolean condition to be verified.
        :param message: Error message to display if the condition is False.
        :param step_name: Name of the verification step for the allure report.
        :return: None
        """
        with allure.step(step_name):
            try:
                assert condition, message
            except AssertionError:
                allure.attach(self.driver.get_screenshot_as_png(), name=step_name,
                              attachment_type=allure.attachment_type.PNG)
                raise  # Re-raise the exception to propagate the error

    def handle_exception(self, exception, step_name="Exception Occurred"):
        """
        Handle exceptions by capturing a screenshot and logging the exception message.

        :param exception: The exception object to handle.
        :param step_name: Name of the exception handling step for the allure report.
        :return: None
        :raises: Reraises the original exception after capturing the screenshot.
        """
        with allure.step(step_name):
            allure.attach(self.driver.get_screenshot_as_png(), name=step_name,
                          attachment_type=allure.attachment_type.PNG)
            print(f"Exception occurred: {str(exception)}")
        raise exception

    def capture_screenshot(self, name: str):
        """
        Captures a screenshot and saves it in a designated folder.

        :param name: The name for the screenshot file.
        """
        # Create a folder for the current test run using the current date and time
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        run_folder = os.path.join(self.screenshot_base_dir, current_time)

        # Create the directory if it does not exist
        if not os.path.exists(run_folder):
            os.makedirs(run_folder)

        # Save the screenshot with the provided name
        screenshot_path = os.path.join(run_folder, f"{name}.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

    def assert_text_equal(self, actual_text, expected_text, message=""):
        """
        Compare two text strings for equality, ignoring case and punctuation.

        :param actual_text: The actual text string to compare.
        :param expected_text: The expected text string to compare.
        :param message: Custom error message to display if the comparison fails.
        :return: None
        :raises: AssertionError if the normalized actual and expected texts do not match.
        """
        def normalize(text):
            """
            Normalize text by converting to lowercase, removing leading/trailing whitespace,
            and removing punctuation characters.

            :param text: The text to be normalized.
            :return: Normalized text string.
            """
            return ''.join(char for char in text.strip().lower() if char not in string.punctuation)

        # Normalize both the actual and expected text
        actual = normalize(actual_text)
        expected = normalize(expected_text)
        assert actual == expected, message or f"Expected '{expected}' but got '{actual}'"
