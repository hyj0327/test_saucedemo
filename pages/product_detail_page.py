from playwright.sync_api import Page

from pages.base_page import BasePage


class ProductDetailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.product_name = page.locator("[data-test=\"inventory-item-name\"]")
        self.product_description = page.locator("[data-test=\"inventory-item-desc\"]")
        self.product_image = page.locator(".inventory_details_img")
        self.product_price = page.locator("[data-test=\"inventory-item-price\"]")
        self.cart_button = page.locator("[data-test^=\"add-to-cart\"]")
        self.cart_remove_button = page.locator("[data-test^=\"remove\"]")
        self.shopping_cart_badge = page.locator("[data-test=\"shopping-cart-badge\"]")
        self.shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")

    def get_price(self):
        price = self.product_price.inner_text()

        return float(price.replace("$", ""))

    def get_name(self):
        name = self.product_name.inner_text()

        return name

    def get_description(self):
        description = self.product_description.inner_text()

        return description

    def get_image(self):
        image = self.product_image.get_attribute("src")

        return image

    def add_item_to_cart(self):
        self.cart_button.click()

    def remove_item_from_cart(self):
        self.cart_remove_button.click()
