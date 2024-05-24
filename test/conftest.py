
import pytest
import allure
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from configuration.ConfigProvider import ConfigProvider
from page.BoardApi import BoardApi
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
def api_client(scope="session") -> BoardApi:
    return BoardApi(
        ConfigProvider().get("api", "base_url"),
        DataProvider().get_token(), 
        DataProvider().get_key())

@pytest.fixture
def test_data() -> DataProvider:
    return DataProvider()

# @pytest.fixture
# def delete_all_boards(scope="session"):
#     if (api_client.get_all_boards_by_org_id(DataProvider().get("org_id"), DataProvider().get_auth_creds) > DataProvider().get("num_max_board")):
#         api_client.delete_all_board_of_org(DataProvider().get("org_id"), DataProvider().get_auth_creds)
    
    

# @pytest.fixture
# def auth_user(scope="session"):


