from utilities.common_utilities import CommonUtility
from selenium.webdriver.common.by import By


class ConfirmationPage(CommonUtility):
    # Locator for the 'Finish' button on the confirmation page
    FINISH_BUTTON = (By.ID, "finish")

    # Locator for the order confirmation message text
    ORDER_CONFIRMATION_TEXT = (By.CSS_SELECTOR, ".complete-header")

    def click_finish_button(self):
        """
        Clicks the 'Finish' button to complete the order process.
        This method utilizes the click_element function from the CommonUtility class,
        which abstracts the Selenium click action for better reusability and error handling.
        """
        self.click_element(self.FINISH_BUTTON)

    def get_order_confirmation(self):
        """
        Retrieves the text of the order confirmation message displayed on the confirmation page.
        This method uses the find_element function from the CommonUtility class to locate
        the order confirmation text element and returns its text content.

        Returns:
            str: The text content of the order confirmation message.
        """
        return self.find_element(self.ORDER_CONFIRMATION_TEXT).text
