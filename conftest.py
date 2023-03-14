import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: 'es' or 'fr'")

@pytest.fixture(scope="function")
def browser(request):
    print("\nStart browser..")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome()
    yield browser
    time.sleep(5)
    print("\nquit browser..")
    browser.quit()
