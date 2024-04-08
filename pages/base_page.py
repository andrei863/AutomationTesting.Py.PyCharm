import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from browser import Browser


class BasePage(Browser):

    CART_QUANTITY = (By.CLASS_NAME, "shopping_cart_badge")


    def find(self, locator):
        return self.driver.find_element(*locator)

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def verify_cart_not_empty(self, expected):
        expected_text = f'{expected}'
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.text_to_be_present_in_element(self.CART_QUANTITY, expected_text))
        assert expected_text in self.find(self.CART_QUANTITY).text

    def select_dropdown_option_by_text(self, locator, text):
        dropdown_element = self.find(locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(text)




