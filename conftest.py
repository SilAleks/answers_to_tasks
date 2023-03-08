import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: 'es' or 'fr'",
                     choices=("es", "fr", "en"))

@pytest.fixture(scope="function")
def browser(request):
    print("\nStart browser..")
    language = request.config.getoption("language")
    browser = webdriver.Chrome()
    #browser.get(f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    browser.get(f"https://selenium1py.pythonanywhere.com/{language}")
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()
