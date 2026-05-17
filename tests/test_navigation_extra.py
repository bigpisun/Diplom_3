import pytest
from pages.main_page import MainPage

class TestNavigationExtra:

    def test_password_visibility_toggle_by_eye_button(self, driver):
        page = MainPage(driver)
        # Открываем страницу логина, так как на forgot-password нет поля пароля
        page.open_login_page() 
        page.click_password_eye()
        assert page.is_active_password_input_visible() is True