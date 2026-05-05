import time
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"


def test_login_success(driver):
    login = LoginPage(driver)
    login.open()
    login.login(VALID_USER, VALID_PASSWORD)

    inventory = InventoryPage(driver)
    assert inventory.is_loaded()


def test_login_invalid_credentials(driver):
    login = LoginPage(driver)
    login.open()
    login.login("wrong_user", "wrong_pass")

    assert "Epic sadface" in login.get_error_message()


def test_add_product_to_cart(driver):
    login = LoginPage(driver)
    login.open()
    login.login(VALID_USER, VALID_PASSWORD)
    
    inventory = InventoryPage(driver)
    inventory.is_loaded()
    inventory.add_product_to_cart(0)

    assert inventory.get_cart_count() == 1


def test_e2e_purchase(driver):
    """Fluxo completo: login → adicionar produtos → checkout → confirmação."""
    login = LoginPage(driver)
    login.open()
    login.login(VALID_USER, VALID_PASSWORD)

    inventory = InventoryPage(driver)
    inventory.is_loaded()
    time.sleep(1)

    inventory.add_product_to_cart(0)
    time.sleep(1)  

    inventory.add_product_to_cart(1)
    time.sleep(1)  
    assert inventory.get_cart_count() == 2
    inventory.go_to_cart()
    cart = CartPage(driver)
    assert len(cart.get_cart_items()) == 2
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_info("João", "Silva", "50000-000")
    checkout.finish_order()

    assert checkout.get_confirmation_header() == "Thank you for your order!"
