from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "div > input[name='registration-email']")
    REG_PASSWORD = (By.CSS_SELECTOR, "div > input[name='registration-password1']")
    REG_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "div > input[name='registration-password2']")
    REG_BUTTON = (By.CSS_SELECTOR, "form > button[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "form[id='add_to_basket_form'] > button[type='submit']")
    NAME_PRODUCT = (By.CSS_SELECTOR, 'div[class="col-sm-6 product_main"] > h1')
    PRODUCT_IN_CART_MESSAGE = (By.CSS_SELECTOR, "div[class='alertinner ']")
    CART_PRICE = (By.CSS_SELECTOR, "div[class='alertinner '] > p > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div[class="col-sm-6 product_main"] > p[class="price_color"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:first-child")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, 'span[class="btn-group"] > a[class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    PRODUCTS_ON_BASKET = (By.CSS_SELECTOR, 'div[class="basket-items"]')
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, 'div[id="content_inner"]')


