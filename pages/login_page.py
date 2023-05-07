from .base_page import BasePage
from .locators import LoginPageLocators
import time


# класс LoginPage - наследник класса BasePage
# (класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка)
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, 'It is not login page'
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        email = str(time.time()) + "@fakemail.org"
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        password = str(time.time())
        password_input.send_keys(password)
        password_confirm = self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASSWORD)
        password_confirm.send_keys(password)
        confirm_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        confirm_button.click()


