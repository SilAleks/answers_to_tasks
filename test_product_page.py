import pytest
from .pages.product_page import ProductPage
import click

@pytest.mark.xfail(reason="\n Bad link ..")
@pytest.mark.parametrize('number', [i for i in range(0,10)])
def test_guest_can_add_product_to_basket(browser, number):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    page = ProductPage(browser, link)
    page.open()
    page.examination_add_to_basket()
    page.compare_name()
    page.compare_price()
    #click.pause("\n Нажмите Enter ..")
