import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=option)
    yield driver
    driver.quit()
