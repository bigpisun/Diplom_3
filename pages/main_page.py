from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators.locators import MainPageLocators, IngredientModalLocators


class MainPage(BasePage):
    def wait_for_home_page(self):
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    def close_modal_if_exists(self):
        try:
            self.click(MainPageLocators.CLOSE_MODAL_BUTTON)
        except:
            pass

    def is_ingredient_present(self):
        try:
            self.wait.until(lambda d: d.find_element(*MainPageLocators.INGREDIENT))
            return True
        except TimeoutException:
            return False

    def drag_and_drop_ingredient(self):
        ingredient = self.wait.until(lambda d: d.find_element(*MainPageLocators.INGREDIENT))
        constructor = self.wait.until(lambda d: d.find_element(*MainPageLocators.CONSTRUCTOR_AREA))
        ActionChains(self.driver).drag_and_drop(ingredient, constructor).perform()

    def click_constructor(self):
        self.close_modal_if_exists()
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.close_modal_if_exists()
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        self.close_modal_if_exists()
        self.click(MainPageLocators.INGREDIENT)

    def get_counter_value(self):
        text = self.get_text(MainPageLocators.COUNTER)
        return int(text) if text.isdigit() else 0

    def click_order_button(self):
        self.close_modal_if_exists()
        self.click(MainPageLocators.ORDER_BUTTON)

    def is_modal_visible(self):
        return self.is_visible(IngredientModalLocators.MODAL)

    def close_modal(self):
        self.click(IngredientModalLocators.CLOSE_BUTTON)

    def get_current_url(self):
        return self.driver.current_url