from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object for Cart Page."""

    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    REMOVE_BACKPACK_BTN = (By.ID, "remove-sauce-labs-backpack")
    CHECKOUT_BTN = (By.ID, "checkout")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")

    def get_cart_item_names(self):
        try:
            elements = self.find_elements(*self.ITEM_NAMES)
            return [e.text.strip() for e in elements]
        except Exception:
            return []

    def get_cart_items_count(self):
        try:
            return len(self.find_elements(*self.CART_ITEMS))
        except Exception:
            return 0

    def remove_backpack(self):
        self.click(*self.REMOVE_BACKPACK_BTN)

    def click_checkout(self):
        self.click(*self.CHECKOUT_BTN)
