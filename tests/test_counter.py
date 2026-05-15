import allure
import pytest
from pages.main_page import MainPage


@allure.feature("Счётчик ингредиентов")
class TestCounter:

    @allure.title("Счётчик увеличивается после добавления ингредиента")
    def test_counter_increases_after_drag_and_drop(self, driver):
        page = MainPage(driver)
        page.wait_for_home_page()
        initial = page.get_counter_value()
        page.drag_and_drop_ingredient()
        page.wait.until(lambda d: page.get_counter_value() > initial)
        assert page.get_counter_value() > initial