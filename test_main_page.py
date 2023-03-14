#from selenium.webdriver.common.by import By # Для поиска по селекторам
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):   # тест
    print("\nТест test_guest_can_go_to_login_page..")
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()             # Проверяем ссылку login на main_page
    page.go_to_login_page()                 # Переходим на страницу login_page
    print("\nТест should_be_login_page..")
    #login_page = page.go_to_login_page()    # Работаем с login_page (способ 1)
    login_page = LoginPage(browser, browser.current_url) # # Работаем с login_page (способ 2)
    login_page.should_be_login_page()
