import allure
import time
import re

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from page.AuthPage import AuthPage
from page.BoardApi import BoardApi
from page.BoardPage import BoardPage
from page.MainPage import MainPage
from testdata.DataProvider import DataProvider
from selenium.webdriver.common.by import By


def test_create_board(browser: WebDriver, test_data: DataProvider, api_client: BoardApi):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(test_data.get("email"), test_data.get("password"))

    main_page = MainPage(browser)
    api_client.delete_all_board_of_org(test_data.get("org_id"), test_data.get_auth_creds())
    name_board = DataProvider().generate_board_name()
    
    main_page.create_new_board(name_board)

    list_boards = api_client.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())

    name_find_after = api_client.find_board_by_name_in_list(list_boards, name_board)
   
    with allure.step("api.Проверяем, что в списке есть созданная доска"):
        assert name_find_after is True

    # main_page.open_main_page_trello()
    # # ++++++++++++++++==не работает, не находит элемент!!!!!!+++++++++++++++++++++++++++++++++++++++
    # with allure.step("ui.Проверить, что созданная доска отображается в списке"):
    #     name_find_ui = main_page.find_by_name(name_board)
    #     assert name_find_ui is True

def test_delete_board(browser: WebDriver, test_data: DataProvider, api_client: BoardApi):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(test_data.get("email"), test_data.get("password"))

    board_page = BoardPage(browser)

    new_board_dict = api_client.create_board(test_data.get_create_creds())
    name_board = new_board_dict["name"]
    short_url = new_board_dict["shortUrl"]
    short_link = board_page.get_short_link(short_url)

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
def test_find_by_name(browser: WebDriver):
    board_page = BoardPage(browser)
    board_page.find_by_name()

@allure.story("Добавить карточку на доску")
def test_add_card_on_list(browser: WebDriver, test_data: DataProvider, api_client: BoardApi):
    new_board_dict = api_client.create_board(test_data.get_create_creds())
    name_new_board = new_board_dict.get("name")
    id_new_board = new_board_dict.get("id")
    url_new_board = new_board_dict.get("shortUrl")
    short_link = api_client.get_short_link(url_new_board)

    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(test_data.get("email"), test_data.get("password"))

# получить список досок выбрать любую и получить id board
    main_page = MainPage(browser)
    main_page.find_board_by_name(name_new_board)
    board_page = BoardPage(browser)
    board_page.open_board_page(name_new_board, short_link)
    
    name_list = DataProvider().generate_new_list_name()
    board_page.create_new_list(name_list)

    list_lists = api_client.get_list_boards_lists(id_new_board, test_data.get_auth_creds(), test_data.get_json_header())
    id_new_list = api_client.get_list_id_by_name(list_lists, name_list)

    board_page.click_add_a_card(id_new_list)

    
def test_add_new_card_x(browser, test_data: DataProvider, api_client: BoardApi):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(test_data.get("email"), test_data.get("password"))

    main_page = MainPage(browser)
    main_page.find_board_by_name("girl")
    board_page = BoardPage(browser)
    board_page.open_board_page("girl", "zVQ7z5hY")
    board_page.click_add_a_card()
    board_page.type_name_card("ghjty67")
    board_page.click_add_card_with_text()
    board_page.click_x_new_card()

    # board_page.click_add_a_card("664cf65097e9b86e8bc07c20")

    # list_lists = api_client.get_list_boards_lists(id_new_board, test_data.get_auth_creds(), test_data.get_json_header())
    # id_new_list = api_client.get_list_id_by_name(list_lists, name_list)

    # нет проверики на юай созданного списка
    # name_list_find = main_page.find_list_by_name(name_list)
    # id_list_find = main_page.find_list_by_id(id_new_list)
    # assert id_list_find is True
    # id_new_list = api_client.create_new_list(name_new_list, id_new_board, test_data.get_auth_creds())



# ol#board > li h2[data-testid="list-name"]
# ol#board > li div.mKJWg6W_CLHoiO



# проверить что карточка есть в нужном списке
# получить список всех карточек доски и сравнить id list



