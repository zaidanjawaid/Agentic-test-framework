from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.submit = page.get_by_role("button", name="Login")
        self.error = page.get_by_test_id("error")

    def open(self):
        self.page.goto("/")
        return self

    def login(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.submit.click()
