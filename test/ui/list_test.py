import allure

from selenium.webdriver.chrome.webdriver import WebDriver

from page.AuthPage import AuthPage
from page.BoardApi import BoardApi
from page.BoardPage import BoardPage
from page.ListApi import ListApi
from page.ListPage import ListPage
from page.MainPage import MainPage
from testdata.DataProvider import DataProvider
from selenium.webdriver.common.by import By
from page.BasePage import BasePage

@allure.epic("UI")
@allure.feature("Списки")
@allure.story("Создать список")
@allure.severity("allure.severity_level.CRITICAL")
@allure.tag("Positive")
def test_create_new_list(browser: WebDriver, test_data: DataProvider, api_board: BoardApi, api_list: ListApi):
    board_page = BoardPage(browser)
    auth_page = AuthPage(browser)
    main_page = MainPage(browser)
    list_page = ListPage(browser)

    auth_page.go()
    auth_page.login_as(test_data.get("email"), test_data.get("password"))

    name_board = DataProvider().generate_board_name()
    new_board_dict = api_board.create_board(name_board, test_data.get_auth_creds())
    short_url = new_board_dict.get("shortUrl") # как бы это описать одной строчкой, спрятав все манипуляции 27-28
    short_link = main_page.get_short_link(short_url)
    id_board = new_board_dict.get("id")

    board_page.open_board_page(name_board, short_link)

    name_new_list = test_data.generate_new_list_name()
    list_page.create_new_list(name_new_list)
    browser.refresh()
    list_lists = api_board.get_list_boards_lists(id_board, test_data.get_auth_creds(), test_data.get_json_header())
    id_list = list_page.get_id_list_by_name(name_new_list)
    find_list = list_page.find_x_in_list(list_lists, id_list)
    
    with allure.step("api.Проверить, что новый список есть на доске"):
        assert find_list is True

    api_board.delete_board_by_id(id_board, test_data.get_auth_creds())











    
