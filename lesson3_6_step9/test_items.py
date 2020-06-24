from typing import Union

from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_should_be_displayed(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    browser.get(link)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button.is_displayed(), "Add to basket button should be displayed"
