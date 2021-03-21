from pages.base_page import BasePage
from pages.product_page import ProductPage


# pytest -vs --language=en test_product_page.py

# Открываем страницу товара (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear).
# Обратите внимание, что в ссылке есть параметр "?promo=newYear". Не теряйте его в авто-тесте, чтобы получить проверочный код.
# Нажимаем на кнопку "Добавить в корзину".
# *Посчитать результат математического выражения и ввести ответ.
#
# Ожидаемый результат:
# Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
# Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.check_added_product()
    page.solve_quiz_and_get_code()
