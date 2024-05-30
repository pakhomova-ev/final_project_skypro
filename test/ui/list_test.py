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

@allure.story("ui.Создать новый список на доске")
def test_create_new_list(browser: WebDriver, test_data: DataProvider, api_board: BoardApi, api_list: ListApi):
    board_page = BoardPage(browser)
    auth_page = AuthPage(browser)
    main_page = MainPage(browser)
    list_page = ListPage(browser)

    auth_page.auth_user(test_data.get("email"), test_data.get("password"))

    name_board = DataProvider().generate_board_name()
    new_board_dict = api_board.create_board(test_data.get_create_creds_with_name(name_board))
    short_url = new_board_dict.get("shortUrl") # как бы это описать одной строчкой, спрятав все манипуляции 27-28
    short_link = main_page.get_short_link(short_url)
    id_board = new_board_dict.get("id")

    board_page.open_board_page(name_board, short_link)

    name_new_list = test_data.generate_new_list_name()
    list_page.create_new_list(name_new_list)
    browser.refresh()
    list_lists = api_board.get_list_boards_lists(id_board, test_data.get_auth_creds(), test_data.get_json_header())
    id_list = api_list.get_list_id_by_name(list_lists, name_new_list)
    find_list = api_board.find_x_by_id_in_list(list_lists, id_list)
    
    with allure.step("api.Проверить, что новый список - {name_new_list} есть на доске {name_board}"):
        assert find_list is True

    # with allure.step("ui.Проверить, что новый список - {id_list} есть на доске"):
    #     assert ui_list is True

    api_board.delete_board_by_id(id_board, test_data.get_auth_creds())











    
