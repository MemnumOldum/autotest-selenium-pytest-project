from .base_page import BasePage
from .locators import ProductPageLocators


# класс ProductPage - наследник класса BasePage
# (класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка)
# Методы класса вызываются в тесте test_guest_can_add_product_to_basket из файла test_product_page.py:
# def add_to_cart - добавляет продукт в корзину
# def product_in_cart - проверяет что в сообщении о добавлении товара содержится корректное название этого товара
# def cart_price - проверяет что стоимость корзины, после добавления равна стоимости товара
class ProductPage(BasePage):
    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def product_in_cart(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        element = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_CART_MESSAGE)
        assert (product_name.text + ' has been added to your basket.') == element.text, 'No message about adding item to cart'

    def cart_price(self):
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert cart_price.text == product_price.text, 'The price of the product differs from the amount in the cart'




