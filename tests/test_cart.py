from playwright.sync_api import expect

from config import USERS, PASSWORD
from pages.inventory_page import InventoryPage


def test_cart_badge_counts_items(login_page, page):
    login_page.login(USERS["standard"], PASSWORD)
    inventory = InventoryPage(page)

    inventory.add_to_cart("sauce-labs-backpack")
    expect(inventory.cart_badge).to_have_text("1")

    inventory.add_to_cart("sauce-labs-bike-light")
    expect(inventory.cart_badge).to_have_text("2")
