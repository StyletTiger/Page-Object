from .base_page import BasePage
from .locators import BasePageLocators

class MainPage(BasePage):
    def go_to_basket_from_home_page(self):
        go_to_basket = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        go_to_basket.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"