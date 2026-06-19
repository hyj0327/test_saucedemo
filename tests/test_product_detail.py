from playwright.sync_api import expect

from pages.product_detail_page import ProductDetailPage
from tests import constant


def test_TC_PRODUCT_DETAIL_002(product_detail_page: ProductDetailPage):
    assert product_detail_page.get_name() == constant.EXPECTED_PRODUCTS[0].get("name")


def test_TC_PRODUCT_DETAIL_003(product_detail_page: ProductDetailPage):
    assert product_detail_page.get_price() == constant.EXPECTED_PRODUCTS[0].get("price")


def test_TC_PRODUCT_DETAIL_004(product_detail_page: ProductDetailPage):
    assert product_detail_page.get_image() == constant.EXPECTED_PRODUCTS[0].get("image_src")


def test_TC_PRODUCT_DETAIL_005(product_detail_page: ProductDetailPage):
    assert product_detail_page.get_description() == constant.EXPECTED_PRODUCTS[0].get("description")


def test_TC_PRODUCT_DETAIL_006(product_detail_page: ProductDetailPage):
    product_detail_page.add_item_to_cart()
    expect(product_detail_page.shopping_cart_badge).to_be_visible()

    assert int(product_detail_page.shopping_cart_badge.inner_text()) == 1
