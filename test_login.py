import pytest
from utilities.test_base import TestBase
from pages.login_page import LoginPage

class TestLogin(TestBase):
    @pytest.mark.parametrize("username,password", [
        ("user1", "pass1"),
        ("user2", "pass2")
    ])
    def test_valid_login(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        assert login_page.is_logged_in(), "Login failed"

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("invalid", "invalid")
        assert login_page.get_error_message() == "Invalid credentials"