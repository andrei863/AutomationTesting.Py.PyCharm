Python BDD Testing Framework

Overview:
This project aims to implement a Behavior-Driven Development (BDD) testing framework in Python, fostering collaboration among developers, QA engineers by using a common language to describe system behavior.

Features:

Executable Specifications: Write human-readable specifications executable as automated tests using Python's BDD libraries like Behave or pytest-bdd.
Reusability: Encourage reusable test components and scenarios for improved maintainability and scalability.
Reporting and Analytics: Generate comprehensive reports to track test coverage, identify bottlenecks, and measure project health.
Usage:

Writing Specifications: Create feature files using a BDD language such as Gherkin to describe system behavior.

gherkin
Feature: Login Page
  Background: Open login page
    Given Currently I am on the login page

  @smoke
  Scenario: Check if the URL is correct
    Given Currently I am on the login page
    Then The URL of the page is "https://www.saucedemo.com/v1/"
Implementing Step Definitions: Write step definitions executing the test logic.

python
from behave import *

@given(u'Currently I am on the login page')
def step_impl(context):
    context.login_page.open_page()

@then('The URL of the page is "https://www.saucedemo.com/v1/"')
def step_impl(context):
    context.login_page.verify_url()

Executing Tests: Run the test suite to validate the application's behavior against specifications.
behave
Conclusion:
The Python BDD Testing Framework facilitates collaborative and efficient software testing through human-readable specifications, reusable components, and comprehensive reporting. Its adoption empowers teams to ensure software quality and project success.
