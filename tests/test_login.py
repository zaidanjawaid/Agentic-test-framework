import re

import pytest
from playwright.sync_api import Page, expect

URL = "https://www.saucedemo.com/"


# Live coding 3: first UI test
def test_valid_login(page: Page):
    page.goto(URL)
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(re.compile("inventory"))
    expect(page.get_by_text("Products")).to_be_visible()


# YOUR TURN (core): the locked-out user
def test_locked_out_user(page: Page):
    page.goto(URL)
    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page.locator('[data-test="error"]')).to_contain_text("locked out")


# YOUR TURN (stretch): one test, many users.
# Note the wrong password in the last row - without it there is no error!
@pytest.mark.parametrize("user, password, message", [
    ("locked_out_user", "secret_sauce", "locked out"),
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "wrong", "do not match"),
])
def test_login_error(page: Page, user, password, message):
    page.goto(URL)
    page.get_by_placeholder("Username").fill(user)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()

    error = page.locator('[data-test="error"]')
    expect(error).to_contain_text(message)
