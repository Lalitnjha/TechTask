# TechTask

## Project Overview
**TechTask** is an automation framework designed for testing various components of a web or mobile application. This framework is built using Python and leverages different tools and libraries to create robust, scalable, and maintainable test automation solutions.

## Repository Structure
The repository is structured to provide modularity and ease of use when adding new features or tests. Below is a brief overview of each folder and file:

- `pages/` - Contains page object models (POM) for the application under test. Each page of the application has its own Python class.
- `tests/` - Contains all the test scripts for different components of the application. Each test file corresponds to a specific functionality or set of features.
- `utilities/` - Contains utility functions and helper classes to support the test framework, such as logging, configurations, and common methods.
- `conftest.py` - Configuration file for pytest that includes fixtures and other setup information.
- `requirements.txt` - Lists all the dependencies required to run the framework. Make sure to install them using the `pip install -r requirements.txt` command.

## Installation

To set up this project locally, follow these steps:

1. Clone the repository:
   git clone https://github.com/Lalitnjha/TechTask.git

2. Navigate to the project directory:
   cd TechTask
3. Install the required dependencies:
   pip install -r requirements.txt

## Running Tests
To execute the tests, you can use the following command with pytest:
   pytest

You can also customize the test runs by passing additional options. For example, to run tests in a specific module or folder:
   pytest tests/

## Commands to run for Allure reports
   pytest --alluredir=allure-results
   allure generate allure-results -o allure-report --clean
   allure open allure-report










