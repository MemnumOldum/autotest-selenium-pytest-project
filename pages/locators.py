from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "form[id='add_to_basket_form'] > button[type='submit']")
    NAME_PRODUCT = (By.CSS_SELECTOR, 'div[class="col-sm-6 product_main"] > h1')
    PRODUCT_IN_CART_MESSAGE = (By.CSS_SELECTOR, "div[class='alertinner ']")
    CART_PRICE = (By.CSS_SELECTOR, "div[class='alertinner '] > p > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div[class="col-sm-6 product_main"] > p[class="price_color"]')
