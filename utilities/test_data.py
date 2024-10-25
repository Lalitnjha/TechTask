class TestData:
    # Base URL for the application under test
    BASE_URL = "https://www.saucedemo.com/"

    # Valid user credentials for logging into the application
    VALID_USERNAME = "standard_user"
    VALID_PASSWORD = "secret_sauce"

    # Invalid user credentials for testing negative login scenarios
    INVALID_USERNAME = "invalid_user"
    INVALID_PASSWORD = "invalid_password"

    # User information for filling out forms at Checkout: Your Information page
    FIRST_NAME = "Lalit"
    LAST_NAME = "J"
    POSTAL_CODE = "847423"

    # Expected error message when login fails due to incorrect credentials
    LOGIN_ERROR_MESSAGE = "Epic sadface: Username and password do not match any user in this service"
