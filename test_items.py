#import pytest
#from selenium import webdriver
#from selenium.webdriver.common.by import By
import time


def test_button(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"      
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector('button.btn')
    assert button is not None, "нет кнопочки"

