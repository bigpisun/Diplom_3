import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators, IngredientModalLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step("Ожидание загрузки главной страницы")
    def wait_for_home_page(self):
        return self.wait_for_element_visibility(MainPageLocators.ORDER_BUTTON)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click(MainPageLocators.INGREDIENT_BUN)

    @allure.step("Проверка видимости модального окна")
    def is_modal_visible(self):
        return self.is_visible(IngredientModalLocators.MODAL)

    @allure.step("Закрыть модальное окно, если оно открыто")
    def close_modal_if_exists(self):
        if self.is_visible(MainPageLocators.CLOSE_MODAL_BUTTON):
            self.click(MainPageLocators.CLOSE_MODAL_BUTTON)
            # Вместо time.sleep используем ожидание исчезновения
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located(MainPageLocators.CLOSE_MODAL_BUTTON)
            )
            
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url