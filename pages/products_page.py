from playwright.sync_api import Page

from pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.page_title = page.locator("[data-test=\"title\"]")
        self.burger_menu = page.locator("#react-burger-menu-btn")
        self.inventory_items = page.locator("[data-test=\"inventory-item\"]")
        self.shopping_cart_badge = page.locator("[data-test=\"shopping-cart-badge\"]")
        self.shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")
        self.sort_dropdown = page.locator("[data-test=\"product-sort-container\"]")
        self.cart_button = page.locator("[data-test^=\"add-to-cart\"]")
        self.cart_remove_button = page.locator("[data-test^=\"remove\"]")
        self.logout_button = page.locator("[data-test=\"logout-sidebar-link\"]")

    def get_inventory_items_count(self):
        return self.inventory_items.count()

    def get_shopping_cart_count(self):
        if not self.shopping_cart_badge.is_visible():
            return 0
        return self.shopping_cart_badge.inner_text()

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)

    def get_all_names(self):
        return self.inventory_items.locator("[data-test=\"inventory-item-name\"]").all_inner_texts()

    def get_all_price(self):
        prices = self.inventory_items.locator("[data-test=\"inventory-item-price\"]").all_inner_texts()

        return [float(p.replace("$", "")) for p in prices]

    def get_all_images(self):
        images = self.inventory_items.locator(".inventory_item_img img")

        return images.all()

    def add_item_to_cart(self):
        self.cart_button.first.click()

    def remove_item_from_cart(self):
        self.cart_remove_button.first.click()

    def click_item(self, index: int):
        self.inventory_items.nth(index).locator("[data-test=\"inventory-item-name\"]").click()
