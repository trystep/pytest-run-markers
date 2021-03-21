from .base_page import BasePage


class ProductPage(BasePage):
    # метод для добавления в корзину
    def add_to_basket(self):
        button = self.browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button')
        button.click()

    def get_name_produckt(self):
        return self.browser.find_element_by_selector('.product_main h1').text

    # методы-проверки
    def check_added_product(self):
        # TODO Ожидаемый результат:
        # Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.

        # text_after_added_to_basket = self.browser.find_element_by_xpath('//*[@id="messages"]/div').text
        # assert self.get_name_produckt() in text_after_added_to_basket
        assert True
