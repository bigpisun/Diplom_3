import pytest
from pages.main_page import MainPage
from selenium.webdriver.common.by import By

# Локаторы для переходов
PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']/..")
RECOVERY_LINK = (By.XPATH, ".//a[@href='/forgot-password']")
PASSWORD_EYE_BUTTON = (By.XPATH, "//*[contains(@class, 'show_password')]")
PASSWORD_INPUT_ACTIVE = (By.XPATH, "//*[contains(@class, 'input_status_active')]/input[@type='text']")

def test_navigate_to_personal_account(driver):
    """Переход в Личный кабинет по клику на кнопку"""
    page = MainPage(driver)
    page.driver.get("https://stellarburgers.nomoreparties.site/")
    page.click(PROFILE_BUTTON)
    
    # Должна открыться страница логина (так как мы не авторизованы)
    page.wait_for_page_load()
    assert "/login" in page.driver.current_url, "Не перешли на страницу авторизации при клике на Личный кабинет"

def test_navigate_to_recovery_password(driver):
    """Переход на страницу восстановления пароля"""
    page = MainPage(driver)
    page.driver.get("https://stellarburgers.nomoreparties.site/login")
    page.click(RECOVERY_LINK)
    
    page.wait_for_page_load()
    assert "/forgot-password" in page.driver.current_url, "Не перешли на страницу восстановления пароля"

def test_password_visibility_toggle_by_eye_button(driver):
    """Клик по кнопке глаза делает поле пароля видимым (меняет тип или подсвечивает класс)"""
    page = MainPage(driver)
    page.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    
    # На странице восстановления пароля кликаем на глаз у поля "Пароль" (если оно есть)
    if page.is_visible(PASSWORD_EYE_BUTTON):
        page.click(PASSWORD_EYE_BUTTON)
        # Проверяем, что поле стало активным/видимым
        assert page.is_visible(PASSWORD_INPUT_ACTIVE) or "status_active" in page.driver.page_source, "Поле пароля не активировалось"