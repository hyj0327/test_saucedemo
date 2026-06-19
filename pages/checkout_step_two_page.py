import re

from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckOutStepTwoPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.locator("[data-test=\"title\"]")
        self.cart_item = page.locator("[data-test=\"inventory-item\"]")
        self.item_total = page.locator("[data-test=\"subtotal-label\"]")
        self.tax = page.locator("[data-test=\"tax-label\"]")
        self.total = page.locator("[data-test=\"total-label\"]")
        self.cancel_button = page.locator("[data-test=\"cancel\"]")
        self.finish_button = page.locator("[data-test=\"finish\"]")

    def get_title(self):
        return self.title.inner_text()

    def get_price(self):
        price = self.item_total.inner_text()

        match = re.search(r"\$(\d+\.\d+)", price)

        return float(match.group(1))

    def get_name(self):
        name = self.cart_item.locator("[data-test=\"inventory-item-name\"]").inner_text()

        return name
