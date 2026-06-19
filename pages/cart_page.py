from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_items = page.locator("[data-test=\"inventory-item\"]")
        self.cart_remove_button = page.locator("[data-test^=\"remove\"]")
        self.checkout_button = page.locator("[data-test=\"checkout\"]")
        self.shopping_cart_badge = page.locator("[data-test=\"shopping-cart-badge\"]")

    def remove_item_from_cart(self):
        self.cart_remove_button.click()

    def item_click(self):
        self.cart_items.locator("[data-test=\"inventory-item-name\"]").click()

    def get_shopping_cart_count(self):
        if not self.shopping_cart_badge.is_visible():
            return 0
        return self.shopping_cart_badge.inner_text()
