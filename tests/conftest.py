import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import safari


@pytest.fixture
def browser_chrome(request):
    options = ChromeOptions()
    options.add_argument('--start-fullscreen')
    # options.headless = True
    wd = webdriver.Chrome(options=options)
    request.addfinalizer(wd.quit)
    return wd


# @pytest.fixture
# def browser_ff(request):
#     options = FirefoxOptions()
#     options.add_argument('--start-fullscreen')
#     # options.headless = True
#     wd = webdriver.Firefox(options=options)
#     request.addfinalizer(wd.quit)
#     return wd


@pytest.fixture
def browser_safari(request):
    options = safari()
    options.binary_location = "/usr/bin/safaridriver"
    options.add_argument('--start-fullscreen')
    # options.headless = True
    wd = webdriver.safari(options=options)
    request.addfinalizer(wd.quit)
    return wd
