from selenium.webdriver.common.by import By
from utilities.common_utilities import CommonUtility


class CartPage(CommonUtility):
    def __init__(self, driver):
        """
        Constructor to initialize the CartPage object.

        :param driver: WebDriver instance used for interacting with the web page.
        """
        super().__init__(driver)
        self.driver = driver

    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_DESCRIPTION = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    # Page Actions
    def verify_product_in_cart(self):
        """
        Verifies if there are any products present in the cart.

        :return: True if one or more items are present in the cart, False otherwise.
        """
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items) > 0

    def get_item_description(self):
        """
        Retrieves the description of the first item in the cart.

        :return: Text description of the first item found in the cart.
        """
        return self.find_element(self.ITEM_DESCRIPTION).text

    def click_checkout_button(self):
        """
        Clicks on the checkout button to proceed to the next page in the checkout process.
        """
        self.click_element(self.CHECKOUT_BUTTON)
