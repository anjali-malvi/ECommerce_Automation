
import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert login_page.get_products_title() == "Products"


@pytest.mark.regression
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.enter_username("invalid_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    error = login_page.get_error_message()

    assert "Username and password do not match" in error



@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("invalid_user", "wrong_password", "Username and password do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ],
)
def test_login_validation_messages(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    error = login_page.get_error_message()

    assert expected_error in error

