import pytest
from pages.main_page import MainPage

class TestRecovery:
    def test_click_recovery_password_button(self, driver):
        page = MainPage(driver)
        page.open_login_page()
        page.click_recovery_link()
        assert "/forgot-password" in page.get_current_url()