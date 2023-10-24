from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "div.alert-info p strong")
