from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name = page.locator("[data-test=\"firstName\"]")
        self.last_name = page.locator("[data-test=\"lastName\"]")
        self.postal_code = page.locator("[data-test=\"postalCode\"]")
        self.continue_button = page.locator("[data-test=\"continue\"]")
        self.cancel_button = page.locator("[data-test=\"cancel\"]")
        self.error_message = page.locator("[data-test=\"error\"]")

    def input_first_name(self, first_name: str):
        self.first_name.fill(first_name)

    def input_last_name(self, last_name: str):
        self.last_name.fill(last_name)

    def input_postal_code(self, postal_code: str):
        self.postal_code.fill(postal_code)


    def verify_error_message(self, message: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(message)