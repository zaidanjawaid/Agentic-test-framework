import pytest
from pages.login_page import LoginPage


@pytest.fixture(scope="session", autouse=True)
def use_data_test(playwright):
    # saucedemo uses data-test="...", Playwright's default is data-testid
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture
def login_page(page):
    return LoginPage(page).open()
