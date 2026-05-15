import allure
import pytest
from pages.main_page import MainPage

@allure.feature("Модальное окно ингредиента")
class TestIngredient:
    @allure.title("Клик по ингредиенту открывает модальное окно")
    def test_modal_appears(self, driver):
        page = MainPage(driver)
        page.wait_for_home_page()
        page.click_ingredient()
        assert page.is_modal_visible() is True, "Модальное окно не появилось"