from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def examination_add_to_basket(self):
        self.add_to_basket()
        self.solve_quiz_and_get_code()

    def add_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        print(product_name, product_price)
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
    
    def compare_name(self):
        name1 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name2 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT).text
        assert name1 == name2, "\n Names don't match.."

    def compare_price(self):
        price1 = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price2 = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ALERT).text
        assert price1 == price2, "\n Price don't match.."
