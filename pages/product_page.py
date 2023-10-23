from pages.locators import ProductPageLocators


class ProductPage():
    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()








# проверки на ожидаемый результат: