import time


def test_open_chrome(browser_chrome):
    browser_chrome.get('http://localhost/')
    time.sleep(3)
    assert browser_chrome.title == 'Your Store'


def test_open_firefox(browser_ff):
    browser_ff.get('http://localhost/')
    time.sleep(3)
    assert browser_ff.title == 'Your Store'


def test_open_safari(browser_safari):
    browser_safari.get('http://localhost/')
    time.sleep(3)
    assert browser_safari.title == 'Your Store'
