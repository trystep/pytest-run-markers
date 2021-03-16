import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """PyTest method for adding custom console parameters"""

    parser.addoption("--language", action="store", default='ru', type=str,
                     help="Set language for Browser")


@pytest.fixture(scope="session")
def additional_value(request):
    """Handler for --language parameter"""

    return request.config.getoption("--language")


@pytest.fixture(scope='function')
def browser(request):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': f'{request.config.getoption("language")}'})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
