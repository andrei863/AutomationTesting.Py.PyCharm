
from selenium.webdriver.common.by import By


from browser import Browser


class BasePage(Browser):

    CART_QUANTITY = (By.CLASS_NAME, "fa-layers-counter shopping_cart_badge")

    def find(self, locator):
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

