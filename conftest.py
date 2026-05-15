import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import BASE_URL


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    
    if browser_name == "chrome":
        options = Options()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Browser {browser_name} not supported")
    
    driver.get(BASE_URL)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()