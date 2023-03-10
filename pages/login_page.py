from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print("\nПроверяем <login> в текущей ссылке..")
        assert 'login' in self.browser.current_url, "Cant find word <login> in url"

    def should_be_login_form(self):
        print("\nПроверяем форму логина на login_page..")
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), "LOGIN link is not presented"

    def should_be_register_form(self):
        print("\nПроверяем форму регистрации на login_page..")
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "REGISTRATION link is not presented"
