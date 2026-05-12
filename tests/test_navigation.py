import allure
from pages.main_page import MainPage


@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Переход на страницу Конструктор")
    def test_constructor_click(self, driver):
        page = MainPage(driver)
        page.wait_for_home_page()
        page.click_order_feed()
        page.click_constructor()
        assert page.get_current_url() == "https://stellarburgers.education-services.ru/"

    @allure.title("Переход на страницу Лента заказов")
    def test_order_feed_click(self, driver):
        page = MainPage(driver)
        page.wait_for_home_page()
        page.click_order_feed()
        assert "feed" in page.get_current_url()