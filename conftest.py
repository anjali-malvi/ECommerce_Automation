
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    # Slow down browser actions for learning/demo
    options.add_argument("--start-maximized")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)

    yield browser

    browser.quit()
