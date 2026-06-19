from playwright.sync_api import expect

from pages.cart_page import CartPage


def test_TC_PRODUCT_CART_005(cart_page: CartPage):
    cart_page.remove_item_from_cart()

    expect(cart_page.shopping_cart_badge).to_be_hidden()


def test_TC_PRODUCT_CART_006(cart_page: CartPage):
    cart_page.item_click()

    cart_page.page.wait_for_url("**/inventory-item.html?id=4")
    assert cart_page.get_url().endswith("/inventory-item.html?id=4")


