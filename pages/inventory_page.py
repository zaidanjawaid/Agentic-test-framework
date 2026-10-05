from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.get_by_test_id("title")
        self.cart_badge = page.get_by_test_id("shopping-cart-badge")

    def add_to_cart(self, product_slug: str):
        # e.g. "sauce-labs-backpack" -> data-test="add-to-cart-sauce-labs-backpack"
        self.page.get_by_test_id(f"add-to-cart-{product_slug}").click()
