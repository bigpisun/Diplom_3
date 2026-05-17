import pytest
from pages.main_page import MainPage

class TestIngredient:
    def test_open_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.drag_and_drop_ingredient()
        assert page.is_ingredient_present() is True

    def test_close_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.drag_and_drop_ingredient()
        page.close_modal_if_exists()
        assert page.is_modal_visible() is False