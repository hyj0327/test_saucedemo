from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from tests import constant


def test_login_page_loads(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    expect(page).to_have_title("Swag Labs")


def test_TC_LOGIN_001(login_page: LoginPage):
    login_page.login("standard_user", constant.PASSWORD)

    login_page.page.wait_for_url("**/inventory.html")
    assert login_page.get_url().endswith("/inventory.html")


def test_TC_LOGIN_002(login_page: LoginPage):
    login_page.login("", constant.PASSWORD)
    login_page.verify_error_message(constant.EMPTY_USERNAME_ERROR_MESSAGE)


def test_TC_LOGIN_003(login_page: LoginPage):
    login_page.login("standard_user", "")
    login_page.verify_error_message(constant.EMPTY_PASSWORD_ERROR_MESSAGE)


def test_TC_LOGIN_004(login_page: LoginPage):
    login_page.login("", "")
    login_page.verify_error_message(constant.EMPTY_USERNAME_ERROR_MESSAGE)


def test_TC_LOGIN_005(login_page: LoginPage):
    login_page.login("standard_user", "wrong_password")
    login_page.verify_error_message(constant.WRONG_USERNAME_PASSWORD_ERROR_MESSAGE)


def test_TC_LOGIN_006(login_page: LoginPage):
    login_page.login("STANDARD_USER", constant.PASSWORD)
    login_page.verify_error_message(constant.WRONG_USERNAME_PASSWORD_ERROR_MESSAGE)


def test_TC_LOGIN_007(login_page: LoginPage):
    login_page.login("'OR 1=1'", constant.PASSWORD)
    login_page.verify_error_message(constant.WRONG_USERNAME_PASSWORD_ERROR_MESSAGE)


def test_TC_LOGIN_008(login_page: LoginPage):
    login_page.login("problem_user", constant.PASSWORD)
    login_page.page.wait_for_url("**/inventory.html")
    assert login_page.get_url().endswith("/inventory.html")


def test_TC_LOGIN_009(login_page: LoginPage):
    login_page.login("locked_out_user", constant.PASSWORD)
    login_page.verify_error_message(constant.LOCK_ERROR_MESSAGE)
