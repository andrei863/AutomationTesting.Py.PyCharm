from behave import *


@given(u'Currently i am on the product page')
def step_impl(context):
    context.login_page.open_page()


@then('The current of the page is "https://www.saucedemo.com/v1/"')
def step_impl(context):
    context.login_page.verify_url()


@given(u'Now i am on the login page')
def step_impl(context):
    context.login_page.open_page()


@given('I am on the login page')
def step_impl(context):
    context.login_page.open_page()


@when('I put "{text}" email')
def step_impl(context, text):
    context.login_page.set_email(text)


@when('I put "{text}" password')
def step_impl(context, text):
    context.login_page.set_password(text)


@when('I access the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('The URL of the product page is "https://www.saucedemo.com/v1/inventory.html"')
def step_impl(context):
    context.product_feature.verify_product_page_url()


# SCENARIUL 3 PENTRU COS

@given('Located on the login page')
def step_impl(context):
    context.login_page.open_page()


@when('I introduce "{text}" email')
def step_impl(context, text):
    context.login_page.set_email(text)


@when('I introduce "{text}" password')
def step_impl(context, text):
    context.login_page.set_password(text)


@when('I press the login button')
def stept_impl(context):
    context.login_page.click_login_button()


@when('The URL of the product page is "https://www.saucedemo.com/v1/inventory.html"')
def step_impl(context):
    context.product_feature.verify_product_page_url()


@when('I click Add to cart')
def step_impl(context):
    context.product_feature.click_add_to_cart()


@then('Cart has "{number}" item in it')
def step_impl(context, number):
    context.product_feature.verify_cart_not_empty(number)

#SCENARIUL 4

@given('Present on the login page')
def step_impl(context):
    context.login_page.open_page()

@when('I push "{text}" email')
def step_impl(context, text):
    context.login_page.set_email(text)

@when('I push "{text}" password')
def step_impl(context, text):
    context.login_page.set_password(text)

@when('I push the login button')
def stept_impl(context):
    context.login_page.click_login_button()

@when(' I navigate to page "https://www.saucedemo.com/v1/inventory.html"')
def step_impl(context):
    context.product_feature.verify_product_page_url()

@when('I push Add to cart')
def step_impl(context):
    context.product_feature.click_add_to_cart()

@when('I navigate to page "https://www.saucedemo.com/v1/cart.html"')
def step_impl(context):
    context.product_feature.verify_cart_not_empty()

@then('I should see no product in the cart')
def step_impl(context):
    context.product_feature.verify_shopping_cart()
