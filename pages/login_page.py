

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_PAGE_URL = "https://www.saucedemo.com/v1/"
    INPUT_EMAIL = (By.ID,"user-name")
    INPUT_PASSWORD = (By.ID,"password")
    INPUT_LOGIN_BUTTON= (By.ID,"login-button")
    XPATH_ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")
    POP_UP_BUTTON = (By.CLASS_NAME, "bm-burger-button")


    def open_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)


    def verify_url(self):
        assert self.driver.current_url == self.LOGIN_PAGE_URL


    def set_email(self, text):
        self.type(self.INPUT_EMAIL, text)

    def set_password(self, text):
        self.type(self.INPUT_PASSWORD, text)

    def click_login_button(self):
        self.find(self.INPUT_LOGIN_BUTTON).click()

    def verify_login_error_message(self, text):
        assert text in self.find(self.XPATH_ERROR_MESSAGE).text

    def click_pop_up_button(self):
        self.find(self.POP_UP_BUTTON).click()






