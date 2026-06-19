from playwright.sync_api import expect

from pages.checkout_complete_page import CheckOutCompletePage
from pages.checkout_step_two_page import CheckOutStepTwoPage
from pages.order_page import OrderPage
from tests import constant
from tests.conftest import checkout_step_two_page


def test_TC_ORDER_002(order_page: OrderPage):
    order_page.input_last_name(constant.LAST_NAME)
    order_page.input_postal_code(constant.POSTAL_CODE)
    order_page.continue_button.click()

    order_page.verify_error_message(constant.ORDER_FIRST_NAME_EMPTY_ERROR_MESSAGE)


def test_TC_ORDER_003(order_page: OrderPage):
    order_page.input_first_name(constant.FIRST_NAME)
    order_page.input_postal_code(constant.POSTAL_CODE)
    order_page.continue_button.click()

    order_page.verify_error_message(constant.ORDER_LAST_NAME_EMPTY_ERROR_MESSAGE)


def test_TC_ORDER_004(order_page: OrderPage):
    order_page.input_first_name(constant.FIRST_NAME)
    order_page.input_last_name(constant.LAST_NAME)
    order_page.continue_button.click()

    order_page.verify_error_message(constant.ORDER_POSTAL_CODE_EMPTY_ERROR_MESSAGE)


def test_TC_ORDER_005(order_page: OrderPage):
    order_page.input_first_name(constant.FIRST_NAME)
    order_page.input_last_name(constant.LAST_NAME)
    order_page.input_postal_code(constant.POSTAL_CODE)

    order_page.continue_button.click()

    order_page.page.wait_for_url("**/checkout-step-two.html")
    assert order_page.get_url().endswith("/checkout-step-two.html")


def test_TC_ORDER_006(checkout_step_two_page: CheckOutStepTwoPage):
    assert checkout_step_two_page.get_title() == "Checkout: Overview"
    assert checkout_step_two_page.get_name() == constant.EXPECTED_PRODUCTS[0].get("name")
    assert checkout_step_two_page.get_price() == constant.EXPECTED_PRODUCTS[0].get("price")

    checkout_step_two_page.finish_button.click()

    checkout_step_two_page.page.wait_for_url("**/checkout-complete.html")
    assert checkout_step_two_page.get_url().endswith("/checkout-complete.html")
