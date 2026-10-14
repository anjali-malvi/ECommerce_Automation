
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger


class ProductPage:
    BACKPACK_ADD_BUTTON = (
        By.ID, "add-to-cart-sauce-labs-backpack"
    )
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCTS_TITLE)
        ).text

    def add_backpack_to_cart(self):
        logger.info("Adding backpack to cart")
        self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK_ADD_BUTTON)
        ).click()

    def get_cart_count(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        ).text

    def open_cart(self):
        logger.info("Opening shopping cart")
        self.wait.until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()
