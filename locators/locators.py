from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@href, '/')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@href, 'feed')]")
    INGREDIENT = (By.XPATH, "(//*[contains(@class, 'BurgerIngredient')])[1]")
    CONSTRUCTOR_AREA = (By.XPATH, "//*[contains(@class, 'constructor')]")
    COUNTER = (By.XPATH, "(//*[contains(@class, 'counter')])[1]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'close')]")


class IngredientModalLocators:
    MODAL = (By.XPATH, "//*[contains(@class, 'Modal')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'close')]")


class OrderFeedLocators:
    ORDER_NUMBER = (By.XPATH, "//*[contains(@class, 'orderNumber')]")
    TOTAL_COUNTER = (By.XPATH, "//*[contains(@class, 'totalCounter')]")
    TODAY_COUNTER = (By.XPATH, "//*[contains(@class, 'todayCounter')]")
    IN_WORK_ORDER = (By.XPATH, "//*[contains(@class, 'inWork')]")