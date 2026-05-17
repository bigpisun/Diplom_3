from selenium.webdriver.common.by import By

class MainPageLocators:
    INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    CONSTRUCTOR_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket')]")
    COUNTER = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]//p[contains(@class, 'counter_counter__num')]")
    ORDER_BUTTON = (By.XPATH, "//main//button[contains(@class, 'button_button_type_primary')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")

class AuthLocators:
    RECOVERY_LINK = (By.XPATH, "//a[@href='/forgot-password']")
    PASSWORD_EYE_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]/*[local-name()='svg'] | //div[contains(@class, 'input__icon')]")
    PASSWORD_INPUT_ACTIVE = (By.XPATH, "//input[@type='text']")

class OrderFeedLocators:
    ORDER_CARD = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]//a")
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'OrderFeed_number')]")

class IngredientModalLocators:
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal_opened')]")
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")