import re

import pytest
from playwright.sync_api import expect

from config import USERS, PASSWORD


@pytest.mark.smoke
def test_valid_login(login_page, page):
    login_page.login(USERS["standard"], PASSWORD)
    expect(page).to_have_url(re.compile("inventory"))


@pytest.mark.parametrize("user, pwd, message", [
    (USERS["locked"], PASSWORD, "locked out"),
    (USERS["standard"], "wrong", "do not match"),
    ("", PASSWORD, "Username is required"),
])
def test_login_errors(login_page, user, pwd, message):
    login_page.login(user, pwd)
    expect(login_page.error).to_contain_text(message)
