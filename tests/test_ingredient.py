import allure
import pytest
from pages.main_page import MainPage


@allure.feature("Ингредиенты")
class TestIngredient:

    @allure.title("Клик по ингредиенту открывает модальное окно")
    def test_modal_appears(self, driver):
        page = MainPage(driver)
        page.wait_for_home_page()
        page.close_modal_if_exists()
        page.click_ingredient()
        assert page.is_modal_visible() is True

    @allure.title("Модальное окно закрывается крестиком")
    def test_modal_close(self, driver):
        page = MainPage(driver)
        page.wait_for_home_page()
        page.close_modal_if_exists()
        page.click_ingredient()
        assert page.is_modal_visible() is True
        page.close_modal()
        assert page.is_modal_visible() is False