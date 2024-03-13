from behave import *

@given(u'Currently I am on the login page')
def step_impl(context):
    context.login_page.open_page()

@then('The URL of the page is "https://www.saucedemo.com/v1/"')
def step_impl(context):
    context.login_page.verify_url()

@when('I enter "{text}" email')
def step_impl(context, text):
    context.login_page.set_email(text)

@when('I enter "{text}" password')
def step_impl(context, text):
    context.login_page.set_password(text)

@when('I click the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('I have to see "{text}"')
def step_impl(context, text):
    context.login_page.verify_login_error_message(text)


