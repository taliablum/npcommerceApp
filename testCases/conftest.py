from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=="chrom":
        driver=webdriver.Chrome()
    elif browser=="edge":
        driver=webdriver.Edge()
    else:
         driver=webdriver.Chrome()

    return driver
 

def pytest_addoption(parser):
    parser.addoption("--browser")

#return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")





