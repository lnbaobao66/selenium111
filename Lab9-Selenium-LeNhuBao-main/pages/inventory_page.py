from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object for Products Inventory Page."""

    # Locators
    PAGE_TITLE = (By.CSS_SELECTOR, "span.title")
    SORT_SELECT = (By.CSS_SELECTOR, "select.product_sort_container")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    CART_LINK = (By.CSS_SELECTOR, "a.shopping_cart_link")
    CART_BADGE = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    # Product Add/Remove Buttons
    ADD_BACKPACK_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT_BTN = (By.ID, "add-to-cart-sauce-labs-bike-light")
    REMOVE_BACKPACK_BTN = (By.ID, "remove-sauce-labs-backpack")

    def get_title(self):
        return self.get_text(*self.PAGE_TITLE)

    def select_sort_option(self, value):
        """Sort options: 'az', 'za', 'lohi', 'hilo'"""
        select_elem = self.find_element(*self.SORT_SELECT)
        select = Select(select_elem)
        select.select_by_value(value)

    def get_all_prices(self):
        elements = self.find_elements(*self.ITEM_PRICES)
        return [float(e.text.replace("$", "").strip()) for e in elements]

    def get_all_item_names(self):
        elements = self.find_elements(*self.ITEM_NAMES)
        return [e.text.strip() for e in elements]

    def add_backpack_to_cart(self):
        self.click(*self.ADD_BACKPACK_BTN)

    def add_bike_light_to_cart(self):
        self.click(*self.ADD_BIKE_LIGHT_BTN)

    def remove_backpack(self):
        self.click(*self.REMOVE_BACKPACK_BTN)

    def get_cart_badge_count(self):
        if self.is_displayed(*self.CART_BADGE):
            return int(self.get_text(*self.CART_BADGE))
        return 0

    def open_cart(self):
        self.click(*self.CART_LINK)

    def logout(self):
        self.click(*self.MENU_BUTTON)
        self.click(*self.LOGOUT_LINK)
