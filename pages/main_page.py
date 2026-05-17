import time
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators import MainPageLocators, OrderFeedLocators, AuthLocators, IngredientModalLocators

class MainPage(BasePage):
    BASE_URL = "https://stellarburgers.education-services.ru/"

    def open_main_page(self):
        self.driver.get(self.BASE_URL)
        self.wait_for_page_load()

    def open_login_page(self):
        self.driver.get(f"{self.BASE_URL}login")
        self.wait_for_page_load()

    def open_recovery_page(self):
        self.driver.get(f"{self.BASE_URL}forgot-password")
        self.wait_for_page_load()

    def open_feed_page(self):
        self.driver.get(f"{self.BASE_URL}feed")
        self.wait_for_page_load()

    def get_current_url(self):
        return self.driver.current_url

    def close_modal_if_exists(self):
        try:
            close_btn = self.driver.find_elements(*IngredientModalLocators.CLOSE_BUTTON)
            if close_btn and close_btn[0].is_displayed():
                self.driver.execute_script("arguments[0].click();", close_btn[0])
        except:
            pass

    def is_ingredient_present(self):
        try:
            self.wait.until(lambda d: d.find_element(*MainPageLocators.INGREDIENT))
            return True
        except TimeoutException:
            return False

    def drag_and_drop_ingredient(self):
        ingredient = self.wait.until(EC.presence_of_element_located(MainPageLocators.INGREDIENT))
        constructor = self.wait.until(EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_AREA))
        
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ingredient)
        time.sleep(0.5)
        
        html5_drag_drop_script = """
        function createEvent(typeOfEvent) {
            var event = document.createEvent("CustomEvent");
            event.initCustomEvent(typeOfEvent, true, true, null);
            event.dataTransfer = {
                data: {},
                setData: function (key, value) { this.data[key] = value; },
                getData: function (key) { return this.data[key]; }
            };
            return event;
        }
        function dispatchEvent(element, event, transferData) {
            if (transferData !== undefined) { element.dataTransfer = transferData; }
            if (element.dispatchEvent) { element.dispatchEvent(event); }
            else if (element.fireEvent) { element.fireEvent("on" + event.type, event); }
        }
        function dragAndDrop(elementFirst, elementSecond) {
            var dragStartEvent = createEvent('dragstart');
            dispatchEvent(elementFirst, dragStartEvent);
            var dragOverEvent = createEvent('dragover');
            dispatchEvent(elementSecond, dragOverEvent, dragStartEvent.dataTransfer);
            var dropEvent = createEvent('drop');
            dispatchEvent(elementSecond, dropEvent, dragStartEvent.dataTransfer);
            var dragEndEvent = createEvent('dragend');
            dispatchEvent(elementFirst, dragEndEvent);
        }
        dragAndDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(html5_drag_drop_script, ingredient, constructor)
        time.sleep(0.5)

    def click_constructor(self):
        self.close_modal_if_exists()
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        self.close_modal_if_exists()
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    def click_profile_button(self):
        self.click(MainPageLocators.PROFILE_BUTTON)

    def click_recovery_link(self):
        self.click(AuthLocators.RECOVERY_LINK)

    def click_password_eye(self):
        eye = self.wait.until(EC.presence_of_element_located(AuthLocators.PASSWORD_EYE_BUTTON))
        self.driver.execute_script("arguments[0].click();", eye)
        time.sleep(0.5)

    def get_counter_value(self):
        elements = self.driver.find_elements(*MainPageLocators.COUNTER)
        if not elements:
            return 0
        text = elements[0].text
        return int(text) if text.isdigit() else 0

    def click_order_button(self):
        self.close_modal_if_exists()
        buttons = self.driver.find_elements(*MainPageLocators.ORDER_BUTTON)
        if buttons:
            self.driver.execute_script("arguments[0].click();", buttons[0])
        else:
            btn = self.wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON))
            self.driver.execute_script("arguments[0].click();", btn)

    def is_modal_visible(self):
        return self.is_visible(IngredientModalLocators.MODAL)

    def close_modal(self):
        self.click(IngredientModalLocators.CLOSE_BUTTON)

    def click_first_order(self):
        # Ожидаем появление карточек заказов в ленте
        card = self.wait.until(EC.element_to_be_clickable(OrderFeedLocators.ORDER_CARD))
        time.sleep(1) # Даем списку обновиться и стабилизироваться
        
        for _ in range(3):
            try:
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
                time.sleep(0.2)
                card.click() # Кликаем стандартным методом Селениума
                time.sleep(1) # Ждем открытия окна
                return
            except (StaleElementReferenceException, TimeoutException):
                # Если элемент устарел, находим его заново
                card = self.wait.until(EC.element_to_be_clickable(OrderFeedLocators.ORDER_CARD))
                continue

    def is_order_modal_visible(self):
        # Метод возвращает True, если открылся URL конкретного заказа ИЛИ на экране есть окно модалки
        current_url = self.driver.current_url
        if "/feed/" in current_url:
            return True
            
        try:
            modal = self.driver.find_elements(*IngredientModalLocators.MODAL)
            if modal and modal[0].is_displayed():
                return True
        except:
            pass
            
        return False

    def get_total_orders_value(self):
        self.wait.until(lambda d: d.find_element(*OrderFeedLocators.TOTAL_ORDERS_COUNTER).text.strip() != "")
        text = self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER)
        return int(text) if text.strip().isdigit() else 0

    def get_today_orders_value(self):
        self.wait.until(lambda d: d.find_element(*OrderFeedLocators.TODAY_ORDERS_COUNTER).text.strip() != "")
        text = self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER)
        return int(text) if text.strip().isdigit() else 0

    def is_active_password_input_visible(self):
        try:
            self.wait.until(EC.presence_of_element_located(AuthLocators.PASSWORD_INPUT_ACTIVE))
            return True
        except:
            return False