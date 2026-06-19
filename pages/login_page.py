from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.username_field = page.locator("[data-test=\"username\"]")
        self.password_field = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
        self.error_message = page.locator("[data-test=\"error\"]")

    def navigate(self):
        self.navigate_to("")

    def fill_username(self, username: str):
        self.username_field.fill(username)

    def fill_password(self, password: str):
        self.password_field.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def login(self, username: str, password: str):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()

    def verify_error_message(self, message: str):
        expect(self.error_message).to_be_visible()
        expect(self.error_message).to_contain_text(message)
