import allure

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from page.AuthPage import AuthPage
from page.BoardApi import BoardApi
from page.BoardPage import BoardPage
from page.CardPage import CardPage
from page.ListPage import ListPage
from page.MainPage import MainPage
from testdata.DataProvider import DataProvider
from selenium.webdriver.common.by import By
from page.BasePage import BasePage

@allure.epic("UI")
@allure.feature("Доски")
@allure.story("Создать доску")
@allure.severity("allure.severity_level.BLOCKED")
@allure.tag("Positive")
def test_create_board(browser: WebDriver, test_data: DataProvider, api_board: BoardApi):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(test_data.get("email"), test_data.get("password"))

    main_page = MainPage(browser)
    
    name_board = DataProvider().generate_board_name()
    
    main_page.create_new_board(name_board)

    list_boards = api_board.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())

    name_find_after = api_board.find_board_by_name_in_list(list_boards, name_board)
   
    with allure.step("api.Проверяем, что в списке есть созданная доска"):
        assert name_find_after is True

    api_board.delete_all_board_of_org(test_data.get("org_id"), test_data.get_auth_creds())

@allure.epic("UI")
@allure.feature("Доски")
@allure.story("Удалить доску")
@allure.severity("allure.severity_level.NORMAL")
@allure.tag("Positive")
def test_delete_board(browser: WebDriver, test_data: DataProvider, api_board: BoardApi):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(test_data.get("email"), test_data.get("password"))

    board_page = BoardPage(browser)
    main_page = MainPage(browser)
    name_board = test_data.generate_board_name()
    new_board_dict = api_board.create_board(test_data.get_create_creds_with_name(name_board))
    short_url = new_board_dict["shortUrl"]
    short_link = main_page.get_short_link(short_url)

    board_list_before = api_board.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())
    len_board_list_before = len(board_list_before)

    board_page = BoardPage(browser)
    board_page.open_board_page(name_board, short_link)
    board_page.delete_board()
    
    board_list_after = api_board.get_all_boards_by_org_id(test_data.get("org_id"), test_data.get_auth_creds())
    len_board_list_after = len(board_list_after)
    find_board_false = api_board.find_board_by_name_in_list(board_list_after, name_board)

    with allure.step("Проверить, что кол-во досок стало на 1 меньше"):
        assert len_board_list_before - len_board_list_after == 1

    with allure.step("Проверить, что удаленной доски нет в списке досок"):
        assert find_board_false is False

    