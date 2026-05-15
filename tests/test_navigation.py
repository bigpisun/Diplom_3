import allure
from pages.main_page import MainPage
from config import BASE_URL

@allure.feature("Навигация")
class TestNavigation:
    @allure.title("Переход из конструктора в ленту заказов и обратно")
    def test_navigation_constructor_to_feed(self, driver):
        page = MainPage(driver)
        page.wait_for_home_page()
        page.click_order_feed()
        assert "feed" in page.get_current_url()
        
        page.click_constructor()
        assert page.get_current_url() == BASE_URL