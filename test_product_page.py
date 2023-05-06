# Открываем страницу товара (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear).
# Обратите внимание, что в ссылке есть параметр "?promo=newYear". Не теряйте его в авто-тесте, чтобы получить проверочный
# код.
# Нажимаем на кнопку "Добавить в корзину".
# *Посчитать результат математического выражения и ввести ответ. Используйте для этого метод solve_quiz_and_get_code(),
# который приведен ниже. Например, можете добавить его в класс BasePage, чтобы использовать его на любой странице.
# Этот метод нужен только для проверки того, что вы написали тест на Selenium. После этого вы получите код, который
# нужно ввести в качестве ответа на данное задание. Код будет выведен в консоли интерпретатора, в котором вы запускаете
# тест. Не забудьте в конце теста добавить проверки на ожидаемый результат.

# Попробуйте запустить автотест, который мы написали на предыдущем шаге, на странице
# http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019.
#
# Чтобы тест был независимым от контента:
#
# Измените методы проверки таким образом, чтобы они принимали как аргумент название товара и цену товара.
# Сделайте метод, который вытаскивает из элемента текст-название товара и возвращает его.
# Сделайте такой же метод для цены.
# Теперь проверяйте, что название товара в сообщении совпадает с заголовком товара.

# К счастью, нам не придется менять наш тест, чтобы проверить изменения в коде. Мы просто запустим всё тот же тест на
# странице http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/ с параметризацией. Вам нужно определить,
# при каком значении параметра promo автотест упадет. Для этого проверьте результат работы PyTest и найдите url, на
# котором произошла ошибка. Значение параметра может изменяться от offer0 до offer9.
# После того как вы обнаружили баг, учитывая что чинить его не собираются, лучше всего пометить падающий тест как
# xfail или skip.

from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
                                               "?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    browser.implicitly_wait(2)
    page.solve_quiz_and_get_code()
    browser.implicitly_wait(10)
    page.product_in_cart()
    page.cart_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/studyguide-for-counter-hack-reloaded_205/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/studyguide-for-counter-hack-reloaded_205/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/studyguide-for-counter-hack-reloaded_205/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message_disappeared()

