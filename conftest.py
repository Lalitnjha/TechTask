import pytest
from utilities.setup import BrowserSetUp


# This fixture is used to set up and tear down the browser instance for each test function.
# The 'scope' parameter defines the fixture's lifespan, and here it's set to 'function',
# meaning this setup will be executed before and after each test function.
@pytest.fixture(scope="function")
def browser_setup():
    # Create an instance of the BrowserSetUp class, which handles browser initialization.
    setup_instance = BrowserSetUp()
    # Call the setup method to initialize the browser with desired configurations.
    setup_instance.setup()
    # Provide the initialized browser instance to the test function.
    yield setup_instance
    # After the test function execution, call the teardown method to close the browser.
    setup_instance.teardown()
