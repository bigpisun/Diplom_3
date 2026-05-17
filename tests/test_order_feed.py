import pytest
from pages.main_page import MainPage

class TestOrderFeed:

    def test_open_order_modal_details(self, driver):
        page = MainPage(driver)
        page.open_feed_page()
        page.click_first_order()
        assert page.is_order_modal_visible() is True