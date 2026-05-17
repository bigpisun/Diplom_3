from pages.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait

def test_ingredient_counter_increases_on_drag_and_drop(driver):
    page = MainPage(driver)
    page.open_main_page()
    initial_counter = page.get_counter_value()
    
    page.drag_and_drop_ingredient()
    
    # Ждем до 5 секунд, пока счетчик на странице станет больше, чем был изначально
    WebDriverWait(driver, 5).until(
        lambda d: page.get_counter_value() > initial_counter
    )
    
    new_counter = page.get_counter_value()
    assert new_counter > initial_counter