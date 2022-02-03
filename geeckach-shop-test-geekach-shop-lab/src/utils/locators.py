from selenium.webdriver.common.by import By


class GeekachShopMainPageLocators:
    SEARCH_FIELD = (By.CLASS_NAME, 'search__input')
    SEARCH_BUTTON = (By.CLASS_NAME, 'search__button')


class GeekachShopSearchPageLocators:
    BUY_BUTTON = (By.ID, 'j-buy-button-widget-10895')
    ORDER_BUTTON = (By.CLASS_NAME, 'cart-btnOrder')
    PRODUCT = (By.CLASS_NAME, 'cart-title')


class GeekachShopOrderPageLocators:
    NAME_FIELD = (By.NAME, "Recipient[delivery_name]")
    PHONE_FIELD = (By.NAME, "Recipient[delivery_phone]")
    CITY_FIELD = (By.NAME, "Recipient[delivery_city]")
    MAIL_FIELD = (By.NAME, "Recipient[delivery_email]")
    PRODUCT = (By.CLASS_NAME, 'order-i-title')
