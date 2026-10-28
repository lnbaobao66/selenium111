from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page Object for Checkout process (Information, Overview, Complete)."""

    # Step One Locators
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    # Step Two Locators
    SUBTOTAL_LABEL = (By.CSS_SELECTOR, ".summary_subtotal_label")
    FINISH_BTN = (By.ID, "finish")

    # Complete Locators
    COMPLETE_HEADER = (By.CSS_SELECTOR, "h2.complete-header")
    BACK_HOME_BTN = (By.ID, "back-to-products")

    def fill_information(self, first_name, last_name, postal_code):
        self.enter_text(*self.FIRST_NAME_INPUT, first_name)
        self.enter_text(*self.LAST_NAME_INPUT, last_name)
        self.enter_text(*self.POSTAL_CODE_INPUT, postal_code)
        self.click(*self.CONTINUE_BTN)

    def get_subtotal(self):
        return self.get_text(*self.SUBTOTAL_LABEL)

    def click_finish(self):
        self.click(*self.FINISH_BTN)

    def get_complete_header(self):
        return self.get_text(*self.COMPLETE_HEADER)
