import os
import time
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

SCREENSHOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "screenshots"))


class TestSauceDemo:
    """Test suite containing automated tests for SauceDemo (Swag Labs)."""

    def test_01_login_success(self, driver):
        """TC01: Verify successful login with valid credentials."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        assert "/inventory.html" in driver.current_url, "User should be redirected to inventory page."
        assert inventory_page.get_title() == "Products", "Page title should be 'Products'."

        screenshot_path = os.path.join(SCREENSHOT_DIR, "tc01_login_success.png")
        login_page.take_screenshot(screenshot_path)

    def test_02_login_locked_out_user(self, driver):
        """TC02: Verify login failure and error message for locked out user."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        error_message = login_page.get_error_message()
        assert "Sorry, this user has been locked out" in error_message, "Expected locked out error message."

        screenshot_path = os.path.join(SCREENSHOT_DIR, "tc02_login_locked_out.png")
        login_page.take_screenshot(screenshot_path)

    def test_03_login_invalid_password(self, driver):
        """TC03: Verify login failure when entering incorrect password."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "wrong_password_123")

        error_message = login_page.get_error_message()
        assert "Username and password do not match" in error_message, "Expected credentials mismatch message."

        screenshot_path = os.path.join(SCREENSHOT_DIR, "tc03_login_invalid_password.png")
        login_page.take_screenshot(screenshot_path)

    def test_04_sort_products_price_low_to_high(self, driver):
        """TC04: Verify sorting products by price from low to high."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.select_sort_option("lohi")
        time.sleep(1)  # allow DOM re-render

        prices = inventory_page.get_all_prices()
        assert prices == sorted(prices), f"Prices should be sorted low to high: {prices}"

        screenshot_path = os.path.join(SCREENSHOT_DIR, "tc04_sort_price_low_to_high.png")
        inventory_page.take_screenshot(screenshot_path)

    def test_05_add_multiple_items_to_cart(self, driver):
        """TC05: Verify adding multiple products to the shopping cart."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bike_light_to_cart()

        badge_count = inventory_page.get_cart_badge_count()
        assert badge_count == 2, f"Expected 2 items in cart badge, got {badge_count}"

        inventory_page.open_cart()
        cart_page = CartPage(driver)
        item_names = cart_page.get_cart_item_names()

        assert "Sauce Labs Backpack" in item_names, "Backpack should be in cart."
        assert "Sauce Labs Bike Light" in item_names, "Bike Light should be in cart."

        screenshot_path = os.path.join(SCREENSHOT_DIR, "tc05_add_to_cart.png")
        cart_page.take_screenshot(screenshot_path)

    def test_06_remove_item_from_cart(self, driver):
        """TC06: Verify removing an item from the cart."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bike_light_to_cart()
        inventory_page.open_cart()

        cart_page = CartPage(driver)
        cart_page.remove_backpack()

        remaining_items = cart_page.get_cart_item_names()
        assert "Sauce Labs Backpack" not in remaining_items, "Backpack should be removed."
        assert len(remaining_items) == 1, "Only 1 item should remain in cart."

        screenshot_path = os.path.join(SCREENSHOT_DIR, "tc06_remove_from_cart.png")
        cart_page.take_screenshot(screenshot_path)

    def test_07_checkout_flow_complete(self, driver):
        """TC07: Verify end-to-end checkout and order placement process."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack_to_cart()
        inventory_page.open_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_information("Tu", "Nguyen", "100000")

        assert "checkout-step-two.html" in driver.current_url, "User should be on overview page."
        checkout_page.click_finish()

        assert "checkout-complete.html" in driver.current_url, "User should reach order completion page."
        header = checkout_page.get_complete_header()
        assert "Thank you for your order!" in header, f"Expected confirmation header, got: {header}"

        screenshot_path = os.path.join(SCREENSHOT_DIR, "tc07_checkout_complete.png")
        checkout_page.take_screenshot(screenshot_path)

    def test_08_logout_success(self, driver):
        """TC08: Verify user can successfully log out of the system."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.logout()
        time.sleep(1)

        assert login_page.is_login_button_displayed(), "Login button should be visible after logout."
        assert driver.current_url == "https://www.saucedemo.com/", "Should be redirected back to login page."

        screenshot_path = os.path.join(SCREENSHOT_DIR, "tc08_logout_success.png")
        login_page.take_screenshot(screenshot_path)
