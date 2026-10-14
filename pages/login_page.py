
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class LoginPage:

    URL = "https://www.saucedemo.com/"

    # Locators
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        logger.info("Opening SauceDemo login page")
        self.driver.get(self.URL)

    def enter_username(self, username):
        logger.info("Entering username")
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        ).send_keys(username)

    def enter_password(self, password):
        logger.info("Entering password")
        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        ).send_keys(password)

    def click_login(self):
        logger.info("Clicking login button")
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def get_products_title(self):
        logger.info("Getting products page title")
        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCTS_TITLE)
        ).text

    def get_error_message(self):
        logger.info("Getting login error message")
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text
