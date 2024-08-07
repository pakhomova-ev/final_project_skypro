
import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from configuration.ConfigProvider import ConfigProvider
from page.BoardApi import BoardApi
from page.CardApi import CardApi
from page.ListApi import ListApi
from testdata.DataProvider import DataProvider

@pytest.fixture
def browser():
    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.implicitly_wait(ConfigProvider().get_int("ui", "timeout"))
        browser.maximize_window()

        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture
def api_board(scope="session") -> BoardApi:
    return BoardApi(
        ConfigProvider().get("api", "base_url"),
        DataProvider().get_token(), 
        DataProvider().get_key())

@pytest.fixture
def api_card() -> CardApi:
    return CardApi(
        ConfigProvider().get("api", "base_url"),
        DataProvider().get_token(), 
        DataProvider().get_key())

@pytest.fixture
def api_list() -> ListApi:
    return ListApi(
        ConfigProvider().get("api", "base_url"),
        DataProvider().get_token(), 
        DataProvider().get_key())

@pytest.fixture
def test_data() -> DataProvider:
    return DataProvider()




