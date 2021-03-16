import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """PyTest method for adding custom console parameters"""

    parser.addoption("--language", action="store", default=0, type=int,
                     help="Set additional value for timestamp")


@pytest.fixture(scope="session")
def additional_value(request):
    """Handler for --language parameter"""

    return request.config.getoption("--language")


@pytest.fixture(scope='function')
def browser(language):
    browser = webdriver.Chrome()
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': f'{language}'})
    yield browser
    browser.quit()
