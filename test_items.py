import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# How to run
# pytest --language=es test_items.py
# pytest --language=fr test_items.py
@pytest.mark.parametrize('link', [
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/',
])
def test_button_exists(browser, link):
    browser.get(link)
    # time.sleep(30)
    button = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="add_to_basket_form"]/button')))
    assert len(button) > 0
