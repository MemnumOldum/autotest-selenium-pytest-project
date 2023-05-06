from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_items_disappeared(self):
        assert self.is_disappeared(*BasketPageLocators.PRODUCTS_ON_BASKET), \
            "Success message is presented, but should not be"

    def basket_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART_MESSAGE), "Login link is not presented"