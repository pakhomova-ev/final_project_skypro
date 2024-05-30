import allure
import time

from selenium.webdriver.chrome.webdriver import WebDriver

from page.AuthPage import AuthPage
from page.BoardApi import BoardApi
from page.BoardPage import BoardPage
from page.CardApi import CardApi
from page.CardPage import CardPage
from page.ListApi import ListApi
from page.ListPage import ListPage
from page.MainPage import MainPage

from testdata.DataProvider import DataProvider
from selenium.webdriver.common.by import By

@allure.story("ui.Создать новую карточку в листе")
def test_create_card(browser: WebDriver, test_data: DataProvider, api_board: BoardApi, api_card: CardApi, api_list:ListApi):
    auth_page = AuthPage(browser)
    main_page = MainPage(browser)
    board_page = BoardPage(browser)
    card_page = CardPage(browser)

    auth_page.auth_user(test_data.get("email"), test_data.get("password"))


    name_board = DataProvider().generate_board_name()
    new_board_dict = api_board.create_board(test_data.get_create_creds_with_name(name_board))
    short_url = new_board_dict.get("shortUrl") # как бы это описать одной строчкой, спрятав все манипуляции 27-28
    short_link = main_page.get_short_link(short_url)
    id_board = new_board_dict.get("id")

    name_new_list = test_data.generate_new_list_name()
    list = api_list.create_new_list(name_new_list, id_board, test_data.get_auth_creds())
    id_list = list.get("id")

    board_page.open_board_page(name_board, short_link)


    name_card = test_data.generate_card_name()
    card_page.create_new_card(id_list, name_card)

    cards_list = api_card.get_cards_of_list(id_list, test_data.get_auth_creds(), test_data.get_json_header())
    
    with allure.step("api.Проверить, что карточка {name_card} существует"):
        assert api_card.find_card_by_name_in_list(cards_list, name_card) is True

    api_board.delete_board_by_id(id_board, test_data.get_auth_creds())

@allure.story("ui.Создать новую карточку")
def test_update_card(browser: WebDriver, test_data: DataProvider, api_board: BoardApi, api_card: CardApi, api_list: ListApi):
    auth_page = AuthPage(browser)
    main_page = MainPage(browser)
    board_page = BoardPage(browser)
    card_page = CardPage(browser)

    auth_page.auth_user(test_data.get("email"), test_data.get("password"))

    name_board = DataProvider().generate_board_name()
    new_board_dict = api_board.create_board(test_data.get_create_creds_with_name(name_board))
    short_url = new_board_dict.get("shortUrl") # как бы это описать одной строчкой, спрятав все манипуляции 27-28
    short_link = main_page.get_short_link(short_url)
    id_board = new_board_dict.get("id")

    

    name_new_list = test_data.generate_new_list_name()
    list = api_list.create_new_list(name_new_list, id_board, test_data.get_auth_creds())
    id_list = list.get("id")

    board_page.open_board_page(name_board, short_link)

    card_new = api_card.create_card(id_list, test_data.get_card_creds(id_list), test_data.get_json_header())
    new_card_name = test_data.generate_card_name()
    
    card_page.scroll_to_list(id_list)
    card_page.update_name_card(card_new.get("name"), new_card_name)

@allure.story("ui.Переместить карточку в другой список")
def test_move_card_another_list(browser: WebDriver, test_data: DataProvider, api_board: BoardApi, api_card: CardApi, api_list: ListApi):
    auth_page = AuthPage(browser)
    main_page = MainPage(browser)
    board_page = BoardPage(browser)
    card_page = CardPage(browser)

    auth_page.auth_user(test_data.get("email"), test_data.get("password"))


    name_board = DataProvider().generate_board_name()
    new_board_dict = api_board.create_board(test_data.get_create_creds_with_name(name_board))
    short_url = new_board_dict.get("shortUrl") # как бы это описать одной строчкой, спрятав все манипуляции 27-28
    short_link = main_page.get_short_link(short_url)
    id_board = new_board_dict.get("id")

    name_new_list = test_data.generate_new_list_name()
    list = api_list.create_new_list(name_new_list, id_board, test_data.get_auth_creds())
    id_list = list.get("id")

    name_new_list = test_data.generate_new_list_name()
    list_2 = api_list.create_new_list(name_new_list, id_board, test_data.get_auth_creds())
    id_new_list = list_2.get("id")

    board_page.open_board_page(name_board, short_link)


    name_card = test_data.generate_card_name()
    card_page.create_new_card(id_list, name_card)
    card_list = api_card.get_cards_of_list(id_list, test_data.get_auth_creds(), test_data.get_json_header())
    id_card = api_card.find_id_card_by_name_in_list(card_list, name_card)
 
    card_page.move_to_another_list(id_card, id_new_list)
  

    




