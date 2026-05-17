import pytest
from pages.main_page import MainPage
# Если у тебя локаторы лежат в отдельном файле locators.py, импортируй их. 
# Если они внутри MainPage, то вызывай через MainPage.LOCATOR

def test_click_recovery_password_button(driver):
    page = MainPage(driver)
    # 1. Открываем главную -> переходим на логин -> кликаем "Восстановить пароль"
    # Замени методы на свои актуальные из main_page.py
    page.driver.get("https://stellarburgers.nomoreparties.site/login") 
    # Предположим, у тебя есть локатор для ссылки восстановления:
    # page.click(MainPage.RECOVERY_LINK)
    # assert "forgot-password" in page.driver.current_url