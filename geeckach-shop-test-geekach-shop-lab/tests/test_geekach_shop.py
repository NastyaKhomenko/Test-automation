import config
import time
import uuid

from src.models.geekach_shop_main_page import GeekachShopMainManager
from src.models.geekach_shop_search_page import GeekachShopSearchManager
from src.models.geekach_shop_order_page import GeekachShopOrderManager


def test_geekach_shop(browser):
    geekach_shop_main_page = GeekachShopMainManager(browser, config.GEEKACH_SHOP_URL)
    geekach_shop_main_page.go_to_site()
    geekach_shop_main_page.search_product(config.PRODUCT)
    time.sleep(3)
    geekach_shop_main_page.click_on_the_search_button()
    geekach_shop_search_page = GeekachShopSearchManager(browser, browser.driver.current_url)
    geekach_shop_search_page.go_to_site()
    geekach_shop_search_page.click_on_the_buy_button()
    product = geekach_shop_search_page.get_product()
    assert config.PRODUCT in product
    geekach_shop_search_page.click_on_the_order_button()
    geekach_shop_order_page = GeekachShopOrderManager(browser, browser.driver.current_url)
    geekach_shop_order_page.go_to_site()
    product = geekach_shop_order_page.get_product()
    assert config.PRODUCT in product
    geekach_shop_order_page.enter_order_data(config.NAME, config.PHONE, config.CITY, config.MAIL)
    time.sleep(3)
