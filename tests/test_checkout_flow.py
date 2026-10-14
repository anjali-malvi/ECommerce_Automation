
import pytest
import time

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
@pytest.mark.regression
def test_complete_checkout_flow(driver):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Step 2: Verify products page
    product_page = ProductPage(driver)
    assert product_page.get_title() == "Products"

    # Step 3: Add backpack to cart
    product_page.add_backpack_to_cart()
    assert product_page.get_cart_count() == "1"

    # Step 4: Open cart and verify product
    product_page.open_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_title() == "Your Cart"
    assert cart_page.get_item_name() == "Sauce Labs Backpack"

    # Step 5: Start checkout
    cart_page.click_checkout()

    # Step 6: Enter customer details
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_customer_details(
        "Anjali", "Tester", "452001"
    )
    checkout_page.click_continue()

    # Step 7: Verify checkout overview
    assert checkout_page.get_summary_title() == "Checkout: Overview"

    # Step 8: Complete order
    checkout_page.click_finish()
    assert checkout_page.get_complete_message() == "Thank you for your order!"
