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


@when('I put right email')
def step_impl(context):
    context.login_page.set_email('standard_user')


@when('I put right password')
def step_impl(context):
    context.login_page.set_password('secret_sauce')


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
def step_impl(context):
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

@given('Located in the login page')
def step_impl(context):
    context.login_page.open_page()

@when('I press the right email')
def step_impl(context):
    context.login_page.set_email('standard_user')

@when('I press  the right password')
def step_impl(context):
    context.login_page.set_password('secret_sauce')

@when('I enter the login button')
def step_impl(context):
    context.login_page.click_login_button()

@when('The product page URL is "https://www.saucedemo.com/v1/inventory.html"')
def step_impl(context):
    context.product_feature.verify_product_page_url()

@when('I click the cart button')
def step_impl(context):
    context.product_feature.click_shopping_cart()

@then('I should see "https://www.saucedemo.com/v1/cart.html"')
def step_impl(context):
    context.product_feature.verify_shopping_cart_page()


#Scenariul 5

@given('Present on the login page')
def step_impl(context):
    context.login_page.open_page()

@when('I write my correct email')
def step_impl(context):
    context.login_page.set_email('problem_user')

@when('I write my correct password')
def step_impl(context):
    context.login_page.set_password('secret_sauce')

@when('I click the login function')
def step_impl(context):
    context.login_page.click_login_button()

@when('The product page URL is correct "https://www.saucedemo.com/v1/inventory.html"')
def step_impl(context):
    context.product_feature.verify_product_page_url()

@when('I press the cart button')
def step_impl(context):
    context.product_feature.click_shopping_cart()

@when('I have to see "https://www.saucedemo.com/v1/cart.html"')
def step_impl(context):
    context.product_feature.verify_shopping_cart_page()

@when('I press the CHECKOUT button')
def stept(context):
    context.product_feature.click_check_out_button()

@then('I should see the Checkout information page "https://www.saucedemo.com/v1/checkout-step-one.html"')
def step_impl(context):
    context.product_feature.verify_checkout_page_url()

#Scenariu 6
@given('I press the login button')
def step_impl(context):
    context.login_page.open_page()

@when('I enter correct username')
def step_impl(context):
    context.login_page.set_email('standard_user')

@when('I enter correct password')
def step_impl(context):
    context.login_page.set_password('secret_sauce')

@when('I click the button')
def step_impl(context):
    context.login_page.click_login_button()

@when('I add product to cart')
def step_impl(context):
    context.product_feature.click_add_to_cart()

@when('I click the cart')
def step_impl(context):
    context.product_feature.click_shopping_cart()

@when('I click checkout button')
def step_impl(context):
    context.product_feature.click_check_out_button()

@when('I enter First Name')
def step_impl(context):
    context.product_feature.set_first_name('Dorian')

@when('I enter Last Name')
def step_impl(context):
    context.product_feature.set_last_name('Ciuca')

@when('I enter zip postal code')
def step_impl(context):
    context.product_feature.set_zip_code('213214')

@when('I click the continue button')
def step_impl(context):
    context.product_feature.press_continue_button()

@when('I click finish button')
def step_impl(context):
    context.product_feature.press_finish_button()

@then('I see "{text}"')
def step_impl(context, text):
    context.product_feature.thank_message(text)

@given('I access the login button')
def step_impl(context):
    context.login_page.open_page()

@when('I introduce the correct email')
def step_impl(context):
    context.login_page.set_email('standard_user')

@when('I introduce the correct password')
def step_impl(context):
    context.login_page.set_password('secret_sauce')

@when('I press the access button')
def step_impl(context):
    context.login_page.click_login_button()

@when('I put the product in to the cart')
def step_impl(context):
    context.product_feature.click_add_to_cart()

@when('I access the cart')
def step_impl(context):
    context.product_feature.click_shopping_cart()

@then('I click the remove from cart button')
def step_impl(context):
    context.product_feature.press_remove_button_from_cart()



