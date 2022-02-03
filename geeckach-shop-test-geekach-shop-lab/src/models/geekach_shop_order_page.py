import uuid
from src.models.base_page import BasePage
from src.utils.locators import GeekachShopOrderPageLocators


class GeekachShopOrderManager(BasePage):
    def get_product(self):
        product = self.find_element(GeekachShopOrderPageLocators.PRODUCT, time=2)
        return product.text

    def enter_order_data(self, name, phone, city, mail):
        name_field = self.find_element(GeekachShopOrderPageLocators.NAME_FIELD)
        name_field.click()
        name_field.send_keys(name)
        phone_field = self.find_element(GeekachShopOrderPageLocators.PHONE_FIELD)
        phone_field.click()
        phone_field.send_keys(phone)
        city_field = self.find_element(GeekachShopOrderPageLocators.CITY_FIELD)
        city_field.click()
        city_field.send_keys(city)
        mail_field = self.find_element(GeekachShopOrderPageLocators.MAIL_FIELD)
        mail_field.click()
        mail_field.send_keys(mail)
        return (name_field, phone_field, city_field, mail_field)