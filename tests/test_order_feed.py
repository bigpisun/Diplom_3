import pytest
from pages.main_page import MainPage
from selenium.webdriver.common.by import By

# Добавим локаторы для ленты прямо в тест, чтобы не ковырять файл locators.py
ORDER_CARD = (By.XPATH, "(//*[contains(@class, 'OrderHistory_link')])[1]") # Первый заказ в ленте
ORDER_MODAL = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]") # Открытое модальное окно заказа
TOTAL_ORDERS_COUNTER = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p") # Счетчик за все время

def test_open_order_modal_details(driver):
    """При клике на заказ открывается всплывающее окно с деталями"""
    page = MainPage(driver)
    page.driver.get("https://stellarburgers.nomoreparties.site/")
    page.click_order_feed() # Переходим в ленту
    
    # Кликаем на первый заказ в ленте и проверяем модалку
    page.click(ORDER_CARD)
    assert page.is_visible(ORDER_MODAL) is True, "Модальное окно с деталями заказа не открылось"

def test_total_orders_counter_exists(driver):
    """Счетчик 'Выполнено за всё время' отображается в ленте"""
    page = MainPage(driver)
    page.driver.get("https://stellarburgers.nomoreparties.site/")
    page.click_order_feed()
    
    # Проверяем, что счетчик заказов виден и содержит цифры
    assert page.is_visible(TOTAL_ORDERS_COUNTER) is True, "Счетчик заказов не отображается"
    counter_value = page.get_text(TOTAL_ORDERS_COUNTER)
    assert counter_value.isdigit(), f"Значение счетчика '{counter_value}' не является числом"