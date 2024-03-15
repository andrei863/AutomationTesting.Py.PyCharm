from browser import Browser
from pages.login_page import LoginPage
from pages.product_feature import ProductPage



def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.product_feature = ProductPage()


def after_all(context):
    context.browser.close()