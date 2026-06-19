from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckOutCompletePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.locator("[data-test=\"title\"]")
        self.back_home_button = page.locator("[data-test=\"back-to-products\"]")

