from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):
    def wait_for_home_page(self):
        self.wait_for_page_load()

    def close_modal_if_exists(self):
        try:
            self.click(MainPageLocators.CLOSE_MODAL_BUTTON)
            import time
            time.sleep(0.5)
        except:
            pass

    def is_ingredient_present(self):
        from selenium.common.exceptions import TimeoutException
        try:
            self.wait.until(lambda d: d.find_element(*MainPageLocators.INGREDIENT))
            return True
        except TimeoutException:
            return False

    def drag_and_drop_ingredient(self):
        """Перетаскивает ингредиент в конструктор"""
        ingredient = self.wait.until(lambda d: d.find_element(*MainPageLocators.INGREDIENT))
        constructor = self.wait.until(lambda d: d.find_element(*MainPageLocators.CONSTRUCTOR_AREA))
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, constructor).perform()
        import time
        time.sleep(1)

    def click_constructor(self):
        self.close_modal_if_exists()
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.close_modal_if_exists()
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    def get_counter_value(self):
        text = self.get_text(MainPageLocators.COUNTER)
        return int(text) if text.isdigit() else 0

    def click_order_button(self):
        self.close_modal_if_exists()
        self.click(MainPageLocators.ORDER_BUTTON)

    def is_modal_visible(self):
        from locators.locators import IngredientModalLocators
        return self.is_visible(IngredientModalLocators.MODAL)

    def close_modal(self):
        from locators.locators import IngredientModalLocators
        self.click(IngredientModalLocators.CLOSE_BUTTON)