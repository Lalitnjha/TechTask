from selenium.webdriver.common.by import By
from utilities.common_utilities import CommonUtility


class CheckoutPage(CommonUtility):
    # Locators for the checkout page elements
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def enter_checkout_information(self, first_name, last_name, postal_code):
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.POSTAL_CODE, postal_code)

    def click_continue_button(self):
        self.click_element(self.CONTINUE_BUTTON)
