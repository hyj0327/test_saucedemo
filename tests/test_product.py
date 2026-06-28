from playwright.sync_api import expect

from pages.products_page import ProductsPage

from tests import constant


def test_TC_PRODUCT_SORT_001(products_page: ProductsPage):
    products_page.sort_by("az")

    names = products_page.get_all_names()

    assert names == sorted(names)


def test_TC_PRODUCT_SORT_002(products_page: ProductsPage):
    products_page.sort_by("za")

    names = products_page.get_all_names()

    assert names == sorted(names, reverse=True)


def test_TC_PRODUCT_SORT_003(products_page: ProductsPage):
    products_page.sort_by("lohi")

    prices = products_page.get_all_price()

    assert prices == sorted(prices)


def test_TC_PRODUCT_SORT_004(products_page: ProductsPage):
    products_page.sort_by("hilo")

    prices = products_page.get_all_price()

    assert prices == sorted(prices, reverse=True)


def test_TC_PRODUCT_DISPLAY_001(products_page: ProductsPage):
    names = products_page.get_all_names()
    assert len(names) == 6

    for i in range(6):
        assert names[i].strip() == constant.EXPECTED_PRODUCTS[i].get("name")


def test_TC_PRODUCT_DISPLAY_002(products_page: ProductsPage):
    images = products_page.get_all_images()

    assert len(images) == 6

    for i in range(6):
        assert images[i].get_attribute("src") == constant.EXPECTED_PRODUCTS[i].get("image_src")


def test_TC_PRODUCT_DISPLAY_003(products_page: ProductsPage):
    prices = products_page.get_all_price()

    assert len(prices) == 6
    for price in prices:
        assert price > 0


def test_TC_PRODUCT_DISPLAY_004(products_page: ProductsPage):
    expect(products_page.inventory_items).to_have_count(6)


def test_TC_PRODUCT_CART_001(products_page: ProductsPage):
    products_page.add_item_to_cart()

    expect(products_page.shopping_cart_badge).to_be_visible()

    assert int(products_page.shopping_cart_badge.inner_text()) == 1


def test_TC_PRODUCT_CART_002(products_page: ProductsPage):
    count = products_page.cart_button.count()

    for _ in range(count):
        products_page.add_item_to_cart()

    assert int(products_page.shopping_cart_badge.inner_text()) == 6


def test_TC_PRODUCT_CART_003(products_page: ProductsPage):
    products_page.add_item_to_cart()

    expect(products_page.shopping_cart_badge).to_be_visible()

    products_page.remove_item_from_cart()

    expect(products_page.shopping_cart_badge).to_be_hidden()


def test_TC_PRODUCT_CART_004(products_page: ProductsPage):
    products_page.shopping_cart_link.click()

    products_page.page.wait_for_url("**/cart.html")
    assert products_page.get_url().endswith("/cart.html")


def test_TC_PRODUCT_DETAIL_001(products_page: ProductsPage):
    products_page.inventory_items.first.locator("[data-test=\"inventory-item-name\"]").click()

    products_page.page.wait_for_url("**/inventory-item.html?id=4")
    assert products_page.get_url().endswith("/inventory-item.html?id=4")
