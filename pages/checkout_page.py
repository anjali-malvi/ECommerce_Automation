
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger


class CheckoutPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUMMARY_TITLE = (By.CLASS_NAME, "title")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_customer_details(self, first_name, last_name, postal_code):
        logger.info("Entering checkout customer details")

        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)

        self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        ).send_keys(last_name)

        self.wait.until(
            EC.visibility_of_element_located(self.POSTAL_CODE)
        ).send_keys(postal_code)

    def click_continue(self):
        logger.info("Continuing to checkout overview")
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def get_summary_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUMMARY_TITLE)
        ).text

    def click_finish(self):
        logger.info("Finishing order")
        self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        ).click()

    def get_complete_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.COMPLETE_HEADER)
        ).text

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text
