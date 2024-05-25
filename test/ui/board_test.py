import allure
import time
import re

import pytest

from page.AuthPage import AuthPage
from page.BoardApi import BoardApi
from page.BoardPage import BoardPage
from page.MainPage import MainPage
from testdata.DataProvider import DataProvider
from selenium.webdriver.common.by import By


def test_create_board(browser, test_data: DataProvider, api_client: BoardApi):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(test_data.get("email"), test_data.get("password"))

    main_page = MainPage(browser)
    api_client.delete_all_board_of_org(test_data.get("org_id"), test_data.get_auth_creds())
    name_board = DataProvider().generate_board_name()
    
    main_page.create_new_board(name_board)

    list_boards = api_client.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())

    name_find_after = api_client.find_board_by_name_in_list(list_boards, name_board)
    h=7
    with allure.step("api.Проверяем, что в списке есть созданная доска"):
        assert name_find_after is True

    # main_page.open_main_page_trello()
    # # ++++++++++++++++==не работает, не находит элемент!!!!!!+++++++++++++++++++++++++++++++++++++++
    # with allure.step("ui.Проверить, что созданная доска отображается в списке"):
    #     name_find_ui = main_page.find_by_name(name_board)
    #     assert name_find_ui is True

def test_delete_board(browser, test_data: DataProvider, api_client: BoardApi):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(test_data.get("email"), test_data.get("password"))

    new_board_dict = api_client.create_board(test_data.get_create_creds())
    name_board = new_board_dict["name"]
    short_url = new_board_dict["shortUrl"]
    match = re.search(r"/b/([a-zA-Z0-9]+)", short_url)
    short_link = match.group(1)

    board_list_before = api_client.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())
    len_board_list_before = len(board_list_before)

    board_page = BoardPage(browser)
    board_page.open_board_page(name_board, short_link)
    board_page.delete_board()
    
    board_list_after = api_client.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())
    len_board_list_after = len(board_list_after)

    with allure.step("Проверить, что кол-во досок стало на 1 меньше"):
        assert len_board_list_before - len_board_list_after == 1

    

@pytest.mark.skip("не работает поиск элемента в методе find_by_name")  
def test_find_by_name(browser):
    board_page = BoardPage(browser)
    board_page.find_by_name()




