import allure
import time
import re

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

    
def test_add_new_card_x(browser: WebDriver, test_data: DataProvider, api_client: BoardApi):
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
    # board_page.find_lists('6654cccadb15713775b136cf')
    board_page.click_add_a_card()
    board_page.open_card()
    board_page.change_name_card()
    board_page.open_card()
    board_page.add_to_archive_card()
    board_page.delete_card()

    time.sleep(3)

def test_click_textarea(browser: WebDriver, test_data: DataProvider):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(test_data.get("email"), test_data.get("password"))

    main_page = MainPage(browser)
    main_page.find_board_by_name("rtm")
    board_page = BoardPage(browser)
    board_page.open_board_page("rtm", "uF0vIUeg")

    list_page = ListPage(browser)
    name_new_list = test_data.generate_new_list_name()
    list_page.create_new_list(name_new_list)
    browser.refresh()
    id_list = list_page.get_id_list_by_name(name_new_list)

    name_card = test_data.generate_card_name()
    
    card_page = CardPage(browser)
    card_page.create_new_card(id_list, name_card)


def test_drag_drop(browser: WebDriver, test_data: DataProvider):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(test_data.get("email"), test_data.get("password"))

    main_page = MainPage(browser)
    main_page.find_board_by_name("girl")
    board_page = BoardPage(browser)
    board_page.open_board_page("girl", "zVQ7z5hY")

    board_page.move_card_to_another_list()
    time.sleep(3)

def test_find_elenemt(browser: WebDriver, test_data: DataProvider):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(test_data.get("email"), test_data.get("password"))

    main_page = MainPage(browser)
    main_page.find_board_by_name("rtm")
    board_page = BoardPage(browser)
    board_page.open_board_page("rtm", "uF0vIUeg")
    name_list = "DimGray 2946"    
    elements = browser.find_elements(By.CSS_SELECTOR, "ol#board > li")
    id_list = ''
    elements = browser.find_elements(By.CSS_SELECTOR, "ol#board > li")
    for elem in elements:
            text = elem.text
            list = text.splitlines()
            if(list[0] == name_list): 
                id_list = elem.get_attribute('data-list-id')
                break            
    return id_list


def test_create_card_x(browser: WebDriver, test_data: DataProvider):
    auth_page = AuthPage(browser)
    auth_page.go()
    auth_page.login_as(test_data.get("email"), test_data.get("password"))

    main_page = MainPage(browser)
    main_page.find_board_by_name("rtm")
    board_page = BoardPage(browser)
    board_page.open_board_page("rtm", "uF0vIUeg")

    list_page = ListPage(browser)
    name_new_list = test_data.generate_new_list_name()
    new_list = list_page.create_new_list(name_new_list)
    browser.refresh()
    id_list = list_page.get_id_list_by_name(name_new_list)

    name_card = test_data.generate_card_name()

    card_page = CardPage(browser)

    card_page.scroll_to_list(id_list)
    click_card_add = card_page.click_add_a_card(id_list)
    card_page.type_name_card(name_card, id_list)
    card_page.click_add_card_with_text(id_list)
    card_page.click_x_new_card()

    elem_info = list_page.elem_info(id_list)

    y = 67
