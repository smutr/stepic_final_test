from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):

        assert 'login' in self.browser.current_url.split('/')

    def should_be_login_form(self):

        assert self.browser.find_element(*LoginPageLocators.EMAIL)
        assert self.browser.find_element(*LoginPageLocators.PASSWORD)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице

        assert self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER)
        assert self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER)