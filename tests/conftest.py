import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions


@pytest.fixture
def browser_chrome():
    options = ChromeOptions()
    options.headless = True
    wd = webdriver.Chrome(options=options)
    yield wd
    wd.quit()


@pytest.fixture
def browser_ff():
    options = FirefoxOptions()
    options.headless = True
    wd = webdriver.Firefox(options=options)
    yield wd
    wd.quit()

# @pytest.fixture
# def browser_safari():
#     wd = webdriver.Safari()
#     yield wd
#     wd.quit()
