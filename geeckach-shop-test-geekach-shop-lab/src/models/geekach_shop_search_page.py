import uuid
from src.models.base_page import BasePage
from src.utils.locators import GeekachShopSearchPageLocators


class GeekachShopSearchManager(BasePage):

    def search_product(self, product):
        search_field = self.find_element(GeekachShopSearchPageLocators.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(product)
        return (search_field)

    def click_on_the_buy_button(self):
        return self.find_element(GeekachShopSearchPageLocators.BUY_BUTTON,time=2).click()

    def click_on_the_order_button(self):
        return self.find_element(GeekachShopSearchPageLocators.ORDER_BUTTON,time=2).click()

    def get_product(self):
        product = self.find_element(GeekachShopSearchPageLocators.PRODUCT,time=2)
        return product.text