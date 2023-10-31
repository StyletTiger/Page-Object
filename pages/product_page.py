from pages.locators import ProductPageLocators, BasePageLocators
from .base_page import BasePage

class ProductPage(BasePage):

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_product_added_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE), "Product added message is not present"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert product_name == message, "Product name in message does not match the product added"

    def should_be_basket_total_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), "Basket total message is not present"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
