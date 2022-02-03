import uuid
from src.models.base_page import BasePage
from src.utils.locators import GeekachShopMainPageLocators


class GeekachShopMainManager(BasePage):

    def search_product(self, product):
        search_field = self.find_element(GeekachShopMainPageLocators.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(product)
        return (search_field)

    def click_on_the_search_button(self):
        return self.find_element(GeekachShopMainPageLocators.SEARCH_BUTTON, time=2).click()
