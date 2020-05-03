import pytest
from selenium import webdriver
import time

def test_open_test(browser_chrome):
    browser_chrome.get('http://192.168.99.100/')
    time.sleep(3)
    assert browser_chrome.title == 'Your Store'


def test_open_test(browser_safari):
    browser_safari.get('http://192.168.99.100/')
    time.sleep(3)
    assert browser_safari.title == 'Your Store'