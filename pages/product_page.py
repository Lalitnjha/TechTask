from selenium.webdriver.common.by import By
from utilities.common_utilities import CommonUtility


class ProductListingPage(CommonUtility):
    """
    Page Object Model for the Product Listing Page.
    This class contains locators and methods related to interactions on the product listing page.
    """

    def __init__(self, driver):
        """
        Initializes the ProductListingPage object.

        Args:
            driver: WebDriver instance used for interacting with the page elements.
        """
        super().__init__(driver)
        self.driver = driver

    # Locators
    FIRST_PRODUCT_ADD_BUTTON = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    # Locator for the 'Add to cart' button for the first product in the listing.

    CART_ICON = (By.ID, "shopping_cart_container")

    # Locator for the shopping cart icon in the header.

    # Page Actions
    def add_product_to_cart(self):
        """
        Clicks on the 'Add to cart' button of the first product in the product listing.
        This method is used to add the first product displayed on the page to the cart.
        """
        self.driver.find_element(*self.FIRST_PRODUCT_ADD_BUTTON).click()

    def go_to_cart(self):
        """
        Clicks on the cart icon in the header.
        This method navigates the user to the shopping cart page where they can review their selected products.
        """
        self.driver.find_element(*self.CART_ICON).click()
