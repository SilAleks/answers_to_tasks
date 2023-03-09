from selenium.webdriver.common.by import By # Для поиска по селекторам
from .pages.main_page import MainPage
#import time

#link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):  # ф-я клика по ссылке логина
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser):   # тест
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    #page.go_to_login_page()
