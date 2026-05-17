import pytest
from pages.main_page import MainPage

class TestNavigation:

    def test_click_constructor_button_opens_constructor(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_order_feed()
        page.click_constructor()
        assert "feed" not in page.get_current_url()

    def test_click_order_feed_button_opens_order_feed(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_order_feed()
        assert "feed" in page.get_current_url()