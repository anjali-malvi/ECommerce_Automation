
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger


class CartPage:
    CART_TITLE = (By.CLASS_NAME, "title")
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_TITLE)
        ).text

    def get_item_name(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_ITEM)
        ).text

    def click_checkout(self):
        logger.info("Clicking checkout")
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
