import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckOutCompletePage
from pages.checkout_step_two_page import CheckOutStepTwoPage
from pages.login_page import LoginPage
from pages.order_page import OrderPage
from pages.product_detail_page import ProductDetailPage
from pages.products_page import ProductsPage
from tests import constant


@pytest.fixture()
def login_page(page: Page):
    page.goto(constant.BASE_URL)
    return LoginPage(page)


@pytest.fixture(params=["standard_user", "problem_user"])
def logged_in_page(request, login_page: LoginPage):
    login_page.login(request.param, constant.PASSWORD)

    return login_page.page


@pytest.fixture()
def products_page(logged_in_page: Page):
    return ProductsPage(logged_in_page)


@pytest.fixture()
def product_detail_page(products_page: ProductsPage):
    products_page.click_item(0)
    return ProductDetailPage(products_page.page)


@pytest.fixture()
def cart_page(products_page: ProductsPage):
    products_page.add_item_to_cart()
    products_page.shopping_cart_link.click()

    return CartPage(products_page.page)


@pytest.fixture()
def order_page(cart_page: CartPage):
    cart_page.checkout_button.click()
    return OrderPage(cart_page.page)


@pytest.fixture()
def checkout_step_two_page(order_page: OrderPage):
    order_page.input_first_name(constant.FIRST_NAME)
    order_page.input_last_name(constant.LAST_NAME)
    order_page.input_postal_code(constant.POSTAL_CODE)
    order_page.continue_button.click()

    return CheckOutStepTwoPage(order_page.page)


@pytest.fixture()
def checkout_complete_page(checkout_step_two_page: CheckOutStepTwoPage):
    checkout_step_two_page.finish_button.click()

    return CheckOutCompletePage(checkout_step_two_page.page)
