from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def should_be_login_link(self):
        print("\nПроверяем ссылку login на main_page..")
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" # символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
    
    def go_to_login_page(self): # self - для доступа к элементам импортируемого класса 
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK) # через self
        login_link.click()
        # Добавляем обработку alert, если таковой будет на странице
        #alert = self.browser.switch_to.alert
        #alert.accept()
        # Возвращаем занчения для LoginPage (способ 1)
        #return LoginPage(browser=self.browser, url=self.browser.current_url)
    '''
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # Возвращаем занчения для LoginPage (способ 1)
        #return LoginPage(browser=self.browser, url=self.browser.current_url)
    '''