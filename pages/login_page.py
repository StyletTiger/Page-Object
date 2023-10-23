from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        # реализуйте проверку на корректный url адрес
        assert "login" in current_url, f"Expected 'login' in URL, but got: {current_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_ADRES), "Элемент не найден на странице"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS), "Элемент не найден на странице"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_ADRES), "Элемент не найден на странице"
        assert self.is_element_present(*LoginPageLocators.REG_PASS1), "Элемент не найден на странице"
        assert self.is_element_present(*LoginPageLocators.REG_PASS2), "Элемент не найден на странице"