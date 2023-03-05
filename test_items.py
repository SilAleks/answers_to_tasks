from selenium.webdriver.common.by import By # Для поиска по селекторам
import time

def test_btn_add_to_basket(browser):
    time.sleep(30)
    btn_add_to_basket = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert str((type(btn_add_to_basket))) == "<class 'selenium.webdriver.remote.webelement.WebElement'>", "\n Нема кнопки !"
=======
from selenium.webdriver.common.by import By # Для поиска по селекторам
import time

def test_btn_add_to_basket(browser):
    time.sleep(30)
    btn_add_to_basket = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert str((type(btn_add_to_basket))) == "<class 'selenium.webdriver.remote.webelement.WebElement'>", "\n Нема кнопки !"
>>>>>>> 23b2b86d6308ed9227695baf7a22f7b0ee713d3c
