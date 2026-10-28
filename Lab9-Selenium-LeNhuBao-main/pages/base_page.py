import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base class for all Page Objects containing common utilities and element actions."""

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def find_visible_element(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def find_elements(self, by, locator):
        return self.wait.until(EC.presence_of_all_elements_located((by, locator)))

    def click(self, by, locator):
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()

    def enter_text(self, by, locator, text):
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        element.clear()
        element.send_keys(text)

    def get_text(self, by, locator):
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        return element.text

    def is_displayed(self, by, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located((by, locator))).is_displayed()
        except Exception:
            return False

    def take_screenshot(self, filepath):
        """Save screenshot to the specified file path."""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        return self.driver.save_screenshot(filepath)
